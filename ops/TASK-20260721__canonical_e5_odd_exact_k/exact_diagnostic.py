"""Independent bounded checks for the canonical odd-v, e=5 exact K map.

This standalone script imports only the Python standard library. It builds
the one prescribed ``n = 10*m + 9`` path-to-gap assignment, checks every
assigned support incidence, expands its literal cyclic core, and computes
``K`` with a candidate-free least-selected-position max-plus recurrence.
A separate traversal audits every proper oriented arc, every isolated-hole
gain, the exact raw-arc plus hole-budget identity, and every shortcut through
the cyclic cut.

The minimum row is handled literally: its unique optimizer is ``8..19`` and
has score 2175. Formula, residue, support, K825, and coefficient identities
continue to the declared larger bound. On the bounded max-plus rows the
script also checks every insertion gap of label one and the exact elementary
elimination inequalities. It enumerates no assignment, matching, subset,
permanent, or alternative order family. The all-``m`` claims remain the
symbolic proof in the research note.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


MAX_DP_M = 30
FORMULA_MAX_M = 1000


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a nonnegative exact quotient."""
    assert numerator >= 0 and denominator > 0
    return (numerator + denominator - 1) // denominator


def closing_threshold(m: int) -> int:
    """Return ``q = kappa_(2m)`` on the canonical odd-v scaffold."""
    assert m >= 1
    return (4 * m + 5) // 5


def thresholds(m: int) -> tuple[int, ...]:
    """Return the literal PGE5ODD column thresholds."""
    d = 8 * m + 9
    return tuple(ceil_div(j * (d - 1), 2 * (d + j)) for j in range(2 * m + 1))


def prescribed_assignment(m: int) -> tuple[int, ...]:
    """Return only the map fixed in the exact-K theorem."""
    q = closing_threshold(m)
    return (
        *range(q),
        *range(q + 1, m + 2),
        *range(2 * m, m + 1, -1),
        q,
    )


def check_fixed_assignment(m: int, assignment: tuple[int, ...]) -> int:
    """Check the image partition and every assigned PGE5ODD support edge."""
    size = 2 * m + 1
    q = closing_threshold(m)
    kappas = thresholds(m)
    assert len(assignment) == size
    assert sorted(assignment) == list(range(size))
    for j, image in enumerate(assignment):
        if j < q:
            expected = j
        elif j <= m:
            expected = j + 1
        elif j <= 2 * m - 1:
            expected = 3 * m + 1 - j
        else:
            expected = q
        assert image == expected
    assert assignment[0] == kappas[0] == 0
    assert assignment[-1] == kappas[-1] == q
    assert all(assignment[j] >= kappas[j] for j in range(1, size))
    return size


def path(m: int, k: int) -> tuple[int, ...]:
    """Return the unchanged oriented PGE5ODD path ``P_k``."""
    d = 8 * m + 9
    assert 0 <= k <= 2 * m
    if k <= m + 1:
        return d - 1 - 2 * k, 4 * m + 4 + k, d - 2 - 2 * k
    return (4 * m + 4 + k,)


def core_order(m: int, assignment: tuple[int, ...]) -> tuple[int, ...]:
    """Expand the literal terminal/low/path scaffold from gap ``G_0``."""
    d = 8 * m + 9
    n = 10 * m + 9
    size = 2 * m + 1
    order: list[int] = []
    for j, k in enumerate(assignment):
        order.extend((d + j, 4 * m + 2 - 2 * j))
        order.extend(path(m, k))
        order.append(4 * m + 3 - 2 * ((j + 1) % size))
    result = tuple(order)
    assert len(result) == n - 1
    assert sorted(result) == list(range(2, n + 1))
    return result


def stable_backbone(m: int) -> frozenset[int]:
    """Return the all-row tail whose score is the polynomial ``F``."""
    return frozenset(range(4 * m + 3, 10 * m + 10))


def claimed_optimizer(m: int) -> frozenset[int]:
    """Return the claimed optimizer, including the exceptional minimum row."""
    lower = 8 if m == 1 else 4 * m + 3
    return frozenset(range(lower, 10 * m + 10))


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


def stable_score_formula(m: int) -> int:
    """Return the q-dependent score of the stable tail ``4m+3..n``."""
    q = closing_threshold(m)
    numerator = (
        1714 * m**3 + 4977 * m**2 + 24 * m * q + 4721 * m + 12 * q**2 + 72 * q + 1464
    )
    assert numerator % 6 == 0
    return numerator // 6


def score_formula(m: int) -> int:
    """Return the exact K value, including the ``m=1`` correction."""
    return stable_score_formula(m) + 11 * (m == 1)


def residue_formula(m: int) -> int:
    """Return the equivalent five-branch expression plus its sole residual."""
    c = (5, 1, 2, 3, 4)[m % 5]
    assert closing_threshold(m) == (4 * m + c) // 5
    numerator = (
        42_850 * m**3
        + 125_097 * m**2
        + (119_465 + 216 * c) * m
        + 36_600
        + 360 * c
        + 12 * c**2
    )
    assert numerator % 150 == 0
    return numerator // 150 + 11 * (m == 1)


def n_form_score_formula(m: int) -> int:
    """Return the equivalent n-form, including the minimum-row residual."""
    n = 10 * m + 9
    q = closing_threshold(m)
    assert q == (2 * n + 7) // 25
    numerator = (
        857 * n**3
        + 1746 * n**2
        + 1200 * n * q
        - 3629 * n
        + 6000 * q**2
        + 25_200 * q
        - 1518
        + 33_000 * (m == 1)
    )
    assert numerator % 3000 == 0
    return numerator // 3000


def check_symbolic_n_form_identity() -> tuple[int, ...]:
    """Check the regular n-form coefficientwise in independent ``m,q``."""
    # Coefficient order: m^3, m^2, m*q, m, q^2, q, 1.
    from_m_form = (
        500 * 1714,
        500 * 4977,
        500 * 24,
        500 * 4721,
        500 * 12,
        500 * 72,
        500 * 1464,
    )
    from_n_form_after_n_equals_10m_plus_9 = (
        857 * 1000,
        857 * 2700 + 1746 * 100,
        1200 * 10,
        857 * 2430 + 1746 * 180 - 3629 * 10,
        6000,
        1200 * 9 + 25_200,
        857 * 729 + 1746 * 81 - 3629 * 9 - 1518,
    )
    expected = (857_000, 2_488_500, 12_000, 2_360_500, 6_000, 36_000, 732_000)
    assert from_m_form == from_n_form_after_n_equals_10m_plus_9 == expected
    assert (2 * 10, 2 * 9 + 7) == (5 * 4, 5 * 5)
    return expected


def canonical_k825(m: int) -> int:
    """Return canonical K825 on the same ``n=10m+9`` row."""
    numerator = 572 * m**3 + 1667 * m**2 + 1627 * m + 532
    assert numerator % 2 == 0
    return numerator // 2 - 13 * (m == 1)


def canonical_gap(m: int) -> int:
    """Return ``K825-K`` from the exact q-dependent subtraction."""
    q = closing_threshold(m)
    numerator = m**3 + 12 * m**2 - 12 * m * q + 80 * m - 6 * q**2 - 36 * q + 66
    assert numerator % 3 == 0
    return numerator // 3 - 24 * (m == 1)


def max_plus_k(order: tuple[int, ...]) -> tuple[int, int, frozenset[int], int]:
    """Return K, optimizer count, one witness, and transition count."""
    size = len(order)
    optimum = -1
    optimum_count = 0
    optimum_witness: tuple[int, ...] = ()
    transitions = 0

    # Every nonempty subset has one least selected position. Fixing it turns
    # the remaining induced order into an increasing-position DAG path.
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

    assert transitions == comb(size + 1, 3)
    return optimum, optimum_count, frozenset(optimum_witness), transitions


def all_arcs_audit(
    m: int,
    order: tuple[int, ...],
    selected: frozenset[int],
) -> tuple[int, int, int, int]:
    """Audit every isolated-hole gain and every proper oriented arc."""
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
    proper_arcs = 0
    nontrivial_shortcuts = 0

    for start in range(size):
        first = order[start]
        kept = [first]
        raw_sum = 0
        compressed_sum = 0
        budget = 0

        for step in range(1, size):
            previous = order[(start + step - 1) % size]
            current = order[(start + step) % size]
            raw_sum += previous * current

            if step > 1 and previous in holes:
                assert kept[-1] == previous
                compressed_sum -= kept[-2] * kept[-1]
                kept.pop()
                budget += hole_gain[previous]

            compressed_sum += kept[-1] * current
            kept.append(current)
            assert raw_sum + budget == compressed_sum
            proper_arcs += 1

            if len(kept) >= 3:
                margin = compressed_sum - first * current
                shortcut_gain = first * current - raw_sum
                assert margin > 0
                assert shortcut_gain < budget
                nontrivial_shortcuts += 1
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
    if m == 1:
        assert (minimum_hole, minimum_holes) == (11, (7,))
        assert (minimum_margin, tuple(minimum_paths)) == (8, ((16, 8, 15),))
    elif m == 2:
        assert (minimum_hole, minimum_holes) == (110, (10,))
        assert (minimum_margin, tuple(minimum_paths)) == (9, ((19, 11, 25),))
    else:
        assert (minimum_hole, minimum_holes) == (36 * m + 38, (4 * m + 2,))
        expected = (8 * m + 8, 4 * m + 4, 8 * m + 7)
        assert (minimum_margin, tuple(minimum_paths)) == (
            4 * m + 4,
            (expected,),
        )

    return len(hole_gain), proper_arcs, nontrivial_shortcuts, selected_score


def insert_label_one(core: tuple[int, ...], gap: int) -> tuple[int, ...]:
    """Insert label one in one literal cyclic gap of the displayed core."""
    assert 0 <= gap < len(core)
    return core[:gap] + (1,) + core[gap:]


def label_one_elimination_audit(
    core: tuple[int, ...], selected: frozenset[int], score: int
) -> tuple[int, int]:
    """Check every insertion gap and the exact CR12m--CR12o inequalities."""
    n = len(core) + 1
    assert sorted(core) == list(range(2, n + 1))
    assert score > n**2
    for label in core:
        assert 2 * label <= label**2 <= n**2 < score

    neighbor_pairs = 0
    for left in range(2, n + 1):
        for right in range(left + 1, n + 1):
            gain = left * right - left - right
            assert gain == (left - 1) * (right - 1) - 1
            assert gain >= 1
            neighbor_pairs += 1

    for gap in range(len(core)):
        complete = insert_label_one(core, gap)
        assert sorted(complete) == list(range(1, n + 1))
        assert tuple(label for label in complete if label != 1) == core
        assert 1 not in selected
        assert cycle_score(complete, selected) == score

    return len(core), neighbor_pairs


def check_formula_row(m: int) -> tuple[int, int]:
    """Check one support/formula/comparator row without max-plus work."""
    assignment = prescribed_assignment(m)
    support_edges = check_fixed_assignment(m, assignment)
    order = core_order(m, assignment)
    stable = stable_backbone(m)
    winner = claimed_optimizer(m)

    assert cycle_score(order, stable) == stable_score_formula(m)
    assert cycle_score(order, winner) == score_formula(m)
    if m == 1:
        assert stable - winner == frozenset({7})
        assert score_formula(m) - stable_score_formula(m) == 11
    else:
        assert stable == winner

    assert score_formula(m) == residue_formula(m) == n_form_score_formula(m)
    assert canonical_k825(m) - score_formula(m) == canonical_gap(m) > 0
    assert score_formula(m) > (10 * m + 9) ** 2
    return len(order), support_edges


def main() -> None:
    """Run bounded max-plus/all-arcs checks and the longer exact formula tail."""
    minimum_order = (
        17,
        6,
        16,
        8,
        15,
        5,
        18,
        4,
        12,
        10,
        11,
        3,
        19,
        2,
        14,
        9,
        13,
        7,
    )
    assert prescribed_assignment(1) == (0, 2, 1)
    assert core_order(1, prescribed_assignment(1)) == minimum_order
    assert (stable_score_formula(1), score_formula(1), canonical_k825(1)) == (
        2164,
        2175,
        2186,
    )
    assert prescribed_assignment(2) == (0, 1, 3, 4, 2)
    symbolic_coefficients = check_symbolic_n_form_identity()

    core_entries = 0
    support_incidences = 0
    for m in range(1, FORMULA_MAX_M + 1):
        entries, incidences = check_formula_row(m)
        core_entries += entries
        support_incidences += incidences

    expected_initial = (
        2175,
        7469,
        17_873,
        35_090,
        60_834,
        96_761,
        144_693,
        206_294,
        283_278,
        377_359,
    )
    observed_initial: list[int] = []
    dp_transitions = 0
    deletion_gains = 0
    proper_arcs = 0
    nontrivial_shortcuts = 0
    insertion_gaps = 0
    elimination_neighbor_pairs = 0

    for m in range(1, MAX_DP_M + 1):
        order = core_order(m, prescribed_assignment(m))
        expected_winner = claimed_optimizer(m)
        score, count, witness, transitions = max_plus_k(order)
        assert (score, count, witness) == (
            score_formula(m),
            1,
            expected_winner,
        )
        if m <= 10:
            observed_initial.append(score)
        dp_transitions += transitions

        gains, arcs, shortcuts, audited_score = all_arcs_audit(
            m, order, expected_winner
        )
        assert audited_score == score
        deletion_gains += gains
        proper_arcs += arcs
        nontrivial_shortcuts += shortcuts

        gaps, pairs = label_one_elimination_audit(order, expected_winner, score)
        insertion_gaps += gaps
        elimination_neighbor_pairs += pairs

    assert tuple(observed_initial) == expected_initial
    assert core_entries == 5_013_000
    assert support_incidences == 1_002_000
    assert dp_transitions == 39_970_045
    assert deletion_gains == 1_891
    assert proper_arcs == 1_016_930
    assert nontrivial_shortcuts == 1_010_149
    assert insertion_gaps == 4_890
    assert elimination_neighbor_pairs == 508_465
    assert Fraction(143, 500) - Fraction(857, 3000) == Fraction(1, 3000)

    print("canonical odd-v e=5 exact-K diagnostic: PASS")
    print(f"max-plus/all-arcs rows: {MAX_DP_M} (m=1..{MAX_DP_M})")
    print(f"max-plus transitions: {dp_transitions}")
    print(f"isolated-hole gains checked: {deletion_gains}")
    print(f"proper oriented arcs checked: {proper_arcs}")
    print(f"nontrivial compressed shortcuts checked: {nontrivial_shortcuts}")
    print(f"label-one insertion gaps checked: {insertion_gaps}")
    print(f"label-one neighbor-pair inequalities: {elimination_neighbor_pairs}")
    print(f"formula/support rows: {FORMULA_MAX_M} (m=1..{FORMULA_MAX_M})")
    print(f"literal core entries checked: {core_entries}")
    print(f"assigned support incidences checked: {support_incidences}")
    print("unique argmax; minimum-row residual; closure; K825 gap verified")
    print(f"symbolic n-form coefficient tuple: {symbolic_coefficients}")
    print("rho and R2* consequences use CR22/CR27; no floating-pi check")


if __name__ == "__main__":
    main()
