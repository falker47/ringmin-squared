"""Local fixed-order interval bracket verification semantics.

This module implements the fixed-order endpoint checks described in
``ops/TASK-20260711__interval_verifier_semantics/DESIGN.md``.  It verifies one
local bracket only; it does not aggregate a global small-n certificate.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import re
from typing import Any, Literal, Protocol

import mpmath as mp

from power_ringmin.search_small_n import canonicalize_index_order, index_order_to_radius_order

FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION = "power-ringmin.fixed_order_interval_bracket.v1"
EDGE_KINDS = frozenset({"forward_lower", "wrap_upper"})
DEFAULT_INTERVAL_DIGITS = 100

DecimalString = str
EdgeKind = Literal["forward_lower", "wrap_upper"]

DECIMAL_STRING_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?$")


@dataclass(frozen=True)
class DecimalInterval:
    """Closed decimal interval represented by high-precision endpoints."""

    lower: mp.mpf
    upper: mp.mpf

    def __post_init__(self) -> None:
        lower = mp.mpf(self.lower)
        upper = mp.mpf(self.upper)
        if not (mp.isfinite(lower) and mp.isfinite(upper)):
            raise ValueError("interval endpoints must be finite")
        if lower > upper:
            raise ValueError(f"interval lower endpoint exceeds upper endpoint: {lower!r} > {upper!r}")
        object.__setattr__(self, "lower", lower)
        object.__setattr__(self, "upper", upper)


@dataclass(frozen=True)
class IntervalBackendInfo:
    """Metadata required from an angular interval backend."""

    backend: str
    precision_digits: int
    rounding_policy: str
    outward_enclosure: bool
    certification_capable: bool
    tolerance_based: bool
    guard_decimal: str | None = None

    def to_record(self) -> dict[str, Any]:
        """Return JSON-compatible interval semantics metadata."""
        record: dict[str, Any] = {
            "backend": self.backend,
            "precision_digits": self.precision_digits,
            "rounding_policy": self.rounding_policy,
            "outward_enclosure": self.outward_enclosure,
            "certification_capable": self.certification_capable,
            "tolerance_based": self.tolerance_based,
        }
        if self.guard_decimal is not None:
            record["guard_decimal"] = self.guard_decimal
        return record


class AngularIntervalOracle(Protocol):
    """Protocol for certified angular interval oracles."""

    @property
    def backend_info(self) -> IntervalBackendInfo:
        """Return backend metadata."""

    def theta(self, R: mp.mpf, a: mp.mpf, b: mp.mpf) -> DecimalInterval:
        """Return an interval enclosing ``theta_R(a,b)``."""

    def tau(self) -> DecimalInterval:
        """Return an interval enclosing ``2*pi``."""


@dataclass(frozen=True)
class MPMathIntervalAngularOracle:
    """Guarded ``mpmath.iv`` angular interval oracle.

    ``mpmath.iv`` does not expose ``asin`` in the local environment, so this
    backend evaluates ``asin(x)`` as ``atan2(x, sqrt(1-x^2))`` for
    ``0 < x < 1``. Endpoints are widened by ``guard_decimal`` after interval
    evaluation. The verifier treats this backend as certification-capable only
    under this documented interval contract; the global certificate task should
    revisit backend provenance before publishing production certificates.
    """

    digits: int = DEFAULT_INTERVAL_DIGITS
    guard_decimal: str | None = None
    certification_capable: bool = True

    @property
    def backend_info(self) -> IntervalBackendInfo:
        guard = self._guard_decimal()
        return IntervalBackendInfo(
            backend="mpmath_iv_guarded_atan2_v1",
            precision_digits=self.digits,
            rounding_policy=(
                "mpmath.iv interval arithmetic; asin(x) evaluated as "
                "atan2(x, sqrt(1-x^2)); final endpoints widened by guard_decimal"
            ),
            outward_enclosure=True,
            certification_capable=self.certification_capable,
            tolerance_based=False,
            guard_decimal=guard,
        )

    def theta(self, R: mp.mpf, a: mp.mpf, b: mp.mpf) -> DecimalInterval:
        """Return a guarded interval for the required angular separation."""
        R_value = _positive_mpf(R, "R")
        a_value = _positive_mpf(a, "a")
        b_value = _positive_mpf(b, "b")
        with _mp_interval_precision(self.digits):
            R_iv = mp.iv.mpf(str(R_value))
            a_iv = mp.iv.mpf(str(a_value))
            b_iv = mp.iv.mpf(str(b_value))
            x2 = (a_iv * b_iv) / ((R_iv + a_iv) * (R_iv + b_iv))
            x = mp.iv.sqrt(x2)
            theta_iv = 2 * mp.iv.atan2(x, mp.iv.sqrt(1 - x * x))
        interval = _guarded_interval(theta_iv, self._guard())
        if not (interval.lower > 0 and interval.upper < mp.pi):
            raise ValueError(
                "theta interval must lie inside (0, pi): "
                f"R={R_value}, a={a_value}, b={b_value}, interval={interval}"
            )
        return interval

    def tau(self) -> DecimalInterval:
        """Return a guarded interval for ``2*pi``."""
        with _mp_interval_precision(self.digits):
            tau_iv = 2 * mp.iv.pi
        return _guarded_interval(tau_iv, self._guard())

    def _guard(self) -> mp.mpf:
        return mp.mpf(self._guard_decimal())

    def _guard_decimal(self) -> str:
        if self.guard_decimal is not None:
            _assert_decimal_string(self.guard_decimal, "guard_decimal")
            guard = mp.mpf(self.guard_decimal)
            if guard < 0:
                raise ValueError("guard_decimal must be nonnegative")
            return self.guard_decimal
        return f"1e-{max(10, self.digits - 10)}"


@dataclass(frozen=True)
class CycleEdge:
    """One directed STN edge in a lower-endpoint negative-cycle certificate."""

    source: int
    target: int
    edge_kind: EdgeKind
    pair: tuple[int, int]


@dataclass(frozen=True)
class FixedOrderIntervalVerification:
    """Result of checking one fixed-order interval bracket record."""

    verified: bool
    index_order: tuple[int, ...]
    radius_order: tuple[int, ...]
    lower_radius: mp.mpf
    upper_radius: mp.mpf
    lower_negative_cycle_sum_upper: mp.mpf
    min_upper_witness_slack_lower: mp.mpf
    messages: tuple[str, ...]


def verify_fixed_order_interval_bracket(
    record: Mapping[str, Any],
    *,
    oracle: AngularIntervalOracle | None = None,
) -> FixedOrderIntervalVerification:
    """Verify one local fixed-order interval bracket record.

    The returned ``verified`` flag is true only when both endpoints pass strict
    interval checks and the record declares non-tolerance interval semantics.
    No STN diagonal tolerance is used anywhere in this verifier.
    """
    source = _expect_mapping(record, "fixed-order interval bracket record")
    oracle = oracle or MPMathIntervalAngularOracle()
    messages: list[str] = []

    index_order = _parse_index_order(source.get("index_order"))
    radius_order = _parse_radius_order(source.get("radius_order"), len(index_order))
    lower_radius = _positive_mpf_decimal(source.get("lower_radius_decimal"), "lower_radius_decimal")
    upper_radius = _positive_mpf_decimal(source.get("upper_radius_decimal"), "upper_radius_decimal")

    if source.get("schema_version") != FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION:
        messages.append("schema_version is missing or unsupported")
    if radius_order != index_order_to_radius_order(index_order):
        messages.append("radius_order must match the quadratic square of index_order")
    if canonicalize_index_order(index_order) != index_order:
        messages.append("index_order must be canonical modulo rotation and reflection")
    if lower_radius > upper_radius:
        messages.append("lower_radius_decimal must be <= upper_radius_decimal")

    if not _backend_metadata_matches(source.get("theta_interval_backend"), oracle.backend_info, messages):
        pass

    try:
        cycle = _parse_negative_cycle(source.get("lower_certificate"), len(index_order))
        cycle_sum_upper = _negative_cycle_sum_upper(
            cycle,
            radius_order,
            lower_radius,
            oracle,
        )
    except ValueError as exc:
        cycle_sum_upper = mp.inf
        messages.append(str(exc))

    if cycle_sum_upper >= 0:
        messages.append(
            "lower negative-cycle upper bound must be strictly negative, "
            f"got {mp.nstr(cycle_sum_upper, 30)}"
        )
    _check_reported_cycle_sum(source.get("lower_negative_cycle_sum_upper"), cycle_sum_upper, messages)

    try:
        positions = _parse_witness_positions(source.get("upper_certificate"), len(index_order))
        min_slack_lower = _min_witness_slack_lower(
            positions,
            radius_order,
            upper_radius,
            oracle,
        )
    except ValueError as exc:
        min_slack_lower = -mp.inf
        messages.append(str(exc))

    if min_slack_lower < 0:
        messages.append(
            "upper witness minimum slack lower bound must be nonnegative, "
            f"got {mp.nstr(min_slack_lower, 30)}"
        )
    _check_reported_min_slack(source.get("min_upper_witness_slack_lower"), min_slack_lower, messages)

    return FixedOrderIntervalVerification(
        verified=not messages,
        index_order=index_order,
        radius_order=radius_order,
        lower_radius=lower_radius,
        upper_radius=upper_radius,
        lower_negative_cycle_sum_upper=cycle_sum_upper,
        min_upper_witness_slack_lower=min_slack_lower,
        messages=tuple(messages),
    )


def assert_fixed_order_interval_bracket_verified(
    record: Mapping[str, Any],
    *,
    oracle: AngularIntervalOracle | None = None,
) -> FixedOrderIntervalVerification:
    """Return the verification result or raise ``ValueError`` with messages."""
    result = verify_fixed_order_interval_bracket(record, oracle=oracle)
    if not result.verified:
        raise ValueError("; ".join(result.messages))
    return result


def _negative_cycle_sum_upper(
    cycle: Sequence[CycleEdge],
    radius_order: Sequence[int],
    R: mp.mpf,
    oracle: AngularIntervalOracle,
) -> mp.mpf:
    tau = oracle.tau()
    total = mp.mpf("0")
    for edge in cycle:
        i, j = edge.pair
        theta = oracle.theta(R, mp.mpf(radius_order[i]), mp.mpf(radius_order[j]))
        if edge.edge_kind == "forward_lower":
            total += -theta.lower
        elif edge.edge_kind == "wrap_upper":
            total += tau.upper - theta.lower
        else:  # pragma: no cover - parser enforces edge kind
            raise ValueError(f"unsupported edge kind {edge.edge_kind!r}")
    return total


def _min_witness_slack_lower(
    positions: Sequence[mp.mpf],
    radius_order: Sequence[int],
    R: mp.mpf,
    oracle: AngularIntervalOracle,
) -> mp.mpf:
    tau = oracle.tau()
    minimum: mp.mpf | None = None
    for i in range(len(radius_order)):
        for j in range(i + 1, len(radius_order)):
            theta = oracle.theta(R, mp.mpf(radius_order[i]), mp.mpf(radius_order[j]))
            delta = positions[j] - positions[i]
            forward = delta - theta.upper
            wrap = tau.lower - theta.upper - delta
            pair_min = min(forward, wrap)
            minimum = pair_min if minimum is None else min(minimum, pair_min)
    if minimum is None:
        raise ValueError("witness requires at least one pair")
    return minimum


def _parse_negative_cycle(value: Any, n: int) -> tuple[CycleEdge, ...]:
    certificate = _expect_mapping(value, "lower_certificate")
    if certificate.get("kind") != "negative_cycle":
        raise ValueError("lower_certificate.kind must be negative_cycle")
    raw_edges = certificate.get("cycle", certificate.get("negative_cycle"))
    if not isinstance(raw_edges, list) or len(raw_edges) < 2:
        raise ValueError("lower_certificate must contain a cycle list with at least two edges")
    edges = tuple(_parse_cycle_edge(edge, n, position=i) for i, edge in enumerate(raw_edges))
    for current, nxt in zip(edges, edges[1:] + edges[:1], strict=True):
        if current.target != nxt.source:
            raise ValueError(
                "negative cycle edges must be connected: "
                f"edge target {current.target} != next source {nxt.source}"
            )
    return edges


def _parse_cycle_edge(value: Any, n: int, *, position: int) -> CycleEdge:
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, Mapping)):
        if len(value) != 3:
            raise ValueError(f"cycle edge {position} sequence must have length 3")
        source, target, edge_kind = value
        source = _parse_node(source, n, f"cycle[{position}].source")
        target = _parse_node(target, n, f"cycle[{position}].target")
    else:
        edge = _expect_mapping(value, f"cycle[{position}]")
        source = _parse_node(edge.get("source"), n, f"cycle[{position}].source")
        target = _parse_node(edge.get("target"), n, f"cycle[{position}].target")
        edge_kind = edge.get("edge_kind")

    if edge_kind not in EDGE_KINDS:
        raise ValueError(f"cycle[{position}].edge_kind must be one of {sorted(EDGE_KINDS)}")
    if edge_kind == "forward_lower":
        if source <= target:
            raise ValueError("forward_lower edges must be j -> i for i < j")
        pair = (target, source)
    else:
        if source >= target:
            raise ValueError("wrap_upper edges must be i -> j for i < j")
        pair = (source, target)
    return CycleEdge(source=source, target=target, edge_kind=edge_kind, pair=pair)


def _parse_witness_positions(value: Any, n: int) -> tuple[mp.mpf, ...]:
    certificate = _expect_mapping(value, "upper_certificate")
    if certificate.get("kind") not in {"witness_positions", "feasible_witness"}:
        raise ValueError("upper_certificate.kind must be witness_positions")
    raw_positions = certificate.get("positions_rad", certificate.get("witness_positions"))
    if not isinstance(raw_positions, list) or len(raw_positions) != n:
        raise ValueError("upper_certificate positions must contain one angle per radius")
    positions = tuple(
        _mpf_decimal(item, f"upper_certificate.positions_rad[{i}]")
        for i, item in enumerate(raw_positions)
    )
    if positions[0] != 0:
        raise ValueError("upper witness must anchor positions[0] at decimal zero")
    return positions


def _backend_metadata_matches(
    value: Any,
    info: IntervalBackendInfo,
    messages: list[str],
) -> bool:
    metadata = _expect_mapping(value, "theta_interval_backend")
    ok = True
    expected = info.to_record()
    for key in ("backend", "precision_digits", "guard_decimal"):
        if key in expected and metadata.get(key) != expected[key]:
            ok = False
            messages.append(
                f"theta_interval_backend.{key} must match oracle metadata "
                f"{expected[key]!r}"
            )
    if not isinstance(metadata.get("rounding_policy"), str) or not metadata["rounding_policy"]:
        ok = False
        messages.append("theta_interval_backend.rounding_policy must be non-empty")
    if metadata.get("outward_enclosure") is not True:
        ok = False
        messages.append("theta_interval_backend must declare outward_enclosure=true")
    if metadata.get("certification_capable") is not True:
        ok = False
        messages.append("theta_interval_backend must declare certification_capable=true")
    if metadata.get("tolerance_based") is not False:
        ok = False
        messages.append("theta_interval_backend must declare tolerance_based=false")
    if info.tolerance_based:
        ok = False
        messages.append("oracle backend is tolerance-based and cannot certify interval brackets")
    if not info.outward_enclosure:
        ok = False
        messages.append("oracle backend does not provide outward interval enclosures")
    if not info.certification_capable:
        ok = False
        messages.append("oracle backend is not certification-capable")
    return ok


def _check_reported_min_slack(value: Any, computed: mp.mpf, messages: list[str]) -> None:
    reported = _mpf_decimal(value, "min_upper_witness_slack_lower")
    if reported < 0:
        messages.append("min_upper_witness_slack_lower must be nonnegative")
    if reported > computed:
        messages.append(
            "min_upper_witness_slack_lower overstates recomputed lower bound: "
            f"reported={mp.nstr(reported, 30)} computed={mp.nstr(computed, 30)}"
        )


def _check_reported_cycle_sum(value: Any, computed: mp.mpf, messages: list[str]) -> None:
    reported = _mpf_decimal(value, "lower_negative_cycle_sum_upper")
    if reported >= 0:
        messages.append("lower_negative_cycle_sum_upper must be strictly negative")
    if reported < computed:
        messages.append(
            "lower_negative_cycle_sum_upper understates recomputed upper bound: "
            f"reported={mp.nstr(reported, 30)} computed={mp.nstr(computed, 30)}"
        )


def _parse_index_order(value: Any) -> tuple[int, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise ValueError("index_order must be a sequence of integers")
    order = tuple(_parse_positive_int(item, "index_order") for item in value)
    if len(order) < 3:
        raise ValueError("index_order must contain at least three indices")
    expected = tuple(range(1, len(order) + 1))
    if tuple(sorted(order)) != expected:
        raise ValueError("index_order must be a permutation of 1..n")
    return order


def _parse_radius_order(value: Any, n: int) -> tuple[int, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise ValueError("radius_order must be a sequence of positive integers")
    order = tuple(_parse_positive_int(item, "radius_order") for item in value)
    if len(order) != n:
        raise ValueError("radius_order length must equal index_order length")
    return order


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


def _parse_node(value: Any, n: int, name: str) -> int:
    node = _parse_nonnegative_int(value, name)
    if node >= n:
        raise ValueError(f"{name} must be less than n={n}")
    return node


def _parse_nonnegative_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a nonnegative integer")
    if isinstance(value, int):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = int(value, 10)
        except ValueError as exc:
            raise ValueError(f"{name} must be a nonnegative integer") from exc
        if str(parsed) != value:
            raise ValueError(f"{name} must be a nonnegative integer")
    else:
        raise ValueError(f"{name} must be a nonnegative integer")
    if parsed < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return parsed


def _positive_mpf_decimal(value: Any, name: str) -> mp.mpf:
    parsed = _mpf_decimal(value, name)
    if parsed <= 0:
        raise ValueError(f"{name} must be positive")
    return parsed


def _positive_mpf(value: Any, name: str) -> mp.mpf:
    parsed = mp.mpf(value)
    if not mp.isfinite(parsed) or parsed <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return parsed


def _mpf_decimal(value: Any, name: str) -> mp.mpf:
    _assert_decimal_string(value, name)
    parsed = mp.mpf(value)
    if not mp.isfinite(parsed):
        raise ValueError(f"{name} must be finite")
    return parsed


def _assert_decimal_string(value: Any, name: str) -> None:
    if not isinstance(value, str) or DECIMAL_STRING_RE.fullmatch(value) is None:
        raise ValueError(f"{name} must be a decimal string, got {value!r}")


def _expect_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be a mapping")
    return value


def _guarded_interval(value: Any, guard: mp.mpf) -> DecimalInterval:
    lower = mp.mpf(value.a) - guard
    upper = mp.mpf(value.b) + guard
    return DecimalInterval(lower=lower, upper=upper)


class _mp_interval_precision:
    def __init__(self, digits: int):
        if isinstance(digits, bool) or not isinstance(digits, int) or digits < 30:
            raise ValueError(f"interval digits must be an integer at least 30, got {digits!r}")
        self.digits = digits
        self.old_mp_dps: int | None = None
        self.old_iv_dps: int | None = None

    def __enter__(self) -> None:
        self.old_mp_dps = mp.mp.dps
        self.old_iv_dps = mp.iv.dps
        mp.mp.dps = self.digits
        mp.iv.dps = self.digits

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        if self.old_mp_dps is not None:
            mp.mp.dps = self.old_mp_dps
        if self.old_iv_dps is not None:
            mp.iv.dps = self.old_iv_dps


__all__ = [
    "AngularIntervalOracle",
    "CycleEdge",
    "DecimalInterval",
    "FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION",
    "FixedOrderIntervalVerification",
    "IntervalBackendInfo",
    "MPMathIntervalAngularOracle",
    "assert_fixed_order_interval_bracket_verified",
    "verify_fixed_order_interval_bracket",
]
