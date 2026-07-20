"""Bounded exact checks for the canonical even-v e=5 path/gap support.

The script reconstructs the literal ``n = 10*m + 4`` scaffold directly.
It scans no path permutation and searches for no matching.  Exact integer
comparisons check every local one- and two-step pair, the closed cutoff
formulas, every residual suffix Hall inequality, and the global/reduced
Ferrers distinction on the declared interval ``m = 2..40``.  Constant-size
integer margins also corroborate the separate symbolic full-distance
collapse without constructing a complete assignment.
"""

MIN_M = 2
MAX_M = 40


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative exact quotient."""
    return (numerator + denominator - 1) // denominator


def scaffold(
    m: int,
) -> tuple[int, int, int, tuple[tuple[int, ...], ...]]:
    """Return ``d, n, W_n, paths`` for the canonical even-v e=5 row."""
    if m < MIN_M:
        raise ValueError("the canonical even-v e=5 scaffold requires m >= 2")

    d = 8 * m + 5
    n = 10 * m + 4
    threshold = d * (d - 1) // 2

    paths: list[tuple[int, ...]] = [
        (d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k) for k in range(m + 1)
    ]
    paths.append((5 * m + 3, 5 * m + 4))
    paths.extend((4 * m + 3 + k,) for k in range(m + 2, 2 * m))
    result = tuple(paths)

    assert len(result) == 2 * m
    assert sorted(label for path in result for label in path) == list(
        range(4 * m + 2, d)
    )
    low_labels = sorted(
        [4 * m - 2 * j for j in range(2 * m)]
        + [4 * m + 1 - 2 * j for j in range(2 * m)]
    )
    assert low_labels == list(range(2, 4 * m + 2))
    assert set(range(d, n + 1)) == {d + j for j in range(2 * m)}
    return d, n, threshold, result


def path_type(m: int, k: int) -> str:
    """Classify one path index without inspecting its entries."""
    if 0 <= k <= m:
        return "triple"
    if k == m + 1:
        return "doubleton"
    if m + 2 <= k < 2 * m:
        return "singleton"
    raise ValueError("path index outside the scaffold")


def local_word(
    m: int,
    d: int,
    paths: tuple[tuple[int, ...], ...],
    k: int,
    j: int,
) -> tuple[int, ...]:
    """Return the literal oriented word for path ``k`` in gap ``j``."""
    next_j = (j + 1) % (2 * m)
    return (
        d + j,
        4 * m - 2 * j,
        *paths[k],
        4 * m + 1 - 2 * next_j,
        d + next_j,
    )


def locally_allowed(word: tuple[int, ...], threshold: int) -> bool:
    """Check every local pair at positional distance one or two."""
    for distance in (1, 2):
        for start in range(len(word) - distance):
            if word[start] * word[start + distance] > distance * threshold:
                return False
    return True


def thresholds(m: int, d: int) -> tuple[int, ...]:
    """Return all exact Ferrers column thresholds."""
    return tuple(ceil_div(j * (d - 1), 2 * (d + j)) for j in range(2 * m))


def row_cutoff(m: int, d: int, k: int) -> int:
    """Return the exact last local gap of a triple row."""
    assert 0 <= k <= m
    return min(2 * m - 1, 2 * k * d // (d - 1 - 2 * k))


def residual_hall(
    m: int,
    k: int,
    j: int,
    kappas: tuple[int, ...],
) -> tuple[bool, int]:
    """Check every residual suffix directly after fixing ``(k,j)``."""
    size = 2 * m
    checks = 0
    passes = True
    neighborhood_masks = tuple(
        ((1 << size) - 1) ^ ((1 << kappa) - 1) for kappa in kappas
    )
    for r in range(size):
        if r == j:
            continue
        residual_gap_count = 0
        neighbors = 0
        for gap in range(r, size):
            if gap != j:
                residual_gap_count += 1
                neighbors |= neighborhood_masks[gap]
        neighbors &= ~(1 << k)

        direct = neighbors.bit_count() >= residual_gap_count
        closed = kappas[r] + int(k >= kappas[r]) <= r + int(j > r)
        assert direct == closed
        passes = passes and direct
        checks += 1
    return passes, checks


def check_row(m: int) -> tuple[int, int, int, int, int]:
    """Check one complete parameter row and return exact counters."""
    d, n, threshold, paths = scaffold(m)
    size = 2 * m
    kappas = thresholds(m, d)

    assert kappas[0] == 0
    assert kappas[1] == 1
    assert all(kappas[j] <= kappas[j + 1] for j in range(size - 1))
    assert all(1 <= kappas[j] <= j - 1 for j in range(2, size))
    assert kappas[size - 2] == (4 * m + 1) // 5
    assert kappas[size - 1] == (4 * m + 3) // 5
    assert kappas[size - 1] <= m

    assert sum(path_type(m, k) == "triple" for k in range(size)) == m + 1
    assert sum(path_type(m, k) == "doubleton" for k in range(size)) == 1
    assert sum(path_type(m, k) == "singleton" for k in range(size)) == m - 2
    assert all(path for path in paths)
    if m == 2:
        assert paths == (
            (20, 10, 19),
            (18, 11, 17),
            (16, 12, 15),
            (13, 14),
        )
        assert kappas == (0, 1, 1, 2)
    if m == 3:
        assert kappas == (0, 1, 1, 2, 2, 3)
        assert paths[-2] == (18, 19)
        assert paths[-1] == (20,)
    if m == 10:
        assert 17 * (d - 1 - 2 * 7) == 2 * 7 * d

    assert 2 * (3 * threshold - n * (d - 1)) == (d - 1) * (4 * m + 7)
    assert 4 * threshold - n * (n - 1) == 28 * m * m + 74 * m + 28
    for j in range(size):
        assert (d + j) * (d - 1) - 2 * threshold == j * (d - 1)

    # The unchanged two-step pair across each terminal is always safe.
    for j in range(size):
        rho_j = 4 * m + 1 - 2 * j
        lambda_j = 4 * m - 2 * j
        assert rho_j * lambda_j < 2 * threshold

    local_checks = 0
    local_edges = 0
    hall_checks = 0
    support_checks = 0
    support_edges = 0
    local_board: list[set[int]] = []
    support_board: list[set[int]] = []

    for j in range(size):
        local_column: set[int] = set()
        support_column: set[int] = set()
        for k, path in enumerate(paths):
            kind = path_type(m, k)
            word = local_word(m, d, paths, k, j)
            assert (
                max(word[start] * word[start + 1] for start in range(len(word) - 1))
                < threshold
            )

            distance_two = [
                word[start] * word[start + 2] for start in range(len(word) - 2)
            ]
            if kind == "triple":
                a_k = d - 1 - 2 * k
                expected_max = (d + j) * a_k
                expected_local = j * a_k <= 2 * k * d
                assert expected_local == (j <= row_cutoff(m, d, k))
            elif kind == "doubleton":
                u, w = path
                expected_max = w * (d + j + 1) if j < size - 1 else n * u
                expected_local = True
                assert d * (d - 1) - n * w == 14 * m * m + 12 * m + 4
            else:
                (x_k,) = path
                expected_max = x_k * (d + j + 1) if j < size - 1 else n * x_k
                expected_local = True

            assert max(distance_two) == expected_max
            assert distance_two.count(expected_max) == 1
            direct_local = locally_allowed(word, threshold)
            cutoff_local = k >= kappas[j]
            assert direct_local == expected_local == cutoff_local
            local_checks += 1

            if direct_local:
                local_column.add(k)
                local_edges += 1
                direct_hall, row_hall_checks = residual_hall(m, k, j, kappas)
                expected_support = j > 0 or k == 0
                assert direct_hall == expected_support
                hall_checks += row_hall_checks
                if direct_hall:
                    support_column.add(k)
                    support_edges += 1
            support_checks += 1

            if j == size - 1:
                assert word[:2] == (n, 2)
                assert word[-2:] == (4 * m + 1, d)

        assert local_column == set(range(kappas[j], size))
        expected_support_column = {0} if j == 0 else set(range(kappas[j], size))
        assert support_column == expected_support_column
        local_board.append(local_column)
        support_board.append(support_column)

    # The local board is Ferrers in its literal nested-column order.
    assert all(local_board[j + 1].issubset(local_board[j]) for j in range(size - 1))

    # The complete matching support is not Ferrers: these four incidences
    # are an induced 2K2, invariant under row or column reorderings.
    assert 0 in support_board[0]
    assert 1 in support_board[1]
    assert 0 not in support_board[1]
    assert 1 not in support_board[0]

    # Removing the forced pair (P_0,G_0) leaves a Ferrers support.
    assert all(
        support_board[j + 1].issubset(support_board[j]) for j in range(1, size - 1)
    )
    return local_checks, local_edges, hall_checks, support_checks, support_edges


def main() -> None:
    """Run the declared bounded exact checks."""
    local_checks = 0
    local_edges = 0
    hall_checks = 0
    support_checks = 0
    support_edges = 0
    for m in range(MIN_M, MAX_M + 1):
        row = check_row(m)
        local_checks += row[0]
        local_edges += row[1]
        hall_checks += row[2]
        support_checks += row[3]
        support_edges += row[4]

    assert local_checks == 88_556
    assert local_edges == 69_124
    assert hall_checks == 4_132_070
    assert support_checks == 88_556
    assert support_edges == 67_525

    print("canonical even-v e=5 path/gap support diagnostic: PASS")
    print(f"parameter rows: {MAX_M - MIN_M + 1} (m={MIN_M}..{MAX_M})")
    print(f"literal local relation checks: {local_checks}")
    print(f"local Ferrers edges checked: {local_edges}")
    print(f"residual suffix Hall inequalities: {hall_checks}")
    print(f"support incidences checked: {support_checks}")
    print(f"Hall-extendible support edges: {support_edges}")
    print(f"local zero-column obstructions: {local_edges - support_edges}")
    print("minimum row, empty singleton range, and cyclic closure verified")
    print("full-distance symbolic margins checked on every parameter row")
    print("local board Ferrers; full support non-Ferrers; reduced support Ferrers")


if __name__ == "__main__":
    main()
