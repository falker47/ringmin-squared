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

from power_ringmin.patterns import interleave, zigzag


MIN_ENUMERATION_N = 3
MAX_ENUMERATION_N = 11
MAX_CANONICAL_ORDERS = math.factorial(MAX_ENUMERATION_N - 2) // 2


_EIGHT_TWENTY_FIFTHS_EXCEPTIONAL_ORDERS = {
    9: (9, 2, 8, 4, 6, 5, 7, 3),
    10: (10, 2, 9, 4, 7, 6, 5, 8, 3),
    11: (11, 2, 10, 4, 8, 6, 7, 5, 9, 3),
    12: (12, 2, 11, 4, 9, 6, 7, 8, 5, 10, 3),
    14: (14, 3, 11, 2, 13, 4, 12, 6, 9, 8, 7, 10, 5),
    15: (15, 3, 12, 2, 14, 4, 13, 6, 10, 8, 9, 7, 11, 5),
    16: (16, 2, 13, 4, 15, 6, 11, 8, 9, 10, 7, 14, 5, 12, 3),
    17: (17, 5, 14, 3, 13, 2, 16, 4, 15, 6, 12, 8, 10, 9, 11, 7),
    20: (20, 2, 13, 10, 11, 12, 9, 17, 7, 16, 5, 18, 3, 15, 8, 19, 4, 14, 6),
    21: (21, 6, 15, 4, 20, 2, 16, 3, 19, 5, 17, 7, 18, 9, 13, 11, 12, 10, 14, 8),
    22: (22, 2, 16, 4, 19, 6, 20, 8, 15, 10, 13, 12, 11, 14, 9, 21, 7, 18, 5, 17, 3),
    26: (
        26,
        2,
        18,
        4,
        23,
        11,
        21,
        8,
        24,
        10,
        17,
        12,
        15,
        14,
        13,
        16,
        6,
        25,
        9,
        20,
        7,
        22,
        5,
        19,
        3,
    ),
    27: (
        27,
        2,
        18,
        4,
        24,
        6,
        22,
        8,
        20,
        10,
        23,
        12,
        16,
        14,
        15,
        13,
        17,
        11,
        25,
        9,
        21,
        7,
        26,
        5,
        19,
        3,
    ),
    32: (
        32,
        2,
        22,
        4,
        29,
        6,
        26,
        13,
        25,
        10,
        30,
        12,
        21,
        14,
        19,
        16,
        17,
        18,
        15,
        20,
        8,
        31,
        11,
        24,
        9,
        27,
        7,
        28,
        5,
        23,
        3,
    ),
}


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


@dataclass(frozen=True)
class TruncatedProductDistanceEnumeration:
    """Exact result for one bounded positional-distance truncation."""

    n: int
    max_position_distance: int
    canonical_order_count: int
    optimum: Fraction
    minimizer_count: int
    representative: tuple[int, ...]


@dataclass(frozen=True)
class AdjacentEqualityStructure:
    """Parity-specific structure of one adjacent-optimal core cycle.

    ``active_high_path`` lists the high vertices separated by the low vertices
    in ``low_neighbor_high_pairs``.  Each triple in the latter field is
    ``(low, left_high, right_high)`` in path order.
    """

    n: int
    optimum: int
    low_vertices: tuple[int, ...]
    high_vertices: tuple[int, ...]
    forced_high_high_edges: tuple[tuple[int, int], ...]
    active_high_path: tuple[int, ...]
    low_neighbor_high_pairs: tuple[tuple[int, int, int], ...]


@dataclass(frozen=True)
class TwoThresholdTailPacking:
    """Exact tail data for the distance-two cyclic packing obstruction.

    ``a_threshold`` and ``b_threshold`` are the least integers at least two
    whose consecutive products are strictly greater than ``threshold`` and
    ``2 * threshold``, respectively.  Intersecting the corresponding integer
    tails with ``{2, ..., n}`` gives sizes ``u_size`` and ``v_size``.
    ``clique_incompatibility_bound`` is the earlier independent-tail bound.
    ``minimum_incompatibilities`` is the exact minimum over cycles of the
    first tail, counting both oriented arcs when that tail has two vertices.
    ``required_positions`` is the exact proved packing requirement
    ``2*u + minimum_incompatibilities``.  ``compatible_low_capacity`` is the
    number of labels ``ell`` with ``2 <= ell < a_threshold`` and
    ``ell * b_threshold <= threshold``.
    """

    n: int
    threshold: Fraction
    a_threshold: int
    b_threshold: int
    u_size: int
    v_size: int
    compatible_low_capacity: int
    clique_incompatibility_bound: int
    minimum_incompatibilities: int
    required_positions: int


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


def truncated_product_distance_score(
    order: Sequence[int],
    max_position_distance: int,
) -> Fraction:
    """Return the exact score restricted to pairs at distance at most ``q``."""
    core_order = _normalize_core_order(order)
    _validate_max_position_distance(max_position_distance)
    numerator, denominator = _score_without_cutoff(
        core_order,
        _position_pairs_at_most(len(core_order), max_position_distance),
    )
    return Fraction(numerator, denominator)


def adjacent_product_optimum(n: int) -> int:
    """Return the exact adjacent relaxation optimum ``A_n``.

    The all-``n`` proof is recorded in
    ``research/PRODUCT_DISTANCE_SURROGATE.md``.  The exceptional two-vertex
    core has value ``A_3 = 6``.
    """
    _validate_problem_n(n)
    if n == 3:
        return 6
    return (n // 2 + 1) * ((n + 1) // 2 + 2)


def adjacent_equality_structure(
    order: Sequence[int],
) -> AdjacentEqualityStructure | None:
    """Return the exact high/low equality structure, or ``None``.

    This is the parity-specific characterization of orders attaining ``A_n``
    for ``n >= 4``.  It checks the forced high-high edges, absence of low-low
    edges, and every crossing product directly; it does not decide equality by
    calling the adjacent scorer.  The exceptional two-vertex core at ``n=3``
    is outside this simple-cycle characterization.
    """
    core_order = _normalize_core_order(order)
    n = len(core_order) + 1
    if n == 3:
        raise ValueError(
            "adjacent equality structure requires n >= 4; "
            "the n=3 core has two vertices"
        )

    t = n // 2
    optimum = adjacent_product_optimum(n)
    if n % 2 == 0:
        low_vertices = tuple(range(2, t + 1))
        high_vertices = tuple(range(t + 1, n + 1))
        forced_edges = ((t + 1, t + 2),)
        path_start = t + 1
        blocked_neighbor = t + 2
        path_end = t + 2
        path_length = len(core_order)
    else:
        low_vertices = tuple(range(2, t + 1))
        high_vertices = tuple(range(t + 1, n + 1))
        forced_edges = ((t + 1, t + 2), (t + 1, t + 3))
        path_start = t + 2
        blocked_neighbor = t + 1
        path_end = t + 3
        path_length = len(core_order) - 1

    low_set = set(low_vertices)
    high_set = set(high_vertices)
    cycle_edges = {
        tuple(
            sorted(
                (
                    core_order[position],
                    core_order[(position + 1) % len(core_order)],
                )
            )
        )
        for position in range(len(core_order))
    }
    high_high_edges = {
        edge for edge in cycle_edges if edge[0] in high_set and edge[1] in high_set
    }
    low_low_edges = {
        edge for edge in cycle_edges if edge[0] in low_set and edge[1] in low_set
    }
    crossing_edges = cycle_edges - high_high_edges - low_low_edges

    if high_high_edges != set(forced_edges) or low_low_edges:
        return None
    if any(left * right > optimum for left, right in crossing_edges):
        return None

    path = _cycle_path_away_from_neighbor(
        core_order,
        start=path_start,
        blocked_neighbor=blocked_neighbor,
        end=path_end,
        length=path_length,
    )
    if path is None:
        raise AssertionError("forced equality edges did not determine the active path")
    if any(vertex not in high_set for vertex in path[::2]):
        raise AssertionError("equality path has a non-high vertex in a high position")
    if any(vertex not in low_set for vertex in path[1::2]):
        raise AssertionError("equality path has a non-low vertex in a low position")

    active_high_path = path[::2]
    low_neighbor_high_pairs = tuple(
        (path[position], path[position - 1], path[position + 1])
        for position in range(1, len(path), 2)
    )
    return AdjacentEqualityStructure(
        n=n,
        optimum=optimum,
        low_vertices=low_vertices,
        high_vertices=high_vertices,
        forced_high_high_edges=forced_edges,
        active_high_path=active_high_path,
        low_neighbor_high_pairs=low_neighbor_high_pairs,
    )


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


def two_threshold_tail_packing(
    n: int,
    threshold: int | Fraction,
) -> TwoThresholdTailPacking:
    """Return exact ``U_T``/``V_T`` sizes and their packing requirement.

    The threshold must be a nonnegative integer or
    :class:`fractions.Fraction`; floating-point inputs are rejected.  Tail
    starts are not clamped to ``n``, so the returned sizes distinguish
    singleton and empty tails exactly.
    """
    _validate_problem_n(n)
    exact_threshold = _normalize_nonnegative_threshold(threshold)
    a_threshold = _strict_product_tail_start(exact_threshold)
    b_threshold = _strict_product_tail_start(2 * exact_threshold)
    u_size = max(0, n - a_threshold + 1)
    v_size = max(0, n - b_threshold + 1)
    compatible_low_maximum = exact_threshold.numerator // (
        exact_threshold.denominator * b_threshold
    )
    compatible_low_capacity = max(
        0,
        min(a_threshold - 1, compatible_low_maximum) - 1,
    )
    clique_incompatibility_bound = max(0, 2 * v_size - u_size)
    if u_size <= 1:
        minimum_incompatibilities = 0
    else:
        nested_correction = int(
            a_threshold < b_threshold <= n - 1
            and 2 * exact_threshold < b_threshold * b_threshold - 1
        )
        minimum_incompatibilities = max(
            0,
            2 * v_size - u_size + nested_correction,
        )
    required_positions = 2 * u_size + minimum_incompatibilities
    return TwoThresholdTailPacking(
        n=n,
        threshold=exact_threshold,
        a_threshold=a_threshold,
        b_threshold=b_threshold,
        u_size=u_size,
        v_size=v_size,
        compatible_low_capacity=compatible_low_capacity,
        clique_incompatibility_bound=clique_incompatibility_bound,
        minimum_incompatibilities=minimum_incompatibilities,
        required_positions=required_positions,
    )


def tail_cycle_incompatibility_minimum(
    n: int,
    threshold: int | Fraction,
) -> int:
    """Return the exact threshold-tail cycle incompatibility ``eta_n(T)``.

    Cycles on zero or one tail vertex contribute no distinct-vertex arc.  A
    two-vertex tail has two oriented arcs, so an incompatible pair contributes
    two.  The nested-neighborhood proof for all cardinalities is recorded in
    ``research/PRODUCT_DISTANCE_SURROGATE.md``.
    """
    return two_threshold_tail_packing(
        n,
        threshold,
    ).minimum_incompatibilities


def _two_threshold_event_thresholds(n: int) -> set[Fraction]:
    """Return the exhaustive event set for the unchanged ``Q_n``."""
    event_thresholds = {Fraction(0)}
    for k in range(2, n + 1):
        product = k * (k + 1)
        event_thresholds.add(Fraction(product, 2))
        event_thresholds.add(Fraction(product))
        event_thresholds.add(Fraction(k * k - 1, 2))
    return event_thresholds


def two_threshold_lower_obstruction(n: int) -> Fraction:
    """Return the exact finite two-threshold lower obstruction ``Q_n``.

    ``Q_n`` is the least nonnegative half-integer threshold whose tail
    packing requirement fits in the ``n-1`` core positions.  The requirement
    changes only at ``k(k+1)/2``, ``k(k+1)``, or ``(k^2-1)/2``.  The last
    event makes the skip-one pair ``(k-1, k+1)`` compatible.  Checking these
    finite events is equivalent to minimizing over all nonnegative
    half-integers.
    """
    _validate_problem_n(n)
    for threshold in sorted(_two_threshold_event_thresholds(n)):
        packing = two_threshold_tail_packing(n, threshold)
        if packing.required_positions <= n - 1:
            return threshold
    raise AssertionError("finite two-threshold event set was not exhaustive")


def terminal_high_incidence_lower_obstruction(n: int) -> Fraction:
    """Return the joint terminal-high incidence obstruction ``H_n``.

    ``H_n`` is the least nonnegative half-integer threshold satisfying both
    the exact cyclic tail-packing requirement used for ``Q_n`` and the
    compatible-low incidence capacity ``2*v <= C_n(T)``.  The definition of
    ``Q_n`` is unchanged.  Besides its events, the compatible-low floor can
    change only at ``k^2/2`` for even ``4 <= k <= n``.
    """
    _validate_problem_n(n)
    event_thresholds = _two_threshold_event_thresholds(n)
    event_thresholds.update(
        Fraction(k * k, 2) for k in range(4, n + 1, 2)
    )

    for threshold in sorted(event_thresholds):
        packing = two_threshold_tail_packing(n, threshold)
        if (
            packing.required_positions <= n - 1
            and 2 * packing.v_size <= packing.compatible_low_capacity
        ):
            return threshold
    raise AssertionError("finite terminal-high event set was not exhaustive")


def terminal_high_incidence_closed_form(n: int) -> Fraction:
    """Return the exact residue-class formula for ``H_n`` when ``n >= 9``.

    With ``d_n = ceil((4*n+8)/5)``, residues zero, three, and four give
    ``d_n(d_n-1)/2``; residue one gives ``(d_n-1)^2/2``; and residue two
    gives ``(d_n-1)(d_n-2)/2`` except for the exact value ``H_12 = 56``.
    The event-set inversion in :func:`terminal_high_incidence_lower_obstruction`
    remains an independent exact implementation of the definition.
    """
    _validate_eight_twenty_fifths_n(n)
    if n == 12:
        return Fraction(56)

    d = (4 * n + 12) // 5
    residue = n % 5
    if residue in (0, 3, 4):
        numerator = d * (d - 1)
    elif residue == 1:
        numerator = (d - 1) ** 2
    else:
        numerator = (d - 1) * (d - 2)
    return Fraction(numerator, 2)


def eight_twenty_fifths_threshold(n: int) -> int:
    """Return ``T_n = d_n(d_n-1)/2`` for the matching upper construction.

    Here ``d_n = ceil((4*n+8)/5)``.  The construction theorem is stated for
    ``n >= 9``, so this helper deliberately has the same domain.
    """
    _validate_eight_twenty_fifths_n(n)
    d = (4 * n + 12) // 5
    return d * (d - 1) // 2


def eight_twenty_fifths_order(n: int) -> tuple[int, ...]:
    """Return an explicit core order with score at most ``T_n``.

    The fourteen small orders not covered by the uniform block parameters are
    stored explicitly.  Every other ``n >= 9`` uses the exact block family
    proved in ``research/PRODUCT_DISTANCE_SURROGATE.md``.  This routine does
    not enumerate or search over cyclic orders.
    """
    _validate_eight_twenty_fifths_n(n)
    exceptional = _EIGHT_TWENTY_FIFTHS_EXCEPTIONAL_ORDERS.get(n)
    if exceptional is not None:
        return exceptional

    d = (4 * n + 12) // 5
    v = n - d + 1
    residue_slack = d - 4 * v - 2
    if v < residue_slack:
        raise AssertionError(
            f"missing exceptional order for n={n}, v={v}, s={residue_slack}"
        )

    triple_count, has_doubleton = divmod(v + residue_slack, 2)
    middle_paths: list[tuple[int, ...]] = [
        (
            d - 1 - 2 * block,
            2 * v + 2 + block,
            d - 2 - 2 * block,
        )
        for block in range(triple_count)
    ]
    remaining_middle = list(
        range(
            2 * v + triple_count + 2,
            d - 2 * triple_count,
        )
    )
    if has_doubleton:
        middle_paths.append(tuple(remaining_middle[:2]))
        remaining_middle = remaining_middle[2:]
    middle_paths.extend((value,) for value in remaining_middle)
    if len(middle_paths) != v:
        raise AssertionError(
            f"middle-path count mismatch for n={n}: "
            f"expected {v}, got {len(middle_paths)}"
        )

    left_lows = tuple(2 * v + 1 - 2 * block for block in range(v))
    right_lows = tuple(2 * v - 2 * block for block in range(v))
    order: list[int] = []
    for block, middle_path in enumerate(middle_paths):
        order.extend(
            (
                d + block,
                right_lows[block],
                *middle_path,
                left_lows[(block + 1) % v],
            )
        )

    result = tuple(order)
    if len(result) != n - 1 or set(result) != set(range(2, n + 1)):
        raise AssertionError(f"block construction is not a core order for n={n}")
    return result


def residue_one_product_distance_order(n: int) -> tuple[int, ...]:
    """Return the exact-threshold order for ``n == 1 (mod 5)``, ``n >= 11``.

    Writing ``n = 5*k+1`` and ``D = 4*k+2``, this search-free construction
    has product-distance score exactly ``D**2/2 = H_n``.  It sharpens
    :func:`eight_twenty_fifths_order` only in this residue class; the proof is
    recorded in ``research/PRODUCT_DISTANCE_SURROGATE.md``.
    """
    _validate_residue_one_n(n)
    k = (n - 1) // 5
    terminal_start = 4 * k + 2
    triple_count, has_doubleton = divmod(k, 2)

    middle_paths: list[tuple[int, ...]] = [(terminal_start - 1,)]
    middle_paths.extend(
        (
            terminal_start - 2 * block,
            2 * k + 1 + block,
            terminal_start - 2 * block - 1,
        )
        for block in range(1, triple_count + 1)
    )
    middle_paths.extend(
        (terminal_start - triple_count - block - 1,)
        for block in range(triple_count + 1, k - has_doubleton)
    )
    if has_doubleton:
        middle_paths.append((2 * k + triple_count + 3, 2 * k + triple_count + 2))
    if len(middle_paths) != k:
        raise AssertionError(
            f"middle-path count mismatch for n={n}: "
            f"expected {k}, got {len(middle_paths)}"
        )

    order: list[int] = []
    for block, middle_path in enumerate(middle_paths):
        next_block = (block + 1) % k
        order.extend(
            (
                terminal_start + block,
                2 * k - 2 * block,
                *middle_path,
                2 * k + 1 - 2 * next_block,
            )
        )

    result = tuple(order)
    if len(result) != n - 1 or set(result) != set(range(2, n + 1)):
        raise AssertionError(f"residue-one construction is not a core order for n={n}")
    return result


def residue_two_product_distance_order(n: int) -> tuple[int, ...]:
    """Return the exact-threshold order for ``n == 2 (mod 5)``, ``n >= 12``.

    Writing ``n = 5*k+2`` and ``d = 4*k+4``, this search-free construction
    has product-distance score exactly ``d*(d-2)/2``.  Its two parity branches
    partition the same symbolic middle interval; the proof is recorded in
    ``research/PRODUCT_DISTANCE_SURROGATE.md``.
    """
    _validate_residue_two_n(n)
    k = (n - 2) // 5
    terminal_start = 4 * k + 3
    triple_count = (k + 1) // 2

    middle_paths: list[tuple[int, ...]] = [
        (
            terminal_start - 1 - 2 * block,
            2 * k + 2 + block,
            terminal_start - 2 - 2 * block,
        )
        for block in range(triple_count)
    ]
    residual_start = 2 * k + triple_count + 2
    if k % 2 == 0:
        middle_paths.append((residual_start, residual_start + 1))
        middle_paths.extend(
            (residual_start + block - triple_count + 1,)
            for block in range(triple_count + 1, k)
        )
    else:
        middle_paths.extend(
            (residual_start + block - triple_count,)
            for block in range(triple_count, k)
        )
    if len(middle_paths) != k:
        raise AssertionError(
            f"middle-path count mismatch for n={n}: "
            f"expected {k}, got {len(middle_paths)}"
        )

    order: list[int] = []
    for block, middle_path in enumerate(middle_paths):
        next_block = (block + 1) % k
        order.extend(
            (
                terminal_start + block,
                2 * k - 2 * block,
                *middle_path,
                2 * k + 1 - 2 * next_block,
            )
        )

    result = tuple(order)
    if len(result) != n - 1 or set(result) != set(range(2, n + 1)):
        raise AssertionError(f"residue-two construction is not a core order for n={n}")
    return result


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


def enumerate_truncated_product_distance(
    n: int,
    max_position_distance: int,
    *,
    max_canonical_orders: int = MAX_CANONICAL_ORDERS,
) -> TruncatedProductDistanceEnumeration:
    """Minimize the exact score restricted to positional distances ``<= q``.

    This uses the same canonical order space, hard ``n <= 11`` boundary, work
    ceiling, integer cross-products, and strict incumbent cutoff as the full
    product-distance enumeration.
    """
    _validate_enumeration_n(n)
    _validate_max_position_distance(max_position_distance)
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

    raw_interleave = tuple(int(value) for value in interleave(range(2, n + 1)))
    initial_order = canonicalize_core_order(raw_interleave)
    best = truncated_product_distance_score(
        initial_order,
        max_position_distance,
    )
    representative = initial_order
    minimizer_count = 0
    enumerated_count = 0
    position_pairs = _position_pairs_at_most(n - 1, max_position_distance)

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

    return TruncatedProductDistanceEnumeration(
        n=n,
        max_position_distance=max_position_distance,
        canonical_order_count=enumerated_count,
        optimum=best,
        minimizer_count=minimizer_count,
        representative=representative,
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


def _normalize_nonnegative_threshold(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError(
            "threshold must be a nonnegative integer or Fraction, "
            f"got {value!r}"
        )
    threshold = Fraction(value)
    if threshold < 0:
        raise ValueError(f"threshold must be nonnegative, got {value!r}")
    return threshold


def _strict_product_tail_start(threshold: Fraction) -> int:
    """Return the least integer ``k >= 2`` with ``k(k+1) > threshold``."""
    numerator = threshold.numerator
    denominator = threshold.denominator
    discriminant_floor = (denominator + 4 * numerator) // denominator
    weak_root = (math.isqrt(discriminant_floor) - 1) // 2
    return max(2, weak_root + 1)


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


def _validate_eight_twenty_fifths_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 9:
        raise ValueError(f"n must be an integer at least 9, got {n!r}")


def _validate_residue_one_n(n: int) -> None:
    if (
        isinstance(n, bool)
        or not isinstance(n, int)
        or n < 11
        or n % 5 != 1
    ):
        raise ValueError(
            "n must be an integer congruent to 1 modulo 5 and at least 11, "
            f"got {n!r}"
        )


def _validate_residue_two_n(n: int) -> None:
    if (
        isinstance(n, bool)
        or not isinstance(n, int)
        or n < 12
        or n % 5 != 2
    ):
        raise ValueError(
            "n must be an integer congruent to 2 modulo 5 and at least 12, "
            f"got {n!r}"
        )


def _validate_max_position_distance(max_position_distance: int) -> None:
    if (
        isinstance(max_position_distance, bool)
        or not isinstance(max_position_distance, int)
        or max_position_distance < 1
    ):
        raise ValueError(
            "max_position_distance must be a positive integer, "
            f"got {max_position_distance!r}"
        )


def _rotate_to_front(order: tuple[int, ...], value: int) -> tuple[int, ...]:
    index = order.index(value)
    return order[index:] + order[:index]


def _cycle_path_away_from_neighbor(
    order: tuple[int, ...],
    *,
    start: int,
    blocked_neighbor: int,
    end: int,
    length: int,
) -> tuple[int, ...] | None:
    start_position = order.index(start)
    next_value = order[(start_position + 1) % len(order)]
    previous_value = order[(start_position - 1) % len(order)]
    if next_value == blocked_neighbor:
        step = -1
    elif previous_value == blocked_neighbor:
        step = 1
    else:
        return None

    path = tuple(
        order[(start_position + offset * step) % len(order)]
        for offset in range(length)
    )
    blocked_range = path[1:-1] if blocked_neighbor == end else path[1:]
    if path[-1] != end or blocked_neighbor in blocked_range:
        return None
    return path


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


def _position_pairs_at_most(
    vertex_count: int,
    max_position_distance: int,
) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        pair
        for pair in _position_pairs(vertex_count)
        if pair[2] <= max_position_distance
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
    "AdjacentEqualityStructure",
    "MAX_CANONICAL_ORDERS",
    "MAX_ENUMERATION_N",
    "MIN_ENUMERATION_N",
    "ProductDistanceEnumeration",
    "ProductDistancePairScore",
    "TruncatedProductDistanceEnumeration",
    "TwoThresholdTailPacking",
    "adjacent_equality_structure",
    "adjacent_product_optimum",
    "best_tail_lower_obstruction",
    "canonical_core_order_count",
    "canonical_core_orders",
    "canonicalize_core_order",
    "circular_position_distance",
    "eight_twenty_fifths_order",
    "eight_twenty_fifths_threshold",
    "enumerate_product_distance",
    "enumerate_truncated_product_distance",
    "product_distance_pair_scores",
    "product_distance_score",
    "residue_one_product_distance_order",
    "residue_two_product_distance_order",
    "tail_cycle_incompatibility_minimum",
    "tail_pairing_sum",
    "terminal_high_incidence_closed_form",
    "terminal_high_incidence_lower_obstruction",
    "truncated_product_distance_score",
    "two_threshold_lower_obstruction",
    "two_threshold_tail_packing",
]
