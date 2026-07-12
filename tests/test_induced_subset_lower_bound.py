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


def _explicit_pairing_bound(indices: tuple[int, ...]) -> int:
    q = len(indices)
    half = q // 2
    total = 2 * sum(indices[i] * indices[q - 1 - i] for i in range(half))
    if q % 2 == 1:
        total += indices[half] * indices[half]
    return total


def _cyclic_product_sum(order: tuple[int, ...]) -> int:
    return sum(order[i] * order[(i + 1) % len(order)] for i in range(len(order)))


def _p_delta(m: int, n: int) -> int:
    numerator = n * n + n - m * m - (2 * n + 1) * m
    assert numerator % 2 == 0
    return numerator // 2


def _integer_rho_floor_and_tie(n: int) -> tuple[int, bool]:
    discriminant = 8 * n * n + 8 * n + 1
    root_floor = math.isqrt(discriminant)
    rho_floor = (root_floor - (2 * n + 1)) // 2
    return rho_floor, root_floor * root_floor == discriminant


def test_consecutive_subset_pairing_formula_matches_direct_sum() -> None:
    for n in range(3, 80):
        for m in range(1, n + 1):
            assert _p_closed(m, n) == _p_direct(m, n)


def test_explicit_pairing_formula_matches_duplicated_multiset_definition() -> None:
    for n in range(1, 11):
        indices = tuple(range(1, n + 1))
        for q in range(1, n + 1):
            for subset in itertools.combinations(indices, q):
                assert _explicit_pairing_bound(subset) == _duplicated_pairing_bound(
                    subset
                )


def test_tail_subsets_are_unique_best_fixed_cardinality_pairing_bounds() -> None:
    for n in range(3, 11):
        indices = tuple(range(1, n + 1))
        for q in range(3, n + 1):
            tail = tuple(range(n - q + 1, n + 1))
            tail_bound = _duplicated_pairing_bound(tail)
            best_subsets: set[tuple[int, ...]] = set()
            best_bound = None

            for subset in itertools.combinations(indices, q):
                bound = _duplicated_pairing_bound(subset)
                if best_bound is None or bound > best_bound:
                    best_bound = bound
                    best_subsets = {subset}
                elif bound == best_bound:
                    best_subsets.add(subset)

            assert best_bound == tail_bound
            assert best_subsets == {tail}
            assert tail_bound == _p_closed(n - q + 1, n)


def test_discrete_maximum_over_tails_has_integer_rho_characterization() -> None:
    for n in range(3, 251):
        values = [(_p_closed(m, n), m) for m in range(1, n - 1)]
        maximum = max(value for value, _m in values)
        actual_maximizers = {m for value, m in values if value == maximum}

        if n == 3:
            expected_maximizers = {1}
        else:
            rho_floor, rho_is_integer = _integer_rho_floor_and_tie(n)
            expected_maximizers = (
                {rho_floor, rho_floor + 1}
                if rho_is_integer
                else {rho_floor + 1}
            )

        assert all(1 <= m <= n - 2 for m in expected_maximizers)
        assert actual_maximizers == expected_maximizers


def test_rho_tie_cases_are_exact_zero_delta_cases() -> None:
    tie_cases: list[tuple[int, int]] = []

    for n in range(4, 251):
        rho_floor, rho_is_integer = _integer_rho_floor_and_tie(n)
        if rho_is_integer:
            tie_cases.append((n, rho_floor))
            assert _p_delta(rho_floor, n) == 0
            assert _p_closed(rho_floor, n) == _p_closed(rho_floor + 1, n)
        else:
            assert _p_delta(rho_floor, n) > 0
            assert _p_delta(rho_floor + 1, n) < 0

    assert tie_cases == [(14, 6), (84, 35)]


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
