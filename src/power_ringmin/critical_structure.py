"""Structural analysis for checked finite small-n candidate orders.

This module derives deterministic structural diagnostics from the checked
``n=3..6`` finite interval certificate artifacts. It does not produce new
certificates, does not generate larger ``n``, and does not promote slack or
critical-cycle proxies to exact contact claims.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping, Sequence
import copy
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import shlex
import sys
from typing import Any

import mpmath as mp

from power_ringmin.finite_results import (
    DEFAULT_CHECKED_ARTIFACT_PATHS,
    load_finite_results_summary,
)
from power_ringmin.interval_verifier import MPMathIntervalAngularOracle
from power_ringmin.small_n_interval_certificate import (
    load_small_n_interval_certificate_artifact,
)

CRITICAL_STRUCTURE_SCHEMA_VERSION = "power-ringmin.critical_structure_analysis.v1"
STRUCTURE_FORMAT_VERSION = CRITICAL_STRUCTURE_SCHEMA_VERSION
CRITICAL_STRUCTURE_ARTIFACT_TYPE = "critical_structure_analysis"
COMMAND_NAME = "power-ringmin-analyze-critical-structure"
DEFAULT_FINITE_RESULTS_SUMMARY_PATH = Path("examples/finite_results_summary_n3_n6.json")
DEFAULT_TOP_SLACK_PAIR_COUNT = 5
DEFAULT_DECIMAL_DIGITS = 80


@dataclass(frozen=True)
class CriticalStructureAnalysis:
    """Validated view of a critical-structure analysis artifact."""

    data: dict[str, Any]

    @property
    def n_values(self) -> tuple[int, ...]:
        return tuple(int(item) for item in self.data["analysis_scope"]["n_values"])

    def to_dict(self) -> dict[str, Any]:
        """Return a deep copy suitable for JSON serialization."""

        return copy.deepcopy(self.data)


def build_critical_structure_analysis(
    summary_path: str | Path = DEFAULT_FINITE_RESULTS_SUMMARY_PATH,
    *,
    top_slack_pair_count: int = DEFAULT_TOP_SLACK_PAIR_COUNT,
    created_at_utc: str | None = None,
    command_summary: str = "programmatic call: build_critical_structure_analysis",
) -> dict[str, Any]:
    """Build structural diagnostics from the checked finite-results summary."""

    if top_slack_pair_count <= 0:
        raise ValueError("top_slack_pair_count must be positive")

    summary_file = Path(summary_path)
    summary = load_finite_results_summary(summary_file).to_dict()
    results = []
    for finite_result in summary["results"]:
        n = int(finite_result["n"])
        source_path = Path(finite_result["source_certificate"]["path"])
        certificate = load_small_n_interval_certificate_artifact(source_path).to_dict()
        results.append(
            _analyze_n_result(
                finite_result,
                certificate,
                top_slack_pair_count=top_slack_pair_count,
            )
        )

    analysis: dict[str, Any] = {
        "schema_version": CRITICAL_STRUCTURE_SCHEMA_VERSION,
        "artifact_type": CRITICAL_STRUCTURE_ARTIFACT_TYPE,
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
        "analysis_scope": {
            "n_values": [int(result["n"]) for result in results],
            "source_summary_path": summary_file.as_posix(),
            "source_summary_sha256": _sha256_file(summary_file),
            "source_certificate_paths": [
                str(item["path"]) for item in summary["source_certificates"]
            ],
            "source_certificate_sha256": [
                str(item["content_sha256"]) for item in summary["source_certificates"]
            ],
            "analyzed_orders": "certified_candidate_orders_only",
            "excluded_orders_analyzed": False,
            "n7_generated": False,
        },
        "configuration": {
            "top_slack_pair_count": top_slack_pair_count,
            "slack_computation": (
                "interval-lower all-pairs witness slack using each local record's "
                "guarded mpmath.iv angular backend metadata"
            ),
            "cycle_normalization": (
                "directed stable edge tokens are canonicalized by lexicographically "
                "minimal cyclic rotation; pair-set signatures ignore directed "
                "traversal and edge kind"
            ),
            "weak_constraint_rule": (
                "minimum combined finite proxy incidence across lower-cycle pairs, "
                "minimum-slack pairs, and top-ranked slack pairs, with zero "
                "lower-cycle incidence required; heuristic only"
            ),
        },
        "definitions": _definitions_record(),
        "evidence_classification_by_field": _classification_record(),
        "results": results,
        "cross_n_patterns": _cross_n_patterns(results),
        "provenance": _provenance_record(
            created_at_utc=created_at_utc,
            command_summary=command_summary,
        ),
        "limitations": _limitations_record(),
    }
    validate_critical_structure_analysis_artifact(analysis)
    return analysis


def dump_critical_structure_analysis(
    analysis: Mapping[str, Any] | CriticalStructureAnalysis,
    path: str | Path,
    *,
    indent: int = 2,
) -> None:
    """Validate and write a structural analysis JSON artifact."""

    Path(path).write_text(dumps_critical_structure_analysis(analysis, indent=indent), encoding="utf-8")


def dumps_critical_structure_analysis(
    analysis: Mapping[str, Any] | CriticalStructureAnalysis,
    *,
    indent: int = 2,
) -> str:
    """Validate and serialize a structural analysis JSON artifact."""

    data = analysis.to_dict() if isinstance(analysis, CriticalStructureAnalysis) else copy.deepcopy(dict(analysis))
    validate_critical_structure_analysis_artifact(data)
    return json.dumps(data, indent=indent, sort_keys=False) + "\n"


def load_critical_structure_analysis(path: str | Path) -> CriticalStructureAnalysis:
    """Load and validate a structural analysis JSON artifact."""

    return loads_critical_structure_analysis(Path(path).read_text(encoding="utf-8"))


def loads_critical_structure_analysis(text: str) -> CriticalStructureAnalysis:
    """Parse and validate a structural analysis JSON artifact."""

    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("critical-structure analysis JSON must contain an object")
    validate_critical_structure_analysis_artifact(payload)
    return CriticalStructureAnalysis(copy.deepcopy(payload))


def validate_critical_structure_analysis_artifact(artifact: Mapping[str, Any]) -> None:
    """Raise ``ValueError`` if the analysis artifact has an invalid v1 shape."""

    source = _expect_mapping(artifact, "artifact")
    if source.get("schema_version") != CRITICAL_STRUCTURE_SCHEMA_VERSION:
        raise ValueError("unsupported critical-structure schema_version")
    if source.get("artifact_type") != CRITICAL_STRUCTURE_ARTIFACT_TYPE:
        raise ValueError("unsupported critical-structure artifact_type")
    scope = _expect_mapping(source.get("analysis_scope"), "analysis_scope")
    n_values = _expect_list(scope.get("n_values"), "analysis_scope.n_values")
    if n_values != [3, 4, 5, 6]:
        raise ValueError("critical-structure v1 artifact must analyze n=3..6")
    if scope.get("analyzed_orders") != "certified_candidate_orders_only":
        raise ValueError("analysis_scope.analyzed_orders is unsupported")
    if scope.get("excluded_orders_analyzed") is not False:
        raise ValueError("excluded orders must not be marked analyzed")
    if scope.get("n7_generated") is not False:
        raise ValueError("n7_generated must be false")
    config = _expect_mapping(source.get("configuration"), "configuration")
    if int(config.get("top_slack_pair_count", 0)) <= 0:
        raise ValueError("configuration.top_slack_pair_count must be positive")
    _validate_classifications(source.get("evidence_classification_by_field"))
    results = _expect_list(source.get("results"), "results")
    if [int(_expect_mapping(item, "result").get("n")) for item in results] != n_values:
        raise ValueError("results must match analysis_scope.n_values")
    for result in results:
        _validate_result_shape(_expect_mapping(result, "result"))


def normalize_cyclic_signature(tokens: Sequence[str]) -> tuple[str, ...]:
    """Return the lexicographically smallest cyclic rotation of ``tokens``."""

    if not tokens:
        return ()
    values = tuple(tokens)
    rotations = (values[i:] + values[:i] for i in range(len(values)))
    return min(rotations)


def build_parser() -> argparse.ArgumentParser:
    """Build the structural analysis CLI parser."""

    parser = argparse.ArgumentParser(
        prog=COMMAND_NAME,
        description="Analyze critical-cycle and slack structure in checked finite candidate orders.",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=DEFAULT_FINITE_RESULTS_SUMMARY_PATH,
        help="checked finite-results summary artifact path",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="path to write JSON output; stdout is used when omitted",
    )
    parser.add_argument(
        "--top-slack-pair-count",
        type=int,
        default=DEFAULT_TOP_SLACK_PAIR_COUNT,
        help="number of top-ranked upper-witness slack pairs to treat as near-critical proxies",
    )
    parser.add_argument(
        "--created-at-utc",
        help="override generation timestamp for reproducible artifacts",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indentation level",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the structural analysis CLI."""

    parser = build_parser()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    args = parser.parse_args(raw_argv)
    command_summary = (
        COMMAND_NAME + " " + shlex.join(str(item) for item in raw_argv)
        if raw_argv
        else f"programmatic call: {COMMAND_NAME}"
    )
    analysis = build_critical_structure_analysis(
        args.summary,
        top_slack_pair_count=args.top_slack_pair_count,
        created_at_utc=args.created_at_utc,
        command_summary=command_summary,
    )
    output = dumps_critical_structure_analysis(analysis, indent=args.indent)
    if args.output is None:
        print(output, end="")
    else:
        args.output.write_text(output, encoding="utf-8")
    return 0


def _analyze_n_result(
    finite_result: Mapping[str, Any],
    certificate: Mapping[str, Any],
    *,
    top_slack_pair_count: int,
) -> dict[str, Any]:
    n = int(finite_result["n"])
    local_by_order = {
        tuple(record["index_order"]): record for record in certificate["local_brackets"]
    }
    candidate_orders = [
        tuple(order["index_order"]) for order in finite_result["candidate_set"]["orders"]
    ]
    candidates = [
        _analyze_candidate(local_by_order[order], top_slack_pair_count=top_slack_pair_count)
        for order in candidate_orders
    ]
    aggregate = _candidate_aggregate(
        n,
        candidates,
        identical_bracket_groups=finite_result["identical_serialized_bracket_groups"]["groups"],
    )
    return {
        "n": n,
        "classification": "empirical_pattern",
        "finite_certificate_facts": {
            "classification": "computer_certified_result",
            "canonical_order_count": int(finite_result["canonical_order_count"]),
            "certified_global_bracket": copy.deepcopy(finite_result["certified_global_bracket"]),
            "candidate_set_size": int(finite_result["candidate_set"]["size"]),
            "excluded_order_count": int(finite_result["excluded_orders"]["count"]),
            "exclusion_gap": copy.deepcopy(finite_result["excluded_orders"]["exclusion_gap"]),
            "candidate_orders": [
                copy.deepcopy(order) for order in finite_result["candidate_set"]["orders"]
            ],
            "ratios_to_reference": copy.deepcopy(
                finite_result["exploratory_asymptotic_ratios"]
            ),
        },
        "candidate_order_analyses": candidates,
        "candidate_common_core_intersections": aggregate["common_core_intersections"],
        "candidate_differences": aggregate["candidate_differences"],
        "pair_incidence_counts": aggregate["pair_incidence_counts"],
        "index_participation_counts": aggregate["index_participation_counts"],
        "recurring_near_critical_pairs": aggregate["recurring_near_critical_pairs"],
        "possible_weakly_constrained_indices": aggregate["possible_weakly_constrained_indices"],
        "empirical_noncritical_indices": aggregate["empirical_noncritical_indices"],
        "identical_bracket_group_diagnostics": aggregate[
            "identical_bracket_group_diagnostics"
        ],
    }


def _analyze_candidate(
    record: Mapping[str, Any],
    *,
    top_slack_pair_count: int,
) -> dict[str, Any]:
    lower = _lower_cycle_analysis(record)
    upper = _upper_witness_slack_analysis(record, top_slack_pair_count=top_slack_pair_count)
    return {
        "classification": "empirical_pattern",
        "index_order": list(record["index_order"]),
        "radius_order": list(record["radius_order"]),
        "lower_radius_decimal": str(record["lower_radius_decimal"]),
        "upper_radius_decimal": str(record["upper_radius_decimal"]),
        "lower_critical_cycle": lower,
        "upper_witness_slack_analysis": upper,
    }


def _lower_cycle_analysis(record: Mapping[str, Any]) -> dict[str, Any]:
    order = tuple(int(item) for item in record["index_order"])
    cycle = _expect_list(_expect_mapping(record["lower_certificate"], "lower_certificate").get("cycle"), "cycle")
    edge_records: list[dict[str, Any]] = []
    directed_tokens: list[str] = []
    pair_kind_tokens: list[str] = []
    pair_tokens: list[str] = []

    for position, edge in enumerate(cycle):
        source = int(edge["source"])
        target = int(edge["target"])
        edge_kind = str(edge["edge_kind"])
        if edge_kind == "forward_lower":
            pair_positions = (target, source)
        elif edge_kind == "wrap_upper":
            pair_positions = (source, target)
        else:
            raise ValueError(f"unsupported lower-cycle edge_kind {edge_kind!r}")
        pair = _pair_from_indices(order[pair_positions[0]], order[pair_positions[1]])
        pair_label = _pair_label(pair)
        radius_label = _radius_pair_label(pair)
        token = (
            f"{edge_kind}:{order[source]}->{order[target]}|"
            f"pair={pair_label}|radii={radius_label}"
        )
        pair_kind_token = f"{edge_kind}:{pair_label}|radii={radius_label}"
        pair_token = f"{pair_label}|radii={radius_label}"
        directed_tokens.append(token)
        pair_kind_tokens.append(pair_kind_token)
        pair_tokens.append(pair_token)
        edge_records.append(
            {
                "cycle_position": position,
                "edge_kind": edge_kind,
                "source_position": source,
                "target_position": target,
                "source_index": order[source],
                "target_index": order[target],
                "source_radius": order[source] * order[source],
                "target_radius": order[target] * order[target],
                "constraint_position_pair": list(pair_positions),
                "constraint_index_pair": list(pair),
                "constraint_radius_pair": [pair[0] * pair[0], pair[1] * pair[1]],
                "pair_label": pair_label,
                "radius_pair_label": radius_label,
                "stable_edge_token": token,
            }
        )

    pair_counts = Counter(pair_tokens)
    index_counts = _index_counts_from_pair_tokens(pair_tokens)
    return {
        "classification": "verified_fact",
        "edge_count": len(edge_records),
        "lower_negative_cycle_sum_upper_decimal": str(
            record["lower_negative_cycle_sum_upper"]
        ),
        "normalized_directed_signature": list(normalize_cyclic_signature(directed_tokens)),
        "normalized_pair_kind_signature": sorted(pair_kind_tokens),
        "normalized_pair_set_signature": sorted(set(pair_tokens)),
        "pair_incidence_counts": _counter_records(pair_counts),
        "index_incidence_counts": _index_counter_records(index_counts, n=len(order)),
        "edges": edge_records,
    }


def _upper_witness_slack_analysis(
    record: Mapping[str, Any],
    *,
    top_slack_pair_count: int,
) -> dict[str, Any]:
    order = tuple(int(item) for item in record["index_order"])
    radii = tuple(int(item) for item in record["radius_order"])
    positions = tuple(
        mp.mpf(str(item))
        for item in _expect_mapping(record["upper_certificate"], "upper_certificate")[
            "positions_rad"
        ]
    )
    R = mp.mpf(str(record["upper_radius_decimal"]))
    oracle = _oracle_from_record(record)

    rows: list[dict[str, Any]] = []
    with mp.workdps(max(mp.mp.dps, oracle.digits, DEFAULT_DECIMAL_DIGITS)):
        tau = oracle.tau()
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                theta = oracle.theta(R, mp.mpf(radii[i]), mp.mpf(radii[j]))
                delta = positions[j] - positions[i]
                forward = delta - theta.upper
                wrap = tau.lower - theta.upper - delta
                slack = min(forward, wrap)
                side = "forward" if forward <= wrap else "wrap"
                pair = _pair_from_indices(order[i], order[j])
                rows.append(
                    {
                        "_slack": slack,
                        "pair_label": _pair_label(pair),
                        "radius_pair_label": _radius_pair_label(pair),
                        "position_pair": [i, j],
                        "oriented_index_pair": [order[i], order[j]],
                        "index_pair": list(pair),
                        "radius_pair": [pair[0] * pair[0], pair[1] * pair[1]],
                        "active_side_proxy": side,
                        "slack_lower_decimal": _mp_decimal_string(slack),
                        "forward_slack_lower_decimal": _mp_decimal_string(forward),
                        "wrap_slack_lower_decimal": _mp_decimal_string(wrap),
                    }
                )

    rows.sort(
        key=lambda item: (
            item["_slack"],
            item["pair_label"],
            item["active_side_proxy"],
            item["oriented_index_pair"],
        )
    )
    ranked: list[dict[str, Any]] = []
    previous: mp.mpf | None = None
    current_rank = 0
    for ordinal, row in enumerate(rows, start=1):
        slack = row.pop("_slack")
        if previous is None or slack != previous:
            current_rank = ordinal
            previous = slack
        row["rank"] = current_rank
        ranked.append(row)

    minimum_pairs = [copy.deepcopy(item) for item in ranked if item["rank"] == 1]
    near_limit = min(top_slack_pair_count, len(ranked))
    near_pairs = [copy.deepcopy(item) for item in ranked[:near_limit]]
    min_slack_decimal = ranked[0]["slack_lower_decimal"] if ranked else None
    return {
        "classification": "numerical_observation",
        "pair_count": len(ranked),
        "reported_min_upper_witness_slack_lower_decimal": str(
            record["min_upper_witness_slack_lower"]
        ),
        "recomputed_min_slack_lower_decimal": min_slack_decimal,
        "minimum_slack_pairs": minimum_pairs,
        "near_minimum_pairs_by_rank": {
            "classification": "heuristic",
            "rank_limit": near_limit,
            "pairs": near_pairs,
        },
        "all_pairs_by_slack_rank": ranked,
    }


def _candidate_aggregate(
    n: int,
    candidates: Sequence[Mapping[str, Any]],
    *,
    identical_bracket_groups: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    lower_sets = [
        set(candidate["lower_critical_cycle"]["normalized_pair_set_signature"])
        for candidate in candidates
    ]
    lower_kind_sets = [
        set(candidate["lower_critical_cycle"]["normalized_pair_kind_signature"])
        for candidate in candidates
    ]
    directed_sets = [
        {tuple(candidate["lower_critical_cycle"]["normalized_directed_signature"])}
        for candidate in candidates
    ]
    min_sets = [_minimum_pair_set(candidate) for candidate in candidates]
    near_sets = [_near_pair_set(candidate) for candidate in candidates]

    lower_core = _intersection(lower_sets)
    lower_union = _union(lower_sets)
    min_core = _intersection(min_sets)
    min_union = _union(min_sets)
    near_core = _intersection(near_sets)
    near_union = _union(near_sets)

    lower_pair_counts = Counter()
    lower_index_counts = Counter()
    min_pair_counts = Counter()
    min_index_counts = Counter()
    near_pair_counts = Counter()
    near_index_counts = Counter()
    for candidate in candidates:
        lower_pair_counts.update(
            candidate["lower_critical_cycle"]["normalized_pair_set_signature"]
        )
        lower_index_counts.update(
            _labels_to_indices(
                candidate["lower_critical_cycle"]["normalized_pair_set_signature"]
            )
        )
        min_pairs = _minimum_pair_set(candidate)
        min_pair_counts.update(min_pairs)
        min_index_counts.update(_labels_to_indices(min_pairs))
        near_pairs = _near_pair_set(candidate)
        near_pair_counts.update(near_pairs)
        near_index_counts.update(_labels_to_indices(near_pairs))

    common = {
        "classification": "empirical_pattern",
        "lower_cycle_pair_core": _pair_records_from_tokens(lower_core),
        "lower_cycle_pair_union": _pair_records_from_tokens(lower_union),
        "lower_cycle_pair_kind_core": sorted(_intersection(lower_kind_sets)),
        "lower_directed_signature_core": [
            list(signature) for signature in sorted(_intersection(directed_sets))
        ],
        "upper_minimum_slack_pair_core": _pair_records_from_tokens(min_core),
        "upper_minimum_slack_pair_union": _pair_records_from_tokens(min_union),
        "upper_near_minimum_pair_core": _pair_records_from_tokens(near_core),
        "upper_near_minimum_pair_union": _pair_records_from_tokens(near_union),
    }
    differences = [
        {
            "classification": "empirical_pattern",
            "index_order": list(candidate["index_order"]),
            "lower_pairs_not_in_common_core": _pair_records_from_tokens(
                set(candidate["lower_critical_cycle"]["normalized_pair_set_signature"])
                - lower_core
            ),
            "upper_minimum_pairs_not_in_common_core": _pair_records_from_tokens(
                _minimum_pair_set(candidate) - min_core
            ),
            "upper_near_minimum_pairs_not_in_common_core": _pair_records_from_tokens(
                _near_pair_set(candidate) - near_core
            ),
        }
        for candidate in candidates
    ]
    pair_counts = {
        "classification": "empirical_pattern",
        "lower_cycle_pairs": _counter_pair_records(lower_pair_counts),
        "upper_minimum_slack_pairs": _counter_pair_records(min_pair_counts),
        "upper_near_minimum_pairs": _counter_pair_records(near_pair_counts),
    }
    index_counts = {
        "classification": "empirical_pattern",
        "lower_cycle_indices": _index_counter_records(lower_index_counts, n=n),
        "upper_minimum_slack_indices": _index_counter_records(min_index_counts, n=n),
        "upper_near_minimum_indices": _index_counter_records(near_index_counts, n=n),
        "combined_proxy_indices": _combined_index_counts(
            n,
            lower_index_counts,
            min_index_counts,
            near_index_counts,
        ),
    }
    recurring = {
        "classification": "empirical_pattern",
        "proxy": "pairs appearing in top-ranked upper-witness slack lists",
        "pairs": [
            item for item in _counter_pair_records(near_pair_counts) if int(item["count"]) > 1
        ],
    }
    weak = _possible_weak_indices(n, index_counts["combined_proxy_indices"])
    empirical_noncritical = {
        "classification": "empirical_pattern",
        "proxy": "absence from lower critical-cycle pair incidence across candidate orders",
        "indices": [
            item["index"]
            for item in index_counts["lower_cycle_indices"]
            if int(item["count"]) == 0
        ],
        "warning": "This does not certify non-incidence with true active constraints.",
    }
    return {
        "common_core_intersections": common,
        "candidate_differences": differences,
        "pair_incidence_counts": pair_counts,
        "index_participation_counts": index_counts,
        "recurring_near_critical_pairs": recurring,
        "possible_weakly_constrained_indices": weak,
        "empirical_noncritical_indices": empirical_noncritical,
        "identical_bracket_group_diagnostics": _identical_bracket_diagnostics(
            n,
            candidates,
            identical_bracket_groups,
        ),
    }


def _identical_bracket_diagnostics(
    n: int,
    candidates: Sequence[Mapping[str, Any]],
    groups: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    by_order = {_order_key(candidate["index_order"]): candidate for candidate in candidates}
    diagnostics = []
    for group in groups:
        candidate_orders = [
            tuple(order["index_order"])
            for order in group["orders"]
            if _order_key(order["index_order"]) in by_order
        ]
        if len(candidate_orders) < 2:
            continue
        group_candidates = [by_order[_order_key(order)] for order in candidate_orders]
        lower_sets = [
            set(candidate["lower_critical_cycle"]["normalized_pair_set_signature"])
            for candidate in group_candidates
        ]
        lower_kind_sets = [
            set(candidate["lower_critical_cycle"]["normalized_pair_kind_signature"])
            for candidate in group_candidates
        ]
        directed_signatures = {
            tuple(candidate["lower_critical_cycle"]["normalized_directed_signature"])
            for candidate in group_candidates
        }
        min_sets = [_minimum_pair_set(candidate) for candidate in group_candidates]
        near_sets = [_near_pair_set(candidate) for candidate in group_candidates]
        lower_core = _intersection(lower_sets)
        core_indices = sorted(set(_labels_to_indices(lower_core)))
        omitted = [index for index in range(1, n + 1) if index not in core_indices]
        diagnostics.append(
            {
                "classification": "empirical_pattern",
                "lower_radius_decimal": str(group["lower_radius_decimal"]),
                "upper_radius_decimal": str(group["upper_radius_decimal"]),
                "candidate_orders": [list(order) for order in candidate_orders],
                "all_share_lower_pair_set": len({tuple(sorted(item)) for item in lower_sets}) == 1,
                "all_share_lower_pair_kind_signature": (
                    len({tuple(sorted(item)) for item in lower_kind_sets}) == 1
                ),
                "all_share_directed_cycle_signature": len(directed_signatures) == 1,
                "all_share_upper_minimum_pair_set": (
                    len({tuple(sorted(item)) for item in min_sets}) == 1
                ),
                "all_share_upper_near_minimum_pair_set": (
                    len({tuple(sorted(item)) for item in near_sets}) == 1
                ),
                "shared_lower_pair_core": _pair_records_from_tokens(lower_core),
                "common_reduced_subconfiguration_indices": core_indices,
                "indices_absent_from_lower_core": omitted,
                "diagnostic_assessment": {
                    "classification": "empirical_pattern",
                    "shared_negative_cycle_pair_set_supported": (
                        len({tuple(sorted(item)) for item in lower_sets}) == 1
                    ),
                    "same_active_pair_proxy_supported": (
                        len({tuple(sorted(item)) for item in lower_sets}) == 1
                    ),
                    "common_reduced_subconfiguration_supported": bool(omitted),
                    "uncaptured_symmetry_status": "unresolved_claim",
                    "numerical_coincidence_not_excluded": True,
                    "warning": (
                        "Identical serialized brackets do not prove exact equality "
                        "of fixed-order optima."
                    ),
                },
            }
        )
    return {
        "classification": "empirical_pattern",
        "candidate_groups": diagnostics,
        "warning": "Diagnostics are finite candidate-order proxies, not exact tie proofs.",
    }


def _cross_n_patterns(results: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    weak_indices = [
        result["possible_weakly_constrained_indices"]["indices"] for result in results
    ]
    lower_noncritical = [
        result["empirical_noncritical_indices"]["indices"] for result in results
    ]
    observed = []
    if weak_indices[-2:] == [[1], [1]]:
        observed.append(
            {
                "classification": "empirical_pattern",
                "name": "index_1_weak_proxy_in_multiple_candidate_cases",
                "n_values": [5, 6],
                "statement": (
                    "In the checked multiple-candidate cases, index 1 has the "
                    "lowest combined finite proxy incidence."
                ),
            }
        )
    if lower_noncritical[-2:] == [[1], [1]]:
        observed.append(
            {
                "classification": "empirical_pattern",
                "name": "index_1_absent_from_lower_cycle_core_for_n5_n6",
                "n_values": [5, 6],
                "statement": (
                    "In the checked multiple-candidate cases, index 1 is absent "
                    "from the lower critical-cycle pair sets."
                ),
            }
        )
    return {
        "classification": "empirical_pattern",
        "observed_patterns": observed,
        "warning": "Cross-n patterns cover only checked n=3..6 candidates.",
    }


def _oracle_from_record(record: Mapping[str, Any]) -> MPMathIntervalAngularOracle:
    metadata = _expect_mapping(record.get("theta_interval_backend"), "theta_interval_backend")
    digits = int(metadata["precision_digits"])
    guard = metadata.get("guard_decimal")
    if guard is not None and not isinstance(guard, str):
        raise ValueError("theta_interval_backend.guard_decimal must be a string")
    return MPMathIntervalAngularOracle(digits=digits, guard_decimal=guard)


def _minimum_pair_set(candidate: Mapping[str, Any]) -> set[str]:
    return {
        _pair_token_from_label(item["pair_label"])
        for item in candidate["upper_witness_slack_analysis"]["minimum_slack_pairs"]
    }


def _near_pair_set(candidate: Mapping[str, Any]) -> set[str]:
    return {
        _pair_token_from_label(item["pair_label"])
        for item in candidate["upper_witness_slack_analysis"]["near_minimum_pairs_by_rank"][
            "pairs"
        ]
    }


def _possible_weak_indices(n: int, combined_counts: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    counts = {int(item["index"]): int(item["count"]) for item in combined_counts}
    values = list(counts.values())
    if not values or len(set(values)) <= 1:
        indices: list[int] = []
        min_count = None
    else:
        min_count = min(values)
        indices = [
            index
            for index in range(1, n + 1)
            if counts[index] == min_count
            and int(combined_counts[index - 1]["lower_cycle_count"]) == 0
        ]
    return {
        "classification": "heuristic",
        "indices": indices,
        "minimum_combined_proxy_incidence": min_count,
        "rule": (
            "Indices absent from lower-cycle pairs and with minimum combined "
            "incidence across lower-cycle pairs, minimum-slack pairs, and "
            "top-ranked slack pairs. This is not a certified non-incidence "
            "statement."
        ),
    }


def _combined_index_counts(
    n: int,
    lower_counts: Counter[int],
    min_counts: Counter[int],
    near_counts: Counter[int],
) -> list[dict[str, Any]]:
    records = []
    for index in range(1, n + 1):
        lower = int(lower_counts[index])
        minimum = int(min_counts[index])
        near = int(near_counts[index])
        records.append(
            {
                "index": index,
                "radius": index * index,
                "lower_cycle_count": lower,
                "upper_minimum_slack_count": minimum,
                "upper_near_minimum_count": near,
                "count": lower + minimum + near,
            }
        )
    return records


def _pair_from_indices(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a <= b else (b, a)


def _pair_label(pair: tuple[int, int]) -> str:
    return f"{pair[0]}-{pair[1]}"


def _radius_pair_label(pair: tuple[int, int]) -> str:
    return f"{pair[0] * pair[0]}-{pair[1] * pair[1]}"


def _pair_token_from_label(label: str) -> str:
    a, b = _parse_pair_label(label)
    return f"{a}-{b}|radii={a * a}-{b * b}"


def _parse_pair_label(token_or_label: str) -> tuple[int, int]:
    label = token_or_label.split("|", 1)[0]
    left, right = label.split("-", 1)
    return int(left), int(right)


def _labels_to_indices(tokens: Iterable[str]) -> list[int]:
    indices = []
    for token in tokens:
        a, b = _parse_pair_label(token)
        indices.extend([a, b])
    return indices


def _pair_records_from_tokens(tokens: Iterable[str]) -> list[dict[str, Any]]:
    return [_pair_record_from_token(token) for token in sorted(tokens)]


def _pair_record_from_token(token: str) -> dict[str, Any]:
    a, b = _parse_pair_label(token)
    return {
        "pair_label": f"{a}-{b}",
        "index_pair": [a, b],
        "radius_pair": [a * a, b * b],
        "radius_pair_label": f"{a * a}-{b * b}",
    }


def _counter_records(counter: Counter[str]) -> list[dict[str, Any]]:
    return [
        {"label": label, "count": int(count)}
        for label, count in sorted(counter.items(), key=lambda item: (item[0], item[1]))
    ]


def _counter_pair_records(counter: Counter[str]) -> list[dict[str, Any]]:
    records = []
    for token, count in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
        record = _pair_record_from_token(token)
        record["count"] = int(count)
        records.append(record)
    return records


def _index_counts_from_pair_tokens(tokens: Iterable[str]) -> Counter[int]:
    counter: Counter[int] = Counter()
    counter.update(_labels_to_indices(tokens))
    return counter


def _index_counter_records(counter: Counter[int], *, n: int) -> list[dict[str, Any]]:
    return [
        {"index": index, "radius": index * index, "count": int(counter[index])}
        for index in range(1, n + 1)
    ]


def _intersection(sets: Sequence[set[Any]]) -> set[Any]:
    if not sets:
        return set()
    return set.intersection(*(set(item) for item in sets))


def _union(sets: Sequence[set[Any]]) -> set[Any]:
    result: set[Any] = set()
    for item in sets:
        result.update(item)
    return result


def _order_key(order: Sequence[int]) -> tuple[int, ...]:
    return tuple(int(item) for item in order)


def _mp_decimal_string(value: mp.mpf, *, digits: int = DEFAULT_DECIMAL_DIGITS) -> str:
    return mp.nstr(value, n=digits, strip_zeros=False, min_fixed=-10, max_fixed=80)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _created_at_utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _definitions_record() -> dict[str, str]:
    return {
        "lower_critical_cycle": (
            "The lower-endpoint negative cycle embedded in a verified local "
            "fixed-order interval bracket, translated from positional nodes to "
            "stable index and radius-pair labels."
        ),
        "normalized_directed_signature": (
            "A cyclic-rotation-normalized sequence of stable directed edge "
            "tokens. It preserves edge kind and source/target indices."
        ),
        "normalized_pair_set_signature": (
            "The sorted set of stable index/radius pair tokens in the lower "
            "negative cycle, ignoring traversal direction and edge kind."
        ),
        "upper_witness_slack_ranking": (
            "All-pairs interval-lower slack ranking at the certified upper "
            "witness. The ranking is a finite numerical diagnostic, not an "
            "exact active-contact certificate."
        ),
        "weakly_constrained_index": (
            "A heuristic label for an index absent from lower critical-cycle "
            "pairs and with minimum combined incidence in the finite proxy data. "
            "It is not a certified floating circle."
        ),
    }


def _classification_record() -> dict[str, dict[str, str]]:
    return {
        "finite_certificate_facts": {
            "classification": "computer_certified_result",
            "basis": "semantically validated finite-results summary and source certificates",
        },
        "lower_critical_cycle_signatures": {
            "classification": "verified_fact",
            "basis": "deterministic translation and normalization of embedded negative-cycle records",
        },
        "upper_witness_slack_rankings": {
            "classification": "numerical_observation",
            "basis": "deterministic interval-lower all-pairs slack recomputation at upper witnesses",
        },
        "candidate_common_core_intersections": {
            "classification": "empirical_pattern",
            "basis": "finite intersections across certified candidate orders",
        },
        "weakly_constrained_indices": {
            "classification": "heuristic",
            "basis": "threshold-free minimum combined proxy incidence in finite data",
        },
        "identical_bracket_group_diagnostics": {
            "classification": "empirical_pattern",
            "basis": "finite comparison of candidate orders with identical serialized local brackets",
        },
    }


def _limitations_record() -> list[str]:
    return [
        "Analyzes only checked finite n=3..6 certificates.",
        "Does not generate n=7 or any new finite certificate.",
        "Lower negative cycles are infeasibility certificates, not exact active contact graphs.",
        "Upper-witness slack rankings are finite numerical diagnostics at bracket upper endpoints.",
        "Weakly constrained indices are heuristic proxy labels, not certified floating circles.",
        "Identical serialized brackets do not prove exact equality of fixed-order optima.",
    ]


def _provenance_record(
    *,
    created_at_utc: str | None,
    command_summary: str,
) -> dict[str, Any]:
    return {
        "created_at_utc": created_at_utc or _created_at_utc_now(),
        "software": [
            {"name": "Python", "version": platform.python_version(), "role": "runtime"},
            {
                "name": "mpmath",
                "version": getattr(mp, "__version__", "unknown"),
                "role": "interval lower slack recomputation",
            },
            {
                "name": "power-ringmin",
                "version": "0.1.0",
                "role": "critical-structure analyzer",
            },
        ],
        "source_files": [
            {
                "path": "src/power_ringmin/critical_structure.py",
                "role": "critical-structure analysis",
            },
            {
                "path": "src/power_ringmin/finite_results.py",
                "role": "candidate-set source summary loader",
            },
            {
                "path": "src/power_ringmin/interval_verifier.py",
                "role": "guarded interval angular oracle",
            },
        ],
        "source_artifacts": [
            path.as_posix() for path in DEFAULT_CHECKED_ARTIFACT_PATHS
        ],
        "commands": [
            {
                "command": command_summary,
                "result": "pass",
                "output_summary": (
                    "Built structural diagnostics for certified candidate orders "
                    "from checked n=3..6 finite artifacts."
                ),
            }
        ],
        "randomness": {"used": False, "seeds": []},
    }


def _validate_classifications(value: Any) -> None:
    record = _expect_mapping(value, "evidence_classification_by_field")
    expected = set(_classification_record())
    if set(record) != expected:
        raise ValueError("evidence_classification_by_field keys do not match v1")
    allowed = {
        "definition",
        "verified_fact",
        "computer_certified_result",
        "numerical_observation",
        "empirical_pattern",
        "heuristic",
        "conjecture",
        "unresolved_claim",
    }
    for key, item in record.items():
        source = _expect_mapping(item, f"evidence_classification_by_field.{key}")
        if source.get("classification") not in allowed:
            raise ValueError(f"{key} has unsupported classification")
        if not isinstance(source.get("basis"), str) or not source["basis"]:
            raise ValueError(f"{key}.basis must be non-empty")


def _validate_result_shape(result: Mapping[str, Any]) -> None:
    facts = _expect_mapping(result.get("finite_certificate_facts"), "finite_certificate_facts")
    if facts.get("classification") != "computer_certified_result":
        raise ValueError("finite_certificate_facts classification is unsupported")
    candidates = _expect_list(result.get("candidate_order_analyses"), "candidate_order_analyses")
    if int(facts.get("candidate_set_size")) != len(candidates):
        raise ValueError("candidate count mismatch")
    for candidate in candidates:
        source = _expect_mapping(candidate, "candidate")
        lower = _expect_mapping(source.get("lower_critical_cycle"), "lower_critical_cycle")
        upper = _expect_mapping(
            source.get("upper_witness_slack_analysis"),
            "upper_witness_slack_analysis",
        )
        if lower.get("classification") != "verified_fact":
            raise ValueError("lower_critical_cycle classification is unsupported")
        if upper.get("classification") != "numerical_observation":
            raise ValueError("upper_witness_slack_analysis classification is unsupported")
        if not _expect_list(lower.get("normalized_pair_set_signature"), "pair_set"):
            raise ValueError("lower critical pair set must be non-empty")
        if not _expect_list(upper.get("all_pairs_by_slack_rank"), "slack rankings"):
            raise ValueError("slack rankings must be non-empty")


def _expect_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be a mapping")
    return value


def _expect_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
    return value


__all__ = [
    "COMMAND_NAME",
    "CRITICAL_STRUCTURE_ARTIFACT_TYPE",
    "CRITICAL_STRUCTURE_SCHEMA_VERSION",
    "DEFAULT_FINITE_RESULTS_SUMMARY_PATH",
    "DEFAULT_TOP_SLACK_PAIR_COUNT",
    "STRUCTURE_FORMAT_VERSION",
    "CriticalStructureAnalysis",
    "build_critical_structure_analysis",
    "build_parser",
    "dump_critical_structure_analysis",
    "dumps_critical_structure_analysis",
    "load_critical_structure_analysis",
    "loads_critical_structure_analysis",
    "main",
    "normalize_cyclic_signature",
    "validate_critical_structure_analysis_artifact",
]


if __name__ == "__main__":
    raise SystemExit(main())
