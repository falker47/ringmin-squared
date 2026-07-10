from __future__ import annotations

import json
from pathlib import Path
import tomllib

import pytest

from power_ringmin.export_fixed_order_batch_cli import main
from power_ringmin.fixed_order_artifact import load_fixed_order_artifact


def test_batch_cli_float64_radius_orders_export_artifacts(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    orders_json = tmp_path / "orders.json"
    orders_json.write_text(json.dumps([[16, 1, 9, 4], [1, 4, 9]]), encoding="utf-8")
    output_dir = tmp_path / "artifacts"

    exit_code = main(
        [
            str(orders_json),
            "--output-dir",
            str(output_dir),
            "--created-at-utc",
            "2026-07-10T00:00:00Z",
        ]
    )

    assert exit_code == 0
    stdout = capsys.readouterr().out
    assert "batch complete count=2" in stdout
    assert "backend=float64" in stdout

    paths = sorted(output_dir.glob("*.json"))
    assert [path.name for path in paths] == [
        "fixed_order_0001_n4.json",
        "fixed_order_0002_n3.json",
    ]

    first = load_fixed_order_artifact(paths[0])
    second = load_fixed_order_artifact(paths[1])
    assert first.index_order == (4, 1, 3, 2)
    assert first.radius_order == ("16", "1", "9", "4")
    assert second.index_order == (1, 2, 3)
    assert second.radius_order == ("1", "4", "9")

    artifact = first.to_dict()
    assert artifact["precision"]["primary_backend"] == "float64"
    assert artifact["provenance"]["created_at_utc"] == "2026-07-10T00:00:00Z"
    assert artifact["provenance"]["commands"][0]["command"].startswith(
        "power-ringmin-export-fixed-order-batch"
    )
    assert any(
        item["path"] == "src/power_ringmin/export_fixed_order_batch_cli.py"
        for item in artifact["provenance"]["source_files"]
    )


def test_batch_cli_mpmath_index_orders_export_artifact(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    orders_json = tmp_path / "index_orders.json"
    orders_json.write_text(json.dumps({"index_orders": [[1, 2, 3]]}), encoding="utf-8")
    output_dir = tmp_path / "artifacts"

    exit_code = main(
        [
            str(orders_json),
            "--order-kind",
            "index",
            "--backend",
            "mpmath",
            "--digits",
            "80",
            "--local-radius-eta",
            "1e-12",
            "--output-dir",
            str(output_dir),
            "--created-at-utc",
            "2026-07-10T00:00:00Z",
        ]
    )

    assert exit_code == 0
    assert "batch complete count=1" in capsys.readouterr().out

    loaded = load_fixed_order_artifact(output_dir / "fixed_order_0001_n3.json")
    artifact = loaded.to_dict()
    assert loaded.index_order == (1, 2, 3)
    assert loaded.radius_order == ("1", "4", "9")
    assert loaded.positions_rad is not None
    assert artifact["precision"]["primary_backend"] == "mpmath"
    assert artifact["precision"]["working_precision_digits"] == 80
    assert artifact["result"]["local_radius_bracket"]["claimed_radius_feasible"] is True


def test_batch_cli_rejects_non_quadratic_radius_order(tmp_path: Path) -> None:
    orders_json = tmp_path / "bad_orders.json"
    orders_json.write_text(json.dumps([[1, 2, 9]]), encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        main([str(orders_json), "--output-dir", str(tmp_path / "artifacts")])

    assert exc_info.value.code == 2


def test_batch_cli_refuses_to_overwrite_without_flag(tmp_path: Path) -> None:
    orders_json = tmp_path / "orders.json"
    orders_json.write_text(json.dumps([[1, 4, 9]]), encoding="utf-8")
    output_dir = tmp_path / "artifacts"

    assert main([str(orders_json), "--output-dir", str(output_dir)]) == 0

    with pytest.raises(SystemExit) as exc_info:
        main([str(orders_json), "--output-dir", str(output_dir)])

    assert exc_info.value.code == 2
    assert main([str(orders_json), "--output-dir", str(output_dir), "--overwrite"]) == 0


def test_batch_console_script_entry_point_is_registered() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"]["power-ringmin-export-fixed-order-batch"] == (
        "power_ringmin.export_fixed_order_batch_cli:main"
    )
