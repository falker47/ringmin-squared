from __future__ import annotations

from fractions import Fraction
import itertools
import math

import pytest

from power_ringmin.product_distance import (
    MAX_CANONICAL_ORDERS,
    best_tail_lower_obstruction,
    canonical_core_order_count,
    canonical_core_orders,
    canonicalize_core_order,
    circular_position_distance,
    enumerate_product_distance,
    product_distance_pair_scores,
    product_distance_score,
    tail_pairing_sum,
)


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


@pytest.fixture(scope="module")
def exact_enumerations():
    return {n: enumerate_product_distance(n) for n in range(3, 12)}


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


def test_enumeration_is_deterministically_bounded() -> None:
    with pytest.raises(ValueError, match=r"\[3, 11\]"):
        enumerate_product_distance(12)
    with pytest.raises(ValueError, match="requires 181440 orders"):
        enumerate_product_distance(11, max_canonical_orders=181439)
    with pytest.raises(ValueError, match="positive integer"):
        enumerate_product_distance(5, max_canonical_orders=True)


def test_core_order_validation_rejects_wrong_domain() -> None:
    with pytest.raises(ValueError):
        product_distance_score((4, 2, 2))
    with pytest.raises(ValueError):
        product_distance_score((4, 1, 3))
    with pytest.raises(ValueError):
        canonicalize_core_order((3,))
