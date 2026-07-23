"""Small exact diagnostic for two-prefix nested-capacity rows.

The script imports only the Python standard library.  It enumerates bounded
binary base/recursive histories, checks the two nested capacity rows, and
compares their exact minima with the quadratic first-difference rule in
(CR28dw73).  It corroborates, but does not replace, the all-history proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


Q = Fraction


@dataclass(frozen=True)
class Row:
    name: str
    n: int
    r: int
    s1: int
    s2: int
    upper_weight: Fraction
    lower_weight: Fraction
    expected_minimizers: tuple[int, ...]


ROWS = (
    Row("inactive_singleton", 7, 5, 3, 2, Q(1, 2), Q(1, 4), (0,)),
    Row("lower_endpoint", 7, 5, 2, 1, Q(1, 2), Q(1, 4), (0,)),
    Row("upper_endpoint", 7, 5, 2, 1, Q(1, 4), Q(1, 4), (1,)),
    Row("interior_quadratic", 14, 10, 5, 1, Q(1, 2), Q(1, 4), (1,)),
    Row("adjacent_collision", 9, 7, 4, 1, Q(1, 2), Q(1, 4), (0, 1)),
    Row("outer_capacity_active", 8, 6, 2, 1, Q(1, 4), Q(1, 4), (2,)),
)


def advantage(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    distance = n - r
    return (
        weight
        * (
            distance * distance
            + 4 * (n - label)
            + 2 * weight * (r - 1 - label) * (n - label)
        )
        / (2 * (2 - weight))
    )


def cumulative_advantage(n: int, r: int, weight: Fraction, count: int) -> Fraction:
    distance = n - r
    return (
        weight
        * (
            count * (distance + 2) ** 2
            + 2 * count * (count - 1)
            + weight * count * (count - 1) * (distance + 1 + Q(2 * count - 1, 3))
        )
        / (2 * (2 - weight))
    )


def allocation_data(row: Row) -> tuple[int, int, int, int, int, int, int]:
    first_length = row.r - row.s1
    second_length = row.s1 - row.s2
    capacity = row.n - row.r + 1
    first_forced = max(0, first_length - capacity)
    total_forced = max(0, first_length + second_length - capacity)
    lower = max(first_forced, total_forced - second_length)
    upper = min(first_length - 1, total_forced)
    return (
        first_length,
        second_length,
        capacity,
        first_forced,
        total_forced,
        lower,
        upper,
    )


def omega(row: Row, upper_recursive: int) -> Fraction:
    first_length, _, _, _, total_forced, _, _ = allocation_data(row)
    lower_recursive = total_forced - upper_recursive
    return (
        cumulative_advantage(row.n, row.r, row.upper_weight, upper_recursive + 1)
        - cumulative_advantage(row.n, row.r, row.upper_weight, 1)
        + cumulative_advantage(
            row.n,
            row.r,
            row.lower_weight,
            first_length + lower_recursive,
        )
        - cumulative_advantage(row.n, row.r, row.lower_weight, first_length)
    )


def first_difference(row: Row, upper_recursive: int) -> Fraction:
    _, _, _, _, total_forced, _, _ = allocation_data(row)
    return advantage(
        row.n,
        row.r,
        row.upper_weight,
        row.r - upper_recursive - 2,
    ) - advantage(
        row.n,
        row.r,
        row.lower_weight,
        row.s1 - total_forced + upper_recursive,
    )


def quadratic_row(row: Row) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    values = tuple(first_difference(row, index) for index in range(3))
    leading = (values[2] - 2 * values[1] + values[0]) / 2
    linear = values[1] - values[0] - leading
    constant = values[0]
    expected_leading = row.upper_weight**2 / (
        2 - row.upper_weight
    ) - row.lower_weight**2 / (2 - row.lower_weight)
    assert leading == expected_leading
    discriminant = linear * linear - 4 * leading * constant
    return leading, linear, constant, discriminant


def predicted_minimizers(row: Row) -> tuple[int, ...]:
    *_, lower, upper = allocation_data(row)
    if lower == upper:
        return (lower,)
    for index in range(lower, upper):
        difference = first_difference(row, index)
        if difference > 0:
            return (index,)
        if difference == 0:
            return (index, index + 1)
    return (upper,)


def enumerate_type_histories(
    row: Row,
) -> tuple[int, Fraction, tuple[int, ...]]:
    (
        first_length,
        second_length,
        capacity,
        first_forced,
        total_forced,
        _,
        _,
    ) = allocation_data(row)
    labels = tuple(range(row.r - 1, row.s2 - 1, -1))
    assert len(labels) == first_length + second_length

    history_count = 0
    minimum: Fraction | None = None
    minimizing_upper_counts: set[int] = set()
    for tail in product((False, True), repeat=len(labels) - 1):
        # False is base and True is recursive; the first letter is forced base.
        recursive = (False, *tail)
        base_count = sum(not value for value in recursive)
        if base_count > capacity:
            continue

        upper_count = sum(recursive[index] for index in range(first_length))
        total_count = sum(recursive)
        assert upper_count >= first_forced
        assert total_count >= total_forced

        cost = sum(
            (
                advantage(
                    row.n,
                    row.r,
                    (row.upper_weight if index < first_length else row.lower_weight),
                    label,
                )
                for index, (label, is_recursive) in enumerate(zip(labels, recursive))
                if is_recursive
            ),
            Q(),
        )
        if minimum is None or cost < minimum:
            minimum = cost
            minimizing_upper_counts = {upper_count}
        elif cost == minimum:
            minimizing_upper_counts.add(upper_count)
        history_count += 1

    assert minimum is not None
    return history_count, minimum, tuple(sorted(minimizing_upper_counts))


def audit_row(row: Row) -> None:
    *_, lower, upper = allocation_data(row)
    assert lower <= upper
    formula_values = {index: omega(row, index) for index in range(lower, upper + 1)}
    formula_minimum = min(formula_values.values())
    formula_minimizers = tuple(
        index for index, value in formula_values.items() if value == formula_minimum
    )
    assert formula_minimizers == row.expected_minimizers
    assert predicted_minimizers(row) == row.expected_minimizers

    differences = [first_difference(row, index) for index in range(lower, upper)]
    assert differences == sorted(differences)
    if row.upper_weight > 0:
        assert all(right > left for left, right in zip(differences, differences[1:]))
    assert all(
        omega(row, index + 1) - omega(row, index) == first_difference(row, index)
        for index in range(lower, upper)
    )

    leading, linear, constant, discriminant = quadratic_row(row)
    history_count, history_minimum, history_upper_counts = enumerate_type_histories(row)
    assert history_minimum == formula_minimum
    assert set(row.expected_minimizers).issubset(history_upper_counts)

    print(
        f"{row.name}: histories={history_count}; Q=[{lower},{upper}]; "
        f"minimizers={formula_minimizers}; "
        f"D(q)=({leading})q^2+({linear})q+({constant}); "
        f"disc={discriminant}"
    )


def audit() -> None:
    if not __debug__:
        raise RuntimeError("exact diagnostic requires assertions; do not use python -O")
    for row in ROWS:
        audit_row(row)
    print(f"finite_discriminant_rows={len(ROWS)}")
    print("two-prefix label-aware finite diagnostic: PASS")


if __name__ == "__main__":
    audit()
