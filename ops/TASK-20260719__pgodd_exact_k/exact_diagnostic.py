"""Bounded exact checks for the induced K score of fixed map (PGODD-6).

This standalone standard-library diagnostic constructs only the prescribed
odd-v PG49-star parity order on ``n = 10*m + 8``.  It imports no project
helper and searches no order, matching, or path permutation.  An independent
least-selected-position max-plus recurrence checks the induced-subset maximum,
and a separate all-proper-oriented-arcs scan checks every compressed shortcut.
All finite limits are explicit below.
"""

from math import comb


DP_MAX_M = 30
FORMULA_MAX_M = 1000


def scaffold(m: int) -> tuple[int, int, tuple[tuple[int, ...], ...]]:
    """Return ``d, n, paths`` for the odd-v e=4 symbolic scaffold."""
    if m < 1:
        raise ValueError("the symbolic branch requires m >= 1")
    d = 8 * m + 8
    n = 10 * m + 8
    paths: list[tuple[int, ...]] = [
        (d - 1 - 2 * k, 4 * m + 4 + k, d - 2 - 2 * k) for k in range(m + 1)
    ]
    paths.append((5 * m + 5, 5 * m + 6))
    paths.extend((4 * m + 5 + k,) for k in range(m + 2, 2 * m + 1))
    result = tuple(paths)
    assert len(result) == 2 * m + 1
    assert sorted(label for path in result for label in path) == list(
        range(4 * m + 4, d)
    )
    return d, n, result


def candidate(m: int) -> tuple[int, ...]:
    """Return the single fixed path-to-gap map (PGODD-6)."""
    q = (4 * m + 5) // 5
    alpha: list[int | None] = [None] * (2 * m + 1)
    alpha[0] = 0
    for j in range(1, q):
        alpha[j] = j
    for j in range(q, m + 1):
        alpha[j] = j + 1
    for j in range(m + 1, 2 * m):
        alpha[j] = 3 * m + 1 - j
    alpha[2 * m] = q
    assert all(value is not None for value in alpha)
    return tuple(int(value) for value in alpha)


def expanded_order(m: int) -> tuple[int, ...]:
    """Expand only (PGODD-6) into its literal cyclic core order."""
    d, n, paths = scaffold(m)
    order: list[int] = []
    for j, k in enumerate(candidate(m)):
        next_j = (j + 1) % (2 * m + 1)
        order.extend((d + j, 4 * m + 2 - 2 * j))
        order.extend(paths[k])
        order.append(4 * m + 3 - 2 * next_j)
    result = tuple(order)
    assert len(result) == n - 1
    assert set(result) == set(range(2, n + 1))
    return result


def cyclic_score(labels: tuple[int, ...]) -> int:
    """Return the exact cyclic adjacent-product sum of a nonempty word."""
    if len(labels) == 1:
        return labels[0] ** 2
    return sum(labels[i - 1] * labels[i] for i in range(len(labels)))


def formula_value(m: int) -> int:
    """Return the proposed exact PGODD K formula."""
    q = (4 * m + 5) // 5
    numerator = (
        1714 * m**3 + 4467 * m**2 + 24 * m * q + 3749 * m + 12 * q**2 + 60 * q + 1032
    )
    assert numerator % 6 == 0
    return numerator // 6


def k825_value(m: int) -> int:
    """Return canonical K825 specialized to the same subsequence."""
    numerator = 572 * m**3 + 1497 * m**2 + 1279 * m + 354
    assert numerator % 2 == 0
    return numerator // 2


def reconstruct_path(
    start: int, end: int, predecessors: list[int | None]
) -> tuple[int, ...]:
    """Reconstruct one maximizing increasing-index path."""
    path = [end]
    cursor = end
    while cursor != start:
        predecessor = predecessors[cursor]
        assert predecessor is not None
        cursor = predecessor
        path.append(cursor)
    path.reverse()
    return tuple(path)


def max_plus_oracle(
    order: tuple[int, ...],
) -> tuple[int, int, tuple[int, ...], int]:
    """Maximize over all nonempty induced subsets without enumerating them."""
    size = len(order)
    best_score = -1
    best_count = 0
    best_indices: tuple[int, ...] = ()
    transitions = 0

    for start in range(size):
        singleton_score = order[start] ** 2
        if singleton_score > best_score:
            best_score = singleton_score
            best_count = 1
            best_indices = (start,)
        elif singleton_score == best_score:
            best_count += 1

        values: list[int | None] = [None] * size
        counts = [0] * size
        predecessors: list[int | None] = [None] * size
        values[start] = 0
        counts[start] = 1

        for end in range(start + 1, size):
            open_best: int | None = None
            open_count = 0
            open_predecessor: int | None = None
            for prior in range(start, end):
                prior_value = values[prior]
                assert prior_value is not None
                candidate_value = prior_value + order[prior] * order[end]
                transitions += 1
                if open_best is None or candidate_value > open_best:
                    open_best = candidate_value
                    open_count = counts[prior]
                    open_predecessor = prior
                elif candidate_value == open_best:
                    open_count += counts[prior]
            assert open_best is not None and open_predecessor is not None
            values[end] = open_best
            counts[end] = open_count
            predecessors[end] = open_predecessor

            closed_score = open_best + order[end] * order[start]
            if closed_score > best_score:
                best_score = closed_score
                best_count = open_count
                best_indices = reconstruct_path(start, end, predecessors)
            elif closed_score == best_score:
                best_count += open_count

    return best_score, best_count, best_indices, transitions


def compressed_arc(
    order: tuple[int, ...], start: int, steps: int, backbone: set[int]
) -> tuple[int, ...]:
    """Materialize one oriented arc after deleting only its internal holes."""
    size = len(order)
    return (
        order[start],
        *(
            order[(start + offset) % size]
            for offset in range(1, steps)
            if order[(start + offset) % size] in backbone
        ),
        order[(start + steps) % size],
    )


def all_arcs_audit(
    m: int, order: tuple[int, ...]
) -> tuple[int, int, int, tuple[int, ...], int, int]:
    """Check every hole and every proper oriented compressed arc."""
    size = len(order)
    low_end = 4 * m + 2
    backbone = set(range(low_end + 1, 10 * m + 9))

    hole_records: list[tuple[int, int, tuple[int, int]]] = []
    for index, label in enumerate(order):
        if label <= low_end:
            left = order[(index - 1) % size]
            right = order[(index + 1) % size]
            assert left in backbone and right in backbone
            gain = left * right - label * (left + right)
            hole_records.append((gain, label, (left, right)))
    minimum_hole = min(gain for gain, _label, _edge in hole_records)
    hole_winners = [record for record in hole_records if record[0] == minimum_hole]
    assert minimum_hole == 28 * m + 26
    assert hole_winners == [(minimum_hole, 4 * m + 2, (8 * m + 8, 8 * m + 7))]

    minimum_shortcut: int | None = None
    shortcut_witness: tuple[int, ...] = ()
    shortcut_winners = 0
    proper_arcs = 0
    shortcut_arcs = 0

    for start in range(size):
        last_kept = order[start]
        retained_edge_sum = 0
        retained_edges = 0
        for steps in range(1, size):
            end = order[(start + steps) % size]
            proper_arcs += 1
            compressed_sum = retained_edge_sum + last_kept * end
            compressed_edges = retained_edges + 1
            if compressed_edges >= 2:
                margin = compressed_sum - order[start] * end
                shortcut_arcs += 1
                if minimum_shortcut is None or margin < minimum_shortcut:
                    minimum_shortcut = margin
                    shortcut_winners = 1
                    shortcut_witness = compressed_arc(order, start, steps, backbone)
                elif margin == minimum_shortcut:
                    shortcut_winners += 1

            if end in backbone:
                retained_edge_sum = compressed_sum
                retained_edges = compressed_edges
                last_kept = end

    assert minimum_shortcut is not None
    q = (4 * m + 5) // 5
    if m == 1:
        expected_margin = 4
        expected_witness = (12, 7, 16)
    elif m == 2:
        expected_margin = 30
        expected_witness = (18, 11, 24)
    else:
        expected_margin = 12 * m + 10
        expected_witness = (8 * m + 7, 4 * m + 4, 8 * m + 6)
    assert q >= 1
    assert minimum_shortcut == expected_margin
    assert shortcut_winners == 1
    assert shortcut_witness == expected_witness
    return (
        minimum_hole,
        minimum_shortcut,
        shortcut_winners,
        shortcut_witness,
        proper_arcs,
        shortcut_arcs,
    )


def check_formula_row(m: int) -> int:
    """Check the literal order, backbone score, residues, and K825 gap."""
    d, n, paths = scaffold(m)
    alpha = candidate(m)
    order = expanded_order(m)
    q = (4 * m + 5) // 5
    backbone_word = tuple(label for label in order if label >= 4 * m + 3)

    assert set(alpha) == set(range(2 * m + 1))
    assert alpha[2 * m] == q
    assert paths[m + 1] == (5 * m + 5, 5 * m + 6)
    assert cyclic_score(backbone_word) == formula_value(m)
    assert formula_value(m) < k825_value(m)

    residue = m % 5
    residue_constants = (5, 1, 2, 3, 4)
    c = residue_constants[residue]
    assert q == (4 * m + c) // 5
    assert 5 * q == 4 * m + c
    residue_numerator = (
        42850 * m**3
        + 112347 * m**2
        + (94925 + 216 * c) * m
        + 25800
        + 300 * c
        + 12 * c**2
    )
    assert residue_numerator == 150 * formula_value(m)

    if m == 1:
        assert alpha == (0, 2, 1)
        assert order == (16, 6, 15, 8, 14, 5, 17, 4, 10, 11, 3, 18, 2, 13, 9, 12, 7)
        assert formula_value(m) == 1843
    elif m == 2:
        assert alpha == (0, 1, 3, 4, 2)
        assert order == (
            24,
            10,
            23,
            12,
            22,
            9,
            25,
            8,
            21,
            13,
            20,
            7,
            26,
            6,
            15,
            16,
            5,
            27,
            4,
            17,
            3,
            28,
            2,
            19,
            14,
            18,
            11,
        )
        assert formula_value(m) == 6729

    assert d == 8 * m + 8 and n == 10 * m + 8
    return len(order)


def main() -> None:
    """Run the declared bounded exact checks."""
    formula_entries = sum(check_formula_row(m) for m in range(1, FORMULA_MAX_M + 1))

    transitions = 0
    proper_arcs = 0
    shortcut_arcs = 0
    for m in range(1, DP_MAX_M + 1):
        order = expanded_order(m)
        score, count, indices, row_transitions = max_plus_oracle(order)
        winner = tuple(order[index] for index in indices)
        assert score == formula_value(m)
        assert count == 1
        assert set(winner) == set(range(4 * m + 3, 10 * m + 9))
        assert row_transitions == comb(len(order) + 1, 3)
        transitions += row_transitions

        (
            _minimum_hole,
            _minimum_shortcut,
            _shortcut_winners,
            _shortcut_witness,
            row_proper_arcs,
            row_shortcut_arcs,
        ) = all_arcs_audit(m, order)
        proper_arcs += row_proper_arcs
        shortcut_arcs += row_shortcut_arcs

    print("odd-v PG49-star induced K diagnostic: PASS")
    print(f"formula/residue rows: {FORMULA_MAX_M} (m=1..{FORMULA_MAX_M})")
    print(f"literal core entries checked: {formula_entries}")
    print(f"max-plus rows: {DP_MAX_M} (m=1..{DP_MAX_M})")
    print(f"max-plus transitions: {transitions}")
    print(f"proper oriented arcs checked: {proper_arcs}")
    print(f"nontrivial compressed shortcuts checked: {shortcut_arcs}")
    print("unique backbone, boundary witnesses, and K825 strictness verified")


if __name__ == "__main__":
    main()
