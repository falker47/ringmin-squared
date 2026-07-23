"""Exact discriminants for PG49/KPGZERO filtered cardinality.

This standalone script imports only the Python standard library.  It checks
the exact filtered predicate on accepted and rejected primitive parameters,
constructs only prescribed PG44--PG46 interval shifts, and directly scores
one moderate PG49-supported core.  It performs no matching, subset, cyclic-
order, path-assignment, or permutation-family enumeration.

The all-parameter statements remain the symbolic proofs in the research
notes.  In particular, this finite diagnostic does not decide whether the
filtered cubic-convergent set is finite or infinite.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


LEFT = (
    4,
    11_116_408_784,
    7_852_541_895,
)
LEFT_BELOW = (
    1,
    445_038_621_131_943_653_377_466_928,
    314_371_708_097_094_017_492_647_115,
)
RIGHT = (
    19,
    7_473_073_805_813_661_315_256_495_159_240_494_740_302_603_139_227,
    5_278_919_324_111_360_426_689_943_587_091_134_465_306_838_560_333,
)


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the exact ceiling of a nonnegative quotient."""
    assert numerator >= 0 and denominator > 0
    return (numerator + denominator - 1) // denominator


def kappa(m: int, j: int) -> int:
    """Return the exact PG49 column threshold."""
    d = 8 * m + 4
    return ceil_div(j * (d - 1), 2 * (d + j))


def path(m: int, k: int) -> tuple[int, ...]:
    """Return the retained oriented scaffold path P_k."""
    d = 8 * m + 4
    assert 0 <= k < 2 * m
    if k <= m:
        return d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k
    return (4 * m + 2 + k,)


def interval_shift(m: int, k: int, j: int) -> tuple[int, ...]:
    """Construct exactly the PG44, PG45, or PG46 witness for (k,j)."""
    v = 2 * m
    assert 0 <= j < v and 0 <= k < v
    alpha = list(range(v))
    if j < k:
        alpha[j] = k
        for i in range(j + 1, k + 1):
            alpha[i] = i - 1
    elif j > k:
        for i in range(k, j):
            alpha[i] = i + 1
        alpha[j] = k
    return tuple(alpha)


def check_supported(m: int, alpha: tuple[int, ...]) -> None:
    """Check bijectivity and every literal PG49 support edge."""
    v = 2 * m
    assert len(alpha) == v
    assert sorted(alpha) == list(range(v))
    assert alpha[0] == 0
    for j in range(1, v):
        assert alpha[j] >= kappa(m, j)


def core_order(m: int, alpha: tuple[int, ...]) -> tuple[int, ...]:
    """Expand one prescribed scaffold assignment from the canonical cut."""
    n = 10 * m + 3
    d = 8 * m + 4
    v = 2 * m
    order: list[int] = []
    for j, k in enumerate(alpha):
        order.extend((d + j, 4 * m - 2 * j))
        order.extend(path(m, k))
        order.append(4 * m + 1 - 2 * ((j + 1) % v))
    result = tuple(order)
    assert len(result) == n - 1
    assert sorted(result) == list(range(2, n + 1))
    return result


def product_distance_score(order: tuple[int, ...]) -> Fraction:
    """Directly score all unordered core pairs for one fixed order."""
    size = len(order)
    score = Fraction(0)
    for left_position, left in enumerate(order):
        for right_position in range(left_position + 1, size):
            gap = right_position - left_position
            distance = min(gap, size - gap)
            score = max(score, Fraction(left * order[right_position], distance))
    return score


def parameters(
    side: int, g: int, u: int, w: int
) -> tuple[int, int, int] | None:
    """Evaluate KPGZERO-3, rejecting nonintegral primitive data."""
    assert side in (0, 1)
    if not (g > 0 and u > w > 0 and gcd(u, w) == 1):
        return None
    j_numerator = g * u * (u - w) - (4 + 3 * side)
    m_numerator = g * u * (2 * u + 3 * w) - (8 + side)
    r_numerator = g * (10 * w * w - 4 * u * u - u * w) + (6 - 3 * side)
    if j_numerator % 5 or m_numerator % 20 or r_numerator % 10:
        return None
    return (
        m_numerator // 20,
        j_numerator // 5,
        r_numerator // 10,
    )


def cubic_form(u: int, w: int) -> int:
    """Return Phi(u,w) from KPGZERO-9."""
    return 50 * w**3 + 51 * u * w**2 - 27 * u * u * w - 24 * u**3


def residuals(side: int, g: int, u: int, w: int) -> tuple[int, int]:
    """Return the exact (N_delta,Q_delta) plateau residuals."""
    phi = cubic_form(u, w)
    if side == 0:
        return (
            g * g * u * phi
            + g * (7 * u * u + 18 * u * w + 50 * w * w)
            + 31,
            g * g * u * phi - 3 * g * u * (u - w) - 4,
        )
    return (
        g * g * u * phi + 2 * g * u * (13 * u + 12 * w) - 6,
        g * g * u * phi
        + g * (16 * u * u + 9 * u * w - 50 * w * w)
        + 14,
    )


def literal_gains(m: int, j: int, r: int) -> tuple[int, int]:
    """Return KPGMIN-7 left and right insertion gains."""
    left = (
        j * j
        - 26 * j * m
        - 3 * j * r
        - 7 * j
        + 8 * m * m
        - 4 * m * r
        - 12 * m
        - 4 * r
        - 4
    )
    return left, left - j - 16 * m - 2 * r - 7


def singleton_gain(m: int, j: int, k: int, side: int) -> int:
    """Evaluate one local insertion gain for a singleton P_k in G_j."""
    assert m < k < 2 * m
    if side == 0:
        low = 4 * m - 2 * j
        terminal = 8 * m + 4 + j
    else:
        low = 4 * m - 2 * j - 1
        terminal = 8 * m + 5 + j
    singleton = 4 * m + 2 + k
    return low * (terminal + singleton) - terminal * singleton


def filtered(side: int, g: int, u: int, w: int) -> bool:
    """Evaluate every exact KPGZERO filter, with no generated convergents."""
    row = parameters(side, g, u, w)
    if row is None:
        return False
    m, j, r = row
    if not (m >= 3 and 1 <= j < m and r >= 1):
        return False
    if not (r == kappa(m, j) == kappa(m, j + 1)):
        return False
    if literal_gains(m, j, r)[side] != 0:
        return False
    upper, lower = residuals(side, g, u, w)
    return upper >= 0 and lower < 0


def phi(value: Fraction) -> Fraction:
    """Evaluate the decreasing cubic phi(t) exactly."""
    return 50 + 51 * value - 27 * value**2 - 24 * value**3


def check_legendre_bracket(u: int, w: int) -> None:
    """Bracket xi inside the strict Legendre interval around u/w."""
    lower = Fraction(2 * u * w - 1, 2 * w * w)
    upper = Fraction(2 * u * w + 1, 2 * w * w)
    assert lower > Fraction(7, 5)
    assert phi(lower) > 0 > phi(upper)


def check_pg49_boundary_and_supported_false_positive() -> None:
    """Separate exact PG49 support from the stricter KPGZERO predicate."""
    m = 34
    d = 8 * m + 4

    assert kappa(m, 24) == 11
    assert 24 * (d - 1 - 2 * 11) == 2 * 11 * d == 6_072
    boundary = interval_shift(m, 11, 24)
    check_supported(m, boundary)
    assert 10 < kappa(m, 24)

    false_row = parameters(1, 1, 13, 9)
    assert false_row == (34, 9, 2)
    false_m, false_j, false_r = false_row
    false_k = false_r + 2 * false_m - 1 - false_j
    assert false_k == 60
    assert singleton_gain(false_m, false_j, false_k, 1) == 0
    assert literal_gains(false_m, false_j, false_r) == (564, 0)
    assert kappa(false_m, false_j) == kappa(false_m, false_j + 1) == 5
    assert not filtered(1, 1, 13, 9)

    supported = interval_shift(false_m, false_k, false_j)
    check_supported(false_m, supported)
    order = core_order(false_m, supported)
    expected_w = Fraction(d * (d - 1), 2)
    assert product_distance_score(order) == expected_w

    actual_r = kappa(false_m, false_j)
    actual_k = actual_r + 2 * false_m - 1 - false_j
    assert actual_k == 63
    assert literal_gains(false_m, false_j, actual_r) == (63, -507)


def check_infinite_unfiltered_ray() -> None:
    """Check discriminating rows of the exact affine support-only false ray."""
    for t in (0, 1, 17):
        g = 20 * t + 1
        row = parameters(1, g, 13, 9)
        assert row == (689 * t + 34, 208 * t + 9, 34 * t + 2)
        m, j, r = row
        k = r + 2 * m - 1 - j
        assert k == 1_204 * t + 60
        assert m < k < 2 * m
        assert singleton_gain(m, j, k, 1) == 0
        assert j > 0 and k >= kappa(m, j)

        d = 8 * m + 4
        c_j = 2 * r * (d + j) - j * (d - 1)
        c_next = 2 * r * (d + j + 1) - (j + 1) * (d - 1)
        assert c_j == -757_536 * t * t - 64_548 * t - 1_335
        assert c_next == -757_536 * t * t - 69_992 * t - 1_606
        assert c_j < 0 and c_next < 0
        assert not filtered(1, g, 13, 9)


def check_true_filters_and_scale_rejections() -> None:
    """Check both branches, both left-branch signs, and adjacent scales."""
    left_g, left_u, left_w = LEFT
    assert filtered(0, left_g, left_u, left_w)
    left_row = parameters(0, left_g, left_u, left_w)
    assert left_row == (
        101_805_057_120_180_546_870,
        29_025_982_843_749_082_380,
        14_013_559_766_810_587_979,
    )
    assert cubic_form(left_u, left_w) == -106_362_375_186
    assert literal_gains(*left_row) == (0, -1_685_934_016_300_259_008_265)
    assert (9 * left_u * (2 * left_u + 3 * left_w)) % 20 == 8
    rejected_upper, _ = residuals(0, 9, left_u, left_w)
    assert rejected_upper < 0
    assert not filtered(0, 9, left_u, left_w)
    check_legendre_bracket(left_u, left_w)

    below_g, below_u, below_w = LEFT_BELOW
    assert cubic_form(below_u, below_w) == (
        204_072_236_208_253_758_153_026_182
    )
    assert filtered(0, below_g, below_u, below_w)
    assert parameters(0, below_g, below_u, below_w) == (
        40_792_070_154_065_859_512_071_297_982_281_118_663_120_554_586_442_626,
        11_630_364_560_919_415_355_581_227_985_973_747_074_671_677_129_328_892,
        5_615_065_982_833_353_861_194_126_249_971_319_559_410_303_615_609_080,
    )
    check_legendre_bracket(below_u, below_w)

    right_g, right_u, right_w = RIGHT
    assert filtered(1, right_g, right_u, right_w)
    assert cubic_form(right_u, right_w) < 0
    right_row = parameters(1, right_g, right_u, right_w)
    assert right_row is not None
    assert literal_gains(*right_row)[1] == 0
    rejected_row = parameters(1, 39, right_u, right_w)
    assert rejected_row is not None
    rejected_m, rejected_j, rejected_r = rejected_row
    assert kappa(rejected_m, rejected_j) == rejected_r
    assert kappa(rejected_m, rejected_j + 1) == rejected_r + 1
    assert residuals(1, 39, right_u, right_w)[0] < 0
    assert not filtered(1, 39, right_u, right_w)
    check_legendre_bracket(right_u, right_w)


def check_same_board_different_k_cardinality() -> None:
    """Check the exact local discriminator between alpha_min and alpha_*."""
    m, j, r = parameters(0, *LEFT)  # type: ignore[misc]
    q = (4 * m + 3) // 5
    assert j < q

    descending_k = r + 2 * m - 1 - j
    assert descending_k > m
    assert descending_k >= kappa(m, j)
    assert literal_gains(m, j, r)[0] == 0

    star_k = j
    assert star_k >= kappa(m, j)
    star_deletion_gain = -4 * j * j + (28 * m + 9) * j + 28 * m + 12
    assert star_deletion_gain == (
        79_369_740_838_380_701_409_883_290_058_284_963_412_992
    )
    assert star_deletion_gain > 0


def main() -> None:
    check_pg49_boundary_and_supported_false_positive()
    check_infinite_unfiltered_ray()
    check_true_filters_and_scale_rejections()
    check_same_board_different_k_cardinality()
    print("PG49/KPGZERO filtered-cardinality diagnostic: PASS")
    print("PG49 interval-shift witnesses checked: 2 (one boundary equality)")
    print("direct all-pairs W row: m=34")
    print("unfiltered affine-ray rows checked: t=(0,1,17)")
    print("accepted filtered branches checked: left-above, left-below, right-above")
    print("rejected congruent scales checked: left g=9, right g=39")
    print("same-board induced-K discriminator: alpha_min versus alpha_star")
    print("matching, subset, and permutation-family enumerations: 0")


if __name__ == "__main__":
    main()
