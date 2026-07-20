"""Internal bounded verification for the canonical even-v PGE5 scaffold.

This standalone standard-library script reconstructs the literal scaffold.  It
does not import production code, tests, or the preceding task diagnostic.

Two bounded checks are deliberately separate.  On ``m = 2..20``, a bipartite
oracle builds edges only from literal local words and decides forced-edge
extendibility with augmenting paths.  It uses neither the closed Hall formula
nor ``kappa``; the theoretical support is constructed only afterward for a
set comparison.  On ``m = 2, 3, 4``, an exhaustive check expands every path-to-
gap bijection and compares two independent exact cyclic-score traversals.

This is an internal repository diagnostic.  It is not production code, an
external audit, or evidence of a hosted CI run.
"""

from fractions import Fraction
from itertools import permutations
from math import factorial


MIN_M = 2
ORACLE_MAX_M = 20
EXHAUSTIVE_ROWS = (2, 3, 4)

EXPECTED_ORACLE_ROWS = {
    2: (12, 9, 3),
    3: (27, 22, 5),
    4: (49, 42, 7),
    5: (77, 68, 9),
    6: (110, 99, 11),
    7: (151, 138, 13),
    8: (197, 182, 15),
    9: (251, 234, 17),
    10: (310, 291, 19),
    11: (374, 353, 21),
    12: (447, 424, 23),
    13: (524, 499, 25),
    14: (610, 583, 27),
    15: (699, 670, 29),
    16: (796, 765, 31),
    17: (900, 867, 33),
    18: (1_009, 974, 35),
    19: (1_125, 1_088, 37),
    20: (1_246, 1_207, 39),
}

EXPECTED_ORACLE_TOTALS = (11_476, 8_914, 8_515, 399)

EXPECTED_EXHAUSTIVE_ROWS = {
    2: (24, 4, 20, 6_072, 1_104, 96),
    3: (720, 36, 684, 380_160, 47_520, 4_320),
    4: (40_320, 720, 39_600, 36_408_960, 3_467_520, 322_560),
}

EXPECTED_EXHAUSTIVE_TOTALS = (
    41_064,
    760,
    40_304,
    36_795_192,
    3_516_144,
    326_976,
)


def scaffold(
    m: int,
) -> tuple[int, int, int, tuple[tuple[int, ...], ...]]:
    """Return ``d, n, W_n, paths`` from the literal PGE5 definitions."""
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
    return d, n, threshold, result


def local_word(
    m: int,
    d: int,
    paths: tuple[tuple[int, ...], ...],
    path_index: int,
    gap_index: int,
) -> tuple[int, ...]:
    """Build the literal word ``(E_j, lambda_j, P_k, rho_j+, E_j+)``."""
    next_gap = (gap_index + 1) % (2 * m)
    return (
        d + gap_index,
        4 * m - 2 * gap_index,
        *paths[path_index],
        4 * m + 1 - 2 * next_gap,
        d + next_gap,
    )


def locally_allowed(word: tuple[int, ...], threshold: int) -> bool:
    """Decide local compatibility from every literal distance-one/two pair."""
    return all(
        word[left] * word[left + distance] <= distance * threshold
        for distance in (1, 2)
        for left in range(len(word) - distance)
    )


def literal_adjacency(m: int) -> tuple[tuple[int, ...], ...]:
    """Build path-to-gap adjacency only from literal local-word checks."""
    d, _n, threshold, paths = scaffold(m)
    size = 2 * m
    return tuple(
        tuple(
            gap_index
            for gap_index in range(size)
            if locally_allowed(
                local_word(m, d, paths, path_index, gap_index), threshold
            )
        )
        for path_index in range(size)
    )


def forced_edge_has_perfect_matching(
    adjacency: tuple[tuple[int, ...], ...],
    forced_path: int,
    forced_gap: int,
) -> bool:
    """Decide forced-edge extendibility by residual augmenting paths."""
    size = len(adjacency)
    if forced_gap not in adjacency[forced_path]:
        return False

    gap_owner: list[int | None] = [None] * size
    gap_owner[forced_gap] = forced_path

    def augment(path_index: int, seen_gaps: list[bool]) -> bool:
        for gap_index in adjacency[path_index]:
            if gap_index == forced_gap or seen_gaps[gap_index]:
                continue
            seen_gaps[gap_index] = True
            owner = gap_owner[gap_index]
            if owner is None or augment(owner, seen_gaps):
                gap_owner[gap_index] = path_index
                return True
        return False

    for path_index in range(size):
        if path_index == forced_path:
            continue
        if not augment(path_index, [False] * size):
            return False

    return all(owner is not None for owner in gap_owner)


def augmenting_path_support(
    adjacency: tuple[tuple[int, ...], ...],
) -> frozenset[tuple[int, int]]:
    """Return all literal edges admitted by the forced-edge matching oracle."""
    return frozenset(
        (path_index, gap_index)
        for path_index, gap_indices in enumerate(adjacency)
        for gap_index in gap_indices
        if forced_edge_has_perfect_matching(adjacency, path_index, gap_index)
    )


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of one nonnegative exact quotient."""
    return (numerator + denominator - 1) // denominator


def theoretical_support(m: int, d: int) -> frozenset[tuple[int, int]]:
    """Construct the proved PGE5 support, after the oracle has run."""
    size = 2 * m
    kappas = tuple(
        ceil_div(gap_index * (d - 1), 2 * (d + gap_index)) for gap_index in range(size)
    )
    return frozenset(
        {(0, 0)}
        | {
            (path_index, gap_index)
            for gap_index in range(1, size)
            for path_index in range(kappas[gap_index], size)
        }
    )


def check_oracle_row(m: int) -> tuple[int, int, int, int]:
    """Compare the formula-free oracle with theory on one bounded row."""
    adjacency = literal_adjacency(m)
    local_edges = frozenset(
        (path_index, gap_index)
        for path_index, gap_indices in enumerate(adjacency)
        for gap_index in gap_indices
    )

    # The oracle finishes before the separate theorem-side set is built.
    oracle_edges = augmenting_path_support(adjacency)
    d, _n, _threshold, _paths = scaffold(m)
    expected_edges = theoretical_support(m, d)

    assert oracle_edges == expected_edges
    assert oracle_edges.issubset(local_edges)
    relation_cells = (2 * m) ** 2
    rejected_edges = len(local_edges - oracle_edges)
    observed_row = (len(local_edges), len(oracle_edges), rejected_edges)
    assert observed_row == EXPECTED_ORACLE_ROWS[m]
    return relation_cells, *observed_row


def expanded_order(m: int, assignment: tuple[int, ...]) -> tuple[int, ...]:
    """Expand a path-per-gap bijection into its literal cyclic core order."""
    d, n, _threshold, paths = scaffold(m)
    size = 2 * m
    assert len(assignment) == size
    assert set(assignment) == set(range(size))

    order: list[int] = []
    for gap_index, path_index in enumerate(assignment):
        next_gap = (gap_index + 1) % size
        order.extend((d + gap_index, 4 * m - 2 * gap_index))
        order.extend(paths[path_index])
        order.append(4 * m + 1 - 2 * next_gap)

    result = tuple(order)
    assert len(result) == n - 1
    assert sorted(result) == list(range(2, n + 1))
    return result


def all_pairs_cyclic_score(order: tuple[int, ...]) -> tuple[Fraction, int]:
    """Score every unordered cyclic pair by a direct positional traversal."""
    size = len(order)
    best_numerator = 0
    best_denominator = 1
    pair_checks = 0
    for left in range(size):
        for right in range(left + 1, size):
            separation = right - left
            distance = min(separation, size - separation)
            numerator = order[left] * order[right]
            if numerator * best_denominator > best_numerator * distance:
                best_numerator = numerator
                best_denominator = distance
            pair_checks += 1
    return Fraction(best_numerator, best_denominator), pair_checks


def distance_two_cyclic_score(order: tuple[int, ...]) -> tuple[Fraction, int]:
    """Independently score cyclic offsets one and two, including the cut."""
    size = len(order)
    assert size > 4
    best_numerator = 0
    best_denominator = 1
    pair_checks = 0
    for distance in (1, 2):
        for left in range(size):
            right = (left + distance) % size
            numerator = order[left] * order[right]
            if numerator * best_denominator > best_numerator * distance:
                best_numerator = numerator
                best_denominator = distance
            pair_checks += 1
    return Fraction(best_numerator, best_denominator), pair_checks


def check_exhaustive_row(m: int) -> tuple[int, int, int, int, int, int]:
    """Enumerate every scaffold bijection and check both score statements."""
    if m not in EXHAUSTIVE_ROWS:
        raise ValueError(f"exhaustive rows are exactly {EXHAUSTIVE_ROWS}")

    d, _n, threshold, paths = scaffold(m)
    size = 2 * m
    permutation_count = 0
    compatible_count = 0
    threshold_score_count = 0
    collapse_count = 0
    all_pair_checks = 0
    distance_two_checks = 0
    local_incidence_checks = 0

    for assignment in permutations(range(size)):
        permutation_count += 1
        local_flags = tuple(
            locally_allowed(local_word(m, d, paths, path_index, gap_index), threshold)
            for gap_index, path_index in enumerate(assignment)
        )
        local_incidence_checks += len(local_flags)
        compatible = all(local_flags)

        order = expanded_order(m, assignment)
        full_score, full_checks = all_pairs_cyclic_score(order)
        short_score, short_checks = distance_two_cyclic_score(order)
        all_pair_checks += full_checks
        distance_two_checks += short_checks

        assert full_score >= threshold
        assert full_score == short_score
        assert compatible == (full_score == threshold)

        compatible_count += int(compatible)
        threshold_score_count += int(full_score == threshold)
        collapse_count += int(full_score == short_score)

    assert permutation_count == factorial(size)
    assert collapse_count == permutation_count
    assert threshold_score_count == compatible_count
    incompatible_count = permutation_count - compatible_count
    observed_row = (
        permutation_count,
        compatible_count,
        incompatible_count,
        all_pair_checks,
        distance_two_checks,
        local_incidence_checks,
    )
    assert observed_row == EXPECTED_EXHAUSTIVE_ROWS[m]
    return observed_row


def main() -> None:
    """Run both bounded internal verification layers and print provenance."""
    print("PGE5 augmenting-path oracle")
    print("m literal_edges oracle_support rejected_edges")
    oracle_totals = [0, 0, 0, 0]
    for m in range(MIN_M, ORACLE_MAX_M + 1):
        relation_cells, local_edges, support_edges, rejected_edges = check_oracle_row(m)
        print(f"{m} {local_edges} {support_edges} {rejected_edges}")
        oracle_totals[0] += relation_cells
        oracle_totals[1] += local_edges
        oracle_totals[2] += support_edges
        oracle_totals[3] += rejected_edges

    assert tuple(oracle_totals) == EXPECTED_ORACLE_TOTALS
    print(
        "oracle totals: "
        f"rows={ORACLE_MAX_M - MIN_M + 1} "
        f"literal_cells={oracle_totals[0]} "
        f"forced_edge_decisions={oracle_totals[1]} "
        f"supported={oracle_totals[2]} rejected={oracle_totals[3]}"
    )

    print("PGE5 exhaustive scaffold bijections")
    print(
        "m bijections compatible noncompatible all_pairs "
        "distance_at_most_two local_incidences"
    )
    exhaustive_totals = [0, 0, 0, 0, 0, 0]
    for m in EXHAUSTIVE_ROWS:
        row = check_exhaustive_row(m)
        print(f"{m} " + " ".join(str(value) for value in row))
        for index, value in enumerate(row):
            exhaustive_totals[index] += value

    assert tuple(exhaustive_totals) == EXPECTED_EXHAUSTIVE_TOTALS
    print(
        "exhaustive totals: "
        f"bijections={exhaustive_totals[0]} "
        f"compatible_and_W_eq_Wn={exhaustive_totals[1]} "
        f"noncompatible_and_W_ne_Wn={exhaustive_totals[2]} "
        f"all_pairs={exhaustive_totals[3]} "
        f"distance_at_most_two={exhaustive_totals[4]} "
        f"local_incidences={exhaustive_totals[5]}"
    )
    print("PASS: every enumerated bijection has W = W^(<=2)")
    print("PASS: literal local compatibility iff W = W_n")
    print(
        "scope: internal repository diagnostic; not production, external audit, or hosted CI"
    )


if __name__ == "__main__":
    main()
