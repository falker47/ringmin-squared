"""Independent exact diagnostic for the global four-prefix optimization.

This script uses only the Python standard library.  It does not import the
project package, tests, production scorers, artifact code, or the historical
four-prefix literal oracle.  The written proof remains the all-real proof;
these exact calculations independently corroborate its reduction, branch
transitions, optimizer, and coefficient comparison.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement
from math import gcd, isqrt, sqrt

F = Fraction

RADICAND = 2_903_456_040_383

M_VALUES = (
    F(0),
    F(4, 27),
    F(108, 529),
    F(1_119_364, 4_785_507),
    F(3_392_752_184_748, 13_440_604_496_449),
)
Q_VALUES = (
    F(2, 3),
    F(18, 23),
    F(1_058, 1_263),
    F(3_190_338, 3_666_143),
)
X_STAR = (
    F(3_190_338, 3_666_143),
    F(2_672_508, 3_666_143),
    F(2_091_528, 3_666_143),
    F(1_394_352, 3_666_143),
)

ENVELOPE_COEFFICIENTS = (
    F(5_448_020_178_944, 40_321_813_489_347),
    F(31_611_445_368_198, 40_321_813_489_347),
    F(-54_512_522_615_247, 40_321_813_489_347),
    F(27_631_313_622_349, 40_321_813_489_347),
)
Q_COEFFICIENTS = (
    F(10_537_148_456_066),
    F(-36_341_681_743_498),
    F(27_631_313_622_349),
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
    denominator = right[0] * right[0] - RADICAND * right[1] * right[1]
    assert denominator != 0
    conjugate = right[0], -right[1]
    return surd_scale(surd_multiply(left, conjugate), 1 / denominator)


def surd_sign(value: Surd) -> int:
    """Return the exact sign of a + b sqrt(RADICAND)."""

    rational, radical = value
    if radical == 0:
        return (rational > 0) - (rational < 0)
    if rational == 0:
        return (radical > 0) - (radical < 0)
    if (rational > 0) == (radical > 0):
        return 1 if rational > 0 else -1
    square_difference = rational * rational - RADICAND * radical * radical
    if square_difference == 0:
        return 0
    if rational > 0:
        return 1 if square_difference > 0 else -1
    return -1 if square_difference > 0 else 1


def surd_polynomial_value(coefficients: tuple[Fraction, ...], value: Surd) -> Surd:
    result = surd()
    for coefficient in reversed(coefficients):
        result = surd_add(surd_multiply(result, value), surd(coefficient))
    return result


def rational_polynomial_value(
    coefficients: tuple[Fraction, ...], value: Fraction
) -> Fraction:
    result = F(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def surd_p(alpha: Surd) -> Surd:
    return surd_polynomial_value((F(1, 6), F(1, 2), F(-1, 2), F(-1, 6)), alpha)


def surd_g(alpha: Surd, beta: Surd, weight: Surd) -> Surd:
    center = surd_add(surd(1), alpha)
    beta_squared = surd_multiply(beta, beta)
    bracket = surd_subtract(
        surd_subtract(
            surd_scale(surd_multiply(center, beta), 4),
            surd_multiply(center, center),
        ),
        surd_scale(surd_multiply(weight, beta_squared), 2),
    )
    numerator = surd_multiply(weight, bracket)
    denominator = surd_scale(surd_subtract(surd(2), weight), 2)
    return surd_divide(numerator, denominator)


def surd_middle_floor(alpha: Surd, beta: Surd) -> Surd:
    center = surd_add(surd(1), alpha)
    displacement = surd_subtract(surd_scale(beta, 4), center)
    return surd_scale(surd_multiply(displacement, displacement), F(1, 2))


def surd_literal_coefficient(
    alpha: Surd, betas: tuple[Surd, ...], weights: tuple[Surd, ...]
) -> Surd:
    previous = alpha
    total = surd_p(alpha)
    for beta, weight in zip(betas, weights, strict=True):
        total = surd_add(
            total,
            surd_multiply(surd_subtract(previous, beta), surd_g(alpha, beta, weight)),
        )
        previous = beta
    return total


def surd_middle_reduced_coefficient(alpha: Surd, betas: tuple[Surd, ...]) -> Surd:
    previous = alpha
    total = surd_p(alpha)
    for beta in betas:
        total = surd_add(
            total,
            surd_multiply(
                surd_subtract(previous, beta), surd_middle_floor(alpha, beta)
            ),
        )
        previous = beta
    return total


def normalized_objective(values: tuple[Fraction, ...]) -> Fraction:
    previous = F(1)
    total = F(0)
    for value in values:
        total += (previous - value) * value * value
        previous = value
    return total


def simplex_certificate(values: tuple[Fraction, ...]) -> Fraction:
    previous = F(1)
    total = F(0)
    for index, value in enumerate(values):
        remaining = 4 - index
        q_value = Q_VALUES[remaining - 1]
        m_tail = M_VALUES[remaining - 1]
        total += (
            (1 - m_tail)
            * (value - q_value * previous) ** 2
            * (value + q_value * previous / 2)
        )
        previous = value
    return total


def grid_maximum(denominator: int) -> tuple[Fraction, tuple[int, ...]]:
    best_numerator = -1
    best_values: tuple[int, ...] | None = None
    for ascending in combinations_with_replacement(range(denominator + 1), 4):
        values = tuple(reversed(ascending))
        previous = denominator
        numerator = 0
        for value in values:
            numerator += (previous - value) * value * value
            previous = value
        if numerator > best_numerator:
            best_numerator = numerator
            best_values = values
    assert best_values is not None
    return F(best_numerator, denominator**3), best_values


def p(alpha: Fraction) -> Fraction:
    return (1 - alpha) * (alpha * alpha + 4 * alpha + 1) / 6


def g(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    center = 1 + alpha
    return (
        weight
        * (4 * center * beta - center * center - 2 * weight * beta * beta)
        / (2 * (2 - weight))
    )


def clipped_weight(alpha: Fraction, beta: Fraction) -> Fraction:
    center = 1 + alpha
    lower = center / 4
    upper = center / 3
    if beta <= lower:
        return F(0)
    if beta < upper:
        return 4 - center / beta
    return F(1)


def clipped_floor(alpha: Fraction, beta: Fraction) -> Fraction:
    center = 1 + alpha
    lower = center / 4
    upper = center / 3
    if beta <= lower:
        return F(0)
    if beta <= upper:
        return (4 * beta - center) ** 2 / 2
    return (4 * center * beta - center * center - 2 * beta * beta) / 2


def reduced_coefficient(alpha: Fraction, betas: tuple[Fraction, ...]) -> Fraction:
    previous = alpha
    total = p(alpha)
    for beta in betas:
        total += (previous - beta) * clipped_floor(alpha, beta)
        previous = beta
    return total


def literal_coefficient(
    alpha: Fraction, betas: tuple[Fraction, ...], weights: tuple[Fraction, ...]
) -> Fraction:
    previous = alpha
    total = p(alpha)
    for beta, weight in zip(betas, weights, strict=True):
        total += (previous - beta) * g(alpha, beta, weight)
        previous = beta
    return total


def clipping_gap_factor(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    """Exact factorization of clipped_floor(alpha,beta) - g(alpha,beta,weight)."""

    center = 1 + alpha
    lower = center / 4
    upper = center / 3
    if beta <= lower:
        return (
            weight
            * (center * center - 4 * center * beta + 2 * weight * beta * beta)
            / (2 * (2 - weight))
        )
    if beta < upper:
        optimum = 4 - center / beta
        return beta * beta * (optimum - weight) ** 2 / (2 - weight)
    return (
        (1 - weight)
        * (4 * center * beta - center * center - beta * beta * (weight + 2))
        / (2 - weight)
    )


def branch(alpha: Fraction, betas: tuple[Fraction, ...]) -> str:
    center = 1 + alpha
    lower = center / 4
    upper = center / 3
    symbols = []
    for beta in betas:
        if beta <= lower:
            symbols.append("0")
        elif beta >= upper:
            symbols.append("H")
        else:
            symbols.append("M")
    return "".join(symbols)


def branch_witnesses() -> dict[str, tuple[Fraction, ...]]:
    alpha = F(4, 5)
    center = 1 + alpha
    lower = center / 4
    upper = center / 3
    witnesses: dict[str, tuple[Fraction, ...]] = {}
    for high_count in range(5):
        for middle_count in range(5 - high_count):
            zero_count = 4 - high_count - middle_count
            high = [
                upper + (high_count - index) * (alpha - upper) / (high_count + 1)
                for index in range(high_count)
            ]
            middle = [
                lower + (middle_count - index) * (upper - lower) / (middle_count + 1)
                for index in range(middle_count)
            ]
            zero = [
                (zero_count - index) * lower / (zero_count + 1)
                for index in range(zero_count)
            ]
            betas = tuple(high + middle + zero)
            witnesses[branch(alpha, betas)] = betas
    return witnesses


def phi(value: Fraction) -> Fraction:
    if value <= F(1, 4):
        return F(0)
    if value <= F(1, 3):
        return (4 * value - 1) ** 2 / 2
    return -value * value + 2 * value - F(1, 2)


def high_parent_with_middle_tail(tail_size: int, value: Fraction) -> Fraction:
    """The parent coordinate R_m(value) for m optimized middle descendants."""

    high_value = -value * value + 2 * value - F(1, 2)
    tail_derivative = F(3, 2) * M_VALUES[tail_size] * (4 * value - 1) ** 2
    return value + (high_value - tail_derivative) / (2 * (1 - value))


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


def check_weight_reduction() -> None:
    witnesses = branch_witnesses()
    expected = {
        "0000",
        "M000",
        "H000",
        "MM00",
        "HM00",
        "HH00",
        "MMM0",
        "HMM0",
        "HHM0",
        "HHH0",
        "MMMM",
        "HMMM",
        "HHMM",
        "HHHM",
        "HHHH",
    }
    assert set(witnesses) == expected

    weight_grid = [F(index, 6) for index in range(7)]
    for alpha in (F(2, 5), F(3, 5), F(4, 5), F(1)):
        center = 1 + alpha
        lower = center / 4
        upper = center / 3
        density_grid = sorted(
            {
                *(F(index, 8) for index in range(9) if F(index, 8) <= alpha),
                lower,
                upper,
            }
        )

        # Exact C^1 joins of the low/middle and middle/high formulas.
        assert clipped_weight(alpha, lower) == 0
        assert clipped_floor(alpha, lower) == g(alpha, lower, F(0)) == 0
        assert 4 * (4 * lower - center) == 0
        assert clipped_weight(alpha, upper) == 1
        assert clipped_floor(alpha, upper) == g(alpha, upper, F(1))
        assert 4 * (4 * upper - center) == 2 * center - 2 * upper

        # The three exact gap factorizations establish coordinatewise clipping.
        for beta in density_grid:
            optimum = clipped_weight(alpha, beta)
            assert g(alpha, beta, optimum) == clipped_floor(alpha, beta)
            for weight in weight_grid:
                gap = clipped_floor(alpha, beta) - g(alpha, beta, weight)
                assert gap == clipping_gap_factor(alpha, beta, weight)
                assert gap >= 0

        for ascending in combinations_with_replacement(density_grid, 4):
            betas = tuple(reversed(ascending))
            clipped = tuple(clipped_weight(alpha, beta) for beta in betas)
            assert clipped == tuple(sorted(clipped, reverse=True))
            assert literal_coefficient(alpha, betas, clipped) == reduced_coefficient(
                alpha, betas
            )


def transition_weights(
    tau: Fraction, normalized_densities: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    alpha = tau / (1 - tau)
    center = 1 + alpha
    return tuple(
        clipped_weight(alpha, center * density) for density in normalized_densities
    )


def check_branch_transitions() -> None:
    tau_1 = F(13_237_157, 38_284_056)
    tau_2 = F(76_718_581, 209_712_528)
    tau_3 = F(1_806_469_369, 4_470_813_792)
    tau_4 = F(199_200_916_177, 391_198_109_760)
    alpha_values = tuple(
        tau / (1 - tau) for tau in (F(1, 4), tau_1, tau_2, tau_3, tau_4)
    )
    assert alpha_values == (
        F(1, 3),
        F(13_237_157, 25_046_899),
        F(76_718_581, 132_993_947),
        F(1_806_469_369, 2_664_344_423),
        F(199_200_916_177, 191_997_193_583),
    )

    first = (F(1, 3),) + middle_children(
        F(1, 3), (Q_VALUES[2], Q_VALUES[1], Q_VALUES[0])
    )
    assert first == (
        F(1, 3),
        F(4_847, 15_156),
        F(513, 1_684),
        F(1_447, 5_052),
    )
    assert transition_weights(tau_1, first) == (
        F(1),
        F(4_232, 4_847),
        F(368, 513),
        F(736, 1_447),
    )
    assert high_parent_with_middle_tail(3, first[0]) == tau_1

    second_first = F(1_479, 4_232)
    second = (second_first,) + middle_children(
        second_first, (Q_VALUES[2], Q_VALUES[1], Q_VALUES[0])
    )
    assert second == (
        F(1_479, 4_232),
        F(1, 3),
        F(29, 92),
        F(27, 92),
    )
    assert transition_weights(tau_2, second) == (
        F(1),
        F(1),
        F(24, 29),
        F(16, 27),
    )
    assert high_parent_with_middle_tail(3, second_first) == tau_2
    assert high_parent_with_middle_tail(2, second[1]) == second[0]
    assert high_parent(second[0], second[1]) == tau_2

    third_second = F(77, 216)
    third_first = high_parent_with_middle_tail(2, third_second)
    third = (third_first, third_second) + middle_children(
        third_second, (Q_VALUES[1], Q_VALUES[0])
    )
    assert third == (
        F(7_607, 20_016),
        F(77, 216),
        F(1, 3),
        F(11, 36),
    )
    assert transition_weights(tau_3, third) == (F(1), F(1), F(1), F(8, 11))
    assert high_parent(third_first, third_second) == tau_3

    fourth_third = F(3, 8)
    fourth_second = high_parent_with_middle_tail(1, fourth_third)
    fourth_first = high_parent(fourth_second, fourth_third)
    fourth = (fourth_first, fourth_second, fourth_third, F(1, 3))
    assert fourth == (
        F(93_059, 201_120),
        F(301, 720),
        F(3, 8),
        F(1, 3),
    )
    assert transition_weights(tau_4, fourth) == (F(1), F(1), F(1), F(1))
    assert high_parent(fourth_first, fourth_second) == tau_4
    assert tau_4 > F(1, 2)
    assert alpha_values[-1] > 1


def check_collision_reductions() -> None:
    alpha = F(4, 5)
    b1, b2, b3, b4 = F(7, 10), F(3, 5), F(1, 2), F(12, 25)

    assert reduced_coefficient(alpha, (alpha, b2, b3, b4)) == reduced_coefficient(
        alpha, (b2, b3, b4)
    )
    assert reduced_coefficient(alpha, (b1, b1, b3, b4)) == reduced_coefficient(
        alpha, (b1, b3, b4)
    )
    assert reduced_coefficient(alpha, (b1, b2, b2, b4)) == reduced_coefficient(
        alpha, (b1, b2, b4)
    )
    assert reduced_coefficient(alpha, (b1, b2, b3, b3)) == reduced_coefficient(
        alpha, (b1, b2, b3)
    )
    assert reduced_coefficient(alpha, (b1, b2, b3, F(0))) == reduced_coefficient(
        alpha, (b1, b2, b3)
    )

    clipped = tuple(clipped_weight(alpha, beta) for beta in (b1, b2, b3, b4))
    assert literal_coefficient(
        alpha, (b1, b2, b3, b4), clipped[:-1] + (F(0),)
    ) == literal_coefficient(alpha, (b1, b2, b3), clipped[:-1])

    boundary_weights = (F(1),) + clipped[1:]
    assert literal_coefficient(
        b1, (b1, b2, b3, b4), boundary_weights
    ) == literal_coefficient(b1, (b2, b3, b4), boundary_weights[1:])


def check_global_algebra() -> tuple[Surd, Surd, tuple[Surd, ...], tuple[Surd, ...]]:
    # The Bellman recurrence and specialized nonnegative certificate.
    for index in range(1, 5):
        q_value = F(2, 3) / (1 - M_VALUES[index - 1])
        assert q_value == Q_VALUES[index - 1]
        assert M_VALUES[index] == q_value * q_value / 3
    assert normalized_objective(X_STAR) == M_VALUES[4]
    assert simplex_certificate(X_STAR) == 0
    for denominator in (5, 7, 9):
        for ascending in combinations_with_replacement(range(denominator + 1), 4):
            values = tuple(F(value, denominator) for value in reversed(ascending))
            assert M_VALUES[4] - normalized_objective(values) == simplex_certificate(
                values
            )

    # Derive the envelope from p(alpha) + M4(3 alpha - 1)^3/8, rather than
    # merely checking a separately hard-coded polynomial.
    p_coefficients = (F(1, 6), F(1, 2), F(-1, 2), F(-1, 6))
    cube_coefficients = (F(-1), F(9), F(-27), F(27))
    derived_envelope = tuple(
        p_coefficient + M_VALUES[4] * cube_coefficient / 8
        for p_coefficient, cube_coefficient in zip(
            p_coefficients, cube_coefficients, strict=True
        )
    )
    assert derived_envelope == ENVELOPE_COEFFICIENTS

    # Envelope differentiation and exact critical-point signs.
    derivative = tuple(
        index * ENVELOPE_COEFFICIENTS[index]
        for index in range(1, len(ENVELOPE_COEFFICIENTS))
    )
    expected_derivative = tuple(
        coefficient / F(13_440_604_496_449) for coefficient in Q_COEFFICIENTS
    )
    assert derivative == expected_derivative
    assert rational_polynomial_value(Q_COEFFICIENTS, F(1, 3)) == F(
        13_440_604_496_449, 9
    )
    assert rational_polynomial_value(Q_COEFFICIENTS, F(1, 2)) == F(
        -2_903_456_040_383, 4
    )
    assert rational_polynomial_value(Q_COEFFICIENTS, F(1)) == F(1_826_780_334_917)
    assert F(22, 81) - M_VALUES[4] == F(20_880_371_957_290, 1_088_688_964_212_369)

    alpha = surd(
        F(18_170_840_871_749, 27_631_313_622_349),
        F(-3_666_143, 27_631_313_622_349),
    )
    assert surd_polynomial_value(Q_COEFFICIENTS, alpha) == surd()
    assert surd_sign(surd_subtract(alpha, surd(F(1, 3)))) > 0
    assert surd_sign(surd_subtract(surd(F(1, 2)), alpha)) > 0

    coefficient = surd(
        F(
            597_580_022_071_777_213_687_318_156,
            2_290_468_477_489_828_247_376_833_403,
        ),
        F(
            21_288_970_076_515_705_538,
            2_290_468_477_489_828_247_376_833_403,
        ),
    )
    assert surd_polynomial_value(ENVELOPE_COEFFICIENTS, alpha) == coefficient
    minimal_polynomial = (
        F(465_999_835_246_384_276_537_748_084),
        F(-3_585_480_132_430_663_282_123_908_936),
        F(6_871_405_432_469_484_742_130_500_209),
    )
    assert surd_polynomial_value(minimal_polynomial, coefficient) == surd()
    integer_polynomial = tuple(int(value) for value in minimal_polynomial)
    assert (
        gcd(
            gcd(abs(integer_polynomial[0]), abs(integer_polynomial[1])),
            abs(integer_polynomial[2]),
        )
        == 1
    )
    discriminant = (
        integer_polynomial[1] ** 2 - 4 * integer_polynomial[2] * integer_polynomial[0]
    )
    assert discriminant > 0
    assert isqrt(discriminant) ** 2 != discriminant

    isolating_left = F(276_736_149_860, 10**12)
    isolating_right = F(276_736_149_861, 10**12)
    assert surd_sign(surd_subtract(coefficient, surd(isolating_left))) > 0
    assert surd_sign(surd_subtract(surd(isolating_right), coefficient)) > 0
    conjugate = coefficient[0], -coefficient[1]
    assert surd_sign(surd_subtract(surd(isolating_left), conjugate)) > 0
    assert (
        rational_polynomial_value(minimal_polynomial, isolating_left)
        * rational_polynomial_value(minimal_polynomial, isolating_right)
        < 0
    )

    transformed = surd_subtract(surd_scale(alpha, 3), surd(1))
    center = surd_add(surd(1), alpha)
    betas = tuple(
        surd_scale(surd_add(center, surd_scale(transformed, coordinate)), F(1, 4))
        for coordinate in X_STAR
    )
    weights = tuple(
        surd_divide(surd_scale(transformed, coordinate), beta)
        for coordinate, beta in zip(X_STAR, betas, strict=True)
    )
    assert surd_sign(surd_subtract(alpha, betas[0])) > 0
    assert all(
        surd_sign(surd_subtract(left, right)) > 0
        for left, right in zip(betas[:-1], betas[1:], strict=True)
    )
    assert surd_sign(betas[-1]) > 0
    lower = surd_scale(center, F(1, 4))
    upper = surd_scale(center, F(1, 3))
    assert all(surd_sign(surd_subtract(beta, lower)) > 0 for beta in betas)
    assert all(surd_sign(surd_subtract(upper, beta)) > 0 for beta in betas)
    assert surd_sign(surd_subtract(surd(1), weights[0])) > 0
    assert all(
        surd_sign(surd_subtract(left, right)) > 0
        for left, right in zip(weights[:-1], weights[1:], strict=True)
    )
    assert surd_sign(weights[-1]) > 0

    # End-to-end evaluation in the original and independently reduced
    # four-prefix formulas at the surd optimizer.
    assert surd_literal_coefficient(alpha, betas, weights) == coefficient
    assert surd_middle_reduced_coefficient(alpha, betas) == coefficient
    return alpha, coefficient, betas, weights


def check_three_prefix_separator() -> tuple[int, int]:
    separator_numerator = 2_767
    separator_denominator = 10_000

    c3_rational = 753_972_193_324
    c3_radical = 106_042_322
    c3_denominator = 2_960_667_770_787
    c3_gap = separator_numerator * c3_denominator - separator_denominator * c3_rational
    c3_square_difference = (
        c3_gap * c3_gap - (separator_denominator * c3_radical) ** 2 * 377_823
    )
    assert c3_gap > 0
    assert c3_square_difference == 824_523_723_482_111_238_496_361_641
    assert c3_square_difference > 0

    c4_rational = 597_580_022_071_777_213_687_318_156
    c4_radical = 21_288_970_076_515_705_538
    c4_denominator = 2_290_468_477_489_828_247_376_833_403
    c4_gap = separator_numerator * c4_denominator - separator_denominator * c4_rational
    c4_square_difference = (
        separator_denominator * c4_radical
    ) ** 2 * RADICAND - c4_gap * c4_gap
    assert c4_gap > 0
    assert c4_square_difference == (
        600_035_982_853_463_093_354_803_882_519_517_840_276_863_691_635_717_857_799
    )
    assert c4_square_difference > 0
    return c3_square_difference, c4_square_difference


def decimal(value: Surd) -> float:
    return float(value[0]) + float(value[1]) * sqrt(RADICAND)


def main() -> None:
    if not __debug__:
        raise RuntimeError(
            "run this diagnostic without Python's -O assertion stripping"
        )

    check_weight_reduction()
    check_branch_transitions()
    check_collision_reductions()
    alpha, coefficient, betas, weights = check_global_algebra()
    c3_difference, c4_difference = check_three_prefix_separator()

    expected_grid = {
        12: F(1, 4),
        24: F(871, 3_456),
        48: F(27_907, 110_592),
    }
    grid_results = {}
    for denominator, expected in expected_grid.items():
        value, point = grid_maximum(denominator)
        assert value == expected
        assert value < M_VALUES[4]
        grid_results[denominator] = (value, point)

    print("global four-prefix exact diagnostic: PASS")
    print(f"M4 = {M_VALUES[4]}")
    print(f"x* = {X_STAR}")
    print(f"alpha* ~= {decimal(alpha):.16f}")
    print(f"beta* ~= {tuple(round(decimal(value), 12) for value in betas)}")
    print(f"lambda* ~= {tuple(round(decimal(value), 12) for value in weights)}")
    print(f"C4* ~= {decimal(coefficient):.16f}")
    print(f"branch count = {len(branch_witnesses())}")
    print(f"grid maxima = {grid_results}")
    print(f"C3 separator square difference = {c3_difference}")
    print(f"C4 separator square difference = {c4_difference}")


if __name__ == "__main__":
    main()
