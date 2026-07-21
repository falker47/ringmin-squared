"""Exact small-row checks for the canonical odd-v, e=5 path/gap support.

This standalone standard-library script reconstructs the literal
``v = 2*m + 1``, ``n = 10*m + 9`` scaffold.  It checks every local
path/gap incidence and every residual suffix Hall inequality for
``m = 1..30``.  Independently, it exhausts every path-to-gap bijection for
``m = 1..3`` and scores every unordered core pair by its true smaller cyclic
distance.  It imports no project or test helper and computes no induced-
subset objective.
"""

from itertools import permutations


MIN_M = 1
MAX_M = 30
EXHAUSTIVE_MAX_M = 3


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative exact quotient."""
    return (numerator + denominator - 1) // denominator


def scaffold(
    m: int,
) -> tuple[int, int, int, tuple[tuple[int, ...], ...]]:
    """Return ``d, n, W_n, paths`` for one canonical odd-v, e=5 row."""
    if m < MIN_M:
        raise ValueError("the canonical odd-v e=5 scaffold requires m >= 1")

    size = 2 * m + 1
    d = 8 * m + 9
    n = 10 * m + 9
    threshold = d * (d - 1) // 2
    middle_count = d - 2 * size - 2
    triple_count = (size + 5 - 2) // 2
    epsilon = middle_count - size - 2 * triple_count
    singleton_count = size - triple_count - epsilon
    assert (triple_count, epsilon, singleton_count) == (m + 2, 0, m - 1)
    paths: list[tuple[int, ...]] = [
        (d - 1 - 2 * k, 4 * m + 4 + k, d - 2 - 2 * k) for k in range(m + 2)
    ]
    paths.extend((4 * m + 4 + k,) for k in range(m + 2, size))
    result = tuple(paths)

    assert len(result) == size
    assert sorted(label for path in result for label in path) == list(
        range(4 * m + 4, d)
    )
    low_labels = sorted(
        [4 * m + 2 - 2 * j for j in range(size)]
        + [4 * m + 3 - 2 * j for j in range(size)]
    )
    assert low_labels == list(range(2, 4 * m + 4))
    assert set(range(d, n + 1)) == {d + j for j in range(size)}
    return d, n, threshold, result


def path_type(m: int, k: int) -> str:
    """Classify one path index without inspecting its entries."""
    if 0 <= k <= m + 1:
        return "triple"
    if m + 2 <= k <= 2 * m:
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
    size = 2 * m + 1
    next_j = (j + 1) % size
    return (
        d + j,
        4 * m + 2 - 2 * j,
        *paths[k],
        4 * m + 3 - 2 * next_j,
        d + next_j,
    )


def locally_allowed(word: tuple[int, ...], threshold: int) -> bool:
    """Check every pair at linear distance one or two in a local word."""
    for distance in (1, 2):
        for start in range(len(word) - distance):
            if word[start] * word[start + distance] > distance * threshold:
                return False
    return True


def thresholds(m: int, d: int) -> tuple[int, ...]:
    """Return all exact Ferrers column thresholds."""
    return tuple(ceil_div(j * (d - 1), 2 * (d + j)) for j in range(2 * m + 1))


def row_cutoff(m: int, d: int, k: int) -> int:
    """Return the exact last local gap of a triple row."""
    assert 0 <= k <= m + 1
    return min(2 * m, 2 * k * d // (d - 1 - 2 * k))


def residual_hall(
    m: int,
    k: int,
    j: int,
    kappas: tuple[int, ...],
) -> tuple[bool, int]:
    """Check every residual suffix directly after fixing ``(k,j)``."""
    size = 2 * m + 1
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


def expand_order(
    m: int,
    d: int,
    paths: tuple[tuple[int, ...], ...],
    assignment: tuple[int, ...],
) -> tuple[int, ...]:
    """Expand one assigned scaffold into its literal cyclic core order."""
    size = 2 * m + 1
    order: list[int] = []
    for j, k in enumerate(assignment):
        next_j = (j + 1) % size
        order.extend(
            (
                d + j,
                4 * m + 2 - 2 * j,
                *paths[k],
                4 * m + 3 - 2 * next_j,
            )
        )
    return tuple(order)


def exact_scores(
    order: tuple[int, ...],
) -> tuple[tuple[int, int], tuple[int, int], tuple[tuple[int, int], ...]]:
    """Return maxima for full, <=2, and the four requested distance classes."""
    length = len(order)
    full = (0, 1)
    truncated = (0, 1)
    classes = [(0, 1) for _ in range(4)]
    for left in range(length):
        for right in range(left + 1, length):
            separation = right - left
            distance = min(separation, length - separation)
            product = order[left] * order[right]
            if product * full[1] > full[0] * distance:
                full = (product, distance)
            if distance <= 2 and product * truncated[1] > truncated[0] * distance:
                truncated = (product, distance)
            class_index = min(distance, 4) - 1
            if product * classes[class_index][1] > classes[class_index][0] * distance:
                classes[class_index] = (product, distance)
    return full, truncated, tuple(classes)


def check_row(m: int) -> tuple[int, int, int, int, int]:
    """Check one complete symbolic row and return exact counters."""
    d, n, threshold, paths = scaffold(m)
    size = 2 * m + 1
    kappas = thresholds(m, d)

    assert kappas[0] == 0
    assert kappas[1] == 1
    assert all(kappas[j] <= kappas[j + 1] for j in range(size - 1))
    assert all(1 <= kappas[j] <= j - 1 for j in range(2, size))
    assert kappas[size - 2] == (4 * m + 3) // 5
    assert kappas[size - 1] == (4 * m + 5) // 5
    assert kappas[size - 1] <= m

    assert sum(path_type(m, k) == "triple" for k in range(size)) == m + 2
    assert sum(path_type(m, k) == "singleton" for k in range(size)) == m - 1
    if m == 1:
        assert paths == ((16, 8, 15), (14, 9, 13), (12, 10, 11))
        assert kappas == (0, 1, 1)
    if m == 2:
        assert paths == (
            (24, 12, 23),
            (22, 13, 21),
            (20, 14, 19),
            (18, 15, 17),
            (16,),
        )
        assert kappas == (0, 1, 1, 2, 2)
    if m == 4:
        assert (d + 2 * m - 1) * (d - 1 - 2 * 3) < 2 * threshold
        assert n * (d - 1 - 2 * 3) > 2 * threshold
    if m == 5:
        assert 7 * (d - 1 - 2 * 3) == 2 * 3 * d

    assert threshold - d * (4 * m + 3) == d
    assert threshold - (4 * m + 3) * (d - 1) == 12 * m + 12
    assert 3 * d - 2 * n == 4 * m + 9
    assert 4 * threshold - n * (n - 1) == 28 * m * m + 102 * m + 72
    for k in range(m + 2):
        a_k, c_k, _b_k = paths[k]
        assert threshold - a_k * c_k == 4 * m + 4 + 2 * k * k
    for j in range(size):
        assert (d + j) * (d - 1) - 2 * threshold == j * (d - 1)
        rho_j = 4 * m + 3 - 2 * j
        lambda_j = 4 * m + 2 - 2 * j
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
            adjacent = [word[start] * word[start + 1] for start in range(len(word) - 1)]
            assert max(adjacent) < threshold
            distance_two = [
                word[start] * word[start + 2] for start in range(len(word) - 2)
            ]

            if kind == "triple":
                a_k = d - 1 - 2 * k
                expected_max = (d + j) * a_k
                expected_local = j * a_k <= 2 * k * d
                assert expected_local == (j <= row_cutoff(m, d, k))
            else:
                (x_k,) = path
                expected_max = x_k * (d + j + 1) if j < size - 1 else x_k * n
                expected_local = True
                assert d * (d - 1) - n * x_k >= 4 * m * m + 42 * m + 36

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
                assert word[-2:] == (4 * m + 3, d)

        assert local_column == set(range(kappas[j], size))
        expected_support_column = {0} if j == 0 else set(range(kappas[j], size))
        assert support_column == expected_support_column
        local_board.append(local_column)
        support_board.append(support_column)

    assert all(local_board[j + 1].issubset(local_board[j]) for j in range(size - 1))
    assert 0 in support_board[0]
    assert 1 in support_board[1]
    assert 0 not in support_board[1]
    assert 1 not in support_board[0]
    assert all(
        support_board[j + 1].issubset(support_board[j]) for j in range(1, size - 1)
    )
    return local_checks, local_edges, hall_checks, support_checks, support_edges


def check_exhaustive_row(m: int) -> tuple[int, int]:
    """Score every scaffold bijection on one small row."""
    d, n, threshold, paths = scaffold(m)
    size = 2 * m + 1
    kappas = thresholds(m, d)
    observed_support: set[tuple[int, int]] = set()
    compatible_count = 0
    assignment_count = 0

    for assignment in permutations(range(size)):
        assignment_count += 1
        order = expand_order(m, d, paths, assignment)
        assert len(order) == n - 1
        assert sorted(order) == list(range(2, n + 1))
        full, truncated, classes = exact_scores(order)
        assert full[0] * truncated[1] == truncated[0] * full[1]
        assert full[0] >= threshold * full[1]
        assert classes[0] == (threshold - (4 * m + 4), 1)
        assert classes[1][0] >= threshold * classes[1][1]
        assert classes[2][0] < threshold * classes[2][1]
        assert classes[3][0] < threshold * classes[3][1]

        compatible = all(assignment[j] >= kappas[j] for j in range(size))
        at_threshold = full[0] == threshold * full[1]
        assert compatible == at_threshold
        if compatible:
            compatible_count += 1
            observed_support.update((assignment[j], j) for j in range(size))

    expected_support = {(0, 0)} | {
        (k, j) for j in range(1, size) for k in range(kappas[j], size)
    }
    assert observed_support == expected_support
    expected_counts = {1: (6, 2), 2: (120, 12), 3: (5_040, 144)}
    assert (assignment_count, compatible_count) == expected_counts[m]
    return assignment_count, compatible_count


def main() -> None:
    """Run the declared direct and exhaustive exact checks."""
    try:
        scaffold(0)
    except ValueError:
        pass
    else:
        raise AssertionError("m=0 must not be admitted by this scaffold")

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

    exhaustive_assignments = 0
    compatible_assignments = 0
    for m in range(MIN_M, EXHAUSTIVE_MAX_M + 1):
        row_assignments, row_compatible = check_exhaustive_row(m)
        exhaustive_assignments += row_assignments
        compatible_assignments += row_compatible

    assert (
        local_checks,
        local_edges,
        hall_checks,
        support_checks,
        support_edges,
    ) == (39_710, 30_948, 1_408_738, 39_710, 30_018)
    assert (exhaustive_assignments, compatible_assignments) == (5_166, 158)

    print("canonical odd-v e=5 path/gap support diagnostic: PASS")
    print(f"direct parameter rows: {MAX_M - MIN_M + 1} (m={MIN_M}..{MAX_M})")
    print(f"literal local relation checks: {local_checks}")
    print(f"local Ferrers edges checked: {local_edges}")
    print(f"residual suffix Hall inequalities: {hall_checks}")
    print(f"support incidences checked: {support_checks}")
    print(f"Hall-extendible support edges: {support_edges}")
    print(f"local zero-column obstructions: {local_edges - support_edges}")
    print(
        "exhaustive scaffold bijections: "
        f"{exhaustive_assignments} (m={MIN_M}..{EXHAUSTIVE_MAX_M})"
    )
    print(f"compatible/full-threshold bijections: {compatible_assignments}")
    print("minimum row, empty singleton range, and true cyclic closure verified")
    print("distance classes 1, 2, 3, and >=4 checked independently")
    print("local board Ferrers; full support non-Ferrers; reduced support Ferrers")


if __name__ == "__main__":
    main()
