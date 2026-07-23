"""Fixed falsification checks for the local KPGZERO continued-fraction test.

This standalone diagnostic uses only the Python standard library.  It does
not generate convergents and does not scan m, g, subsets, matchings, or
permutations.  Its finitely many hard-coded cases can falsify transcription,
rounding, congruence, and half-open-endpoint formulas; they cannot prove the
symbolic criterion or decide global finiteness versus infinitude.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


LEFT_ABOVE = (
    19,
    0,
    11_116_408_784,
    7_852_541_895,
    3_956_486_681,
    2_794_830_419,
)
LEFT_BELOW = (
    48,
    0,
    445_038_621_131_943_653_377_466_928,
    314_371_708_097_094_017_492_647_115,
    106_968_186_910_788_045_794_799_539,
    75_561_468_228_672_667_087_267_653,
)
RIGHT_ABOVE = (
    81,
    1,
    7_473_073_805_813_661_315_256_495_159_240_494_740_302_603_139_227,
    5_278_919_324_111_360_426_689_943_587_091_134_465_306_838_560_333,
    3_054_110_982_900_027_850_458_258_545_885_918_105_900_862_169_232,
    2_157_399_472_365_615_849_811_321_075_621_115_912_012_063_349_891,
)
LEFT_RESIDUE_MISS = (
    11,
    0,
    117_851,
    83_249,
    9_465,
    6_686,
)
RIGHT_BELOW_EMPTY = (
    4,
    1,
    109,
    77,
    17,
    12,
)


@dataclass(frozen=True)
class Decision:
    """Exact local output for one fixed convergent and branch."""

    domain_minimum: int
    modulus: int
    residue: int
    quadratic_discriminant: int
    window_lower: int | None
    window_upper: int | None
    first_scale: int | None
    last_scale: int | None
    count: int
    minimizing_scale: int
    admission_discriminant: int


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the mathematical ceiling for a signed integer quotient."""
    assert denominator > 0
    return -((-numerator) // denominator)


def cubic_form(p: int, q: int) -> int:
    """Return Phi(p,q) from KPGZERO-9."""
    return 50 * q**3 + 51 * p * q**2 - 27 * p**2 * q - 24 * p**3


def domain_data(delta: int, p: int, q: int) -> tuple[int, tuple[int, ...]] | None:
    """Return G_delta and the four positive domain coefficients."""
    assert delta in (0, 1)
    coefficients = (
        p * (p - q),
        p * (2 * p + 3 * q),
        p * (7 * q - 2 * p),
        10 * q**2 - 4 * p**2 - p * q,
    )
    if any(value <= 0 for value in coefficients):
        return None
    targets = (9 + 3 * delta, 68 + delta, 12 - 11 * delta, 4 + 3 * delta)
    minimum = max(
        1,
        *(ceil_div(target, value) for target, value in zip(targets, coefficients)),
    )
    return minimum, coefficients


def congruence_class(delta: int, coefficient: int) -> tuple[int, int] | None:
    """Return modulus and least positive residue for KPGZERO-5."""
    divisor = gcd(coefficient, 20)
    target = 8 + delta
    if target % divisor:
        return None
    modulus = 20 // divisor
    reduced_coefficient = coefficient // divisor
    reduced_target = target // divisor
    raw_residue = (
        0
        if modulus == 1
        else reduced_target * pow(reduced_coefficient, -1, modulus) % modulus
    )
    return modulus, raw_residue or modulus


def quadratic_coefficients(delta: int, p: int, q: int) -> tuple[int, int, int]:
    """Return (A,b,C) for A*g^2-b*g+C <= 0."""
    form = cubic_form(p, q)
    assert form
    leading = p * abs(form)
    if form < 0:
        if delta == 0:
            return leading, 7 * p**2 + 18 * p * q + 50 * q**2, -31
        return leading, 2 * p * (13 * p + 12 * q), 31
    if delta == 0:
        return leading, 3 * p * (p - q), 21
    return leading, 50 * q**2 - 16 * p**2 - 9 * p * q, 39


def local_decision(delta: int, p: int, q: int) -> Decision:
    """Evaluate KPGZERO-24d--KPGZERO-24h without an m or g scan."""
    domain = domain_data(delta, p, q)
    assert domain is not None
    domain_minimum, coefficients = domain
    congruence = congruence_class(delta, coefficients[1])
    assert congruence is not None
    modulus, residue = congruence

    leading, linear, constant = quadratic_coefficients(delta, p, q)
    discriminant = linear**2 - 4 * leading * constant

    first_domain_index = max(0, ceil_div(domain_minimum - residue, modulus))
    first_domain_scale = residue + modulus * first_domain_index
    vertex_steps = max(
        0,
        (
            linear
            - 2 * leading * first_domain_scale
            + leading * modulus
        )
        // (2 * leading * modulus),
    )
    minimizing_scale = first_domain_scale + modulus * vertex_steps
    admission_discriminant = discriminant - (
        2 * leading * minimizing_scale - linear
    ) ** 2

    if discriminant < 0:
        return Decision(
            domain_minimum,
            modulus,
            residue,
            discriminant,
            None,
            None,
            None,
            None,
            0,
            minimizing_scale,
            admission_discriminant,
        )

    root_floor = isqrt(discriminant)
    lower = max(
        domain_minimum,
        ceil_div(linear - root_floor, 2 * leading),
    )
    upper = (linear + root_floor) // (2 * leading)
    first_index = max(0, ceil_div(lower - residue, modulus))
    last_index = (upper - residue) // modulus
    count = max(0, last_index - first_index + 1)
    first_scale = residue + modulus * first_index if count else None
    last_scale = residue + modulus * last_index if count else None
    assert (count > 0) == (admission_discriminant >= 0)
    return Decision(
        domain_minimum,
        modulus,
        residue,
        discriminant,
        lower,
        upper,
        first_scale,
        last_scale,
        count,
        minimizing_scale,
        admission_discriminant,
    )


def parameters(delta: int, g: int, p: int, q: int) -> tuple[int, int, int] | None:
    """Reconstruct (m,j,r) directly from one local scale."""
    j_numerator = g * p * (p - q) - (4 + 3 * delta)
    m_numerator = g * p * (2 * p + 3 * q) - (8 + delta)
    r_numerator = g * (10 * q**2 - 4 * p**2 - p * q) + (6 - 3 * delta)
    if j_numerator % 5 or m_numerator % 20 or r_numerator % 10:
        return None
    return (
        m_numerator // 20,
        j_numerator // 5,
        r_numerator // 10,
    )


def kappa(m: int, j: int) -> int:
    """Return the literal descending-min threshold."""
    d = 8 * m + 4
    numerator = j * (d - 1)
    denominator = 2 * (d + j)
    return (numerator + denominator - 1) // denominator


def residuals(delta: int, g: int, p: int, q: int) -> tuple[int, int]:
    """Return (N_delta,Q_delta) from KPGZERO-10 or KPGZERO-12."""
    form = cubic_form(p, q)
    if delta == 0:
        return (
            g**2 * p * form + g * (7 * p**2 + 18 * p * q + 50 * q**2) + 31,
            g**2 * p * form - 3 * g * p * (p - q) - 4,
        )
    return (
        g**2 * p * form + 2 * g * p * (13 * p + 12 * q) - 6,
        g**2 * p * form
        + g * (16 * p**2 + 9 * p * q - 50 * q**2)
        + 14,
    )


def gain(m: int, j: int, r: int, delta: int) -> int:
    """Return the literal left or right insertion gain."""
    left = (
        j**2
        - 26 * j * m
        - 3 * j * r
        - 7 * j
        + 8 * m**2
        - 4 * m * r
        - 12 * m
        - 4 * r
        - 4
    )
    return left if delta == 0 else left - j - 16 * m - 2 * r - 7


def assert_literal_admission(delta: int, g: int, p: int, q: int) -> None:
    """Cross-check one admitted local scale against the literal row."""
    row = parameters(delta, g, p, q)
    assert row is not None
    m, j, r = row
    assert m >= 3 and 1 <= j < m and r >= 1
    assert r == kappa(m, j) == kappa(m, j + 1)
    assert gain(m, j, r, delta) == 0
    upper, lower = residuals(delta, g, p, q)
    assert upper >= 0 and lower < 0


def assert_complete_quotient_identity(
    nu: int,
    p: int,
    q: int,
    p_previous: int,
    q_previous: int,
) -> None:
    """Check the universal error identity with an exact complete quotient."""
    determinant = p_previous * q - p * q_previous
    assert determinant == (-1) ** nu
    complete_quotient = Fraction(17, 5)
    reconstructed = Fraction(
        p * complete_quotient.numerator
        + p_previous * complete_quotient.denominator,
        q * complete_quotient.numerator
        + q_previous * complete_quotient.denominator,
    )
    theta = complete_quotient + Fraction(q_previous, q)
    expected_error = Fraction((-1) ** nu, q**2) / theta
    assert reconstructed - Fraction(p, q) == expected_error
    assert (cubic_form(p, q) > 0) == (nu % 2 == 0)


def assert_shifted_half_open_form(delta: int, g: int, p: int, q: int) -> None:
    """Check the four lattice-adjusted forms retaining <= at equality."""
    leading, linear, constant = quadratic_coefficients(delta, p, q)
    active = leading * g**2 - linear * g + constant
    upper, lower = residuals(delta, g, p, q)
    form = cubic_form(p, q)
    if form < 0 and delta == 0:
        assert active == -upper
    elif form < 0:
        assert active == 25 - upper
    else:
        assert active == lower + 25


def ceiling_residual(m: int, t: int, r: int) -> tuple[int, int, bool]:
    """Return c_t, its half-open denominator, and literal membership."""
    d = 8 * m + 4
    value = 2 * r * (d + t) - t * (d - 1)
    denominator = 2 * (d + t)
    return value, denominator, 0 <= value < denominator


def main() -> None:
    fixed_cases = (
        LEFT_ABOVE,
        LEFT_BELOW,
        RIGHT_ABOVE,
        LEFT_RESIDUE_MISS,
        RIGHT_BELOW_EMPTY,
    )
    for case in fixed_cases:
        assert_complete_quotient_identity(case[0], *case[2:])

    left_above = local_decision(0, LEFT_ABOVE[2], LEFT_ABOVE[3])
    assert (
        left_above.window_lower,
        left_above.window_upper,
        left_above.modulus,
        left_above.residue,
        left_above.first_scale,
        left_above.last_scale,
        left_above.count,
    ) == (1, 4, 5, 4, 4, 4, 1)
    assert left_above.admission_discriminant >= 0
    assert_literal_admission(0, 4, LEFT_ABOVE[2], LEFT_ABOVE[3])

    left_below = local_decision(0, LEFT_BELOW[2], LEFT_BELOW[3])
    assert (
        left_below.window_lower,
        left_below.window_upper,
        left_below.modulus,
        left_below.residue,
        left_below.first_scale,
        left_below.last_scale,
        left_below.count,
    ) == (1, 1, 5, 1, 1, 1, 1)
    assert left_below.admission_discriminant >= 0
    assert_literal_admission(0, 1, LEFT_BELOW[2], LEFT_BELOW[3])

    right_above = local_decision(1, RIGHT_ABOVE[2], RIGHT_ABOVE[3])
    assert (
        right_above.window_lower,
        right_above.window_upper,
        right_above.modulus,
        right_above.residue,
        right_above.first_scale,
        right_above.last_scale,
        right_above.count,
    ) == (1, 36, 20, 19, 19, 19, 1)
    assert right_above.admission_discriminant >= 0
    assert_literal_admission(1, 19, RIGHT_ABOVE[2], RIGHT_ABOVE[3])

    residue_miss = local_decision(
        0,
        LEFT_RESIDUE_MISS[2],
        LEFT_RESIDUE_MISS[3],
    )
    assert residue_miss.quadratic_discriminant > 0
    assert (
        residue_miss.window_lower,
        residue_miss.window_upper,
        residue_miss.modulus,
        residue_miss.residue,
        residue_miss.count,
    ) == (1, 4, 20, 12, 0)
    assert residue_miss.admission_discriminant < 0

    right_below = local_decision(
        1,
        RIGHT_BELOW_EMPTY[2],
        RIGHT_BELOW_EMPTY[3],
    )
    assert right_below.quadratic_discriminant > 0
    assert (right_below.window_lower, right_below.window_upper) == (1, 0)
    assert right_below.count == 0
    assert right_below.admission_discriminant < 0

    assert domain_data(1, 3, 2) is None

    assert_shifted_half_open_form(0, 4, LEFT_ABOVE[2], LEFT_ABOVE[3])
    assert_shifted_half_open_form(0, 1, LEFT_BELOW[2], LEFT_BELOW[3])
    assert_shifted_half_open_form(1, 19, RIGHT_ABOVE[2], RIGHT_ABOVE[3])
    assert_shifted_half_open_form(
        1,
        right_below.residue,
        RIGHT_BELOW_EMPTY[2],
        RIGHT_BELOW_EMPTY[3],
    )

    lower_outside = ceiling_residual(13, 19, 8)
    upper_inside = ceiling_residual(13, 19, 9)
    lower_inside = ceiling_residual(34, 24, 11)
    upper_outside = ceiling_residual(34, 24, 12)
    assert lower_outside == (-1, 254, False)
    assert upper_inside == (253, 254, True)
    assert lower_inside == (0, 600, True)
    assert upper_outside == (600, 600, False)

    print("KPGZERO local-CF criterion diagnostic: PASS")
    print("fixed convergents checked: 5; generated convergents: 0")
    print("singleton scale fibres: L-/g=4, L+/g=1, R-/g=19")
    print("ordinary-discriminant false positives: residue miss and empty integer window")
    print("half-open residuals checked: -1, 0, D-1, D")
    print("m and g scans: 0; global finite/infinite inference: none")


if __name__ == "__main__":
    main()
