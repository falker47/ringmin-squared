from __future__ import annotations

from fractions import Fraction
import itertools

import pytest

import power_ringmin.fixed_order_cycle_ratio as cycle_ratio_module
from power_ringmin.fixed_order_cycle_ratio import (
    MAX_CANONICAL_ORDERS,
    enumerate_fixed_order_cycle_ratio,
    fixed_order_cycle_ratio_score,
)
from power_ringmin.product_distance import product_distance_score
from power_ringmin.search_small_n import (
    canonical_index_order_count,
    canonical_index_orders,
)


def _simple_cycle_ratio_oracle(order: tuple[int, ...]) -> Fraction:
    """Enumerate simple directed cycles directly for small test instances."""
    best: Fraction | None = None
    for cycle_length in range(2, len(order) + 1):
        for vertices in itertools.combinations(range(len(order)), cycle_length):
            anchor = vertices[0]
            for tail in itertools.permutations(vertices[1:]):
                cycle = (anchor, *tail)
                score_sum = 0
                wrap_count = 0
                for position, left in enumerate(cycle):
                    right = cycle[(position + 1) % cycle_length]
                    score_sum += order[left] * order[right]
                    wrap_count += int(left < right)

                assert wrap_count >= 1
                ratio = Fraction(score_sum, wrap_count)
                if best is None or ratio > best:
                    best = ratio

    assert best is not None
    return best


def test_two_cycle_counts_both_edge_occurrences() -> None:
    score = fixed_order_cycle_ratio_score((3, 1, 2))

    assert isinstance(score, Fraction)
    assert score == Fraction(2 * 3 * 2, 1) == 12


def test_production_scorer_matches_independent_simple_cycle_oracle_n3_to_n6() -> None:
    checked_order_count = 0
    for n in range(3, 7):
        for order in canonical_index_orders(n):
            assert fixed_order_cycle_ratio_score(order) == _simple_cycle_ratio_oracle(
                order
            )
            checked_order_count += 1

    assert checked_order_count == 76


def test_score_is_invariant_under_rotation_and_reflection() -> None:
    order = (6, 1, 2, 4, 5, 3)
    rotated = order[2:] + order[:2]
    reflected = tuple(reversed(order))

    assert fixed_order_cycle_ratio_score(order) == 77
    assert fixed_order_cycle_ratio_score(rotated) == 77
    assert fixed_order_cycle_ratio_score(reflected) == 77


def test_bounded_enumeration_reproduces_n3_to_n8_prediction() -> None:
    expected = {
        3: (12, 1, (3, 1, 2)),
        4: (26, 3, (4, 1, 2, 3)),
        5: (47, 4, (5, 1, 2, 4, 3)),
        6: (77, 15, (6, 1, 2, 3, 5, 4)),
        7: (118, 24, (7, 1, 2, 3, 5, 6, 4)),
        8: (172, 84, (8, 1, 2, 3, 5, 6, 7, 4)),
    }

    total_orders = 0
    for n, (optimum, minimizer_count, representative) in expected.items():
        result = enumerate_fixed_order_cycle_ratio(n)

        assert result.n == n
        assert result.canonical_order_count == canonical_index_order_count(n)
        assert result.optimum == Fraction(optimum)
        assert result.minimizer_count == minimizer_count
        assert result.representative == representative
        total_orders += result.canonical_order_count

    assert total_orders == 2_956


def test_lambda_and_core_product_distance_are_distinct_scores() -> None:
    same_lambda_left = (6, 1, 2, 4, 5, 3)
    same_lambda_right = (6, 3, 5, 2, 1, 4)
    same_w_right = (6, 2, 5, 4, 1, 3)

    def induced_core(order: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(index for index in order if index != 1)

    assert fixed_order_cycle_ratio_score(same_lambda_left) == 77
    assert fixed_order_cycle_ratio_score(same_lambda_right) == 77
    assert product_distance_score(induced_core(same_lambda_left)) == 20
    assert product_distance_score(induced_core(same_lambda_right)) == 24

    assert fixed_order_cycle_ratio_score(same_w_right) == 80
    assert product_distance_score(induced_core(same_w_right)) == 20


@pytest.mark.parametrize(
    "order",
    [
        (),
        (1, 2),
        (1, 2, 2),
        (1, 2, 4),
        (1, 2, True),
        (1, 2, 3.0),
    ],
)
def test_scorer_rejects_invalid_complete_orders(order: tuple[object, ...]) -> None:
    with pytest.raises(ValueError):
        fixed_order_cycle_ratio_score(order)  # type: ignore[arg-type]


@pytest.mark.parametrize("n", [2, 9, True, 4.0])
def test_bounded_enumerator_rejects_values_outside_hard_domain(n: object) -> None:
    with pytest.raises(ValueError, match="3 <= n <= 8"):
        enumerate_fixed_order_cycle_ratio(n)  # type: ignore[arg-type]


@pytest.mark.parametrize("ceiling", [0, -1, True, 1.0])
def test_bounded_enumerator_validates_work_ceiling(ceiling: object) -> None:
    with pytest.raises(ValueError, match="positive integer"):
        enumerate_fixed_order_cycle_ratio(3, max_canonical_orders=ceiling)  # type: ignore[arg-type]


def test_bounded_enumerator_checks_work_before_permutations() -> None:
    assert MAX_CANONICAL_ORDERS == 2_520
    with pytest.raises(ValueError, match="requires 2520 orders"):
        enumerate_fixed_order_cycle_ratio(8, max_canonical_orders=2_519)


def test_domain_and_work_rejections_precede_permutation_generation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_if_called(_n: int) -> None:
        raise AssertionError("canonical order generation must not start")

    monkeypatch.setattr(
        cycle_ratio_module,
        "canonical_index_orders",
        fail_if_called,
    )

    with pytest.raises(ValueError, match="3 <= n <= 8"):
        enumerate_fixed_order_cycle_ratio(9)
    with pytest.raises(ValueError, match="requires 2520 orders"):
        enumerate_fixed_order_cycle_ratio(8, max_canonical_orders=2_519)
