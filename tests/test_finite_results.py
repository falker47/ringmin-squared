from __future__ import annotations

from decimal import Decimal, localcontext
import json
from pathlib import Path
import tomllib

import pytest

from power_ringmin.finite_results import (
    COMMAND_NAME,
    analyze_checked_finite_results,
    analyze_finite_result_artifact,
    dumps_finite_results_summary,
    format_finite_results_markdown,
    main,
)
from power_ringmin.small_n_interval_certificate import (
    load_small_n_interval_certificate_artifact,
)


CHECKED_ARTIFACT_PATHS = (
    Path("examples/small_n_interval_certificate_n3.json"),
    Path("examples/small_n_interval_certificate_n4.json"),
    Path("examples/small_n_interval_certificate_n5.json"),
    Path("examples/small_n_interval_certificate_n6.json"),
)


@pytest.fixture(scope="module")
def checked_summary() -> dict:
    return analyze_checked_finite_results(CHECKED_ARTIFACT_PATHS)


def test_loads_all_checked_n3_to_n6_artifacts(checked_summary: dict) -> None:
    assert checked_summary["source_artifact_count"] == 4
    assert [result["n"] for result in checked_summary["results"]] == [3, 4, 5, 6]
    assert [
        result["source_artifact"]["path"] for result in checked_summary["results"]
    ] == [path.as_posix() for path in CHECKED_ARTIFACT_PATHS]


def test_candidate_set_semantics_and_current_sizes(checked_summary: dict) -> None:
    independently_derived_sizes = {}

    for path, result in zip(CHECKED_ARTIFACT_PATHS, checked_summary["results"], strict=True):
        artifact = load_small_n_interval_certificate_artifact(path).to_dict()
        upper = Decimal(str(artifact["result"]["global_upper_bound"]["radius_decimal"]))
        expected_candidate_orders = [
            summary["index_order"]
            for summary in artifact["local_bracket_summaries"]
            if Decimal(str(summary["lower_radius_decimal"])) <= upper
        ]
        actual_candidate_orders = [
            order["index_order"] for order in result["candidate_set"]["orders"]
        ]

        independently_derived_sizes[result["n"]] = len(expected_candidate_orders)
        assert actual_candidate_orders == expected_candidate_orders
        assert result["candidate_set"]["size"] == len(expected_candidate_orders)

    assert independently_derived_sizes == {3: 1, 4: 1, 5: 2, 6: 5}


def test_unique_candidate_and_multiple_candidate_classification(
    checked_summary: dict,
) -> None:
    by_n = _results_by_n(checked_summary)

    assert by_n[3]["candidate_set"]["classification"] == (
        "unique_certified_candidate_mod_rotation_reflection"
    )
    assert by_n[4]["candidate_set"]["classification"] == (
        "unique_certified_candidate_mod_rotation_reflection"
    )
    assert by_n[5]["candidate_set"]["classification"] == (
        "multiple_certified_candidates_no_exact_tie_claim"
    )
    assert by_n[6]["candidate_set"]["classification"] == (
        "multiple_certified_candidates_no_exact_tie_claim"
    )
    assert "not an exact tie claim" in by_n[5]["candidate_set"]["warning"]
    assert "not an exact tie claim" in by_n[6]["candidate_set"]["warning"]


def test_exclusion_gap_calculation(checked_summary: dict) -> None:
    by_n = _results_by_n(checked_summary)

    assert by_n[3]["excluded_orders"]["count"] == 0
    assert by_n[3]["excluded_orders"]["exclusion_gap_decimal"] is None

    for path in CHECKED_ARTIFACT_PATHS[1:]:
        artifact = load_small_n_interval_certificate_artifact(path).to_dict()
        n = int(artifact["instance"]["n"])
        with localcontext() as context:
            context.prec = 120
            upper = Decimal(str(artifact["result"]["global_upper_bound"]["radius_decimal"]))
            excluded_differences = [
                Decimal(str(summary["lower_radius_decimal"])) - upper
                for summary in artifact["local_bracket_summaries"]
                if Decimal(str(summary["lower_radius_decimal"])) > upper
            ]
        expected_gap = min(excluded_differences)

        assert by_n[n]["excluded_orders"]["count"] == len(excluded_differences)
        assert by_n[n]["excluded_orders"]["exclusion_gap_decimal"] == format(
            expected_gap,
            "f",
        )
        assert by_n[n]["excluded_orders"]["exclusion_gap_orders"]


def test_deterministic_ordering_and_serialization(checked_summary: dict) -> None:
    assert dumps_finite_results_summary(checked_summary) == dumps_finite_results_summary(
        checked_summary
    )
    assert [result["n"] for result in checked_summary["results"]] == [3, 4, 5, 6]

    for path, result in zip(CHECKED_ARTIFACT_PATHS, checked_summary["results"], strict=True):
        artifact = load_small_n_interval_certificate_artifact(path).to_dict()
        upper = Decimal(str(artifact["result"]["global_upper_bound"]["radius_decimal"]))
        expected_candidates = [
            summary["index_order"]
            for summary in artifact["local_bracket_summaries"]
            if Decimal(str(summary["lower_radius_decimal"])) <= upper
        ]
        expected_excluded = [
            summary["index_order"]
            for summary in artifact["local_bracket_summaries"]
            if Decimal(str(summary["lower_radius_decimal"])) > upper
        ]

        assert [order["index_order"] for order in result["candidate_set"]["orders"]] == (
            expected_candidates
        )
        assert [order["index_order"] for order in result["excluded_orders"]["orders"]] == (
            expected_excluded
        )


def test_preserves_source_decimal_strings(checked_summary: dict) -> None:
    for path, result in zip(CHECKED_ARTIFACT_PATHS, checked_summary["results"], strict=True):
        artifact = load_small_n_interval_certificate_artifact(path).to_dict()
        first_candidate = result["candidate_set"]["orders"][0]
        first_candidate_order = first_candidate["index_order"]
        matching_summary = next(
            summary
            for summary in artifact["local_bracket_summaries"]
            if summary["index_order"] == first_candidate_order
        )

        assert result["global_bracket"]["lower_endpoint_decimal"] == str(
            artifact["result"]["global_lower_bound"]["radius_decimal"]
        )
        assert result["global_bracket"]["upper_endpoint_decimal"] == str(
            artifact["result"]["global_upper_bound"]["radius_decimal"]
        )
        assert first_candidate["lower_radius_decimal"] == matching_summary["lower_radius_decimal"]
        assert first_candidate["upper_radius_decimal"] == matching_summary["upper_radius_decimal"]


def test_identical_serialized_local_bracket_groups(checked_summary: dict) -> None:
    for path, result in zip(CHECKED_ARTIFACT_PATHS, checked_summary["results"], strict=True):
        artifact = load_small_n_interval_certificate_artifact(path).to_dict()
        grouped: dict[tuple[str, str], list[list[int]]] = {}
        for summary in artifact["local_bracket_summaries"]:
            key = (
                str(summary["lower_radius_decimal"]),
                str(summary["upper_radius_decimal"]),
            )
            grouped.setdefault(key, []).append(summary["index_order"])

        expected_groups = {
            key: orders for key, orders in grouped.items() if len(orders) > 1
        }
        actual_groups = {
            (
                group["lower_radius_decimal"],
                group["upper_radius_decimal"],
            ): [order["index_order"] for order in group["orders"]]
            for group in result["identical_serialized_local_bracket_groups"]
        }

        assert actual_groups == expected_groups
        for group in result["identical_serialized_local_bracket_groups"]:
            assert "not an exact equality claim" in group["warning"]


def test_rejects_tampered_or_incomplete_certificate_data(tmp_path: Path) -> None:
    artifact = load_small_n_interval_certificate_artifact(CHECKED_ARTIFACT_PATHS[0]).to_dict()
    artifact.pop("local_brackets")
    tampered = tmp_path / "tampered_n3_certificate.json"
    tampered.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    with pytest.raises(ValueError, match="local_brackets"):
        analyze_finite_result_artifact(tampered)


def test_all_orders_remain_candidates_case_is_handled(checked_summary: dict) -> None:
    n3 = _results_by_n(checked_summary)[3]

    assert n3["canonical_order_count"] == 1
    assert n3["candidate_set"]["size"] == n3["canonical_order_count"]
    assert n3["excluded_orders"]["count"] == 0
    assert n3["excluded_orders"]["exclusion_gap_decimal"] is None
    assert n3["excluded_orders"]["exclusion_gap_orders"] == []


def test_non_overclaiming_language_in_generated_summaries(checked_summary: dict) -> None:
    markdown = format_finite_results_markdown(checked_summary)
    claims = checked_summary["claims_and_limitations"]

    assert "not an exact tie claim" in markdown
    assert "not certified asymptotic claims" in markdown
    assert "not an exact tie claim" in claims["multiple_candidate_warning"]
    assert "never certified asymptotic claims" in claims["asymptotic_diagnostics"]
    assert "proves an exact tie" not in markdown.lower()
    assert "asymptotic theorem" not in markdown.lower()


def test_cli_writes_json_and_markdown_outputs(tmp_path: Path) -> None:
    json_output = tmp_path / "finite_results.json"
    markdown_output = tmp_path / "finite_results.md"

    assert main([str(CHECKED_ARTIFACT_PATHS[0]), "--output", str(json_output)]) == 0
    assert main(
        [
            str(CHECKED_ARTIFACT_PATHS[0]),
            "--format",
            "markdown",
            "--output",
            str(markdown_output),
        ]
    ) == 0

    payload = json.loads(json_output.read_text(encoding="utf-8"))
    assert [result["n"] for result in payload["results"]] == [3]
    assert "| n | canonical orders |" in markdown_output.read_text(encoding="utf-8")


def test_finite_results_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"][COMMAND_NAME] == "power_ringmin.finite_results:main"


def _results_by_n(summary: dict) -> dict[int, dict]:
    return {int(result["n"]): result for result in summary["results"]}
