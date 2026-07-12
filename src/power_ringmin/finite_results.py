"""Derived finite-results summary artifacts for checked small-n certificates.

This module reads checked finite interval certificate artifacts through the
existing semantic loader and derives candidate-set information, exclusion gaps,
serialized bracket groups, and finite-n ratio diagnostics.  The summary is a
separate derived artifact contract; it does not change the primary
``small_n_interval_certificate`` evidence schema.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
import copy
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path
import platform
import re
import shlex
import sys
from typing import Any

import mpmath as mp

from power_ringmin.fixed_order_artifact import (
    EVIDENCE_CLASSIFICATIONS,
    detect_repository_state,
)
from power_ringmin.small_n_interval_certificate import (
    ARTIFACT_TYPE as SMALL_N_INTERVAL_CERTIFICATE_ARTIFACT_TYPE,
    EVIDENCE_SCOPE,
    SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION,
    load_small_n_interval_certificate_artifact,
)

FINITE_RESULTS_SUMMARY_SCHEMA_VERSION = "power-ringmin.finite_results_summary.v1"
SUMMARY_FORMAT_VERSION = FINITE_RESULTS_SUMMARY_SCHEMA_VERSION
FINITE_RESULTS_SUMMARY_ARTIFACT_TYPE = "finite_results_summary"
COMMAND_NAME = "power-ringmin-analyze-finite-results"
DEFAULT_CHECKED_ARTIFACT_PATHS = (
    Path("examples/small_n_interval_certificate_n3.json"),
    Path("examples/small_n_interval_certificate_n4.json"),
    Path("examples/small_n_interval_certificate_n5.json"),
    Path("examples/small_n_interval_certificate_n6.json"),
)
ASYMPTOTIC_REFERENCE = "n^3/(6*pi)"
ASYMPTOTIC_DIAGNOSTIC_CLASSIFICATION = "numerical_observation"
DECIMAL_STRING_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class FiniteResultsSummary:
    """Validated view of a derived finite-results summary artifact."""

    data: dict[str, Any]

    @property
    def n_values(self) -> tuple[int, ...]:
        return tuple(int(item) for item in self.data["summary_scope"]["n_values"])

    @property
    def source_certificate_count(self) -> int:
        return int(self.data["source_certificate_count"])

    def to_dict(self) -> dict[str, Any]:
        """Return a deep copy suitable for JSON serialization."""
        return copy.deepcopy(self.data)


@dataclass(frozen=True)
class _LocalBracket:
    index_order: tuple[int, ...]
    radius_order: tuple[int, ...]
    lower_decimal: str
    upper_decimal: str
    lower: Decimal
    upper: Decimal
    source_check_id: str


def build_finite_results_summary(
    artifact_paths: Sequence[str | Path] | None = None,
    *,
    include_additive_differences: bool = True,
    created_at_utc: str | None = None,
    command_summary: str = "programmatic call: build_finite_results_summary",
) -> dict[str, Any]:
    """Build the v1 derived summary from checked small-n certificates."""

    paths = tuple(Path(path) for path in (artifact_paths or DEFAULT_CHECKED_ARTIFACT_PATHS))
    if not paths:
        raise ValueError("at least one checked artifact path is required")

    source_records: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []
    for path in paths:
        source_record, result = _analyze_source_certificate(
            path,
            include_additive_differences=include_additive_differences,
        )
        source_records.append(source_record)
        results.append(result)

    source_records.sort(key=lambda item: (item["n"], item["path"]))
    results.sort(key=lambda item: (item["n"], item["source_certificate"]["path"]))
    n_values = [int(result["n"]) for result in results]
    if len(set(n_values)) != len(n_values):
        raise ValueError(f"duplicate finite-result summary n values: {n_values!r}")

    summary: dict[str, Any] = {
        "schema_version": FINITE_RESULTS_SUMMARY_SCHEMA_VERSION,
        "artifact_type": FINITE_RESULTS_SUMMARY_ARTIFACT_TYPE,
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
        "summary_scope": {
            "n_values": n_values,
            "source_certificate_schema_version": SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION,
            "source_certificate_artifact_type": SMALL_N_INTERVAL_CERTIFICATE_ARTIFACT_TYPE,
            "source_evidence_scope": EVIDENCE_SCOPE,
        },
        "source_certificate_count": len(source_records),
        "definitions": _definitions_record(),
        "evidence_classification_by_category": _classification_record(),
        "source_certificates": source_records,
        "results": results,
        "cross_n_analysis": _cross_n_analysis(results),
        "provenance": _provenance_record(
            created_at_utc=created_at_utc,
            command_summary=command_summary,
            source_count=len(source_records),
        ),
        "limitations": _limitations_record(n_values),
    }
    validate_finite_results_summary_artifact(summary)
    return summary


def analyze_checked_finite_results(
    artifact_paths: Sequence[str | Path] | None = None,
    *,
    include_additive_differences: bool = True,
) -> dict[str, Any]:
    """Analyze checked certificates and return a v1 summary artifact."""

    return build_finite_results_summary(
        artifact_paths,
        include_additive_differences=include_additive_differences,
    )


def analyze_finite_result_artifact(
    path: str | Path,
    *,
    include_additive_differences: bool = True,
) -> dict[str, Any]:
    """Load one checked finite certificate and derive its per-n summary."""

    return _analyze_source_certificate(
        Path(path),
        include_additive_differences=include_additive_differences,
    )[1]


def validate_finite_results_summary_artifact(
    artifact: Mapping[str, Any],
    *,
    base_dir: str | Path | None = None,
) -> None:
    """Raise ``ValueError`` if a v1 finite-results summary is invalid or stale."""

    source = _expect_mapping(artifact, "artifact")
    if source.get("schema_version") != FINITE_RESULTS_SUMMARY_SCHEMA_VERSION:
        raise ValueError("unsupported finite-results summary schema_version")
    if source.get("artifact_type") != FINITE_RESULTS_SUMMARY_ARTIFACT_TYPE:
        raise ValueError("unsupported finite-results summary artifact_type")

    _validate_problem(source.get("problem"))
    scope = _expect_mapping(source.get("summary_scope"), "summary_scope")
    if scope.get("source_certificate_schema_version") != SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION:
        raise ValueError("summary_scope.source_certificate_schema_version is unsupported")
    if scope.get("source_certificate_artifact_type") != SMALL_N_INTERVAL_CERTIFICATE_ARTIFACT_TYPE:
        raise ValueError("summary_scope.source_certificate_artifact_type is unsupported")
    if scope.get("source_evidence_scope") != EVIDENCE_SCOPE:
        raise ValueError("summary_scope.source_evidence_scope is unsupported")
    n_values = _expect_list(scope.get("n_values"), "summary_scope.n_values")
    if not n_values or any(isinstance(item, bool) or not isinstance(item, int) or item < 3 for item in n_values):
        raise ValueError("summary_scope.n_values must contain n values at least 3")

    source_certificates = _expect_list(source.get("source_certificates"), "source_certificates")
    results = _expect_list(source.get("results"), "results")
    source_count = _parse_nonnegative_int(source.get("source_certificate_count"), "source_certificate_count")
    if source_count != len(source_certificates) or source_count != len(results):
        raise ValueError("source certificate count must match source_certificates and results")
    if n_values != [int(_expect_mapping(result, "result").get("n")) for result in results]:
        raise ValueError("summary_scope.n_values must match results")

    _validate_definitions(source.get("definitions"))
    _validate_classification_record(source.get("evidence_classification_by_category"))
    _validate_provenance(source.get("provenance"))
    _validate_limitations(source.get("limitations"))
    _reject_forbidden_claim_phrases(source)

    expected_sources: list[dict[str, Any]] = []
    expected_results: list[dict[str, Any]] = []
    root = Path.cwd() if base_dir is None else Path(base_dir)
    for raw_source in source_certificates:
        certificate_record = _validate_source_certificate_record(raw_source)
        path = _resolve_source_path(str(certificate_record["path"]), root)
        expected_source, expected_result = _analyze_source_certificate(
            path,
            include_additive_differences=_result_uses_additive_differences(results),
        )
        expected_sources.append(expected_source)
        expected_results.append(expected_result)

    expected_sources.sort(key=lambda item: (item["n"], item["path"]))
    expected_results.sort(key=lambda item: (item["n"], item["source_certificate"]["path"]))
    if source_certificates != expected_sources:
        raise ValueError("source_certificates are stale or inconsistent with source artifacts")
    if results != expected_results:
        raise ValueError("results are stale or inconsistent with source artifacts")
    if source.get("cross_n_analysis") != _cross_n_analysis(expected_results):
        raise ValueError("cross_n_analysis is stale or inconsistent with results")


def dump_finite_results_summary(
    summary: Mapping[str, Any] | FiniteResultsSummary,
    path: str | Path,
    *,
    indent: int = 2,
) -> None:
    """Validate and write a v1 finite-results summary JSON artifact."""

    Path(path).write_text(dumps_finite_results_summary(summary, indent=indent), encoding="utf-8")


def dumps_finite_results_summary(
    summary: Mapping[str, Any] | FiniteResultsSummary,
    *,
    indent: int = 2,
) -> str:
    """Validate and serialize a v1 finite-results summary deterministically."""

    data = summary.to_dict() if isinstance(summary, FiniteResultsSummary) else copy.deepcopy(dict(summary))
    validate_finite_results_summary_artifact(data)
    return json.dumps(data, indent=indent, sort_keys=False) + "\n"


def load_finite_results_summary(
    path: str | Path,
    *,
    base_dir: str | Path | None = None,
) -> FiniteResultsSummary:
    """Load and semantically validate a v1 finite-results summary artifact."""

    summary_path = Path(path)
    root = base_dir if base_dir is not None else Path.cwd()
    return loads_finite_results_summary(summary_path.read_text(encoding="utf-8"), base_dir=root)


def loads_finite_results_summary(
    text: str,
    *,
    base_dir: str | Path | None = None,
) -> FiniteResultsSummary:
    """Parse and semantically validate a v1 finite-results summary artifact."""

    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("finite-results summary JSON must contain an object")
    validate_finite_results_summary_artifact(payload, base_dir=base_dir)
    return FiniteResultsSummary(copy.deepcopy(payload))


dump_finite_results_summary_artifact = dump_finite_results_summary
dumps_finite_results_summary_artifact = dumps_finite_results_summary
load_finite_results_summary_artifact = load_finite_results_summary
loads_finite_results_summary_artifact = loads_finite_results_summary


def format_finite_results_markdown(summary: Mapping[str, Any] | FiniteResultsSummary) -> str:
    """Render a deterministic Markdown table from a finite-results summary."""

    data = summary.to_dict() if isinstance(summary, FiniteResultsSummary) else summary
    lines = [
        "# Derived finite results summary",
        "",
        "This summary is derived from checked finite interval certificate artifacts.",
        "A candidate-set size greater than 1 is not an exact tie claim.",
        "Ratios to n^3/(6*pi) are finite-n numerical observations.",
        "",
        "| n | canonical orders | global bracket | width | candidates | excluded | exclusion gap | selected order | lower ratio | midpoint ratio | upper ratio |",
        "|---:|---:|---|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    for result in data["results"]:
        bracket_record = result["certified_global_bracket"]
        bracket = (
            f"({bracket_record['lower_endpoint']['radius_decimal']}, "
            f"{bracket_record['upper_endpoint']['radius_decimal']}]"
        )
        gap = result["excluded_orders"]["exclusion_gap"]["gap_decimal"]
        gap_text = gap if gap is not None else "undefined"
        ratios = result["exploratory_asymptotic_ratios"]
        lines.append(
            "| {n} | {count} | `{bracket}` | `{width}` | {candidates} | {excluded} | "
            "`{gap}` | `{selected}` | `{lower_ratio}` | `{mid_ratio}` | `{upper_ratio}` |".format(
                n=result["n"],
                count=result["canonical_order_count"],
                bracket=bracket,
                width=bracket_record["width_decimal"],
                candidates=result["candidate_set"]["size"],
                excluded=result["excluded_orders"]["count"],
                gap=gap_text,
                selected=_format_order(bracket_record["upper_endpoint"]["source_index_order"]),
                lower_ratio=ratios["lower_ratio_decimal"],
                mid_ratio=ratios["midpoint_ratio_decimal"],
                upper_ratio=ratios["upper_ratio_decimal"],
            )
        )
    lines.extend(
        [
            "",
            "Identical serialized bracket groups record matching endpoint strings only.",
            "",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Build the finite-results analysis CLI parser."""

    parser = argparse.ArgumentParser(
        prog=COMMAND_NAME,
        description=(
            "Build a derived finite-results summary from checked small-n "
            "interval certificate artifacts."
        ),
    )
    parser.add_argument(
        "artifacts",
        nargs="*",
        type=Path,
        help="checked small-n interval certificate JSON artifact path(s)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="path to write the derived summary; stdout is used when omitted",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="output format",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indentation level",
    )
    parser.add_argument(
        "--created-at-utc",
        help="override generation timestamp for reproducible artifacts",
    )
    parser.add_argument(
        "--no-additive-differences",
        dest="include_additive_differences",
        action="store_false",
        help="omit additive differences from the finite-n ratio diagnostics",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the finite-results summary CLI."""

    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)
    paths = args.artifacts if args.artifacts else DEFAULT_CHECKED_ARTIFACT_PATHS
    command_summary = (
        COMMAND_NAME + " " + shlex.join(str(item) for item in raw_argv)
        if raw_argv
        else f"programmatic call: {COMMAND_NAME}"
    )
    summary = build_finite_results_summary(
        paths,
        include_additive_differences=args.include_additive_differences,
        created_at_utc=args.created_at_utc,
        command_summary=command_summary,
    )
    if args.format == "json":
        output = dumps_finite_results_summary(summary, indent=args.indent)
    else:
        output = format_finite_results_markdown(summary)

    if args.output is None:
        print(output, end="" if output.endswith("\n") else "\n")
    else:
        args.output.write_text(output, encoding="utf-8")
    return 0


def _analyze_source_certificate(
    path: str | Path,
    *,
    include_additive_differences: bool,
) -> tuple[dict[str, Any], dict[str, Any]]:
    artifact_path = Path(path)
    certificate = load_small_n_interval_certificate_artifact(artifact_path)
    artifact = certificate.to_dict()
    _require_checked_certificate(artifact)
    source_record = _source_certificate_record(
        artifact_path,
        artifact,
        content_sha256=_sha256_file(artifact_path),
    )
    result = _finite_result_from_artifact(
        artifact,
        source_record=source_record,
        include_additive_differences=include_additive_differences,
    )
    return source_record, result


def _finite_result_from_artifact(
    artifact: Mapping[str, Any],
    *,
    source_record: Mapping[str, Any],
    include_additive_differences: bool,
) -> dict[str, Any]:
    n = int(artifact["instance"]["n"])
    local_brackets = _local_brackets_from_artifact(artifact)
    if not local_brackets:
        raise ValueError("checked finite certificate must contain local bracket summaries")

    global_lower_decimal = str(artifact["result"]["global_lower_bound"]["radius_decimal"])
    global_upper_decimal = str(artifact["result"]["global_upper_bound"]["radius_decimal"])
    with localcontext() as context:
        context.prec = 120
        global_lower = Decimal(global_lower_decimal)
        global_upper = Decimal(global_upper_decimal)
        if global_lower > global_upper:
            raise ValueError("global lower endpoint must not exceed global upper endpoint")
        bracket_width = global_upper - global_lower

        candidate_orders: list[dict[str, Any]] = []
        excluded_orders: list[dict[str, Any]] = []
        for item in local_brackets:
            order_record = _order_bracket_record(item)
            if item.lower <= global_upper:
                candidate_orders.append(order_record)
            else:
                lower_minus_upper = item.lower - global_upper
                excluded_record = dict(order_record)
                excluded_record["lower_minus_global_upper_decimal"] = _decimal_string(
                    lower_minus_upper
                )
                excluded_orders.append(excluded_record)

        if excluded_orders:
            exclusion_gap = min(
                Decimal(order["lower_minus_global_upper_decimal"]) for order in excluded_orders
            )
            exclusion_gap_decimal: str | None = _decimal_string(exclusion_gap)
            exclusion_gap_orders = [
                {
                    "index_order": order["index_order"],
                    "radius_order": order["radius_order"],
                    "lower_radius_decimal": order["lower_radius_decimal"],
                    "lower_minus_global_upper_decimal": order[
                        "lower_minus_global_upper_decimal"
                    ],
                }
                for order in excluded_orders
                if Decimal(order["lower_minus_global_upper_decimal"]) == exclusion_gap
            ]
        else:
            exclusion_gap_decimal = None
            exclusion_gap_orders = []

    result = {
        "n": n,
        "source_certificate": copy.deepcopy(dict(source_record)),
        "canonical_order_count": int(artifact["order_space"]["covered_canonical_count"]),
        "certified_global_bracket": {
            "classification": "computer_certified_result",
            "lower_endpoint": {
                "radius_decimal": global_lower_decimal,
                "encoding": "decimal_string",
                "included": bool(artifact["result"]["global_lower_bound"]["included"]),
                "source_index_order": list(
                    artifact["result"]["global_lower_bound"]["source_index_order"]
                ),
            },
            "upper_endpoint": {
                "radius_decimal": global_upper_decimal,
                "encoding": "decimal_string",
                "included": bool(artifact["result"]["global_upper_bound"]["included"]),
                "source_index_order": list(
                    artifact["result"]["global_upper_bound"]["source_index_order"]
                ),
            },
            "width_decimal": _decimal_string(bracket_width),
        },
        "candidate_set": {
            "classification": "computer_certified_result",
            "semantics": "canonical orders whose verified strict lower endpoint L_sigma is <= verified global upper endpoint U",
            "size": len(candidate_orders),
            "multiplicity_interpretation": _candidate_set_classification(len(candidate_orders)),
            "orders": candidate_orders,
            "warning": (
                "Multiple certified candidates are not an exact tie claim."
                if len(candidate_orders) > 1
                else "The unique candidate is modulo the current rotation/reflection convention."
            ),
        },
        "excluded_orders": {
            "classification": "computer_certified_result",
            "semantics": "canonical orders whose verified strict lower endpoint L_sigma is > verified global upper endpoint U",
            "count": len(excluded_orders),
            "orders": excluded_orders,
            "exclusion_gap": {
                "classification": "computer_certified_result",
                "defined": bool(excluded_orders),
                "gap_decimal": exclusion_gap_decimal,
                "orders": exclusion_gap_orders,
            },
        },
        "identical_serialized_bracket_groups": {
            "classification": "verified_fact",
            "warning": (
                "Identical serialized bracket endpoints are not an exact equality "
                "claim for fixed-order optima."
            ),
            "groups": _identical_bracket_groups(local_brackets),
        },
        "exploratory_asymptotic_ratios": _asymptotic_diagnostics(
            n,
            lower=global_lower,
            upper=global_upper,
            include_additive_differences=include_additive_differences,
        ),
        "limitations": [
            "Finite checked certificate evidence for this n only.",
            "Candidate multiplicity is not an exact tie claim.",
            "Identical serialized brackets are not exact optimum equality claims.",
        ],
    }
    _validate_derived_result(result)
    return result


def _require_checked_certificate(artifact: Mapping[str, Any]) -> None:
    if artifact.get("schema_version") != SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION:
        raise ValueError("finite-result analysis requires small-n interval certificate v1")
    if artifact.get("artifact_type") != SMALL_N_INTERVAL_CERTIFICATE_ARTIFACT_TYPE:
        raise ValueError("finite-result analysis requires a small-n interval certificate")
    evidence = _expect_mapping(artifact.get("evidence"), "evidence")
    if evidence.get("classification") != "computer_certified_result":
        raise ValueError("finite-result analysis requires a computer_certified_result artifact")
    claim = _expect_mapping(evidence.get("claim"), "evidence.claim")
    if claim.get("scope") != EVIDENCE_SCOPE:
        raise ValueError(
            "finite-result analysis requires finite_global_small_n_interval_bracket scope"
        )


def _source_certificate_record(
    path: Path,
    artifact: Mapping[str, Any],
    *,
    content_sha256: str,
) -> dict[str, Any]:
    provenance = _expect_mapping(artifact.get("provenance"), "provenance")
    repository = _expect_mapping(provenance.get("repository"), "provenance.repository")
    evidence = _expect_mapping(artifact.get("evidence"), "evidence")
    claim = _expect_mapping(evidence.get("claim"), "evidence.claim")
    return {
        "path": _display_path(path),
        "content_sha256": content_sha256,
        "schema_version": str(artifact["schema_version"]),
        "artifact_type": str(artifact["artifact_type"]),
        "n": int(_expect_mapping(artifact["instance"], "instance")["n"]),
        "evidence_classification": str(evidence["classification"]),
        "evidence_scope": str(claim["scope"]),
        "source_provenance": {
            "repository_git_commit": repository.get("git_commit"),
            "repository_git_dirty": bool(repository.get("git_dirty")),
        },
    }


def _local_brackets_from_artifact(artifact: Mapping[str, Any]) -> tuple[_LocalBracket, ...]:
    items: list[_LocalBracket] = []
    with localcontext() as context:
        context.prec = 120
        for summary in artifact["local_bracket_summaries"]:
            lower_decimal = str(summary["lower_radius_decimal"])
            upper_decimal = str(summary["upper_radius_decimal"])
            items.append(
                _LocalBracket(
                    index_order=tuple(int(value) for value in summary["index_order"]),
                    radius_order=tuple(int(value) for value in summary["radius_order"]),
                    lower_decimal=lower_decimal,
                    upper_decimal=upper_decimal,
                    lower=Decimal(lower_decimal),
                    upper=Decimal(upper_decimal),
                    source_check_id=str(summary["check_id"]),
                )
            )
    return tuple(items)


def _order_bracket_record(item: _LocalBracket) -> dict[str, Any]:
    return {
        "source_check_id": item.source_check_id,
        "index_order": list(item.index_order),
        "radius_order": list(item.radius_order),
        "lower_radius_decimal": item.lower_decimal,
        "upper_radius_decimal": item.upper_decimal,
    }


def _identical_bracket_groups(local_brackets: Iterable[_LocalBracket]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[_LocalBracket]] = defaultdict(list)
    for item in local_brackets:
        grouped[(item.lower_decimal, item.upper_decimal)].append(item)

    groups: list[dict[str, Any]] = []
    for (lower_decimal, upper_decimal), items in grouped.items():
        if len(items) <= 1:
            continue
        groups.append(
            {
                "lower_radius_decimal": lower_decimal,
                "upper_radius_decimal": upper_decimal,
                "size": len(items),
                "orders": [
                    {
                        "source_check_id": item.source_check_id,
                        "index_order": list(item.index_order),
                        "radius_order": list(item.radius_order),
                    }
                    for item in items
                ],
            }
        )
    groups.sort(key=lambda group: (group["orders"][0]["index_order"], group["size"]))
    return groups


def _candidate_set_classification(candidate_count: int) -> str:
    if candidate_count == 1:
        return "unique_certified_candidate_mod_rotation_reflection"
    return "multiple_certified_candidates_no_exact_tie_claim"


def _asymptotic_diagnostics(
    n: int,
    *,
    lower: Decimal,
    upper: Decimal,
    include_additive_differences: bool,
) -> dict[str, Any]:
    with localcontext() as context:
        context.prec = 120
        midpoint = (lower + upper) / Decimal(2)

    with mp.workdps(100):
        reference = mp.mpf(n) ** 3 / (6 * mp.pi)
        lower_mpf = mp.mpf(str(lower))
        midpoint_mpf = mp.mpf(str(midpoint))
        upper_mpf = mp.mpf(str(upper))
        diagnostics: dict[str, Any] = {
            "classification": ASYMPTOTIC_DIAGNOSTIC_CLASSIFICATION,
            "reference": ASYMPTOTIC_REFERENCE,
            "reference_value_decimal": _mp_decimal_string(reference),
            "midpoint_decimal": _decimal_string(midpoint),
            "lower_ratio_decimal": _mp_decimal_string(lower_mpf / reference),
            "midpoint_ratio_decimal": _mp_decimal_string(midpoint_mpf / reference),
            "upper_ratio_decimal": _mp_decimal_string(upper_mpf / reference),
            "warning": (
                "These finite-n diagnostics are numerical observations only."
            ),
        }
        if include_additive_differences:
            diagnostics["additive_difference_from_reference"] = {
                "lower_minus_reference_decimal": _mp_decimal_string(lower_mpf - reference),
                "midpoint_minus_reference_decimal": _mp_decimal_string(
                    midpoint_mpf - reference
                ),
                "upper_minus_reference_decimal": _mp_decimal_string(upper_mpf - reference),
            }
    return diagnostics


def _cross_n_analysis(results: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    n_values = [int(result["n"]) for result in results]
    candidate_sizes = [int(result["candidate_set"]["size"]) for result in results]
    excluded_counts = [int(result["excluded_orders"]["count"]) for result in results]
    upper_ratios = [
        str(result["exploratory_asymptotic_ratios"]["upper_ratio_decimal"])
        for result in results
    ]
    midpoint_ratios = [
        str(result["exploratory_asymptotic_ratios"]["midpoint_ratio_decimal"])
        for result in results
    ]
    observed_patterns: list[dict[str, Any]] = []
    if candidate_sizes == sorted(candidate_sizes):
        observed_patterns.append(
            {
                "name": "candidate_set_size_nondecreasing_on_checked_range",
                "classification": "empirical_pattern",
                "n_values": n_values,
                "values": candidate_sizes,
                "statement": "Candidate-set size is nondecreasing across these checked finite inputs.",
            }
        )
    return {
        "classification": "empirical_pattern",
        "n_values": n_values,
        "finite_sequences": {
            "candidate_set_sizes": candidate_sizes,
            "excluded_order_counts": excluded_counts,
            "midpoint_ratios_to_reference": midpoint_ratios,
            "upper_ratios_to_reference": upper_ratios,
        },
        "observed_patterns": observed_patterns,
        "warning": "Cross-n entries describe the listed checked finite inputs only.",
    }


def _definitions_record() -> dict[str, str]:
    return {
        "candidate_set": (
            "For one checked finite certificate, U is the verified global upper "
            "endpoint and C is the set of canonical orders sigma with verified "
            "strict lower endpoint L_sigma <= U."
        ),
        "excluded_order": (
            "An excluded order has verified strict lower endpoint L_sigma > U."
        ),
        "exclusion_gap": (
            "When excluded orders exist, the exclusion gap is min(L_sigma - U) "
            "over excluded orders; otherwise it is null."
        ),
        "identical_serialized_brackets": (
            "Groups of canonical orders whose source summary lower and upper "
            "endpoint strings are identical."
        ),
        "ratio_reference": "n^3/(6*pi).",
    }


def _classification_record() -> dict[str, dict[str, str]]:
    return {
        "certified_global_bracket": {
            "classification": "computer_certified_result",
            "basis": "verified source certificate global endpoints",
        },
        "candidate_set_membership": {
            "classification": "computer_certified_result",
            "basis": "verified source lower endpoints compared with verified global upper endpoint",
        },
        "excluded_order_count": {
            "classification": "computer_certified_result",
            "basis": "verified source lower endpoints compared with verified global upper endpoint",
        },
        "exclusion_gap": {
            "classification": "computer_certified_result",
            "basis": "verified source lower endpoints minus verified global upper endpoint",
        },
        "identical_serialized_bracket_groups": {
            "classification": "verified_fact",
            "basis": "string identity in semantically validated source certificate summaries",
        },
        "ratios_to_reference": {
            "classification": "numerical_observation",
            "basis": "finite-n arithmetic diagnostic against n^3/(6*pi)",
        },
        "cross_n_trends": {
            "classification": "empirical_pattern",
            "basis": "patterns visible only in the listed checked finite inputs",
        },
        "limitations": {
            "classification": "unresolved_claim",
            "basis": "explicit scope boundaries not settled by this artifact",
        },
    }


def _limitations_record(n_values: Sequence[int]) -> list[str]:
    n_text = ",".join(str(n) for n in n_values)
    return [
        f"Derived from checked finite certificates for n={n_text} only.",
        "Does not establish exact optimum values.",
        "Does not establish exact ties between multiple candidate orders.",
        "Ratios and cross-n sequences do not establish behavior beyond the listed inputs.",
        "Depends on the documented guarded mpmath.iv interval-backend contract of the source certificates.",
    ]


def _provenance_record(
    *,
    created_at_utc: str | None,
    command_summary: str,
    source_count: int,
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
                "role": "finite-n ratio arithmetic",
            },
            {
                "name": "power-ringmin",
                "version": "0.1.0",
                "role": "finite-results summary generator",
            },
        ],
        "source_files": [
            {
                "path": "src/power_ringmin/finite_results.py",
                "role": "derived finite-results summary contract",
            },
            {
                "path": "src/power_ringmin/small_n_interval_certificate.py",
                "role": "source certificate semantic loader",
            },
            {
                "path": "src/power_ringmin/interval_verifier.py",
                "role": "source certificate local interval verifier",
            },
            {
                "path": "src/power_ringmin/search_small_n.py",
                "role": "source certificate canonical order-space regeneration",
            },
        ],
        "commands": [
            {
                "command": command_summary,
                "cwd": str(Path.cwd()),
                "result": "pass",
                "output_summary": (
                    f"Built derived finite-results summary from {source_count} "
                    "semantically validated source certificate artifact(s)."
                ),
            }
        ],
        "randomness": {
            "used": False,
            "seeds": [],
        },
    }


def _validate_problem(value: Any) -> None:
    problem = _expect_mapping(value, "problem")
    constraints = _expect_mapping(problem.get("constraints"), "problem.constraints")
    if problem.get("project") != "power-ringmin":
        raise ValueError("problem.project must be power-ringmin")
    if problem.get("radius_model") != "quadratic":
        raise ValueError("problem.radius_model must be quadratic")
    if problem.get("dimension") != 2:
        raise ValueError("problem.dimension must be 2")
    for key in (
        "central_external_tangency",
        "peripheral_pairwise_disjoint_interiors",
        "all_pairs_checked",
    ):
        if constraints.get(key) is not True:
            raise ValueError(f"problem.constraints.{key} must be true")


def _validate_definitions(value: Any) -> None:
    definitions = _expect_mapping(value, "definitions")
    expected = set(_definitions_record())
    if set(definitions) != expected:
        raise ValueError("definitions keys do not match the v1 contract")
    for key, text in definitions.items():
        if not isinstance(text, str) or not text:
            raise ValueError(f"definitions.{key} must be a non-empty string")


def _validate_classification_record(value: Any) -> None:
    record = _expect_mapping(value, "evidence_classification_by_category")
    expected = set(_classification_record())
    if set(record) != expected:
        raise ValueError("evidence_classification_by_category keys do not match the v1 contract")
    for key, item in record.items():
        source = _expect_mapping(item, f"evidence_classification_by_category.{key}")
        classification = source.get("classification")
        if classification not in EVIDENCE_CLASSIFICATIONS:
            raise ValueError(f"{key} has unsupported evidence classification")
        if not isinstance(source.get("basis"), str) or not source["basis"]:
            raise ValueError(f"{key}.basis must be non-empty")


def _validate_provenance(value: Any) -> None:
    provenance = _expect_mapping(value, "provenance")
    if not isinstance(provenance.get("created_at_utc"), str) or not provenance["created_at_utc"]:
        raise ValueError("provenance.created_at_utc must be a non-empty string")
    repository = _expect_mapping(provenance.get("repository"), "provenance.repository")
    if repository.get("name") != "power-ringmin":
        raise ValueError("provenance.repository.name must be power-ringmin")
    commit = repository.get("git_commit")
    if commit is not None and (not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit)):
        raise ValueError("provenance.repository.git_commit must be null or a 40-character hash")
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


def _validate_limitations(value: Any) -> None:
    limitations = _expect_list(value, "limitations")
    if not limitations:
        raise ValueError("limitations must be non-empty")
    for i, item in enumerate(limitations):
        if not isinstance(item, str) or not item:
            raise ValueError(f"limitations[{i}] must be a non-empty string")
    required_phrases = (
        "checked finite certificates",
        "exact optimum",
        "exact ties",
        "beyond the listed inputs",
        "interval-backend contract",
    )
    joined = "\n".join(limitations)
    for phrase in required_phrases:
        if phrase not in joined:
            raise ValueError(f"limitations must mention {phrase!r}")


def _validate_source_certificate_record(value: Any) -> Mapping[str, Any]:
    source = _expect_mapping(value, "source_certificates[]")
    required = {
        "path",
        "content_sha256",
        "schema_version",
        "artifact_type",
        "n",
        "evidence_classification",
        "evidence_scope",
        "source_provenance",
    }
    if set(source) != required:
        raise ValueError("source certificate record keys do not match the v1 contract")
    if not isinstance(source.get("path"), str) or not source["path"]:
        raise ValueError("source certificate path must be a non-empty string")
    if not isinstance(source.get("content_sha256"), str) or not SHA256_RE.fullmatch(source["content_sha256"]):
        raise ValueError("source certificate content_sha256 must be a SHA-256 hex digest")
    if source.get("schema_version") != SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION:
        raise ValueError("source certificate schema_version is unsupported")
    if source.get("artifact_type") != SMALL_N_INTERVAL_CERTIFICATE_ARTIFACT_TYPE:
        raise ValueError("source certificate artifact_type is unsupported")
    _parse_positive_int(source.get("n"), "source certificate n")
    if source.get("evidence_classification") != "computer_certified_result":
        raise ValueError("source certificate evidence_classification is unsupported")
    if source.get("evidence_scope") != EVIDENCE_SCOPE:
        raise ValueError("source certificate evidence_scope is unsupported")
    provenance = _expect_mapping(source.get("source_provenance"), "source_provenance")
    commit = provenance.get("repository_git_commit")
    if commit is not None and (not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit)):
        raise ValueError("source_provenance.repository_git_commit must be null or a 40-character hash")
    if not isinstance(provenance.get("repository_git_dirty"), bool):
        raise ValueError("source_provenance.repository_git_dirty must be boolean")
    return source


def _validate_derived_result(result: Mapping[str, Any]) -> None:
    candidate_size = int(result["candidate_set"]["size"])
    excluded_count = int(result["excluded_orders"]["count"])
    canonical_count = int(result["canonical_order_count"])
    if candidate_size <= 0:
        raise ValueError("candidate set must be non-empty")
    if candidate_size + excluded_count != canonical_count:
        raise ValueError("candidate and excluded counts must cover the canonical order space")
    gap = _expect_mapping(result["excluded_orders"]["exclusion_gap"], "exclusion_gap")
    if excluded_count == 0 and (gap.get("defined") is not False or gap.get("gap_decimal") is not None):
        raise ValueError("exclusion gap must be undefined when no order is excluded")
    if excluded_count > 0 and (gap.get("defined") is not True or gap.get("gap_decimal") is None):
        raise ValueError("exclusion gap is required when at least one order is excluded")
    bracket = _expect_mapping(result["certified_global_bracket"], "certified_global_bracket")
    if bracket.get("classification") != "computer_certified_result":
        raise ValueError("certified global bracket classification is unsupported")
    for name in ("lower_endpoint", "upper_endpoint"):
        endpoint = _expect_mapping(bracket.get(name), f"certified_global_bracket.{name}")
        _assert_decimal_string(endpoint.get("radius_decimal"), f"{name}.radius_decimal")
        if endpoint.get("encoding") != "decimal_string":
            raise ValueError(f"{name}.encoding must be decimal_string")
        if not isinstance(endpoint.get("included"), bool):
            raise ValueError(f"{name}.included must be boolean")
        _expect_list(endpoint.get("source_index_order"), f"{name}.source_index_order")
    _assert_decimal_string(bracket.get("width_decimal"), "certified_global_bracket.width_decimal")


def _result_uses_additive_differences(results: Sequence[Any]) -> bool:
    if not results:
        return True
    first = _expect_mapping(results[0], "results[0]")
    diagnostics = _expect_mapping(
        first.get("exploratory_asymptotic_ratios"),
        "exploratory_asymptotic_ratios",
    )
    return "additive_difference_from_reference" in diagnostics


def _reject_forbidden_claim_phrases(source: Mapping[str, Any]) -> None:
    text = json.dumps(source, sort_keys=True).lower()
    forbidden = (
        "asymptotic theorem",
        "all-n theorem",
        "for all n",
        "exact tie theorem",
    )
    for phrase in forbidden:
        if phrase in text:
            raise ValueError(f"finite-results summary must not contain forbidden claim phrase: {phrase}")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _resolve_source_path(path_text: str, base_dir: Path) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return base_dir / path


def _decimal_string(value: Decimal) -> str:
    return format(value, "f")


def _mp_decimal_string(value: mp.mpf, *, digits: int = 50) -> str:
    return mp.nstr(value, n=digits, strip_zeros=False, min_fixed=-10, max_fixed=80)


def _display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return resolved.as_posix()


def _format_order(order: Sequence[int]) -> str:
    return "[" + ",".join(str(value) for value in order) + "]"


def _parse_positive_int(value: Any, name: str) -> int:
    parsed = _parse_nonnegative_int(value, name)
    if parsed <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return parsed


def _parse_nonnegative_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be an integer")
    if isinstance(value, int):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = int(value, 10)
        except ValueError as exc:
            raise ValueError(f"{name} must be an integer") from exc
        if str(parsed) != value:
            raise ValueError(f"{name} must be an integer")
    else:
        raise ValueError(f"{name} must be an integer")
    if parsed < 0:
        raise ValueError(f"{name} must be nonnegative")
    return parsed


def _assert_decimal_string(value: Any, name: str) -> None:
    if not isinstance(value, str) or DECIMAL_STRING_RE.fullmatch(value) is None:
        raise ValueError(f"{name} must be a decimal string")
    Decimal(value)


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
    "ASYMPTOTIC_DIAGNOSTIC_CLASSIFICATION",
    "ASYMPTOTIC_REFERENCE",
    "COMMAND_NAME",
    "DEFAULT_CHECKED_ARTIFACT_PATHS",
    "FINITE_RESULTS_SUMMARY_ARTIFACT_TYPE",
    "FINITE_RESULTS_SUMMARY_SCHEMA_VERSION",
    "SUMMARY_FORMAT_VERSION",
    "FiniteResultsSummary",
    "analyze_checked_finite_results",
    "analyze_finite_result_artifact",
    "build_finite_results_summary",
    "build_parser",
    "dump_finite_results_summary",
    "dump_finite_results_summary_artifact",
    "dumps_finite_results_summary",
    "dumps_finite_results_summary_artifact",
    "format_finite_results_markdown",
    "load_finite_results_summary",
    "load_finite_results_summary_artifact",
    "loads_finite_results_summary",
    "loads_finite_results_summary_artifact",
    "main",
    "validate_finite_results_summary_artifact",
]


if __name__ == "__main__":
    raise SystemExit(main())
