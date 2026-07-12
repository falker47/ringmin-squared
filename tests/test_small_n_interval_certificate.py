from __future__ import annotations

import copy
import json
from pathlib import Path
import tomllib

import pytest

from power_ringmin.interval_bracket_exporter import build_fixed_order_interval_bracket_record
from power_ringmin.search_small_n import canonical_index_orders
from power_ringmin.small_n_interval_certificate import (
    COMMAND_NAME,
    N4_COMMAND_NAME,
    SMALL_N_COMMAND_NAME,
    SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION,
    build_n3_interval_certificate_fixture,
    build_n4_interval_certificate_fixture,
    build_small_n_interval_certificate,
    dump_small_n_interval_certificate_artifact,
    load_small_n_interval_certificate_artifact,
    main,
    main_n4,
    main_small_n,
    validate_small_n_interval_certificate_artifact,
)


def test_small_n_interval_certificate_schema_contract_and_examples() -> None:
    schema = json.loads(Path("schemas/small_n_interval_certificate.schema.json").read_text())

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["properties"]["schema_version"]["const"] == (
        SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION
    )
    assert schema["properties"]["artifact_type"]["const"] == "small_n_interval_certificate"
    assert "aggregation_method" in schema["required"]
    assert "local_brackets" in schema["required"]
    assert schema["properties"]["evidence"]["$ref"] == "#/$defs/evidence"

    for path in (
        Path("examples/small_n_interval_certificate_n3.json"),
        Path("examples/small_n_interval_certificate_n4.json"),
        Path("examples/small_n_interval_certificate_n5.json"),
    ):
        artifact = json.loads(path.read_text(encoding="utf-8"))
        validate_small_n_interval_certificate_artifact(artifact)
        assert artifact["schema_version"] == SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION
        assert artifact["artifact_type"] == schema["properties"]["artifact_type"]["const"]
        assert artifact["evidence"]["classification"] == "computer_certified_result"


def test_n3_interval_certificate_fixture_covers_every_canonical_order() -> None:
    artifact = build_n3_interval_certificate_fixture(
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )

    validate_small_n_interval_certificate_artifact(artifact)

    local = artifact["local_brackets"][0]
    assert artifact["schema_version"] == SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION
    assert artifact["artifact_type"] == "small_n_interval_certificate"
    assert artifact["instance"]["n"] == 3
    assert artifact["order_space"]["expected_canonical_count"] == 1
    assert artifact["order_space"]["covered_canonical_count"] == 1
    assert [tuple(item["index_order"]) for item in artifact["local_bracket_summaries"]] == [(3, 1, 2)]
    assert local["index_order"] == [3, 1, 2]
    assert local["radius_order"] == [9, 1, 4]
    assert artifact["result"]["global_lower_bound"]["radius_decimal"] == local["lower_radius_decimal"]
    assert artifact["result"]["global_lower_bound"]["included"] is False
    assert artifact["result"]["global_upper_bound"]["radius_decimal"] == local["upper_radius_decimal"]
    assert artifact["result"]["global_upper_bound"]["included"] is True
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_n4_interval_certificate_fixture_covers_every_canonical_order() -> None:
    artifact = build_n4_interval_certificate_fixture(
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        max_canonical_orders=3,
        local_max_attempts=8,
        created_at_utc="2026-07-11T00:00:00Z",
    )

    validate_small_n_interval_certificate_artifact(artifact)

    assert artifact["instance"]["n"] == 4
    assert artifact["order_space"]["expected_canonical_count"] == 3
    assert artifact["order_space"]["covered_canonical_count"] == 3
    assert [tuple(item["index_order"]) for item in artifact["local_bracket_summaries"]] == [
        (4, 1, 2, 3),
        (4, 1, 3, 2),
        (4, 2, 1, 3),
    ]
    assert artifact["result"]["global_lower_bound"]["source_index_order"] == [4, 1, 3, 2]
    assert artifact["result"]["global_upper_bound"]["source_index_order"] == [4, 1, 3, 2]
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_n4_interval_certificate_fixture_enforces_order_space_bound() -> None:
    with pytest.raises(ValueError, match="exceeding max_canonical_orders=2"):
        build_n4_interval_certificate_fixture(
            digits=80,
            guard_decimal="1e-70",
            radius_eta="1e-4",
            max_canonical_orders=2,
            created_at_utc="2026-07-11T00:00:00Z",
        )


def test_small_n_interval_certificate_dump_load_round_trips(tmp_path: Path) -> None:
    artifact = build_n3_interval_certificate_fixture(
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )
    output = tmp_path / "n3_global_interval_certificate.json"

    dump_small_n_interval_certificate_artifact(artifact, output)
    loaded = load_small_n_interval_certificate_artifact(output)

    assert loaded.n == 3
    assert loaded.covered_canonical_count == 1
    assert loaded.lower_radius_decimal == artifact["result"]["global_lower_bound"]["radius_decimal"]
    assert loaded.upper_radius_decimal == artifact["result"]["global_upper_bound"]["radius_decimal"]
    assert loaded.to_dict() == artifact


def test_small_n_interval_certificate_rejects_missing_duplicate_and_wrong_n() -> None:
    record = build_fixed_order_interval_bracket_record(
        next(canonical_index_orders(3)),
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )

    with pytest.raises(ValueError, match="coverage mismatch"):
        build_small_n_interval_certificate([], n=3)

    with pytest.raises(ValueError, match="duplicate local bracket"):
        build_small_n_interval_certificate([record, record], n=3)

    with pytest.raises(ValueError, match="does not match n=4"):
        build_small_n_interval_certificate([record], n=4)


def test_small_n_interval_certificate_validation_rechecks_embedded_local_brackets() -> None:
    artifact = build_n3_interval_certificate_fixture(
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )
    broken = copy.deepcopy(artifact)
    broken["local_brackets"][0]["upper_certificate"]["positions_rad"][1] = "0"

    with pytest.raises(ValueError, match="upper witness"):
        validate_small_n_interval_certificate_artifact(broken)

    broken_bound = copy.deepcopy(artifact)
    broken_bound["result"]["global_upper_bound"]["radius_decimal"] = "1"
    with pytest.raises(ValueError, match="global_upper_bound"):
        validate_small_n_interval_certificate_artifact(broken_bound)

    broken_summary = copy.deepcopy(artifact)
    broken_summary["local_bracket_summaries"][0]["min_upper_witness_slack_lower_decimal"] = "0"
    with pytest.raises(ValueError, match="min_upper_witness_slack_lower_decimal"):
        validate_small_n_interval_certificate_artifact(broken_summary)

    broken_method = copy.deepcopy(artifact)
    broken_method["aggregation_method"]["local_verifier"] = "some.other.verifier"
    with pytest.raises(ValueError, match="aggregation_method.local_verifier"):
        validate_small_n_interval_certificate_artifact(broken_method)


def test_small_n_interval_certificate_rejects_embedded_local_artifact_type_tampering() -> None:
    artifact = build_n3_interval_certificate_fixture(
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )
    broken = copy.deepcopy(artifact)
    broken["local_brackets"][0]["artifact_type"] = "fixed_order_numerical_result"

    with pytest.raises(ValueError, match="artifact_type"):
        validate_small_n_interval_certificate_artifact(broken)


def test_small_n_interval_certificate_rejects_embedded_backend_policy_tampering() -> None:
    artifact = build_n3_interval_certificate_fixture(
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )
    broken = copy.deepcopy(artifact)
    broken["local_brackets"][0]["theta_interval_backend"]["rounding_policy"] = (
        "mpmath.iv interval arithmetic"
    )

    with pytest.raises(ValueError, match="rounding_policy"):
        validate_small_n_interval_certificate_artifact(broken)


def test_n3_interval_certificate_cli_writes_checked_finite_artifact(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / "n3_interval_certificate.json"

    exit_code = main(
        [
            "--output",
            str(output),
            "--digits",
            "80",
            "--guard-decimal",
            "1e-70",
            "--radius-eta",
            "1e-4",
            "--created-at-utc",
            "2026-07-11T00:00:00Z",
        ]
    )

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "classification=computer_certified_result" in stdout
    assert "covered=1" in stdout

    loaded = load_small_n_interval_certificate_artifact(output)
    artifact = loaded.to_dict()
    assert loaded.n == 3
    assert loaded.covered_canonical_count == 1
    assert artifact["provenance"]["created_at_utc"] == "2026-07-11T00:00:00Z"
    assert artifact["provenance"]["commands"][0]["command"].startswith(
        f"{COMMAND_NAME} --output"
    )
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert artifact["evidence"]["claim"]["scope"] == "finite_global_small_n_interval_bracket"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_n4_interval_certificate_cli_writes_checked_finite_artifact(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / "n4_interval_certificate.json"

    exit_code = main_n4(
        [
            "--output",
            str(output),
            "--digits",
            "80",
            "--guard-decimal",
            "1e-70",
            "--radius-eta",
            "1e-4",
            "--max-canonical-orders",
            "3",
            "--local-max-attempts",
            "8",
            "--created-at-utc",
            "2026-07-11T00:00:00Z",
        ]
    )

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "classification=computer_certified_result" in stdout
    assert "covered=3" in stdout

    loaded = load_small_n_interval_certificate_artifact(output)
    artifact = loaded.to_dict()
    assert loaded.n == 4
    assert loaded.covered_canonical_count == 3
    assert artifact["provenance"]["created_at_utc"] == "2026-07-11T00:00:00Z"
    assert artifact["provenance"]["commands"][0]["command"].startswith(
        f"{N4_COMMAND_NAME} --output"
    )
    assert artifact["result"]["global_lower_bound"]["source_index_order"] == [4, 1, 3, 2]
    assert artifact["result"]["global_upper_bound"]["source_index_order"] == [4, 1, 3, 2]
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert artifact["evidence"]["claim"]["scope"] == "finite_global_small_n_interval_bracket"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_small_n_interval_certificate_cli_dry_run_reports_n5_order_count(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main_small_n(
        [
            "--n",
            "5",
            "--max-canonical-orders",
            "12",
            "--dry-run",
        ]
    )

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "preflight n=5" in stdout
    assert "canonical_orders=12" in stdout
    assert "generation_allowed=true" in stdout


def test_small_n_interval_certificate_cli_writes_bounded_n3_artifact(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / "small_n3_interval_certificate.json"

    exit_code = main_small_n(
        [
            "--n",
            "3",
            "--max-canonical-orders",
            "1",
            "--output",
            str(output),
            "--digits",
            "80",
            "--guard-decimal",
            "1e-70",
            "--radius-eta",
            "1e-4",
            "--local-max-attempts",
            "8",
            "--created-at-utc",
            "2026-07-11T00:00:00Z",
        ]
    )

    assert exit_code == 0
    assert "covered=1" in capsys.readouterr().out

    loaded = load_small_n_interval_certificate_artifact(output)
    artifact = loaded.to_dict()
    assert loaded.n == 3
    assert artifact["provenance"]["commands"][0]["command"].startswith(
        f"{SMALL_N_COMMAND_NAME} --n 3"
    )
    assert artifact["order_space"]["covered_canonical_count"] == 1


def test_small_n_interval_certificate_cli_refuses_unbounded_larger_generation(
    tmp_path: Path,
) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main_small_n(
            [
                "--n",
                "5",
                "--max-canonical-orders",
                "11",
                "--output",
                str(tmp_path / "n5.json"),
            ]
        )

    assert exc_info.value.code == 2


def test_checked_n3_interval_certificate_artifact_loads() -> None:
    path = Path("examples/small_n_interval_certificate_n3.json")

    loaded = load_small_n_interval_certificate_artifact(path)
    artifact = loaded.to_dict()

    assert loaded.n == 3
    assert loaded.covered_canonical_count == 1
    assert artifact["local_bracket_summaries"][0]["index_order"] == [3, 1, 2]
    assert artifact["local_bracket_summaries"][0]["radius_order"] == [9, 1, 4]
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert artifact["evidence"]["claim"]["scope"] == "finite_global_small_n_interval_bracket"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_checked_n4_interval_certificate_artifact_loads() -> None:
    path = Path("examples/small_n_interval_certificate_n4.json")

    loaded = load_small_n_interval_certificate_artifact(path)
    artifact = loaded.to_dict()

    assert loaded.n == 4
    assert loaded.covered_canonical_count == 3
    assert [tuple(item["index_order"]) for item in artifact["local_bracket_summaries"]] == [
        (4, 1, 2, 3),
        (4, 1, 3, 2),
        (4, 2, 1, 3),
    ]
    assert artifact["result"]["global_lower_bound"]["source_index_order"] == [4, 1, 3, 2]
    assert artifact["result"]["global_upper_bound"]["source_index_order"] == [4, 1, 3, 2]
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert artifact["evidence"]["claim"]["scope"] == "finite_global_small_n_interval_bracket"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_checked_n5_interval_certificate_artifact_loads() -> None:
    path = Path("examples/small_n_interval_certificate_n5.json")

    loaded = load_small_n_interval_certificate_artifact(path)
    artifact = loaded.to_dict()

    assert loaded.n == 5
    assert loaded.covered_canonical_count == 12
    assert artifact["order_space"]["expected_canonical_count"] == 12
    assert artifact["provenance"]["repository"]["git_dirty"] is False
    assert artifact["result"]["global_lower_bound"]["source_index_order"] == [5, 1, 3, 4, 2]
    assert artifact["result"]["global_upper_bound"]["source_index_order"] == [5, 1, 3, 4, 2]
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert artifact["evidence"]["claim"]["scope"] == "finite_global_small_n_interval_bracket"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_checked_n6_interval_certificate_artifact_loads() -> None:
    path = Path("examples/small_n_interval_certificate_n6.json")

    loaded = load_small_n_interval_certificate_artifact(path)
    artifact = loaded.to_dict()

    assert loaded.n == 6
    assert loaded.covered_canonical_count == 60
    assert artifact["order_space"]["expected_canonical_count"] == 60
    assert artifact["provenance"]["repository"]["git_dirty"] is False
    assert artifact["result"]["global_lower_bound"]["source_index_order"] == [6, 1, 2, 5, 4, 3]
    assert artifact["result"]["global_upper_bound"]["source_index_order"] == [6, 1, 2, 5, 4, 3]
    assert artifact["evidence"]["classification"] == "computer_certified_result"
    assert artifact["evidence"]["claim"]["scope"] == "finite_global_small_n_interval_bracket"
    assert "No theorem for all n." in artifact["evidence"]["limitations"]


def test_n3_interval_certificate_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"][COMMAND_NAME] == (
        "power_ringmin.small_n_interval_certificate:main"
    )


def test_n4_interval_certificate_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"][N4_COMMAND_NAME] == (
        "power_ringmin.small_n_interval_certificate:main_n4"
    )


def test_small_n_interval_certificate_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"][SMALL_N_COMMAND_NAME] == (
        "power_ringmin.small_n_interval_certificate:main_small_n"
    )
