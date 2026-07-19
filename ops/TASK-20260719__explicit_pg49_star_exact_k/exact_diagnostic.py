"""Independent bounded checks for the explicit PG49-star core order.

This standalone script imports only the Python standard library. It builds
the one prescribed Ferrers assignment directly, expands the retained
scaffold, scores induced cycles with an increasing-path max-plus dynamic
program, and checks every oriented compressed shortcut on bounded rows. It
enumerates no subset, path permutation, or matching.

The all-parameter claims remain the symbolic proofs in the research notes.
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
    """Return the exact PG49 Ferrers column thresholds."""
    d = 8 * m + 4
    return tuple(ceil_div(j * (d - 1), 2 * (d + j)) for j in range(2 * m))


def star_assignment(m: int) -> tuple[int, ...]:
    """Return the prescribed explicit assignment, without any search."""
    assert m >= 3
    q = (4 * m + 3) // 5
    return (
        0,
        *range(1, q),
        *range(q + 1, m + 1),
        *range(2 * m - 1, m, -1),
        q,
    )


def check_ferrers(m: int, alpha: tuple[int, ...]) -> None:
    """Check bijectivity, every Ferrers edge, and the cyclic threshold."""
    v = 2 * m
    q = (4 * m + 3) // 5
    kappa = thresholds(m)
    assert len(alpha) == v
    assert sorted(alpha) == list(range(v))
    assert alpha[0] == kappa[0] == 0
    assert alpha[-1] == kappa[-1] == q
    assert all(alpha[j] >= kappa[j] for j in range(1, v))


def path(m: int, k: int) -> tuple[int, ...]:
    """Return the retained oriented scaffold path P_k."""
    d = 8 * m + 4
    assert 0 <= k < 2 * m
    if k <= m:
        return d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k
    return (4 * m + 2 + k,)


def core_order(m: int, alpha: tuple[int, ...]) -> tuple[int, ...]:
    """Expand the fixed terminal/low/path scaffold from gap G_0."""
    n = 10 * m + 3
    d = 8 * m + 4
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


def candidate(m: int) -> frozenset[int]:
    """Return the claimed unique maximizing backbone."""
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


def score_formula(m: int) -> int:
    """Return the exact floor formula for the prescribed order."""
    q = (4 * m + 3) // 5
    numerator = (
        1714 * m**3 + 1863 * m**2 + 24 * m * q + 617 * m + 12 * q**2 + 48 * q + 66
    )
    assert numerator % 6 == 0
    return numerator // 6


def residue_formula(m: int) -> int:
    """Return the equivalent five-branch quasipolynomial."""
    correction = (0, 1, 2, 3, -1)[m % 5]
    numerator = (
        42850 * m**3
        + 47247 * m**2
        + (16385 + 216 * correction) * m
        + 1650
        + 240 * correction
        + 12 * correction**2
    )
    assert numerator % 150 == 0
    return numerator // 150


def k825(m: int) -> int:
    """Return canonical K825 on n=10m+3."""
    return (572 * m**3 + 629 * m**2 + 235 * m + 30) // 2


def closing_pg46(m: int) -> int:
    """Return the closing-PG46 score on the same row."""
    return (572 * m**3 + 631 * m**2 + 223 * m + 22) // 2


def preclosing_pg46(m: int) -> int:
    """Return the preclosing-PG46 score on the same row."""
    return (572 * m**3 + 631 * m**2 + 235 * m + 22) // 2


def max_plus_k(order: tuple[int, ...]) -> tuple[int, int, frozenset[int], int]:
    """Return K, optimizer count, one witness, and transition count."""
    size = len(order)
    optimum = -1
    optimum_count = 0
    optimum_witness: tuple[int, ...] = ()
    transitions = 0

    # Every subset has a unique least selected position. Fixing it turns the
    # induced cyclic order into one path in the increasing-position DAG.
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
    """Check all isolated-hole gains and every oriented compressed arc."""
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
                minimum_margin = (
                    margin if minimum_margin is None else min(minimum_margin, margin)
                )

    assert minimum_margin is not None
    return minimum_margin, min(hole_gain.values()), checked_arcs


def check_row(m: int, *, use_dp: bool) -> tuple[int, int, int]:
    """Check one exact row and return finite-work counters."""
    alpha = star_assignment(m)
    check_ferrers(m, alpha)
    order = core_order(m, alpha)
    selected = candidate(m)
    score = cycle_score(order, selected)
    assert score == score_formula(m) == residue_formula(m)
    assert score < min(k825(m), closing_pg46(m), preclosing_pg46(m))
    assert score > (10 * m + 3) ** 2

    if not use_dp:
        return 0, 0, score

    optimum, count, witness, transitions = max_plus_k(order)
    assert (optimum, count, witness) == (score, 1, selected)
    minimum_margin, minimum_hole, arcs = shortcut_certificate(order, selected)
    assert minimum_margin == 12 * m + 4
    assert minimum_hole == 28 * m + 12
    return transitions, arcs, score


def main() -> None:
    """Run bounded max-plus/shortcut checks and a finite formula tail."""
    assert star_assignment(3) == (0, 1, 2, 5, 4, 3)
    expected_initial = (
        10905,
        23763,
        44140,
        73720,
        114217,
        167345,
        234744,
        318268,
    )
    observed_initial: list[int] = []
    dp_transitions = 0
    shortcut_arcs = 0

    for m in range(3, MAX_DP_M + 1):
        transitions, arcs, score = check_row(m, use_dp=True)
        dp_transitions += transitions
        shortcut_arcs += arcs
        if m <= 10:
            observed_initial.append(score)

    assert tuple(observed_initial) == expected_initial

    for m in range(MAX_DP_M + 1, FORMULA_MAX_M + 1):
        check_row(m, use_dp=False)

    assert dp_transitions == 36_989_498
    assert shortcut_arcs == 958_916
    assert Fraction(1714, 6 * 10**3) == Fraction(857, 3000)
    assert (score_formula(3), closing_pg46(3), k825(3), preclosing_pg46(3)) == (
        10905,
        10907,
        10920,
        10925,
    )

    print("explicit PG49-star exact-K diagnostic: PASS")
    print(f"max-plus/shortcut rows: {MAX_DP_M - 2} (m=3..{MAX_DP_M})")
    print(f"max-plus transitions: {dp_transitions}")
    print(f"oriented proper-arc checks: {shortcut_arcs}")
    print(f"formula/Ferrers rows: {FORMULA_MAX_M - 2} (m=3..{FORMULA_MAX_M})")
    print("unique argmax B_m on every max-plus row")
    print("cyclic closure included in every oriented-arc audit")
    print("strictly below K825 and both PG46 orders on every checked row")


if __name__ == "__main__":
    main()
