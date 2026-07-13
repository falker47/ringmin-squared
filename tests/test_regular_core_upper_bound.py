from __future__ import annotations

import math

import pytest

from power_ringmin.geometry import TAU, theta


def _regular_core_upper_bound(n: int) -> float:
    lower = (n - 1) ** 2
    upper = n**2
    half_edge_angle = math.pi / (n - 1)
    return math.sqrt(
        lower * upper / math.sin(half_edge_angle) ** 2
        + (2 * n - 1) ** 2 / 4
    ) - (lower + upper) / 2


def test_regular_core_closed_formula_solves_tight_pair_equation() -> None:
    for n in (12, 13, 25, 50, 100, 250):
        lower = (n - 1) ** 2
        upper = n**2
        half_edge_angle = math.pi / (n - 1)
        radius = _regular_core_upper_bound(n)

        assert radius > 0
        assert (radius + lower) * (radius + upper) == pytest.approx(
            lower * upper / math.sin(half_edge_angle) ** 2,
            rel=1e-14,
        )
        assert theta(radius, lower, upper) == pytest.approx(
            2 * half_edge_angle,
            rel=1e-14,
            abs=2e-15,
        )


def test_largest_core_separation_is_top_two_radii_on_finite_grid() -> None:
    for n in (12, 13, 25, 50):
        upper_bound = _regular_core_upper_bound(n)
        for radius in (1.0, upper_bound, 10 * upper_bound):
            values = {
                (i, j): theta(radius, i * i, j * j)
                for i in range(2, n + 1)
                for j in range(i + 1, n + 1)
            }
            maximum = max(values.values())
            maximizers = {pair for pair, value in values.items() if value == maximum}

            assert maximizers == {(n - 1, n)}
            assert all(value <= values[n - 1, n] for value in values.values())


def test_regular_core_is_all_pairs_feasible_on_finite_samples() -> None:
    for n in (12, 13, 25, 50, 100):
        vertex_count = n - 1
        radius = _regular_core_upper_bound(n)
        total_pairs = 0
        adjacent_pairs = 0
        nonadjacent_slacks: list[float] = []

        for left in range(vertex_count):
            for right in range(left + 1, vertex_count):
                index_left = left + 2
                index_right = right + 2
                raw_step = right - left
                step = min(raw_step, vertex_count - raw_step)
                available = TAU * step / vertex_count
                required = theta(
                    radius,
                    index_left * index_left,
                    index_right * index_right,
                )

                assert required <= available + 1e-14
                total_pairs += 1
                if step == 1:
                    adjacent_pairs += 1
                else:
                    nonadjacent_slacks.append(available - required)

        expected_pairs = vertex_count * (vertex_count - 1) // 2
        assert total_pairs == expected_pairs
        assert adjacent_pairs == vertex_count
        assert len(nonadjacent_slacks) == expected_pairs - vertex_count
        assert min(nonadjacent_slacks) > 0
