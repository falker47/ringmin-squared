"""Bounded exact checks for local-edge extendibility constructions.

For each fixed ``m``, this script scans the already classified local edges
``(k, j)``.  It constructs exactly the interval-shift bijection prescribed by
the proof, checks all of its Ferrers edges, and checks the residual Hall
formula.  It performs no matching search, enumerates no path permutation,
constructs no cyclic core order, and scores no positional pair.
"""

from __future__ import annotations


CASES = (3, 4, 9, 34)
EXPECTED_COUNTS = {
    3: (27, 22),
    4: (49, 42),
    9: (251, 234),
    34: (3614, 3547),
}
EXPECTED_SHIFT_CASES = {
    3: (6, 6, 10),
    4: (13, 8, 21),
    9: (80, 18, 136),
    34: (1268, 68, 2211),
}


def ceiling_fraction(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative rational number."""
    return (numerator + denominator - 1) // denominator


def column_threshold(m: int, gap: int) -> int:
    """Return the exact Ferrers threshold ``kappa_j``."""
    if m < 3:
        raise ValueError("expected m >= 3")
    gap_count = 2 * m
    if not 0 <= gap < gap_count:
        raise ValueError("gap index outside 0 <= j < 2*m")

    d = 8 * m + 4
    return ceiling_fraction(gap * (d - 1), 2 * (d + gap))


def is_local_edge(m: int, path_index: int, gap: int) -> bool:
    """Return whether ``(path_index, gap)`` belongs to ``R_loc``."""
    gap_count = 2 * m
    if not 0 <= path_index < gap_count:
        raise ValueError("path index outside 0 <= k < 2*m")
    return path_index >= column_threshold(m, gap)


def residual_hall_holds(m: int, path_index: int, gap: int) -> bool:
    """Evaluate the exact residual suffix form of Hall's condition."""
    if not is_local_edge(m, path_index, gap):
        raise ValueError("the prescribed edge must be local")

    for minimum_gap in range(2 * m):
        if minimum_gap == gap:
            continue
        kappa = column_threshold(m, minimum_gap)
        left = kappa + int(path_index >= kappa)
        right = minimum_gap + int(gap > minimum_gap)
        if left > right:
            return False
    return True


def interval_shift(m: int, path_index: int, gap: int) -> tuple[int, ...]:
    """Construct the proof's unique prescribed interval shift."""
    if not is_local_edge(m, path_index, gap):
        raise ValueError("the prescribed edge must be local")
    if gap == 0 and path_index > 0:
        raise ValueError("the prescribed local edge is not extendible")

    gap_count = 2 * m
    assignment = list(range(gap_count))
    if gap < path_index:
        if gap < 1:
            raise AssertionError("right shifts must start at a positive gap")
        assignment[gap] = path_index
        for shifted_gap in range(gap + 1, path_index + 1):
            assignment[shifted_gap] = shifted_gap - 1
    elif gap > path_index:
        if path_index < 1:
            raise AssertionError("locality must preserve the forced zero edge")
        for shifted_gap in range(path_index, gap):
            assignment[shifted_gap] = shifted_gap + 1
        assignment[gap] = path_index

    result = tuple(assignment)
    assert tuple(sorted(result)) == tuple(range(gap_count))
    assert result[gap] == path_index
    assert result[0] == 0
    assert all(
        is_local_edge(m, assigned_path, assigned_gap)
        for assigned_gap, assigned_path in enumerate(result)
    )
    return result


def direct_deficient_suffix(m: int, path_index: int) -> tuple[int, int]:
    """Return gap/neighbor counts after forcing ``(path_index, 0)``."""
    gap_count = 2 * m
    residual_gaps = tuple(range(1, gap_count))
    residual_neighbors = {
        candidate_path
        for candidate_path in range(gap_count)
        if candidate_path != path_index
        and any(
            is_local_edge(m, candidate_path, candidate_gap)
            for candidate_gap in residual_gaps
        )
    }
    assert residual_neighbors == set(range(1, gap_count)) - {path_index}
    return len(residual_gaps), len(residual_neighbors)


def main() -> None:
    for m in CASES:
        gap_count = 2 * m
        kappas = tuple(column_threshold(m, gap) for gap in range(gap_count))
        assert tuple(sorted(kappas)) == kappas
        assert kappas[0] == 0
        assert kappas[1] == 1
        assert all(1 <= kappas[gap] <= gap - 1 for gap in range(2, gap_count))
        assert kappas[-1] == (4 * m + 3) // 5

        local_count = 0
        extendible_count = 0
        obstruction_count = 0
        shift_cases = {"left": 0, "identity": 0, "right": 0}

        for path_index in range(gap_count):
            for gap in range(gap_count):
                if not is_local_edge(m, path_index, gap):
                    continue
                local_count += 1
                expected_extendible = gap >= 1 or path_index == 0
                assert residual_hall_holds(m, path_index, gap) == expected_extendible

                if expected_extendible:
                    assignment = interval_shift(m, path_index, gap)
                    assert assignment[gap] == path_index
                    extendible_count += 1
                    if gap < path_index:
                        shift_cases["right"] += 1
                    elif gap == path_index:
                        shift_cases["identity"] += 1
                    else:
                        shift_cases["left"] += 1
                else:
                    assert gap == 0 < path_index
                    gap_size, neighbor_size = direct_deficient_suffix(m, path_index)
                    assert gap_size == gap_count - 1
                    assert neighbor_size == gap_count - 2
                    obstruction_count += 1

        assert (local_count, extendible_count) == EXPECTED_COUNTS[m]
        assert (
            shift_cases["left"],
            shift_cases["identity"],
            shift_cases["right"],
        ) == EXPECTED_SHIFT_CASES[m]
        assert obstruction_count == gap_count - 1
        assert local_count - extendible_count == obstruction_count

        # Direct boundary witnesses: path-type crossing, terminal singleton,
        # and the cyclic closing column already encoded by kappa_{v-1}.
        assert interval_shift(m, m, m + 1)[m + 1] == m
        assert interval_shift(m, m + 1, m)[m] == m + 1
        assert interval_shift(m, gap_count - 1, 1)[1] == gap_count - 1
        closing_path = kappas[-1]
        assert interval_shift(m, closing_path, gap_count - 1)[-1] == closing_path
        assert interval_shift(m, gap_count - 1, gap_count - 1) == tuple(
            range(gap_count)
        )

        if m == 3:
            assert kappas == (0, 1, 1, 2, 2, 3)
        if m == 34:
            assert is_local_edge(m, 11, 24)
            assert interval_shift(m, 11, 24)[24] == 11

        print(
            f"m={m} local={local_count} extendible={extendible_count} "
            f"obstructions={obstruction_count} shifts={shift_cases} "
            f"closing_kappa={kappas[-1]}"
        )


if __name__ == "__main__":
    main()
