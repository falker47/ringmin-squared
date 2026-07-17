"""Independent exact diagnostic for the global five-prefix optimization.

The script uses only the Python standard library.  It imports no project,
test, production, artifact, certificate, backend, or enumeration helper.  The
written compact proof remains the all-real proof; these calculations check its
clipping data, transition rows, optimizer polynomial and isolating interval,
strict branch inequalities, coefficient identity, and comparison margins.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt

F = Fraction

RADICAND = 183_342_238_504_950_468_196_395_903
SIMPLEX_DENOMINATOR = 30_143_556_935_103

M_VALUES = (
    F(0),
    F(4, 27),
    F(108, 529),
    F(1_119_364, 4_785_507),
    F(3_392_752_184_748, 13_440_604_496_449),
    F(
        722_599_396_919_860_307_414_438_404,
        2_725_902_074_099_388_500_860_861_827,
    ),
)

Q_VALUES = (
    F(2, 3),
    F(18, 23),
    F(1_058, 1_263),
    F(3_190_338, 3_666_143),
    F(26_881_208_992_898, 30_143_556_935_103),
)

X_STAR = tuple(
    F(value, SIMPLEX_DENOMINATOR)
    for value in (
        26_881_208_992_898,
        23_392_470_652_668,
        19_595_592_993_288,
        15_335_681_473_008,
        10_223_787_648_672,
    )
)

# Coefficients are in ascending order.
ALPHA_POLYNOMIAL = (
    F(241_763_928_731_615_232_919_074_902),
    F(-844_827_555_923_160_619_545_369_006),
    F(661_485_317_418_210_151_348_973_103),
)

COEFFICIENT_POLYNOMIAL = (
    F(2_466_564_342_132_814_822_688_647_712_444_341_404_477_077_569_119_884_404),
    F(-18_721_433_760_133_213_108_101_428_477_952_679_485_052_680_576_852_659_016),
    F(35_442_588_837_949_489_298_273_217_193_311_251_597_156_465_942_013_337_329),
)

COEFFICIENT_RATIONAL_NUMERATOR = (
    346_693_217_780_244_687_187_063_490_332_457_027_500_975_566_238_012_204
)
COEFFICIENT_RADICAL_NUMERATOR = 1_228_130_489_996_268_437_333_105_902_690_103_574_002
COEFFICIENT_DENOMINATOR = (
    1_312_688_475_479_610_714_750_859_896_048_564_873_968_757_997_852_345_827
)

Surd = tuple[Fraction, Fraction]


def surd(rational: int | Fraction = 0, radical: int | Fraction = 0) -> Surd:
    return F(rational), F(radical)


def surd_add(left: Surd, right: Surd) -> Surd:
    return left[0] + right[0], left[1] + right[1]


def surd_subtract(left: Surd, right: Surd) -> Surd:
    return left[0] - right[0], left[1] - right[1]


def surd_multiply(left: Surd, right: Surd) -> Surd:
    return (
        left[0] * right[0] + RADICAND * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def surd_scale(value: Surd, factor: int | Fraction) -> Surd:
    factor = F(factor)
    return value[0] * factor, value[1] * factor


def surd_divide(left: Surd, right: Surd) -> Surd:
    denominator = right[0] ** 2 - RADICAND * right[1] ** 2
    assert denominator != 0
    return surd_scale(
        surd_multiply(left, (right[0], -right[1])),
        1 / denominator,
    )


def surd_sign(value: Surd) -> int:
    """Return the exact sign of a + b sqrt(RADICAND)."""

    rational, radical = value
    if radical == 0:
        return (rational > 0) - (rational < 0)
    if rational == 0:
        return (radical > 0) - (radical < 0)
    if (rational > 0) == (radical > 0):
        return 1 if rational > 0 else -1
    square_difference = rational**2 - RADICAND * radical**2
    if square_difference == 0:
        return 0
    if rational > 0:
        return 1 if square_difference > 0 else -1
    return -1 if square_difference > 0 else 1


def rational_polynomial_value(
    coefficients: tuple[Fraction, ...], value: Fraction
) -> Fraction:
    result = F(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def surd_polynomial_value(coefficients: tuple[Fraction, ...], value: Surd) -> Surd:
    result = surd()
    for coefficient in reversed(coefficients):
        result = surd_add(surd_multiply(result, value), surd(coefficient))
    return result


def p(alpha: Fraction) -> Fraction:
    return (1 - alpha) * (alpha**2 + 4 * alpha + 1) / 6


def surd_p(alpha: Surd) -> Surd:
    return surd_polynomial_value((F(1, 6), F(1, 2), F(-1, 2), F(-1, 6)), alpha)


def g(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    center = 1 + alpha
    return (
        weight
        * (4 * center * beta - center**2 - 2 * weight * beta**2)
        / (2 * (2 - weight))
    )


def surd_g(alpha: Surd, beta: Surd, weight: Surd) -> Surd:
    center = surd_add(surd(1), alpha)
    bracket = surd_subtract(
        surd_subtract(
            surd_scale(surd_multiply(center, beta), 4),
            surd_multiply(center, center),
        ),
        surd_scale(surd_multiply(weight, surd_multiply(beta, beta)), 2),
    )
    return surd_divide(
        surd_multiply(weight, bracket),
        surd_scale(surd_subtract(surd(2), weight), 2),
    )


def clipped_weight(alpha: Fraction, beta: Fraction) -> Fraction:
    center = 1 + alpha
    if beta <= center / 4:
        return F(0)
    if beta < center / 3:
        return 4 - center / beta
    return F(1)


def clipped_floor(alpha: Fraction, beta: Fraction) -> Fraction:
    center = 1 + alpha
    if beta <= center / 4:
        return F(0)
    if beta <= center / 3:
        return (4 * beta - center) ** 2 / 2
    return (4 * center * beta - center**2 - 2 * beta**2) / 2


def clipping_gap(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    center = 1 + alpha
    if beta <= center / 4:
        return (
            weight
            * (center**2 - 4 * center * beta + 2 * weight * beta**2)
            / (2 * (2 - weight))
        )
    if beta < center / 3:
        optimum = 4 - center / beta
        return beta**2 * (optimum - weight) ** 2 / (2 - weight)
    return (
        (1 - weight)
        * (4 * center * beta - center**2 - beta**2 * (weight + 2))
        / (2 - weight)
    )


def reduced_coefficient(alpha: Fraction, betas: tuple[Fraction, ...]) -> Fraction:
    total = p(alpha)
    previous = alpha
    for beta in betas:
        total += (previous - beta) * clipped_floor(alpha, beta)
        previous = beta
    return total


def literal_coefficient(
    alpha: Fraction,
    betas: tuple[Fraction, ...],
    weights: tuple[Fraction, ...],
) -> Fraction:
    total = p(alpha)
    previous = alpha
    for beta, weight in zip(betas, weights, strict=True):
        total += (previous - beta) * g(alpha, beta, weight)
        previous = beta
    return total


def branch(alpha: Fraction, betas: tuple[Fraction, ...]) -> str:
    center = 1 + alpha
    result = []
    for beta in betas:
        if beta <= center / 4:
            result.append("0")
        elif beta >= center / 3:
            result.append("H")
        else:
            result.append("M")
    return "".join(result)


def branch_witnesses() -> dict[str, tuple[Fraction, ...]]:
    alpha = F(4, 5)
    lower = (1 + alpha) / 4
    upper = (1 + alpha) / 3
    result: dict[str, tuple[Fraction, ...]] = {}
    for high_count in range(6):
        for middle_count in range(6 - high_count):
            zero_count = 5 - high_count - middle_count
            high = tuple(
                upper + (high_count - index) * (alpha - upper) / (high_count + 1)
                for index in range(high_count)
            )
            middle = tuple(
                lower + (middle_count - index) * (upper - lower) / (middle_count + 1)
                for index in range(middle_count)
            )
            zero = tuple(
                (zero_count - index) * lower / (zero_count + 1)
                for index in range(zero_count)
            )
            betas = high + middle + zero
            result[branch(alpha, betas)] = betas
    return result


def normalized_objective(values: tuple[Fraction, ...]) -> Fraction:
    previous = F(1)
    total = F(0)
    for value in values:
        total += (previous - value) * value**2
        previous = value
    return total


def simplex_certificate(values: tuple[Fraction, ...]) -> Fraction:
    previous = F(1)
    total = F(0)
    for index, value in enumerate(values):
        remaining = 5 - index
        q_value = Q_VALUES[remaining - 1]
        m_tail = M_VALUES[remaining - 1]
        total += (
            (1 - m_tail)
            * (value - q_value * previous) ** 2
            * (value + q_value * previous / 2)
        )
        previous = value
    return total


def phi(value: Fraction) -> Fraction:
    if value <= F(1, 4):
        return F(0)
    if value <= F(1, 3):
        return (4 * value - 1) ** 2 / 2
    return -(value**2) + 2 * value - F(1, 2)


def high_parent_with_middle_tail(tail_size: int, value: Fraction) -> Fraction:
    tail_derivative = F(3, 2) * M_VALUES[tail_size] * (4 * value - 1) ** 2
    return value + (phi(value) - tail_derivative) / (2 * (1 - value))


def high_parent(value: Fraction, child: Fraction) -> Fraction:
    return value + (phi(value) - phi(child)) / (2 * (1 - value))


def middle_children(
    parent: Fraction, ratios: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    transformed = 4 * parent - 1
    result = []
    for ratio in ratios:
        transformed *= ratio
        result.append((1 + transformed) / 4)
    return tuple(result)


def derive_transition(
    high_count: int,
) -> tuple[Fraction, Fraction, tuple[Fraction, ...], tuple[Fraction, ...]]:
    densities: list[Fraction | None] = [None] * 5
    densities[high_count - 1] = F(1, 3)
    descendants = middle_children(F(1, 3), tuple(reversed(Q_VALUES[: 5 - high_count])))
    for index, value in enumerate(descendants, start=high_count):
        densities[index] = value

    if high_count == 1:
        tau = high_parent_with_middle_tail(4, F(1, 3))
    else:
        densities[high_count - 2] = high_parent_with_middle_tail(
            5 - high_count, F(1, 3)
        )
        for index in range(high_count - 3, -1, -1):
            current = densities[index + 1]
            child = densities[index + 2]
            assert current is not None and child is not None
            densities[index] = high_parent(current, child)
        assert densities[0] is not None and densities[1] is not None
        tau = high_parent(densities[0], densities[1])

    exact_densities = tuple(value for value in densities if value is not None)
    assert len(exact_densities) == 5
    weights = tuple(
        F(1) if value >= F(1, 3) else 4 - 1 / value for value in exact_densities
    )
    return tau, tau / (1 - tau), exact_densities, weights


def check_clipping_and_transitions() -> None:
    witnesses = branch_witnesses()
    expected_words = {
        "H" * high + "M" * middle + "0" * (5 - high - middle)
        for high in range(6)
        for middle in range(6 - high)
    }
    assert len(expected_words) == 21
    assert set(witnesses) == expected_words

    alpha = F(4, 5)
    weight_grid = tuple(F(index, 6) for index in range(7))
    for betas in witnesses.values():
        clipped = tuple(clipped_weight(alpha, beta) for beta in betas)
        assert clipped == tuple(sorted(clipped, reverse=True))
        assert literal_coefficient(alpha, betas, clipped) == reduced_coefficient(
            alpha, betas
        )
        for beta in betas:
            optimum = clipped_weight(alpha, beta)
            assert g(alpha, beta, optimum) == clipped_floor(alpha, beta)
            for weight in weight_grid:
                gap = clipped_floor(alpha, beta) - g(alpha, beta, weight)
                assert gap == clipping_gap(alpha, beta, weight)
                assert gap >= 0

    lower = (1 + alpha) / 4
    upper = (1 + alpha) / 3
    assert clipped_floor(alpha, lower) == g(alpha, lower, F(0)) == 0
    assert clipped_floor(alpha, upper) == g(alpha, upper, F(1))
    assert 4 * (4 * lower - 1 - alpha) == 0
    assert 4 * (4 * upper - 1 - alpha) == 2 * (1 + alpha) - 2 * upper

    expected = (
        (
            F(36_929_061_304_599, 107_524_835_971_592),
            F(36_929_061_304_599, 70_595_774_666_993),
            (
                F(1, 3),
                F(4_729_589, 14_664_572),
                F(4_556_979, 14_664_572),
                F(4_363_319, 14_664_572),
                F(4_130_927, 14_664_572),
            ),
            (
                F(1),
                F(4_253_784, 4_729_589),
                F(3_563_344, 4_556_979),
                F(2_788_704, 4_363_319),
                F(1_859_136, 4_130_927),
            ),
        ),
        (
            F(229_053_579_602_567, 639_264_589_294_896),
            F(229_053_579_602_567, 410_211_009_692_329),
            (
                F(13_237_157, 38_284_056),
                F(1, 3),
                F(4_847, 15_156),
                F(513, 1_684),
                F(1_447, 5_052),
            ),
            (F(1), F(1), F(4_232, 4_847), F(368, 513), F(736, 1_447)),
        ),
        (
            F(309_127_972_999_621, 808_420_198_088_928),
            F(309_127_972_999_621, 499_292_225_089_307),
            (
                F(76_718_581, 209_712_528),
                F(1_479, 4_232),
                F(1, 3),
                F(29, 92),
                F(27, 92),
            ),
            (F(1), F(1), F(1), F(24, 29), F(16, 27)),
        ),
        (
            F(3_403_232_546_992_614_203, 7_941_191_861_991_121_344),
            F(3_403_232_546_992_614_203, 4_537_959_314_998_507_141),
            (
                F(1_806_469_369, 4_470_813_792),
                F(7_607, 20_016),
                F(77, 216),
                F(1, 3),
                F(11, 36),
            ),
            (F(1), F(1), F(1), F(1), F(8, 11)),
        ),
        (
            F(27_936_208_629_060_590_955_659, 50_072_626_139_262_934_446_720),
            F(27_936_208_629_060_590_955_659, 22_136_417_510_202_343_491_061),
            (
                F(199_200_916_177, 391_198_109_760),
                F(93_059, 201_120),
                F(301, 720),
                F(3, 8),
                F(1, 3),
            ),
            (F(1), F(1), F(1), F(1), F(1)),
        ),
    )
    derived = tuple(derive_transition(index) for index in range(1, 6))
    assert derived == expected
    transition_alphas = tuple(row[1] for row in derived)
    assert (
        F(1, 3)
        < transition_alphas[0]
        < transition_alphas[1]
        < transition_alphas[2]
        < transition_alphas[3]
        < 1
        < transition_alphas[4]
    )
    assert derived[-1][0] > F(1, 2)

    mixed_margins = tuple(
        17 - (1 + 8 * q_value**2) * (1 / (3 * q_value)) * (6 - 1 / (3 * q_value))
        for q_value in Q_VALUES[:4]
    )
    assert mixed_margins == (
        F(161, 36),
        F(200_735, 67_068),
        F(9_571_263_245, 4_241_270_196),
        F(609_160_555_391_902_550_135, 335_834_496_166_911_848_028),
    )
    assert all(value > 0 for value in mixed_margins)

    # Exact density-facet deletion identities at a representative strict row.
    b1, b2, b3, b4, b5 = F(7, 10), F(13, 20), F(3, 5), F(11, 20), F(1, 2)
    assert reduced_coefficient(alpha, (alpha, b2, b3, b4, b5)) == reduced_coefficient(
        alpha, (b2, b3, b4, b5)
    )
    assert reduced_coefficient(alpha, (b1, b1, b3, b4, b5)) == reduced_coefficient(
        alpha, (b1, b3, b4, b5)
    )
    assert reduced_coefficient(alpha, (b1, b2, b2, b4, b5)) == reduced_coefficient(
        alpha, (b1, b2, b4, b5)
    )
    assert reduced_coefficient(alpha, (b1, b2, b3, b3, b5)) == reduced_coefficient(
        alpha, (b1, b2, b3, b5)
    )
    assert reduced_coefficient(alpha, (b1, b2, b3, b4, b4)) == reduced_coefficient(
        alpha, (b1, b2, b3, b4)
    )
    assert reduced_coefficient(alpha, (b1, b2, b3, b4, F(0))) == reduced_coefficient(
        alpha, (b1, b2, b3, b4)
    )


def check_optimizer_and_coefficient() -> tuple[Surd, Surd]:
    for index in range(1, 6):
        q_value = F(2, 3) / (1 - M_VALUES[index - 1])
        assert q_value == Q_VALUES[index - 1]
        assert M_VALUES[index] == q_value**2 / 3
    assert normalized_objective(X_STAR) == M_VALUES[5]
    assert simplex_certificate(X_STAR) == 0
    for index, current in enumerate(X_STAR):
        previous = F(1) if index == 0 else X_STAR[index - 1]
        following = F(0) if index == 4 else X_STAR[index + 1]
        assert 2 * previous * current - 3 * current**2 + following**2 == 0

    alpha = surd(
        F(140_804_592_653_860_103_257_561_501, 220_495_105_806_070_050_449_657_701),
        F(-10_047_852_311_701, 661_485_317_418_210_151_348_973_103),
    )
    assert surd_polynomial_value(ALPHA_POLYNOMIAL, alpha) == surd()
    integer_alpha_polynomial = tuple(int(value) for value in ALPHA_POLYNOMIAL)
    assert (
        gcd(
            gcd(abs(integer_alpha_polynomial[0]), abs(integer_alpha_polynomial[1])),
            abs(integer_alpha_polynomial[2]),
        )
        == 1
    )
    discriminant = (
        integer_alpha_polynomial[1] ** 2
        - 4 * integer_alpha_polynomial[2] * integer_alpha_polynomial[0]
    )
    assert discriminant == (2 * 10_047_852_311_701) ** 2 * RADICAND
    assert isqrt(RADICAND) ** 2 != RADICAND

    alpha_left = F(432_907_432_458_521, 10**15)
    alpha_right = F(432_907_432_458_522, 10**15)
    assert rational_polynomial_value(ALPHA_POLYNOMIAL, alpha_left) > 0
    assert rational_polynomial_value(ALPHA_POLYNOMIAL, alpha_right) < 0
    assert surd_sign(surd_subtract(alpha, surd(alpha_left))) > 0
    assert surd_sign(surd_subtract(surd(alpha_right), alpha)) > 0

    first_transition = F(36_929_061_304_599, 70_595_774_666_993)
    assert surd_sign(surd_subtract(alpha, surd(F(1, 3)))) > 0
    assert surd_sign(surd_subtract(surd(F(1, 2)), alpha)) > 0
    assert first_transition > F(1, 2)

    amplitude = surd_subtract(surd_scale(alpha, 3), surd(1))
    center = surd_add(surd(1), alpha)
    betas = tuple(
        surd_scale(
            surd_add(center, surd_scale(amplitude, coordinate)),
            F(1, 4),
        )
        for coordinate in X_STAR
    )
    weights = tuple(
        surd_divide(surd_scale(amplitude, coordinate), beta)
        for coordinate, beta in zip(X_STAR, betas, strict=True)
    )
    lower = surd_scale(center, F(1, 4))
    upper = surd_scale(center, F(1, 3))
    assert surd_sign(surd_subtract(alpha, betas[0])) > 0
    assert all(
        surd_sign(surd_subtract(left, right)) > 0
        for left, right in zip(betas[:-1], betas[1:], strict=True)
    )
    assert surd_sign(betas[-1]) > 0
    assert all(surd_sign(surd_subtract(beta, lower)) > 0 for beta in betas)
    assert all(surd_sign(surd_subtract(upper, beta)) > 0 for beta in betas)
    assert surd_sign(surd_subtract(surd(1), weights[0])) > 0
    assert all(
        surd_sign(surd_subtract(left, right)) > 0
        for left, right in zip(weights[:-1], weights[1:], strict=True)
    )
    assert surd_sign(weights[-1]) > 0

    coefficient = surd(
        F(COEFFICIENT_RATIONAL_NUMERATOR, COEFFICIENT_DENOMINATOR),
        F(COEFFICIENT_RADICAL_NUMERATOR, COEFFICIENT_DENOMINATOR),
    )
    envelope = surd_add(
        surd_p(alpha),
        surd_scale(
            surd_multiply(surd_multiply(amplitude, amplitude), amplitude),
            M_VALUES[5] / 8,
        ),
    )
    assert envelope == coefficient

    direct = surd_p(alpha)
    reduced = surd_p(alpha)
    previous = alpha
    for beta, weight in zip(betas, weights, strict=True):
        segment = surd_subtract(previous, beta)
        direct = surd_add(direct, surd_multiply(segment, surd_g(alpha, beta, weight)))
        displacement = surd_subtract(surd_scale(beta, 4), center)
        middle_floor = surd_scale(surd_multiply(displacement, displacement), F(1, 2))
        reduced = surd_add(reduced, surd_multiply(segment, middle_floor))
        previous = beta
    assert direct == reduced == coefficient

    assert surd_polynomial_value(COEFFICIENT_POLYNOMIAL, coefficient) == surd()
    integer_coefficient_polynomial = tuple(
        int(value) for value in COEFFICIENT_POLYNOMIAL
    )
    assert (
        gcd(
            gcd(
                abs(integer_coefficient_polynomial[0]),
                abs(integer_coefficient_polynomial[1]),
            ),
            abs(integer_coefficient_polynomial[2]),
        )
        == 1
    )
    coefficient_discriminant = (
        integer_coefficient_polynomial[1] ** 2
        - 4 * integer_coefficient_polynomial[2] * integer_coefficient_polynomial[0]
    )
    assert coefficient_discriminant > 0
    assert isqrt(coefficient_discriminant) ** 2 != coefficient_discriminant

    coefficient_left = F(276_777_463_862_376, 10**15)
    coefficient_right = F(276_777_463_862_377, 10**15)
    assert rational_polynomial_value(COEFFICIENT_POLYNOMIAL, coefficient_left) < 0
    assert rational_polynomial_value(COEFFICIENT_POLYNOMIAL, coefficient_right) > 0
    assert surd_sign(surd_subtract(coefficient, surd(coefficient_left))) > 0
    assert surd_sign(surd_subtract(surd(coefficient_right), coefficient)) > 0
    conjugate = coefficient[0], -coefficient[1]
    assert surd_sign(surd_subtract(surd(coefficient_left), conjugate)) > 0
    return alpha, coefficient


def check_comparisons(coefficient: Surd) -> tuple[int, int, int, int]:
    separator_numerator = 1_383_887
    separator_denominator = 5_000_000
    separator = F(separator_numerator, separator_denominator)
    assert surd_sign(surd_subtract(coefficient, surd(separator))) > 0

    radical_gap = (
        separator_numerator * COEFFICIENT_DENOMINATOR
        - separator_denominator * COEFFICIENT_RATIONAL_NUMERATOR
    )
    radical_square_margin = (
        separator_denominator * COEFFICIENT_RADICAL_NUMERATOR
    ) ** 2 * RADICAND - radical_gap**2
    assert (
        radical_gap
        == 83_146_427_364_828_597_269_105_797_300_675_160_237_124_768_183_828_289_489_549
    )
    assert (
        radical_square_margin
        == 69_702_993_976_900_185_951_520_100_524_212_537_636_065_043_490_026_138_423_895_122_957_763_867_476_110_120_496_231_186_335_955_872_868_657_019_776_599
    )
    assert radical_gap > 0 and radical_square_margin > 0

    rational_numerator = 2_263_404_122_555_368_590_593_580_404_287
    rational_denominator = 8_177_706_222_298_165_502_582_585_481_000
    separator_margin = (
        separator_numerator * rational_denominator
        - separator_denominator * rational_numerator
    )
    assert separator_margin == 718_080_698_409_904_604_452_109_647_000
    assert separator_margin > 0

    rational_to_old_separator = 271 * rational_numerator - 75 * rational_denominator
    assert rational_to_old_separator == 54_550_540_142_475_357_166_378_486_777
    assert rational_to_old_separator > 0

    c4_rational = 597_580_022_071_777_213_687_318_156
    c4_radical = 21_288_970_076_515_705_538
    c4_radicand = 2_903_456_040_383
    c4_denominator = 2_290_468_477_489_828_247_376_833_403
    c4_gap = 75 * c4_denominator - 271 * c4_rational
    c4_square_margin = c4_gap**2 - c4_radicand * (271 * c4_radical) ** 2
    assert c4_gap == 9_840_949_830_285_493_643_999_284_949
    assert (
        c4_square_margin
        == 202_909_790_739_538_065_073_835_756_341_295_480_167_322_654_096_276_669
    )
    assert c4_gap > 0 and c4_square_margin > 0
    return (
        radical_square_margin,
        separator_margin,
        rational_to_old_separator,
        c4_square_margin,
    )


def main() -> None:
    if not __debug__:
        raise RuntimeError(
            "run this diagnostic without Python's -O assertion stripping"
        )

    check_clipping_and_transitions()
    alpha, coefficient = check_optimizer_and_coefficient()
    margins = check_comparisons(coefficient)

    print("global five-prefix exact diagnostic: PASS")
    print(f"alpha_5_star={alpha}")
    print(f"C_5_star={coefficient}")
    print(f"comparison_margins={margins}")
    print(f"clipping_regimes={len(branch_witnesses())}")


if __name__ == "__main__":
    main()
