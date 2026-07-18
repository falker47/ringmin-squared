"""Bounded exact checks for the canonical 8/25 core-order K theorem.

This dossier-local script is deliberately independent of production imports.
It reconstructs the search-free block order, uses a max-plus dynamic program
over increasing paths (not subset or permutation enumeration), and checks the
local shortcut-budget certificate for ``9 <= n <= 120``. A lighter direct
score/formula comparison continues through ``n = 1000``.
"""

from __future__ import annotations

from dataclasses import dataclass


MAX_N = 120
FORMULA_MAX_N = 1000


EXCEPTIONAL_ORDERS = {
    9: (9, 2, 8, 4, 6, 5, 7, 3),
    10: (10, 2, 9, 4, 7, 6, 5, 8, 3),
    11: (11, 2, 10, 4, 8, 6, 7, 5, 9, 3),
    12: (12, 2, 11, 4, 9, 6, 7, 8, 5, 10, 3),
    14: (14, 3, 11, 2, 13, 4, 12, 6, 9, 8, 7, 10, 5),
    15: (15, 3, 12, 2, 14, 4, 13, 6, 10, 8, 9, 7, 11, 5),
    16: (16, 2, 13, 4, 15, 6, 11, 8, 9, 10, 7, 14, 5, 12, 3),
    17: (17, 5, 14, 3, 13, 2, 16, 4, 15, 6, 12, 8, 10, 9, 11, 7),
    20: (20, 2, 13, 10, 11, 12, 9, 17, 7, 16, 5, 18, 3, 15, 8, 19, 4, 14, 6),
    21: (21, 6, 15, 4, 20, 2, 16, 3, 19, 5, 17, 7, 18, 9, 13, 11, 12, 10, 14, 8),
    22: (22, 2, 16, 4, 19, 6, 20, 8, 15, 10, 13, 12, 11, 14, 9, 21, 7, 18, 5, 17, 3),
    26: (
        26,
        2,
        18,
        4,
        23,
        11,
        21,
        8,
        24,
        10,
        17,
        12,
        15,
        14,
        13,
        16,
        6,
        25,
        9,
        20,
        7,
        22,
        5,
        19,
        3,
    ),
    27: (
        27,
        2,
        18,
        4,
        24,
        6,
        22,
        8,
        20,
        10,
        23,
        12,
        16,
        14,
        15,
        13,
        17,
        11,
        25,
        9,
        21,
        7,
        26,
        5,
        19,
        3,
    ),
    32: (
        32,
        2,
        22,
        4,
        29,
        6,
        26,
        13,
        25,
        10,
        30,
        12,
        21,
        14,
        19,
        16,
        17,
        18,
        15,
        20,
        8,
        31,
        11,
        24,
        9,
        27,
        7,
        28,
        5,
        23,
        3,
    ),
}


EXCEPTIONAL_RESULTS = {
    9: (4, 256, 8, 15),
    10: (4, 346, 1, 26),
    11: (5, 459, 17, 8),
    12: (5, 593, 10, 19),
    14: (6, 917, 18, 20),
    15: (6, 1125, 8, 35),
    16: (7, 1346, 28, 9),
    17: (7, 1609, 9, 18),
    20: (9, 2554, 57, 13),
    21: (9, 2976, 45, 14),
    22: (9, 3431, 21, 20),
    26: (10, 5516, 1, 95),
    27: (11, 6204, 37, 30),
    32: (13, 10299, 13, 18),
}


BOUNDARY_RESULTS = {
    13: (724, 4, 40),
    18: (1851, 13, 54),
    19: (2186, 8, 74),
    24: (4309, 10, 92),
    25: (4898, 16, 10),
    30: (8333, 31, 12),
    31: (9248, 25, 38),
    36: (14311, 43, 44),
    37: (15608, 36, 76),
    42: (22613, 49, 86),
}


@dataclass(frozen=True)
class Parameters:
    d: int
    v: int
    e: int
    t: int
    epsilon: int
    r: int


def parameters(n: int) -> Parameters:
    d = (4 * n + 12) // 5
    v = n - d + 1
    e = d - 4 * v
    t, epsilon = divmod(v + e - 2, 2)
    return Parameters(d=d, v=v, e=e, t=t, epsilon=epsilon, r=v - t - epsilon)


def build_order(n: int) -> tuple[int, ...]:
    exceptional = EXCEPTIONAL_ORDERS.get(n)
    if exceptional is not None:
        return exceptional

    p = parameters(n)
    assert 4 <= p.e <= 8 and p.v >= p.e - 2
    paths: list[tuple[int, ...]] = [
        (p.d - 1 - 2 * j, 2 * p.v + 2 + j, p.d - 2 - 2 * j) for j in range(p.t)
    ]
    remaining = list(range(2 * p.v + p.t + 2, p.d - 2 * p.t))
    if p.epsilon:
        paths.append(tuple(remaining[:2]))
        remaining = remaining[2:]
    paths.extend((x,) for x in remaining)
    assert len(paths) == p.v

    order: list[int] = []
    for j, path in enumerate(paths):
        order.extend(
            (p.d + j, 2 * p.v - 2 * j, *path, 2 * p.v + 1 - 2 * ((j + 1) % p.v))
        )
    result = tuple(order)
    assert len(result) == n - 1 and set(result) == set(range(2, n + 1))
    return result


def candidate(n: int) -> frozenset[int]:
    exceptional = EXCEPTIONAL_RESULTS.get(n)
    if exceptional is not None:
        return frozenset(range(exceptional[0], n + 1))
    p = parameters(n)
    result = set(range(2 * p.v + 1, n + 1))
    if p.e >= 6:
        result.remove(2 * p.v + 2)
    return frozenset(result)


def cycle_score(order: tuple[int, ...], selected: frozenset[int]) -> int:
    induced = [x for x in order if x in selected]
    assert induced
    if len(induced) == 1:
        return induced[0] ** 2
    return sum(a * b for a, b in zip(induced, induced[1:] + induced[:1], strict=True))


def symbolic_formula(n: int) -> int:
    p = parameters(n)
    assert 4 <= p.e <= 8 and p.v >= p.e - 2
    e, v, epsilon = p.e, p.v, p.epsilon
    numerator = (
        286 * v**3
        + (180 * e - 91 + 10 * epsilon) * v**2
        + (38 * e**2 - 34 * e - 2 - 8 * (e + 2) * epsilon) * v
        + e * (8 * e**2 - 9 * e - 2) // 3
        + (-2 * e**2 - 10 * e + 21) * epsilon
    )
    assert numerator % 8 == 0
    boundary = (4 * e - 7) if v == e - 2 else 0
    extra_hole = max(0, (4 * e - 22) * v + e**2 - 7 * e + 8)
    return numerator // 8 - boundary + extra_hole


def max_plus_k(order: tuple[int, ...]) -> tuple[int, int, frozenset[int], int]:
    """Return exact K, optimizer count, one witness, and DP transition count."""
    size = len(order)
    optimum = -1
    optimum_count = 0
    optimum_witness: tuple[int, ...] = ()
    transitions = 0

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
                path = witness[previous] + (order[end],)
                if value > best[end]:
                    best[end], count[end], witness[end] = value, count[previous], path
                elif value == best[end]:
                    count[end] += count[previous]
                    if path < witness[end]:
                        witness[end] = path
            closed = best[end] + order[end] * order[start]
            if closed > optimum:
                optimum, optimum_count = closed, count[end]
                optimum_witness = witness[end]
            elif closed == optimum:
                optimum_count += count[end]
                if witness[end] < optimum_witness:
                    optimum_witness = witness[end]

    return optimum, optimum_count, frozenset(optimum_witness), transitions


def shortcut_certificate(
    order: tuple[int, ...], selected: frozenset[int]
) -> tuple[int, int, int, int]:
    """Check the exact isolated-hole budget and all compressed arc margins."""
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

    full_score = cycle_score(order, frozenset(order))
    selected_score = cycle_score(order, selected)
    assert selected_score == full_score + sum(hole_gain.values())

    min_margin: int | None = None
    min_four_edge_margin: int | None = None
    checked_arcs = 0
    for start in range(size):
        arc = [order[start]]
        for step in range(1, size):
            arc.append(order[(start + step) % size])
            checked_arcs += 1
            internal_holes = [x for x in arc[1:-1] if x in holes]
            compressed = [arc[0], *(x for x in arc[1:-1] if x in selected), arc[-1]]
            original_sum = sum(a * b for a, b in zip(arc, arc[1:]))
            compressed_sum = sum(a * b for a, b in zip(compressed, compressed[1:]))
            budget = sum(hole_gain[x] for x in internal_holes)
            assert original_sum + budget == compressed_sum
            shortcut_gain = arc[0] * arc[-1] - original_sum
            assert shortcut_gain <= budget
            if len(compressed) >= 3:
                margin = compressed_sum - arc[0] * arc[-1]
                assert margin > 0
                assert shortcut_gain < budget
                min_margin = margin if min_margin is None else min(min_margin, margin)
                if len(compressed) == 5:
                    min_four_edge_margin = (
                        margin
                        if min_four_edge_margin is None
                        else min(min_four_edge_margin, margin)
                    )

    assert min_margin is not None and min_four_edge_margin is not None and hole_gain
    return min_margin, min(hole_gain.values()), checked_arcs, min_four_edge_margin


def main() -> None:
    symbolic_rows = 0
    dp_transitions = 0
    shortcut_arcs = 0

    for n in range(9, MAX_N + 1):
        order = build_order(n)
        selected = candidate(n)
        score = cycle_score(order, selected)
        if n in EXCEPTIONAL_RESULTS:
            _, expected_score, expected_margin, expected_hole = EXCEPTIONAL_RESULTS[n]
        else:
            symbolic_rows += 1
            expected_score = symbolic_formula(n)
            expected_margin = expected_hole = None
        assert score == expected_score
        assert {n - 1, n} <= selected and score > n**2

        optimum, count, witness, transitions = max_plus_k(order)
        dp_transitions += transitions
        assert (optimum, count, witness) == (score, 1, selected)

        min_margin, min_hole, arcs, min_four_edge_margin = shortcut_certificate(
            order, selected
        )
        shortcut_arcs += arcs
        if expected_margin is not None:
            assert (min_margin, min_hole) == (expected_margin, expected_hole)
        if n in BOUNDARY_RESULTS:
            boundary_score, boundary_margin, boundary_hole = BOUNDARY_RESULTS[n]
            assert (score, min_margin, min_hole) == (
                boundary_score,
                boundary_margin,
                boundary_hole,
            )
        if n == 47:
            assert (min_margin, min_hole, min_four_edge_margin) == (55, 96, 1446)

    for n in range(MAX_N + 1, FORMULA_MAX_N + 1):
        order = build_order(n)
        selected = candidate(n)
        assert cycle_score(order, selected) == symbolic_formula(n)

    print("canonical 8/25 K diagnostic: PASS")
    print(f"rows: {MAX_N - 8} (n=9..{MAX_N})")
    print(f"symbolic rows: {symbolic_rows}; explicit rows: {len(EXCEPTIONAL_RESULTS)}")
    print(f"max-plus transitions: {dp_transitions}")
    print(f"oriented shortcut arcs: {shortcut_arcs}")
    print(f"shortcut-certificate rows: {MAX_N - 8}")
    print("hard-coded shortcut anchor rows: 25")
    print(f"formula-only tail rows: {FORMULA_MAX_N - MAX_N}")
    print("leading coefficient: 143/500")


if __name__ == "__main__":
    main()
