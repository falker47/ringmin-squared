"""Exact local checks for the terminal-gap placement lemma for ``P_0``.

For each fixed ``m``, this script scans only the ``2*m`` terminal-gap
indices.  It constructs the seven labels in the local gap word containing
``P_0`` and checks its distance-one and distance-two inequalities with exact
``Fraction`` arithmetic.  It constructs no complete cyclic order, assigns no
other path, and enumerates no path reassignment.
"""

from __future__ import annotations

from fractions import Fraction


CASES = (3, 4, 9, 25)


def local_gap_word(m: int, gap: int) -> tuple[int, ...]:
    """Return only ``(E_j, lambda_j, P_0, rho_{j+1}, E_{j+1})``."""
    if m < 3:
        raise ValueError("expected m >= 3")

    gap_count = 2 * m
    if not 0 <= gap < gap_count:
        raise ValueError("gap index outside 0 <= j < 2*m")

    d = 8 * m + 4
    successor = (gap + 1) % gap_count
    return (
        d + gap,
        4 * m - 2 * gap,
        d - 1,
        4 * m + 2,
        d - 2,
        4 * m + 1 - 2 * successor,
        d + successor,
    )


def local_rows(
    word: tuple[int, ...], distance: int
) -> tuple[tuple[Fraction, int, int], ...]:
    """Score the displayed local pairs at one fixed positional distance."""
    return tuple(
        (
            Fraction(word[index] * word[index + distance], distance),
            index,
            index + distance,
        )
        for index in range(len(word) - distance)
    )


def maximum_rows(
    rows: tuple[tuple[Fraction, int, int], ...],
) -> tuple[Fraction, tuple[tuple[int, int], ...]]:
    """Return the exact maximum and all maximizing local position pairs."""
    maximum = max(score for score, _, _ in rows)
    maximizers = tuple((left, right) for score, left, right in rows if score == maximum)
    return maximum, maximizers


def main() -> None:
    for m in CASES:
        d = 8 * m + 4
        n = 10 * m + 3
        gap_count = 2 * m
        threshold = Fraction(d * (d - 1), 2)
        left_allowed: list[int] = []
        right_allowed: list[int] = []
        locally_allowed: list[int] = []

        assert n - 1 == 10 * m + 2 > 4

        for gap in range(gap_count):
            word = local_gap_word(m, gap)
            distance_one = local_rows(word, 1)
            distance_two = local_rows(word, 2)

            observed_one = maximum_rows(distance_one)
            expected_one = (threshold, ((2, 3),))
            assert observed_one == expected_one

            expected_two_score = threshold + Fraction(gap * (d - 1), 2)
            observed_two = maximum_rows(distance_two)
            expected_two = (expected_two_score, ((0, 2),))
            assert observed_two == expected_two

            left_score = distance_two[0][0]
            right_score = distance_two[-1][0]
            assert left_score == expected_two_score
            if gap <= gap_count - 2:
                expected_right = threshold + Fraction(gap * (d - 2) - 2, 2)
                assert left_score - right_score == Fraction(gap + 2, 2)
            else:
                expected_right = threshold - Fraction(d, 2)
                assert left_score - right_score == Fraction(
                    d + (gap_count - 1) * (d - 1), 2
                )
            assert right_score == expected_right

            # The unchanged low--terminal--low scaffold pair across E_j is safe.
            rho_j = 4 * m + 1 - 2 * gap
            lambda_j = 4 * m - 2 * gap
            assert Fraction(rho_j * lambda_j, 2) < threshold

            one_ok = all(score <= threshold for score, _, _ in distance_one)
            two_ok = all(score <= threshold for score, _, _ in distance_two)
            assert one_ok
            assert (left_score <= threshold) == (gap == 0)
            assert (right_score <= threshold) == (gap in (0, gap_count - 1))
            assert two_ok == (gap == 0)

            if left_score <= threshold:
                left_allowed.append(gap)
            if right_score <= threshold:
                right_allowed.append(gap)
            if one_ok and two_ok:
                locally_allowed.append(gap)

        closing_word = local_gap_word(m, gap_count - 1)
        assert closing_word == (n, 2, d - 1, 4 * m + 2, d - 2, 4 * m + 1, d)
        assert tuple(left_allowed) == (0,)
        assert tuple(right_allowed) == (0, gap_count - 1)
        assert tuple(locally_allowed) == (0,)
        assert m - 1 not in locally_allowed
        assert m not in locally_allowed
        assert m + 1 not in locally_allowed

        closing_left = Fraction(n * (d - 1), 2)
        closing_right = Fraction(d * (d - 2), 2)
        print(
            f"m={m} gaps={gap_count} "
            f"left_allowed={tuple(left_allowed)} "
            f"right_allowed={tuple(right_allowed)} "
            f"locally_allowed={tuple(locally_allowed)} "
            f"closing_scores=({closing_left}, {closing_right})"
        )


if __name__ == "__main__":
    main()
