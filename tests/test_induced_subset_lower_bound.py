from __future__ import annotations

import itertools
import math


def _p_direct(m: int, n: int) -> int:
    return sum(k * (m + n - k) for k in range(m, n + 1))


def _p_closed(m: int, n: int) -> int:
    numerator = (n - m + 1) * (m * m + 4 * m * n + m + n * n - n)
    assert numerator % 6 == 0
    return numerator // 6


def _duplicated_pairing_bound(indices: tuple[int, ...]) -> int:
    doubled = sorted([index for index in indices for _ in range(2)])
    q = len(indices)
    return sum(doubled[i] * doubled[2 * q - 1 - i] for i in range(q))


def _cyclic_product_sum(order: tuple[int, ...]) -> int:
    return sum(order[i] * order[(i + 1) % len(order)] for i in range(len(order)))


def test_consecutive_subset_pairing_formula_matches_direct_sum() -> None:
    for n in range(3, 80):
        for m in range(1, n + 1):
            assert _p_closed(m, n) == _p_direct(m, n)


def test_discrete_maximum_over_consecutive_subsets_tracks_sqrt2_minus_one() -> None:
    alpha = math.sqrt(2.0) - 1.0

    for n in range(4, 121):
        values = [(_p_closed(m, n), m) for m in range(1, n - 1)]
        maximum = max(value for value, _m in values)
        maximizing_m = {m for value, m in values if value == maximum}

        rounded_candidates = {
            candidate
            for candidate in (math.ceil(alpha * n), math.ceil(alpha * n) + 1)
            if 1 <= candidate <= n - 2
        }

        assert maximizing_m <= rounded_candidates
        assert maximum == max(_p_closed(m, n) for m in rounded_candidates)


def test_pairing_bound_on_nonconsecutive_subset_cyclic_orders() -> None:
    subsets = (
        (1, 3, 4),
        (1, 3, 5, 8),
        (2, 4, 7, 9, 10),
        (1, 4, 6, 8, 11, 13),
    )

    for subset in subsets:
        lower_bound = _duplicated_pairing_bound(subset)

        for order in itertools.permutations(subset):
            assert _cyclic_product_sum(order) >= lower_bound


def test_pairing_bound_on_induced_orders_from_larger_cycles() -> None:
    full_cycles = (
        (9, 1, 5, 2, 8, 3, 7, 4, 6),
        (12, 3, 10, 1, 8, 5, 11, 2, 7, 4, 9, 6),
        (14, 2, 11, 5, 9, 1, 13, 4, 8, 6, 12, 3, 10, 7),
    )
    subsets = (
        (1, 4, 7, 9),
        (2, 5, 8, 11, 12),
        (3, 6, 10, 13, 14),
    )

    for full_cycle in full_cycles:
        full_set = set(full_cycle)
        for subset in subsets:
            if not set(subset) <= full_set:
                continue

            induced_order = tuple(index for index in full_cycle if index in subset)
            lower_bound = _duplicated_pairing_bound(subset)
            assert _cyclic_product_sum(induced_order) >= lower_bound
