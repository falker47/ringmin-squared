"""Exact product-distance surrogate for regular-direction core orders.

The bounded enumeration in this module is deliberately limited to
``3 <= n <= 11``.  It uses integer cross-products internally and exposes
scores as :class:`fractions.Fraction`; no floating-point arithmetic is used.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from fractions import Fraction
import itertools
import math

from power_ringmin.patterns import zigzag


MIN_ENUMERATION_N = 3
MAX_ENUMERATION_N = 11
MAX_CANONICAL_ORDERS = math.factorial(MAX_ENUMERATION_N - 2) // 2


@dataclass(frozen=True)
class ProductDistancePairScore:
    """Exact score contribution of one unordered pair in a core order."""

    left_position: int
    right_position: int
    left_index: int
    right_index: int
    distance: int
    ratio: Fraction


@dataclass(frozen=True)
class ProductDistanceEnumeration:
    """Exact result of one bounded canonical enumeration."""

    n: int
    canonical_order_count: int
    optimum: Fraction
    minimizer_count: int
    representative: tuple[int, ...]
    zigzag_order: tuple[int, ...]
    zigzag_score: Fraction
    tail_lower_obstruction: Fraction | None
    tail_maximizers: tuple[int, ...]


def circular_position_distance(
    left_position: int,
    right_position: int,
    vertex_count: int,
) -> int:
    """Return the smaller circular distance between two distinct positions."""
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int):
        raise ValueError(f"vertex_count must be an integer, got {vertex_count!r}")
    if vertex_count < 2:
        raise ValueError(f"vertex_count must be at least 2, got {vertex_count!r}")
    for name, position in (
        ("left_position", left_position),
        ("right_position", right_position),
    ):
        if isinstance(position, bool) or not isinstance(position, int):
            raise ValueError(f"{name} must be an integer, got {position!r}")
        if not 0 <= position < vertex_count:
            raise ValueError(
                f"{name} must lie in [0, {vertex_count}), got {position!r}"
            )
    if left_position == right_position:
        raise ValueError("positions must be distinct")

    forward = abs(right_position - left_position)
    return min(forward, vertex_count - forward)


def product_distance_pair_scores(
    order: Sequence[int],
) -> tuple[ProductDistancePairScore, ...]:
    """Return exact ``ij / d_sigma(i,j)`` values for every unordered pair."""
    core_order = _normalize_core_order(order)
    pairs: list[ProductDistancePairScore] = []
    for left, right, distance in _position_pairs(len(core_order)):
        left_index = core_order[left]
        right_index = core_order[right]
        pairs.append(
            ProductDistancePairScore(
                left_position=left,
                right_position=right,
                left_index=left_index,
                right_index=right_index,
                distance=distance,
                ratio=Fraction(left_index * right_index, distance),
            )
        )
    return tuple(pairs)


def product_distance_score(order: Sequence[int]) -> Fraction:
    """Return ``W(sigma) = max_{i<j} ij / d_sigma(i,j)`` exactly."""
    core_order = _normalize_core_order(order)
    numerator, denominator = _score_without_cutoff(
        core_order,
        _position_pairs(len(core_order)),
    )
    return Fraction(numerator, denominator)


def canonicalize_core_order(order: Sequence[int]) -> tuple[int, ...]:
    """Canonicalize a core cycle modulo rotation and reflection.

    The largest index is fixed first.  For cores of at least three elements,
    the retained orientation has its second index smaller than its last.  The
    two-element core for ``n=3`` is handled separately.
    """
    core_order = _normalize_core_order(order)
    n = len(core_order) + 1
    forward = _rotate_to_front(core_order, n)
    if len(core_order) == 2:
        return forward
    backward = _rotate_to_front(tuple(reversed(core_order)), n)
    return forward if forward[1] < forward[-1] else backward


def canonical_core_order_count(n: int) -> int:
    """Return the bounded core-cycle count modulo rotation and reflection."""
    _validate_enumeration_n(n)
    if n == 3:
        return 1
    return math.factorial(n - 2) // 2


def canonical_core_orders(n: int) -> Iterator[tuple[int, ...]]:
    """Yield every bounded canonical core order exactly once."""
    _validate_enumeration_n(n)
    if n == 3:
        yield (3, 2)
        return

    for tail in itertools.permutations(range(2, n)):
        order = (n, *tail)
        if order[1] < order[-1]:
            yield order


def tail_pairing_sum(m: int, n: int) -> int:
    """Return ``P_{m,n} = sum(k * (m+n-k), k=m..n)`` exactly."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (m, n)):
        raise ValueError(f"m and n must be integers, got m={m!r}, n={n!r}")
    if n < 4 or not 2 <= m <= n - 2:
        raise ValueError(f"expected n >= 4 and 2 <= m <= n-2, got m={m}, n={n}")
    return sum(k * (m + n - k) for k in range(m, n + 1))


def best_tail_lower_obstruction(n: int) -> tuple[Fraction | None, tuple[int, ...]]:
    """Return ``max_m P_{m,n}/(n-1)`` and all maximizing tail starts."""
    _validate_problem_n(n)
    if n == 3:
        return None, ()

    values = tuple(
        (Fraction(tail_pairing_sum(m, n), n - 1), m)
        for m in range(2, n - 1)
    )
    best = max(value for value, _m in values)
    return best, tuple(m for value, m in values if value == best)


def enumerate_product_distance(
    n: int,
    *,
    max_canonical_orders: int = MAX_CANONICAL_ORDERS,
) -> ProductDistanceEnumeration:
    """Determine ``W_n`` by exact bounded canonical enumeration.

    The deterministic work ceiling is checked before permutation generation.
    A strict cutoff is used while scoring: an order is abandoned only after a
    pair score is proved greater than the current incumbent, so exact ties are
    retained.
    """
    _validate_enumeration_n(n)
    if (
        isinstance(max_canonical_orders, bool)
        or not isinstance(max_canonical_orders, int)
        or max_canonical_orders < 1
    ):
        raise ValueError(
            "max_canonical_orders must be a positive integer, "
            f"got {max_canonical_orders!r}"
        )

    expected_count = canonical_core_order_count(n)
    if expected_count > max_canonical_orders:
        raise ValueError(
            f"canonical enumeration for n={n} requires {expected_count} orders, "
            f"exceeding max_canonical_orders={max_canonical_orders}"
        )

    raw_zigzag = tuple(int(value) for value in zigzag(range(2, n + 1)))
    zigzag_order = canonicalize_core_order(raw_zigzag)
    best = product_distance_score(zigzag_order)
    representative = zigzag_order
    minimizer_count = 0
    enumerated_count = 0
    position_pairs = _position_pairs(n - 1)

    for order in canonical_core_orders(n):
        enumerated_count += 1
        raw_score = _score_with_cutoff(
            order,
            position_pairs,
            cutoff_numerator=best.numerator,
            cutoff_denominator=best.denominator,
        )
        if raw_score is None:
            continue

        numerator, denominator = raw_score
        comparison = numerator * best.denominator - best.numerator * denominator
        if comparison < 0:
            best = Fraction(numerator, denominator)
            minimizer_count = 1
            representative = order
        elif comparison == 0:
            minimizer_count += 1
            if order < representative:
                representative = order

    if enumerated_count != expected_count:
        raise AssertionError(
            f"canonical enumeration count mismatch for n={n}: "
            f"expected {expected_count}, got {enumerated_count}"
        )
    if minimizer_count < 1:
        raise AssertionError(f"enumeration found no minimizer for n={n}")

    tail_obstruction, tail_maximizers = best_tail_lower_obstruction(n)
    return ProductDistanceEnumeration(
        n=n,
        canonical_order_count=enumerated_count,
        optimum=best,
        minimizer_count=minimizer_count,
        representative=representative,
        zigzag_order=zigzag_order,
        zigzag_score=product_distance_score(zigzag_order),
        tail_lower_obstruction=tail_obstruction,
        tail_maximizers=tail_maximizers,
    )


def _normalize_core_order(order: Sequence[int]) -> tuple[int, ...]:
    values = tuple(order)
    if len(values) < 2:
        raise ValueError("a core order must contain at least two indices")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError(f"core indices must be integers: {values!r}")

    n = len(values) + 1
    expected = tuple(range(2, n + 1))
    if tuple(sorted(values)) != expected:
        raise ValueError(
            f"core order must be a permutation of {expected!r}, got {values!r}"
        )
    return values


def _validate_enumeration_n(n: int) -> None:
    if (
        isinstance(n, bool)
        or not isinstance(n, int)
        or not MIN_ENUMERATION_N <= n <= MAX_ENUMERATION_N
    ):
        raise ValueError(
            f"bounded enumeration requires an integer n in "
            f"[{MIN_ENUMERATION_N}, {MAX_ENUMERATION_N}], got {n!r}"
        )


def _validate_problem_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError(f"n must be an integer at least 3, got {n!r}")


def _rotate_to_front(order: tuple[int, ...], value: int) -> tuple[int, ...]:
    index = order.index(value)
    return order[index:] + order[:index]


def _position_pairs(vertex_count: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (
            left,
            right,
            min(right - left, vertex_count - (right - left)),
        )
        for left in range(vertex_count)
        for right in range(left + 1, vertex_count)
    )


def _score_without_cutoff(
    order: tuple[int, ...],
    position_pairs: tuple[tuple[int, int, int], ...],
) -> tuple[int, int]:
    best_numerator = 0
    best_denominator = 1
    for left, right, distance in position_pairs:
        numerator = order[left] * order[right]
        if numerator * best_denominator > best_numerator * distance:
            best_numerator = numerator
            best_denominator = distance
    return best_numerator, best_denominator


def _score_with_cutoff(
    order: tuple[int, ...],
    position_pairs: tuple[tuple[int, int, int], ...],
    *,
    cutoff_numerator: int,
    cutoff_denominator: int,
) -> tuple[int, int] | None:
    best_numerator = 0
    best_denominator = 1
    for left, right, distance in position_pairs:
        numerator = order[left] * order[right]
        if numerator * cutoff_denominator > cutoff_numerator * distance:
            return None
        if numerator * best_denominator > best_numerator * distance:
            best_numerator = numerator
            best_denominator = distance
    return best_numerator, best_denominator


__all__ = [
    "MAX_CANONICAL_ORDERS",
    "MAX_ENUMERATION_N",
    "MIN_ENUMERATION_N",
    "ProductDistanceEnumeration",
    "ProductDistancePairScore",
    "best_tail_lower_obstruction",
    "canonical_core_order_count",
    "canonical_core_orders",
    "canonicalize_core_order",
    "circular_position_distance",
    "enumerate_product_distance",
    "product_distance_pair_scores",
    "product_distance_score",
    "tail_pairing_sum",
]
