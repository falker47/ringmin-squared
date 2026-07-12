from __future__ import annotations

import copy
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path
import shutil
import tomllib

import pytest

from power_ringmin.finite_results import (
    COMMAND_NAME,
    FINITE_RESULTS_SUMMARY_ARTIFACT_TYPE,
    FINITE_RESULTS_SUMMARY_SCHEMA_VERSION,
    build_finite_results_summary,
    dump_finite_results_summary,
    dumps_finite_results_summary,
    format_finite_results_markdown,
    load_finite_results_summary,
    main,
    source_content_sha256,
    validate_finite_results_summary_artifact,
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
CHECKED_SUMMARY_PATH = Path("examples/finite_results_summary_n3_n6.json")
FIXED_CREATED_AT = "2026-07-12T00:00:00Z"
FIXED_COMMAND = (
    "power-ringmin-analyze-finite-results --created-at-utc "
    "2026-07-12T00:00:00Z --output examples/finite_results_summary_n3_n6.json"
)


@pytest.fixture(scope="module")
def checked_summary() -> dict:
    return build_finite_results_summary(
        CHECKED_ARTIFACT_PATHS,
        created_at_utc=FIXED_CREATED_AT,
        command_summary=FIXED_COMMAND,
    )


def test_finite_results_summary_schema_contract() -> None:
    schema = json.loads(Path("schemas/finite_results_summary.schema.json").read_text())

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["properties"]["schema_version"]["const"] == (
        FINITE_RESULTS_SUMMARY_SCHEMA_VERSION
    )
    assert schema["properties"]["artifact_type"]["const"] == (
        FINITE_RESULTS_SUMMARY_ARTIFACT_TYPE
    )
    required = set(schema["required"])
    assert {
        "summary_scope",
        "source_certificates",
        "results",
        "cross_n_analysis",
        "provenance",
        "limitations",
    } <= required
    assert schema["$defs"]["sourceCertificate"]["properties"]["content_sha256"][
        "$ref"
    ] == "#/$defs/sha256"
    assert "CRLF" in schema["$defs"]["sourceCertificate"]["properties"][
        "content_sha256"
    ]["description"]
    assert "lone CR" in schema["$defs"]["sourceCertificate"]["properties"][
        "content_sha256"
    ]["description"]
    assert schema["$defs"]["candidateSet"]["properties"]["classification"]["const"] == (
        "computer_certified_result"
    )
    assert schema["$defs"]["asymptoticRatios"]["properties"]["classification"]["const"] == (
        "numerical_observation"
    )


def test_checked_summary_has_v1_structure_and_source_hashes(checked_summary: dict) -> None:
    validate_finite_results_summary_artifact(checked_summary)

    assert checked_summary["schema_version"] == FINITE_RESULTS_SUMMARY_SCHEMA_VERSION
    assert checked_summary["artifact_type"] == FINITE_RESULTS_SUMMARY_ARTIFACT_TYPE
    assert checked_summary["source_certificate_count"] == 4
    assert checked_summary["summary_scope"]["n_values"] == [3, 4, 5, 6]
    assert [result["n"] for result in checked_summary["results"]] == [3, 4, 5, 6]

    for source, path in zip(
        checked_summary["source_certificates"],
        CHECKED_ARTIFACT_PATHS,
        strict=True,
    ):
        expected_hash = source_content_sha256(path)
        assert source["path"] == path.as_posix()
        assert source["content_sha256"] == expected_hash
        assert source["artifact_type"] == "small_n_interval_certificate"
        assert source["evidence_classification"] == "computer_certified_result"


def test_source_content_sha256_normalizes_line_endings_only(tmp_path: Path) -> None:
    chunk_minus_one = 1024 * 1024 - 1
    normalized = b"a" * chunk_minus_one + b"\nsecond line\n"
    lf_path = tmp_path / "source_lf.json"
    crlf_path = tmp_path / "source_crlf.json"
    cr_path = tmp_path / "source_cr.json"
    changed_path = tmp_path / "source_changed.json"

    lf_path.write_bytes(normalized)
    crlf_path.write_bytes(b"a" * chunk_minus_one + b"\r\nsecond line\r\n")
    cr_path.write_bytes(b"a" * chunk_minus_one + b"\rsecond line\r")
    changed_path.write_bytes(b"a" * chunk_minus_one + b"\nsecond line!\n")

    expected = hashlib.sha256(normalized).hexdigest()
    assert source_content_sha256(lf_path) == expected
    assert source_content_sha256(crlf_path) == expected
    assert source_content_sha256(cr_path) == expected
    assert source_content_sha256(changed_path) != expected


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
        assert result["candidate_set"]["classification"] == "computer_certified_result"

    assert independently_derived_sizes == {3: 1, 4: 1, 5: 2, 6: 5}


def test_unique_and_multiple_candidate_classification(checked_summary: dict) -> None:
    by_n = _results_by_n(checked_summary)

    assert by_n[3]["candidate_set"]["multiplicity_interpretation"] == (
        "unique_certified_candidate_mod_rotation_reflection"
    )
    assert by_n[4]["candidate_set"]["multiplicity_interpretation"] == (
        "unique_certified_candidate_mod_rotation_reflection"
    )
    assert by_n[5]["candidate_set"]["multiplicity_interpretation"] == (
        "multiple_certified_candidates_no_exact_tie_claim"
    )
    assert by_n[6]["candidate_set"]["multiplicity_interpretation"] == (
        "multiple_certified_candidates_no_exact_tie_claim"
    )
    assert "not an exact tie claim" in by_n[5]["candidate_set"]["warning"]
    assert "not an exact tie claim" in by_n[6]["candidate_set"]["warning"]


def test_exclusion_gap_calculation(checked_summary: dict) -> None:
    by_n = _results_by_n(checked_summary)

    assert by_n[3]["excluded_orders"]["count"] == 0
    assert by_n[3]["excluded_orders"]["exclusion_gap"]["defined"] is False
    assert by_n[3]["excluded_orders"]["exclusion_gap"]["gap_decimal"] is None

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

        excluded = by_n[n]["excluded_orders"]
        assert excluded["count"] == len(excluded_differences)
        assert excluded["exclusion_gap"]["gap_decimal"] == format(expected_gap, "f")
        assert excluded["exclusion_gap"]["orders"]


def test_identical_serialized_bracket_groups(checked_summary: dict) -> None:
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
            for group in result["identical_serialized_bracket_groups"]["groups"]
        }

        assert actual_groups == expected_groups
        assert result["identical_serialized_bracket_groups"]["classification"] == (
            "verified_fact"
        )
        assert "not an exact equality claim" in result[
            "identical_serialized_bracket_groups"
        ]["warning"]


def test_cross_n_ratios_and_trends_are_non_certifying(checked_summary: dict) -> None:
    classifications = checked_summary["evidence_classification_by_category"]
    cross_n = checked_summary["cross_n_analysis"]

    assert classifications["ratios_to_reference"]["classification"] == (
        "numerical_observation"
    )
    assert classifications["cross_n_trends"]["classification"] == "empirical_pattern"
    assert cross_n["classification"] == "empirical_pattern"
    assert cross_n["finite_sequences"]["candidate_set_sizes"] == [1, 1, 2, 5]
    assert cross_n["finite_sequences"]["excluded_order_counts"] == [0, 2, 10, 55]
    assert all(
        result["exploratory_asymptotic_ratios"]["classification"]
        == "numerical_observation"
        for result in checked_summary["results"]
    )
    serialized = json.dumps(checked_summary).lower()
    assert "asymptotic theorem" not in serialized
    assert "for all n" not in serialized


def test_summary_validation_detects_stale_source_hash(tmp_path: Path) -> None:
    source_path = tmp_path / "n3_certificate.json"
    shutil.copyfile(CHECKED_ARTIFACT_PATHS[0], source_path)
    summary = build_finite_results_summary(
        [source_path],
        created_at_utc=FIXED_CREATED_AT,
        command_summary="test fixed summary",
    )

    source_artifact = json.loads(source_path.read_text(encoding="utf-8"))
    source_artifact["provenance"]["commands"][0]["output_summary"] += " changed"
    source_path.write_text(json.dumps(source_artifact, indent=2), encoding="utf-8")

    with pytest.raises(ValueError, match="source_certificates"):
        validate_finite_results_summary_artifact(summary)


def test_summary_validation_accepts_source_line_ending_only_changes(tmp_path: Path) -> None:
    source_path = tmp_path / "n3_certificate.json"
    lf_source = CHECKED_ARTIFACT_PATHS[0].read_bytes().replace(b"\r\n", b"\n").replace(
        b"\r", b"\n"
    )
    source_path.write_bytes(lf_source)
    summary = build_finite_results_summary(
        [source_path],
        created_at_utc=FIXED_CREATED_AT,
        command_summary="test fixed summary",
    )

    source_path.write_bytes(lf_source.replace(b"\n", b"\r\n"))

    validate_finite_results_summary_artifact(summary)


def test_summary_validation_detects_tampered_candidate_content(checked_summary: dict) -> None:
    tampered = copy.deepcopy(checked_summary)
    tampered["results"][1]["candidate_set"]["size"] = 2

    with pytest.raises(ValueError, match="results are stale"):
        validate_finite_results_summary_artifact(tampered)


def test_dump_load_helpers_round_trip_and_revalidate_sources(
    checked_summary: dict,
    tmp_path: Path,
) -> None:
    output = tmp_path / "finite_results_summary.json"

    dump_finite_results_summary(checked_summary, output)
    loaded = load_finite_results_summary(output)

    assert loaded.n_values == (3, 4, 5, 6)
    assert loaded.source_certificate_count == 4
    assert loaded.to_dict() == checked_summary


def test_checked_artifact_loader() -> None:
    loaded = load_finite_results_summary(CHECKED_SUMMARY_PATH)
    artifact = loaded.to_dict()

    assert loaded.n_values == (3, 4, 5, 6)
    assert artifact["schema_version"] == FINITE_RESULTS_SUMMARY_SCHEMA_VERSION
    assert artifact["source_certificate_count"] == 4
    assert _results_by_n(artifact)[6]["candidate_set"]["size"] == 5


def test_deterministic_generation(checked_summary: dict) -> None:
    regenerated = build_finite_results_summary(
        CHECKED_ARTIFACT_PATHS,
        created_at_utc=FIXED_CREATED_AT,
        command_summary=FIXED_COMMAND,
    )

    assert dumps_finite_results_summary(regenerated) == dumps_finite_results_summary(
        checked_summary
    )


def test_cli_writes_json_and_markdown_outputs(tmp_path: Path) -> None:
    json_output = tmp_path / "finite_results.json"
    markdown_output = tmp_path / "finite_results.md"

    assert main(
        [
            str(CHECKED_ARTIFACT_PATHS[0]),
            "--created-at-utc",
            FIXED_CREATED_AT,
            "--output",
            str(json_output),
        ]
    ) == 0
    assert main(
        [
            str(CHECKED_ARTIFACT_PATHS[0]),
            "--format",
            "markdown",
            "--created-at-utc",
            FIXED_CREATED_AT,
            "--output",
            str(markdown_output),
        ]
    ) == 0

    payload = load_finite_results_summary(json_output).to_dict()
    assert [result["n"] for result in payload["results"]] == [3]
    markdown = markdown_output.read_text(encoding="utf-8")
    assert "| n | canonical orders |" in markdown
    assert "not an exact tie claim" in markdown


def test_finite_results_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"][COMMAND_NAME] == "power_ringmin.finite_results:main"


def _results_by_n(summary: dict) -> dict[int, dict]:
    return {int(result["n"]): result for result in summary["results"]}
