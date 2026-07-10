from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp
import pytest

from power_ringmin.evaluator import full_radius
from power_ringmin.geometry import quadratic_radii
from power_ringmin.highprec import full_radius_mp, recover_positions_mp
import verify as standalone_verify


def test_slsqp_fixed_order_cross_validation_quadratic_n4() -> None:
    pytest.importorskip("numpy")
    pytest.importorskip("scipy.optimize")

    from power_ringmin import crosscheck
    from power_ringmin.crosscheck import slsqp_fixed_order

    assert not hasattr(crosscheck, "slsqp_unconstrained_global")

    order = (16, 1, 9, 4)
    exact = full_radius(order)
    check = slsqp_fixed_order(order, starts=8, seed=20260710)

    assert check.success
    assert check.starts_attempted == 8
    assert check.min_pair_margin >= -1e-6
    assert check.min_order_margin >= -1e-6
    assert check.R == pytest.approx(exact.R_full, rel=1e-7, abs=1e-6)


def test_standalone_verifier_accepts_fixed_order_payload(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    order = quadratic_radii(3)
    R = full_radius_mp(order, digits=90)
    positions = recover_positions_mp(order, R, digits=90)
    payload = {
        "ordering": list(order),
        "R_mpmath_full": mp.nstr(R, 90),
        "positions": [mp.nstr(position, 90) for position in positions],
    }
    path = tmp_path / "fixed_order.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "verify.py",
            "--input",
            str(path),
            "--digits",
            "90",
            "--eta",
            "1e-20",
        ],
    )

    assert standalone_verify.main() == 0
    stdout = capsys.readouterr().out
    assert "fixed_order=PASS" in stdout
    assert "local=PASS" in stdout
    assert "witness=PASS" in stdout


def test_standalone_verifier_rejects_too_small_radius(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    order = quadratic_radii(3)
    R = full_radius_mp(order, digits=80)
    too_small = mp.nstr(R - mp.mpf("1e-8"), 80)

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "verify.py",
            "--order",
            ",".join(str(value) for value in order),
            "--radius",
            too_small,
            "--digits",
            "80",
        ],
    )

    assert standalone_verify.main() == 1
    assert "fixed_order=FAIL" in capsys.readouterr().out
