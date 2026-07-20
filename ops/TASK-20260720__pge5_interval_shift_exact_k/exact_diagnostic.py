"""Independent bounded checks for the fixed PGE5 interval shift.

This standalone script imports only the Python standard library. It builds
only alpha_(q,2m-1) on the e=5, n=10m+4 scaffold, expands the literal cyclic
core, and computes K with a candidate-free increasing-path max-plus dynamic
program. A separate all-oriented-arc traversal audits every isolated-hole
gain and every compressed shortcut, including the cyclic cut.

It enumerates no subset, path permutation, matching, supported bijection, or
permanent. The all-m claims remain the symbolic proof in the research note.
"""

from __future__ import annotations

from fractions import Fraction


MAX_DP_M = 30
FORMULA_MAX_M = 1000


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative exact quotient."""
    assert numerator >= 0 and denominator > 0
    return (numerator + denominator - 1) // denominator


def thresholds(m: int) -> tuple[int, ...]:
    """Return the exact PGE5 Ferrers column thresholds."""
    d = 8 * m + 5
    return tuple(ceil_div(j * (d - 1), 2 * (d + j)) for j in range(2 * m))


def interval_shift(m: int) -> tuple[int, ...]:
    """Return only alpha_(q,2m-1), directly and without search."""
    assert m >= 2
    q = (4 * m + 3) // 5
    return (*range(q), *range(q + 1, 2 * m), q)


def check_fixed_assignment(m: int, alpha: tuple[int, ...]) -> None:
    """Check the prescribed map, its closing target, and every used edge."""
    v = 2 * m
    q = (4 * m + 3) // 5
    kappa = thresholds(m)
    assert len(alpha) == v
    assert sorted(alpha) == list(range(v))
    assert alpha[:-1] == (*range(q), *range(q + 1, v))
    assert alpha[0] == kappa[0] == 0
    assert alpha[-1] == kappa[-1] == q
    assert all(alpha[j] >= kappa[j] for j in range(1, v))


def path(m: int, k: int) -> tuple[int, ...]:
    """Return the unchanged oriented PGE5 path P_k."""
    d = 8 * m + 5
    assert 0 <= k < 2 * m
    if k <= m:
        return d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k
    if k == m + 1:
        return 5 * m + 3, 5 * m + 4
    return (4 * m + 3 + k,)


def core_order(m: int, alpha: tuple[int, ...]) -> tuple[int, ...]:
    """Expand the literal terminal/low/path scaffold from gap G_0."""
    n = 10 * m + 4
    d = 8 * m + 5
    v = 2 * m
    order: list[int] = []
    for j, k in enumerate(alpha):
        order.extend((d + j, 4 * m - 2 * j))
        order.extend(path(m, k))
        order.append(4 * m + 1 - 2 * ((j + 1) % v))
    result = tuple(order)
    assert len(result) == n - 1
    assert sorted(result) == list(range(2, n + 1))
    return result


def claimed_backbone(m: int) -> frozenset[int]:
    """Return the set compared with, but not supplied to, the max-plus DP."""
    return frozenset(range(4 * m + 1, 10 * m + 5))


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


def score_formula(m: int) -> int:
    """Return the exact q-dependent formula obtained by the block sum."""
    q = (4 * m + 3) // 5
    numerator = 572 * m**3 + 809 * m**2 + 8 * m * q + 329 * m + 4 * q**2 + 20 * q + 36
    assert numerator % 2 == 0
    return numerator // 2


def residue_formula(m: int) -> int:
    """Return the equivalent five-branch quasipolynomial."""
    correction = (0, 1, 2, 3, -1)[m % 5]
    numerator = (
        14_300 * m**3
        + 20_449 * m**2
        + (8_625 + 72 * correction) * m
        + 900
        + 100 * correction
        + 4 * correction**2
    )
    assert numerator % 50 == 0
    return numerator // 50


def canonical_k825(m: int) -> int:
    """Return canonical K825 on the same n=10m+4 row."""
    numerator = 572 * m**3 + 819 * m**2 + 361 * m + 44
    assert numerator % 2 == 0
    return numerator // 2


def exact_canonical_gap(m: int) -> int:
    """Return K825 minus the fixed PGE5 score by its residue branch."""
    correction = (0, 1, 2, 3, -1)[m % 5]
    numerator = (
        13 * m**2
        + (200 - 36 * correction) * m
        + 100
        - 50 * correction
        - 2 * correction**2
    )
    assert numerator % 25 == 0
    return numerator // 25


def max_plus_k(order: tuple[int, ...]) -> tuple[int, int, frozenset[int], int]:
    """Return K, all-optimizer count, one witness, and transition count."""
    size = len(order)
    optimum = -1
    optimum_count = 0
    optimum_witness: tuple[int, ...] = ()
    transitions = 0

    # Every nonempty subset has a unique least selected position. Fixing it
    # turns the remaining induced order into a path in an increasing DAG.
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
) -> tuple[int, int, int, tuple[tuple[int, ...], ...], tuple[int, ...]]:
    """Check every isolated-hole gain and every proper oriented arc."""
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

    minimum_margin: int | None = None
    minimum_paths: list[tuple[int, ...]] = []
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
                compressed_path = tuple(kept)
                if minimum_margin is None or margin < minimum_margin:
                    minimum_margin = margin
                    minimum_paths = [compressed_path]
                elif margin == minimum_margin:
                    minimum_paths.append(compressed_path)

    assert minimum_margin is not None
    minimum_hole = min(hole_gain.values())
    minimum_holes = tuple(
        sorted(hole for hole, gain in hole_gain.items() if gain == minimum_hole)
    )
    return (
        minimum_margin,
        minimum_hole,
        checked_arcs,
        tuple(minimum_paths),
        minimum_holes,
    )


def check_row(m: int, *, use_dp: bool) -> tuple[int, int, int]:
    """Check one exact row and return finite-work counters."""
    alpha = interval_shift(m)
    check_fixed_assignment(m, alpha)
    order = core_order(m, alpha)
    selected = claimed_backbone(m)
    score = cycle_score(order, selected)
    q = (4 * m + 3) // 5

    assert score == score_formula(m) == residue_formula(m)
    assert canonical_k825(m) - score == exact_canonical_gap(m)
    assert canonical_k825(m) - score == (
        5 * m**2 - 4 * m * q + 16 * m - 2 * q**2 - 10 * q + 4
    )
    assert score < canonical_k825(m)
    assert score > (10 * m + 4) ** 2

    if not use_dp:
        return 0, 0, score

    optimum, count, witness, transitions = max_plus_k(order)
    assert (optimum, count, witness) == (score, 1, selected)
    minimum_margin, minimum_hole, arcs, minimum_paths, minimum_holes = (
        shortcut_certificate(order, selected)
    )
    expected_margin = 9 if m == 2 else 4 * m + 2
    expected_path = (15, 9, 21) if m == 2 else (8 * m + 4, 4 * m + 2, 8 * m + 3)
    assert minimum_margin == expected_margin
    assert minimum_hole == 36 * m + 20
    assert minimum_paths == (expected_path,)
    assert minimum_holes == (4 * m,)
    return transitions, arcs, score


def main() -> None:
    """Run bounded max-plus/shortcut checks and a finite formula tail."""
    minimum_order = (
        21,
        8,
        20,
        10,
        19,
        7,
        22,
        6,
        18,
        11,
        17,
        5,
        23,
        4,
        13,
        14,
        3,
        24,
        2,
        16,
        12,
        15,
        9,
    )
    assert interval_shift(2) == (0, 1, 3, 2)
    assert core_order(2, interval_shift(2)) == minimum_order

    expected_initial = (
        4_297,
        11_958,
        25_548,
        46_855,
        77_563,
        119_388,
        174_046,
        243_177,
        328_641,
    )
    observed_initial: list[int] = []
    dp_transitions = 0
    shortcut_arcs = 0

    for m in range(2, MAX_DP_M + 1):
        transitions, arcs, score = check_row(m, use_dp=True)
        dp_transitions += transitions
        shortcut_arcs += arcs
        if m <= 10:
            observed_initial.append(score)

    assert tuple(observed_initial) == expected_initial

    for m in range(MAX_DP_M + 1, FORMULA_MAX_M + 1):
        check_row(m, use_dp=False)

    assert dp_transitions == 37_475_656
    assert shortcut_arcs == 968_774
    assert Fraction(286, 10**3) == Fraction(143, 500)
    assert Fraction(13, 25) / 10**2 == Fraction(13, 2500)
    assert Fraction(13, 2500) / Fraction(143, 500) == Fraction(1, 55)
    assert (score_formula(2), canonical_k825(2), exact_canonical_gap(2)) == (
        4_297,
        4_309,
        12,
    )

    print("fixed PGE5 interval-shift exact-K diagnostic: PASS")
    print(f"max-plus/shortcut rows: {MAX_DP_M - 1} (m=2..{MAX_DP_M})")
    print(f"max-plus transitions: {dp_transitions}")
    print(f"proper oriented-arc checks: {shortcut_arcs}")
    print(f"formula/support rows: {FORMULA_MAX_M - 1} (m=2..{FORMULA_MAX_M})")
    print("unique argmax B_m on every max-plus row")
    print("m=2 and every cyclic closing arc included")
    print("five residue branches and exact canonical gaps verified")


if __name__ == "__main__":
    main()
