"""Independent bounded check of the PG49 Ferrers matching count.

The support is built directly from cross-multiplied integer inequalities.
Its reduced permanent is computed by Ryser inclusion-exclusion over column
subsets and compared with both symbolic Ferrers products. The script uses
only the Python standard library and enumerates no path permutation,
matching, cyclic core order, or positional score.
"""

from __future__ import annotations

from math import factorial, prod


CASES = tuple(range(3, 9))
EXPECTED_COUNTS = {
    3: 36,
    4: 720,
    5: 21_600,
    6: 725_760,
    7: 46_448_640,
    8: 3_292_047_360,
}


def ceiling_fraction(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative rational number."""
    return (numerator + denominator - 1) // denominator


def column_threshold(m: int, gap: int) -> int:
    """Return the exact formula-side threshold ``kappa_j``."""
    if m < 3:
        raise ValueError("expected m >= 3")
    if not 0 <= gap < 2 * m:
        raise ValueError("gap index outside 0 <= j < 2*m")
    d = 8 * m + 4
    return ceiling_fraction(gap * (d - 1), 2 * (d + gap))


def row_cutoff(m: int, path_index: int) -> int:
    """Return the triple-row cutoff ``ell_k``."""
    if not 1 <= path_index <= m:
        raise ValueError("expected a positive triple index")
    d = 8 * m + 4
    return min(2 * m - 1, 2 * path_index * d // (d - 1 - 2 * path_index))


def support_entry(m: int, gap: int, path_index: int) -> int:
    """Build PG49 directly, without calling the threshold functions."""
    size = 2 * m
    if not 0 <= gap < size or not 0 <= path_index < size:
        raise ValueError("support index outside the Ferrers board")
    if gap == 0:
        return int(path_index == 0)

    d = 8 * m + 4
    return int(2 * path_index * (d + gap) >= gap * (d - 1))


def ryser_permanent(matrix: tuple[tuple[int, ...], ...]) -> int:
    """Compute an exact permanent by Ryser subset inclusion-exclusion."""
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("expected a nonempty square matrix")

    total = 0
    for mask in range(1, 1 << size):
        term = 1
        for row in matrix:
            row_sum = sum(row[column] for column in range(size) if mask & (1 << column))
            term *= row_sum
            if term == 0:
                break
        if (size - mask.bit_count()) % 2:
            total -= term
        else:
            total += term
    return total


def column_product(m: int) -> int:
    """Evaluate the symbolic column-threshold formula."""
    return prod(gap + 1 - column_threshold(m, gap) for gap in range(1, 2 * m))


def row_product(m: int) -> int:
    """Evaluate the equivalent triple/singleton row formula."""
    return factorial(m - 1) * prod(
        row_cutoff(m, path_index) - path_index + 1 for path_index in range(1, m + 1)
    )


def check_case(m: int) -> tuple[int, int, int, int]:
    """Check one bounded row and return its displayed summary."""
    size = 2 * m
    kappas = tuple(column_threshold(m, gap) for gap in range(size))

    assert kappas == tuple(sorted(kappas))
    assert kappas[0] == 0
    assert kappas[1] == 1
    assert all(1 <= kappas[gap] <= gap - 1 for gap in range(2, size))
    assert kappas[-2] == (4 * m + 1) // 5
    assert kappas[-1] == (4 * m + 3) // 5
    assert kappas[-1] <= m

    full_support = tuple(
        tuple(support_entry(m, gap, path) for gap in range(size))
        for path in range(size)
    )
    assert full_support[0] == (1,) + (0,) * (size - 1)
    assert all(full_support[path][0] == 0 for path in range(1, size))
    assert all(
        full_support[path][gap] == int(path >= kappas[gap])
        for gap in range(1, size)
        for path in range(1, size)
    )

    reduced = tuple(tuple(row[1:]) for row in full_support[1:])
    ryser_count = ryser_permanent(reduced)
    by_columns = column_product(m)
    by_rows = row_product(m)
    assert ryser_count == by_columns == by_rows == EXPECTED_COUNTS[m]

    if m == 3:
        assert kappas == (0, 1, 1, 2, 2, 3)
        assert tuple(gap + 1 - kappas[gap] for gap in range(1, size)) == (1, 2, 2, 3, 3)
        assert tuple(row_cutoff(m, path) for path in range(1, m + 1)) == (
            2,
            4,
            5,
        )

    reduced_size = size - 1
    return reduced_size, kappas[-2], kappas[-1], ryser_count


def main() -> None:
    """Run the bounded independent permanent checks."""
    print(
        "m reduced_size kappa_penultimate kappa_closing "
        "ferrers_count ryser_count subsets"
    )
    for m in CASES:
        reduced_size, penultimate, closing, ryser_count = check_case(m)
        ferrers_count = column_product(m)
        subset_count = (1 << reduced_size) - 1
        print(
            f"{m} {reduced_size} {penultimate} {closing} "
            f"{ferrers_count} {ryser_count} {subset_count}"
        )
    print("PASS: exact Ryser subset check; no path-permutation enumeration")


if __name__ == "__main__":
    main()
