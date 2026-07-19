"""Standalone formula-only diagnostic for the PG98 logarithmic coefficient.

The script evaluates only the explicit PG69 and PG75 factors indexed by
``j``. It imports no project helper and constructs no combinatorial or
geometric object.
"""

from __future__ import annotations

from math import fsum, lgamma, log


SMALL_CASES = (3, 4, 5, 6, 7)
RESIDUE_BLOCKS = (125, 2_045, 32_765, 262_140)
CASES = SMALL_CASES + tuple(
    base + residue for base in RESIDUE_BLOCKS for residue in range(5)
)
LINEAR_COEFFICIENT = 14 * log(2) + 6 * log(3) - 10 * log(5) - 2
LOG_COEFFICIENT = 3 / 4
ROUNDING_COEFFICIENT = 5 / 4


def ceiling_fraction(numerator: int, denominator: int) -> int:
    """Return the exact ceiling of a nonnegative rational number."""
    return (numerator + denominator - 1) // denominator


def endpoint_factors(m: int) -> tuple[int, int]:
    """Return the two exact PG71 endpoint factors."""
    values = []
    for gap in (2 * m - 2, 2 * m - 1):
        denominator = 2 * (8 * m + 4 + gap)
        threshold = ceiling_fraction(gap * (8 * m + 3), denominator)
        values.append(gap + 1 - threshold)
    return values[0], values[1]


def expected_endpoint_factors(m: int) -> tuple[int, int]:
    """Evaluate the five residue branches displayed in PG97."""
    quotient, residue = divmod(m, 5)
    branches = (
        (6 * quotient - 1, 6 * quotient),
        (6 * quotient, 6 * quotient + 1),
        (6 * quotient + 2, 6 * quotient + 2),
        (6 * quotient + 3, 6 * quotient + 3),
        (6 * quotient + 4, 6 * quotient + 5),
    )
    return branches[residue]


def assert_close(left: float, right: float) -> None:
    """Assert agreement at a scale appropriate for summed float logs."""
    tolerance = 2e-10 + 3e-12 * max(abs(left), abs(right))
    assert abs(left - right) <= tolerance, (left, right, tolerance)


def check_case(m: int) -> tuple[float, ...]:
    """Evaluate one formula row and return its component residuals."""
    if m < 3:
        raise ValueError("expected m >= 3")

    log_a_terms: list[float] = []
    log_c_terms: list[float] = []
    log_s_terms: list[float] = []
    log_r_terms: list[float] = []
    delta_terms: list[float] = []
    theta_terms: list[float] = []
    direct_ceiling_terms: list[float] = []

    for gap in range(1, 2 * m):
        common_denominator = 2 * (8 * m + 4 + gap)
        threshold_numerator = gap * (8 * m + 3)
        threshold = ceiling_fraction(threshold_numerator, common_denominator)
        factor_a = gap + 1 - threshold
        numerator_c = gap * (2 * gap + 8 * m + 5)
        numerator_s = numerator_c + common_denominator
        rounding_numerator = factor_a * common_denominator - numerator_c

        assert factor_a == 1 + numerator_c // common_denominator
        assert 0 < rounding_numerator <= common_denominator

        log_a = log(factor_a)
        log_c = log(numerator_c) - log(common_denominator)
        log_s = log(numerator_s) - log(common_denominator)
        log_r = log(gap) + log(gap + 4 * m) - log(gap + 8 * m)
        log_a_terms.append(log_a)
        log_c_terms.append(log_c)
        log_s_terms.append(log_s)
        log_r_terms.append(log_r)
        delta_terms.append(log_c - log_r)
        theta_terms.append(log_a - log_c)
        direct_ceiling_terms.append(log_a - log_s)

    assert endpoint_factors(m) == expected_endpoint_factors(m)

    log_count = fsum(log_a_terms)
    log_c = fsum(log_c_terms)
    log_s = fsum(log_s_terms)
    log_z = fsum(log_r_terms)
    log_z_gamma = (
        lgamma(2 * m)
        + lgamma(6 * m)
        + lgamma(8 * m + 1)
        - lgamma(4 * m + 1)
        - lgamma(10 * m)
    )
    delta = fsum(delta_terms)
    theta = fsum(theta_terms)
    direct_ceiling = fsum(direct_ceiling_terms)

    assert delta > 0
    assert theta > 0
    assert direct_ceiling <= 0
    assert_close(log_z, log_z_gamma)
    assert_close(log_c, log_z + delta)
    assert_close(log_count, log_c + theta)
    assert_close(log_count, log_s + direct_ceiling)
    assert_close(log_count, log_z + delta + theta)

    log_m = log(m)
    main_term = 2 * m * log_m + LINEAR_COEFFICIENT * m
    total_centered = log_count - main_term - LOG_COEFFICIENT * log_m
    z_centered = log_z - main_term + 0.5 * log_m
    theta_centered = theta - ROUNDING_COEFFICIENT * log_m
    direct_centered = direct_ceiling + LOG_COEFFICIENT * log_m
    decomposition_gap = log_count - (log_z + delta + theta)
    return (
        total_centered,
        z_centered,
        delta,
        theta_centered,
        direct_centered,
        decomposition_gap,
    )


def main() -> None:
    """Print the separated PG98 component table."""
    print(
        "m mod5 total_centered z_centered delta theta_centered "
        "direct_ceiling_centered decomposition_gap"
    )
    for m in CASES:
        values = check_case(m)
        rendered = " ".join(f"{value:.12g}" for value in values)
        print(f"{m} {m % 5} {rendered}")
    print("PASS: listed rows satisfy the formula-only component checks")


if __name__ == "__main__":
    main()
