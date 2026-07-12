from __future__ import annotations

from fractions import Fraction
import math

from power_ringmin.geometry import theta


def _p_direct(m: int, n: int) -> int:
    return sum(k * (m + n - k) for k in range(m, n + 1))


def _theta_majorant(R: float, j: int) -> float:
    return 2 * j / math.sqrt(R * (R + j * j + 1))


def test_theta_majorant_diagnostic_samples() -> None:
    for R in (0.1, 1.0, 27.5, 47.0, 100.0, 10_000.0):
        for j in (2, 3, 7, 12, 13, 50):
            value = theta(R, 1, j * j)
            majorant = _theta_majorant(R, j)
            assert value < majorant < 2 * j / R


def test_n12_exact_rational_majorants() -> None:
    assert _p_direct(6, 12) == 539
    assert Fraction(7 * 539, 22) - 144 == Fraction(55, 2)

    numerators = (134, 187, 229, 261, 285, 304, 318, 329, 337, 344, 349)
    expected_margins = (
        192_700,
        247_125,
        698_695,
        892_085,
        291_375,
        3_846_400,
        4_936_700,
        7_762_845,
        5_297_815,
        10_035_520,
        7_173_975,
    )
    margins = tuple(
        k * k * 55 * (57 + 2 * j * j) - 16_000_000 * j * j
        for j, k in zip(range(2, 13), numerators, strict=True)
    )

    assert margins == expected_margins
    assert all(margin > 0 for margin in margins)
    assert sum(numerators) == 3_077
    assert Fraction(sum(numerators), 1_000) < Fraction(31, 10)

    boundary_sum = sum(theta(27.5, 1, j * j) for j in range(2, 13))
    assert boundary_sum < 3.077 < 3.1 < math.pi


def test_n13_integral_majorant_exact_checks() -> None:
    assert _p_direct(6, 13) == 680
    assert Fraction(7 * 680, 22) - 169 == Fraction(521, 11)
    assert Fraction(521, 11) > 47
    assert 107 * 107 < 47 * 244
    assert 49 * 49 < 47 * 52
    assert Fraction(384, 156) == Fraction(32, 13) < 3

    boundary_sum = sum(theta(47.0, 1, j * j) for j in range(2, 14))
    assert boundary_sum < 32 / 13 < 3 < math.pi


def test_uniform_n14_parity_bounds_are_exact_diagnostics() -> None:
    for t in range(7, 201):
        even_n = 2 * t
        even_p = _p_direct(t, even_n)
        assert even_p == t * (t + 1) * (13 * t - 1) // 6
        even_margin = 42 * (
            Fraction(even_p) - Fraction(29 * even_n * even_n, 7) - even_n + 2
        )
        u = t - 7
        assert even_margin == 91 * u**3 + 1_299 * u**2 + 4_718 * u + 672
        assert even_margin > 0

        odd_n = 2 * t + 1
        odd_p = _p_direct(t, odd_n)
        assert odd_p == t * (t + 2) * (13 * t + 7) // 6
        odd_margin = 42 * (
            Fraction(odd_p) - Fraction(29 * odd_n * odd_n, 7) - odd_n + 2
        )
        assert odd_margin == 91 * u**3 + 1_446 * u**2 + 6_185 * u + 3_522
        assert odd_margin > 0


def test_documented_sufficient_threshold_branches() -> None:
    covered = {12, 13}
    covered.update(range(14, 101))

    assert min(covered) == 12
    assert all(n in covered for n in range(12, 101))
    assert 11 not in covered
