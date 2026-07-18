"""Bounded exact checks for the residue-one core-order K theorem.

This dossier-local script imports only the Python standard library and no
project or test helper.  It reconstructs both fixed block words, uses an
increasing-path max-plus dynamic program rather than subset enumeration, and
audits every oriented shortcut budget for the residue-one order on
``2 <= k <= 30``.  Direct block-score and formula checks continue through
``k = 1000``.  No cyclic-order permutation is generated or searched.
"""

from __future__ import annotations

from dataclasses import dataclass


MAX_K = 30
FORMULA_MAX_K = 1000


CANONICAL_EXPLICIT_ORDERS = {
    2: (11, 2, 10, 4, 8, 6, 7, 5, 9, 3),
    3: (16, 2, 13, 4, 15, 6, 11, 8, 9, 10, 7, 14, 5, 12, 3),
    4: (21, 6, 15, 4, 20, 2, 16, 3, 19, 5, 17, 7, 18, 9, 13, 11, 12, 10, 14, 8),
    5: (
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
}


CANONICAL_EXPLICIT_RESULTS = {
    2: (frozenset(range(5, 12)), 459),
    3: (frozenset(range(7, 17)), 1346),
    4: (frozenset(range(9, 22)), 2976),
    5: (frozenset(range(10, 27)), 5516),
}


@dataclass(frozen=True)
class DpResult:
    value: int
    count: int
    witness: frozenset[int]
    transitions: int


def residue_one_order(k: int) -> tuple[int, ...]:
    n = 5 * k + 1
    d = 4 * k + 2
    t, epsilon = divmod(k, 2)

    paths: list[tuple[int, ...]] = [(d - 1,)]
    paths.extend((d - 2 * j, 2 * k + 1 + j, d - 2 * j - 1) for j in range(1, t + 1))
    paths.extend((d - t - j - 1,) for j in range(t + 1, k - epsilon))
    if epsilon:
        paths.append((2 * k + t + 3, 2 * k + t + 2))
    assert len(paths) == k

    result: list[int] = []
    for j, path in enumerate(paths):
        result.extend(
            (
                d + j,
                2 * k - 2 * j,
                *path,
                2 * k + 1 - 2 * ((j + 1) % k),
            )
        )
    order = tuple(result)
    assert len(order) == n - 1 and set(order) == set(range(2, n + 1))
    return order


def residue_one_candidate(k: int) -> frozenset[int]:
    return frozenset(range(2 * k + 1, 5 * k + 2))


def residue_one_formula(k: int) -> int:
    epsilon = k % 2
    numerator = 857 * k**3 + 891 * k**2 + 214 * k + epsilon * (27 * k**2 - 51 * k - 18)
    assert numerator % 24 == 0
    return numerator // 24


def residue_one_n_formula(k: int) -> int:
    n = 5 * k + 1
    if k % 2 == 0:
        numerator = 857 * n**3 + 1884 * n**2 - 989 * n - 1752
    else:
        numerator = 857 * n**3 + 2019 * n**2 - 2534 * n - 2592
    assert numerator % 3000 == 0
    return numerator // 3000


def canonical_order(k: int) -> tuple[int, ...]:
    explicit = CANONICAL_EXPLICIT_ORDERS.get(k)
    if explicit is not None:
        return explicit

    n = 5 * k + 1
    v = k - 1
    e = 7
    d = 4 * v + e
    t, epsilon = divmod(v + e - 2, 2)
    assert d == 4 * k + 3 and v >= e - 2

    paths: list[tuple[int, ...]] = [
        (d - 1 - 2 * j, 2 * v + 2 + j, d - 2 - 2 * j) for j in range(t)
    ]
    remaining = list(range(2 * v + t + 2, d - 2 * t))
    if epsilon:
        paths.append(tuple(remaining[:2]))
        remaining = remaining[2:]
    paths.extend((x,) for x in remaining)
    assert len(paths) == v

    result: list[int] = []
    for j, path in enumerate(paths):
        result.extend((d + j, 2 * v - 2 * j, *path, 2 * v + 1 - 2 * ((j + 1) % v)))
    order = tuple(result)
    assert len(order) == n - 1 and set(order) == set(range(2, n + 1))
    return order


def canonical_candidate(k: int) -> frozenset[int]:
    explicit = CANONICAL_EXPLICIT_RESULTS.get(k)
    if explicit is not None:
        return explicit[0]
    result = set(range(2 * k - 1, 5 * k + 2))
    result.remove(2 * k)
    return frozenset(result)


def canonical_formula(k: int) -> int:
    explicit = CANONICAL_EXPLICIT_RESULTS.get(k)
    if explicit is not None:
        return explicit[1]
    epsilon = k % 2
    numerator = (
        858 * k**3
        + (933 + 30 * epsilon) * k**2
        + (570 - 276 * epsilon) * k
        + 120
        - 195 * epsilon
    )
    assert numerator % 24 == 0
    return numerator // 24 - (21 if k == 6 else 0)


def expected_gap(k: int) -> int:
    if k < 6:
        return canonical_formula(k) - residue_one_formula(k)
    epsilon = k % 2
    numerator = (
        k**3
        + (42 + 3 * epsilon) * k**2
        + (356 - 225 * epsilon) * k
        + 120
        - 177 * epsilon
    )
    assert numerator % 24 == 0
    return numerator // 24 - (21 if k == 6 else 0)


def cycle_score(order: tuple[int, ...], selected: frozenset[int]) -> int:
    induced = [x for x in order if x in selected]
    assert induced
    if len(induced) == 1:
        return induced[0] ** 2
    return sum(a * b for a, b in zip(induced, induced[1:] + induced[:1], strict=True))


def max_plus_k(order: tuple[int, ...]) -> DpResult:
    """Optimize induced increasing paths without enumerating subsets."""
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

    return DpResult(
        value=optimum,
        count=optimum_count,
        witness=frozenset(optimum_witness),
        transitions=transitions,
    )


def shortcut_certificate(
    order: tuple[int, ...], selected: frozenset[int], k: int
) -> tuple[int, int, int]:
    """Audit every oriented arc against the isolated-hole budget."""
    size = len(order)
    holes = set(range(2, 2 * k + 1))
    assert holes == set(order) - selected

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

    assert len(hole_gain) == 2 * k - 1
    assert min(hole_gain.values()) == 6 * k + 2
    full_score = cycle_score(order, frozenset(order))
    selected_score = cycle_score(order, selected)
    assert selected_score == full_score + sum(hole_gain.values())

    minimum_margin: int | None = None
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
                minimum_margin = (
                    margin if minimum_margin is None else min(minimum_margin, margin)
                )

    assert minimum_margin is not None
    return min(hole_gain.values()), minimum_margin, checked_arcs


def main() -> None:
    residue_transitions = 0
    canonical_transitions = 0
    shortcut_arcs = 0
    minimum_hole_gain: int | None = None
    minimum_path_margin: int | None = None

    for k in range(2, MAX_K + 1):
        residue_order = residue_one_order(k)
        residue_candidate = residue_one_candidate(k)
        residue_score = cycle_score(residue_order, residue_candidate)
        assert residue_score == residue_one_formula(k) == residue_one_n_formula(k)

        residue_dp = max_plus_k(residue_order)
        residue_transitions += residue_dp.transitions
        assert (residue_dp.value, residue_dp.count, residue_dp.witness) == (
            residue_score,
            1,
            residue_candidate,
        )

        hole_gain, path_margin, arcs = shortcut_certificate(
            residue_order, residue_candidate, k
        )
        shortcut_arcs += arcs
        minimum_hole_gain = (
            hole_gain
            if minimum_hole_gain is None
            else min(minimum_hole_gain, hole_gain)
        )
        minimum_path_margin = (
            path_margin
            if minimum_path_margin is None
            else min(minimum_path_margin, path_margin)
        )

        comparison_order = canonical_order(k)
        comparison_candidate = canonical_candidate(k)
        comparison_score = cycle_score(comparison_order, comparison_candidate)
        assert comparison_score == canonical_formula(k)
        comparison_dp = max_plus_k(comparison_order)
        canonical_transitions += comparison_dp.transitions
        assert (
            comparison_dp.value,
            comparison_dp.count,
            comparison_dp.witness,
        ) == (comparison_score, 1, comparison_candidate)

        gap = comparison_score - residue_score
        assert gap == expected_gap(k) and gap > 0

    for k in range(MAX_K + 1, FORMULA_MAX_K + 1):
        residue_order = residue_one_order(k)
        residue_score = cycle_score(residue_order, residue_one_candidate(k))
        assert residue_score == residue_one_formula(k) == residue_one_n_formula(k)

        comparison_order = canonical_order(k)
        comparison_score = cycle_score(comparison_order, canonical_candidate(k))
        assert comparison_score == canonical_formula(k)
        assert comparison_score - residue_score == expected_gap(k) > 0

    assert minimum_hole_gain == 14
    assert minimum_path_margin == 15
    print("residue-one exact K diagnostic: PASS")
    print(f"full-certificate rows: {MAX_K - 1} (k=2..{MAX_K})")
    print(f"residue max-plus transitions: {residue_transitions}")
    print(f"canonical max-plus transitions: {canonical_transitions}")
    print(f"oriented shortcut arcs: {shortcut_arcs}")
    print(f"formula/comparison tail rows: {FORMULA_MAX_K - MAX_K}")
    print(f"minimum bounded hole gain: {minimum_hole_gain}")
    print(f"minimum bounded path margin: {minimum_path_margin}")
    print("maximizers per residue row: 1")
    print("admissible K825 crossovers: 0")
    print("residue-one leading coefficient: 857/3000")


if __name__ == "__main__":
    main()
