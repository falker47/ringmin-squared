"""Independent exact checks for the one-triple reversal obstruction.

This script uses only the Python standard library.  It reconstructs the
specialized ``n = 10*m + 3`` block family directly, without importing project
or test helpers and without enumerating cyclic orders.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


CASES = ((3, 0), (3, 1), (3, 3), (4, 2), (9, 0), (9, 9))


def perturbed_order(m: int, triple_index: int) -> tuple[int, ...]:
    if m < 3 or not 0 <= triple_index <= m:
        raise ValueError("expected m >= 3 and 0 <= triple_index <= m")

    d = 8 * m + 4
    v = 2 * m
    middle_paths: list[tuple[int, ...]] = [
        (d - 1 - 2 * block, 4 * m + 2 + block, d - 2 - 2 * block)
        for block in range(m + 1)
    ]
    left, connector, right = middle_paths[triple_index]
    middle_paths[triple_index] = (right, connector, left)
    middle_paths.extend((value,) for value in range(5 * m + 3, 6 * m + 2))
    assert len(middle_paths) == v

    order: list[int] = []
    for block, middle_path in enumerate(middle_paths):
        order.extend(
            (
                d + block,
                4 * m - 2 * block,
                *middle_path,
                4 * m + 1 - 2 * ((block + 1) % v),
            )
        )

    result = tuple(order)
    n = 10 * m + 3
    assert len(result) == n - 1
    assert set(result) == set(range(2, n + 1))
    return result


def pair_rows(order: tuple[int, ...]) -> tuple[tuple[Fraction, int, int, int], ...]:
    positions = {label: position for position, label in enumerate(order)}
    vertex_count = len(order)
    rows = []
    for left, right in combinations(sorted(positions), 2):
        separation = abs(positions[left] - positions[right])
        distance = min(separation, vertex_count - separation)
        rows.append((Fraction(left * right, distance), left, right, distance))
    return tuple(rows)


def closing_scores(order: tuple[int, ...]) -> tuple[Fraction, Fraction, Fraction]:
    vertex_count = len(order)
    return tuple(
        max(
            Fraction(
                order[position] * order[(position + distance) % vertex_count],
                distance,
            )
            for position in range(vertex_count - distance, vertex_count)
        )
        for distance in (1, 2, 3)
    )


def main() -> None:
    for m, triple_index in CASES:
        n = 10 * m + 3
        d = 8 * m + 4
        threshold = Fraction(d * (d - 1), 2)
        expected = Fraction(d * d - 1, 2) if triple_index == 0 else threshold
        order = perturbed_order(m, triple_index)
        rows = pair_rows(order)
        distance_scores = tuple(
            max(score for score, _, _, q in rows if q == distance)
            for distance in (1, 2, 3)
        )
        long_score = max(score for score, _, _, q in rows if q >= 4)
        expected_closing = (
            Fraction((4 * m + 1) * d),
            Fraction((6 * m + 1) * d, 2),
            Fraction(
                (4 * m + 1) * (d - 2 if triple_index == 0 else d - 1),
                3,
            ),
        )

        assert distance_scores[0] == threshold
        assert distance_scores[1] == expected
        assert distance_scores[2] == Fraction((5 * m + 2) * (9 * m + 5), 3)
        assert distance_scores[2] < threshold
        assert long_score == Fraction(n * (n - 1), 4) < threshold
        assert closing_scores(order) == expected_closing
        assert max(score for score, _, _, _ in rows) == expected

        print(
            f"m={m} s={triple_index} n={n} "
            f"M1={distance_scores[0]} M2={distance_scores[1]} "
            f"M3={distance_scores[2]} M>=4={long_score} "
            f"C={expected_closing} W={expected}"
        )


if __name__ == "__main__":
    main()
