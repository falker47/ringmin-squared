"""Exact checks for the fixed nonlocal middle-path rotation.

The family was fixed before this diagnostic: for ``n = 10*m + 3`` the
terminal gap ``G_j`` receives the entire oriented path
``P_{j+1 mod 2*m}``.  This script uses only the Python standard library,
imports no project or test helper, and does not enumerate cyclic orders.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


CASES = (3, 4, 9, 25)


def rotated_order(m: int) -> tuple[int, ...]:
    """Construct only the a-priori fixed one-gap path rotation."""
    if m < 3:
        raise ValueError("expected m >= 3")

    d = 8 * m + 4
    path_count = 2 * m
    paths: list[tuple[int, ...]] = [
        (d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k) for k in range(m + 1)
    ]
    paths.extend((4 * m + 2 + k,) for k in range(m + 1, path_count))
    assert len(paths) == path_count

    order: list[int] = []
    for gap in range(path_count):
        path = paths[(gap + 1) % path_count]
        order.extend(
            (
                d + gap,
                4 * m - 2 * gap,
                *path,
                4 * m + 1 - 2 * ((gap + 1) % path_count),
            )
        )

    result = tuple(order)
    n = 10 * m + 3
    assert len(result) == n - 1
    assert set(result) == set(range(2, n + 1))
    return result


def all_pair_rows(
    order: tuple[int, ...],
) -> tuple[tuple[Fraction, int, int, int], ...]:
    """Score every unordered label pair from an independent position map."""
    positions = {label: position for position, label in enumerate(order)}
    vertex_count = len(order)
    rows = []
    for left, right in combinations(sorted(positions), 2):
        separation = abs(positions[left] - positions[right])
        distance = min(separation, vertex_count - separation)
        rows.append((Fraction(left * right, distance), left, right, distance))
    return tuple(rows)


def maximum_rows(
    rows: tuple[tuple[Fraction, int, int, int], ...],
    *,
    distance: int | None = None,
    long: bool = False,
) -> tuple[Fraction, tuple[tuple[int, int, int], ...]]:
    selected = tuple(
        row
        for row in rows
        if (long and row[3] >= 4) or (not long and row[3] == distance)
    )
    best = max(row[0] for row in selected)
    maximizers = tuple(
        (left, right, q) for score, left, right, q in selected if score == best
    )
    return best, maximizers


def closing_rows(
    order: tuple[int, ...],
) -> tuple[tuple[Fraction, int, int, int], ...]:
    """Score shorter forward arcs that cross the cut before ``order[0]``."""
    vertex_count = len(order)
    rows = []
    for distance in range(1, vertex_count // 2 + 1):
        for position in range(vertex_count - distance, vertex_count):
            left = order[position]
            right = order[(position + distance) % vertex_count]
            rows.append(
                (
                    Fraction(left * right, distance),
                    min(left, right),
                    max(left, right),
                    distance,
                )
            )
    return tuple(rows)


def main() -> None:
    for m in CASES:
        n = 10 * m + 3
        d = 8 * m + 4
        threshold = Fraction(d * (d - 1), 2)
        expected_classes = (
            (threshold, ((4 * m + 2, d - 1, 1),)),
            (Fraction(n * (d - 1), 2), ((d - 1, n, 2),)),
            (Fraction((5 * m + 2) * (9 * m + 4), 3), ((5 * m + 2, 9 * m + 4, 3),)),
            (Fraction(n * (n - 1), 4), ((n - 1, n, 4),)),
        )
        expected_closing = (
            (Fraction((4 * m + 1) * d), ((4 * m + 1, d, 1),)),
            (Fraction(d * (d - 2), 2), ((d - 2, d, 2),)),
            (Fraction(d * (4 * m + 2), 3), ((4 * m + 2, d, 3),)),
            (Fraction(d * (d - 1), 4), ((d - 1, d, 4),)),
        )
        expected_closing_four_to_six = (
            (Fraction(d * (d - 1), 4), ((d - 1, d, 4),)),
            (Fraction(d * d - 4, 10), ((4 * m + 3, d - 2, 5),)),
            (Fraction(d * n, 6), ((d, n, 6),)),
        )

        order = rotated_order(m)
        rows = all_pair_rows(order)
        observed_classes = (
            maximum_rows(rows, distance=1),
            maximum_rows(rows, distance=2),
            maximum_rows(rows, distance=3),
            maximum_rows(rows, long=True),
        )
        assert observed_classes == expected_classes

        cut_rows = closing_rows(order)
        observed_closing = (
            maximum_rows(cut_rows, distance=1),
            maximum_rows(cut_rows, distance=2),
            maximum_rows(cut_rows, distance=3),
            maximum_rows(cut_rows, long=True),
        )
        assert observed_closing == expected_closing
        assert (
            tuple(maximum_rows(cut_rows, distance=distance) for distance in (4, 5, 6))
            == expected_closing_four_to_six
        )

        full_score = max(score for score, _, _, _ in rows)
        full_saturators = tuple(
            (left, right, q) for score, left, right, q in rows if score == full_score
        )
        assert full_score == Fraction(n * (d - 1), 2)
        assert full_saturators == ((d - 1, n, 2),)

        print(
            f"m={m} n={n} d={d} "
            f"M={(observed_classes[0][0], observed_classes[1][0], observed_classes[2][0], observed_classes[3][0])} "
            f"C={(observed_closing[0][0], observed_closing[1][0], observed_closing[2][0], observed_closing[3][0])} "
            f"W={full_score} saturators={full_saturators}"
        )


if __name__ == "__main__":
    main()
