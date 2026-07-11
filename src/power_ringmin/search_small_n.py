"""Exhaustive small-n cyclic-order search for quadratic radii."""

from __future__ import annotations

import argparse
import copy
from collections.abc import Iterator, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
import itertools
import json
import math
from pathlib import Path
import shlex
import sys
from typing import Any, Literal

import mpmath as mp

from power_ringmin.evaluator import FULL_REL_TOL, full_radius
from power_ringmin.fixed_order_artifact import (
    EVIDENCE_CLASSIFICATIONS,
    UPSTREAM_RINGMIN_COMMIT,
    detect_repository_state,
)
from power_ringmin.geometry import quadratic_radii
from power_ringmin.highprec import feasibility_margin_mp, full_radius_mp, is_feasible_mp

SEARCH_SCHEMA_VERSION = "power-ringmin.small_n_search_result.v1"
SEARCH_ARTIFACT_TYPE = "small_n_search_numerical_result"
SEARCH_MODE = "exhaustive_float64"
ORDER_EQUIVALENCE = "rotation_reflection"
CANONICALIZATION_RULE = "largest_index_first_second_index_less_than_last"
EVIDENCE_CLASSIFICATION = "numerical_observation"
EVIDENCE_SCOPE = "finite_exhaustive_float64_order_search"
HIGH_PRECISION_RECHECK_BACKEND = "mpmath"
HIGH_PRECISION_RECHECK_SELECTION = "float64_incumbent_and_ties"
DEFAULT_HIGH_PRECISION_RECHECK_DIGITS = 80

SearchMode = Literal["exhaustive_float64"]


@dataclass(frozen=True)
class OrderSearchRecord:
    """One evaluated canonical cyclic index order."""

    index_order: tuple[int, ...]
    radius_order: tuple[int, ...]
    R_chain: float
    R_full: float
    feasible: bool


@dataclass(frozen=True)
class HighPrecisionRecheckRecord:
    """High-precision recomputation for one float64 incumbent/tie order."""

    index_order: tuple[int, ...]
    radius_order: tuple[int, ...]
    float64_R_full: float
    mpmath_R_full_decimal: str
    delta_mpmath_minus_float64_decimal: str
    feasibility_margin_decimal: str
    feasible_with_default_tol: bool
    digits: int


@dataclass(frozen=True)
class SmallNSearchResult:
    """Result of an exhaustive small-n float64 search."""

    n: int
    radius_sequence: tuple[int, ...]
    mode: SearchMode
    order_equivalence: Literal["rotation_reflection"]
    canonicalization_rule: Literal["largest_index_first_second_index_less_than_last"]
    expected_canonical_count: int
    enumerated_count: int
    evaluated_full_count: int
    best: OrderSearchRecord
    ties: tuple[OrderSearchRecord, ...]
    top_records: tuple[OrderSearchRecord, ...]
    top_k: int
    tie_abs_tol: float
    tie_rel_tol: float
    high_precision_recheck_digits: int
    high_precision_rechecks: tuple[HighPrecisionRecheckRecord, ...]
    evidence_classification: Literal["numerical_observation"]


def canonical_index_order_count(n: int) -> int:
    """Return the number of cyclic orders modulo rotation and reflection."""
    _validate_search_n(n)
    return math.factorial(n - 1) // 2


def canonical_index_orders(n: int) -> Iterator[tuple[int, ...]]:
    """Yield canonical cyclic index orders modulo rotation and reflection.

    The largest index is fixed in position 0. Reflection duplicates are removed
    by retaining exactly the orientation where the second index is smaller than
    the last index.
    """
    _validate_search_n(n)
    for tail in itertools.permutations(range(1, n)):
        order = (n, *tail)
        if order[1] < order[-1]:
            yield order


def canonicalize_index_order(order: Sequence[int]) -> tuple[int, ...]:
    """Return the canonical representative of one quadratic index cycle."""
    indices = _normalize_index_order(order, min_n=3)
    n = len(indices)
    forward = _rotate_to_front(indices, n)
    backward = _rotate_to_front(tuple(reversed(indices)), n)
    return forward if forward[1] < forward[-1] else backward


def index_order_to_radius_order(order: Sequence[int]) -> tuple[int, ...]:
    """Map a quadratic index order to explicit quadratic radii."""
    indices = _normalize_index_order(order, min_n=1)
    return tuple(index * index for index in indices)


def exhaustive_float64_search(
    n: int,
    *,
    top_k: int = 20,
    tie_abs_tol: float = 1e-9,
    tie_rel_tol: float = 1e-12,
    high_precision_recheck: bool = True,
    high_precision_recheck_digits: int = DEFAULT_HIGH_PRECISION_RECHECK_DIGITS,
) -> SmallNSearchResult:
    """Evaluate every canonical quadratic index order with the float64 backend."""
    _validate_search_n(n)
    if top_k < 1:
        raise ValueError(f"top_k must be positive, got {top_k!r}")
    if tie_abs_tol < 0.0 or tie_rel_tol < 0.0:
        raise ValueError("tie tolerances must be nonnegative")
    _validate_high_precision_digits(high_precision_recheck_digits)

    records: list[OrderSearchRecord] = []
    for index_order in canonical_index_orders(n):
        radius_order = index_order_to_radius_order(index_order)
        fixed = full_radius(radius_order)
        records.append(
            OrderSearchRecord(
                index_order=index_order,
                radius_order=radius_order,
                R_chain=fixed.R_chain,
                R_full=fixed.R_full,
                feasible=fixed.feasible,
            )
        )

    expected_count = canonical_index_order_count(n)
    if len(records) != expected_count:
        raise AssertionError(
            f"canonical enumeration count mismatch for n={n}: "
            f"expected {expected_count}, got {len(records)}"
        )

    ranked = tuple(sorted(records, key=lambda record: (record.R_full, record.index_order)))
    best = ranked[0]
    ties = tuple(
        record
        for record in ranked
        if _within_tolerance(
            record.R_full,
            best.R_full,
            abs_tol=tie_abs_tol,
            rel_tol=tie_rel_tol,
        )
    )
    high_precision_rechecks = (
        _build_high_precision_rechecks(ties, digits=high_precision_recheck_digits)
        if high_precision_recheck
        else ()
    )
    return SmallNSearchResult(
        n=n,
        radius_sequence=quadratic_radii(n),
        mode=SEARCH_MODE,
        order_equivalence=ORDER_EQUIVALENCE,
        canonicalization_rule=CANONICALIZATION_RULE,
        expected_canonical_count=expected_count,
        enumerated_count=len(records),
        evaluated_full_count=len(records),
        best=best,
        ties=ties,
        top_records=ranked[:top_k],
        top_k=top_k,
        tie_abs_tol=float(tie_abs_tol),
        tie_rel_tol=float(tie_rel_tol),
        high_precision_recheck_digits=high_precision_recheck_digits,
        high_precision_rechecks=high_precision_rechecks,
        evidence_classification=EVIDENCE_CLASSIFICATION,
    )


def build_small_n_search_artifact(
    result: SmallNSearchResult,
    *,
    created_at_utc: str | None = None,
    argv_for_provenance: Sequence[str] | None = None,
    output: Path | None = None,
) -> dict[str, Any]:
    """Build and validate a JSON-serializable search summary artifact."""
    command = _command_record(
        argv_for_provenance,
        output=output,
        n=result.n,
        top_k=result.top_k,
        high_precision_recheck_count=len(result.high_precision_rechecks),
        high_precision_recheck_digits=result.high_precision_recheck_digits,
    )
    software = [
        {
            "name": "Python",
            "version": sys.version.split()[0],
            "role": "runtime",
        },
        {
            "name": "power-ringmin",
            "version": "0.1.0",
            "role": "small-n search implementation",
        },
    ]
    source_files = [
        {
            "path": "src/power_ringmin/search_small_n.py",
            "role": "canonical enumeration and exhaustive float64 search",
        },
        {
            "path": "src/power_ringmin/evaluator.py",
            "role": "float64 all-pairs fixed-order STN evaluator",
            "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
        },
        {
            "path": "src/power_ringmin/geometry.py",
            "role": "quadratic radii and geometric primitives",
            "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
        },
    ]
    if result.high_precision_rechecks:
        software.append(
            {
                "name": "mpmath",
                "version": mp.__version__,
                "role": "high-precision incumbent/tie recheck",
            }
        )
        source_files.append(
            {
                "path": "src/power_ringmin/highprec.py",
                "role": "mpmath fixed-order STN recheck",
                "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
            }
        )

    artifact: dict[str, Any] = {
        "schema_version": SEARCH_SCHEMA_VERSION,
        "artifact_type": SEARCH_ARTIFACT_TYPE,
        "problem": {
            "project": "power-ringmin",
            "radius_model": "quadratic",
            "dimension": 2,
            "constraints": {
                "central_external_tangency": True,
                "peripheral_pairwise_disjoint_interiors": True,
                "all_pairs_checked": True,
            },
        },
        "instance": {
            "n": result.n,
            "radius_sequence": {
                "kind": "explicit",
                "formula": "k^2",
                "index_base": 1,
                "indices": list(range(1, result.n + 1)),
                "radii": list(result.radius_sequence),
            },
        },
        "order_space": {
            "order_type": "cyclic",
            "equivalence": result.order_equivalence,
            "canonicalization_rule": result.canonicalization_rule,
            "expected_canonical_count": result.expected_canonical_count,
            "enumerated_count": result.enumerated_count,
        },
        "search_method": {
            "mode": result.mode,
            "backend": "float64",
            "top_k": result.top_k,
            "tie_abs_tol_decimal": _decimal_string(result.tie_abs_tol),
            "tie_rel_tol_decimal": _decimal_string(result.tie_rel_tol),
            "high_precision_recheck": {
                "enabled": bool(result.high_precision_rechecks),
                "selection": HIGH_PRECISION_RECHECK_SELECTION,
                "backend": HIGH_PRECISION_RECHECK_BACKEND,
                "digits": result.high_precision_recheck_digits,
            },
            "randomness": {
                "used": False,
                "seeds": [],
            },
        },
        "result": {
            "best": _record_to_json(result.best),
            "ties": [_record_to_json(record) for record in result.ties],
            "top_records": [_record_to_json(record) for record in result.top_records],
            "evaluated_full_count": result.evaluated_full_count,
        },
        "high_precision_recheck": {
            "enabled": bool(result.high_precision_rechecks),
            "selection": HIGH_PRECISION_RECHECK_SELECTION,
            "backend": HIGH_PRECISION_RECHECK_BACKEND,
            "digits": result.high_precision_recheck_digits,
            "record_count": len(result.high_precision_rechecks),
            "records": [
                _high_precision_recheck_to_json(record)
                for record in result.high_precision_rechecks
            ],
            "limitations": [
                "Rechecks only the float64 incumbent and float64 tie orders.",
                "High-precision bisection outputs are numerical values, not certified intervals.",
                "No lower interval bounds are computed for every nonwinner order.",
            ],
        },
        "precision": {
            "value_encoding": "decimal_string",
            "primary_backend": "float64",
            "working_precision_digits": 17,
            "rounding_policy": "Float64 values encoded with Python repr.",
            "tolerances": [
                {
                    "name": "full_radius_relative_bisection",
                    "value_decimal": _decimal_string(FULL_REL_TOL),
                    "tolerance_type": "relative",
                    "applies_to": "float64 fixed-order radius bisection",
                },
                {
                    "name": "tie_abs_tol",
                    "value_decimal": _decimal_string(result.tie_abs_tol),
                    "tolerance_type": "absolute",
                    "applies_to": "best-order tie grouping",
                },
                {
                    "name": "tie_rel_tol",
                    "value_decimal": _decimal_string(result.tie_rel_tol),
                    "tolerance_type": "relative",
                    "applies_to": "best-order tie grouping",
                },
            ],
        },
        "provenance": {
            "created_at_utc": created_at_utc or _created_at_utc_now(),
            "repository": detect_repository_state(),
            "software": software,
            "source_files": source_files,
            "commands": [command],
        },
        "evidence": {
            "classification": result.evidence_classification,
            "claim": {
                "scope": EVIDENCE_SCOPE,
                "statement": (
                    "This artifact records a finite exhaustive float64 search over "
                    "canonical cyclic index orders for one quadratic-radii instance. "
                    "It is a numerical observation, not a computer-certified global "
                    "optimum."
                ),
            },
            "checks": [
                {
                    "check_id": "EV-001",
                    "classification": "verified_fact",
                    "method": "canonical index-order enumeration",
                    "result": "pass",
                    "output_summary": (
                        f"Enumerated {result.enumerated_count} canonical orders; "
                        f"expected {result.expected_canonical_count}."
                    ),
                    "limitations": "Enumeration count does not certify float64 numerical values.",
                },
                {
                    "check_id": "EV-002",
                    "classification": "numerical_observation",
                    "method": "float64 all-pairs STN fixed-order evaluation",
                    "result": "pass",
                    "output_summary": (
                        f"Evaluated {result.evaluated_full_count} fixed orders; "
                        f"best R_full={_decimal_string(result.best.R_full)}."
                    ),
                    "limitations": "Float64 exhaustive output is finite numerical evidence only.",
                },
                {
                    "check_id": "EV-003",
                    "classification": "numerical_observation",
                    "method": "mpmath high-precision recheck of float64 incumbent/tie orders",
                    "result": "pass" if result.high_precision_rechecks else "not_run",
                    "output_summary": (
                        f"Rechecked {len(result.high_precision_rechecks)} "
                        "float64 incumbent/tie orders at "
                        f"{result.high_precision_recheck_digits} digits."
                    ),
                    "limitations": (
                        "This is not interval verification and does not check "
                        "high-precision lower bounds for every nonwinner order."
                    ),
                },
            ],
            "limitations": [
                "Finite n only.",
                "Float64 fixed-order evaluations only.",
                "High-precision incumbent/tie rechecks are numerical observations only.",
                "No independent high-precision interval verifier for every order.",
                "No computer-certified global optimum claim.",
                "No theorem for all n.",
            ],
        },
    }
    validate_small_n_search_artifact(artifact)
    return artifact


def dump_small_n_search_artifact(
    artifact: Mapping[str, Any],
    path: str | Path,
    *,
    indent: int = 2,
) -> None:
    """Validate and write a small-n search artifact as UTF-8 JSON."""
    Path(path).write_text(dumps_small_n_search_artifact(artifact, indent=indent), encoding="utf-8")


def dumps_small_n_search_artifact(
    artifact: Mapping[str, Any],
    *,
    indent: int = 2,
) -> str:
    """Validate and serialize a small-n search artifact."""
    data = copy.deepcopy(dict(artifact))
    validate_small_n_search_artifact(data)
    return json.dumps(data, indent=indent, sort_keys=False) + "\n"


def load_small_n_search_artifact(path: str | Path) -> dict[str, Any]:
    """Load and validate a small-n search artifact from JSON."""
    return loads_small_n_search_artifact(Path(path).read_text(encoding="utf-8"))


def loads_small_n_search_artifact(text: str) -> dict[str, Any]:
    """Load and validate a small-n search artifact from a JSON string."""
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("small-n search artifact JSON must contain an object")
    validate_small_n_search_artifact(payload)
    return payload


def validate_small_n_search_artifact(artifact: Mapping[str, Any]) -> None:
    """Validate the semantic contract for a v1 small-n search artifact."""
    source = _expect_mapping(artifact, "artifact")
    if source.get("schema_version") != SEARCH_SCHEMA_VERSION:
        raise ValueError("unsupported small-n search schema_version")
    if source.get("artifact_type") != SEARCH_ARTIFACT_TYPE:
        raise ValueError("unsupported small-n search artifact_type")

    problem = _expect_mapping(source.get("problem"), "problem")
    constraints = _expect_mapping(problem.get("constraints"), "problem.constraints")
    if problem.get("project") != "power-ringmin":
        raise ValueError("problem.project must be power-ringmin")
    if problem.get("radius_model") != "quadratic":
        raise ValueError("problem.radius_model must be quadratic")
    if constraints.get("all_pairs_checked") is not True:
        raise ValueError("problem.constraints.all_pairs_checked must be true")

    instance = _expect_mapping(source.get("instance"), "instance")
    n = int(instance.get("n"))
    _validate_search_n(n)
    radius_sequence = _expect_mapping(instance.get("radius_sequence"), "instance.radius_sequence")
    if tuple(radius_sequence.get("indices", [])) != tuple(range(1, n + 1)):
        raise ValueError("instance.radius_sequence.indices must equal 1..n")
    if tuple(radius_sequence.get("radii", [])) != quadratic_radii(n):
        raise ValueError("instance.radius_sequence.radii must equal k^2")

    order_space = _expect_mapping(source.get("order_space"), "order_space")
    expected_count = canonical_index_order_count(n)
    if order_space.get("equivalence") != ORDER_EQUIVALENCE:
        raise ValueError("order_space.equivalence must be rotation_reflection")
    if order_space.get("canonicalization_rule") != CANONICALIZATION_RULE:
        raise ValueError("unsupported order_space.canonicalization_rule")
    if int(order_space.get("expected_canonical_count")) != expected_count:
        raise ValueError("order_space.expected_canonical_count is inconsistent with n")
    enumerated_count = int(order_space.get("enumerated_count"))
    if enumerated_count != expected_count:
        raise ValueError("order_space.enumerated_count must equal expected count")

    method = _expect_mapping(source.get("search_method"), "search_method")
    if method.get("mode") != SEARCH_MODE:
        raise ValueError("search_method.mode must be exhaustive_float64")
    if method.get("backend") != "float64":
        raise ValueError("search_method.backend must be float64")
    _assert_decimal_string(method.get("tie_abs_tol_decimal"), "search_method.tie_abs_tol_decimal")
    _assert_decimal_string(method.get("tie_rel_tol_decimal"), "search_method.tie_rel_tol_decimal")
    method_recheck = method.get("high_precision_recheck")
    if method_recheck is not None:
        _validate_high_precision_recheck_metadata(
            method_recheck,
            "search_method.high_precision_recheck",
        )

    result = _expect_mapping(source.get("result"), "result")
    if int(result.get("evaluated_full_count")) != expected_count:
        raise ValueError("result.evaluated_full_count must equal expected count")
    _validate_record(result.get("best"), n, "result.best")
    for i, record in enumerate(_expect_list(result.get("ties"), "result.ties")):
        _validate_record(record, n, f"result.ties[{i}]")
    for i, record in enumerate(_expect_list(result.get("top_records"), "result.top_records")):
        _validate_record(record, n, f"result.top_records[{i}]")
    tie_orders = {
        tuple(_expect_list(record["index_order"], f"result.ties[{i}].index_order"))
        for i, record in enumerate(_expect_list(result.get("ties"), "result.ties"))
    }

    recheck = source.get("high_precision_recheck")
    if recheck is not None:
        _validate_high_precision_recheck_block(recheck, n, tie_orders)
        if method_recheck is not None:
            _validate_high_precision_recheck_consistency(method_recheck, recheck)

    evidence = _expect_mapping(source.get("evidence"), "evidence")
    classification = evidence.get("classification")
    if classification not in EVIDENCE_CLASSIFICATIONS:
        raise ValueError("unsupported evidence.classification")
    if classification != EVIDENCE_CLASSIFICATION:
        raise ValueError("small-n float64 search artifacts must be numerical_observation")
    claim = _expect_mapping(evidence.get("claim"), "evidence.claim")
    if claim.get("scope") != EVIDENCE_SCOPE:
        raise ValueError("evidence.claim.scope must be finite_exhaustive_float64_order_search")
    _expect_list(evidence.get("checks"), "evidence.checks")
    limitations = _expect_list(evidence.get("limitations"), "evidence.limitations")
    if not any("No computer-certified global optimum claim" in str(item) for item in limitations):
        raise ValueError("evidence.limitations must disclaim certified global optimality")


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for exhaustive small-n search."""
    parser = argparse.ArgumentParser(
        description="Run an exhaustive float64 search over canonical quadratic index orders.",
    )
    parser.add_argument("--n", required=True, type=int, help="quadratic instance size, minimum 3")
    parser.add_argument(
        "--backend",
        choices=("float64",),
        default="float64",
        help="search backend (only float64 is implemented)",
    )
    parser.add_argument("--top-k", type=int, default=20, help="number of best records to retain")
    parser.add_argument(
        "--tie-abs-tol",
        type=float,
        default=1e-9,
        help="absolute tolerance for grouping best-order ties",
    )
    parser.add_argument(
        "--tie-rel-tol",
        type=float,
        default=1e-12,
        help="relative tolerance for grouping best-order ties",
    )
    parser.add_argument(
        "--highprec-recheck-digits",
        type=int,
        default=DEFAULT_HIGH_PRECISION_RECHECK_DIGITS,
        help="mpmath digits for incumbent/tie rechecks",
    )
    parser.add_argument(
        "--no-highprec-recheck",
        action="store_true",
        help="skip the default mpmath incumbent/tie recheck",
    )
    parser.add_argument("-o", "--output", required=True, type=Path, help="path to write JSON summary")
    parser.add_argument("--created-at-utc", help="optional UTC timestamp to record in provenance")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the exhaustive small-n search CLI."""
    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)

    try:
        result = exhaustive_float64_search(
            args.n,
            top_k=args.top_k,
            tie_abs_tol=args.tie_abs_tol,
            tie_rel_tol=args.tie_rel_tol,
            high_precision_recheck=not args.no_highprec_recheck,
            high_precision_recheck_digits=args.highprec_recheck_digits,
        )
        artifact = build_small_n_search_artifact(
            result,
            created_at_utc=args.created_at_utc,
            argv_for_provenance=raw_argv,
            output=args.output,
        )
        dump_small_n_search_artifact(artifact, args.output)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    radius = artifact["result"]["best"]["R_full"]["decimal"]
    print(
        f"wrote {args.output} n={args.n} backend={args.backend} "
        f"enumerated={result.enumerated_count} best_R={radius} "
        f"highprec_rechecks={len(result.high_precision_rechecks)}"
    )
    return 0


def _normalize_index_order(order: Sequence[int], *, min_n: int) -> tuple[int, ...]:
    if isinstance(order, (str, bytes)):
        raise ValueError("index order must be a sequence of integers, not a string")
    indices = tuple(_parse_positive_int(value, "index") for value in order)
    if len(indices) < min_n:
        raise ValueError(f"index order requires at least {min_n} entries")
    expected = tuple(range(1, len(indices) + 1))
    if tuple(sorted(indices)) != expected:
        raise ValueError(f"index order must contain exactly 1..{len(indices)}, got {indices!r}")
    return indices


def _parse_positive_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} value must be a positive integer: {value!r}")
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
        raise ValueError(f"{name} value must be a positive integer: {value!r}")
    return parsed


def _validate_search_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError(f"n must be an integer at least 3, got {n!r}")


def _rotate_to_front(order: tuple[int, ...], value: int) -> tuple[int, ...]:
    index = order.index(value)
    return order[index:] + order[:index]


def _within_tolerance(left: float, right: float, *, abs_tol: float, rel_tol: float) -> bool:
    scale = max(1.0, abs(left), abs(right))
    return abs(left - right) <= max(abs_tol, rel_tol * scale)


def _build_high_precision_rechecks(
    records: Sequence[OrderSearchRecord],
    *,
    digits: int,
) -> tuple[HighPrecisionRecheckRecord, ...]:
    _validate_high_precision_digits(digits)
    rechecks: list[HighPrecisionRecheckRecord] = []
    for record in records:
        mp.mp.dps = digits
        radius = full_radius_mp(record.radius_order, digits=digits)
        margin = feasibility_margin_mp(record.radius_order, radius, digits=digits)
        feasible = is_feasible_mp(record.radius_order, radius, digits=digits)
        delta = radius - mp.mpf(repr(record.R_full))
        rechecks.append(
            HighPrecisionRecheckRecord(
                index_order=record.index_order,
                radius_order=record.radius_order,
                float64_R_full=record.R_full,
                mpmath_R_full_decimal=_mp_decimal_string(radius, digits=digits),
                delta_mpmath_minus_float64_decimal=_mp_decimal_string(delta, digits=digits),
                feasibility_margin_decimal=_mp_decimal_string(margin, digits=digits),
                feasible_with_default_tol=bool(feasible),
                digits=digits,
            )
        )
    return tuple(rechecks)


def _record_to_json(record: OrderSearchRecord) -> dict[str, Any]:
    return {
        "index_order": list(record.index_order),
        "radius_order": list(record.radius_order),
        "R_chain": _numeric_value(record.R_chain),
        "R_full": _numeric_value(record.R_full),
        "feasible": record.feasible,
    }


def _high_precision_recheck_to_json(record: HighPrecisionRecheckRecord) -> dict[str, Any]:
    return {
        "index_order": list(record.index_order),
        "radius_order": list(record.radius_order),
        "float64_R_full": _numeric_value(record.float64_R_full),
        "mpmath_R_full": _high_precision_numeric_value(
            record.mpmath_R_full_decimal,
            digits=record.digits,
        ),
        "delta_mpmath_minus_float64": _high_precision_numeric_value(
            record.delta_mpmath_minus_float64_decimal,
            digits=record.digits,
        ),
        "feasibility_margin_at_mpmath_R": _high_precision_numeric_value(
            record.feasibility_margin_decimal,
            digits=record.digits,
        ),
        "feasible_with_default_tol": record.feasible_with_default_tol,
    }


def _numeric_value(value: float) -> dict[str, Any]:
    return {
        "decimal": _decimal_string(value),
        "encoding": "decimal_string",
        "source_precision_digits": 17,
    }


def _high_precision_numeric_value(decimal: str, *, digits: int) -> dict[str, Any]:
    _assert_decimal_string(decimal, "high-precision decimal value")
    return {
        "decimal": decimal,
        "encoding": "decimal_string",
        "source_precision_digits": digits,
    }


def _decimal_string(value: Any) -> str:
    if isinstance(value, bool):
        raise ValueError("boolean values are not numeric decimal strings")
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(f"float must be finite: {value!r}")
        return str(int(value)) if value.is_integer() else repr(value)
    text = str(value).strip()
    _assert_decimal_string(text, "decimal value")
    return text


def _mp_decimal_string(value: Any, *, digits: int) -> str:
    _validate_high_precision_digits(digits)
    with mp.workdps(digits):
        text = mp.nstr(mp.mpf(value), n=digits, strip_zeros=False)
    _assert_decimal_string(text, "mpmath decimal value")
    return text


def _assert_decimal_string(value: Any, name: str) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a non-empty decimal string")
    try:
        parsed = float(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be a decimal string, got {value!r}") from exc
    if not math.isfinite(parsed):
        raise ValueError(f"{name} must be finite, got {value!r}")


def _validate_high_precision_digits(digits: int) -> None:
    if isinstance(digits, bool) or not isinstance(digits, int) or digits < 30:
        raise ValueError(f"high_precision_recheck_digits must be an integer at least 30, got {digits!r}")


def _command_record(
    argv: Sequence[str] | None,
    *,
    output: Path | None,
    n: int,
    top_k: int,
    high_precision_recheck_count: int,
    high_precision_recheck_digits: int,
) -> dict[str, str]:
    command = "power-ringmin-search-small-n"
    if argv:
        command += " " + shlex.join(str(item) for item in argv)
    return {
        "command": command,
        "cwd": str(Path.cwd()),
        "result": "pass",
        "output_summary": (
            f"Ran exhaustive float64 small-n search for n={n}, top_k={top_k}"
            f", high_precision_rechecks={high_precision_recheck_count}"
            f", high_precision_recheck_digits={high_precision_recheck_digits}"
            + (f", output={output}" if output is not None else "")
            + "."
        ),
    }


def _created_at_utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _validate_record(value: Any, n: int, name: str) -> None:
    record = _expect_mapping(value, name)
    index_order = tuple(
        _parse_positive_int(item, f"{name}.index_order")
        for item in _expect_list(record.get("index_order"), f"{name}.index_order")
    )
    if len(index_order) != n:
        raise ValueError(f"{name}.index_order length must equal n")
    if canonicalize_index_order(index_order) != index_order:
        raise ValueError(f"{name}.index_order must be canonical")
    radius_order = tuple(
        _parse_positive_int(item, f"{name}.radius_order")
        for item in _expect_list(record.get("radius_order"), f"{name}.radius_order")
    )
    if radius_order != index_order_to_radius_order(index_order):
        raise ValueError(f"{name}.radius_order must match index_order")
    for key in ("R_chain", "R_full"):
        numeric = _expect_mapping(record.get(key), f"{name}.{key}")
        if numeric.get("encoding") != "decimal_string":
            raise ValueError(f"{name}.{key}.encoding must be decimal_string")
        _assert_decimal_string(numeric.get("decimal"), f"{name}.{key}.decimal")
    if not isinstance(record.get("feasible"), bool):
        raise ValueError(f"{name}.feasible must be boolean")


def _validate_high_precision_recheck_metadata(value: Any, name: str) -> None:
    recheck = _expect_mapping(value, name)
    if not isinstance(recheck.get("enabled"), bool):
        raise ValueError(f"{name}.enabled must be boolean")
    if recheck.get("selection") != HIGH_PRECISION_RECHECK_SELECTION:
        raise ValueError(f"{name}.selection must be {HIGH_PRECISION_RECHECK_SELECTION}")
    if recheck.get("backend") != HIGH_PRECISION_RECHECK_BACKEND:
        raise ValueError(f"{name}.backend must be {HIGH_PRECISION_RECHECK_BACKEND}")
    _validate_high_precision_digits(int(recheck.get("digits")))


def _validate_high_precision_recheck_block(
    value: Any,
    n: int,
    tie_orders: set[tuple[Any, ...]],
) -> None:
    recheck = _expect_mapping(value, "high_precision_recheck")
    _validate_high_precision_recheck_metadata(recheck, "high_precision_recheck")
    record_count = int(recheck.get("record_count"))
    records = _expect_list(recheck.get("records"), "high_precision_recheck.records")
    if record_count != len(records):
        raise ValueError("high_precision_recheck.record_count must equal records length")
    if bool(recheck.get("enabled")) != bool(records):
        raise ValueError("high_precision_recheck.enabled must match whether records are present")
    actual_orders: set[tuple[Any, ...]] = set()
    for i, record in enumerate(records):
        actual_orders.add(
            _validate_high_precision_recheck_record(
                record,
                n,
                f"high_precision_recheck.records[{i}]",
            )
        )
    if records and actual_orders != tie_orders:
        raise ValueError("high_precision_recheck.records must cover exactly the float64 tie set")
    limitations = _expect_list(recheck.get("limitations"), "high_precision_recheck.limitations")
    if not any("not certified intervals" in str(item) for item in limitations):
        raise ValueError("high_precision_recheck.limitations must disclaim interval certification")


def _validate_high_precision_recheck_consistency(method_value: Any, block_value: Any) -> None:
    method = _expect_mapping(method_value, "search_method.high_precision_recheck")
    block = _expect_mapping(block_value, "high_precision_recheck")
    for key in ("enabled", "selection", "backend", "digits"):
        if method.get(key) != block.get(key):
            raise ValueError(
                "search_method.high_precision_recheck must match high_precision_recheck"
            )


def _validate_high_precision_recheck_record(value: Any, n: int, name: str) -> tuple[Any, ...]:
    record = _expect_mapping(value, name)
    index_order = tuple(
        _parse_positive_int(item, f"{name}.index_order")
        for item in _expect_list(record.get("index_order"), f"{name}.index_order")
    )
    if len(index_order) != n:
        raise ValueError(f"{name}.index_order length must equal n")
    if canonicalize_index_order(index_order) != index_order:
        raise ValueError(f"{name}.index_order must be canonical")
    radius_order = tuple(
        _parse_positive_int(item, f"{name}.radius_order")
        for item in _expect_list(record.get("radius_order"), f"{name}.radius_order")
    )
    if radius_order != index_order_to_radius_order(index_order):
        raise ValueError(f"{name}.radius_order must match index_order")
    _validate_numeric_value(record.get("float64_R_full"), f"{name}.float64_R_full")
    for key in (
        "mpmath_R_full",
        "delta_mpmath_minus_float64",
        "feasibility_margin_at_mpmath_R",
    ):
        numeric = _validate_numeric_value(record.get(key), f"{name}.{key}")
        digits = int(numeric.get("source_precision_digits"))
        _validate_high_precision_digits(digits)
    if not isinstance(record.get("feasible_with_default_tol"), bool):
        raise ValueError(f"{name}.feasible_with_default_tol must be boolean")
    return index_order


def _validate_numeric_value(value: Any, name: str) -> Mapping[str, Any]:
    numeric = _expect_mapping(value, name)
    if numeric.get("encoding") != "decimal_string":
        raise ValueError(f"{name}.encoding must be decimal_string")
    _assert_decimal_string(numeric.get("decimal"), f"{name}.decimal")
    digits = int(numeric.get("source_precision_digits"))
    if digits < 1:
        raise ValueError(f"{name}.source_precision_digits must be positive")
    return numeric


def _expect_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be a mapping")
    return value


def _expect_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
    return value


if __name__ == "__main__":
    raise SystemExit(main())
