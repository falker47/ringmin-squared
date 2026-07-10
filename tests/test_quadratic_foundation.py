from __future__ import annotations

import math
import random

import pytest

from power_ringmin.evaluator import chain_radius, full_radius, is_feasible
from power_ringmin.geometry import cycle_equivalent, quadratic_radii, theta
from power_ringmin.highprec import full_radius_mp, verify_fixed_order_mp
from power_ringmin.patterns import interleave, sequential, supnick_max_tour, supnick_min_tour


def test_quadratic_radii_and_theta_properties() -> None:
    radii = quadratic_radii(5)
    assert radii == (1, 4, 9, 16, 25)

    for R in (1.0, 10.0, 100.0, 1000.0):
        for a in radii[:4]:
            for b in radii[:4]:
                value = theta(R, a, b)
                assert 0.0 < value < math.pi
                assert value == pytest.approx(theta(R, b, a), abs=1e-15)
                assert theta(R * 1.5, a, b) < value


def test_n3_quadratic_fixed_order_matches_high_precision() -> None:
    order = quadratic_radii(3)
    result = full_radius(order)
    highprec = full_radius_mp(order, digits=80)

    assert result.feasible
    assert result.R_full == pytest.approx(result.R_chain, abs=1e-10)
    assert float(highprec) == pytest.approx(result.R_full, rel=1e-10, abs=1e-10)
    assert verify_fixed_order_mp(order, result.R_full * (1.0 + 1e-10), digits=80)
    assert not verify_fixed_order_mp(order, result.R_full * (1.0 - 1e-8), digits=80)


def test_quadratic_full_never_below_chain_on_samples() -> None:
    rng = random.Random(20260710)
    for _ in range(8):
        order = list(quadratic_radii(7))
        rng.shuffle(order)
        result = full_radius(tuple(order))
        assert result.R_full + 1e-10 >= result.R_chain
        assert chain_radius(tuple(order)) == pytest.approx(result.R_chain, abs=1e-11)
        assert is_feasible(tuple(order), result.R_full)
        assert len(result.positions) == len(order)


def test_rotation_reflection_invariance_quadratic_samples() -> None:
    rng = random.Random(4619480)
    for _ in range(8):
        order = list(quadratic_radii(6))
        rng.shuffle(order)
        base = full_radius(tuple(order)).R_full
        shift = rng.randrange(len(order))
        rotated = tuple(order[shift:] + order[:shift])
        reflected = tuple(reversed(order))
        assert full_radius(rotated).R_full == pytest.approx(base, abs=1e-9)
        assert full_radius(reflected).R_full == pytest.approx(base, abs=1e-9)


def test_pattern_helpers_on_quadratic_values() -> None:
    values = quadratic_radii(7)

    assert sequential(reversed(values)) == values
    assert set(interleave(values)) == set(values)
    assert cycle_equivalent(supnick_max_tour(values), interleave(values))
    assert supnick_min_tour(values) == (1, 9, 25, 49, 36, 16, 4)
