"""Independent growing-row diagnostic for the PG69 Ferrers residual.

The exact ceiling factors are built with integer arithmetic and their logs
are summed directly. The script imports no project helper and enumerates no
path permutation, matching, cyclic order, or geometric object.
"""

from __future__ import annotations

from collections import Counter
from math import fsum, log


CASES = (3, 4, 5, 6, 7, 16, 64, 256, 1_024, 4_096, 16_384, 65_536, 262_144)
LINEAR_COEFFICIENT = 14 * log(2) + 6 * log(3) - 10 * log(5) - 2


def ceiling_fraction(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative rational number."""
    return (numerator + denominator - 1) // denominator


def column_threshold(m: int, gap: int) -> int:
    """Evaluate the exact PG69 threshold with integer arithmetic."""
    numerator = gap * (8 * m + 3)
    denominator = 2 * (8 * m + 4 + gap)
    return ceiling_fraction(numerator, denominator)


def row_cutoff(m: int, path_index: int) -> int:
    """Evaluate the inclusive PG70 cutoff for one triple row."""
    return min(
        2 * m - 1,
        2 * path_index * (8 * m + 4) // (8 * m + 3 - 2 * path_index),
    )


def check_case(m: int) -> tuple[float, ...]:
    """Check one row and return its displayed residual summary."""
    if m < 3:
        raise ValueError("expected m >= 3")

    log_factors: list[float] = []
    log_smooth_factors: list[float] = []
    log_lower_factors: list[float] = []
    log_base_factors: list[float] = []
    column_factors: list[int] = []
    previous_threshold = 0

    for gap in range(1, 2 * m):
        denominator = 2 * (8 * m + 4 + gap)
        threshold_numerator = gap * (8 * m + 3)
        threshold = ceiling_fraction(threshold_numerator, denominator)
        factor = gap + 1 - threshold

        assert previous_threshold <= threshold
        assert 1 <= threshold <= max(1, gap - 1)
        assert factor >= 1
        previous_threshold = threshold
        column_factors.append(factor)

        smooth_numerator = (gap + 1) * denominator - threshold_numerator
        lower_numerator = gap * (2 * gap + 8 * m + 5)

        log_factors.append(log(factor))
        log_smooth_factors.append(log(smooth_numerator) - log(denominator))
        log_lower_factors.append(log(lower_numerator) - log(denominator))
        log_base_factors.append(log(gap) + log(gap + 4 * m) - log(gap + 8 * m))

    assert column_threshold(m, 0) == 0
    assert 1 - column_threshold(m, 0) == 1
    assert column_threshold(m, 1) == 1
    assert column_threshold(m, 2 * m - 2) == (4 * m + 1) // 5
    assert column_threshold(m, 2 * m - 1) == (4 * m + 3) // 5
    universal_row = column_threshold(m, 2 * m - 1)
    assert universal_row <= m
    assert all(
        (row_cutoff(m, path) == 2 * m - 1) == (path >= universal_row)
        for path in range(1, m + 1)
    )
    assert row_cutoff(m, m) == 2 * m - 1

    triple_factors = [row_cutoff(m, path) - path + 1 for path in range(1, m + 1)]
    singleton_factors = list(range(m - 1, 0, -1))
    assert triple_factors[-1] == m
    assert singleton_factors[0] == m - 1
    assert singleton_factors[-1] == 1
    row_factors = triple_factors + singleton_factors
    assert Counter(column_factors) == Counter(row_factors)

    log_count = fsum(log_factors)
    log_smooth = fsum(log_smooth_factors)
    log_lower = fsum(log_lower_factors)
    log_base = fsum(log_base_factors)
    log_row = fsum(log(value) for value in row_factors)

    log_m = log(m)
    main_term = 2 * m * log_m + LINEAR_COEFFICIENT * m
    residual = log_count - main_term
    lower_bound = 1 + log(5 / 6) - log_m
    upper_bound = 9 / 4 + log(2 * m * (2 * m + 1))

    assert lower_bound < residual < upper_bound

    direct_ceiling_delta = log_count - log_smooth
    lower_comparator_gap = log_count - log_lower
    homogeneous_gap = log_lower - log_base
    assert -log(m * (2 * m + 1)) < direct_ceiling_delta <= 0
    assert 0 < lower_comparator_gap < log(m * (2 * m + 1))
    assert 0 < homogeneous_gap < 5 / 4

    coefficient_estimate = (log_count - 2 * m * log_m) / m
    return (
        coefficient_estimate,
        residual,
        residual / log_m,
        direct_ceiling_delta / log_m,
        (log_smooth - log_base) / log_m,
        (log_base - main_term) / log_m,
        log_count - log_row,
    )


def main() -> None:
    """Print the growing-row residual table."""
    print(
        "m coefficient_estimate residual residual/log_m count_minus_smooth/log_m "
        "smooth_minus_base/log_m base_residual/log_m dual_row_gap"
    )
    for m in CASES:
        values = check_case(m)
        rendered = " ".join(f"{value:.12g}" for value in values)
        print(f"{m} {rendered}")
    print(
        "PASS: listed rows satisfy the stated all-m envelopes; "
        "no permutation or matching enumeration"
    )


if __name__ == "__main__":
    main()
