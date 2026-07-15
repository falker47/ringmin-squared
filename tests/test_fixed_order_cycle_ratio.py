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
from power_ringmin.product_distance import (
    canonical_core_order_count,
    canonical_core_orders,
    product_distance_score,
)
from power_ringmin.search_small_n import (
    canonical_index_order_count,
    canonical_index_orders,
    canonicalize_index_order,
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


def _subset_path_cycle_ratio_oracle(order: tuple[int, ...]) -> Fraction:
    """Score all simple cycles by an exact subset/path dynamic program.

    This test oracle shares neither descending-path compression nor the macro
    graph and Karp maximum-cycle-mean recurrence used by the production
    scorer.  Every cycle is anchored at its least position; states retain its
    visited subset, last position, and exact wrap count.
    """
    best: Fraction | None = None
    vertex_count = len(order)

    for anchor in range(vertex_count - 1):
        anchor_mask = 1 << anchor
        layer = {(anchor_mask, anchor, 0): 0}

        while layer:
            next_layer: dict[tuple[int, int, int], int] = {}
            for (mask, last, wrap_count), path_score in layer.items():
                if last != anchor:
                    assert wrap_count >= 1
                    cycle_score = path_score + order[last] * order[anchor]
                    ratio = Fraction(cycle_score, wrap_count)
                    if best is None or ratio > best:
                        best = ratio

                for next_position in range(anchor + 1, vertex_count):
                    next_bit = 1 << next_position
                    if mask & next_bit:
                        continue
                    next_mask = mask | next_bit
                    next_wrap_count = wrap_count + int(last < next_position)
                    next_score = path_score + order[last] * order[next_position]
                    key = (next_mask, next_position, next_wrap_count)
                    previous = next_layer.get(key)
                    if previous is None or next_score > previous:
                        next_layer[key] = next_score

            layer = next_layer

    assert best is not None
    return best


def _induced_subset_one_wrap_oracle(order: tuple[int, ...]) -> Fraction:
    """Maximize the cyclic adjacent-product sum over nonempty subsets.

    Singleton squares cannot attain the maximum for a complete order with
    ``n >= 3``; including them makes the all-subsets convention literal.
    """
    best = 0
    for subset_size in range(1, len(order) + 1):
        for positions in itertools.combinations(range(len(order)), subset_size):
            score = sum(
                order[left] * order[right]
                for left, right in zip(
                    positions,
                    positions[1:] + positions[:1],
                    strict=True,
                )
            )
            best = max(best, score)

    return Fraction(best)


def _insert_one_after(
    core_order: tuple[int, ...],
    left_position: int,
) -> tuple[int, ...]:
    """Insert label one in the cyclic gap after ``left_position``."""
    return (
        core_order[: left_position + 1]
        + (1,)
        + core_order[left_position + 1 :]
    )


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


def test_independent_oracles_verify_one_wrap_saturation_n3_to_n8() -> None:
    checked_order_count = 0
    for n in range(3, 9):
        row_count = 0
        for order in canonical_index_orders(n):
            full_score = _subset_path_cycle_ratio_oracle(order)
            one_wrap_score = _induced_subset_one_wrap_oracle(order)

            assert full_score == one_wrap_score
            assert fixed_order_cycle_ratio_score(order) == one_wrap_score
            row_count += 1

        assert row_count == canonical_index_order_count(n)
        checked_order_count += row_count

    assert checked_order_count == 2_956


def test_induced_subset_oracle_counts_two_element_product_twice() -> None:
    assert _induced_subset_one_wrap_oracle((3, 1, 2)) == 12


def test_index_one_elimination_is_explicit_for_n3() -> None:
    core_order = (3, 2)
    inserted_orders = tuple(
        _insert_one_after(core_order, position)
        for position in range(len(core_order))
    )

    assert _induced_subset_one_wrap_oracle(core_order) == max(
        3 * 3,
        2 * 2,
        2 * 3 * 2,
    ) == 12
    assert inserted_orders == ((3, 1, 2), (3, 2, 1))
    assert {
        canonicalize_index_order(order) for order in inserted_orders
    } == {(3, 1, 2)}
    assert {
        fixed_order_cycle_ratio_score(order) for order in inserted_orders
    } == {Fraction(12)}


def test_index_one_elimination_on_all_core_orders_and_insertions_n3_to_n8() -> None:
    expected = {
        3: (1, 2, 1, 12, 1, 1),
        4: (1, 3, 3, 26, 1, 3),
        5: (3, 12, 12, 47, 1, 4),
        6: (12, 60, 60, 77, 3, 15),
        7: (60, 360, 360, 118, 4, 24),
        8: (360, 2_520, 2_520, 172, 12, 84),
    }

    total_core_orders = 0
    total_insertion_trials = 0
    total_complete_orders = 0

    for n, row in expected.items():
        (
            expected_core_count,
            expected_insertion_count,
            expected_complete_count,
            expected_optimum,
            expected_core_minimizers,
            expected_complete_minimizers,
        ) = row
        core_scores: dict[tuple[int, ...], Fraction] = {}
        complete_scores: dict[tuple[int, ...], Fraction] = {}
        insertion_count = 0

        for core_order in canonical_core_orders(n):
            core_score = _induced_subset_one_wrap_oracle(core_order)
            core_scores[core_order] = core_score
            assert core_score <= (n - 1) * product_distance_score(core_order)

            for left_position in range(len(core_order)):
                complete_order = _insert_one_after(core_order, left_position)
                complete_score = fixed_order_cycle_ratio_score(complete_order)
                canonical_complete_order = canonicalize_index_order(complete_order)

                assert _induced_subset_one_wrap_oracle(complete_order) == core_score
                assert complete_score == core_score
                previous = complete_scores.get(canonical_complete_order)
                if previous is not None:
                    assert previous == complete_score
                complete_scores[canonical_complete_order] = complete_score
                insertion_count += 1

        optimum = min(core_scores.values())
        assert canonical_core_order_count(n) == expected_core_count
        assert len(core_scores) == expected_core_count
        assert insertion_count == expected_insertion_count
        assert set(complete_scores) == set(canonical_index_orders(n))
        assert len(complete_scores) == canonical_index_order_count(n)
        assert len(complete_scores) == expected_complete_count
        assert optimum == expected_optimum
        assert sum(score == optimum for score in core_scores.values()) == (
            expected_core_minimizers
        )
        assert sum(score == optimum for score in complete_scores.values()) == (
            expected_complete_minimizers
        )

        total_core_orders += len(core_scores)
        total_insertion_trials += insertion_count
        total_complete_orders += len(complete_scores)

    assert total_core_orders == 437
    assert total_insertion_trials == 2_957
    assert total_complete_orders == 2_956


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
