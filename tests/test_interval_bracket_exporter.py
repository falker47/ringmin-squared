from __future__ import annotations

import copy
from pathlib import Path
import tomllib

import pytest

from power_ringmin.interval_bracket_exporter import (
    build_fixed_order_interval_bracket_record,
    dump_fixed_order_interval_bracket_record,
    load_fixed_order_interval_bracket_record,
    main,
)
from power_ringmin.interval_verifier import (
    FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION,
    MPMathIntervalAngularOracle,
    verify_fixed_order_interval_bracket,
)


def test_build_interval_bracket_record_verifies_n3_order() -> None:
    oracle = MPMathIntervalAngularOracle(digits=80, guard_decimal="1e-70")

    record = build_fixed_order_interval_bracket_record(
        (3, 1, 2),
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )

    result = verify_fixed_order_interval_bracket(record, oracle=oracle)
    assert result.verified
    assert record["schema_version"] == FIXED_ORDER_INTERVAL_BRACKET_SCHEMA_VERSION
    assert record["artifact_type"] == "fixed_order_interval_bracket"
    assert record["index_order"] == [3, 1, 2]
    assert record["radius_order"] == [9, 1, 4]
    assert record["generator"]["verified"] is True
    assert record["theta_interval_backend"] == oracle.backend_info.to_record()
    assert result.lower_negative_cycle_sum_upper < 0
    assert result.min_upper_witness_slack_lower > 0

    cycle = record["lower_certificate"]["cycle"]
    assert len(cycle) >= 2
    assert all(edge["target"] == nxt["source"] for edge, nxt in zip(cycle, cycle[1:] + cycle[:1]))
    assert record["upper_certificate"]["positions_rad"][0] == "0.0"
    assert record["evidence"]["classification"] == "computer_certified_result"
    assert "not a global small-n certificate" in record["evidence"]["claim"]["statement"]


def test_interval_bracket_record_dump_load_round_trips(tmp_path: Path) -> None:
    record = build_fixed_order_interval_bracket_record(
        (3, 1, 2),
        digits=80,
        guard_decimal="1e-70",
        radius_eta="1e-4",
        created_at_utc="2026-07-11T00:00:00Z",
    )
    output = tmp_path / "interval_bracket.json"

    dump_fixed_order_interval_bracket_record(record, output)
    loaded = load_fixed_order_interval_bracket_record(output)

    assert loaded.index_order == (3, 1, 2)
    assert loaded.radius_order == (9, 1, 4)
    assert loaded.to_dict() == record

    broken = copy.deepcopy(record)
    broken["upper_certificate"]["positions_rad"][1] = "0"
    with pytest.raises(ValueError, match="upper witness"):
        dump_fixed_order_interval_bracket_record(broken, tmp_path / "broken.json")


def test_interval_bracket_cli_writes_verifier_consumable_record(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / "interval_bracket_cli.json"

    exit_code = main(
        [
            "--index-order",
            "3,1,2",
            "--digits",
            "80",
            "--guard-decimal",
            "1e-70",
            "--radius-eta",
            "1e-4",
            "--output",
            str(output),
            "--created-at-utc",
            "2026-07-11T00:00:00Z",
        ]
    )

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "wrote" in stdout
    assert "bracket=[" in stdout

    loaded = load_fixed_order_interval_bracket_record(output)
    record = loaded.to_dict()
    assert loaded.index_order == (3, 1, 2)
    assert record["provenance"]["created_at_utc"] == "2026-07-11T00:00:00Z"
    assert record["provenance"]["commands"][0]["command"].startswith(
        "power-ringmin-export-fixed-order-interval-bracket --index-order 3,1,2"
    )
    assert any(
        item["path"] == "src/power_ringmin/interval_bracket_exporter.py"
        for item in record["provenance"]["source_files"]
    )


def test_interval_bracket_exporter_rejects_noncanonical_order(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(
            [
                "--index-order",
                "1,2,3",
                "--output",
                str(tmp_path / "bad.json"),
            ]
        )

    assert exc_info.value.code == 2


def test_interval_bracket_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"]["power-ringmin-export-fixed-order-interval-bracket"] == (
        "power_ringmin.interval_bracket_exporter:main"
    )
