"""Bounded exact checks for induced K on the fixed map (PGE2ODD-6).

This standalone standard-library diagnostic constructs only the prescribed
odd-v residue-two PG49-star core on ``n = 10*m + 7``.  It imports no project
helper and searches no order, matching, path assignment, or subset.  A
least-selected-position max-plus recurrence checks the induced-subset maximum,
while a separate all-proper-oriented-arcs scan audits every cancellation gain,
compressed shortcut, and cyclic-cut arc.  All finite limits are explicit.
"""

from math import comb


DP_MAX_M = 30
FORMULA_MAX_M = 1000


def closing_index(m: int) -> int:
    """Return the literal threshold ``q = floor((4*m + 3)/5)``."""
    return (4 * m + 3) // 5


def scaffold(m: int) -> tuple[int, int, tuple[tuple[int, ...], ...]]:
    """Return ``D, n, paths`` for the odd-v residue-two scaffold."""
    if m < 1:
        raise ValueError("the symbolic branch requires m >= 1")
    d_terminal = 8 * m + 7
    n = 10 * m + 7
    paths: list[tuple[int, ...]] = [
        (
            d_terminal - 1 - 2 * k,
            4 * m + 4 + k,
            d_terminal - 2 - 2 * k,
        )
        for k in range(m + 1)
    ]
    paths.extend((4 * m + 4 + k,) for k in range(m + 1, 2 * m + 1))
    result = tuple(paths)
    assert len(result) == 2 * m + 1
    assert sum(len(path) == 3 for path in result) == m + 1
    assert sum(len(path) == 1 for path in result) == m
    assert all(len(path) != 2 for path in result)
    assert sorted(label for path in result for label in path) == list(
        range(4 * m + 4, d_terminal)
    )
    return d_terminal, n, result


def fixed_map(m: int) -> tuple[int, ...]:
    """Return only the prescribed path-to-gap map (PGE2ODD-6)."""
    q = closing_index(m)
    alpha = tuple(
        j if j < q else j + 1 if j <= m - 1 else 3 * m - j if j <= 2 * m - 1 else q
        for j in range(2 * m + 1)
    )
    assert set(alpha) == set(range(2 * m + 1))
    return alpha


def expanded_order(m: int) -> tuple[int, ...]:
    """Expand only (PGE2ODD-6) into its literal cyclic core order."""
    d_terminal, n, paths = scaffold(m)
    order: list[int] = []
    for j, k in enumerate(fixed_map(m)):
        next_j = (j + 1) % (2 * m + 1)
        order.extend((d_terminal + j, 4 * m + 2 - 2 * j))
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
    return sum(labels[index - 1] * labels[index] for index in range(len(labels)))


def formula_value(m: int) -> int:
    """Return the proposed exact induced-K formula."""
    q = closing_index(m)
    numerator = (
        1714 * m**3 + 3891 * m**2 + 24 * m * q + 2921 * m + 12 * q**2 + 48 * q + 732
    )
    assert numerator % 6 == 0
    return numerator // 6


def residue_two_value(m: int) -> int:
    """Return (KR2-25), the known residue-two score at ``k = 2*m + 1``."""
    numerator = 572 * m**3 + 1307 * m**2 + 997 * m + 254
    assert numerator % 2 == 0
    return numerator // 2


def k825_value(m: int) -> int:
    """Return canonical K825 on the same ``n = 10*m + 7`` row."""
    explicit = {1: 1609, 2: 6204}
    if m in explicit:
        return explicit[m]
    numerator = 572 * m**3 + 1349 * m**2 + 1119 * m + 324
    assert numerator % 2 == 0
    return numerator // 2 - 25 * int(m == 3)


def reconstruct_path(
    start: int, end: int, predecessors: list[int | None]
) -> tuple[int, ...]:
    """Reconstruct one maximizing increasing-position path."""
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
    """Maximize the induced objective by DP, without enumerating subsets."""
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


def expected_hole_gain(m: int, label: int) -> int:
    """Return the seven-class symbolic cancellation gain for one hole."""
    q = closing_index(m)
    if label % 2 == 0:
        j = (4 * m + 2 - label) // 2
        if j == 2 * m:
            return 80 * m**2 - 20 * m * q + 80 * m - 10 * q + 16
        if j < q:
            return -4 * j**2 + (28 * m + 20) * j + 20 * m + 16
        if j < m:
            return -4 * j**2 + (28 * m + 14) * j + 12 * m + 6
        return -(j**2) + (29 * m + 19) * j - 4 * m**2 + 7 * m + 6

    j = (4 * m + 1 - label) // 2
    if j < q:
        return -4 * j**2 + (28 * m + 16) * j + 36 * m + 27
    if j < m:
        return -4 * j**2 + (28 * m + 10) * j + 28 * m + 13
    return -(j**2) + (29 * m + 20) * j - 4 * m**2 + 25 * m + 20


def compressed_arc(
    order: tuple[int, ...], start: int, steps: int, backbone: set[int]
) -> tuple[int, ...]:
    """Materialize an oriented arc after deleting only its internal holes."""
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
) -> tuple[int, int, int, tuple[int, ...], int, int, int]:
    """Check every cancellation gain and every proper oriented arc exactly."""
    size = len(order)
    low_end = 4 * m + 2
    backbone = set(range(low_end + 1, 10 * m + 8))

    hole_gain: dict[int, int] = {}
    hole_records: list[tuple[int, int, tuple[int, int]]] = []
    for index, label in enumerate(order):
        if label <= low_end:
            left = order[(index - 1) % size]
            right = order[(index + 1) % size]
            assert left in backbone and right in backbone
            gain = left * right - label * (left + right)
            assert gain == expected_hole_gain(m, label)
            assert gain > 0
            hole_gain[label] = gain
            hole_records.append((gain, label, (left, right)))
    assert len(hole_gain) == 4 * m + 1
    minimum_hole = min(gain for gain, _label, _edge in hole_records)
    hole_winners = [record for record in hole_records if record[0] == minimum_hole]
    expected_hole = (20 * m + 16, 4 * m + 2, (8 * m + 7, 8 * m + 6))
    assert hole_winners == [expected_hole]

    minimum_shortcut: int | None = None
    shortcut_witness: tuple[int, ...] = ()
    shortcut_winners = 0
    proper_arcs = 0
    shortcut_arcs = 0

    for start in range(size):
        start_label = order[start]
        previous = start_label
        raw_sum = 0
        internal_budget = 0
        last_kept = start_label
        retained_edge_sum = 0
        retained_edges = 0

        for steps in range(1, size):
            end = order[(start + steps) % size]
            raw_sum += previous * end
            if steps >= 2 and previous in hole_gain:
                internal_budget += hole_gain[previous]

            compressed_sum = retained_edge_sum + last_kept * end
            compressed_edges = retained_edges + 1
            proper_arcs += 1

            assert raw_sum + internal_budget == compressed_sum
            shortcut_gain = start_label * end - raw_sum
            assert shortcut_gain <= internal_budget

            if compressed_edges >= 2:
                margin = compressed_sum - start_label * end
                assert margin > 0
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
            previous = end

    assert minimum_shortcut is not None
    if m == 1:
        expected_margin = 17
        expected_witness = (11, 7, 15)
    elif m == 2:
        expected_margin = 49
        expected_witness = (17, 11, 23)
    else:
        expected_margin = 20 * m + 14
        expected_witness = (8 * m + 6, 4 * m + 4, 8 * m + 5)
    assert minimum_shortcut == expected_margin
    assert shortcut_winners == 1
    assert shortcut_witness == expected_witness
    return (
        minimum_hole,
        minimum_shortcut,
        shortcut_winners,
        shortcut_witness,
        len(hole_gain),
        proper_arcs,
        shortcut_arcs,
    )


def check_formula_row(m: int) -> int:
    """Check the literal order, formula branches, boundaries, and comparators."""
    d_terminal, n, paths = scaffold(m)
    alpha = fixed_map(m)
    order = expanded_order(m)
    q = closing_index(m)
    backbone_word = tuple(label for label in order if label >= 4 * m + 3)

    assert 1 <= q <= m
    assert (q == m) == (m <= 3)
    assert alpha[2 * m] == q
    assert cyclic_score(backbone_word) == formula_value(m)
    assert formula_value(m) < residue_two_value(m) < k825_value(m)

    residuals = (0, 1, 2, 3, -1)
    c_residual = 5 * q - 4 * m
    assert c_residual == residuals[m % 5]
    residue_numerator = (
        42850 * m**3
        + 97947 * m**2
        + (73985 + 216 * c_residual) * m
        + 12 * c_residual**2
        + 240 * c_residual
        + 18300
    )
    assert residue_numerator == 150 * formula_value(m)

    assert (tuple(range(q, m)) == ()) == (m <= 3)
    assert len(tuple(range(m, 2 * m))) == m
    assert tuple(alpha[j] for j in range(m, 2 * m)) == tuple(range(2 * m, m, -1))
    assert all(len(path) != 2 for path in paths)

    closing_word = (n, 2, *paths[q], 4 * m + 3, d_terminal)
    closing_length = len(paths[q]) + 3
    assert order[-closing_length:] + (order[0],) == closing_word

    if m == 1:
        assert alpha == (0, 2, 1)
        assert order == (15, 6, 14, 8, 13, 5, 16, 4, 10, 3, 17, 2, 12, 9, 11, 7)
        assert (formula_value(m), residue_two_value(m), k825_value(m)) == (
            1557,
            1565,
            1609,
        )
    elif m == 2:
        assert alpha == (0, 1, 4, 3, 2)
        assert order == (
            23,
            10,
            22,
            12,
            21,
            9,
            24,
            8,
            20,
            13,
            19,
            7,
            25,
            6,
            16,
            5,
            26,
            4,
            15,
            3,
            27,
            2,
            18,
            14,
            17,
            11,
        )
        assert (formula_value(m), residue_two_value(m), k825_value(m)) == (
            6015,
            6026,
            6204,
        )
    elif m == 3:
        assert alpha == (0, 1, 2, 6, 5, 4, 3)
        assert order == (
            31,
            14,
            30,
            16,
            29,
            13,
            32,
            12,
            28,
            17,
            27,
            11,
            33,
            10,
            26,
            18,
            25,
            9,
            34,
            8,
            22,
            7,
            35,
            6,
            21,
            5,
            36,
            4,
            20,
            3,
            37,
            2,
            24,
            19,
            23,
            15,
        )
        assert (formula_value(m), residue_two_value(m), k825_value(m)) == (
            15210,
            15226,
            15608,
        )

    assert d_terminal == 8 * m + 7 and n == 10 * m + 7
    return len(order)


def main() -> None:
    """Run the declared bounded exact checks."""
    formula_entries = sum(check_formula_row(m) for m in range(1, FORMULA_MAX_M + 1))

    transitions = 0
    deletion_gains = 0
    proper_arcs = 0
    shortcut_arcs = 0
    for m in range(1, DP_MAX_M + 1):
        order = expanded_order(m)
        score, count, indices, row_transitions = max_plus_oracle(order)
        winner = tuple(order[index] for index in indices)
        assert score == formula_value(m)
        assert count == 1
        assert set(winner) == set(range(4 * m + 3, 10 * m + 8))
        assert row_transitions == comb(len(order) + 1, 3)
        transitions += row_transitions

        (
            _minimum_hole,
            _minimum_shortcut,
            _shortcut_winners,
            _shortcut_witness,
            row_deletion_gains,
            row_proper_arcs,
            row_shortcut_arcs,
        ) = all_arcs_audit(m, order)
        deletion_gains += row_deletion_gains
        proper_arcs += row_proper_arcs
        shortcut_arcs += row_shortcut_arcs

    assert formula_entries == 5_011_000
    assert transitions == 38_957_975
    assert deletion_gains == 1_890
    assert proper_arcs == 997_550
    assert shortcut_arcs == 990_830
    print("odd-v residue-two PG49-star induced K diagnostic: PASS")
    print(f"formula/residual rows: {FORMULA_MAX_M} (m=1..{FORMULA_MAX_M})")
    print(f"literal core entries checked: {formula_entries}")
    print(f"max-plus rows: {DP_MAX_M} (m=1..{DP_MAX_M})")
    print(f"max-plus transitions: {transitions}")
    print(f"cancellation gains checked: {deletion_gains}")
    print(f"proper oriented arcs checked: {proper_arcs}")
    print(f"nontrivial compressed shortcuts checked: {shortcut_arcs}")
    print("unique backbone, m=1,2,3, residuals, closure, and comparisons verified")


if __name__ == "__main__":
    main()
