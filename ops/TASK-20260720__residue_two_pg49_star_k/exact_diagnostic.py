"""Bounded exact checks for induced K on the fixed map (PGE2-6).

This standalone standard-library diagnostic constructs only the prescribed
even-v residue-two PG49-star core on ``n = 10*m + 2``.  It imports no project
helper and searches no order, matching, path permutation, or subset.  A
least-selected-position max-plus recurrence checks the induced-subset maximum,
while a separate scan audits every proper oriented arc and the exact shortcut
identity.  All finite limits are explicit below.
"""

from math import comb


DP_MAX_M = 30
FORMULA_MAX_M = 1000


def ceiling_div(numerator: int, denominator: int) -> int:
    """Return the exact ceiling of a nonnegative rational number."""
    return (numerator + denominator - 1) // denominator


def closing_index(m: int) -> int:
    """Return the literal threshold ``q = kappa_(2*m-1)``."""
    return ceiling_div((m - 1) * (4 * m + 1), 5 * m + 1)


def scaffold(m: int) -> tuple[int, int, tuple[tuple[int, ...], ...]]:
    """Return ``D, n, paths`` for the even-v residue-two scaffold."""
    if m < 1:
        raise ValueError("the symbolic branch requires m >= 1")
    d_terminal = 8 * m + 3
    n = 10 * m + 2
    paths: list[tuple[int, ...]] = [
        (
            d_terminal - 1 - 2 * k,
            4 * m + 2 + k,
            d_terminal - 2 - 2 * k,
        )
        for k in range(m)
    ]
    paths.append((5 * m + 2, 5 * m + 3))
    paths.extend((4 * m + 3 + k,) for k in range(m + 1, 2 * m))
    result = tuple(paths)
    assert len(result) == 2 * m
    assert sorted(label for path in result for label in path) == list(
        range(4 * m + 2, d_terminal)
    )
    return d_terminal, n, result


def fixed_map(m: int) -> tuple[int, ...]:
    """Return only the prescribed path-to-gap map (PGE2-6)."""
    q = closing_index(m)
    alpha = tuple(
        j if j < q else j + 1 if j <= m - 1 else 3 * m - 1 - j if j <= 2 * m - 2 else q
        for j in range(2 * m)
    )
    assert set(alpha) == set(range(2 * m))
    return alpha


def expanded_order(m: int) -> tuple[int, ...]:
    """Expand only (PGE2-6) into its literal cyclic core order."""
    d_terminal, n, paths = scaffold(m)
    order: list[int] = []
    for j, k in enumerate(fixed_map(m)):
        next_j = (j + 1) % (2 * m)
        order.extend((d_terminal + j, 4 * m - 2 * j))
        order.extend(paths[k])
        order.append(4 * m + 1 - 2 * next_j)
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
        1714 * m**3 + 1353 * m**2 + 24 * m * q + 281 * m + 12 * q**2 + 36 * q + 30
    )
    assert numerator % 6 == 0
    return numerator // 6


def residue_two_value(m: int) -> int:
    """Return (KR2-22), namely the known residue-two score at k=2*m."""
    numerator = 572 * m**3 + 459 * m**2 + 99 * m + 4
    assert numerator % 2 == 0
    return numerator // 2


def k825_value(m: int) -> int:
    """Return canonical K825 on the same n=10*m+2 row."""
    explicit = {1: 593, 2: 3431, 3: 10299}
    if m in explicit:
        return explicit[m]
    numerator = 572 * m**3 + 501 * m**2 + 149 * m + 6
    assert numerator % 2 == 0
    return numerator // 2


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
    """Maximize over induced subsets by DP, without enumerating them."""
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
    """Check every deletion gain and every proper oriented arc exactly."""
    size = len(order)
    low_end = 4 * m
    backbone = set(range(low_end + 1, 10 * m + 3))

    hole_gain: dict[int, int] = {}
    hole_records: list[tuple[int, int, tuple[int, int]]] = []
    for index, label in enumerate(order):
        if label <= low_end:
            left = order[(index - 1) % size]
            right = order[(index + 1) % size]
            assert left in backbone and right in backbone
            gain = left * right - label * (left + right)
            assert gain > 0
            hole_gain[label] = gain
            hole_records.append((gain, label, (left, right)))
    assert len(hole_gain) == 4 * m - 1
    minimum_hole = min(gain for gain, _label, _edge in hole_records)
    hole_winners = [record for record in hole_records if record[0] == minimum_hole]
    if m == 1:
        expected_hole = (5, 4, (11, 7))
    else:
        expected_hole = (20 * m + 6, 4 * m, (8 * m + 3, 8 * m + 2))
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
        expected_margin = 1
        expected_witness = (9, 5, 11)
    elif m == 2:
        expected_margin = 21
        expected_witness = (15, 9, 19)
    elif m == 3:
        expected_margin = 57
        expected_witness = (21, 13, 27)
    else:
        expected_margin = 20 * m + 4
        expected_witness = (8 * m + 2, 4 * m + 2, 8 * m + 1)
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
    backbone_word = tuple(label for label in order if label >= 4 * m + 1)

    assert alpha[2 * m - 1] == q
    assert paths[m] == (5 * m + 2, 5 * m + 3)
    assert cyclic_score(backbone_word) == formula_value(m)
    assert formula_value(m) < residue_two_value(m) < k825_value(m)

    if m == 1:
        assert q == 0
        expected_c = -4
    else:
        assert q == (4 * m + 1) // 5
        expected_c = (0, 1, -3, -2, -1)[m % 5]
    c_residual = 5 * q - 4 * m
    assert c_residual == expected_c
    residue_numerator = (
        42850 * m**3
        + 34497 * m**2
        + (7745 + 216 * c_residual) * m
        + 12 * c_residual**2
        + 180 * c_residual
        + 750
    )
    assert residue_numerator == 150 * formula_value(m)

    if m == 1:
        assert alpha == (1, 0)
        assert order == (11, 4, 7, 8, 3, 12, 2, 10, 6, 9, 5)
        assert formula_value(m) == 563
    elif m == 2:
        assert alpha == (0, 2, 3, 1)
        assert order == (
            19,
            8,
            18,
            10,
            17,
            7,
            20,
            6,
            12,
            13,
            5,
            21,
            4,
            14,
            3,
            22,
            2,
            16,
            11,
            15,
            9,
        )
        assert formula_value(m) == 3302

    assert d_terminal == 8 * m + 3 and n == 10 * m + 2
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
        assert set(winner) == set(range(4 * m + 1, 10 * m + 3))
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

    assert formula_entries == 5_006_000
    assert transitions == 36_511_800
    assert deletion_gains == 1_830
    assert proper_arcs == 950_150
    assert shortcut_arcs == 943_640
    print("even-v residue-two PG49-star induced K diagnostic: PASS")
    print(f"formula/residual rows: {FORMULA_MAX_M} (m=1..{FORMULA_MAX_M})")
    print(f"literal core entries checked: {formula_entries}")
    print(f"max-plus rows: {DP_MAX_M} (m=1..{DP_MAX_M})")
    print(f"max-plus transitions: {transitions}")
    print(f"deletion gains checked: {deletion_gains}")
    print(f"proper oriented arcs checked: {proper_arcs}")
    print(f"nontrivial compressed shortcuts checked: {shortcut_arcs}")
    print("unique backbone, boundary branches, and both comparisons verified")


if __name__ == "__main__":
    main()
