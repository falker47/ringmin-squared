from __future__ import annotations

import json
from pathlib import Path
import tomllib

import mpmath as mp
import pytest

from power_ringmin.export_fixed_order_batch_cli import export_batch_artifacts
from power_ringmin.verify_fixed_order_artifacts_cli import main


def test_batch_standalone_verifier_accepts_mpmath_artifact_directory(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_dir = tmp_path / "artifacts"
    export_batch_artifacts(
        [(1, 4, 9)],
        backend="mpmath",
        output_dir=output_dir,
        argv_for_provenance=["orders.json", "--backend", "mpmath"],
        digits=80,
        local_radius_eta="1e-12",
        created_at_utc="2026-07-10T00:00:00Z",
    )

    exit_code = main([str(output_dir), "--digits", "80"])

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "PASS" in stdout
    assert "fixed_order=PASS" in stdout
    assert "local=PASS" in stdout
    assert "batch standalone verification complete count=1 passed=1 failed=0" in stdout


def test_batch_standalone_verifier_accepts_float64_artifact_with_explicit_stn_tolerance(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_dir = tmp_path / "artifacts"
    export_batch_artifacts(
        [(16, 1, 9, 4)],
        backend="float64",
        output_dir=output_dir,
        argv_for_provenance=["orders.json"],
        created_at_utc="2026-07-10T00:00:00Z",
    )

    exit_code = main([str(output_dir), "--digits", "80", "--stn-tol", "1e-9"])

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "PASS" in stdout
    assert "stn_tol=1e-9" in stdout
    assert "fixed_order=PASS" in stdout
    assert "witness=PASS" in stdout


def test_batch_standalone_verifier_reports_failed_artifact(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_dir = tmp_path / "artifacts"
    export_batch_artifacts(
        [(1, 4, 9)],
        backend="mpmath",
        output_dir=output_dir,
        argv_for_provenance=["orders.json", "--backend", "mpmath"],
        digits=80,
        local_radius_eta="1e-12",
        created_at_utc="2026-07-10T00:00:00Z",
    )
    artifact_path = output_dir / "fixed_order_0001_n3.json"
    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
    radius = mp.mpf(artifact["result"]["central_radius"]["decimal"])
    artifact["result"]["central_radius"]["decimal"] = mp.nstr(radius - mp.mpf("1e-6"), 80)
    artifact_path.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")

    exit_code = main([str(output_dir), "--digits", "80", "--no-artifact-eta"])

    assert exit_code == 1
    stdout = capsys.readouterr().out
    assert "FAIL" in stdout
    assert "fixed_order=FAIL" in stdout
    assert "failed=1" in stdout


def test_batch_standalone_verifier_rejects_empty_directory(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main([str(tmp_path)])

    assert exc_info.value.code == 2


def test_batch_standalone_verifier_console_script_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"]["power-ringmin-verify-fixed-order-artifacts"] == (
        "power_ringmin.verify_fixed_order_artifacts_cli:main"
    )
