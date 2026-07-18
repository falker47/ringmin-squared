"""Independent exact checks for the preclosing PG46 core-order K theorem.

This standalone standard-library diagnostic imports no project helper.  It
reconstructs only the PG46 order placing P_m in G_{2m-2}, scores the claimed
tail, checks one max-plus increasing-path DP, and audits every oriented
compressed arc.  It enumerates no subset, permutation, or matching.
"""

from __future__ import annotations

from fractions import Fraction


MAX_DP_M = 30
FORMULA_MAX_M = 1000


def path(m: int, k: int) -> tuple[int, ...]:
    """Return the retained oriented scaffold path P_k."""
    d = 8 * m + 4
    assert 0 <= k < 2 * m
    if k <= m:
        return d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k
    return (4 * m + 2 + k,)


def preclosing_pg46_order(m: int) -> tuple[int, ...]:
    """Expand the PG46 shift that places P_m in G_{2m-2}."""
    assert m >= 3
    n = 10 * m + 3
    d = 8 * m + 4
    v = 2 * m
    alpha = (*range(m), *range(m + 1, v - 1), m, v - 1)
    assert len(alpha) == v and sorted(alpha) == list(range(v))

    order: list[int] = []
    for j, k in enumerate(alpha):
        order.extend((d + j, 4 * m - 2 * j))
        order.extend(path(m, k))
        order.append(4 * m + 1 - 2 * ((j + 1) % v))
    result = tuple(order)
    assert len(result) == n - 1
    assert sorted(result) == list(range(2, n + 1))
    return result


def candidate(m: int) -> frozenset[int]:
    """Return the claimed unique maximizing label set."""
    return frozenset(range(4 * m + 1, 10 * m + 4))


def cycle_score(order: tuple[int, ...], selected: frozenset[int]) -> int:
    """Score one nonempty induced cyclic order, including singleton loops."""
    induced = [label for label in order if label in selected]
    assert induced
    if len(induced) == 1:
        return induced[0] ** 2
    return sum(
        left * right
        for left, right in zip(induced, induced[1:] + induced[:1], strict=True)
    )


def preclosing_formula(m: int) -> int:
    """Exact symbolic score of the preclosing PG46 order."""
    numerator = 572 * m**3 + 631 * m**2 + 235 * m + 22
    assert numerator % 2 == 0
    return numerator // 2


def closing_formula(m: int) -> int:
    """Previously proved closing-PG46 score on the same row."""
    numerator = 572 * m**3 + 631 * m**2 + 223 * m + 22
    assert numerator % 2 == 0
    return numerator // 2


def k825_formula(m: int) -> int:
    """Canonical K825 score on the same n=10m+3 row."""
    numerator = 572 * m**3 + 629 * m**2 + 235 * m + 30
    assert numerator % 2 == 0
    return numerator // 2


def max_plus_k(order: tuple[int, ...]) -> tuple[int, int, frozenset[int], int]:
    """Return exact K, optimizer count, one witness, and transition count."""
    size = len(order)
    optimum = -1
    optimum_count = 0
    optimum_witness: tuple[int, ...] = ()
    transitions = 0

    # Every subset has a unique least selected position.  Fixing that start
    # converts its cyclic induced order into one increasing path in the index
    # DAG, so the recurrence counts optimizers without subset enumeration.
    for start in range(size):
        best = [-1] * size
        count = [0] * size
        witness: list[tuple[int, ...]] = [() for _ in range(size)]
        best[start] = 0
        count[start] = 1
        witness[start] = (order[start],)

        singleton = order[start] ** 2
        if singleton > optimum:
            optimum, optimum_count = singleton, 1
            optimum_witness = witness[start]
        elif singleton == optimum:
            optimum_count += 1

        for end in range(start + 1, size):
            for previous in range(start, end):
                transitions += 1
                value = best[previous] + order[previous] * order[end]
                candidate_path = witness[previous] + (order[end],)
                if value > best[end]:
                    best[end] = value
                    count[end] = count[previous]
                    witness[end] = candidate_path
                elif value == best[end]:
                    count[end] += count[previous]
                    if candidate_path < witness[end]:
                        witness[end] = candidate_path

            closed = best[end] + order[end] * order[start]
            if closed > optimum:
                optimum = closed
                optimum_count = count[end]
                optimum_witness = witness[end]
            elif closed == optimum:
                optimum_count += count[end]
                if witness[end] < optimum_witness:
                    optimum_witness = witness[end]

    return optimum, optimum_count, frozenset(optimum_witness), transitions


def shortcut_certificate(
    order: tuple[int, ...], selected: frozenset[int]
) -> tuple[int, int, int]:
    """Check all isolated-hole gains and all oriented compressed arcs."""
    size = len(order)
    holes = set(order) - selected
    hole_gain: dict[int, int] = {}
    for index, hole in enumerate(order):
        if hole not in holes:
            continue
        left = order[(index - 1) % size]
        right = order[(index + 1) % size]
        assert left in selected and right in selected
        gain = left * right - hole * (left + right)
        assert gain > 0
        hole_gain[hole] = gain

    assert set(hole_gain) == holes
    full_score = cycle_score(order, frozenset(order))
    selected_score = cycle_score(order, selected)
    assert selected_score == full_score + sum(hole_gain.values())

    min_margin: int | None = None
    checked_arcs = 0
    for start in range(size):
        first = order[start]
        kept = [first]
        original_sum = 0
        compressed_sum = 0
        budget = 0

        for step in range(1, size):
            previous = order[(start + step - 1) % size]
            current = order[(start + step) % size]
            original_sum += previous * current

            # Once the previous endpoint becomes internal, delete it exactly
            # when it is a hole and credit its local deletion gain.
            if step > 1 and previous in holes:
                assert kept[-1] == previous
                compressed_sum -= kept[-2] * kept[-1]
                kept.pop()
                budget += hole_gain[previous]

            compressed_sum += kept[-1] * current
            kept.append(current)
            assert original_sum + budget == compressed_sum
            checked_arcs += 1

            if len(kept) >= 3:
                margin = compressed_sum - first * current
                assert margin > 0
                min_margin = margin if min_margin is None else min(min_margin, margin)

    assert min_margin is not None and hole_gain
    return min_margin, min(hole_gain.values()), checked_arcs


def main() -> None:
    """Run bounded independent DP, shortcut, and formula checks."""
    expected_m3_order = (
        28,
        12,
        27,
        14,
        26,
        11,
        29,
        10,
        25,
        15,
        24,
        9,
        30,
        8,
        23,
        16,
        22,
        7,
        31,
        6,
        18,
        5,
        32,
        4,
        21,
        17,
        20,
        3,
        33,
        2,
        19,
        13,
    )
    expected_initial_scores = (
        10925,
        23833,
        44236,
        73850,
        114391,
        167575,
        235118,
        318736,
    )
    assert preclosing_pg46_order(3) == expected_m3_order

    dp_transitions = 0
    shortcut_arcs = 0
    observed_initial_scores: list[int] = []
    for m in range(3, MAX_DP_M + 1):
        order = preclosing_pg46_order(m)
        selected = candidate(m)
        score = cycle_score(order, selected)
        assert score == preclosing_formula(m)
        assert score - closing_formula(m) == 6 * m
        assert score - k825_formula(m) == m**2 - 4
        assert score > closing_formula(m)
        assert score > k825_formula(m)
        assert score > (10 * m + 3) ** 2

        optimum, count, witness, transitions = max_plus_k(order)
        dp_transitions += transitions
        assert (optimum, count, witness) == (score, 1, selected)

        min_margin, min_hole, arcs = shortcut_certificate(order, selected)
        shortcut_arcs += arcs
        assert min_margin == 12 * m + 4
        assert min_hole == 28 * m + 12

        if m <= 10:
            observed_initial_scores.append(score)

    assert tuple(observed_initial_scores) == expected_initial_scores

    for m in range(MAX_DP_M + 1, FORMULA_MAX_M + 1):
        order = preclosing_pg46_order(m)
        selected = candidate(m)
        score = cycle_score(order, selected)
        assert score == preclosing_formula(m)
        assert score - closing_formula(m) == 6 * m
        assert score - k825_formula(m) == m**2 - 4

    assert Fraction(572, 2 * 10**3) == Fraction(143, 500)
    assert preclosing_formula(3) == 10925
    assert closing_formula(3) == 10907
    assert k825_formula(3) == 10920

    print("preclosing PG46 K diagnostic: PASS")
    print(f"max-plus/shortcut rows: {MAX_DP_M - 2} (m=3..{MAX_DP_M})")
    print(f"max-plus transitions: {dp_transitions}")
    print(f"oriented shortcut arcs: {shortcut_arcs}")
    print(f"formula rows: {FORMULA_MAX_M - 2} (m=3..{FORMULA_MAX_M})")
    print("minimum row: m=3, K=10925, closing=10907, K825=10920")
    print("pointwise comparison: strictly worse than both comparators for m>=3")
    print("leading coefficient: unchanged at 143/500")


if __name__ == "__main__":
    main()
