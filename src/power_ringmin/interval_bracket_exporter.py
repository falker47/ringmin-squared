"""Generate verifier-consumable fixed-order interval bracket records.

This module is a generator/exporter for the local record consumed by
``power_ringmin.interval_verifier``.  It uses high-precision numerical
computation only to propose a lower negative cycle and an upper witness; the
local interval verifier is then run before a record is returned or written.
"""

from __future__ import annotations

import argparse
import copy
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import shlex
import sys
from typing import Any

import mpmath as mp

from power_ringmin.fixed_order_artifact import UPSTREAM_RINGMIN_COMMIT, detect_repository_state
from power_ringmin.highprec import full_radius_mp, theta_mp
from power_ringmin.interval_verifier import (
    FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION,
    MPMathIntervalAngularOracle,
    assert_fixed_order_interval_bracket_verified,
    verify_fixed_order_interval_bracket,
)
from power_ringmin.search_small_n import canonicalize_index_order, index_order_to_radius_order

ARTIFACT_TYPE = "fixed_order_interval_bracket"
DEFAULT_EXPORT_DIGITS = 100
DEFAULT_RADIUS_ETA_DECIMAL = "1e-4"
DEFAULT_ETA_GROWTH_DECIMAL = "10"
DEFAULT_MAX_ATTEMPTS = 8
DEFAULT_INITIAL_WITNESS_PADDING_DECIMAL = "0.01"
COMMAND_NAME = "power-ringmin-export-fixed-order-interval-bracket"


@dataclass(frozen=True)
class FixedOrderIntervalBracketExport:
    """One verified local interval bracket export."""

    record: dict[str, Any]

    @property
    def index_order(self) -> tuple[int, ...]:
        return tuple(int(value) for value in self.record["index_order"])

    @property
    def radius_order(self) -> tuple[int, ...]:
        return tuple(int(value) for value in self.record["radius_order"])

    @property
    def lower_radius_decimal(self) -> str:
        return str(self.record["lower_radius_decimal"])

    @property
    def upper_radius_decimal(self) -> str:
        return str(self.record["upper_radius_decimal"])

    def to_dict(self) -> dict[str, Any]:
        """Return a deep copy suitable for JSON serialization."""
        return copy.deepcopy(self.record)


@dataclass(frozen=True)
class _STNEdge:
    source: int
    target: int
    edge_kind: str
    weight: mp.mpf


def build_fixed_order_interval_bracket_record(
    index_order: Sequence[int],
    *,
    digits: int = DEFAULT_EXPORT_DIGITS,
    guard_decimal: str | None = None,
    radius_eta: str = DEFAULT_RADIUS_ETA_DECIMAL,
    eta_growth: str = DEFAULT_ETA_GROWTH_DECIMAL,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    created_at_utc: str | None = None,
    argv_for_provenance: Sequence[str] | None = None,
    output: Path | None = None,
) -> dict[str, Any]:
    """Build and verify one fixed-order interval bracket record.

    The input order must already be canonical under the project convention used
    by ``search_small_n.canonical_index_orders``.  The returned record is
    accepted by ``assert_fixed_order_interval_bracket_verified`` with the
    recorded interval backend.
    """
    _validate_digits(digits)
    if isinstance(max_attempts, bool) or max_attempts < 1:
        raise ValueError(f"max_attempts must be a positive integer, got {max_attempts!r}")

    normalized_index_order = _normalize_canonical_index_order(index_order)
    radius_order = index_order_to_radius_order(normalized_index_order)
    oracle = MPMathIntervalAngularOracle(digits=digits, guard_decimal=guard_decimal)
    eta = _positive_decimal_mpf(radius_eta, "radius_eta")
    growth = _positive_decimal_mpf(eta_growth, "eta_growth")
    if growth <= 1:
        raise ValueError("eta_growth must be greater than 1")

    with mp.workdps(digits):
        radius = full_radius_mp(radius_order, digits=digits)

    last_messages: tuple[str, ...] = ()
    last_error: str | None = None
    for attempt in range(1, max_attempts + 1):
        with mp.workdps(digits):
            lower = _lower_radius_candidate(radius, eta)
            upper = radius + eta
            try:
                cycle = _find_negative_cycle(radius_order, lower, digits=digits)
                positions = _strict_witness_positions(radius_order, upper, digits=digits)
            except ValueError as exc:
                last_error = str(exc)
                eta *= growth
                continue

        record = _base_record(
            index_order=normalized_index_order,
            radius_order=radius_order,
            lower_radius=lower,
            upper_radius=upper,
            approximate_radius=radius,
            cycle=cycle,
            positions=positions,
            oracle=oracle,
            digits=digits,
            radius_eta=eta,
            attempt=attempt,
            created_at_utc=created_at_utc,
            argv_for_provenance=argv_for_provenance,
            output=output,
        )
        preliminary = verify_fixed_order_interval_bracket(record, oracle=oracle)
        record["lower_negative_cycle_sum_upper"] = _negative_report_decimal(
            preliminary.lower_negative_cycle_sum_upper,
            digits=digits,
        )
        record["min_upper_witness_slack_lower"] = _nonnegative_report_decimal(
            preliminary.min_upper_witness_slack_lower,
            digits=digits,
        )
        result = verify_fixed_order_interval_bracket(record, oracle=oracle)
        if result.verified:
            record["generator"]["verified"] = True
            record["generator"]["verification_summary"] = {
                "lower_negative_cycle_sum_upper_decimal": _decimal_string(
                    result.lower_negative_cycle_sum_upper,
                    digits=digits,
                ),
                "min_upper_witness_slack_lower_decimal": _decimal_string(
                    result.min_upper_witness_slack_lower,
                    digits=digits,
                ),
            }
            return record
        last_messages = result.messages
        eta *= growth

    details = "; ".join(last_messages) if last_messages else last_error or "no verifier result"
    raise ValueError(
        "could not generate a verified fixed-order interval bracket after "
        f"{max_attempts} attempt(s): {details}"
    )


def export_fixed_order_interval_bracket_record(
    index_order: Sequence[int],
    output: str | Path,
    *,
    digits: int = DEFAULT_EXPORT_DIGITS,
    guard_decimal: str | None = None,
    radius_eta: str = DEFAULT_RADIUS_ETA_DECIMAL,
    eta_growth: str = DEFAULT_ETA_GROWTH_DECIMAL,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    created_at_utc: str | None = None,
    argv_for_provenance: Sequence[str] | None = None,
) -> FixedOrderIntervalBracketExport:
    """Generate, verify, and write one fixed-order interval bracket record."""
    output_path = Path(output)
    record = build_fixed_order_interval_bracket_record(
        index_order,
        digits=digits,
        guard_decimal=guard_decimal,
        radius_eta=radius_eta,
        eta_growth=eta_growth,
        max_attempts=max_attempts,
        created_at_utc=created_at_utc,
        argv_for_provenance=argv_for_provenance,
        output=output_path,
    )
    dump_fixed_order_interval_bracket_record(record, output_path)
    return FixedOrderIntervalBracketExport(record)


def dump_fixed_order_interval_bracket_record(
    record: Mapping[str, Any] | FixedOrderIntervalBracketExport,
    path: str | Path,
    *,
    indent: int = 2,
) -> None:
    """Verify and write one interval bracket record as UTF-8 JSON."""
    Path(path).write_text(
        dumps_fixed_order_interval_bracket_record(record, indent=indent),
        encoding="utf-8",
    )


def dumps_fixed_order_interval_bracket_record(
    record: Mapping[str, Any] | FixedOrderIntervalBracketExport,
    *,
    indent: int = 2,
) -> str:
    """Verify and serialize one interval bracket record."""
    data = (
        record.to_dict()
        if isinstance(record, FixedOrderIntervalBracketExport)
        else copy.deepcopy(dict(record))
    )
    assert_fixed_order_interval_bracket_verified(data, oracle=_oracle_from_record(data))
    return json.dumps(data, indent=indent, sort_keys=False) + "\n"


def load_fixed_order_interval_bracket_record(path: str | Path) -> FixedOrderIntervalBracketExport:
    """Load and verify one fixed-order interval bracket record."""
    return loads_fixed_order_interval_bracket_record(Path(path).read_text(encoding="utf-8"))


def loads_fixed_order_interval_bracket_record(text: str) -> FixedOrderIntervalBracketExport:
    """Parse and verify one fixed-order interval bracket record."""
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("fixed-order interval bracket JSON must contain an object")
    assert_fixed_order_interval_bracket_verified(payload, oracle=_oracle_from_record(payload))
    return FixedOrderIntervalBracketExport(copy.deepcopy(payload))


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the interval bracket exporter."""
    parser = argparse.ArgumentParser(
        description="Export one verifier-consumable fixed-order interval bracket record.",
    )
    parser.add_argument(
        "--index-order",
        required=True,
        help="comma-separated canonical quadratic index order, e.g. 3,1,2",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="path to write the fixed-order interval bracket JSON record",
    )
    parser.add_argument(
        "--digits",
        type=int,
        default=DEFAULT_EXPORT_DIGITS,
        help=f"mpmath working precision digits (default: {DEFAULT_EXPORT_DIGITS})",
    )
    parser.add_argument(
        "--guard-decimal",
        help="optional nonnegative guard added to interval endpoints",
    )
    parser.add_argument(
        "--radius-eta",
        default=DEFAULT_RADIUS_ETA_DECIMAL,
        help=f"initial positive radius bracket offset (default: {DEFAULT_RADIUS_ETA_DECIMAL})",
    )
    parser.add_argument(
        "--eta-growth",
        default=DEFAULT_ETA_GROWTH_DECIMAL,
        help=f"factor used to widen the bracket after failed attempts (default: {DEFAULT_ETA_GROWTH_DECIMAL})",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=DEFAULT_MAX_ATTEMPTS,
        help=f"maximum bracket-widening attempts (default: {DEFAULT_MAX_ATTEMPTS})",
    )
    parser.add_argument(
        "--created-at-utc",
        help="optional UTC timestamp to record in artifact provenance",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the fixed-order interval bracket exporter CLI."""
    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)

    try:
        index_order = _parse_index_order_csv(args.index_order)
        export = export_fixed_order_interval_bracket_record(
            index_order,
            args.output,
            digits=args.digits,
            guard_decimal=args.guard_decimal,
            radius_eta=args.radius_eta,
            eta_growth=args.eta_growth,
            max_attempts=args.max_attempts,
            created_at_utc=args.created_at_utc,
            argv_for_provenance=raw_argv,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(
        f"wrote {args.output} n={len(export.index_order)} "
        f"bracket=[{export.lower_radius_decimal}, {export.upper_radius_decimal}]"
    )
    return 0


def _base_record(
    *,
    index_order: tuple[int, ...],
    radius_order: tuple[int, ...],
    lower_radius: mp.mpf,
    upper_radius: mp.mpf,
    approximate_radius: mp.mpf,
    cycle: Sequence[_STNEdge],
    positions: Sequence[mp.mpf],
    oracle: MPMathIntervalAngularOracle,
    digits: int,
    radius_eta: mp.mpf,
    attempt: int,
    created_at_utc: str | None,
    argv_for_provenance: Sequence[str] | None,
    output: Path | None,
) -> dict[str, Any]:
    return {
        "schema_version": FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION,
        "artifact_type": ARTIFACT_TYPE,
        "index_order": list(index_order),
        "radius_order": list(radius_order),
        "lower_radius_decimal": _decimal_string(lower_radius, digits=digits),
        "upper_radius_decimal": _decimal_string(upper_radius, digits=digits),
        "lower_certificate": {
            "kind": "negative_cycle",
            "cycle": [
                {
                    "source": edge.source,
                    "target": edge.target,
                    "edge_kind": edge.edge_kind,
                }
                for edge in cycle
            ],
        },
        "upper_certificate": {
            "kind": "witness_positions",
            "positions_rad": _position_decimals(positions, digits=digits),
        },
        "theta_interval_backend": oracle.backend_info.to_record(),
        "min_upper_witness_slack_lower": "0",
        "lower_negative_cycle_sum_upper": "-1e-999999",
        "generator": {
            "backend": "mpmath_highprec_proposal_with_interval_verifier_acceptance",
            "digits": digits,
            "radius_eta_decimal": _decimal_string(radius_eta, digits=digits),
            "attempt": attempt,
            "approximate_fixed_order_radius_decimal": _decimal_string(
                approximate_radius,
                digits=digits,
            ),
            "verified": False,
            "claim_scope": "local_fixed_order_interval_bracket",
        },
        "provenance": _provenance_record(
            created_at_utc=created_at_utc,
            argv=argv_for_provenance,
            output=output,
            n=len(index_order),
            digits=digits,
        ),
        "evidence": {
            "classification": "computer_certified_result",
            "claim": {
                "scope": "local_fixed_order_interval_bracket",
                "statement": (
                    "The local interval verifier accepted this fixed-order "
                    "lower infeasibility and upper feasibility bracket. This "
                    "is not a global small-n certificate."
                ),
            },
            "limitations": [
                "Finite fixed-order record only.",
                "No global cyclic-order optimality claim.",
                "No theorem for all n.",
                "Interval backend provenance remains a future production review item.",
            ],
        },
    }


def _find_negative_cycle(
    radius_order: Sequence[int],
    R: mp.mpf,
    *,
    digits: int,
) -> tuple[_STNEdge, ...]:
    radii = tuple(mp.mpf(radius) for radius in radius_order)
    with mp.workdps(digits):
        edges = _stn_edges(radii, mp.mpf(R))
        n = len(radii)
        distances = [mp.mpf("0") for _ in range(n)]
        predecessor: list[_STNEdge | None] = [None for _ in range(n)]
        updated_vertex: int | None = None
        for _ in range(n):
            updated_vertex = None
            for edge in edges:
                candidate = distances[edge.source] + edge.weight
                if candidate < distances[edge.target]:
                    distances[edge.target] = candidate
                    predecessor[edge.target] = edge
                    updated_vertex = edge.target
        if updated_vertex is None:
            raise ValueError("lower endpoint did not produce a negative cycle")

        vertex = updated_vertex
        for _ in range(n):
            edge = predecessor[vertex]
            if edge is None:  # pragma: no cover - defensive Bellman-Ford invariant
                raise ValueError("negative-cycle predecessor chain is incomplete")
            vertex = edge.source

        start = vertex
        reversed_edges: list[_STNEdge] = []
        seen: set[int] = set()
        current = start
        while True:
            if current in seen:
                raise ValueError("negative-cycle predecessor chain repeated before closing")
            seen.add(current)
            edge = predecessor[current]
            if edge is None:  # pragma: no cover - defensive Bellman-Ford invariant
                raise ValueError("negative-cycle predecessor chain is incomplete")
            reversed_edges.append(edge)
            current = edge.source
            if current == start:
                break
            if len(reversed_edges) > n:
                raise ValueError("negative-cycle extraction exceeded node count")

        cycle = tuple(reversed(reversed_edges))
        _assert_connected_cycle(cycle)
        cycle_sum = mp.fsum(edge.weight for edge in cycle)
        if cycle_sum >= 0:
            raise ValueError(
                "extracted cycle is not strictly negative: "
                f"{mp.nstr(cycle_sum, min(digits, 40))}"
            )
        return cycle


def _stn_edges(radii: Sequence[mp.mpf], R: mp.mpf) -> tuple[_STNEdge, ...]:
    tau = 2 * mp.pi
    edges: list[_STNEdge] = []
    for i in range(len(radii)):
        for j in range(i + 1, len(radii)):
            sep = theta_mp(R, radii[i], radii[j])
            edges.append(_STNEdge(source=j, target=i, edge_kind="forward_lower", weight=-sep))
            edges.append(_STNEdge(source=i, target=j, edge_kind="wrap_upper", weight=tau - sep))
    return tuple(edges)


def _strict_witness_positions(
    radius_order: Sequence[int],
    R: mp.mpf,
    *,
    digits: int,
) -> tuple[mp.mpf, ...]:
    radii = tuple(mp.mpf(radius) for radius in radius_order)
    padding = mp.mpf(DEFAULT_INITIAL_WITNESS_PADDING_DECIMAL)
    min_padding = mp.mpf(10) ** (-max(20, digits - 20))
    with mp.workdps(digits):
        while padding >= min_padding:
            positions = _recover_positions_with_padding(radii, mp.mpf(R), padding)
            if positions is not None:
                return positions
            padding /= 2
    raise ValueError("upper endpoint did not admit a strict witness with positive padding")


def _recover_positions_with_padding(
    radii: Sequence[mp.mpf],
    R: mp.mpf,
    padding: mp.mpf,
) -> tuple[mp.mpf, ...] | None:
    dist = _closed_stn_distances_with_padding(radii, R, padding)
    n = len(radii)
    if any(dist[i][i] < 0 for i in range(n)):
        return None
    positions = [dist[0][i] for i in range(n)]
    positions[0] = mp.mpf("0")
    return tuple(positions)


def _closed_stn_distances_with_padding(
    radii: Sequence[mp.mpf],
    R: mp.mpf,
    padding: mp.mpf,
) -> list[list[mp.mpf]]:
    tau = 2 * mp.pi
    n = len(radii)
    dist = [[mp.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = mp.mpf("0")
    for i in range(n):
        for j in range(i + 1, n):
            sep = theta_mp(R, radii[i], radii[j]) + padding
            upper = tau - sep
            if upper < sep:
                dist[0][0] = -mp.mpf("1")
                return dist
            dist[i][j] = min(dist[i][j], upper)
            dist[j][i] = min(dist[j][i], -sep)
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == mp.inf:
                continue
            for j in range(n):
                candidate = dik + dist[k][j]
                if candidate < dist[i][j]:
                    dist[i][j] = candidate
    return dist


def _normalize_canonical_index_order(order: Sequence[int]) -> tuple[int, ...]:
    if isinstance(order, (str, bytes)):
        raise ValueError("index_order must be a sequence of integers, not a string")
    indices = tuple(_parse_positive_int(value, "index_order") for value in order)
    if len(indices) < 3:
        raise ValueError("index_order must contain at least three indices")
    expected = tuple(range(1, len(indices) + 1))
    if tuple(sorted(indices)) != expected:
        raise ValueError(f"index_order must be a permutation of 1..{len(indices)}")
    if canonicalize_index_order(indices) != indices:
        raise ValueError("index_order must be canonical modulo rotation and reflection")
    return indices


def _parse_index_order_csv(text: str) -> tuple[int, ...]:
    parts = tuple(part.strip() for part in text.split(","))
    if not parts or any(not part for part in parts):
        raise ValueError("index-order must be a non-empty comma-separated list")
    return _normalize_canonical_index_order(
        tuple(_parse_positive_int(part, "index-order") for part in parts)
    )


def _parse_positive_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} values must be positive integers")
    if isinstance(value, int):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = int(value, 10)
        except ValueError as exc:
            raise ValueError(f"{name} value must be a positive integer: {value!r}") from exc
        if str(parsed) != value:
            raise ValueError(f"{name} value must be a positive integer: {value!r}")
    else:
        raise ValueError(f"{name} value must be a positive integer: {value!r}")
    if parsed <= 0:
        raise ValueError(f"{name} values must be positive integers")
    return parsed


def _oracle_from_record(record: Mapping[str, Any]) -> MPMathIntervalAngularOracle:
    metadata = record.get("theta_interval_backend")
    if not isinstance(metadata, Mapping):
        raise ValueError("theta_interval_backend must be a mapping")
    if metadata.get("backend") != "mpmath_iv_guarded_atan2_v1":
        raise ValueError("only mpmath_iv_guarded_atan2_v1 records can be loaded here")
    digits = metadata.get("precision_digits")
    _validate_digits(digits)
    guard = metadata.get("guard_decimal")
    if guard is not None and not isinstance(guard, str):
        raise ValueError("theta_interval_backend.guard_decimal must be a string")
    return MPMathIntervalAngularOracle(digits=int(digits), guard_decimal=guard)


def _assert_connected_cycle(cycle: Sequence[_STNEdge]) -> None:
    if not cycle:
        raise ValueError("negative cycle must contain at least one edge")
    for current, nxt in zip(cycle, (*cycle[1:], cycle[0]), strict=True):
        if current.target != nxt.source:
            raise ValueError("negative-cycle extraction produced disconnected edges")


def _lower_radius_candidate(radius: mp.mpf, eta: mp.mpf) -> mp.mpf:
    if radius > eta:
        return radius - eta
    return radius / 2


def _position_decimals(positions: Sequence[mp.mpf], *, digits: int) -> list[str]:
    decimals = [_decimal_string(position, digits=digits) for position in positions]
    decimals[0] = "0.0"
    return decimals


def _negative_report_decimal(value: mp.mpf, *, digits: int) -> str:
    if value >= 0:
        return "-1e-999999"
    return _decimal_string(value / 2, digits=digits)


def _nonnegative_report_decimal(value: mp.mpf, *, digits: int) -> str:
    if value <= 0:
        return "0"
    return _decimal_string(value / 2, digits=digits)


def _positive_decimal_mpf(value: Any, name: str) -> mp.mpf:
    parsed = mp.mpf(str(value))
    if not mp.isfinite(parsed) or parsed <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return parsed


def _decimal_string(value: Any, *, digits: int) -> str:
    text = mp.nstr(mp.mpf(value), n=digits)
    if text.startswith("+"):
        text = text[1:]
    return text


def _validate_digits(value: Any) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 30:
        raise ValueError(f"digits must be an integer at least 30, got {value!r}")


def _provenance_record(
    *,
    created_at_utc: str | None,
    argv: Sequence[str] | None,
    output: Path | None,
    n: int,
    digits: int,
) -> dict[str, Any]:
    return {
        "created_at_utc": created_at_utc or _created_at_utc_now(),
        "repository": detect_repository_state(),
        "software": [
            {
                "name": "Python",
                "version": platform.python_version(),
                "role": "runtime",
            },
            {
                "name": "mpmath",
                "version": getattr(mp, "__version__", "unknown"),
                "role": "high-precision and interval arithmetic",
            },
            {
                "name": "power-ringmin",
                "version": "0.1.0",
                "role": "fixed-order interval bracket exporter",
            },
        ],
        "source_files": [
            {
                "path": "src/power_ringmin/interval_bracket_exporter.py",
                "role": "fixed-order interval bracket generator/exporter",
            },
            {
                "path": "src/power_ringmin/interval_verifier.py",
                "role": "local fixed-order interval bracket verifier",
            },
            {
                "path": "src/power_ringmin/highprec.py",
                "role": "high-precision fixed-order STN proposal",
                "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
            },
        ],
        "commands": [_command_record(argv, output=output, n=n, digits=digits)],
        "randomness": {
            "used": False,
            "seeds": [],
        },
    }


def _command_record(
    argv: Sequence[str] | None,
    *,
    output: Path | None,
    n: int,
    digits: int,
) -> dict[str, str]:
    if argv:
        command = COMMAND_NAME
        command += " " + shlex.join(str(item) for item in argv)
        summary_verb = "Exported"
    else:
        command = "programmatic call: build_fixed_order_interval_bracket_record"
        summary_verb = "Built"
    return {
        "command": command,
        "cwd": str(Path.cwd()),
        "result": "pass",
        "output_summary": (
            f"{summary_verb} one n={n} fixed-order interval bracket record "
            f"at {digits} digits"
            + (f" to {output}" if output is not None else "")
            + "."
        ),
    }


def _created_at_utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


__all__ = [
    "ARTIFACT_TYPE",
    "COMMAND_NAME",
    "DEFAULT_EXPORT_DIGITS",
    "DEFAULT_RADIUS_ETA_DECIMAL",
    "FixedOrderIntervalBracketExport",
    "build_fixed_order_interval_bracket_record",
    "dump_fixed_order_interval_bracket_record",
    "dumps_fixed_order_interval_bracket_record",
    "export_fixed_order_interval_bracket_record",
    "load_fixed_order_interval_bracket_record",
    "loads_fixed_order_interval_bracket_record",
    "main",
]


if __name__ == "__main__":
    raise SystemExit(main())
