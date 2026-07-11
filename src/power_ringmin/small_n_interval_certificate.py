"""Aggregate local interval brackets into finite small-n certificates.

The first intended use is a tiny n=3 fixture: regenerate the canonical cyclic
order space, verify one local fixed-order interval bracket per canonical order,
and report the resulting finite global radius bracket.  This module does not
claim anything for all n.
"""

from __future__ import annotations

import argparse
from collections.abc import Mapping, Sequence
import copy
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import shlex
import sys
from typing import Any

import mpmath as mp

from power_ringmin.fixed_order_artifact import (
    EVIDENCE_CLASSIFICATIONS,
    UPSTREAM_RINGMIN_COMMIT,
    detect_repository_state,
)
from power_ringmin.geometry import quadratic_radii
from power_ringmin.interval_bracket_exporter import (
    DEFAULT_MAX_ATTEMPTS as DEFAULT_LOCAL_BRACKET_MAX_ATTEMPTS,
    FixedOrderIntervalBracketExport,
    build_fixed_order_interval_bracket_record,
)
from power_ringmin.interval_verifier import (
    MPMathIntervalAngularOracle,
    assert_fixed_order_interval_bracket_verified,
)
from power_ringmin.search_small_n import (
    CANONICALIZATION_RULE,
    ORDER_EQUIVALENCE,
    canonical_index_order_count,
    canonical_index_orders,
)

SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION = "power-ringmin.small_n_interval_certificate.v1"
ARTIFACT_TYPE = "small_n_interval_certificate"
EVIDENCE_SCOPE = "finite_global_small_n_interval_bracket"
DEFAULT_N3_FIXTURE_DIGITS = 80
DEFAULT_N3_FIXTURE_GUARD_DECIMAL = "1e-70"
DEFAULT_N3_FIXTURE_RADIUS_ETA = "1e-4"
DEFAULT_N4_FIXTURE_DIGITS = 80
DEFAULT_N4_FIXTURE_GUARD_DECIMAL = "1e-70"
DEFAULT_N4_FIXTURE_RADIUS_ETA = "1e-4"
DEFAULT_N4_MAX_CANONICAL_ORDERS = 3
DEFAULT_N4_LOCAL_MAX_ATTEMPTS = DEFAULT_LOCAL_BRACKET_MAX_ATTEMPTS
DEFAULT_SMALL_N_CERTIFICATE_DIGITS = 80
DEFAULT_SMALL_N_CERTIFICATE_GUARD_DECIMAL = "1e-70"
DEFAULT_SMALL_N_CERTIFICATE_RADIUS_ETA = "1e-4"
DEFAULT_SMALL_N_LOCAL_MAX_ATTEMPTS = DEFAULT_LOCAL_BRACKET_MAX_ATTEMPTS
N3_COMMAND_NAME = "power-ringmin-export-n3-interval-certificate"
N4_COMMAND_NAME = "power-ringmin-export-n4-interval-certificate"
SMALL_N_COMMAND_NAME = "power-ringmin-export-small-n-interval-certificate"
COMMAND_NAME = N3_COMMAND_NAME
LOCAL_VERIFIER_NAME = "power_ringmin.interval_verifier.verify_fixed_order_interval_bracket"
ORDER_SPACE_SOURCE = "power_ringmin.search_small_n.canonical_index_orders"
COVERAGE_RULE = "exactly_one_verified_local_bracket_per_canonical_order"
LOWER_BOUND_RULE = (
    "minimum verified lower endpoint across canonical orders; "
    "monotonicity of fixed-order feasibility in R extends each local "
    "lower infeasibility certificate down to that endpoint"
)
UPPER_BOUND_RULE = "minimum verified upper endpoint across canonical orders"


@dataclass(frozen=True)
class VerifiedLocalIntervalBracket:
    """One locally verified bracket used by a finite aggregate certificate."""

    index_order: tuple[int, ...]
    radius_order: tuple[int, ...]
    lower_radius: mp.mpf
    upper_radius: mp.mpf
    lower_radius_decimal: str
    upper_radius_decimal: str
    lower_negative_cycle_sum_upper: mp.mpf
    min_upper_witness_slack_lower: mp.mpf
    interval_digits: int
    record: dict[str, Any]


@dataclass(frozen=True)
class SmallNIntervalCertificate:
    """Validated view of a finite small-n interval certificate artifact."""

    data: dict[str, Any]

    @property
    def n(self) -> int:
        return int(self.data["instance"]["n"])

    @property
    def lower_radius_decimal(self) -> str:
        return str(self.data["result"]["global_lower_bound"]["radius_decimal"])

    @property
    def upper_radius_decimal(self) -> str:
        return str(self.data["result"]["global_upper_bound"]["radius_decimal"])

    @property
    def covered_canonical_count(self) -> int:
        return int(self.data["order_space"]["covered_canonical_count"])

    def to_dict(self) -> dict[str, Any]:
        """Return a deep copy suitable for JSON serialization."""
        return copy.deepcopy(self.data)


def build_n3_interval_certificate_fixture(
    *,
    digits: int = DEFAULT_N3_FIXTURE_DIGITS,
    guard_decimal: str | None = DEFAULT_N3_FIXTURE_GUARD_DECIMAL,
    radius_eta: str = DEFAULT_N3_FIXTURE_RADIUS_ETA,
    created_at_utc: str | None = None,
    command_summary: str = "programmatic call: build_n3_interval_certificate_fixture",
) -> dict[str, Any]:
    """Build the tiny global n=3 fixture from generated local brackets."""
    return build_bounded_small_n_interval_certificate_fixture(
        3,
        max_canonical_orders=1,
        digits=digits,
        guard_decimal=guard_decimal,
        radius_eta=radius_eta,
        local_max_attempts=DEFAULT_LOCAL_BRACKET_MAX_ATTEMPTS,
        created_at_utc=created_at_utc,
        command_summary=command_summary,
    )


def build_n4_interval_certificate_fixture(
    *,
    digits: int = DEFAULT_N4_FIXTURE_DIGITS,
    guard_decimal: str | None = DEFAULT_N4_FIXTURE_GUARD_DECIMAL,
    radius_eta: str = DEFAULT_N4_FIXTURE_RADIUS_ETA,
    max_canonical_orders: int = DEFAULT_N4_MAX_CANONICAL_ORDERS,
    local_max_attempts: int = DEFAULT_N4_LOCAL_MAX_ATTEMPTS,
    created_at_utc: str | None = None,
    command_summary: str = "programmatic call: build_n4_interval_certificate_fixture",
) -> dict[str, Any]:
    """Build the bounded finite n=4 certificate from generated local brackets."""
    return build_bounded_small_n_interval_certificate_fixture(
        4,
        max_canonical_orders=max_canonical_orders,
        digits=digits,
        guard_decimal=guard_decimal,
        radius_eta=radius_eta,
        local_max_attempts=local_max_attempts,
        created_at_utc=created_at_utc,
        command_summary=command_summary,
    )


def build_bounded_small_n_interval_certificate_fixture(
    n: int,
    *,
    max_canonical_orders: int,
    digits: int,
    guard_decimal: str | None,
    radius_eta: str,
    local_max_attempts: int,
    created_at_utc: str | None = None,
    command_summary: str = "programmatic call: build_bounded_small_n_interval_certificate_fixture",
) -> dict[str, Any]:
    """Build a small-n certificate only when the order-space bound admits it."""
    _validate_n(n)
    max_orders = _parse_positive_int(max_canonical_orders, "max_canonical_orders")
    max_attempts = _parse_positive_int(local_max_attempts, "local_max_attempts")
    expected_count = canonical_index_order_count(n)
    if expected_count > max_orders:
        raise ValueError(
            f"n={n} has {expected_count} canonical orders, "
            f"exceeding max_canonical_orders={max_orders}"
        )

    records = [
        build_fixed_order_interval_bracket_record(
            order,
            digits=digits,
            guard_decimal=guard_decimal,
            radius_eta=radius_eta,
            max_attempts=max_attempts,
            created_at_utc=created_at_utc,
        )
        for order in canonical_index_orders(n)
    ]
    return build_small_n_interval_certificate(
        records,
        n=n,
        created_at_utc=created_at_utc,
        command_summary=command_summary,
    )


def export_n3_interval_certificate_artifact(
    output: str | Path,
    *,
    digits: int = DEFAULT_N3_FIXTURE_DIGITS,
    guard_decimal: str | None = DEFAULT_N3_FIXTURE_GUARD_DECIMAL,
    radius_eta: str = DEFAULT_N3_FIXTURE_RADIUS_ETA,
    created_at_utc: str | None = None,
    argv_for_provenance: Sequence[str] | None = None,
) -> SmallNIntervalCertificate:
    """Build, verify, write, and reload the finite n=3 interval certificate."""
    output_path = Path(output)
    artifact = build_n3_interval_certificate_fixture(
        digits=digits,
        guard_decimal=guard_decimal,
        radius_eta=radius_eta,
        created_at_utc=created_at_utc,
        command_summary=_command_summary(
            argv_for_provenance,
            output=output_path,
            command_name=N3_COMMAND_NAME,
            programmatic_function="export_n3_interval_certificate_artifact",
        ),
    )
    dump_small_n_interval_certificate_artifact(artifact, output_path)
    return load_small_n_interval_certificate_artifact(output_path)


def export_n4_interval_certificate_artifact(
    output: str | Path,
    *,
    digits: int = DEFAULT_N4_FIXTURE_DIGITS,
    guard_decimal: str | None = DEFAULT_N4_FIXTURE_GUARD_DECIMAL,
    radius_eta: str = DEFAULT_N4_FIXTURE_RADIUS_ETA,
    max_canonical_orders: int = DEFAULT_N4_MAX_CANONICAL_ORDERS,
    local_max_attempts: int = DEFAULT_N4_LOCAL_MAX_ATTEMPTS,
    created_at_utc: str | None = None,
    argv_for_provenance: Sequence[str] | None = None,
) -> SmallNIntervalCertificate:
    """Build, verify, write, and reload the bounded finite n=4 certificate."""
    output_path = Path(output)
    artifact = build_n4_interval_certificate_fixture(
        digits=digits,
        guard_decimal=guard_decimal,
        radius_eta=radius_eta,
        max_canonical_orders=max_canonical_orders,
        local_max_attempts=local_max_attempts,
        created_at_utc=created_at_utc,
        command_summary=_command_summary(
            argv_for_provenance,
            output=output_path,
            command_name=N4_COMMAND_NAME,
            programmatic_function="export_n4_interval_certificate_artifact",
        ),
    )
    dump_small_n_interval_certificate_artifact(artifact, output_path)
    return load_small_n_interval_certificate_artifact(output_path)


def export_small_n_interval_certificate_artifact(
    output: str | Path,
    *,
    n: int,
    max_canonical_orders: int,
    digits: int = DEFAULT_SMALL_N_CERTIFICATE_DIGITS,
    guard_decimal: str | None = DEFAULT_SMALL_N_CERTIFICATE_GUARD_DECIMAL,
    radius_eta: str = DEFAULT_SMALL_N_CERTIFICATE_RADIUS_ETA,
    local_max_attempts: int = DEFAULT_SMALL_N_LOCAL_MAX_ATTEMPTS,
    created_at_utc: str | None = None,
    argv_for_provenance: Sequence[str] | None = None,
) -> SmallNIntervalCertificate:
    """Build, verify, write, and reload a bounded finite small-n certificate."""
    output_path = Path(output)
    artifact = build_bounded_small_n_interval_certificate_fixture(
        n,
        max_canonical_orders=max_canonical_orders,
        digits=digits,
        guard_decimal=guard_decimal,
        radius_eta=radius_eta,
        local_max_attempts=local_max_attempts,
        created_at_utc=created_at_utc,
        command_summary=_command_summary(
            argv_for_provenance,
            output=output_path,
            command_name=SMALL_N_COMMAND_NAME,
            programmatic_function="export_small_n_interval_certificate_artifact",
        ),
    )
    dump_small_n_interval_certificate_artifact(artifact, output_path)
    return load_small_n_interval_certificate_artifact(output_path)


def build_small_n_interval_certificate(
    local_bracket_records: Sequence[Mapping[str, Any] | FixedOrderIntervalBracketExport],
    *,
    n: int,
    created_at_utc: str | None = None,
    command_summary: str = "programmatic call: build_small_n_interval_certificate",
) -> dict[str, Any]:
    """Build and validate a finite small-n interval certificate artifact."""
    _validate_n(n)
    verified = _verify_and_cover_local_records(local_bracket_records, n=n)
    lower_source = min(verified, key=lambda item: (item.lower_radius, item.index_order))
    upper_source = min(verified, key=lambda item: (item.upper_radius, item.index_order))

    artifact: dict[str, Any] = {
        "schema_version": SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION,
        "artifact_type": ARTIFACT_TYPE,
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
            "n": n,
            "radius_sequence": {
                "kind": "explicit",
                "formula": "k^2",
                "index_base": 1,
                "indices": list(range(1, n + 1)),
                "radii": list(quadratic_radii(n)),
            },
        },
        "order_space": {
            "order_type": "cyclic",
            "equivalence": ORDER_EQUIVALENCE,
            "canonicalization_rule": CANONICALIZATION_RULE,
            "expected_canonical_count": canonical_index_order_count(n),
            "covered_canonical_count": len(verified),
            "coverage_rule": COVERAGE_RULE,
        },
        "aggregation_method": {
            "local_verifier": LOCAL_VERIFIER_NAME,
            "order_space_source": ORDER_SPACE_SOURCE,
            "lower_bound_rule": LOWER_BOUND_RULE,
            "upper_bound_rule": UPPER_BOUND_RULE,
        },
        "result": {
            "global_lower_bound": {
                "radius_decimal": lower_source.lower_radius_decimal,
                "encoding": "decimal_string",
                "included": False,
                "source_index_order": list(lower_source.index_order),
            },
            "global_upper_bound": {
                "radius_decimal": upper_source.upper_radius_decimal,
                "encoding": "decimal_string",
                "included": True,
                "source_index_order": list(upper_source.index_order),
            },
            "statement": (
                "For this finite n, the global optimum is bracketed between "
                "the strict lower endpoint and the feasible upper endpoint under "
                "the local interval-verifier semantics."
            ),
        },
        "local_bracket_summaries": [
            _local_summary(item, check_id=f"LB-{i:04d}") for i, item in enumerate(verified, start=1)
        ],
        "local_brackets": [copy.deepcopy(item.record) for item in verified],
        "provenance": _provenance_record(
            created_at_utc=created_at_utc,
            command_summary=command_summary,
            n=n,
            local_count=len(verified),
        ),
        "evidence": _evidence_record(n=n, local_count=len(verified)),
    }
    validate_small_n_interval_certificate_artifact(artifact)
    return artifact


def validate_small_n_interval_certificate_artifact(artifact: Mapping[str, Any]) -> None:
    """Raise ``ValueError`` if a finite small-n interval certificate is invalid."""
    source = _expect_mapping(artifact, "artifact")
    if source.get("schema_version") != SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION:
        raise ValueError("unsupported small-n interval certificate schema_version")
    if source.get("artifact_type") != ARTIFACT_TYPE:
        raise ValueError("unsupported small-n interval certificate artifact_type")

    problem = _expect_mapping(source.get("problem"), "problem")
    constraints = _expect_mapping(problem.get("constraints"), "problem.constraints")
    if problem.get("project") != "power-ringmin":
        raise ValueError("problem.project must be power-ringmin")
    if problem.get("radius_model") != "quadratic":
        raise ValueError("problem.radius_model must be quadratic")
    if problem.get("dimension") != 2:
        raise ValueError("problem.dimension must be 2")
    if constraints.get("central_external_tangency") is not True:
        raise ValueError("problem.constraints.central_external_tangency must be true")
    if constraints.get("peripheral_pairwise_disjoint_interiors") is not True:
        raise ValueError(
            "problem.constraints.peripheral_pairwise_disjoint_interiors must be true"
        )
    if constraints.get("all_pairs_checked") is not True:
        raise ValueError("problem.constraints.all_pairs_checked must be true")

    instance = _expect_mapping(source.get("instance"), "instance")
    n = _parse_positive_int(instance.get("n"), "instance.n")
    _validate_n(n)
    radius_sequence = _expect_mapping(instance.get("radius_sequence"), "instance.radius_sequence")
    if radius_sequence.get("kind") != "explicit":
        raise ValueError("instance.radius_sequence.kind must be explicit")
    if radius_sequence.get("formula") != "k^2":
        raise ValueError("instance.radius_sequence.formula must be k^2")
    if radius_sequence.get("index_base") != 1:
        raise ValueError("instance.radius_sequence.index_base must be 1")
    if tuple(radius_sequence.get("indices", [])) != tuple(range(1, n + 1)):
        raise ValueError("instance.radius_sequence.indices must equal 1..n")
    if tuple(radius_sequence.get("radii", [])) != quadratic_radii(n):
        raise ValueError("instance.radius_sequence.radii must equal k^2")

    order_space = _expect_mapping(source.get("order_space"), "order_space")
    expected_count = canonical_index_order_count(n)
    if order_space.get("order_type") != "cyclic":
        raise ValueError("order_space.order_type must be cyclic")
    if order_space.get("equivalence") != ORDER_EQUIVALENCE:
        raise ValueError("order_space.equivalence must be rotation_reflection")
    if order_space.get("canonicalization_rule") != CANONICALIZATION_RULE:
        raise ValueError("unsupported order_space.canonicalization_rule")
    if int(order_space.get("expected_canonical_count")) != expected_count:
        raise ValueError("order_space.expected_canonical_count is inconsistent with n")
    if int(order_space.get("covered_canonical_count")) != expected_count:
        raise ValueError("order_space.covered_canonical_count must equal expected count")
    if order_space.get("coverage_rule") != COVERAGE_RULE:
        raise ValueError("order_space.coverage_rule is unsupported")

    aggregation = _expect_mapping(source.get("aggregation_method"), "aggregation_method")
    if aggregation.get("local_verifier") != LOCAL_VERIFIER_NAME:
        raise ValueError("aggregation_method.local_verifier is unsupported")
    if aggregation.get("order_space_source") != ORDER_SPACE_SOURCE:
        raise ValueError("aggregation_method.order_space_source is unsupported")
    if aggregation.get("lower_bound_rule") != LOWER_BOUND_RULE:
        raise ValueError("aggregation_method.lower_bound_rule is unsupported")
    if aggregation.get("upper_bound_rule") != UPPER_BOUND_RULE:
        raise ValueError("aggregation_method.upper_bound_rule is unsupported")

    local_brackets = _expect_list(source.get("local_brackets"), "local_brackets")
    verified = _verify_and_cover_local_records(local_brackets, n=n)
    validation_digits = max(item.interval_digits for item in verified)
    with mp.workdps(max(mp.mp.dps, validation_digits)):
        summaries = _expect_list(source.get("local_bracket_summaries"), "local_bracket_summaries")
        if len(summaries) != len(verified):
            raise ValueError("local_bracket_summaries length must match local_brackets")
        _validate_local_summaries(summaries, verified)

        lower_source = min(verified, key=lambda item: (item.lower_radius, item.index_order))
        upper_source = min(verified, key=lambda item: (item.upper_radius, item.index_order))
        result = _expect_mapping(source.get("result"), "result")
        lower_bound = _expect_mapping(result.get("global_lower_bound"), "result.global_lower_bound")
        upper_bound = _expect_mapping(result.get("global_upper_bound"), "result.global_upper_bound")
        _validate_bound(lower_bound, lower_source, included=False, name="result.global_lower_bound")
        _validate_bound(upper_bound, upper_source, included=True, name="result.global_upper_bound")
        if mp.mpf(lower_bound["radius_decimal"]) > mp.mpf(upper_bound["radius_decimal"]):
            raise ValueError("global lower bound must not exceed global upper bound")

    _validate_provenance(source.get("provenance"))

    evidence = _expect_mapping(source.get("evidence"), "evidence")
    classification = evidence.get("classification")
    if classification not in EVIDENCE_CLASSIFICATIONS:
        raise ValueError("unsupported evidence.classification")
    if classification != "computer_certified_result":
        raise ValueError("small-n interval certificates must be computer_certified_result")
    claim = _expect_mapping(evidence.get("claim"), "evidence.claim")
    if claim.get("scope") != EVIDENCE_SCOPE:
        raise ValueError("evidence.claim.scope must be finite_global_small_n_interval_bracket")
    _validate_evidence_checks(_expect_list(evidence.get("checks"), "evidence.checks"), n=n)
    limitations = _expect_list(evidence.get("limitations"), "evidence.limitations")
    if not any("No theorem for all n" in str(item) for item in limitations):
        raise ValueError("evidence.limitations must disclaim theorem-for-all-n status")
    if not any("Interval backend provenance" in str(item) for item in limitations):
        raise ValueError("evidence.limitations must mention interval backend provenance")


def dump_small_n_interval_certificate_artifact(
    artifact: Mapping[str, Any] | SmallNIntervalCertificate,
    path: str | Path,
    *,
    indent: int = 2,
) -> None:
    """Validate and write a finite small-n interval certificate as JSON."""
    Path(path).write_text(
        dumps_small_n_interval_certificate_artifact(artifact, indent=indent),
        encoding="utf-8",
    )


def dumps_small_n_interval_certificate_artifact(
    artifact: Mapping[str, Any] | SmallNIntervalCertificate,
    *,
    indent: int = 2,
) -> str:
    """Validate and serialize a finite small-n interval certificate."""
    data = (
        artifact.to_dict()
        if isinstance(artifact, SmallNIntervalCertificate)
        else copy.deepcopy(dict(artifact))
    )
    validate_small_n_interval_certificate_artifact(data)
    return json.dumps(data, indent=indent, sort_keys=False) + "\n"


def load_small_n_interval_certificate_artifact(path: str | Path) -> SmallNIntervalCertificate:
    """Load and validate a finite small-n interval certificate from JSON."""
    return loads_small_n_interval_certificate_artifact(Path(path).read_text(encoding="utf-8"))


def loads_small_n_interval_certificate_artifact(text: str) -> SmallNIntervalCertificate:
    """Parse and validate a finite small-n interval certificate from JSON text."""
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("small-n interval certificate JSON must contain an object")
    validate_small_n_interval_certificate_artifact(payload)
    return SmallNIntervalCertificate(copy.deepcopy(payload))


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the finite n=3 certificate exporter."""
    parser = argparse.ArgumentParser(
        description="Export the checked finite n=3 interval certificate artifact.",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="path to write the finite n=3 interval certificate JSON artifact",
    )
    parser.add_argument(
        "--digits",
        type=int,
        default=DEFAULT_N3_FIXTURE_DIGITS,
        help=f"mpmath working precision digits (default: {DEFAULT_N3_FIXTURE_DIGITS})",
    )
    parser.add_argument(
        "--guard-decimal",
        default=DEFAULT_N3_FIXTURE_GUARD_DECIMAL,
        help=(
            "nonnegative guard added to interval endpoints "
            f"(default: {DEFAULT_N3_FIXTURE_GUARD_DECIMAL})"
        ),
    )
    parser.add_argument(
        "--radius-eta",
        default=DEFAULT_N3_FIXTURE_RADIUS_ETA,
        help=(
            "positive radius bracket offset for the embedded local bracket "
            f"(default: {DEFAULT_N3_FIXTURE_RADIUS_ETA})"
        ),
    )
    parser.add_argument(
        "--created-at-utc",
        help="optional UTC timestamp to record in artifact provenance",
    )
    return parser


def build_n4_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the bounded finite n=4 exporter."""
    parser = argparse.ArgumentParser(
        description="Export the checked finite n=4 interval certificate artifact.",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="path to write the finite n=4 interval certificate JSON artifact",
    )
    parser.add_argument(
        "--digits",
        type=int,
        default=DEFAULT_N4_FIXTURE_DIGITS,
        help=f"mpmath working precision digits (default: {DEFAULT_N4_FIXTURE_DIGITS})",
    )
    parser.add_argument(
        "--guard-decimal",
        default=DEFAULT_N4_FIXTURE_GUARD_DECIMAL,
        help=(
            "nonnegative guard added to interval endpoints "
            f"(default: {DEFAULT_N4_FIXTURE_GUARD_DECIMAL})"
        ),
    )
    parser.add_argument(
        "--radius-eta",
        default=DEFAULT_N4_FIXTURE_RADIUS_ETA,
        help=(
            "positive radius bracket offset for each embedded local bracket "
            f"(default: {DEFAULT_N4_FIXTURE_RADIUS_ETA})"
        ),
    )
    parser.add_argument(
        "--max-canonical-orders",
        type=int,
        default=DEFAULT_N4_MAX_CANONICAL_ORDERS,
        help=(
            "hard ceiling on regenerated canonical orders "
            f"(default: {DEFAULT_N4_MAX_CANONICAL_ORDERS})"
        ),
    )
    parser.add_argument(
        "--local-max-attempts",
        type=int,
        default=DEFAULT_N4_LOCAL_MAX_ATTEMPTS,
        help=(
            "maximum bracket-widening attempts per local fixed order "
            f"(default: {DEFAULT_N4_LOCAL_MAX_ATTEMPTS})"
        ),
    )
    parser.add_argument(
        "--created-at-utc",
        help="optional UTC timestamp to record in artifact provenance",
    )
    return parser


def build_small_n_parser() -> argparse.ArgumentParser:
    """Build the parser for bounded finite small-n certificate production."""
    parser = argparse.ArgumentParser(
        description=(
            "Export a bounded finite small-n interval certificate artifact, "
            "or dry-run the canonical-order preflight."
        ),
    )
    parser.add_argument("--n", required=True, type=int, help="quadratic instance size, minimum 3")
    parser.add_argument(
        "--max-canonical-orders",
        required=True,
        type=int,
        help="explicit hard ceiling on regenerated canonical orders",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="path to write the finite small-n interval certificate JSON artifact",
    )
    parser.add_argument(
        "--digits",
        type=int,
        default=DEFAULT_SMALL_N_CERTIFICATE_DIGITS,
        help=f"mpmath working precision digits (default: {DEFAULT_SMALL_N_CERTIFICATE_DIGITS})",
    )
    parser.add_argument(
        "--guard-decimal",
        default=DEFAULT_SMALL_N_CERTIFICATE_GUARD_DECIMAL,
        help=(
            "nonnegative guard added to interval endpoints "
            f"(default: {DEFAULT_SMALL_N_CERTIFICATE_GUARD_DECIMAL})"
        ),
    )
    parser.add_argument(
        "--radius-eta",
        default=DEFAULT_SMALL_N_CERTIFICATE_RADIUS_ETA,
        help=(
            "positive radius bracket offset for each embedded local bracket "
            f"(default: {DEFAULT_SMALL_N_CERTIFICATE_RADIUS_ETA})"
        ),
    )
    parser.add_argument(
        "--local-max-attempts",
        type=int,
        default=DEFAULT_SMALL_N_LOCAL_MAX_ATTEMPTS,
        help=(
            "maximum bracket-widening attempts per local fixed order "
            f"(default: {DEFAULT_SMALL_N_LOCAL_MAX_ATTEMPTS})"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only report canonical-order count and whether the bound permits generation",
    )
    parser.add_argument(
        "--created-at-utc",
        help="optional UTC timestamp to record in artifact provenance",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the finite n=3 interval certificate exporter CLI."""
    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)

    try:
        certificate = export_n3_interval_certificate_artifact(
            args.output,
            digits=args.digits,
            guard_decimal=args.guard_decimal,
            radius_eta=args.radius_eta,
            created_at_utc=args.created_at_utc,
            argv_for_provenance=raw_argv,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(
        f"wrote {args.output} n={certificate.n} "
        f"bracket=({certificate.lower_radius_decimal}, {certificate.upper_radius_decimal}] "
        "classification=computer_certified_result "
        f"covered={certificate.covered_canonical_count}"
    )
    return 0


def main_n4(argv: Sequence[str] | None = None) -> int:
    """Run the bounded finite n=4 interval certificate exporter CLI."""
    parser = build_n4_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)

    try:
        certificate = export_n4_interval_certificate_artifact(
            args.output,
            digits=args.digits,
            guard_decimal=args.guard_decimal,
            radius_eta=args.radius_eta,
            max_canonical_orders=args.max_canonical_orders,
            local_max_attempts=args.local_max_attempts,
            created_at_utc=args.created_at_utc,
            argv_for_provenance=raw_argv,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(
        f"wrote {args.output} n={certificate.n} "
        f"bracket=({certificate.lower_radius_decimal}, {certificate.upper_radius_decimal}] "
        "classification=computer_certified_result "
        f"covered={certificate.covered_canonical_count}"
    )
    return 0


def main_small_n(argv: Sequence[str] | None = None) -> int:
    """Run the bounded finite small-n interval certificate exporter CLI."""
    parser = build_small_n_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)

    try:
        _validate_n(args.n)
        max_orders = _parse_positive_int(args.max_canonical_orders, "max_canonical_orders")
        expected_count = canonical_index_order_count(args.n)
        generation_allowed = expected_count <= max_orders
        if args.dry_run:
            print(
                f"preflight n={args.n} canonical_orders={expected_count} "
                f"max_canonical_orders={max_orders} "
                f"generation_allowed={str(generation_allowed).lower()}"
            )
            return 0
        if args.output is None:
            parser.error("--output is required unless --dry-run is set")
        certificate = export_small_n_interval_certificate_artifact(
            args.output,
            n=args.n,
            max_canonical_orders=max_orders,
            digits=args.digits,
            guard_decimal=args.guard_decimal,
            radius_eta=args.radius_eta,
            local_max_attempts=args.local_max_attempts,
            created_at_utc=args.created_at_utc,
            argv_for_provenance=raw_argv,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(
        f"wrote {args.output} n={certificate.n} "
        f"bracket=({certificate.lower_radius_decimal}, {certificate.upper_radius_decimal}] "
        "classification=computer_certified_result "
        f"covered={certificate.covered_canonical_count}"
    )
    return 0


def _verify_and_cover_local_records(
    local_bracket_records: Sequence[Mapping[str, Any] | FixedOrderIntervalBracketExport],
    *,
    n: int,
) -> tuple[VerifiedLocalIntervalBracket, ...]:
    expected_orders = tuple(canonical_index_orders(n))
    expected_set = set(expected_orders)
    by_order: dict[tuple[int, ...], VerifiedLocalIntervalBracket] = {}

    for raw_record in local_bracket_records:
        record = _coerce_local_record(raw_record)
        oracle = _oracle_from_local_record(record)
        result = assert_fixed_order_interval_bracket_verified(record, oracle=oracle)
        if len(result.index_order) != n:
            raise ValueError(
                f"local bracket order length {len(result.index_order)} does not match n={n}"
            )
        if result.index_order not in expected_set:
            raise ValueError(f"local bracket index_order is not in the canonical n={n} order space")
        if result.index_order in by_order:
            raise ValueError(f"duplicate local bracket for canonical order {result.index_order}")
        by_order[result.index_order] = VerifiedLocalIntervalBracket(
            index_order=result.index_order,
            radius_order=result.radius_order,
            lower_radius=result.lower_radius,
            upper_radius=result.upper_radius,
            lower_radius_decimal=str(record["lower_radius_decimal"]),
            upper_radius_decimal=str(record["upper_radius_decimal"]),
            lower_negative_cycle_sum_upper=result.lower_negative_cycle_sum_upper,
            min_upper_witness_slack_lower=result.min_upper_witness_slack_lower,
            interval_digits=oracle.digits,
            record=record,
        )

    missing = [order for order in expected_orders if order not in by_order]
    extra = [order for order in by_order if order not in expected_set]
    if missing or extra:
        raise ValueError(
            "local bracket coverage mismatch: "
            f"missing={missing or []}, extra={extra or []}"
        )
    return tuple(by_order[order] for order in expected_orders)


def _coerce_local_record(
    record: Mapping[str, Any] | FixedOrderIntervalBracketExport,
) -> dict[str, Any]:
    if isinstance(record, FixedOrderIntervalBracketExport):
        return record.to_dict()
    if not isinstance(record, Mapping):
        raise ValueError("local bracket records must be mappings")
    return copy.deepcopy(dict(record))


def _oracle_from_local_record(record: Mapping[str, Any]) -> MPMathIntervalAngularOracle:
    metadata = _expect_mapping(record.get("theta_interval_backend"), "theta_interval_backend")
    if metadata.get("backend") != "mpmath_iv_guarded_atan2_v1":
        raise ValueError("only mpmath_iv_guarded_atan2_v1 local records are supported")
    digits = _parse_positive_int(metadata.get("precision_digits"), "theta_interval_backend.precision_digits")
    if digits < 30:
        raise ValueError("theta_interval_backend.precision_digits must be at least 30")
    guard = metadata.get("guard_decimal")
    if guard is not None and not isinstance(guard, str):
        raise ValueError("theta_interval_backend.guard_decimal must be a string")
    return MPMathIntervalAngularOracle(digits=digits, guard_decimal=guard)


def _local_summary(item: VerifiedLocalIntervalBracket, *, check_id: str) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "index_order": list(item.index_order),
        "radius_order": list(item.radius_order),
        "lower_radius_decimal": item.lower_radius_decimal,
        "upper_radius_decimal": item.upper_radius_decimal,
        "lower_negative_cycle_sum_upper_decimal": _decimal_string(
            item.lower_negative_cycle_sum_upper,
            digits=item.interval_digits,
        ),
        "min_upper_witness_slack_lower_decimal": _decimal_string(
            item.min_upper_witness_slack_lower,
            digits=item.interval_digits,
        ),
        "result": "pass",
    }


def _validate_local_summaries(
    summaries: Sequence[Any],
    verified: Sequence[VerifiedLocalIntervalBracket],
) -> None:
    for i, (summary, item) in enumerate(zip(summaries, verified, strict=True)):
        source = _expect_mapping(summary, f"local_bracket_summaries[{i}]")
        expected_check_id = f"LB-{i + 1:04d}"
        if source.get("check_id") != expected_check_id:
            raise ValueError(f"local_bracket_summaries[{i}].check_id must be {expected_check_id}")
        if tuple(source.get("index_order", [])) != item.index_order:
            raise ValueError(f"local_bracket_summaries[{i}].index_order mismatch")
        if tuple(source.get("radius_order", [])) != item.radius_order:
            raise ValueError(f"local_bracket_summaries[{i}].radius_order mismatch")
        if mp.mpf(str(source.get("lower_radius_decimal"))) != item.lower_radius:
            raise ValueError(f"local_bracket_summaries[{i}].lower_radius_decimal mismatch")
        if mp.mpf(str(source.get("upper_radius_decimal"))) != item.upper_radius:
            raise ValueError(f"local_bracket_summaries[{i}].upper_radius_decimal mismatch")
        if mp.mpf(str(source.get("lower_negative_cycle_sum_upper_decimal"))) != mp.mpf(
            _decimal_string(item.lower_negative_cycle_sum_upper, digits=item.interval_digits)
        ):
            raise ValueError(
                f"local_bracket_summaries[{i}].lower_negative_cycle_sum_upper_decimal mismatch"
            )
        if mp.mpf(str(source.get("min_upper_witness_slack_lower_decimal"))) != mp.mpf(
            _decimal_string(item.min_upper_witness_slack_lower, digits=item.interval_digits)
        ):
            raise ValueError(
                f"local_bracket_summaries[{i}].min_upper_witness_slack_lower_decimal mismatch"
            )
        if source.get("result") != "pass":
            raise ValueError(f"local_bracket_summaries[{i}].result must be pass")


def _validate_bound(
    bound: Mapping[str, Any],
    source: VerifiedLocalIntervalBracket,
    *,
    included: bool,
    name: str,
) -> None:
    if bound.get("encoding") != "decimal_string":
        raise ValueError(f"{name}.encoding must be decimal_string")
    if bound.get("included") is not included:
        raise ValueError(f"{name}.included has wrong value")
    decimal = str(bound.get("radius_decimal"))
    if mp.mpf(decimal) != (source.lower_radius if not included else source.upper_radius):
        raise ValueError(f"{name}.radius_decimal is inconsistent with local brackets")
    if tuple(bound.get("source_index_order", [])) != source.index_order:
        raise ValueError(f"{name}.source_index_order mismatch")


def _provenance_record(
    *,
    created_at_utc: str | None,
    command_summary: str,
    n: int,
    local_count: int,
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
                "role": "interval arithmetic verification backend",
            },
            {
                "name": "power-ringmin",
                "version": "0.1.0",
                "role": "small-n interval certificate aggregator",
            },
        ],
        "source_files": [
            {
                "path": "src/power_ringmin/small_n_interval_certificate.py",
                "role": "finite small-n interval certificate aggregation",
            },
            {
                "path": "src/power_ringmin/search_small_n.py",
                "role": "canonical cyclic index-order regeneration",
            },
            {
                "path": "src/power_ringmin/interval_verifier.py",
                "role": "local fixed-order interval bracket verifier",
            },
            {
                "path": "src/power_ringmin/interval_bracket_exporter.py",
                "role": "local fixed-order interval bracket generator/exporter",
            },
            {
                "path": "src/power_ringmin/highprec.py",
                "role": "high-precision fixed-order STN proposal",
                "upstream_ringmin_commit": UPSTREAM_RINGMIN_COMMIT,
            },
        ],
        "commands": [
            {
                "command": command_summary,
                "cwd": str(Path.cwd()),
                "result": "pass",
                "output_summary": (
                    f"Built finite n={n} interval certificate from {local_count} "
                    "verified local bracket record(s)."
                ),
            }
        ],
        "randomness": {
            "used": False,
            "seeds": [],
        },
    }


def _evidence_record(*, n: int, local_count: int) -> dict[str, Any]:
    return {
        "classification": "computer_certified_result",
        "claim": {
            "scope": EVIDENCE_SCOPE,
            "statement": (
                f"This finite n={n} artifact verifies exactly one local "
                "fixed-order interval bracket for every canonical cyclic order "
                "and aggregates those brackets into a global finite-n radius "
                "bracket. It is not a theorem for all n."
            ),
        },
        "checks": [
            {
                "check_id": "EV-001",
                "classification": "verified_fact",
                "method": "independent canonical index-order regeneration",
                "result": "pass",
                "output_summary": (
                    f"Regenerated {canonical_index_order_count(n)} canonical "
                    f"orders for n={n} under {ORDER_EQUIVALENCE} equivalence."
                ),
                "limitations": "Finite order-space enumeration only.",
            },
            {
                "check_id": "EV-002",
                "classification": "computer_certified_result",
                "method": "local fixed-order interval bracket verification",
                "result": "pass",
                "output_summary": (
                    f"Verified {local_count} local bracket record(s), one per "
                    "canonical order."
                ),
                "limitations": "Depends on the documented guarded mpmath.iv interval backend contract.",
            },
            {
                "check_id": "EV-003",
                "classification": "computer_certified_result",
                "method": "finite global bracket aggregation",
                "result": "pass",
                "output_summary": (
                    "Computed the strict global lower endpoint and feasible "
                    "global upper endpoint from verified local brackets."
                ),
                "limitations": "Finite n only; no asymptotic or all-n theorem.",
            },
        ],
        "limitations": [
            "Finite n only.",
            "No theorem for all n.",
            "No asymptotic claim.",
            "Interval backend provenance remains a future production review item.",
            "The lower-bound aggregation relies on fixed-order feasibility monotonicity in R.",
        ],
    }


def _validate_provenance(value: Any) -> None:
    provenance = _expect_mapping(value, "provenance")
    if not isinstance(provenance.get("created_at_utc"), str) or not provenance["created_at_utc"]:
        raise ValueError("provenance.created_at_utc must be a non-empty string")
    repository = _expect_mapping(provenance.get("repository"), "provenance.repository")
    if repository.get("name") != "power-ringmin":
        raise ValueError("provenance.repository.name must be power-ringmin")
    git_commit = repository.get("git_commit")
    if git_commit is not None and (
        not isinstance(git_commit, str) or len(git_commit) != 40
    ):
        raise ValueError("provenance.repository.git_commit must be null or a 40-character string")
    if not isinstance(repository.get("git_dirty"), bool):
        raise ValueError("provenance.repository.git_dirty must be boolean")
    if not _expect_list(provenance.get("software"), "provenance.software"):
        raise ValueError("provenance.software must be non-empty")
    if not _expect_list(provenance.get("source_files"), "provenance.source_files"):
        raise ValueError("provenance.source_files must be non-empty")
    if not _expect_list(provenance.get("commands"), "provenance.commands"):
        raise ValueError("provenance.commands must be non-empty")
    randomness = _expect_mapping(provenance.get("randomness"), "provenance.randomness")
    if randomness.get("used") is not False:
        raise ValueError("provenance.randomness.used must be false")
    if not isinstance(randomness.get("seeds"), list):
        raise ValueError("provenance.randomness.seeds must be a list")


def _validate_evidence_checks(checks: Sequence[Any], *, n: int) -> None:
    expected = (
        ("EV-001", "verified_fact", "independent canonical index-order regeneration"),
        ("EV-002", "computer_certified_result", "local fixed-order interval bracket verification"),
        ("EV-003", "computer_certified_result", "finite global bracket aggregation"),
    )
    if len(checks) != len(expected):
        raise ValueError("evidence.checks must contain the three required checks")
    for i, (check, (check_id, classification, method)) in enumerate(zip(checks, expected, strict=True)):
        source = _expect_mapping(check, f"evidence.checks[{i}]")
        if source.get("check_id") != check_id:
            raise ValueError(f"evidence.checks[{i}].check_id must be {check_id}")
        if source.get("classification") != classification:
            raise ValueError(f"evidence.checks[{i}].classification must be {classification}")
        if source.get("method") != method:
            raise ValueError(f"evidence.checks[{i}].method must be {method}")
        if source.get("result") != "pass":
            raise ValueError(f"evidence.checks[{i}].result must be pass")
    expected_count = canonical_index_order_count(n)
    first_summary = str(_expect_mapping(checks[0], "evidence.checks[0]").get("output_summary", ""))
    if str(expected_count) not in first_summary:
        raise ValueError("evidence.checks[0].output_summary must mention the canonical count")


def _command_summary(
    argv: Sequence[str] | None,
    *,
    output: Path,
    command_name: str,
    programmatic_function: str,
) -> str:
    if argv:
        return command_name + " " + shlex.join(str(item) for item in argv)
    return f"programmatic call: {programmatic_function}(output={str(output)!r})"


def _validate_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError(f"n must be an integer at least 3, got {n!r}")


def _parse_positive_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a positive integer")
    if isinstance(value, int):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = int(value, 10)
        except ValueError as exc:
            raise ValueError(f"{name} must be a positive integer") from exc
        if str(parsed) != value:
            raise ValueError(f"{name} must be a positive integer")
    else:
        raise ValueError(f"{name} must be a positive integer")
    if parsed <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return parsed


def _decimal_string(value: Any, *, digits: int) -> str:
    with mp.workdps(max(mp.mp.dps, digits)):
        text = mp.nstr(mp.mpf(value), n=digits)
    return text[1:] if text.startswith("+") else text


def _expect_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be a mapping")
    return value


def _expect_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
    return value


def _created_at_utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


__all__ = [
    "ARTIFACT_TYPE",
    "COMMAND_NAME",
    "DEFAULT_N4_FIXTURE_DIGITS",
    "DEFAULT_N4_FIXTURE_GUARD_DECIMAL",
    "DEFAULT_N4_FIXTURE_RADIUS_ETA",
    "DEFAULT_N4_LOCAL_MAX_ATTEMPTS",
    "DEFAULT_N4_MAX_CANONICAL_ORDERS",
    "DEFAULT_N3_FIXTURE_DIGITS",
    "DEFAULT_N3_FIXTURE_GUARD_DECIMAL",
    "DEFAULT_N3_FIXTURE_RADIUS_ETA",
    "DEFAULT_SMALL_N_CERTIFICATE_DIGITS",
    "DEFAULT_SMALL_N_CERTIFICATE_GUARD_DECIMAL",
    "DEFAULT_SMALL_N_CERTIFICATE_RADIUS_ETA",
    "DEFAULT_SMALL_N_LOCAL_MAX_ATTEMPTS",
    "EVIDENCE_SCOPE",
    "N3_COMMAND_NAME",
    "N4_COMMAND_NAME",
    "SMALL_N_COMMAND_NAME",
    "SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION",
    "SmallNIntervalCertificate",
    "VerifiedLocalIntervalBracket",
    "build_bounded_small_n_interval_certificate_fixture",
    "build_parser",
    "build_n3_interval_certificate_fixture",
    "build_n4_interval_certificate_fixture",
    "build_small_n_parser",
    "build_small_n_interval_certificate",
    "dump_small_n_interval_certificate_artifact",
    "dumps_small_n_interval_certificate_artifact",
    "export_n3_interval_certificate_artifact",
    "export_n4_interval_certificate_artifact",
    "export_small_n_interval_certificate_artifact",
    "load_small_n_interval_certificate_artifact",
    "loads_small_n_interval_certificate_artifact",
    "main",
    "main_n4",
    "main_small_n",
    "validate_small_n_interval_certificate_artifact",
]


if __name__ == "__main__":
    raise SystemExit(main())
