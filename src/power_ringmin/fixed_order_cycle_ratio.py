"""Exact maximum cyclic-ratio scoring for complete fixed-order STNs.

For a complete quadratic index order ``sigma``, every directed STN edge
``u -> v`` contributes the index product ``sigma[u] * sigma[v]``.  Its
resource contribution is one when ``u < v`` (a ``wrap_upper`` edge) and zero
when ``u > v`` (a ``forward_lower`` edge).  The score is

``Lambda(sigma) = max_C S(C) / q(C)``.

The production algorithm does not enumerate cycles.  It first closes the
acyclic graph of resource-zero descending edges, compresses one resource-one
edge followed by a descending path into a macro edge, and then applies Karp's
maximum-cycle-mean dynamic program to the complete macro graph.  All path
weights are integers; :class:`fractions.Fraction` is used for the exact ratio
comparisons and public result.

The bounded global enumeration in this module has a deliberate hard domain
``3 <= n <= 8`` and checks its work ceiling before generating permutations.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
import math

from power_ringmin.search_small_n import (
    canonical_index_order_count,
    canonical_index_orders,
)


MIN_ENUMERATION_N = 3
MAX_ENUMERATION_N = 8
MAX_CANONICAL_ORDERS = math.factorial(MAX_ENUMERATION_N - 1) // 2


@dataclass(frozen=True)
class FixedOrderCycleRatioEnumeration:
    """Exact result of one bounded canonical full-order enumeration."""

    n: int
    canonical_order_count: int
    optimum: Fraction
    minimizer_count: int
    representative: tuple[int, ...]


def fixed_order_cycle_ratio_score(order: Sequence[int]) -> Fraction:
    """Return ``Lambda(sigma) = max_C S(C) / q(C)`` exactly.

    ``C`` ranges over nontrivial directed cycles of the complete fixed-order
    STN.  Every traversed edge contributes its endpoint-index product to
    ``S(C)``, including multiplicity.  ``q(C)`` counts traversed
    ``wrap_upper`` edges.  In particular, a two-cycle traverses its unordered
    pair twice in ``S`` and has ``q = 1``.

    The input must be a permutation of ``1, ..., n`` with ``n >= 3``.  It
    need not already be canonical.  The algorithm is float-free, takes
    ``O(n^3)`` exact integer operations, and uses ``O(n^2)`` memory.
    """
    index_order = _normalize_complete_order(order)
    descending_scores = _maximum_descending_path_scores(index_order)
    macro_weights = _one_wrap_macro_weights(index_order, descending_scores)
    return _karp_maximum_cycle_mean(macro_weights)


def enumerate_fixed_order_cycle_ratio(
    n: int,
    *,
    max_canonical_orders: int = MAX_CANONICAL_ORDERS,
) -> FixedOrderCycleRatioEnumeration:
    """Minimize the exact cyclic-ratio score over canonical full orders.

    Rotation is removed by fixing ``n`` first, and reflection is removed by
    retaining the orientation whose second label is smaller than its last.
    The hard ``n <= 8`` boundary and caller-supplied work ceiling are checked
    before permutation generation.
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

    expected_count = canonical_index_order_count(n)
    if expected_count > max_canonical_orders:
        raise ValueError(
            f"canonical enumeration for n={n} requires {expected_count} orders, "
            f"exceeding max_canonical_orders={max_canonical_orders}"
        )

    optimum: Fraction | None = None
    minimizer_count = 0
    representative: tuple[int, ...] | None = None
    enumerated_count = 0

    for order in canonical_index_orders(n):
        enumerated_count += 1
        score = fixed_order_cycle_ratio_score(order)
        if optimum is None or score < optimum:
            optimum = score
            minimizer_count = 1
            representative = order
        elif score == optimum:
            minimizer_count += 1
            if representative is None or order < representative:
                representative = order

    if enumerated_count != expected_count:
        raise AssertionError(
            f"canonical enumeration count mismatch for n={n}: "
            f"expected {expected_count}, got {enumerated_count}"
        )
    if optimum is None or representative is None or minimizer_count < 1:
        raise AssertionError(f"enumeration found no minimizer for n={n}")

    return FixedOrderCycleRatioEnumeration(
        n=n,
        canonical_order_count=enumerated_count,
        optimum=optimum,
        minimizer_count=minimizer_count,
        representative=representative,
    )


def _maximum_descending_path_scores(
    order: tuple[int, ...],
) -> list[list[int | None]]:
    """Close the strictly descending, resource-zero edge DAG by max weight."""
    vertex_count = len(order)
    scores: list[list[int | None]] = [
        [None] * vertex_count for _ in range(vertex_count)
    ]
    for high in range(vertex_count):
        scores[high][high] = 0
        for low in range(high):
            candidates = []
            for next_position in range(low, high):
                suffix = scores[next_position][low]
                if suffix is None:
                    raise AssertionError("descending-path recurrence is incomplete")
                candidates.append(
                    order[high] * order[next_position] + suffix
                )
            scores[high][low] = max(candidates)
    return scores


def _one_wrap_macro_weights(
    order: tuple[int, ...],
    descending_scores: list[list[int | None]],
) -> list[list[int]]:
    """Compress one ascending edge and a possibly empty descending path."""
    macro_count = len(order) - 1
    weights: list[list[int]] = []
    for start in range(macro_count):
        row = []
        for end in range(macro_count):
            candidates = []
            first_high = max(start + 1, end)
            for high in range(first_high, len(order)):
                suffix = descending_scores[high][end]
                if suffix is None:
                    raise AssertionError("macro-edge recurrence is incomplete")
                candidates.append(order[start] * order[high] + suffix)
            row.append(max(candidates))
        weights.append(row)
    return weights


def _karp_maximum_cycle_mean(weights: list[list[int]]) -> Fraction:
    """Return the maximum cycle mean of a complete integer-weighted graph."""
    vertex_count = len(weights)
    path_scores: list[list[int | None]] = [
        [None] * vertex_count for _ in range(vertex_count + 1)
    ]
    path_scores[0][0] = 0

    for length in range(1, vertex_count + 1):
        previous = path_scores[length - 1]
        current = path_scores[length]
        for end in range(vertex_count):
            current[end] = max(
                prefix + weights[start][end]
                for start, prefix in enumerate(previous)
                if prefix is not None
            )

    vertex_bounds: list[Fraction] = []
    final_scores = path_scores[vertex_count]
    for end, final_score in enumerate(final_scores):
        if final_score is None:
            continue
        bounds = (
            Fraction(final_score - earlier_score, vertex_count - length)
            for length in range(vertex_count)
            if (earlier_score := path_scores[length][end]) is not None
        )
        vertex_bounds.append(min(bounds))

    if not vertex_bounds:
        raise AssertionError("complete macro graph has no reachable cycle")
    return max(vertex_bounds)


def _normalize_complete_order(order: Sequence[int]) -> tuple[int, ...]:
    values = tuple(order)
    if len(values) < 3:
        raise ValueError("a complete fixed order must contain at least three indices")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError(f"complete-order indices must be integers: {values!r}")

    expected = tuple(range(1, len(values) + 1))
    if tuple(sorted(values)) != expected:
        raise ValueError(
            f"complete order must be a permutation of {expected!r}, got {values!r}"
        )
    return values


def _validate_enumeration_n(n: int) -> None:
    if (
        isinstance(n, bool)
        or not isinstance(n, int)
        or not MIN_ENUMERATION_N <= n <= MAX_ENUMERATION_N
    ):
        raise ValueError(
            f"bounded cyclic-ratio enumeration requires an integer "
            f"{MIN_ENUMERATION_N} <= n <= {MAX_ENUMERATION_N}, got {n!r}"
        )


__all__ = [
    "FixedOrderCycleRatioEnumeration",
    "MAX_CANONICAL_ORDERS",
    "MAX_ENUMERATION_N",
    "MIN_ENUMERATION_N",
    "enumerate_fixed_order_cycle_ratio",
    "fixed_order_cycle_ratio_score",
]
