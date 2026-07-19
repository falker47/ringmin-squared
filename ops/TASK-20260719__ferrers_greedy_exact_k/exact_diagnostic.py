"""Independent bounded checks for the descending-min PG49 core order.

This standalone script imports only the Python standard library.  It builds
the one deterministic descending-min Ferrers assignment in two independent
ways, expands its prescribed scaffold core order, runs an increasing-path
max-plus dynamic program, and checks every oriented shortcut budget on a
bounded set of rows.  It enumerates no subset, permutation, or matching.

The all-parameter claims remain the symbolic proofs in the research notes.
"""

from __future__ import annotations


MAX_DP_M = 30
FORMULA_MAX_M = 1000


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative exact quotient."""
    assert numerator >= 0 and denominator > 0
    return (numerator + denominator - 1) // denominator


def thresholds(m: int) -> tuple[int, ...]:
    """Return the exact PG49 column thresholds."""
    d = 8 * m + 4
    return tuple(ceil_div(j * (d - 1), 2 * (d + j)) for j in range(2 * m))


def literal_greedy(m: int) -> tuple[int, ...]:
    """Run the requested descending-min assignment literally."""
    v = 2 * m
    kappa = thresholds(m)
    alpha: list[int | None] = [None] * v
    alpha[0] = 0
    used = {0}
    for j in range(v - 1, 0, -1):
        k = kappa[j]
        while k in used:
            k += 1
        assert k < v
        alpha[j] = k
        used.add(k)
    assert all(value is not None for value in alpha)
    return tuple(int(value) for value in alpha)


def closed_greedy(m: int) -> tuple[int, ...]:
    """Return the closed 0/1-jump formula for the same assignment."""
    v = 2 * m
    kappa = thresholds(m)
    alpha = [0] * v
    for j in range(1, v - 1):
        delta = kappa[j + 1] - kappa[j]
        assert delta in (0, 1)
        alpha[j] = kappa[j] + (1 - delta) * (v - 1 - j)
    alpha[v - 1] = kappa[v - 1]
    return tuple(alpha)


def check_ferrers_invariant(m: int, alpha: tuple[int, ...]) -> None:
    """Check the interval suffix invariant and every PG49 edge."""
    v = 2 * m
    kappa = thresholds(m)
    assert alpha[0] == 0
    assert sorted(alpha) == list(range(v))
    assert kappa[0] == 0 and kappa[1] == 1
    for j in range(1, v):
        assert alpha[j] >= kappa[j]
        assert set(alpha[j:]) == set(range(kappa[j], kappa[j] + v - j))


def path(m: int, k: int) -> tuple[int, ...]:
    """Return the retained oriented scaffold path P_k."""
    d = 8 * m + 4
    assert 0 <= k < 2 * m
    if k <= m:
        return d - 1 - 2 * k, 4 * m + 2 + k, d - 2 - 2 * k
    return (4 * m + 2 + k,)


def core_order(m: int, alpha: tuple[int, ...]) -> tuple[int, ...]:
    """Expand the fixed terminal/low/path scaffold from gap G_0 onward."""
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


def cycle_score(order: tuple[int, ...], selected: frozenset[int]) -> int:
    """Score one nonempty induced cyclic order."""
    induced = [label for label in order if label in selected]
    assert induced
    if len(induced) == 1:
        return induced[0] ** 2
    return sum(
        left * right
        for left, right in zip(induced, induced[1:] + induced[:1], strict=True)
    )


def isolated_low_gains(m: int, order: tuple[int, ...]) -> dict[int, int]:
    """Return the deletion gain of every isolated low scaffold label."""
    size = len(order)
    gains: dict[int, int] = {}
    for index, label in enumerate(order):
        if label > 4 * m:
            continue
        left = order[(index - 1) % size]
        right = order[(index + 1) % size]
        assert left >= 4 * m + 1 and right >= 4 * m + 1
        gains[label] = left * right - label * (left + right)
    assert set(gains) == set(range(2, 4 * m + 1))
    return gains


def predicted_optimizer(m: int, gains: dict[int, int]) -> frozenset[int]:
    """Keep the high backbone and precisely the negative deletion gains."""
    n = 10 * m + 3
    assert all(gain != 0 for gain in gains.values())
    return frozenset(
        set(range(4 * m + 1, n + 1))
        | {label for label, gain in gains.items() if gain < 0}
    )


def exact_score_formula(order: tuple[int, ...], gains: dict[int, int]) -> int:
    """Evaluate the exact isolated-gain positive-part formula."""
    full = cycle_score(order, frozenset(order))
    return full + sum(max(gain, 0) for gain in gains.values())


def max_plus_k(order: tuple[int, ...]) -> tuple[int, int, frozenset[int], int]:
    """Return K, optimizer count, one witness, and transition count."""
    size = len(order)
    optimum = -1
    optimum_count = 0
    optimum_witness: tuple[int, ...] = ()
    transitions = 0

    # A subset has one least selected position.  Fixing it turns the induced
    # cyclic order into one path in the increasing-position DAG.
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
                candidate = witness[previous] + (order[end],)
                if value > best[end]:
                    best[end] = value
                    count[end] = count[previous]
                    witness[end] = candidate
                elif value == best[end]:
                    count[end] += count[previous]
                    if candidate < witness[end]:
                        witness[end] = candidate

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
    order: tuple[int, ...],
    selected: frozenset[int],
    gains: dict[int, int],
) -> tuple[int, int, int]:
    """Check every positive hole and every oriented compressed shortcut."""
    holes = set(order) - selected
    assert holes == {label for label, gain in gains.items() if gain > 0}
    assert holes
    for hole in holes:
        assert gains[hole] > 0

    full_score = cycle_score(order, frozenset(order))
    selected_score = cycle_score(order, selected)
    assert selected_score == full_score + sum(gains[hole] for hole in holes)

    size = len(order)
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

            if step > 1 and previous in holes:
                assert kept[-1] == previous
                compressed_sum -= kept[-2] * kept[-1]
                kept.pop()
                budget += gains[previous]

            compressed_sum += kept[-1] * current
            kept.append(current)
            assert original_sum + budget == compressed_sum
            checked_arcs += 1

            if len(kept) >= 3:
                margin = compressed_sum - first * current
                assert margin > 0
                min_margin = margin if min_margin is None else min(min_margin, margin)

    assert min_margin is not None
    return min_margin, min(gains[hole] for hole in holes), checked_arcs


def k825(m: int) -> int:
    """Canonical K825 value on n=10m+3."""
    return (572 * m**3 + 629 * m**2 + 235 * m + 30) // 2


def closing_pg46(m: int) -> int:
    """Closing-PG46 value on n=10m+3."""
    return (572 * m**3 + 631 * m**2 + 223 * m + 22) // 2


def preclosing_pg46(m: int) -> int:
    """Preclosing-PG46 value on n=10m+3."""
    return (572 * m**3 + 631 * m**2 + 235 * m + 22) // 2


def check_comparators(m: int, score: int) -> None:
    """Check the exact pointwise ordering against all three witnesses."""
    assert (score < k825(m)) == (m == 4)
    assert score != k825(m)
    assert score > closing_pg46(m)
    assert (score < preclosing_pg46(m)) == (m == 4)
    assert score != preclosing_pg46(m)


def row(m: int) -> int:
    """Build one exact formula row and return its certified score."""
    literal = literal_greedy(m)
    closed = closed_greedy(m)
    assert literal == closed
    check_ferrers_invariant(m, closed)
    order = core_order(m, closed)
    gains = isolated_low_gains(m, order)
    selected = predicted_optimizer(m, gains)
    score = cycle_score(order, selected)
    assert score == exact_score_formula(order, gains)
    check_comparators(m, score)
    return score


def main() -> None:
    """Run the bounded max-plus/shortcut audit and the lighter formula tail."""
    anchors = {
        3: (10932, (), 40, 71),
        4: (23817, (), 52, 57),
        6: (73963, (22,), 19, 87),
        8: (168112, (29, 30), 21, 236),
        13: (686394, (46, 49, 50), 36, 186),
        30: (8059131, (105, 106, 109, 110, 113, 114, 117, 118), 294, 852),
    }
    expected_m3_alpha = (0, 5, 1, 4, 2, 3)
    assert closed_greedy(3) == expected_m3_alpha

    dp_transitions = 0
    shortcut_arcs = 0
    for m in range(3, MAX_DP_M + 1):
        alpha = closed_greedy(m)
        assert literal_greedy(m) == alpha
        check_ferrers_invariant(m, alpha)
        order = core_order(m, alpha)
        gains = isolated_low_gains(m, order)
        selected = predicted_optimizer(m, gains)
        score = exact_score_formula(order, gains)
        assert cycle_score(order, selected) == score
        check_comparators(m, score)

        optimum, count, witness, transitions = max_plus_k(order)
        dp_transitions += transitions
        assert (optimum, count, witness) == (score, 1, selected)

        min_margin, min_hole, arcs = shortcut_certificate(order, selected, gains)
        shortcut_arcs += arcs

        if m in anchors:
            expected_score, expected_low, expected_margin, expected_hole = anchors[m]
            observed_low = tuple(sorted(label for label in selected if label <= 4 * m))
            assert (score, observed_low, min_margin, min_hole) == (
                expected_score,
                expected_low,
                expected_margin,
                expected_hole,
            )

    for m in range(MAX_DP_M + 1, FORMULA_MAX_M + 1):
        score = row(m)
        assert score > (10 * m + 3) ** 2

    assert dp_transitions == 36_989_498
    assert shortcut_arcs == 958_916
    assert k825(3) == 10920 and closing_pg46(3) == 10907
    assert preclosing_pg46(3) == 10925

    print("descending-min PG49 exact-K diagnostic: PASS")
    print(f"max-plus/shortcut rows: {MAX_DP_M - 2} (m=3..{MAX_DP_M})")
    print(f"max-plus transitions: {dp_transitions}")
    print(f"oriented shortcut arcs: {shortcut_arcs}")
    print(f"formula/comparator rows: {FORMULA_MAX_M - 2} (m=3..{FORMULA_MAX_M})")
    print("unique argmax on every max-plus row")
    print("no zero low gain on checked rows m=3..1000")
    print("K825/preclosing improvement only at m=4; closing never improved")


if __name__ == "__main__":
    main()
