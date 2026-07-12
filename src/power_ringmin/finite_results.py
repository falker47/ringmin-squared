"""Derived finite-result summaries for checked small-n certificates.

This module reads checked finite interval certificate artifacts through the
existing semantic loader and derives candidate-set information that is useful
for research notes.  The derived summary is intentionally not a public schema
artifact in this task.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from decimal import Decimal, localcontext
import json
from pathlib import Path
from typing import Any

import mpmath as mp

from power_ringmin.small_n_interval_certificate import (
    EVIDENCE_SCOPE,
    load_small_n_interval_certificate_artifact,
)

SUMMARY_FORMAT_VERSION = "power-ringmin.task_scoped_finite_results_summary.v1"
COMMAND_NAME = "power-ringmin-analyze-finite-results"
DEFAULT_CHECKED_ARTIFACT_PATHS = (
    Path("examples/small_n_interval_certificate_n3.json"),
    Path("examples/small_n_interval_certificate_n4.json"),
    Path("examples/small_n_interval_certificate_n5.json"),
    Path("examples/small_n_interval_certificate_n6.json"),
)
ASYMPTOTIC_REFERENCE = "n^3/(6*pi)"
ASYMPTOTIC_DIAGNOSTIC_CLASSIFICATION = "numerical_observation"


@dataclass(frozen=True)
class _LocalBracket:
    index_order: tuple[int, ...]
    radius_order: tuple[int, ...]
    lower_decimal: str
    upper_decimal: str
    lower: Decimal
    upper: Decimal


def analyze_checked_finite_results(
    artifact_paths: Sequence[str | Path] | None = None,
    *,
    include_additive_differences: bool = True,
) -> dict[str, Any]:
    """Analyze checked small-n interval certificate artifacts.

    The input artifacts are loaded through
    :func:`load_small_n_interval_certificate_artifact`, so malformed,
    incomplete, or semantically inconsistent certificates are rejected before
    this derived analysis is computed.
    """

    paths = tuple(Path(path) for path in (artifact_paths or DEFAULT_CHECKED_ARTIFACT_PATHS))
    if not paths:
        raise ValueError("at least one checked artifact path is required")

    results = [
        analyze_finite_result_artifact(
            path,
            include_additive_differences=include_additive_differences,
        )
        for path in paths
    ]
    results.sort(key=lambda item: (item["n"], item["source_artifact"]["path"]))

    seen_n: set[int] = set()
    for result in results:
        n = int(result["n"])
        if n in seen_n:
            raise ValueError(f"duplicate finite-result artifact for n={n}")
        seen_n.add(n)

    return {
        "summary_format_version": SUMMARY_FORMAT_VERSION,
        "generated_by": "power_ringmin.finite_results",
        "source_artifact_count": len(results),
        "claims_and_limitations": {
            "candidate_set_definition": (
                "For one checked finite certificate with verified local brackets, "
                "U is the minimum verified upper endpoint across all canonical "
                "orders, and C is the set of orders sigma with L_sigma <= U."
            ),
            "excluded_order_definition": (
                "An order with L_sigma > U is certified not to be globally "
                "optimal under the checked artifact semantics."
            ),
            "exclusion_gap_definition": (
                "When at least one order is excluded, the exclusion gap is "
                "min(L_sigma - U) over excluded orders."
            ),
            "unique_candidate_interpretation": (
                "Candidate-set size 1 means there is a unique certified "
                "candidate order modulo the current rotation/reflection "
                "canonicalization convention."
            ),
            "multiple_candidate_warning": (
                "Candidate-set size greater than 1 is not an exact tie claim "
                "between the candidate orders."
            ),
            "serialized_bracket_warning": (
                "Identical serialized local bracket endpoints are not an exact "
                "equality claim for the corresponding fixed-order optima."
            ),
            "asymptotic_diagnostics": (
                "Ratios and differences against n^3/(6*pi) are exploratory "
                "finite-n diagnostics classified as numerical observations or "
                "empirical patterns, never certified asymptotic claims."
            ),
            "summary_scope": (
                "This is a task-scoped derived summary, not a checked permanent "
                "schema artifact."
            ),
        },
        "results": results,
    }


def analyze_finite_result_artifact(
    path: str | Path,
    *,
    include_additive_differences: bool = True,
) -> dict[str, Any]:
    """Load one checked finite certificate and derive its finite-result summary."""

    artifact_path = Path(path)
    certificate = load_small_n_interval_certificate_artifact(artifact_path)
    artifact = certificate.to_dict()
    _require_checked_certificate(artifact)

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
                excluded_record["lower_minus_global_U_decimal"] = _decimal_string(
                    lower_minus_upper
                )
                excluded_orders.append(excluded_record)

        if excluded_orders:
            exclusion_gap = min(
                Decimal(order["lower_minus_global_U_decimal"]) for order in excluded_orders
            )
            exclusion_gap_decimal: str | None = _decimal_string(exclusion_gap)
            exclusion_gap_orders = [
                {
                    "index_order": order["index_order"],
                    "radius_order": order["radius_order"],
                    "lower_radius_decimal": order["lower_radius_decimal"],
                    "lower_minus_global_U_decimal": order["lower_minus_global_U_decimal"],
                }
                for order in excluded_orders
                if Decimal(order["lower_minus_global_U_decimal"]) == exclusion_gap
            ]
        else:
            exclusion_gap_decimal = None
            exclusion_gap_orders = []

    selected_order = list(artifact["result"]["global_upper_bound"]["source_index_order"])
    result = {
        "n": n,
        "source_artifact": {
            "path": _display_path(artifact_path),
            "provenance_commit": artifact["provenance"]["repository"]["git_commit"],
            "provenance_git_dirty": artifact["provenance"]["repository"]["git_dirty"],
        },
        "canonical_order_count": int(artifact["order_space"]["covered_canonical_count"]),
        "global_bracket": {
            "lower_endpoint_decimal": global_lower_decimal,
            "lower_included": bool(artifact["result"]["global_lower_bound"]["included"]),
            "upper_endpoint_decimal": global_upper_decimal,
            "upper_included": bool(artifact["result"]["global_upper_bound"]["included"]),
            "width_decimal": _decimal_string(bracket_width),
        },
        "certificate_source_orders": {
            "selected_order": selected_order,
            "selected_order_meaning": "source_index_order of result.global_upper_bound",
            "global_lower_source_order": list(
                artifact["result"]["global_lower_bound"]["source_index_order"]
            ),
            "global_upper_source_order": selected_order,
        },
        "candidate_set": {
            "definition": "canonical orders with verified strict lower endpoint L_sigma <= U",
            "size": len(candidate_orders),
            "classification": _candidate_set_classification(len(candidate_orders)),
            "orders": candidate_orders,
            "warning": (
                "Multiple certified candidates are not an exact tie claim."
                if len(candidate_orders) > 1
                else "The unique candidate is modulo the current rotation/reflection convention."
            ),
        },
        "excluded_orders": {
            "definition": "canonical orders with verified strict lower endpoint L_sigma > U",
            "count": len(excluded_orders),
            "exclusion_gap_decimal": exclusion_gap_decimal,
            "exclusion_gap_orders": exclusion_gap_orders,
            "orders": excluded_orders,
        },
        "identical_serialized_local_bracket_groups": _identical_bracket_groups(local_brackets),
        "asymptotic_diagnostics": _asymptotic_diagnostics(
            n,
            lower=global_lower,
            upper=global_upper,
            include_additive_differences=include_additive_differences,
        ),
    }
    _validate_derived_result(result)
    return result


def dumps_finite_results_summary(summary: Mapping[str, Any], *, indent: int = 2) -> str:
    """Serialize a derived finite-results summary deterministically."""

    return json.dumps(summary, indent=indent) + "\n"


def dump_finite_results_summary(
    summary: Mapping[str, Any],
    path: str | Path,
    *,
    indent: int = 2,
) -> None:
    """Write a derived finite-results JSON summary."""

    Path(path).write_text(dumps_finite_results_summary(summary, indent=indent), encoding="utf-8")


def format_finite_results_markdown(summary: Mapping[str, Any]) -> str:
    """Render a deterministic Markdown table from a finite-results summary."""

    lines = [
        "# Derived finite results summary",
        "",
        "This task-scoped summary is derived from checked finite interval certificate artifacts.",
        "A candidate-set size greater than 1 is not an exact tie claim.",
        "Ratios to n^3/(6*pi) are exploratory finite-n diagnostics, not certified asymptotic claims.",
        "",
        "| n | canonical orders | global bracket | width | candidates | excluded | exclusion gap | selected order | lower ratio | midpoint ratio | upper ratio |",
        "|---:|---:|---|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    for result in summary["results"]:
        bracket = (
            f"({result['global_bracket']['lower_endpoint_decimal']}, "
            f"{result['global_bracket']['upper_endpoint_decimal']}]"
        )
        gap = result["excluded_orders"]["exclusion_gap_decimal"]
        gap_text = gap if gap is not None else "undefined"
        diag = result["asymptotic_diagnostics"]
        lines.append(
            "| {n} | {count} | `{bracket}` | `{width}` | {candidates} | {excluded} | "
            "`{gap}` | `{selected}` | `{lower_ratio}` | `{mid_ratio}` | `{upper_ratio}` |".format(
                n=result["n"],
                count=result["canonical_order_count"],
                bracket=bracket,
                width=result["global_bracket"]["width_decimal"],
                candidates=result["candidate_set"]["size"],
                excluded=result["excluded_orders"]["count"],
                gap=gap_text,
                selected=_format_order(result["certificate_source_orders"]["selected_order"]),
                lower_ratio=diag["lower_ratio_decimal"],
                mid_ratio=diag["midpoint_ratio_decimal"],
                upper_ratio=diag["upper_ratio_decimal"],
            )
        )
    lines.extend(
        [
            "",
            "Identical serialized bracket groups record matching endpoint strings only; they do not prove equality of fixed-order optima.",
            "",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Build the finite-results analysis CLI parser."""

    parser = argparse.ArgumentParser(
        prog=COMMAND_NAME,
        description=(
            "Analyze checked finite small-n interval certificate artifacts and "
            "derive candidate sets, exclusion gaps, and finite-n diagnostics."
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
        "--no-additive-differences",
        dest="include_additive_differences",
        action="store_false",
        help="omit additive differences from the exploratory asymptotic diagnostics",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the finite-results analysis CLI."""

    parser = build_parser()
    args = parser.parse_args(argv)
    paths = args.artifacts if args.artifacts else DEFAULT_CHECKED_ARTIFACT_PATHS
    summary = analyze_checked_finite_results(
        paths,
        include_additive_differences=args.include_additive_differences,
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


def _require_checked_certificate(artifact: Mapping[str, Any]) -> None:
    evidence = artifact["evidence"]
    if evidence["classification"] != "computer_certified_result":
        raise ValueError("finite-result analysis requires a computer_certified_result artifact")
    if evidence["claim"]["scope"] != EVIDENCE_SCOPE:
        raise ValueError("finite-result analysis requires finite_global_small_n_interval_bracket scope")


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
                )
            )
    return tuple(items)


def _order_bracket_record(item: _LocalBracket) -> dict[str, Any]:
    return {
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
                        "index_order": list(item.index_order),
                        "radius_order": list(item.radius_order),
                    }
                    for item in items
                ],
                "warning": (
                    "Identical serialized bracket endpoints are not an exact "
                    "equality claim for fixed-order optima."
                ),
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
                "These finite-n diagnostics are numerical observations only, "
                "not certified asymptotic claims."
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


def _validate_derived_result(result: Mapping[str, Any]) -> None:
    candidate_size = int(result["candidate_set"]["size"])
    excluded_count = int(result["excluded_orders"]["count"])
    canonical_count = int(result["canonical_order_count"])
    if candidate_size <= 0:
        raise ValueError("candidate set must be non-empty")
    if candidate_size + excluded_count != canonical_count:
        raise ValueError("candidate and excluded counts must cover the canonical order space")
    if excluded_count == 0 and result["excluded_orders"]["exclusion_gap_decimal"] is not None:
        raise ValueError("exclusion gap must be undefined when no order is excluded")
    if excluded_count > 0 and result["excluded_orders"]["exclusion_gap_decimal"] is None:
        raise ValueError("exclusion gap is required when at least one order is excluded")


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


__all__ = [
    "ASYMPTOTIC_DIAGNOSTIC_CLASSIFICATION",
    "ASYMPTOTIC_REFERENCE",
    "COMMAND_NAME",
    "DEFAULT_CHECKED_ARTIFACT_PATHS",
    "SUMMARY_FORMAT_VERSION",
    "analyze_checked_finite_results",
    "analyze_finite_result_artifact",
    "build_parser",
    "dump_finite_results_summary",
    "dumps_finite_results_summary",
    "format_finite_results_markdown",
    "main",
]


if __name__ == "__main__":
    raise SystemExit(main())
