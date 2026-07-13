from __future__ import annotations

import math

from power_ringmin.geometry import TAU, theta
from power_ringmin.patterns import zigzag


def _m_n(n: int) -> int:
    return n * (n // 2 + 1)


def _v_n(n: int) -> float:
    return (n - 1) * _m_n(n) / math.pi


def _circular_step(left: int, right: int, vertex_count: int) -> int:
    forward = right - left
    return min(forward, vertex_count - forward)


def test_general_quadratic_theta_upper_bound_diagnostic_samples() -> None:
    indices = (1, 2, 3, 7, 12, 25, 100)
    for radius in (0.125, 1.0, 7.5, 100.0, 10_000.0, 1_000_000.0):
        for i in indices:
            for j in indices:
                required = theta(radius, i * i, j * j)

                assert 0.0 < required < 2 * i * j / radius


def test_zigzag_product_distance_lemma_exact_on_interval() -> None:
    for n in range(3, 257):
        order = zigzag(range(2, n + 1))
        vertex_count = n - 1
        m_n = _m_n(n)

        assert len(order) == vertex_count
        assert order[0] == n
        assert order[-1] == n // 2 + 1

        adjacent_products = tuple(
            order[position] * order[(position + 1) % vertex_count]
            for position in range(vertex_count)
        )
        assert adjacent_products[-1] == m_n
        assert max(adjacent_products) == m_n
        if n >= 4:
            assert adjacent_products.count(m_n) == 1
            assert all(product < m_n for product in adjacent_products[:-1])

        pair_count = 0
        adjacent_pair_count = 0
        nonadjacent_pair_count = 0
        for left in range(vertex_count):
            for right in range(left + 1, vertex_count):
                q = _circular_step(left, right, vertex_count)
                product = order[left] * order[right]

                assert product <= q * m_n
                pair_count += 1
                if q == 1:
                    assert product <= m_n
                    adjacent_pair_count += 1
                else:
                    assert product <= n * (n - 1) < 2 * m_n <= q * m_n
                    nonadjacent_pair_count += 1

        expected_pairs = vertex_count * (vertex_count - 1) // 2
        expected_adjacent_pairs = 1 if vertex_count == 2 else vertex_count
        assert pair_count == expected_pairs
        assert adjacent_pair_count == expected_adjacent_pairs
        assert nonadjacent_pair_count == expected_pairs - expected_adjacent_pairs


def test_zigzag_regular_directions_are_all_pairs_feasible_on_samples() -> None:
    for n in (12, 13, 24, 25, 50, 101, 250):
        order = zigzag(range(2, n + 1))
        vertex_count = n - 1
        m_n = _m_n(n)
        radius = _v_n(n)
        pair_count = 0
        adjacent_pair_count = 0
        nonadjacent_pair_count = 0

        for left in range(vertex_count):
            for right in range(left + 1, vertex_count):
                i = order[left]
                j = order[right]
                q = _circular_step(left, right, vertex_count)
                available = TAU * q / vertex_count
                required = theta(radius, i * i, j * j)

                assert i * j <= q * m_n
                assert required < 2 * i * j / radius
                assert required < available

                radius_i = i * i
                radius_j = j * j
                distance_squared = (
                    (radius_i - radius_j) ** 2
                    + 4
                    * (radius + radius_i)
                    * (radius + radius_j)
                    * math.sin(available / 2) ** 2
                )
                contact_distance_squared = (radius_i + radius_j) ** 2
                assert distance_squared > contact_distance_squared

                pair_count += 1
                if q == 1:
                    adjacent_pair_count += 1
                else:
                    nonadjacent_pair_count += 1

        expected_pairs = vertex_count * (vertex_count - 1) // 2
        assert pair_count == expected_pairs
        assert adjacent_pair_count == vertex_count
        assert nonadjacent_pair_count == expected_pairs - vertex_count
