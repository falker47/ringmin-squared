from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_DIR = ROOT / "examples" / "fixed_order_batch_end_to_end"


def test_fixed_order_batch_end_to_end_example_exports_and_verifies(
    tmp_path: Path,
) -> None:
    output_dir = tmp_path / "artifacts"
    env = _source_checkout_env()

    export_completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "power_ringmin.export_fixed_order_batch_cli",
            str(EXAMPLE_DIR / "index_orders.json"),
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
        ],
        cwd=ROOT,
        env=env,
        check=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
    )

    assert "batch complete count=2" in export_completed.stdout
    assert sorted(path.name for path in output_dir.glob("*.json")) == [
        "fixed_order_0001_n3.json",
        "fixed_order_0002_n3.json",
    ]

    verify_completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "power_ringmin.verify_fixed_order_artifacts_cli",
            str(output_dir),
            "--digits",
            "80",
        ],
        cwd=ROOT,
        env=env,
        check=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
    )

    assert "fixed_order=PASS" in verify_completed.stdout
    assert "local=PASS" in verify_completed.stdout
    assert "batch standalone verification complete count=2 passed=2 failed=0" in (
        verify_completed.stdout
    )


def _source_checkout_env() -> dict[str, str]:
    env = os.environ.copy()
    source_path = str(ROOT / "src")
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = source_path if not existing else source_path + os.pathsep + existing
    return env
