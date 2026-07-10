from __future__ import annotations

from pathlib import Path
import tomllib

import pytest

from power_ringmin.export_fixed_order_cli import main
from power_ringmin.fixed_order_artifact import load_fixed_order_artifact, verifier_payload_from_artifact


def test_cli_float64_radius_order_exports_artifact(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / "fixed_order_float64.json"

    exit_code = main(
        [
            "--order",
            "16,1,9,4",
            "--output",
            str(output),
            "--created-at-utc",
            "2026-07-10T00:00:00Z",
        ]
    )

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "wrote" in stdout
    assert "backend=float64" in stdout

    loaded = load_fixed_order_artifact(output)
    artifact = loaded.to_dict()
    assert loaded.index_order == (4, 1, 3, 2)
    assert loaded.radius_order == ("16", "1", "9", "4")
    assert artifact["precision"]["primary_backend"] == "float64"
    assert artifact["result"]["binding_structure"]["essential_tight_pairs"]
    assert artifact["evidence"]["classification"] == "numerical_observation"
    assert artifact["evidence"]["claim"]["scope"] == "fixed_order_radius_bracket"
    assert artifact["provenance"]["created_at_utc"] == "2026-07-10T00:00:00Z"
    assert artifact["provenance"]["commands"][0]["command"].startswith(
        "power-ringmin-export-fixed-order --order 16,1,9,4"
    )
    assert any(
        item["path"] == "src/power_ringmin/export_fixed_order_cli.py"
        for item in artifact["provenance"]["source_files"]
    )


def test_cli_mpmath_index_order_exports_verifier_payload(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / "fixed_order_mpmath.json"

    exit_code = main(
        [
            "--index-order",
            "1,2,3",
            "--backend",
            "mpmath",
            "--digits",
            "80",
            "--local-radius-eta",
            "1e-12",
            "--output",
            str(output),
            "--created-at-utc",
            "2026-07-10T00:00:00Z",
        ]
    )

    assert exit_code == 0
    assert "backend=mpmath" in capsys.readouterr().out

    loaded = load_fixed_order_artifact(output)
    artifact = loaded.to_dict()
    assert loaded.index_order == (1, 2, 3)
    assert loaded.radius_order == ("1", "4", "9")
    assert loaded.positions_rad is not None
    assert artifact["precision"]["primary_backend"] == "mpmath"
    assert artifact["precision"]["working_precision_digits"] == 80
    assert artifact["result"]["local_radius_bracket"]["lower_radius_feasible"] is False
    assert artifact["result"]["local_radius_bracket"]["claimed_radius_feasible"] is True

    payload = verifier_payload_from_artifact(loaded)
    assert payload["ordering"] == ["1", "4", "9"]
    assert payload["R_mpmath_full"] == loaded.central_radius_decimal
    assert "positions" in payload


def test_cli_rejects_non_quadratic_radius_order(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--order", "1,2,9", "--output", str(tmp_path / "bad.json")])

    assert exc_info.value.code == 2


def test_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"]["power-ringmin-export-fixed-order"] == (
        "power_ringmin.export_fixed_order_cli:main"
    )
