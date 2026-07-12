from __future__ import annotations

import json
from pathlib import Path
import tomllib

from power_ringmin.critical_structure import (
    COMMAND_NAME,
    CRITICAL_STRUCTURE_ARTIFACT_TYPE,
    CRITICAL_STRUCTURE_SCHEMA_VERSION,
    build_critical_structure_analysis,
    dumps_critical_structure_analysis,
    load_critical_structure_analysis,
    main,
    normalize_cyclic_signature,
    validate_critical_structure_analysis_artifact,
)


FIXED_CREATED_AT = "2026-07-12T00:00:00Z"
FIXED_COMMAND = (
    "power-ringmin-analyze-critical-structure --created-at-utc "
    "2026-07-12T00:00:00Z --output "
    "ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json"
)


def test_normalize_cyclic_signature_is_rotation_invariant() -> None:
    signature = ("c", "d", "a", "b")
    rotated = ("a", "b", "c", "d")

    assert normalize_cyclic_signature(signature) == normalize_cyclic_signature(rotated)
    assert normalize_cyclic_signature(signature) == ("a", "b", "c", "d")


def test_checked_candidate_structure_has_expected_critical_cores() -> None:
    analysis = build_critical_structure_analysis(
        created_at_utc=FIXED_CREATED_AT,
        command_summary=FIXED_COMMAND,
    )
    validate_critical_structure_analysis_artifact(analysis)
    by_n = _results_by_n(analysis)

    assert analysis["schema_version"] == CRITICAL_STRUCTURE_SCHEMA_VERSION
    assert analysis["artifact_type"] == CRITICAL_STRUCTURE_ARTIFACT_TYPE
    assert analysis["analysis_scope"]["n_values"] == [3, 4, 5, 6]
    assert analysis["analysis_scope"]["n7_generated"] is False
    assert [by_n[n]["finite_certificate_facts"]["candidate_set_size"] for n in (3, 4, 5, 6)] == [
        1,
        1,
        2,
        5,
    ]

    assert _lower_core_labels(by_n[5]) == ["2-4", "2-5", "3-4", "3-5"]
    assert _lower_core_labels(by_n[6]) == ["2-5", "2-6", "3-4", "3-6", "4-5"]
    assert by_n[5]["empirical_noncritical_indices"]["indices"] == [1]
    assert by_n[6]["empirical_noncritical_indices"]["indices"] == [1]
    assert by_n[5]["possible_weakly_constrained_indices"]["indices"] == [1]
    assert by_n[6]["possible_weakly_constrained_indices"]["indices"] == [1]
    assert by_n[3]["possible_weakly_constrained_indices"]["indices"] == []
    assert by_n[4]["possible_weakly_constrained_indices"]["indices"] == []


def test_identical_bracket_diagnostics_do_not_claim_exact_ties() -> None:
    analysis = build_critical_structure_analysis(
        created_at_utc=FIXED_CREATED_AT,
        command_summary=FIXED_COMMAND,
    )
    by_n = _results_by_n(analysis)

    for n, expected_core_indices in ((5, [2, 3, 4, 5]), (6, [2, 3, 4, 5, 6])):
        groups = by_n[n]["identical_bracket_group_diagnostics"]["candidate_groups"]
        assert len(groups) == 1
        group = groups[0]
        assert group["all_share_lower_pair_set"] is True
        assert group["all_share_directed_cycle_signature"] is False
        assert group["all_share_upper_minimum_pair_set"] is False
        assert group["common_reduced_subconfiguration_indices"] == expected_core_indices
        assert group["indices_absent_from_lower_core"] == [1]
        assert group["diagnostic_assessment"]["uncaptured_symmetry_status"] == (
            "unresolved_claim"
        )
        assert group["diagnostic_assessment"]["numerical_coincidence_not_excluded"] is True
        assert "do not prove exact equality" in group["diagnostic_assessment"]["warning"]


def test_deterministic_generation_and_loader_round_trip(tmp_path: Path) -> None:
    first = build_critical_structure_analysis(
        created_at_utc=FIXED_CREATED_AT,
        command_summary=FIXED_COMMAND,
    )
    second = build_critical_structure_analysis(
        created_at_utc=FIXED_CREATED_AT,
        command_summary=FIXED_COMMAND,
    )

    assert dumps_critical_structure_analysis(first) == dumps_critical_structure_analysis(second)

    output = tmp_path / "critical_structure.json"
    output.write_text(dumps_critical_structure_analysis(first), encoding="utf-8")
    loaded = load_critical_structure_analysis(output)

    assert loaded.n_values == (3, 4, 5, 6)
    assert loaded.to_dict() == first


def test_cli_writes_json_and_console_script_is_registered(tmp_path: Path) -> None:
    output = tmp_path / "critical_structure.json"

    assert main(["--created-at-utc", FIXED_CREATED_AT, "--output", str(output)]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))

    assert payload["schema_version"] == CRITICAL_STRUCTURE_SCHEMA_VERSION
    assert payload["analysis_scope"]["n7_generated"] is False

    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    assert pyproject["project"]["scripts"][COMMAND_NAME] == (
        "power_ringmin.critical_structure:main"
    )


def _results_by_n(analysis: dict) -> dict[int, dict]:
    return {int(result["n"]): result for result in analysis["results"]}


def _lower_core_labels(result: dict) -> list[str]:
    return [
        item["pair_label"]
        for item in result["candidate_common_core_intersections"]["lower_cycle_pair_core"]
    ]
