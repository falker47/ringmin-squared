from __future__ import annotations

import copy
from pathlib import Path

import pytest

from power_ringmin.interval_bracket_exporter import build_fixed_order_interval_bracket_record
from power_ringmin.search_small_n import canonical_index_orders
from power_ringmin.small_n_interval_certificate import (
    SMALL_N_INTERVAL_CERTIFICATE_SCHEMA_VERSION,
    build_n3_interval_certificate_fixture,
    build_small_n_interval_certificate,
    dump_small_n_interval_certificate_artifact,
    load_small_n_interval_certificate_artifact,
    validate_small_n_interval_certificate_artifact,
)


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
