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
    enumerate_product_distance,
    enumerate_truncated_product_distance,
    product_distance_pair_scores,
    product_distance_score,
    tail_cycle_incompatibility_minimum,
    tail_pairing_sum,
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
    vertex_count = len(order)
    ratios = []
    for left in range(vertex_count):
        for right in range(left + 1, vertex_count):
            step = right - left
            distance = min(step, vertex_count - step)
            ratios.append(Fraction(order[left] * order[right], distance))
    return max(ratios)


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
        t = n // 2
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
        marked_singleton.minimum_incompatibilities,
        marked_singleton.required_positions,
    ) == (4, 5, 2, 1, 0, 4)
    assert (
        marked_empty.a_threshold,
        marked_empty.b_threshold,
        marked_empty.u_size,
        marked_empty.v_size,
        marked_empty.minimum_incompatibilities,
        marked_empty.required_positions,
    ) == (4, 6, 2, 0, 0, 4)
    assert (
        first_tail_singleton.a_threshold,
        first_tail_singleton.b_threshold,
        first_tail_singleton.u_size,
        first_tail_singleton.v_size,
        first_tail_singleton.minimum_incompatibilities,
        first_tail_singleton.required_positions,
    ) == (5, 6, 1, 0, 0, 2)
    assert (
        first_tail_empty.a_threshold,
        first_tail_empty.u_size,
        first_tail_empty.v_size,
        first_tail_empty.required_positions,
    ) == (6, 0, 0, 0)

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


def test_two_threshold_finite_obstruction_and_bounded_table_are_exact(
    exact_truncated_enumerations,
) -> None:
    expected = {
        3: Fraction(6),
        4: Fraction(12),
        5: Fraction(12),
        6: Fraction(20),
        7: Fraction(21),
        8: Fraction(30),
        9: Fraction(63, 2),
        10: Fraction(42),
        11: Fraction(45),
    }

    for n, obstruction in expected.items():
        assert two_threshold_lower_obstruction(n) == obstruction
        assert two_threshold_tail_packing(
            n,
            obstruction,
        ).required_positions <= n - 1
        assert two_threshold_tail_packing(
            n,
            obstruction - Fraction(1, 2),
        ).required_positions > n - 1
        assert obstruction <= exact_truncated_enumerations[n, 2].optimum


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
