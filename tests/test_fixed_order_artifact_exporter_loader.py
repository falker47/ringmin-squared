from __future__ import annotations

import copy
from pathlib import Path

import mpmath as mp
import pytest

import verify as standalone_verify
from power_ringmin.evaluator import full_radius
from power_ringmin.fixed_order_artifact import (
    SCHEMA_VERSION,
    dump_fixed_order_artifact,
    dumps_fixed_order_artifact,
    export_full_result_artifact,
    export_highprec_artifact,
    load_fixed_order_artifact,
    loads_fixed_order_artifact,
    validate_fixed_order_artifact,
    verifier_payload_from_artifact,
)
from power_ringmin.geometry import quadratic_radii
from power_ringmin.highprec import full_radius_mp, recover_positions_mp


FIXED_REPOSITORY = {
    "git_commit": None,
    "git_dirty": True,
    "notes": "Deterministic test artifact.",
}
FIXED_COMMANDS = [
    {
        "command": "pytest exporter test",
        "cwd": str(Path.cwd()),
        "result": "pass",
        "output_summary": "Constructed in a focused unit test.",
    }
]


def test_export_full_result_artifact_round_trips(tmp_path: Path) -> None:
    result = full_radius((16, 1, 9, 4))
    artifact = export_full_result_artifact(
        result,
        created_at_utc="2026-07-10T00:00:00Z",
        repository=FIXED_REPOSITORY,
        commands=FIXED_COMMANDS,
    )

    validate_fixed_order_artifact(artifact)
    assert artifact["schema_version"] == SCHEMA_VERSION
    assert artifact["fixed_order"]["index_order"] == [4, 1, 3, 2]
    assert artifact["fixed_order"]["radius_order"] == ["16", "1", "9", "4"]
    assert artifact["result"]["feasible"] is True
    assert artifact["result"]["binding_structure"]["essential_tight_pairs"]

    path = tmp_path / "fixed_order_artifact.json"
    dump_fixed_order_artifact(artifact, path)
    loaded = load_fixed_order_artifact(path)

    assert loaded.n == 4
    assert loaded.index_order == (4, 1, 3, 2)
    assert loaded.radius_order == ("16", "1", "9", "4")
    assert loaded.central_radius_decimal == artifact["result"]["central_radius"]["decimal"]
    assert loads_fixed_order_artifact(dumps_fixed_order_artifact(loaded)).to_dict() == loaded.to_dict()


def test_export_highprec_artifact_derives_standalone_verifier_payload() -> None:
    order = quadratic_radii(3)
    digits = 80
    radius = full_radius_mp(order, digits=digits)
    positions = recover_positions_mp(order, radius, digits=digits)
    artifact = export_highprec_artifact(
        order,
        radius,
        positions=positions,
        chain_radius=radius,
        digits=digits,
        local_radius_eta="1e-15",
        created_at_utc="2026-07-10T00:00:00Z",
        repository=FIXED_REPOSITORY,
        commands=FIXED_COMMANDS,
    )

    loaded = loads_fixed_order_artifact(dumps_fixed_order_artifact(artifact))
    payload = verifier_payload_from_artifact(loaded)
    assert payload == loaded.to_verifier_payload()
    assert payload["ordering"] == ["1", "4", "9"]

    mp.mp.dps = digits
    verifier_order = standalone_verify._as_mpf_order(payload["ordering"])
    verifier_radius = mp.mpf(payload["R_mpmath_full"])
    messages: list[str] = []
    assert standalone_verify.feasible(verifier_order, verifier_radius, mp.mpf("1e-40"))
    assert standalone_verify.check_witness(verifier_order, verifier_radius, payload["positions"], messages)
    assert messages == []

    bracket = loaded.to_dict()["result"]["local_radius_bracket"]
    assert bracket["lower_radius_feasible"] is False
    assert bracket["claimed_radius_feasible"] is True
    assert bracket["upper_radius_feasible"] is True


def test_loader_rejects_fixed_order_radius_mismatch() -> None:
    result = full_radius(quadratic_radii(3))
    artifact = export_full_result_artifact(
        result,
        created_at_utc="2026-07-10T00:00:00Z",
        repository=FIXED_REPOSITORY,
        commands=FIXED_COMMANDS,
    )
    broken = copy.deepcopy(artifact)
    broken["fixed_order"]["radius_order"][1] = "9"

    with pytest.raises(ValueError, match="does not match index_order"):
        validate_fixed_order_artifact(broken)
