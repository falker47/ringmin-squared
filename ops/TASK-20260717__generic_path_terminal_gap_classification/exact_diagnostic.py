"""Exact local checks for the generic path-to-gap relation.

For each fixed ``m``, this script scans only triples ``(m, k, j)``.  It
constructs the constant-size local word obtained by placing the unchanged
oriented path ``P_k`` in terminal gap ``G_j`` and compares every distance-one
and distance-two pair directly with the symbolic formulas.  It constructs no
complete cyclic order or bijection and enumerates no path permutation.
"""

from __future__ import annotations

from fractions import Fraction


CASES = (3, 4, 9, 34)


def path_labels(m: int, path_index: int) -> tuple[int, ...]:
    """Return the unchanged oriented labels of ``P_k``."""
    if m < 3:
        raise ValueError("expected m >= 3")
    if not 0 <= path_index < 2 * m:
        raise ValueError("path index outside 0 <= k < 2*m")

    d = 8 * m + 4
    if path_index <= m:
        return (
            d - 1 - 2 * path_index,
            4 * m + 2 + path_index,
            d - 2 - 2 * path_index,
        )
    return (4 * m + 2 + path_index,)


def local_gap_word(m: int, path_index: int, gap: int) -> tuple[int, ...]:
    """Return only ``(E_j, lambda_j, P_k, rho_{j+1}, E_{j+1})``."""
    gap_count = 2 * m
    if not 0 <= gap < gap_count:
        raise ValueError("gap index outside 0 <= j < 2*m")

    d = 8 * m + 4
    successor = (gap + 1) % gap_count
    return (
        d + gap,
        4 * m - 2 * gap,
        *path_labels(m, path_index),
        4 * m + 1 - 2 * successor,
        d + successor,
    )


def local_rows(
    word: tuple[int, ...], distance: int
) -> tuple[tuple[Fraction, int, int], ...]:
    """Score every displayed pair at one fixed positional distance."""
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


def ceiling_fraction(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative rational number."""
    return (numerator + denominator - 1) // denominator


def main() -> None:
    for m in CASES:
        d = 8 * m + 4
        n = 10 * m + 3
        gap_count = 2 * m
        threshold = Fraction(d * (d - 1), 2)
        allowed_pair_count = 0

        for path_index in range(gap_count):
            observed_allowed: list[int] = []

            for gap in range(gap_count):
                word = local_gap_word(m, path_index, gap)
                distance_one = local_rows(word, 1)
                distance_two = local_rows(word, 2)
                one_ok = all(score <= threshold for score, _, _ in distance_one)
                two_ok = all(score <= threshold for score, _, _ in distance_two)

                successor = (gap + 1) % gap_count
                e_j = d + gap
                lambda_j = 4 * m - 2 * gap
                rho_successor = 4 * m + 1 - 2 * successor
                e_successor = d + successor

                # The unchanged low--terminal--low pair across E_j is also safe.
                rho_j = 4 * m + 1 - 2 * gap
                assert Fraction(rho_j * lambda_j, 2) < threshold
                assert one_ok

                if path_index <= m:
                    a_k, c_k, b_k = path_labels(m, path_index)
                    expected_distance_one = (
                        (Fraction(e_j * lambda_j), 0, 1),
                        (Fraction(lambda_j * a_k), 1, 2),
                        (Fraction(a_k * c_k), 2, 3),
                        (Fraction(c_k * b_k), 3, 4),
                        (Fraction(b_k * rho_successor), 4, 5),
                        (Fraction(rho_successor * e_successor), 5, 6),
                    )
                    expected_distance_two = (
                        (Fraction(e_j * a_k, 2), 0, 2),
                        (Fraction(lambda_j * c_k, 2), 1, 3),
                        (Fraction(a_k * b_k, 2), 2, 4),
                        (Fraction(c_k * rho_successor, 2), 3, 5),
                        (Fraction(b_k * e_successor, 2), 4, 6),
                    )
                    assert distance_one == expected_distance_one
                    assert distance_two == expected_distance_two

                    path_positions = frozenset((2, 3, 4))
                    path_distance_one = tuple(
                        row
                        for row in distance_one
                        if row[1] in path_positions or row[2] in path_positions
                    )
                    assert maximum_rows(path_distance_one) == (
                        Fraction(a_k * c_k),
                        ((2, 3),),
                    )
                    assert Fraction(a_k * c_k) == threshold - path_index * (
                        2 * path_index + 1
                    )

                    expected_left = Fraction((d + gap) * a_k, 2)
                    assert maximum_rows(distance_two) == (expected_left, ((0, 2),))

                    observed_right = distance_two[-1][0]
                    if gap <= gap_count - 2:
                        expected_right = Fraction(b_k * (d + gap + 1), 2)
                        assert expected_left - expected_right == Fraction(
                            gap + 2 * path_index + 2, 2
                        )
                        assert (expected_right <= threshold) == (
                            (gap + 1) * b_k <= d * (2 * path_index + 1)
                        )
                    else:
                        expected_right = Fraction(d * b_k, 2)
                        assert expected_right < threshold
                        assert word == (
                            n,
                            2,
                            a_k,
                            c_k,
                            b_k,
                            4 * m + 1,
                            d,
                        )
                    assert observed_right == expected_right
                    assert expected_left > expected_right

                    formula_ok = gap * a_k <= 2 * path_index * d
                    cutoff = min(gap_count - 1, (2 * path_index * d) // a_k)
                    kappa = ceiling_fraction(gap * (d - 1), 2 * (d + gap))
                    assert formula_ok == (gap <= cutoff)
                    assert formula_ok == (path_index >= kappa)
                    assert two_ok == formula_ok
                else:
                    (x_k,) = path_labels(m, path_index)
                    expected_distance_one = (
                        (Fraction(e_j * lambda_j), 0, 1),
                        (Fraction(lambda_j * x_k), 1, 2),
                        (Fraction(x_k * rho_successor), 2, 3),
                        (Fraction(rho_successor * e_successor), 3, 4),
                    )
                    expected_distance_two = (
                        (Fraction(e_j * x_k, 2), 0, 2),
                        (Fraction(lambda_j * rho_successor, 2), 1, 3),
                        (Fraction(x_k * e_successor, 2), 2, 4),
                    )
                    assert distance_one == expected_distance_one
                    assert distance_two == expected_distance_two

                    path_positions = frozenset((2,))
                    path_distance_one = tuple(
                        row
                        for row in distance_one
                        if row[1] in path_positions or row[2] in path_positions
                    )
                    if gap <= gap_count - 2:
                        expected_one = (Fraction(x_k * (4 * m - 2 * gap)), ((1, 2),))
                        expected_two = (Fraction(x_k * (d + gap + 1), 2), ((2, 4),))
                    else:
                        expected_one = (Fraction(x_k * (4 * m + 1)), ((2, 3),))
                        expected_two = (Fraction(x_k * n, 2), ((0, 2),))
                        assert word == (n, 2, x_k, 4 * m + 1, d)
                    assert maximum_rows(path_distance_one) == expected_one
                    assert maximum_rows(distance_two) == expected_two
                    assert two_ok
                    formula_ok = True

                assert (one_ok and two_ok) == formula_ok
                if formula_ok:
                    observed_allowed.append(gap)
                    allowed_pair_count += 1

            if path_index <= m:
                a_k = d - 1 - 2 * path_index
                cutoff = min(gap_count - 1, (2 * path_index * d) // a_k)
                assert tuple(observed_allowed) == tuple(range(cutoff + 1))
            else:
                assert tuple(observed_allowed) == tuple(range(gap_count))

        last_nonclosing_kappa = ceiling_fraction(
            (gap_count - 2) * (d - 1), 2 * (d + gap_count - 2)
        )
        closing_kappa = ceiling_fraction((gap_count - 1) * (d - 1), 2 * n)
        assert last_nonclosing_kappa == (4 * m + 1) // 5
        assert closing_kappa == (4 * m + 3) // 5

        # Check the path-type transition without constructing an assignment.
        assert path_labels(m, m) == (6 * m + 3, 5 * m + 2, 6 * m + 2)
        assert path_labels(m, m + 1) == (5 * m + 3,)
        assert local_gap_word(m, m, gap_count - 2) == (
            n - 1,
            4,
            6 * m + 3,
            5 * m + 2,
            6 * m + 2,
            3,
            n,
        )

        if m == 3:
            expected_rows = {
                0: (0,),
                1: (0, 1, 2),
                2: (0, 1, 2, 3, 4),
                3: (0, 1, 2, 3, 4, 5),
                4: (0, 1, 2, 3, 4, 5),
                5: (0, 1, 2, 3, 4, 5),
            }
            for path_index, expected in expected_rows.items():
                actual = tuple(
                    gap
                    for gap in range(gap_count)
                    if all(
                        score <= threshold
                        for distance in (1, 2)
                        for score, _, _ in local_rows(
                            local_gap_word(m, path_index, gap), distance
                        )
                    )
                )
                assert actual == expected

        if m == 34:
            equality_word = local_gap_word(m, 11, 24)
            equality_score = local_rows(equality_word, 2)[0][0]
            assert equality_score == threshold

        total_triples = gap_count * gap_count
        print(
            f"m={m} scanned={total_triples} allowed={allowed_pair_count} "
            f"last_nonclosing_kappa={last_nonclosing_kappa} "
            f"closing_kappa={closing_kappa}"
        )


if __name__ == "__main__":
    main()
