from __future__ import annotations

from fractions import Fraction
import itertools
import math

import pytest

from power_ringmin.product_distance import (
    MAX_CANONICAL_ORDERS,
    adjacent_equality_structure,
    adjacent_product_optimum,
    best_tail_lower_obstruction,
    canonical_core_order_count,
    canonical_core_orders,
    canonicalize_core_order,
    circular_position_distance,
    eight_twenty_fifths_order,
    eight_twenty_fifths_threshold,
    enumerate_product_distance,
    enumerate_truncated_product_distance,
    product_distance_pair_scores,
    product_distance_score,
    residue_one_product_distance_order,
    residue_two_product_distance_order,
    tail_cycle_incompatibility_minimum,
    tail_pairing_sum,
    terminal_high_incidence_closed_form,
    terminal_high_incidence_lower_obstruction,
    truncated_product_distance_score,
    two_threshold_lower_obstruction,
    two_threshold_tail_packing,
)
from power_ringmin.patterns import interleave


EXPECTED_TABLE = {
    3: (1, Fraction(6), 1, (3, 2), Fraction(6), None, ()),
    4: (1, Fraction(12), 1, (4, 2, 3), Fraction(12), Fraction(25, 3), (2,)),
    5: (3, Fraction(15), 1, (5, 2, 4, 3), Fraction(15), Fraction(23, 2), (3,)),
    6: (12, Fraction(20), 2, (6, 2, 4, 5, 3), Fraction(24), Fraction(76, 5), (3,)),
    7: (60, Fraction(24), 2, (7, 2, 5, 4, 6, 3), Fraction(28), Fraction(58, 3), (4,)),
    8: (
        360,
        Fraction(30),
        4,
        (8, 2, 5, 6, 4, 7, 3),
        Fraction(40),
        Fraction(170, 7),
        (4,),
    ),
    9: (
        2520,
        Fraction(36),
        12,
        (9, 2, 6, 5, 7, 3, 8, 4),
        Fraction(45),
        Fraction(59, 2),
        (4,),
    ),
    10: (
        20160,
        Fraction(45),
        72,
        (10, 2, 6, 7, 3, 8, 5, 9, 4),
        Fraction(60),
        Fraction(320, 9),
        (5,),
    ),
    11: (
        181440,
        Fraction(50),
        24,
        (11, 2, 7, 6, 8, 3, 10, 5, 9, 4),
        Fraction(66),
        Fraction(42),
        (5,),
    ),
}


EXPECTED_TRUNCATED_TABLE = {
    3: (Fraction(6), 1, (3, 2), Fraction(6), 1, (3, 2)),
    4: (Fraction(12), 1, (4, 2, 3), Fraction(12), 1, (4, 2, 3)),
    5: (Fraction(15), 1, (5, 2, 4, 3), Fraction(15), 1, (5, 2, 4, 3)),
    6: (
        Fraction(20),
        2,
        (6, 2, 4, 5, 3),
        Fraction(20),
        2,
        (6, 2, 4, 5, 3),
    ),
    7: (
        Fraction(24),
        2,
        (7, 2, 5, 4, 6, 3),
        Fraction(24),
        2,
        (7, 2, 5, 4, 6, 3),
    ),
    8: (
        Fraction(30),
        4,
        (8, 2, 5, 6, 4, 7, 3),
        Fraction(30),
        4,
        (8, 2, 5, 6, 4, 7, 3),
    ),
    9: (
        Fraction(35),
        4,
        (9, 2, 6, 5, 7, 4, 8, 3),
        Fraction(36),
        12,
        (9, 2, 6, 5, 7, 3, 8, 4),
    ),
    10: (
        Fraction(42),
        24,
        (10, 2, 6, 7, 5, 8, 3, 9, 4),
        Fraction(45),
        72,
        (10, 2, 6, 7, 3, 8, 5, 9, 4),
    ),
    11: (
        Fraction(48),
        24,
        (11, 2, 7, 6, 8, 5, 9, 3, 10, 4),
        Fraction(50),
        24,
        (11, 2, 7, 6, 8, 3, 10, 5, 9, 4),
    ),
}


EXPECTED_EIGHT_TWENTY_FIFTHS_EXCEPTIONS = {
    9: (
        (9, 2, 8, 4, 6, 5, 7, 3),
        (Fraction(35), Fraction(36), Fraction(15)),
        (Fraction(27), Fraction(63, 2), Fraction(15)),
    ),
    10: (
        (10, 2, 9, 4, 7, 6, 5, 8, 3),
        (Fraction(42), Fraction(45), Fraction(56, 3)),
        (Fraction(30), Fraction(40), Fraction(50, 3)),
    ),
    11: (
        (11, 2, 10, 4, 8, 6, 7, 5, 9, 3),
        (Fraction(48), Fraction(55), Fraction(20)),
        (Fraction(33), Fraction(99, 2), Fraction(55, 3)),
    ),
    12: (
        (12, 2, 11, 4, 9, 6, 7, 8, 5, 10, 3),
        (Fraction(56), Fraction(66), Fraction(24)),
        (Fraction(36), Fraction(60), Fraction(20)),
    ),
    14: (
        (14, 3, 11, 2, 13, 4, 12, 6, 9, 8, 7, 10, 5),
        (Fraction(72), Fraction(78), Fraction(98, 3)),
        (Fraction(70), Fraction(70), Fraction(98, 3)),
    ),
    15: (
        (15, 3, 12, 2, 14, 4, 13, 6, 10, 8, 9, 7, 11, 5),
        (Fraction(80), Fraction(91), Fraction(35)),
        (Fraction(75), Fraction(165, 2), Fraction(35)),
    ),
    16: (
        (16, 2, 13, 4, 15, 6, 11, 8, 9, 10, 7, 14, 5, 12, 3),
        (Fraction(98), Fraction(104), Fraction(42)),
        (Fraction(48), Fraction(96), Fraction(80, 3)),
    ),
    17: (
        (17, 5, 14, 3, 13, 2, 16, 4, 15, 6, 12, 8, 10, 9, 11, 7),
        (Fraction(119), Fraction(120), Fraction(51)),
        (Fraction(119), Fraction(187, 2), Fraction(51)),
    ),
    20: (
        (20, 2, 13, 10, 11, 12, 9, 17, 7, 16, 5, 18, 3, 15, 8, 19, 4, 14, 6),
        (Fraction(153), Fraction(144), Fraction(200, 3)),
        (Fraction(120), Fraction(140), Fraction(80, 3)),
    ),
    21: (
        (21, 6, 15, 4, 20, 2, 16, 3, 19, 5, 17, 7, 18, 9, 13, 11, 12, 10, 14, 8),
        (Fraction(168), Fraction(323, 2), Fraction(70)),
        (Fraction(168), Fraction(147), Fraction(70)),
    ),
    22: (
        (22, 2, 16, 4, 19, 6, 20, 8, 15, 10, 13, 12, 11, 14, 9, 21, 7, 18, 5, 17, 3),
        (Fraction(189), Fraction(190), Fraction(77)),
        (Fraction(66), Fraction(187), Fraction(110, 3)),
    ),
    26: (
        (
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
        (Fraction(253), Fraction(252), Fraction(325, 3)),
        (Fraction(78), Fraction(247), Fraction(130, 3)),
    ),
    27: (
        (
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
        (Fraction(276), Fraction(273), Fraction(325, 3)),
        (Fraction(81), Fraction(513, 2), Fraction(45)),
    ),
    32: (
        (
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
        (Fraction(360), Fraction(378), Fraction(155)),
        (Fraction(96), Fraction(368), Fraction(160, 3)),
    ),
}


@pytest.fixture(scope="module")
def exact_enumerations():
    return {n: enumerate_product_distance(n) for n in range(3, 12)}


@pytest.fixture(scope="module")
def exact_truncated_enumerations():
    return {
        (n, max_distance): enumerate_truncated_product_distance(n, max_distance)
        for n in range(3, 12)
        for max_distance in (1, 2)
    }


def _independent_score(order: tuple[int, ...]) -> Fraction:
    """Score all pairs by iterating positions, without production support."""
    vertex_count = len(order)
    ratios = []
    for left in range(vertex_count):
        for right in range(left + 1, vertex_count):
            step = right - left
            distance = min(step, vertex_count - step)
            ratios.append(Fraction(order[left] * order[right], distance))
    return max(ratios)


def _independent_label_first_score(order: tuple[int, ...]) -> Fraction:
    """Score all pairs from a label-to-position map via a separate traversal."""
    positions = {label: position for position, label in enumerate(order)}
    vertex_count = len(order)
    return max(
        Fraction(left * right, distance)
        for left, right in itertools.combinations(sorted(positions), 2)
        for separation in (abs(positions[left] - positions[right]),)
        for distance in (min(separation, vertex_count - separation),)
    )


def _independent_truncated_score(
    order: tuple[int, ...],
    max_position_distance: int,
) -> Fraction:
    """Score a truncated order without production scoring support."""
    vertex_count = len(order)
    return max(
        Fraction(order[left] * order[right], distance)
        for left in range(vertex_count)
        for right in range(left + 1, vertex_count)
        for step in (right - left,)
        for distance in (min(step, vertex_count - step),)
        if distance <= max_position_distance
    )


def _independent_exact_distance_scores(
    order: tuple[int, ...],
    max_distance: int,
) -> tuple[Fraction, ...]:
    """Return exact maxima by distance without production scoring support."""
    vertex_count = len(order)
    return tuple(
        max(
            Fraction(
                order[position] * order[(position + distance) % vertex_count], distance
            )
            for position in range(vertex_count)
        )
        for distance in range(1, max_distance + 1)
    )


def _independent_closing_distance_scores(
    order: tuple[int, ...],
    max_distance: int,
) -> tuple[Fraction, ...]:
    """Return exact maxima over local pairs crossing the displayed cut."""
    vertex_count = len(order)
    return tuple(
        max(
            Fraction(
                order[position] * order[(position + distance) % vertex_count],
                distance,
            )
            for position in range(vertex_count - distance, vertex_count)
        )
        for distance in range(1, max_distance + 1)
    )


def _independent_canonicalize(order: tuple[int, ...]) -> tuple[int, ...]:
    largest = max(order)
    forward_index = order.index(largest)
    forward = order[forward_index:] + order[:forward_index]
    if len(order) == 2:
        return forward
    reversed_order = tuple(reversed(order))
    backward_index = reversed_order.index(largest)
    backward = reversed_order[backward_index:] + reversed_order[:backward_index]
    return min(forward, backward)


def _independent_tail_cycle_incompatibility(
    n: int,
    threshold: Fraction,
) -> int:
    """Brute-force ``eta_n(T)`` without using production tail support."""
    tail = tuple(
        index
        for index in range(2, n + 1)
        if index * (index + 1) > threshold
    )
    if len(tail) <= 1:
        return 0
    if len(tail) > 7:
        raise ValueError("independent eta enumeration is limited to tail size 7")

    anchor = tail[0]
    return min(
        sum(
            order[position] * order[(position + 1) % len(order)]
            > 2 * threshold
            for position in range(len(order))
        )
        for suffix in itertools.permutations(tail[1:])
        for order in ((anchor, *suffix),)
    )


def _independent_threshold_tail_data(
    n: int,
    threshold: Fraction,
) -> tuple[int, int, tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    """Construct ``a,b,U,V`` and compatible lows without production support."""
    a_threshold = next(
        k for k in itertools.count(2) if k * (k + 1) > threshold
    )
    b_threshold = next(
        k for k in itertools.count(2) if k * (k + 1) > 2 * threshold
    )
    u_tail = tuple(
        index
        for index in range(2, n + 1)
        if index * (index + 1) > threshold
    )
    v_tail = tuple(
        index
        for index in range(2, n + 1)
        if index * (index + 1) > 2 * threshold
    )
    compatible_lows = tuple(
        low
        for low in range(2, a_threshold)
        if low * b_threshold <= threshold
    )
    return a_threshold, b_threshold, u_tail, v_tail, compatible_lows


def _independent_joint_threshold(n: int) -> Fraction:
    """Invert both necessary conditions by direct half-integer scanning."""
    for doubled_threshold in range(2 * n * (n - 1) + 1):
        threshold = Fraction(doubled_threshold, 2)
        _a, _b, u_tail, v_tail, compatible_lows = (
            _independent_threshold_tail_data(n, threshold)
        )
        if 2 * len(u_tail) > n - 1:
            continue
        minimum_incompatibilities = _independent_tail_cycle_incompatibility(
            n,
            threshold,
        )
        required_positions = 2 * len(u_tail) + minimum_incompatibilities
        if (
            required_positions <= n - 1
            and 2 * len(v_tail) <= len(compatible_lows)
        ):
            return threshold
    raise AssertionError("independent half-integer scan was not exhaustive")


def _independent_terminal_high_closed_form(n: int) -> Fraction:
    """Evaluate the proposed residue formula without production helpers."""
    k, residue = divmod(n, 5)
    if n == 12:
        return Fraction(56)
    polynomial_by_residue = (
        8 * k * k + 6 * k + 1,
        8 * k * k + 8 * k + 2,
        8 * k * k + 10 * k + 3,
        8 * k * k + 14 * k + 6,
        8 * k * k + 18 * k + 10,
    )
    return Fraction(polynomial_by_residue[residue])


def _independent_product_distance_optimum_closed_form(n: int) -> Fraction:
    """Evaluate the exact ``B_n = W_n`` residue formula independently."""
    if n < 9:
        raise ValueError("the exact residue formula starts at n=9")
    k, residue = divmod(n, 5)
    polynomial_by_residue = (
        8 * k * k + 6 * k + 1,
        8 * k * k + 8 * k + 2,
        8 * k * k + 12 * k + 4,
        8 * k * k + 14 * k + 6,
        8 * k * k + 18 * k + 10,
    )
    return Fraction(polynomial_by_residue[residue])


def test_rational_pair_scores_are_exact_and_cover_every_pair() -> None:
    order = (9, 2, 6, 5, 7, 4, 8, 3)
    pair_scores = product_distance_pair_scores(order)

    assert len(pair_scores) == math.comb(len(order), 2)
    assert all(isinstance(pair.ratio, Fraction) for pair in pair_scores)
    assert {
        frozenset((pair.left_index, pair.right_index)) for pair in pair_scores
    } == {
        frozenset(pair) for pair in itertools.combinations(range(2, 10), 2)
    }

    maximum = max(pair.ratio for pair in pair_scores)
    maximizers = [pair for pair in pair_scores if pair.ratio == maximum]
    adjacent_maximum = max(
        pair.ratio for pair in pair_scores if pair.distance == 1
    )

    assert maximum == Fraction(9 * 8, 2) == Fraction(36)
    assert adjacent_maximum == Fraction(35)
    assert len(maximizers) == 1
    assert {maximizers[0].left_index, maximizers[0].right_index} == {8, 9}
    assert maximizers[0].distance == 2
    assert product_distance_score(order) == maximum
    assert truncated_product_distance_score(order, 1) == adjacent_maximum
    assert truncated_product_distance_score(order, 2) == maximum


def test_adjacent_optimum_formula_and_interleave_construction_are_exact() -> None:
    assert adjacent_product_optimum(3) == 6
    for n in range(4, 201):
        expected = (n // 2 + 1) * ((n + 1) // 2 + 2)
        order = tuple(int(value) for value in interleave(range(2, n + 1)))
        adjacent_sums = tuple(
            order[position] + order[(position + 1) % len(order)]
            for position in range(len(order))
        )

        assert adjacent_product_optimum(n) == expected
        assert truncated_product_distance_score(order, 1) == expected
        assert set(adjacent_sums) <= {n + 1, n + 2, n + 3}

    with pytest.raises(ValueError):
        adjacent_product_optimum(2)


def test_adjacent_equality_structure_is_exact_on_bounded_regression() -> None:
    for n in range(4, 12):
        optimum = Fraction(adjacent_product_optimum(n))
        t = n // 2
        expected_forced_edges = (
            ((t + 1, t + 2),)
            if n % 2 == 0
            else ((t + 1, t + 2), (t + 1, t + 3))
        )

        for order in canonical_core_orders(n):
            structure = adjacent_equality_structure(order)
            is_optimal = truncated_product_distance_score(order, 1) == optimum
            assert (structure is not None) == is_optimal
            if structure is None:
                continue

            assert structure.optimum == optimum
            assert structure.forced_high_high_edges == expected_forced_edges
            assert {triple[0] for triple in structure.low_neighbor_high_pairs} == set(
                structure.low_vertices
            )
            assert len(structure.active_high_path) == len(
                structure.low_neighbor_high_pairs
            ) + 1
            for low, left_high, right_high in structure.low_neighbor_high_pairs:
                assert low * left_high <= optimum
                assert low * right_high <= optimum

    with pytest.raises(ValueError, match="n >= 4"):
        adjacent_equality_structure((3, 2))


def test_distance_two_equals_adjacent_exactly_through_n8_by_witness() -> None:
    for n in range(3, 9):
        order = tuple(int(value) for value in interleave(range(2, n + 1)))
        assert (
            truncated_product_distance_score(order, 2)
            == adjacent_product_optimum(n)
        )


def test_terminal_high_clique_incidence_lemma_boundary_arithmetic() -> None:
    def counts(n: int) -> tuple[int, int, int]:
        optimum = adjacent_product_optimum(n)
        high_maximum = n
        discriminant_root = math.isqrt(1 + 8 * optimum)
        first_high = (discriminant_root - 1) // 2
        while first_high * (first_high + 1) <= 2 * optimum:
            first_high += 1
        clique_size = high_maximum - first_high + 1
        compatible_lows = optimum // first_high - 1
        return first_high, clique_size, compatible_lows

    # These are the exact boundary cases outside the monotone polynomial
    # ranges in the all-n proof.  This is formula evaluation, not order
    # enumeration.
    assert counts(10) == (9, 2, 3)
    assert counts(14) == (12, 3, 5)
    assert counts(9) == (8, 2, 3)
    assert counts(11) == (10, 2, 3)
    assert counts(13) == (11, 3, 4)

    for n in (9, 10, 11, 13, 14, 15, 16):
        _first_high, clique_size, compatible_lows = counts(n)
        assert 2 * clique_size > compatible_lows

    even_boundary = 14 * 8**2 - 94 * 8 - 94
    odd_boundary = 14 * 7**2 - 80 * 7 - 100
    assert even_boundary > 0
    assert odd_boundary > 0
    assert 28 * 8 - 94 > 0
    assert 28 * 7 - 80 > 0


def test_n12_exceptional_degree_obstruction_parameters_are_exact() -> None:
    optimum = adjacent_product_optimum(12)
    active_highs = tuple(range(7, 13))
    small_highs = (7, 8, 9)

    assert optimum == 56
    assert tuple(
        high
        for high in active_highs
        if high != 12 and 12 * high <= 2 * optimum
    ) == small_highs
    assert tuple(high for high in active_highs if 6 * high <= optimum) == small_highs

    # In the active high path, 7 and 8 are endpoints and 9 is internal.
    # Their four degree units would all be consumed by the two edges to 12
    # and the edge labelled by low 6, leaving no connection to 10 or 11.
    available_small_high_degree = 1 + 1 + 2
    consumed_by_high_12 = 2
    consumed_by_low_6_edge = 2
    assert available_small_high_degree == (
        consumed_by_high_12 + consumed_by_low_6_edge
    )


def test_terminal_high_incidence_injection_matches_independent_small_orders() -> None:
    checked_states = 0
    checked_orders = 0
    for n in range(3, 8):
        for order in itertools.permutations(range(2, n + 1)):
            checked_orders += 1
            score = _independent_truncated_score(order, 2)
            for doubled_threshold in range(
                2 * score.numerator // score.denominator,
                2 * n * (n + 1) + 1,
            ):
                threshold = Fraction(doubled_threshold, 2)
                if threshold < score:
                    continue
                _a, b, u_tail, v_tail, compatible_lows = (
                    _independent_threshold_tail_data(n, threshold)
                )
                checked_states += 1

                if n == 3:
                    assert not v_tail
                    continue

                u_set = set(u_tail)
                incidence_lows = []
                for high in v_tail:
                    position = order.index(high)
                    neighbors = (
                        order[(position - 1) % len(order)],
                        order[(position + 1) % len(order)],
                    )
                    assert neighbors[0] != neighbors[1]
                    for low in neighbors:
                        assert low not in u_set
                        assert low * high <= threshold
                        assert low * b <= threshold
                        incidence_lows.append(low)

                assert len(incidence_lows) == 2 * len(v_tail)
                assert len(set(incidence_lows)) == len(incidence_lows)
                assert set(incidence_lows) <= set(compatible_lows)
                assert 2 * len(v_tail) <= len(compatible_lows)

    assert checked_orders == 872
    assert checked_states == 34160


def test_two_threshold_tail_starts_and_degenerate_sizes_are_exact() -> None:
    below_first_boundary = two_threshold_tail_packing(5, Fraction(11, 2))
    at_first_boundary = two_threshold_tail_packing(5, 6)
    marked_singleton = two_threshold_tail_packing(5, 12)
    marked_empty = two_threshold_tail_packing(5, 15)
    first_tail_singleton = two_threshold_tail_packing(5, 20)
    first_tail_empty = two_threshold_tail_packing(5, 30)

    assert below_first_boundary.a_threshold == 2
    assert at_first_boundary.a_threshold == 3
    assert (
        marked_singleton.a_threshold,
        marked_singleton.b_threshold,
        marked_singleton.u_size,
        marked_singleton.v_size,
        marked_singleton.compatible_low_capacity,
        marked_singleton.minimum_incompatibilities,
        marked_singleton.required_positions,
    ) == (4, 5, 2, 1, 1, 0, 4)
    assert (
        marked_empty.a_threshold,
        marked_empty.b_threshold,
        marked_empty.u_size,
        marked_empty.v_size,
        marked_empty.compatible_low_capacity,
        marked_empty.minimum_incompatibilities,
        marked_empty.required_positions,
    ) == (4, 6, 2, 0, 1, 0, 4)
    assert (
        first_tail_singleton.a_threshold,
        first_tail_singleton.b_threshold,
        first_tail_singleton.u_size,
        first_tail_singleton.v_size,
        first_tail_singleton.compatible_low_capacity,
        first_tail_singleton.minimum_incompatibilities,
        first_tail_singleton.required_positions,
    ) == (5, 6, 1, 0, 2, 0, 2)
    assert (
        first_tail_empty.a_threshold,
        first_tail_empty.u_size,
        first_tail_empty.v_size,
        first_tail_empty.compatible_low_capacity,
        first_tail_empty.required_positions,
    ) == (6, 0, 0, 2, 0)

    for threshold in (
        Fraction(0),
        Fraction(11, 2),
        Fraction(6),
        Fraction(59, 2),
        Fraction(1000),
    ):
        packing = two_threshold_tail_packing(11, threshold)
        direct_a = next(
            k for k in itertools.count(2) if k * (k + 1) > threshold
        )
        direct_b = next(
            k for k in itertools.count(2) if k * (k + 1) > 2 * threshold
        )
        assert packing.a_threshold == direct_a
        assert packing.b_threshold == direct_b
        assert 0 <= packing.v_size <= packing.u_size

    with pytest.raises(ValueError, match="nonnegative"):
        two_threshold_tail_packing(5, -1)
    with pytest.raises(ValueError, match="integer or Fraction"):
        two_threshold_tail_packing(5, 1.0)


def test_terminal_high_capacity_strict_and_nonstrict_boundaries_are_exact() -> None:
    n3 = two_threshold_tail_packing(3, 6)
    v_zero = two_threshold_tail_packing(5, 15)
    v_one = two_threshold_tail_packing(7, 21)
    before_even_square = two_threshold_tail_packing(11, Fraction(99, 2))
    at_even_square = two_threshold_tail_packing(11, 50)
    empty_tails = two_threshold_tail_packing(5, 30)

    assert (
        n3.a_threshold,
        n3.b_threshold,
        n3.u_size,
        n3.v_size,
        n3.required_positions,
        n3.compatible_low_capacity,
    ) == (3, 4, 1, 0, 2, 0)
    assert (v_zero.v_size, v_zero.compatible_low_capacity) == (0, 1)
    assert (v_one.v_size, v_one.compatible_low_capacity) == (1, 2)
    assert (
        before_even_square.a_threshold,
        before_even_square.b_threshold,
        before_even_square.u_size,
        before_even_square.v_size,
        before_even_square.required_positions,
        before_even_square.compatible_low_capacity,
    ) == (7, 10, 5, 2, 10, 3)
    assert (
        at_even_square.a_threshold,
        at_even_square.b_threshold,
        at_even_square.u_size,
        at_even_square.v_size,
        at_even_square.required_positions,
        at_even_square.compatible_low_capacity,
    ) == (7, 10, 5, 2, 10, 4)
    assert 5 * at_even_square.b_threshold == at_even_square.threshold
    assert (empty_tails.u_size, empty_tails.v_size) == (0, 0)

    for packing in (
        n3,
        v_zero,
        v_one,
        before_even_square,
        at_even_square,
        empty_tails,
    ):
        _a, _b, _u, _v, compatible_lows = _independent_threshold_tail_data(
            packing.n,
            packing.threshold,
        )
        assert packing.compatible_low_capacity == len(compatible_lows)


def test_terminal_high_incidences_are_distinct_at_n11_equality() -> None:
    order = (11, 2, 7, 6, 8, 3, 10, 5, 9, 4)
    threshold = Fraction(50)
    assert _independent_truncated_score(order, 2) == threshold

    _a, _b, u_tail, v_tail, compatible_lows = (
        _independent_threshold_tail_data(11, threshold)
    )
    assert v_tail == (10, 11)
    incidence_lows = tuple(
        order[(order.index(high) + offset) % len(order)]
        for high in v_tail
        for offset in (-1, 1)
    )
    assert set(incidence_lows).isdisjoint(u_tail)
    assert len(set(incidence_lows)) == 2 * len(v_tail)
    assert set(incidence_lows) == set(compatible_lows) == {2, 3, 4, 5}


def test_exact_tail_cycle_incompatibility_boundaries_and_strict_correction() -> None:
    empty = two_threshold_tail_packing(5, 30)
    singleton = two_threshold_tail_packing(5, 20)
    incompatible_pair = two_threshold_tail_packing(3, 0)
    compatible_pair = two_threshold_tail_packing(3, 3)
    strict_correction = two_threshold_tail_packing(5, 6)
    before_skip_one_equality = two_threshold_tail_packing(9, 30)
    at_skip_one_equality = two_threshold_tail_packing(9, Fraction(63, 2))

    assert (empty.u_size, empty.minimum_incompatibilities) == (0, 0)
    assert (singleton.u_size, singleton.minimum_incompatibilities) == (1, 0)
    assert (
        incompatible_pair.u_size,
        incompatible_pair.clique_incompatibility_bound,
        incompatible_pair.minimum_incompatibilities,
    ) == (2, 2, 2)
    assert (
        compatible_pair.u_size,
        compatible_pair.clique_incompatibility_bound,
        compatible_pair.minimum_incompatibilities,
    ) == (2, 0, 0)
    assert (
        strict_correction.u_size,
        strict_correction.clique_incompatibility_bound,
        strict_correction.minimum_incompatibilities,
    ) == (3, 1, 2)
    assert (
        before_skip_one_equality.u_size,
        before_skip_one_equality.clique_incompatibility_bound,
        before_skip_one_equality.minimum_incompatibilities,
        before_skip_one_equality.required_positions,
    ) == (4, 0, 1, 9)
    assert (
        at_skip_one_equality.u_size,
        at_skip_one_equality.clique_incompatibility_bound,
        at_skip_one_equality.minimum_incompatibilities,
        at_skip_one_equality.required_positions,
    ) == (4, 0, 0, 8)

    for packing in (
        empty,
        singleton,
        incompatible_pair,
        compatible_pair,
        strict_correction,
        before_skip_one_equality,
        at_skip_one_equality,
    ):
        assert tail_cycle_incompatibility_minimum(
            packing.n,
            packing.threshold,
        ) == packing.minimum_incompatibilities
        assert (
            packing.clique_incompatibility_bound
            <= packing.minimum_incompatibilities
            <= packing.clique_incompatibility_bound + 1
        )


def test_exact_tail_cycle_formula_matches_independent_small_tail_enumerator() -> None:
    comparison_count = 0
    for n in range(3, 12):
        events = {Fraction(0)}
        events.update(
            Fraction(index * (index + 1)) for index in range(2, n + 1)
        )
        events.update(
            Fraction(left * right, 2)
            for left, right in itertools.combinations(range(2, n + 1), 2)
        )
        ordered_events = sorted(events)
        thresholds = events | {
            (left + right) / 2
            for left, right in itertools.pairwise(ordered_events)
        }

        for threshold in sorted(thresholds):
            tail_size = sum(
                index * (index + 1) > threshold
                for index in range(2, n + 1)
            )
            if tail_size > 7:
                continue
            assert tail_cycle_incompatibility_minimum(
                n,
                threshold,
            ) == _independent_tail_cycle_incompatibility(n, threshold)
            comparison_count += 1

    assert comparison_count >= 250


def test_two_threshold_and_joint_finite_obstructions_are_exact(
    exact_truncated_enumerations,
) -> None:
    expected = {
        3: (Fraction(6), Fraction(6)),
        4: (Fraction(12), Fraction(12)),
        5: (Fraction(12), Fraction(15)),
        6: (Fraction(20), Fraction(20)),
        7: (Fraction(21), Fraction(21)),
        8: (Fraction(30), Fraction(30)),
        9: (Fraction(63, 2), Fraction(36)),
        10: (Fraction(42), Fraction(45)),
        11: (Fraction(45), Fraction(50)),
    }

    for n, (q_obstruction, h_obstruction) in expected.items():
        assert two_threshold_lower_obstruction(n) == q_obstruction
        assert two_threshold_tail_packing(
            n,
            q_obstruction,
        ).required_positions <= n - 1
        assert two_threshold_tail_packing(
            n,
            q_obstruction - Fraction(1, 2),
        ).required_positions > n - 1
        assert q_obstruction <= exact_truncated_enumerations[n, 2].optimum

        assert (
            terminal_high_incidence_lower_obstruction(n)
            == _independent_joint_threshold(n)
            == h_obstruction
        )
        packing = two_threshold_tail_packing(n, h_obstruction)
        predecessor = two_threshold_tail_packing(
            n,
            h_obstruction - Fraction(1, 2),
        )
        assert packing.required_positions <= n - 1
        assert 2 * packing.v_size <= packing.compatible_low_capacity
        assert (
            predecessor.required_positions > n - 1
            or 2 * predecessor.v_size > predecessor.compatible_low_capacity
        )
        assert h_obstruction <= exact_truncated_enumerations[n, 2].optimum
        assert max(adjacent_product_optimum(n), h_obstruction) == (
            exact_truncated_enumerations[n, 2].optimum
        )


def test_terminal_high_asymptotic_witness_is_exact() -> None:
    for n in range(11, 501):
        d = (4 * n + 12) // 5
        threshold = Fraction(d * (d - 1), 2)
        packing = two_threshold_tail_packing(n, threshold)

        assert packing.b_threshold == d
        assert 2 * packing.v_size <= packing.compatible_low_capacity
        assert packing.required_positions <= n - 1
        assert Fraction(8 * n * n + 10 * n, 25) < threshold
        assert threshold < Fraction(8 * n * n + 42 * n + 52, 25)

    assert 7 * 11**2 - 62 * 11 - 152 > 0
    assert 32 > 25  # 4*sqrt(2)>5, so the first Psi branch is slack.
    assert 2 > 1  # sqrt(2)>1, so the second Psi branch is slack.
    assert 20000 > 16129  # 8/25 exceeds the unchanged Q_n coefficient.


def test_terminal_high_incidence_closed_form_is_exact() -> None:
    for n in range(9, 201):
        expected = _independent_terminal_high_closed_form(n)
        closed_form = terminal_high_incidence_closed_form(n)
        assert isinstance(closed_form, Fraction)
        assert closed_form == expected
        assert terminal_high_incidence_lower_obstruction(n) == expected

    for n in range(9, 5001):
        d = (4 * n + 12) // 5
        upper_threshold = Fraction(d * (d - 1), 2)
        obstruction = terminal_high_incidence_closed_form(n)

        if n % 5 in (0, 3, 4):
            assert obstruction == upper_threshold
        elif n % 5 == 1:
            assert obstruction == Fraction((d - 1) ** 2, 2)
        elif n == 12:
            assert obstruction == 56
        else:
            assert n >= 17
            assert obstruction == Fraction((d - 1) * (d - 2), 2)


@pytest.mark.parametrize(
    ("n", "expected_h", "expected_j", "expected_upper"),
    (
        (12, Fraction(56), Fraction(60), Fraction(66)),
        (17, Fraction(105), Fraction(112), Fraction(120)),
        (22, Fraction(171), Fraction(180), Fraction(190)),
    ),
)
def test_residue_two_saturation_obstruction_exact_cases(
    n: int,
    expected_h: Fraction,
    expected_j: Fraction,
    expected_upper: Fraction,
) -> None:
    """Rebuild every structural input without a production J helper."""
    k = (n - 2) // 5
    d = 4 * k + 4
    x = d - 2
    core = set(range(2, n + 1))
    expected_lows = tuple(range(2, d // 2))
    expected_intermediate = tuple(range(d // 2, d - 1))
    expected_terminal = tuple(range(d - 1, n + 1))

    assert n == 5 * k + 2
    assert d == (4 * n + 12) // 5
    assert terminal_high_incidence_closed_form(n) == expected_h
    assert Fraction(d * (d - 2), 2) == expected_j
    assert Fraction(eight_twenty_fifths_threshold(n)) == expected_upper
    assert set(expected_lows).isdisjoint(expected_intermediate)
    assert set(expected_lows).isdisjoint(expected_terminal)
    assert set(expected_intermediate).isdisjoint(expected_terminal)
    assert (
        set(expected_lows) | set(expected_intermediate) | set(expected_terminal)
        == core
    )

    assert expected_h.denominator == expected_j.denominator == 1
    for doubled_threshold in range(
        2 * expected_h.numerator,
        2 * expected_j.numerator,
    ):
        threshold = Fraction(doubled_threshold, 2)
        a, b, u_tail, v_tail, compatible_lows = (
            _independent_threshold_tail_data(n, threshold)
        )

        assert d // 2 <= a <= x
        assert b == d - 1
        assert x in u_tail
        assert v_tail == expected_terminal
        assert compatible_lows == expected_lows
        assert len(compatible_lows) == 2 * len(v_tail) == 2 * k

        adjacent_candidates = tuple(
            label
            for label in range(2, n + 1)
            if label != x and x * label <= threshold
        )
        distance_two_terminal_candidates = tuple(
            high for high in v_tail if x * high <= 2 * threshold
        )
        assert adjacent_candidates == expected_lows
        assert distance_two_terminal_candidates == (d - 1,)

        cycle_size = n - 1
        assert cycle_size > 4
        assert (-2) % cycle_size != 2 % cycle_size

    boundary_adjacent_intermediate = tuple(
        label
        for label in expected_intermediate
        if x * label <= expected_j
    )
    boundary_terminal_candidates = tuple(
        high
        for high in expected_terminal
        if x * high <= 2 * expected_j
    )
    assert boundary_adjacent_intermediate == (d // 2,)
    assert boundary_terminal_candidates == (d - 1, d)
    assert Fraction(x * (d // 2)) == expected_j
    assert Fraction(x * d, 2) == expected_j


def test_residue_two_saturation_endpoint_arithmetic_broad_falsification() -> None:
    """Check the symbolic strict endpoints for 2 <= k <= 1000 exactly."""
    for k in range(2, 1001):
        n = 5 * k + 2
        d = 4 * k + 4
        q = d // 2 - 1
        x = d - 2
        h = (
            Fraction(56)
            if k == 2
            else Fraction((d - 1) * (d - 2), 2)
        )
        j = Fraction(d * (d - 2), 2)
        last_excluded = j - Fraction(1, 2)
        upper = Fraction(d * (d - 1), 2)

        assert d == (4 * n + 12) // 5
        assert j == 8 * k * k + 12 * k + 4
        assert h <= last_excluded

        # These endpoint inequalities force b_X=d-1 throughout H<=X<J.
        assert (d - 2) * (d - 1) <= 2 * h
        assert 2 * last_excluded < (d - 1) * d

        # They also keep the compatible-low floor equal to q=2k+1.
        assert q == 2 * k + 1
        assert q * (d - 1) <= h
        assert last_excluded < (q + 1) * (d - 1)
        assert q * (q + 1) < h
        assert 2 * k == len(range(2, q + 1))
        assert k == len(range(d - 1, n + 1))

        # The two strict local incompatibilities disappear exactly at J.
        assert x * (d // 2) == j
        assert Fraction(x * (d - 1), 2) <= h
        assert Fraction(x * d, 2) == j > last_excluded
        assert (-2) % (n - 1) != 2 % (n - 1)

        assert upper - j == Fraction(d, 2)
        assert upper - j == Fraction(2 * n + 6, 5)
        if k == 2:
            assert (h, j, upper) == (56, 60, 66)
        else:
            assert j - h == 2 * k + 1


def test_eight_twenty_fifths_exceptional_orders_include_closing_pairs() -> None:
    for n, (
        expected_order,
        expected_scores,
        expected_closing,
    ) in EXPECTED_EIGHT_TWENTY_FIFTHS_EXCEPTIONS.items():
        order = eight_twenty_fifths_order(n)
        threshold = Fraction(eight_twenty_fifths_threshold(n))

        assert order == expected_order
        assert tuple(sorted(order)) == tuple(range(2, n + 1))
        assert _independent_exact_distance_scores(order, 3) == expected_scores
        assert _independent_closing_distance_scores(order, 3) == expected_closing
        assert _independent_score(order) == max(expected_scores)
        assert _independent_score(order) <= threshold


def test_eight_twenty_fifths_symbolic_family_is_exact() -> None:
    exceptional_values = set(EXPECTED_EIGHT_TWENTY_FIFTHS_EXCEPTIONS)
    formula_values_below_33 = {13, 18, 19, 23, 24, 25, 28, 29, 30, 31}

    assert {
        n for n in range(9, 33) if n not in exceptional_values
    } == formula_values_below_33

    for n in range(9, 1001):
        order = eight_twenty_fifths_order(n)
        threshold = eight_twenty_fifths_threshold(n)
        vertex_count = n - 1

        assert tuple(sorted(order)) == tuple(range(2, n + 1))
        for distance in (1, 2, 3):
            assert all(
                order[position] * order[(position + distance) % vertex_count]
                <= distance * threshold
                for position in range(vertex_count)
            )
        assert n * (n - 1) < 4 * threshold

        if n not in exceptional_values:
            d = (4 * n + 12) // 5
            positions = {value: position for position, value in enumerate(order)}
            step = abs(positions[d] - positions[d - 1])
            assert min(step, vertex_count - step) == 2
            assert d * (d - 1) == 2 * threshold

    full_score_values = (
        *sorted(formula_values_below_33),
        *range(33, 43),
        98,
        99,
        100,
        101,
        102,
        498,
        499,
        500,
        501,
        502,
    )
    for n in full_score_values:
        assert _independent_score(eight_twenty_fifths_order(n)) == (
            eight_twenty_fifths_threshold(n)
        )


def test_long_distance_domination_holds_through_92_and_first_fails_at_93() -> None:
    small_optima = (6, 12, 15, 20, 24, 30)
    for n, optimum in enumerate(small_optima, start=3):
        assert 3 * optimum >= n * (n - 1)

    # This is exact residue-formula evaluation, not cyclic-order enumeration.
    for n in range(9, 93):
        optimum = _independent_product_distance_optimum_closed_form(n)
        assert 3 * optimum >= n * (n - 1)

    optimum_93 = _independent_product_distance_optimum_closed_form(93)
    assert optimum_93 == 2850
    assert 3 * optimum_93 == 93 * 92 - 6

    # The failed sufficient inequality is not monotone beyond the first index.
    optimum_94 = _independent_product_distance_optimum_closed_form(94)
    assert optimum_94 == 2926
    assert 3 * optimum_94 >= 94 * 93


def test_n93_long_distance_minimizer_restriction_has_independent_exact_score() -> None:
    base_order = eight_twenty_fifths_order(93)
    source_position = base_order.index(92)
    target_position = base_order.index(16)
    assert base_order[source_position : source_position + 5] == (92, 4, 54, 3, 93)
    assert base_order[target_position : target_position + 2] == (16, 48)
    assert _independent_score(base_order) == 2850

    moved_order = list(base_order)
    moved_order.remove(54)
    insertion_position = moved_order.index(48)
    assert moved_order[insertion_position - 1] == 16
    moved_order.insert(insertion_position, 54)
    order = tuple(moved_order)

    assert len(order) == 92
    assert set(order) == set(range(2, 94))
    assert order[order.index(16) : order.index(16) + 3] == (16, 54, 48)
    assert order[order.index(92) : order.index(92) + 4] == (92, 4, 3, 93)

    distance_scores = _independent_exact_distance_scores(order, 3)
    truncated_score = _independent_truncated_score(order, 2)
    full_score = _independent_score(order)
    assert distance_scores == (Fraction(2850), Fraction(2850), Fraction(2852))
    assert truncated_score == 2850
    assert full_score == 2852
    assert _independent_label_first_score(order) == full_score

    positions = {label: position for position, label in enumerate(order)}
    vertex_count = len(order)
    pair_rows = tuple(
        (
            left,
            right,
            min(
                abs(positions[left] - positions[right]),
                vertex_count - abs(positions[left] - positions[right]),
            ),
        )
        for left, right in itertools.combinations(range(2, 94), 2)
    )
    scored_rows = tuple(
        (left, right, distance, Fraction(left * right, distance))
        for left, right, distance in pair_rows
    )
    assert len(scored_rows) == math.comb(vertex_count, 2)
    assert tuple(
        row for row in scored_rows if row[2] <= 2 and row[3] == truncated_score
    ) == (
        (38, 75, 1, Fraction(2850)),
        (75, 76, 2, Fraction(2850)),
    )
    assert tuple(row for row in scored_rows if row[3] > 2850) == (
        (92, 93, 3, Fraction(2852)),
    )
    assert max(row[3] for row in scored_rows if row[2] >= 4) == 2093

    optimum_93 = _independent_product_distance_optimum_closed_form(93)
    assert truncated_score == optimum_93
    assert full_score > optimum_93
    assert truncated_product_distance_score(order, 2) == truncated_score
    assert product_distance_score(order) == full_score


def test_eight_twenty_fifths_construction_validation_is_strict() -> None:
    for invalid in (True, 8, Fraction(9), 9.0):
        with pytest.raises(ValueError, match="integer at least 9"):
            terminal_high_incidence_closed_form(invalid)  # type: ignore[arg-type]
        with pytest.raises(ValueError, match="integer at least 9"):
            eight_twenty_fifths_order(invalid)  # type: ignore[arg-type]
        with pytest.raises(ValueError, match="integer at least 9"):
            eight_twenty_fifths_threshold(invalid)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("m", "triple_index"),
    ((3, 0), (3, 1), (3, 3), (4, 2), (9, 0), (9, 9)),
)
def test_one_triple_reversal_has_exact_full_distance_obstruction(
    m: int,
    triple_index: int,
) -> None:
    n = 10 * m + 3
    d = 8 * m + 4
    threshold = Fraction(d * (d - 1), 2)
    left = d - 1 - 2 * triple_index
    connector = 4 * m + 2 + triple_index
    right = left - 1

    order_list = list(eight_twenty_fifths_order(n))
    start = order_list.index(left)
    assert tuple(order_list[start : start + 3]) == (left, connector, right)
    order_list[start : start + 3] = (right, connector, left)
    order = tuple(order_list)

    assert len(order) == n - 1
    assert set(order) == set(range(2, n + 1))

    expected_score = Fraction(d * d - 1, 2) if triple_index == 0 else threshold
    distance_scores = _independent_exact_distance_scores(order, 3)
    assert distance_scores[0] == threshold
    assert distance_scores[1] == expected_score
    assert distance_scores[2] == Fraction((5 * m + 2) * (9 * m + 5), 3)
    assert distance_scores[2] < threshold

    positions = {label: position for position, label in enumerate(order)}
    vertex_count = len(order)
    long_score = max(
        Fraction(left_label * right_label, distance)
        for left_label, right_label in itertools.combinations(range(2, n + 1), 2)
        for separation in (abs(positions[left_label] - positions[right_label]),)
        for distance in (min(separation, vertex_count - separation),)
        if distance >= 4
    )
    assert long_score == Fraction(n * (n - 1), 4) < threshold

    closing_third = d - 2 if triple_index == 0 else d - 1
    assert _independent_closing_distance_scores(order, 3) == (
        Fraction((4 * m + 1) * d),
        Fraction((6 * m + 1) * d, 2),
        Fraction((4 * m + 1) * closing_third, 3),
    )
    assert _independent_score(order) == expected_score
    assert _independent_label_first_score(order) == expected_score
    assert product_distance_score(order) == expected_score


def test_residue_one_construction_has_exact_local_scores_and_closing_arcs() -> None:
    expected_diagnostics = {
        2: (
            (10, 4, 9, 3, 11, 2, 8, 6, 7, 5),
            (Fraction(50), Fraction(99, 2), Fraction(22)),
            (Fraction(50), Fraction(35), Fraction(20)),
        ),
        3: (
            (14, 6, 13, 5, 15, 4, 12, 8, 11, 3, 16, 2, 10, 9, 7),
            (Fraction(98), Fraction(195, 2), Fraction(48)),
            (Fraction(98), Fraction(63), Fraction(140, 3)),
        ),
    }
    for k, (expected_order, expected_scores, expected_closing) in (
        expected_diagnostics.items()
    ):
        n = 5 * k + 1
        order = residue_one_product_distance_order(n)

        assert order == expected_order
        assert _independent_exact_distance_scores(order, 3) == expected_scores
        assert _independent_closing_distance_scores(order, 3) == expected_closing


def test_residue_one_construction_is_uniform_and_exact() -> None:
    for k in range(2, 1001):
        n = 5 * k + 1
        vertex_count = n - 1
        terminal_start = 4 * k + 2
        threshold = terminal_high_incidence_closed_form(n)
        order = residue_one_product_distance_order(n)

        assert threshold == Fraction(terminal_start * terminal_start, 2)
        assert tuple(sorted(order)) == tuple(range(2, n + 1))
        local_product_maxima = tuple(
            max(
                order[position] * order[(position + distance) % vertex_count]
                for position in range(vertex_count)
            )
            for distance in (1, 2, 3)
        )
        assert local_product_maxima[0] == threshold
        assert local_product_maxima[1] == 2 * threshold - 1
        assert local_product_maxima[2] <= 3 * threshold
        assert n * (n - 1) < 4 * threshold

    assert _independent_score(residue_one_product_distance_order(11)) == (
        EXPECTED_TABLE[11][1]
    )
    for k in (3, 4, 5, 6, 7, 10, 25, 100):
        n = 5 * k + 1
        assert _independent_score(residue_one_product_distance_order(n)) == (
            terminal_high_incidence_closed_form(n)
        )


def test_residue_one_construction_validation_is_strict() -> None:
    for invalid in (True, 6, 8, 10, 12, Fraction(11), 11.0):
        with pytest.raises(
            ValueError,
            match="integer congruent to 1 modulo 5 and at least 11",
        ):
            residue_one_product_distance_order(invalid)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("k", "expected_order", "expected_scores", "expected_closing"),
    (
        (
            2,
            (11, 4, 10, 6, 9, 3, 12, 2, 7, 8, 5),
            (Fraction(60), Fraction(55), Fraction(32)),
            (Fraction(55), Fraction(44), Fraction(77, 3)),
        ),
        (
            3,
            (15, 6, 14, 8, 13, 5, 16, 4, 12, 9, 11, 3, 17, 2, 10, 7),
            (Fraction(112), Fraction(105), Fraction(51)),
            (Fraction(105), Fraction(75), Fraction(98, 3)),
        ),
    ),
)
def test_residue_two_construction_has_exact_local_scores_and_closing_arcs(
    k: int,
    expected_order: tuple[int, ...],
    expected_scores: tuple[Fraction, ...],
    expected_closing: tuple[Fraction, ...],
) -> None:
    n = 5 * k + 2
    order = residue_two_product_distance_order(n)

    assert order == expected_order
    assert tuple(sorted(order)) == tuple(range(2, n + 1))
    assert _independent_exact_distance_scores(order, 3) == expected_scores
    assert _independent_closing_distance_scores(order, 3) == expected_closing


@pytest.mark.parametrize("parity", (0, 1))
def test_residue_two_construction_symbolic_parity_branches(parity: int) -> None:
    first_k = 2 if parity == 0 else 3
    for k in range(first_k, 1001, 2):
        n = 5 * k + 2
        d = 4 * k + 4
        terminal_start = d - 1
        triple_count = (k + 1) // 2
        residual_end = terminal_start - 2 * triple_count - 1
        threshold = Fraction(d * (d - 2), 2)
        order = residue_two_product_distance_order(n)

        assert tuple(sorted(order)) == tuple(range(2, n + 1))
        expected_distance_three_product = (
            (terminal_start + triple_count) * (2 * k + triple_count + 3)
            if parity == 0
            else (terminal_start + triple_count) * (2 * k + triple_count + 1)
        )
        assert _independent_exact_distance_scores(order, 3) == (
            threshold,
            Fraction(terminal_start * (terminal_start - 1), 2),
            Fraction(expected_distance_three_product, 3),
        )
        closing_third_product = (
            77
            if k == 2
            else (2 * k + 1) * (terminal_start - 1)
        )
        assert _independent_closing_distance_scores(order, 3) == (
            Fraction(terminal_start * (2 * k + 1)),
            Fraction(terminal_start * residual_end, 2),
            Fraction(closing_third_product, 3),
        )
        assert 4 * threshold - n * (n - 1) == 7 * k * k + 33 * k + 14
        assert 7 * k * k + 33 * k + 14 > 0


def test_residue_two_construction_two_independent_all_pairs_scorers() -> None:
    for k in (2, 3, 4, 5, 10, 11, 25, 26, 100, 101):
        n = 5 * k + 2
        d = 4 * k + 4
        threshold = Fraction(d * (d - 2), 2)
        order = residue_two_product_distance_order(n)

        assert _independent_score(order) == threshold
        assert _independent_label_first_score(order) == threshold
        assert product_distance_score(order) == threshold


def test_residue_two_construction_validation_is_strict() -> None:
    for invalid in (True, 7, 8, 11, 13, Fraction(12), 12.0):
        with pytest.raises(
            ValueError,
            match="integer congruent to 2 modulo 5 and at least 12",
        ):
            residue_two_product_distance_order(invalid)  # type: ignore[arg-type]


def test_fraction_comparisons_do_not_use_float_rounding() -> None:
    pair_scores = product_distance_pair_scores((9, 2, 6, 5, 7, 4, 8, 3))
    by_indices = {
        frozenset((pair.left_index, pair.right_index)): pair.ratio
        for pair in pair_scores
    }

    assert by_indices[frozenset((7, 9))] == Fraction(63, 4)
    assert by_indices[frozenset((8, 9))] > by_indices[frozenset((5, 7))]
    assert Fraction(63, 4) < Fraction(16) < Fraction(49, 3)
    assert product_distance_score((6, 2, 4, 5, 3)) < product_distance_score(
        (6, 2, 5, 3, 4)
    )


def test_circular_position_distance_exact_values_and_validation() -> None:
    assert circular_position_distance(0, 1, 8) == 1
    assert circular_position_distance(0, 7, 8) == 1
    assert circular_position_distance(0, 4, 8) == 4

    with pytest.raises(ValueError):
        circular_position_distance(2, 2, 8)
    with pytest.raises(ValueError):
        circular_position_distance(0, 8, 8)


def test_canonical_counts_and_rotation_reflection_convention(
    exact_enumerations,
) -> None:
    expected_counts = (1, 1, 3, 12, 60, 360, 2520, 20160, 181440)
    assert MAX_CANONICAL_ORDERS == expected_counts[-1]

    for n, expected_count in zip(range(3, 12), expected_counts, strict=True):
        assert canonical_core_order_count(n) == expected_count
        assert exact_enumerations[n].canonical_order_count == expected_count

    assert tuple(canonical_core_orders(3)) == ((3, 2),)
    for n in range(4, 9):
        orders = tuple(canonical_core_orders(n))
        assert len(orders) == canonical_core_order_count(n)
        assert len(set(orders)) == len(orders)
        for order in orders:
            assert order[0] == n
            assert order[1] < order[-1]
            assert canonicalize_core_order(order) == order

    base = (8, 2, 5, 6, 4, 7, 3)
    rotated = base[3:] + base[:3]
    reflected = tuple(reversed(base))
    assert canonicalize_core_order(base) == base
    assert canonicalize_core_order(rotated) == base
    assert canonicalize_core_order(reflected) == base
    assert canonicalize_core_order((2, 3)) == (3, 2)


def test_independent_full_permutation_check_for_smallest_cases(
    exact_enumerations,
) -> None:
    for n in range(3, 7):
        scored = [
            (_independent_score(order), order)
            for order in itertools.permutations(range(2, n + 1))
        ]
        optimum = min(score for score, _order in scored)
        canonical_minimizers = {
            _independent_canonicalize(order)
            for score, order in scored
            if score == optimum
        }
        result = exact_enumerations[n]

        assert result.optimum == optimum
        assert result.minimizer_count == len(canonical_minimizers)
        assert result.representative == min(canonical_minimizers)


def test_tail_obstruction_and_zigzag_comparisons_are_exact(
    exact_enumerations,
) -> None:
    assert best_tail_lower_obstruction(3) == (None, ())
    for n in range(4, 12):
        result = exact_enumerations[n]
        direct_values = {
            m: Fraction(
                sum(k * (m + n - k) for k in range(m, n + 1)),
                n - 1,
            )
            for m in range(2, n - 1)
        }
        direct_best = max(direct_values.values())

        assert result.tail_lower_obstruction == direct_best
        assert result.tail_maximizers == tuple(
            m for m, value in direct_values.items() if value == direct_best
        )
        assert result.optimum >= direct_best
        assert result.zigzag_score == Fraction(n * (n // 2 + 1))
        assert result.optimum <= result.zigzag_score
        for m in range(2, n - 1):
            assert tail_pairing_sum(m, n) == sum(
                k * (m + n - k) for k in range(m, n + 1)
            )


def test_tail_obstruction_first_dominates_adjacent_formula_at_33() -> None:
    for n in range(4, 33):
        obstruction, _maximizers = best_tail_lower_obstruction(n)
        assert obstruction is not None
        assert obstruction <= adjacent_product_optimum(n)

    assert adjacent_product_optimum(33) == 323
    assert best_tail_lower_obstruction(33) == (Fraction(2595, 8), (14,))

    # This checks the explicit all-n witness used in the symbolic residue proof;
    # it is formula evaluation, not cyclic-order enumeration.
    for n in range(33, 1001):
        tail_start = (2 * n + 4) // 5
        witness = Fraction(tail_pairing_sum(tail_start, n), n - 1)
        assert witness > adjacent_product_optimum(n)


def test_exact_enumeration_reproduces_reported_table(exact_enumerations) -> None:
    for n, expected in EXPECTED_TABLE.items():
        result = exact_enumerations[n]
        observed = (
            result.canonical_order_count,
            result.optimum,
            result.minimizer_count,
            result.representative,
            result.zigzag_score,
            result.tail_lower_obstruction,
            result.tail_maximizers,
        )
        assert observed == expected


def test_truncated_enumeration_reproduces_exact_table_and_first_gap(
    exact_enumerations,
    exact_truncated_enumerations,
) -> None:
    for n, expected in EXPECTED_TRUNCATED_TABLE.items():
        adjacent = exact_truncated_enumerations[n, 1]
        distance_two = exact_truncated_enumerations[n, 2]
        observed = (
            adjacent.optimum,
            adjacent.minimizer_count,
            adjacent.representative,
            distance_two.optimum,
            distance_two.minimizer_count,
            distance_two.representative,
        )

        assert observed == expected
        assert adjacent.canonical_order_count == canonical_core_order_count(n)
        assert adjacent.optimum == adjacent_product_optimum(n)
        assert distance_two.canonical_order_count == canonical_core_order_count(n)
        assert distance_two.optimum == exact_enumerations[n].optimum
        assert distance_two.minimizer_count == exact_enumerations[n].minimizer_count
        assert distance_two.representative == exact_enumerations[n].representative

    assert [
        n
        for n in range(3, 12)
        if exact_truncated_enumerations[n, 1].optimum
        < exact_enumerations[n].optimum
    ] == [9, 10, 11]
    assert all(
        exact_truncated_enumerations[n, 2].optimum
        == exact_enumerations[n].optimum
        for n in range(3, 12)
    )


def test_enumeration_is_deterministically_bounded() -> None:
    with pytest.raises(ValueError, match=r"\[3, 11\]"):
        enumerate_product_distance(12)
    with pytest.raises(ValueError, match="requires 181440 orders"):
        enumerate_product_distance(11, max_canonical_orders=181439)
    with pytest.raises(ValueError, match="positive integer"):
        enumerate_product_distance(5, max_canonical_orders=True)
    with pytest.raises(ValueError, match=r"\[3, 11\]"):
        enumerate_truncated_product_distance(12, 2)
    with pytest.raises(ValueError, match="requires 181440 orders"):
        enumerate_truncated_product_distance(
            11,
            2,
            max_canonical_orders=181439,
        )
    with pytest.raises(ValueError, match="max_position_distance"):
        enumerate_truncated_product_distance(5, True)


def test_core_order_validation_rejects_wrong_domain() -> None:
    with pytest.raises(ValueError):
        product_distance_score((4, 2, 2))
    with pytest.raises(ValueError):
        product_distance_score((4, 1, 3))
    with pytest.raises(ValueError):
        canonicalize_core_order((3,))
