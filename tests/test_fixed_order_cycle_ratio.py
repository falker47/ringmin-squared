from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
from math import isqrt

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


_SqrtTwoPair = tuple[Fraction, Fraction]


def _sqrt_two_pair(
    rational: int | Fraction = 0,
    radical: int | Fraction = 0,
) -> _SqrtTwoPair:
    """Represent ``rational + radical * sqrt(2)`` exactly in test code."""
    return (Fraction(rational), Fraction(radical))


def _sqrt_two_pair_add(
    left: _SqrtTwoPair,
    right: _SqrtTwoPair,
) -> _SqrtTwoPair:
    return (left[0] + right[0], left[1] + right[1])


def _sqrt_two_pair_subtract(
    left: _SqrtTwoPair,
    right: _SqrtTwoPair,
) -> _SqrtTwoPair:
    return (left[0] - right[0], left[1] - right[1])


def _sqrt_two_pair_multiply(
    left: _SqrtTwoPair,
    right: _SqrtTwoPair,
) -> _SqrtTwoPair:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def _sqrt_two_pair_scale(
    value: _SqrtTwoPair,
    factor: int | Fraction,
) -> _SqrtTwoPair:
    factor = Fraction(factor)
    return (factor * value[0], factor * value[1])


def _sqrt_two_pair_divide(
    numerator: _SqrtTwoPair,
    denominator: _SqrtTwoPair,
) -> _SqrtTwoPair:
    conjugate = (denominator[0], -denominator[1])
    norm = denominator[0] ** 2 - 2 * denominator[1] ** 2
    assert norm
    return _sqrt_two_pair_scale(
        _sqrt_two_pair_multiply(numerator, conjugate),
        1 / norm,
    )


def _sqrt_two_pair_sign(value: _SqrtTwoPair) -> int:
    """Return the exact sign of one rational quadratic surd."""
    rational, radical = value
    if radical == 0:
        return (rational > 0) - (rational < 0)
    if rational == 0:
        return (radical > 0) - (radical < 0)
    if rational > 0 and radical > 0:
        return 1
    if rational < 0 and radical < 0:
        return -1

    rational_square = rational * rational
    radical_square = 2 * radical * radical
    assert rational_square != radical_square
    if rational > 0:
        return 1 if rational_square > radical_square else -1
    return 1 if radical_square > rational_square else -1


def _sqrt_two_pair_ge(
    left: _SqrtTwoPair,
    right: _SqrtTwoPair,
) -> bool:
    return _sqrt_two_pair_sign(_sqrt_two_pair_subtract(left, right)) >= 0


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


def _cyclic_product_sum(values: tuple[int, ...]) -> int:
    """Return the literal cyclic adjacent-product sum for one nonempty tuple."""
    assert values
    return sum(
        left * right
        for left, right in zip(values, values[1:] + values[:1], strict=True)
    )


def _six_label_dihedral_orders_oracle() -> tuple[tuple[int, ...], ...]:
    """Generate the 60 dihedral classes on ``{4, ..., 9}`` test-locally.

    Fixing label nine removes rotations.  The endpoint comparison retains
    exactly one orientation from each reflection pair.  This helper does not
    call a repository canonicalizer or either public enumeration path.
    """
    return tuple(
        order
        for tail in itertools.permutations((4, 5, 6, 7, 8))
        if (order := (9, *tail))[1] < order[-1]
    )


def _seven_label_dihedral_orders_oracle() -> tuple[tuple[int, ...], ...]:
    """Generate the 360 dihedral classes on ``{4, ..., 10}`` locally.

    Fixing label ten removes rotations, and the endpoint comparison keeps one
    orientation from each reflection pair.  No repository canonicalizer,
    public enumerator, or production scorer is used.
    """
    return tuple(
        order
        for tail in itertools.permutations((4, 5, 6, 7, 8, 9))
        if (order := (10, *tail))[1] < order[-1]
    )


def _low_pairing_signatures_oracle(
    entries: tuple[int, ...],
    ceiling: int,
) -> tuple[int, dict[int, tuple[tuple[tuple[int, int], ...], ...]]]:
    """Classify low-score pairings of one explicit test-local multiset."""
    assert len(entries) % 2 == 0
    entries = tuple(sorted(entries))
    minimum: int | None = None
    signatures: dict[int, set[tuple[tuple[int, int], ...]]] = {}

    def visit(
        remaining: tuple[int, ...],
        pairs: tuple[tuple[int, int], ...],
    ) -> None:
        nonlocal minimum
        if not remaining:
            signature = tuple(
                sorted((min(left, right), max(left, right)) for left, right in pairs)
            )
            score = sum(left * right for left, right in signature)
            minimum = score if minimum is None else min(minimum, score)
            if score <= ceiling:
                signatures.setdefault(score, set()).add(signature)
            return

        left = remaining[0]
        for right_position in range(1, len(remaining)):
            right = remaining[right_position]
            visit(
                remaining[1:right_position] + remaining[right_position + 1 :],
                pairs + ((left, right),),
            )

    visit(entries, ())
    assert minimum is not None
    return minimum, {
        score: tuple(sorted(score_signatures))
        for score, score_signatures in sorted(signatures.items())
    }


def _near_minimum_duplicated_pairings_oracle(
    labels: tuple[int, ...],
    ceiling: int,
) -> tuple[int, dict[int, tuple[tuple[tuple[int, int], ...], ...]]]:
    """Classify low pairings of two test-local copies of each label."""
    return _low_pairing_signatures_oracle(
        tuple(label for label in labels for _copy in range(2)),
        ceiling,
    )


def _is_loopless_spanning_cycle_signature(
    signature: tuple[tuple[int, int], ...],
    labels: tuple[int, ...],
) -> bool:
    """Recognize a simple spanning cycle among duplicated-label pairings.

    The two-vertex double-edge convention is deliberately outside this
    helper.  On three or more labels, degree two is not enough: disconnected
    unions of cycles must also be rejected.
    """
    if len(labels) < 3 or len(signature) != len(labels):
        return False

    degrees = {label: 0 for label in labels}
    adjacency = {label: set() for label in labels}
    seen_edges: set[tuple[int, int]] = set()
    for left, right in signature:
        edge = (min(left, right), max(left, right))
        if left not in degrees or right not in degrees:
            return False
        if left == right or edge in seen_edges:
            return False
        seen_edges.add(edge)
        degrees[left] += 1
        degrees[right] += 1
        adjacency[left].add(right)
        adjacency[right].add(left)

    if set(degrees.values()) != {2}:
        return False

    seen = {labels[0]}
    frontier = [labels[0]]
    while frontier:
        current = frontier.pop()
        for neighbor in adjacency[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return seen == set(labels)


def _undirected_cycle_edge_signature(
    order: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    """Record a literal cycle independently of its root and orientation."""
    return tuple(
        sorted(
            (min(left, right), max(left, right))
            for left, right in zip(order, order[1:] + order[:1], strict=True)
        )
    )


def _dihedral_orders_on_labels_oracle(
    labels: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    """Generate labelled simple cycles without repository enumeration."""
    assert len(labels) >= 3
    assert len(labels) == len(set(labels))
    anchor = max(labels)
    remaining = tuple(label for label in labels if label != anchor)
    return tuple(
        order
        for tail in itertools.permutations(remaining)
        if (order := (anchor, *tail))[1] < order[-1]
    )


def _nested_tail_bound_oracle(m: int, n: int) -> tuple[int, int]:
    """Return the minimum tail-cycle score and exact two-tail obstruction."""
    labels = tuple(range(m + 1, n + 1))
    assert len(labels) >= 3
    minimum_cycle_score: int | None = None
    minimum_two_tail_score: int | None = None

    for order in _dihedral_orders_on_labels_oracle(labels):
        tail_score = _cyclic_product_sum(order)
        minimum_cycle_score = (
            tail_score
            if minimum_cycle_score is None
            else min(minimum_cycle_score, tail_score)
        )
        for position, left in enumerate(order):
            right = order[(position + 1) % len(order)]
            inserted_order = order[: position + 1] + (m,) + order[position + 1 :]
            correction = m * (left + right) - left * right

            assert correction == m * m - (left - m) * (right - m)
            assert _cyclic_product_sum(inserted_order) == tail_score + correction

            candidate = tail_score + max(0, correction)
            minimum_two_tail_score = (
                candidate
                if minimum_two_tail_score is None
                else min(minimum_two_tail_score, candidate)
            )

    assert minimum_cycle_score is not None
    assert minimum_two_tail_score is not None
    return minimum_cycle_score, minimum_two_tail_score


def _split_cycle_edge_oracle(
    order: tuple[int, ...],
    position: int,
    label: int,
) -> tuple[int, ...]:
    """Split one literal cyclic edge with a new label."""
    assert label not in order
    assert 0 <= position < len(order)
    return order[: position + 1] + (label,) + order[position + 1 :]


def _three_nested_tail_bound_oracle(
    m: int,
    n: int,
) -> tuple[
    int,
    int,
    frozenset[tuple[tuple[int, int], ...]],
    dict[str, int],
]:
    """Enumerate the exact compatible double splits without production code."""
    x = m + 1
    base_labels = tuple(range(m + 2, n + 1))
    assert len(base_labels) >= 3

    minimum_base_score: int | None = None
    minimum_three_tail_score: int | None = None
    minimum_distinct_edge_score: int | None = None
    final_signatures: set[tuple[tuple[int, int], ...]] = set()
    interaction_counts = {
        "nested": 0,
        "separate_adjacent": 0,
        "separate_disjoint": 0,
    }

    for base in _dihedral_orders_on_labels_oracle(base_labels):
        base_score = _cyclic_product_sum(base)
        minimum_base_score = (
            base_score
            if minimum_base_score is None
            else min(minimum_base_score, base_score)
        )
        base_signature = _undirected_cycle_edge_signature(base)
        base_edges = set(base_signature)
        assert _is_loopless_spanning_cycle_signature(
            base_signature,
            base_labels,
        )

        for first_position, a in enumerate(base):
            b = base[(first_position + 1) % len(base)]
            first_edge = (min(a, b), max(a, b))
            intermediate = _split_cycle_edge_oracle(base, first_position, x)
            intermediate_score = _cyclic_product_sum(intermediate)
            first_correction = x * (a + b) - a * b
            intermediate_signature = _undirected_cycle_edge_signature(intermediate)
            intermediate_edges = set(intermediate_signature)
            child_edges = {
                (min(a, x), max(a, x)),
                (min(x, b), max(x, b)),
            }

            assert first_correction == x * x - (a - x) * (b - x)
            assert intermediate_score == base_score + first_correction
            assert intermediate_edges == (
                base_edges - {first_edge}
            ) | child_edges
            assert _is_loopless_spanning_cycle_signature(
                intermediate_signature,
                (x, *base_labels),
            )

            for second_position, u in enumerate(intermediate):
                v = intermediate[(second_position + 1) % len(intermediate)]
                second_edge = (min(u, v), max(u, v))
                final = _split_cycle_edge_oracle(
                    intermediate,
                    second_position,
                    m,
                )
                final_score = _cyclic_product_sum(final)
                second_correction = m * (u + v) - u * v
                final_signature = _undirected_cycle_edge_signature(final)
                final_edges = set(final_signature)

                assert second_correction == m * m - (u - m) * (v - m)
                assert final_score == intermediate_score + second_correction
                assert final_edges == (
                    intermediate_edges - {second_edge}
                ) | {
                    (min(u, m), max(u, m)),
                    (min(m, v), max(m, v)),
                }
                assert _is_loopless_spanning_cycle_signature(
                    final_signature,
                    (m, x, *base_labels),
                )

                if second_edge in child_edges:
                    interaction = "nested"
                else:
                    assert second_edge in base_edges - {first_edge}
                    common_endpoints = len(
                        set(first_edge).intersection(second_edge)
                    )
                    assert common_endpoints in {0, 1}
                    interaction = (
                        "separate_adjacent"
                        if common_endpoints == 1
                        else "separate_disjoint"
                    )
                interaction_counts[interaction] += 1

                candidate = max(
                    base_score,
                    intermediate_score,
                    final_score,
                )
                assert candidate == base_score + max(
                    0,
                    first_correction,
                    first_correction + second_correction,
                )
                minimum_three_tail_score = (
                    candidate
                    if minimum_three_tail_score is None
                    else min(minimum_three_tail_score, candidate)
                )
                if interaction != "nested":
                    minimum_distinct_edge_score = (
                        candidate
                        if minimum_distinct_edge_score is None
                        else min(minimum_distinct_edge_score, candidate)
                    )
                final_signatures.add(final_signature)

    assert minimum_base_score is not None
    assert minimum_three_tail_score is not None
    assert minimum_distinct_edge_score == minimum_three_tail_score
    return (
        minimum_base_score,
        minimum_three_tail_score,
        frozenset(final_signatures),
        interaction_counts,
    )


def _consecutive_tail_block_oracle(
    m: int,
    n: int,
    r: int,
) -> tuple[
    int,
    int,
    dict[tuple[tuple[int, int], ...], int],
    int,
    int,
]:
    """Enumerate compatible descending splits for one bounded tail block."""
    ell = m + r - 1
    assert m >= 1
    assert r >= 2
    assert ell <= n - 2

    base_labels = tuple(range(ell, n + 1))
    base_orders = _dihedral_orders_on_labels_oracle(base_labels)
    minimum_base_score: int | None = None
    objectives_by_signature: dict[tuple[tuple[int, int], ...], int] = {}
    history_count = 0
    fully_nested_history_count = 0

    for base in base_orders:
        base_score = _cyclic_product_sum(base)
        minimum_base_score = (
            base_score
            if minimum_base_score is None
            else min(minimum_base_score, base_score)
        )
        base_signature = _undirected_cycle_edge_signature(base)
        assert _is_loopless_spanning_cycle_signature(
            base_signature,
            base_labels,
        )

        def visit(
            current: tuple[int, ...],
            next_label: int,
            prefixes: tuple[int, ...],
            previous_children: frozenset[tuple[int, int]] | None,
            fully_nested: bool,
        ) -> None:
            nonlocal history_count, fully_nested_history_count

            if next_label < m:
                history_count += 1
                fully_nested_history_count += int(fully_nested)
                final_signature = _undirected_cycle_edge_signature(current)
                assert final_signature not in objectives_by_signature

                induced_scores = tuple(
                    _cyclic_product_sum(
                        tuple(label for label in current if label >= threshold)
                    )
                    for threshold in range(ell, m - 1, -1)
                )
                prefix_scores = tuple(
                    base_score + prefix for prefix in prefixes
                )
                assert induced_scores == prefix_scores
                objectives_by_signature[final_signature] = max(prefix_scores)
                return

            current_signature = _undirected_cycle_edge_signature(current)
            current_edges = set(current_signature)
            current_score = _cyclic_product_sum(current)

            for position, left in enumerate(current):
                right = current[(position + 1) % len(current)]
                split_edge = (min(left, right), max(left, right))
                inserted = _split_cycle_edge_oracle(
                    current,
                    position,
                    next_label,
                )
                correction = next_label * (left + right) - left * right
                inserted_score = _cyclic_product_sum(inserted)
                inserted_signature = _undirected_cycle_edge_signature(inserted)
                inserted_edges = set(inserted_signature)
                child_edges = frozenset(
                    {
                        (min(left, next_label), max(left, next_label)),
                        (min(next_label, right), max(next_label, right)),
                    }
                )

                assert correction == next_label * next_label - (
                    left - next_label
                ) * (right - next_label)
                assert inserted_score == current_score + correction
                assert inserted_edges == (
                    current_edges - {split_edge}
                ) | set(child_edges)
                assert _is_loopless_spanning_cycle_signature(
                    inserted_signature,
                    tuple(range(next_label, n + 1)),
                )

                visit(
                    inserted,
                    next_label - 1,
                    (*prefixes, prefixes[-1] + correction),
                    child_edges,
                    fully_nested
                    and (
                        previous_children is None
                        or split_edge in previous_children
                    ),
                )

        visit(base, ell - 1, (0,), None, True)

    direct_objectives: dict[tuple[tuple[int, int], ...], int] = {}
    for outer in _dihedral_orders_on_labels_oracle(tuple(range(m, n + 1))):
        signature = _undirected_cycle_edge_signature(outer)
        assert signature not in direct_objectives
        direct_objectives[signature] = max(
            _cyclic_product_sum(
                tuple(label for label in outer if label >= threshold)
            )
            for threshold in range(m, ell + 1)
        )

    assert minimum_base_score is not None
    assert objectives_by_signature == direct_objectives
    assert history_count == len(objectives_by_signature)
    return (
        minimum_base_score,
        min(objectives_by_signature.values()),
        objectives_by_signature,
        history_count,
        fully_nested_history_count,
    )


def _linear_density_prefix_diagnostic_oracle(
    n: int,
    *,
    force_recursive: bool,
) -> None:
    """Audit the optimized linear-block inequalities on one bounded history."""
    r = isqrt(2 * n * n) - n
    cutoff = 1 + (isqrt(162 * n * n) - 8 * n) // 12
    assert cutoff < r

    beta_times_n = _sqrt_two_pair(Fraction(-2 * n, 3), Fraction(3 * n, 4))
    assert _sqrt_two_pair_sign(
        _sqrt_two_pair_subtract(beta_times_n, _sqrt_two_pair(cutoff - 1))
    ) > 0
    assert _sqrt_two_pair_sign(
        _sqrt_two_pair_subtract(_sqrt_two_pair(cutoff), beta_times_n)
    ) > 0

    prefix_weight = _sqrt_two_pair(Fraction(88, 49), Fraction(-48, 49))
    two_minus_weight = _sqrt_two_pair_subtract(
        _sqrt_two_pair(2),
        prefix_weight,
    )
    assert _sqrt_two_pair_sign(prefix_weight) > 0
    assert _sqrt_two_pair_sign(
        _sqrt_two_pair_subtract(_sqrt_two_pair(1), prefix_weight)
    ) > 0

    base = _alternating_tail_cycle_oracle(r - 1, n)
    base_edges = set(_undirected_cycle_edge_signature(base))
    base_score = _cyclic_product_sum(base)
    center = n + r
    tail_size = n - r + 1
    pairing_floor = sum(
        label * (center - label) for label in range(r, n + 1)
    )
    half = tail_size // 2
    alternating_excess = (
        half * (half - 1) // 2
        if tail_size % 2 == 0
        else half * (half + 1) // 2
    )
    base_slack = sum(
        (left + right - center) ** 2 for left, right in base_edges
    )

    assert 2 * (base_score - pairing_floor) == base_slack
    assert base_score == pairing_floor + alternating_excess

    def base_split_floor(label: int) -> _SqrtTwoPair:
        inner = _sqrt_two_pair_subtract(
            _sqrt_two_pair(4 * center * label - center * center),
            _sqrt_two_pair_scale(prefix_weight, 2 * label * label),
        )
        return _sqrt_two_pair_divide(
            _sqrt_two_pair_multiply(prefix_weight, inner),
            _sqrt_two_pair_scale(two_minus_weight, 2),
        )

    def recursive_split_floor(label: int) -> _SqrtTwoPair:
        return _sqrt_two_pair_scale(
            prefix_weight,
            (center - 1) * label - n * (r - 1),
        )

    local_floor = base_split_floor(cutoff)
    assert _sqrt_two_pair_ge(recursive_split_floor(cutoff), local_floor)
    current = base
    prefixes = [0]
    used_base_edges: set[tuple[int, int]] = set()
    local_contributions = _sqrt_two_pair()

    for label in range(r - 1, cutoff - 1, -1):
        candidates = []
        for position, left in enumerate(current):
            right = current[(position + 1) % len(current)]
            edge = (min(left, right), max(left, right))
            is_base_edge = edge in base_edges
            if (
                (force_recursive and label < r - 1 and not is_base_edge)
                or (not force_recursive and is_base_edge)
                or (force_recursive and label == r - 1 and is_base_edge)
            ):
                candidates.append((position, left, right, edge))

        assert candidates
        position, left, right, edge = candidates[0]
        correction = label * (left + right) - left * right

        if edge in base_edges:
            assert edge not in used_base_edges
            used_base_edges.add(edge)
            edge_slack = Fraction((left + right - center) ** 2, 2)
            contribution = _sqrt_two_pair_add(
                _sqrt_two_pair(edge_slack),
                _sqrt_two_pair_scale(prefix_weight, correction),
            )
            relaxed_contribution = _sqrt_two_pair_add(
                _sqrt_two_pair(edge_slack),
                _sqrt_two_pair_scale(
                    prefix_weight,
                    Fraction(
                        4 * label * (left + right) - (left + right) ** 2,
                        4,
                    ),
                ),
            )
            square_argument = _sqrt_two_pair_subtract(
                _sqrt_two_pair_scale(two_minus_weight, left + right),
                _sqrt_two_pair_subtract(
                    _sqrt_two_pair(2 * center),
                    _sqrt_two_pair_scale(prefix_weight, 2 * label),
                ),
            )
            square_term = _sqrt_two_pair_divide(
                _sqrt_two_pair_multiply(square_argument, square_argument),
                _sqrt_two_pair_scale(two_minus_weight, 4),
            )
            assert contribution == _sqrt_two_pair_add(
                relaxed_contribution,
                _sqrt_two_pair_scale(
                    prefix_weight,
                    Fraction((left - right) ** 2, 4),
                ),
            )
            assert relaxed_contribution == _sqrt_two_pair_add(
                base_split_floor(label),
                square_term,
            )
            assert _sqrt_two_pair_ge(contribution, base_split_floor(label))
            assert _sqrt_two_pair_ge(
                base_split_floor(label),
                base_split_floor(cutoff),
            )
        else:
            assert min(left, right) < r
            recursive_lower = (center - 1) * label - n * (r - 1)
            assert correction >= recursive_lower
            contribution = _sqrt_two_pair_scale(prefix_weight, correction)
            assert _sqrt_two_pair_ge(
                contribution,
                recursive_split_floor(label),
            )
            assert _sqrt_two_pair_ge(
                recursive_split_floor(label),
                recursive_split_floor(cutoff),
            )

        finite_gap_numerator = _sqrt_two_pair_add(
            _sqrt_two_pair((n - r) ** 2 + 4 * (n - label)),
            _sqrt_two_pair_scale(
                prefix_weight,
                2 * (r - 1 - label) * (n - label),
            ),
        )
        finite_gap = _sqrt_two_pair_divide(
            _sqrt_two_pair_multiply(prefix_weight, finite_gap_numerator),
            _sqrt_two_pair_scale(two_minus_weight, 2),
        )
        assert _sqrt_two_pair_subtract(
            recursive_split_floor(label),
            base_split_floor(label),
        ) == finite_gap
        assert _sqrt_two_pair_sign(finite_gap) > 0

        local_contributions = _sqrt_two_pair_add(
            local_contributions,
            contribution,
        )
        prefixes.append(prefixes[-1] + correction)
        current = _split_cycle_edge_oracle(current, position, label)

    unused_base_slack = _sqrt_two_pair(
        Fraction(
            sum(
                (left + right - center) ** 2
                for left, right in base_edges - used_base_edges
            ),
            2,
        )
    )
    prefix_length = r - cutoff
    weighted_excess = _sqrt_two_pair_add(
        _sqrt_two_pair(base_score - pairing_floor),
        _sqrt_two_pair_scale(prefix_weight, prefixes[-1]),
    )
    objective = base_score + max(prefixes)
    objective_excess = _sqrt_two_pair(objective - pairing_floor)
    prefix_floor = _sqrt_two_pair_scale(local_floor, prefix_length)

    assert weighted_excess == _sqrt_two_pair_add(
        local_contributions,
        unused_base_slack,
    )
    assert _sqrt_two_pair_ge(local_contributions, prefix_floor)
    assert _sqrt_two_pair_ge(weighted_excess, prefix_floor)
    assert _sqrt_two_pair_ge(objective_excess, weighted_excess)
    assert _sqrt_two_pair_ge(objective_excess, prefix_floor)
    assert _sqrt_two_pair_ge(
        _sqrt_two_pair(objective - pairing_floor - alternating_excess),
        _sqrt_two_pair_subtract(
            prefix_floor,
            _sqrt_two_pair(alternating_excess),
        ),
    )


def _alternating_tail_cycle_oracle(m: int, n: int) -> tuple[int, ...]:
    """Construct the exact near-pairing cycle used in the asymptotic squeeze."""
    labels = tuple(range(m + 1, n + 1))
    q = len(labels)
    assert q >= 3
    half = q // 2

    if q % 2 == 0:
        lows = labels[:half]
        highs = tuple(reversed(labels[half:]))
        return tuple(
            label
            for pair in zip(lows, highs, strict=True)
            for label in pair
        )

    middle = labels[half]
    lows = labels[:half]
    highs = tuple(reversed(labels[half + 1 :]))
    return (
        middle,
        *(
            label
            for pair in zip(lows, highs, strict=True)
            for label in pair
        ),
    )


def _nine_core_dihedral_orders_oracle() -> tuple[tuple[int, ...], ...]:
    """Generate all 2,520 core classes on ``{2, ..., 9}`` test-locally.

    Fixing label nine removes rotations, and the endpoint comparison removes
    reflections.  This helper deliberately calls no repository canonicalizer,
    public enumerator, or production scorer.
    """
    return tuple(
        order
        for tail in itertools.permutations(range(2, 9))
        if (order := (9, *tail))[1] < order[-1]
    )


def _literal_induced_label_subset_scores(
    order: tuple[int, ...],
) -> dict[frozenset[int], int]:
    """Score every nonempty induced label subset without production code."""
    scores: dict[frozenset[int], int] = {}
    for subset_size in range(1, len(order) + 1):
        for positions in itertools.combinations(range(len(order)), subset_size):
            induced_order = tuple(order[position] for position in positions)
            scores[frozenset(induced_order)] = _cyclic_product_sum(induced_order)
    return scores


def _literal_score_and_maximizers(
    order: tuple[int, ...],
) -> tuple[int, tuple[tuple[int, ...], ...]]:
    """Return the literal core score and every maximizing label subset."""
    scores = _literal_induced_label_subset_scores(order)
    maximum = max(scores.values())
    maximizers = tuple(
        sorted(
            (
                tuple(sorted(subset))
                for subset, score in scores.items()
                if score == maximum
            ),
            key=lambda subset: (len(subset), subset),
        )
    )
    return maximum, maximizers


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


def _dihedral_cycle_key_oracle(order: tuple[int, ...]) -> tuple[int, ...]:
    """Root a labelled cycle test-locally and retain one orientation.

    The largest label is unique, so rooting there removes every rotation.
    Comparing the two resulting orientations then removes reflection.  This
    helper deliberately calls no repository canonicalizer.
    """
    assert len(order) == len(set(order))
    root_position = order.index(max(order))
    rooted = order[root_position:] + order[:root_position]
    reflected = (rooted[0], *reversed(rooted[1:]))
    return min(rooted, reflected)


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


def test_pairing_signatures_require_one_connected_simple_cycle() -> None:
    expected_counts = {
        3: (5, 1),
        4: (17, 3),
        5: (73, 12),
        6: (388, 60),
    }

    for q, (expected_pairings, expected_cycles) in expected_counts.items():
        labels = tuple(range(1, q + 1))
        _minimum, signatures_by_score = _near_minimum_duplicated_pairings_oracle(
            labels,
            ceiling=q**3,
        )
        pairing_signatures = {
            signature
            for signatures in signatures_by_score.values()
            for signature in signatures
        }
        literal_cycle_signatures = {
            _undirected_cycle_edge_signature(order)
            for order in _dihedral_orders_on_labels_oracle(labels)
        }
        accepted_signatures = {
            signature
            for signature in pairing_signatures
            if _is_loopless_spanning_cycle_signature(signature, labels)
        }

        assert len(pairing_signatures) == expected_pairings
        assert len(literal_cycle_signatures) == expected_cycles
        assert accepted_signatures == literal_cycle_signatures

    disconnected_triangles = (
        (1, 2),
        (1, 3),
        (2, 3),
        (4, 5),
        (4, 6),
        (5, 6),
    )
    assert not _is_loopless_spanning_cycle_signature(
        disconnected_triangles,
        tuple(range(1, 7)),
    )
    assert not _is_loopless_spanning_cycle_signature(((1, 2), (1, 2)), (1, 2))


def test_nested_tail_bound_matches_literal_cycles_and_insertions() -> None:
    expected = {
        (1, 4): (25, 26, 26),
        (2, 6): (76, 77, 77),
        (3, 8): (170, 172, 172),
        (4, 10): (320, 322, 323),
    }

    for (m, n), (expected_pairing, expected_cycle, expected_nested) in (
        expected.items()
    ):
        labels = tuple(range(m + 1, n + 1))
        pairing_floor = sum(label * (m + 1 + n - label) for label in labels)
        minimum_cycle, nested_bound = _nested_tail_bound_oracle(m, n)

        cycle_signatures = {
            _undirected_cycle_edge_signature(order)
            for order in _dihedral_orders_on_labels_oracle(labels)
        }
        signature_bound = min(
            sum(left * right for left, right in signature)
            + max(0, m * (left + right) - left * right)
            for signature in cycle_signatures
            for left, right in signature
        )

        assert pairing_floor == expected_pairing
        assert minimum_cycle == expected_cycle
        assert nested_bound == signature_bound == expected_nested


def test_alternating_tail_cycle_has_exact_subcubic_pairing_excess() -> None:
    for m in range(1, 7):
        for q in range(3, 13):
            n = m + q
            labels = tuple(range(m + 1, n + 1))
            cycle = _alternating_tail_cycle_oracle(m, n)
            pairing_floor = sum(
                label * (m + 1 + n - label) for label in labels
            )
            half = q // 2
            excess = (
                half * (half - 1) // 2
                if q % 2 == 0
                else half * (half + 1) // 2
            )

            assert len(cycle) == len(set(cycle)) == q
            assert set(cycle) == set(labels)
            assert _cyclic_product_sum(cycle) == pairing_floor + excess
            assert 8 * excess <= q * q

            corrections = tuple(
                m * (left + right) - left * right
                for left, right in zip(cycle, cycle[1:] + cycle[:1], strict=True)
            )
            assert all(max(0, correction) <= m * m for correction in corrections)
            assert (
                min(
                    _cyclic_product_sum(cycle) + max(0, correction)
                    for correction in corrections
                )
                <= pairing_floor + excess + m * m
            )


def test_three_nested_tail_compatible_splits_cover_every_simple_cycle() -> None:
    base_minimum, gamma, final_signatures, interaction_counts = (
        _three_nested_tail_bound_oracle(2, 7)
    )
    literal_final_signatures = {
        _undirected_cycle_edge_signature(order)
        for order in _dihedral_orders_on_labels_oracle(tuple(range(2, 8)))
    }

    assert base_minimum == 117
    assert gamma == 118
    assert interaction_counts == {
        "nested": 24,
        "separate_adjacent": 24,
        "separate_disjoint": 12,
    }
    assert len(final_signatures) == 60
    assert final_signatures == literal_final_signatures


def test_three_nested_tail_bound_matches_literal_double_insertions() -> None:
    expected = {
        (1, 5): (46, 47, 47, 12),
        (2, 7): (116, 117, 118, 60),
        (3, 9): (235, 237, 239, 360),
        (3, 10): (320, 322, 323, 2520),
    }

    for (m, n), (
        expected_pairing,
        expected_base,
        expected_gamma,
        expected_cycle_count,
    ) in expected.items():
        base_labels = tuple(range(m + 2, n + 1))
        pairing_floor = sum(
            label * (m + 2 + n - label) for label in base_labels
        )
        base_minimum, gamma, final_signatures, _ = (
            _three_nested_tail_bound_oracle(m, n)
        )
        direct_gamma = min(
            max(
                _cyclic_product_sum(
                    tuple(label for label in order if label >= threshold)
                )
                for threshold in (m, m + 1, m + 2)
            )
            for order in _dihedral_orders_on_labels_oracle(
                tuple(range(m, n + 1))
            )
        )

        assert pairing_floor == expected_pairing
        assert base_minimum == expected_base
        assert gamma == direct_gamma == expected_gamma
        assert len(final_signatures) == expected_cycle_count


def test_three_nested_tail_alternating_base_has_uniform_quadratic_excess() -> None:
    for m in range(1, 7):
        for q in range(3, 13):
            n = m + q + 1
            x = m + 1
            base_labels = tuple(range(m + 2, n + 1))
            base = _alternating_tail_cycle_oracle(m + 1, n)
            base_score = _cyclic_product_sum(base)
            pairing_floor = sum(
                label * (m + 2 + n - label) for label in base_labels
            )
            half = q // 2
            pairing_excess = (
                half * (half - 1) // 2
                if q % 2 == 0
                else half * (half + 1) // 2
            )
            best_compatible_excess: int | None = None

            assert base_score == pairing_floor + pairing_excess
            assert 8 * pairing_excess <= q * q

            for first_position, a in enumerate(base):
                b = base[(first_position + 1) % len(base)]
                first_correction = x * (a + b) - a * b
                intermediate = _split_cycle_edge_oracle(
                    base,
                    first_position,
                    x,
                )

                for second_position, u in enumerate(intermediate):
                    v = intermediate[
                        (second_position + 1) % len(intermediate)
                    ]
                    second_correction = m * (u + v) - u * v
                    prefix_excess = max(
                        0,
                        first_correction,
                        first_correction + second_correction,
                    )

                    assert prefix_excess <= max(0, first_correction) + max(
                        0,
                        second_correction,
                    )
                    assert first_correction <= x * x - 2
                    assert second_correction <= m * m - 2
                    best_compatible_excess = (
                        prefix_excess
                        if best_compatible_excess is None
                        else min(best_compatible_excess, prefix_excess)
                    )

            assert best_compatible_excess is not None
            assert (
                base_score + best_compatible_excess
                <= pairing_floor
                + pairing_excess
                + (m + 1) * (m + 1)
                + m * m
            )
            assert (
                pairing_excess + (m + 1) * (m + 1) + m * m
                < 2 * n * n
            )


@pytest.mark.parametrize(
    (
        "m",
        "n",
        "r",
        "expected_pairing",
        "expected_base",
        "expected_block",
        "expected_cycles",
        "expected_minimizers",
        "expected_fully_nested",
    ),
    (
        (1, 4, 2, 25, 26, 26, 3, 3, 3),
        (1, 5, 3, 46, 47, 47, 12, 4, 6),
        (1, 6, 4, 73, 74, 77, 60, 15, 12),
        (2, 7, 4, 106, 107, 118, 60, 4, 12),
        (2, 8, 4, 164, 165, 172, 360, 12, 48),
    ),
)
def test_consecutive_tail_block_oracle_matches_every_outer_cycle(
    m: int,
    n: int,
    r: int,
    expected_pairing: int,
    expected_base: int,
    expected_block: int,
    expected_cycles: int,
    expected_minimizers: int,
    expected_fully_nested: int,
) -> None:
    ell = m + r - 1
    base_labels = tuple(range(ell, n + 1))
    pairing_floor = sum(
        label * (ell + n - label) for label in base_labels
    )
    base_minimum, block_minimum, objectives, histories, fully_nested = (
        _consecutive_tail_block_oracle(m, n, r)
    )

    assert pairing_floor == expected_pairing
    assert base_minimum == expected_base
    assert block_minimum == expected_block
    assert histories == len(objectives) == expected_cycles
    assert sum(value == block_minimum for value in objectives.values()) == (
        expected_minimizers
    )
    assert fully_nested == expected_fully_nested


def test_tail_pairing_floor_has_exact_quadratic_edge_slack() -> None:
    for tail_size in range(3, 7):
        r = tail_size + 1
        n = r + tail_size - 1
        labels = tuple(range(r, n + 1))
        center = r + n
        pairing_floor = sum(label * (center - label) for label in labels)

        for cycle in _dihedral_orders_on_labels_oracle(labels):
            edge_slack = sum(
                (left + right - center) ** 2
                for left, right in zip(
                    cycle,
                    cycle[1:] + cycle[:1],
                    strict=True,
                )
            )
            assert 2 * (_cyclic_product_sum(cycle) - pairing_floor) == (
                edge_slack
            )


@pytest.mark.parametrize("n", (99, 141, 200, 500, 1_000))
@pytest.mark.parametrize("force_recursive", (False, True))
def test_first_linear_density_block_prefix_diagnostic_is_exact(
    n: int,
    force_recursive: bool,
) -> None:
    _linear_density_prefix_diagnostic_oracle(
        n,
        force_recursive=force_recursive,
    )


def test_first_linear_density_all_depth_two_literal_histories_are_exact() -> None:
    """Exhaust one bounded base's intact and recursive depth-two splits."""
    n = 141
    r = isqrt(2 * n * n) - n
    cutoff = 1 + (isqrt(162 * n * n) - 8 * n) // 12
    assert (r, cutoff) == (58, 56)

    weight = _sqrt_two_pair(Fraction(88, 49), Fraction(-48, 49))
    two_minus_weight = _sqrt_two_pair_subtract(_sqrt_two_pair(2), weight)
    center = n + r
    base = _alternating_tail_cycle_oracle(r - 1, n)
    base_edges = set(_undirected_cycle_edge_signature(base))
    base_score = _cyclic_product_sum(base)
    pairing_floor = sum(
        label * (center - label) for label in range(r, n + 1)
    )

    def base_floor(label: int) -> _SqrtTwoPair:
        inner = _sqrt_two_pair_subtract(
            _sqrt_two_pair(4 * center * label - center * center),
            _sqrt_two_pair_scale(weight, 2 * label * label),
        )
        return _sqrt_two_pair_divide(
            _sqrt_two_pair_multiply(weight, inner),
            _sqrt_two_pair_scale(two_minus_weight, 2),
        )

    local_floor = base_floor(cutoff)
    final_signatures: set[tuple[tuple[int, int], ...]] = set()
    history_count = 0
    recursive_second_count = 0

    for first_position, first_left in enumerate(base):
        first_right = base[(first_position + 1) % len(base)]
        first_edge = tuple(sorted((first_left, first_right)))
        first_correction = (r - 1) * (first_left + first_right) - (
            first_left * first_right
        )
        first_contribution = _sqrt_two_pair_add(
            _sqrt_two_pair(Fraction((first_left + first_right - center) ** 2, 2)),
            _sqrt_two_pair_scale(weight, first_correction),
        )
        assert _sqrt_two_pair_ge(first_contribution, base_floor(r - 1))
        first_cycle = _split_cycle_edge_oracle(base, first_position, r - 1)
        assert len(set(first_cycle)) == len(first_cycle)

        for second_position, second_left in enumerate(first_cycle):
            second_right = first_cycle[(second_position + 1) % len(first_cycle)]
            second_edge = tuple(sorted((second_left, second_right)))
            second_correction = cutoff * (second_left + second_right) - (
                second_left * second_right
            )
            used_base_edges = {first_edge}

            if second_edge in base_edges:
                assert second_edge != first_edge
                used_base_edges.add(second_edge)
                second_contribution = _sqrt_two_pair_add(
                    _sqrt_two_pair(
                        Fraction((second_left + second_right - center) ** 2, 2)
                    ),
                    _sqrt_two_pair_scale(weight, second_correction),
                )
                assert _sqrt_two_pair_ge(second_contribution, local_floor)
            else:
                recursive_second_count += 1
                assert min(second_left, second_right) == r - 1
                recursive_lower = (center - 1) * cutoff - n * (r - 1)
                assert second_correction >= recursive_lower
                second_contribution = _sqrt_two_pair_scale(
                    weight,
                    second_correction,
                )
                assert _sqrt_two_pair_ge(second_contribution, local_floor)

            final_cycle = _split_cycle_edge_oracle(
                first_cycle,
                second_position,
                cutoff,
            )
            final_signature = _undirected_cycle_edge_signature(final_cycle)
            assert final_signature not in final_signatures
            final_signatures.add(final_signature)
            assert len(set(final_cycle)) == len(final_cycle)
            assert len(final_signature) == len(final_cycle)

            unused_slack = _sqrt_two_pair(
                Fraction(
                    sum(
                        (left + right - center) ** 2
                        for left, right in base_edges - used_base_edges
                    ),
                    2,
                )
            )
            local_sum = _sqrt_two_pair_add(
                first_contribution,
                second_contribution,
            )
            selected_prefix = first_correction + second_correction
            weighted_excess = _sqrt_two_pair_add(
                _sqrt_two_pair(base_score - pairing_floor),
                _sqrt_two_pair_scale(weight, selected_prefix),
            )
            objective_excess = _sqrt_two_pair(
                base_score
                + max(0, first_correction, selected_prefix)
                - pairing_floor
            )
            assert weighted_excess == _sqrt_two_pair_add(
                local_sum,
                unused_slack,
            )
            assert _sqrt_two_pair_ge(
                local_sum,
                _sqrt_two_pair_scale(local_floor, 2),
            )
            assert _sqrt_two_pair_ge(objective_excess, weighted_excess)
            history_count += 1

    assert history_count == len(base) * (len(base) + 1) == 7_140
    assert len(final_signatures) == history_count
    assert recursive_second_count == 2 * len(base) == 168


@pytest.mark.parametrize(
    ("weight", "expected_admissible"),
    (
        (Fraction(-1, 10), False),
        (Fraction(0), True),
        (Fraction(2, 5), True),
        (Fraction(1), True),
        (Fraction(11, 10), False),
    ),
)
def test_first_linear_density_prefix_weight_region_is_exact(
    weight: Fraction,
    expected_admissible: bool,
) -> None:
    witnesses = (-1, 1)
    assert all(max(0, value) >= weight * value for value in witnesses) is (
        expected_admissible
    )


def test_first_linear_density_parameter_optimization_is_exact() -> None:
    """Check the optimizer and coefficients in exact ``Q(sqrt(2))`` arithmetic."""
    one = _sqrt_two_pair(1)
    two = _sqrt_two_pair(2)
    sqrt_two = _sqrt_two_pair(0, 1)
    alpha = _sqrt_two_pair(-1, 1)
    beta = _sqrt_two_pair(Fraction(-2, 3), Fraction(3, 4))
    weight = _sqrt_two_pair(Fraction(88, 49), Fraction(-48, 49))
    beta_squared = _sqrt_two_pair_multiply(beta, beta)
    weight_squared = _sqrt_two_pair_multiply(weight, weight)

    assert _sqrt_two_pair_sign(beta) > 0
    assert _sqrt_two_pair_sign(_sqrt_two_pair_subtract(alpha, beta)) > 0
    assert _sqrt_two_pair_sign(weight) > 0
    assert _sqrt_two_pair_sign(_sqrt_two_pair_subtract(one, weight)) > 0

    weight_stationarity = _sqrt_two_pair_add(
        _sqrt_two_pair_subtract(
            _sqrt_two_pair_multiply(beta_squared, weight_squared),
            _sqrt_two_pair_scale(
                _sqrt_two_pair_multiply(beta_squared, weight),
                4,
            ),
        ),
        _sqrt_two_pair_subtract(
            _sqrt_two_pair_scale(
                _sqrt_two_pair_multiply(sqrt_two, beta),
                4,
            ),
            _sqrt_two_pair(2),
        ),
    )
    beta_stationarity = _sqrt_two_pair_add(
        _sqrt_two_pair_subtract(
            _sqrt_two_pair_scale(
                _sqrt_two_pair_multiply(weight, beta_squared),
                3,
            ),
            _sqrt_two_pair_scale(
                _sqrt_two_pair_multiply(
                    _sqrt_two_pair_multiply(weight, alpha),
                    beta,
                ),
                2,
            ),
        ),
        _sqrt_two_pair_add(
            _sqrt_two_pair_scale(
                _sqrt_two_pair_multiply(sqrt_two, beta),
                -4,
            ),
            _sqrt_two_pair(5, -2),
        ),
    )
    assert weight_stationarity == _sqrt_two_pair()
    assert beta_stationarity == _sqrt_two_pair()

    limiting_base_numerator = _sqrt_two_pair_subtract(
        _sqrt_two_pair_subtract(
            _sqrt_two_pair_scale(
                _sqrt_two_pair_multiply(sqrt_two, beta),
                2,
            ),
            one,
        ),
        _sqrt_two_pair_multiply(weight, beta_squared),
    )
    limiting_base_floor = _sqrt_two_pair_divide(
        _sqrt_two_pair_multiply(weight, limiting_base_numerator),
        _sqrt_two_pair_subtract(two, weight),
    )
    limiting_recursive_floor = _sqrt_two_pair_multiply(
        weight,
        _sqrt_two_pair_subtract(
            _sqrt_two_pair_multiply(sqrt_two, beta),
            alpha,
        ),
    )
    residual_coefficient = _sqrt_two_pair_multiply(
        _sqrt_two_pair_subtract(alpha, beta),
        limiting_base_floor,
    )
    tail_coefficient = _sqrt_two_pair(Fraction(-2, 3), Fraction(2, 3))
    global_coefficient = _sqrt_two_pair_add(
        tail_coefficient,
        residual_coefficient,
    )

    assert limiting_base_floor == _sqrt_two_pair(
        Fraction(68, 9),
        Fraction(-16, 3),
    )
    assert _sqrt_two_pair_subtract(
        limiting_recursive_floor,
        limiting_base_floor,
    ) == _sqrt_two_pair_scale(weight, Fraction(1, 9))
    assert residual_coefficient == _sqrt_two_pair(
        Fraction(-140, 27),
        Fraction(11, 3),
    )
    assert global_coefficient == _sqrt_two_pair(
        Fraction(-158, 27),
        Fraction(13, 3),
    )

    old_beta = _sqrt_two_pair(Fraction(2, 5))
    old_weight = _sqrt_two_pair(Fraction(1, 2))
    old_base_floor = _sqrt_two_pair_divide(
        _sqrt_two_pair_multiply(
            old_weight,
            _sqrt_two_pair_subtract(
                _sqrt_two_pair_subtract(
                    _sqrt_two_pair_scale(
                        _sqrt_two_pair_multiply(sqrt_two, old_beta),
                        2,
                    ),
                    one,
                ),
                _sqrt_two_pair_multiply(
                    old_weight,
                    _sqrt_two_pair_multiply(old_beta, old_beta),
                ),
            ),
        ),
        _sqrt_two_pair_subtract(two, old_weight),
    )
    old_coefficient = _sqrt_two_pair_multiply(
        _sqrt_two_pair_subtract(alpha, old_beta),
        old_base_floor,
    )
    assert old_coefficient == _sqrt_two_pair(
        Fraction(389, 375),
        Fraction(-275, 375),
    )

    finite_n = 141
    finite_r = 58
    center = finite_n + finite_r
    label = 56
    old_finite_base = _sqrt_two_pair_divide(
        _sqrt_two_pair_multiply(
            old_weight,
            _sqrt_two_pair_subtract(
                _sqrt_two_pair(4 * center * label - center * center),
                _sqrt_two_pair_scale(old_weight, 2 * label * label),
            ),
        ),
        _sqrt_two_pair_scale(
            _sqrt_two_pair_subtract(two, old_weight),
            2,
        ),
    )
    old_finite_recursive = _sqrt_two_pair_scale(
        old_weight,
        (center - 1) * label - finite_n * (finite_r - 1),
    )
    assert old_finite_base == _sqrt_two_pair(
        Fraction(4 * center * label - center * center - label * label, 6)
    )
    assert old_finite_recursive == _sqrt_two_pair(
        Fraction((center - 1) * label - finite_n * (finite_r - 1), 2)
    )
    assert _sqrt_two_pair_subtract(
        residual_coefficient,
        old_coefficient,
    ) == _sqrt_two_pair(
        Fraction(-21001, 3375),
        Fraction(14850, 3375),
    )

    assert 2 * 99**2 - 140**2 == 2
    assert 2 * 14_850**2 - 21_001**2 == 2_999
    assert _sqrt_two_pair_sign(residual_coefficient) > 0
    assert _sqrt_two_pair_sign(
        _sqrt_two_pair_subtract(residual_coefficient, old_coefficient)
    ) > 0


def test_first_linear_density_optimized_finite_bounds_are_exact() -> None:
    """Audit every rounded finite ingredient on a bounded exact range."""
    alpha = _sqrt_two_pair(-1, 1)
    beta = _sqrt_two_pair(Fraction(-2, 3), Fraction(3, 4))
    weight = _sqrt_two_pair(Fraction(88, 49), Fraction(-48, 49))
    two_minus_weight = _sqrt_two_pair_subtract(_sqrt_two_pair(2), weight)
    limiting_floor = _sqrt_two_pair(Fraction(68, 9), Fraction(-16, 3))
    residual_coefficient = _sqrt_two_pair(
        Fraction(-140, 27),
        Fraction(11, 3),
    )
    residual_quadratic = _sqrt_two_pair(
        Fraction(1097, 72),
        Fraction(-32, 3),
    )
    global_coefficient = _sqrt_two_pair(
        Fraction(-158, 27),
        Fraction(13, 3),
    )
    global_quadratic = _sqrt_two_pair(
        Fraction(136, 9),
        Fraction(-32, 3),
    )

    for n in range(99, 1_001):
        r = isqrt(2 * n * n) - n
        cutoff = 1 + (isqrt(162 * n * n) - 8 * n) // 12
        center = n + r
        prefix_length = r - cutoff
        tail_size = n - r + 1
        assert prefix_length >= 1

        beta_times_n = _sqrt_two_pair_scale(beta, n)
        assert _sqrt_two_pair_sign(
            _sqrt_two_pair_subtract(beta_times_n, _sqrt_two_pair(cutoff - 1))
        ) > 0
        assert _sqrt_two_pair_sign(
            _sqrt_two_pair_subtract(_sqrt_two_pair(cutoff), beta_times_n)
        ) > 0
        assert _sqrt_two_pair_sign(
            _sqrt_two_pair_subtract(
                _sqrt_two_pair(r),
                _sqrt_two_pair_scale(alpha, n),
            )
        ) < 0

        base_floor_inner = _sqrt_two_pair_subtract(
            _sqrt_two_pair(4 * center * cutoff - center * center),
            _sqrt_two_pair_scale(weight, 2 * cutoff * cutoff),
        )
        base_floor = _sqrt_two_pair_divide(
            _sqrt_two_pair_multiply(weight, base_floor_inner),
            _sqrt_two_pair_scale(two_minus_weight, 2),
        )
        recursive_floor = _sqrt_two_pair_scale(
            weight,
            (center - 1) * cutoff - n * (r - 1),
        )
        assert _sqrt_two_pair_ge(recursive_floor, base_floor)
        assert _sqrt_two_pair_ge(
            base_floor,
            _sqrt_two_pair_scale(limiting_floor, n * n),
        )

        alternating_excess = (
            tail_size * (tail_size - 2) // 8
            if tail_size % 2 == 0
            else (tail_size * tail_size - 1) // 8
        )
        exact_residual_floor = _sqrt_two_pair_subtract(
            _sqrt_two_pair_scale(base_floor, prefix_length),
            _sqrt_two_pair(alternating_excess),
        )
        coarse_residual_floor = _sqrt_two_pair_subtract(
            _sqrt_two_pair_scale(residual_coefficient, n**3),
            _sqrt_two_pair_scale(residual_quadratic, n * n),
        )
        assert _sqrt_two_pair_ge(
            exact_residual_floor,
            coarse_residual_floor,
        )

        pairing_floor = sum(
            label * (center - label) for label in range(r, n + 1)
        )
        exact_global_floor = _sqrt_two_pair_add(
            _sqrt_two_pair(pairing_floor),
            _sqrt_two_pair_scale(base_floor, prefix_length),
        )
        coarse_global_floor = _sqrt_two_pair_subtract(
            _sqrt_two_pair_scale(global_coefficient, n**3),
            _sqrt_two_pair_scale(global_quadratic, n * n),
        )
        assert _sqrt_two_pair_ge(exact_global_floor, coarse_global_floor)

    residual_at_572 = _sqrt_two_pair_subtract(
        _sqrt_two_pair_scale(residual_coefficient, 572),
        residual_quadratic,
    )
    assert residual_at_572 == _sqrt_two_pair(
        Fraction(-643931, 216),
        Fraction(455328, 216),
    )
    assert 2 * 455_328**2 - 643_931**2 == 42_407
    assert _sqrt_two_pair_sign(residual_at_572) > 0


def test_consecutive_tail_block_keeps_admissible_domino_prefixes() -> None:
    m, n, r = 2, 7, 4
    ell = m + r - 1
    current = (7, 5, 6)
    base_score = _cyclic_product_sum(current)
    prefixes = [0]

    for label in range(ell - 1, m - 1, -1):
        target_edge = {label + 1, label + 2}
        position = next(
            position
            for position, left in enumerate(current)
            if {left, current[(position + 1) % len(current)]} == target_edge
        )
        left = current[position]
        right = current[(position + 1) % len(current)]
        old_edges = set(_undirected_cycle_edge_signature(current))
        split_edge = (min(left, right), max(left, right))
        inserted = _split_cycle_edge_oracle(current, position, label)
        correction = label * (left + right) - left * right
        new_edges = set(_undirected_cycle_edge_signature(inserted))

        assert correction == label * label - 2
        assert _cyclic_product_sum(inserted) == (
            _cyclic_product_sum(current) + correction
        )
        assert new_edges == (
            old_edges - {split_edge}
        ) | {
            (min(left, label), max(left, label)),
            (min(label, right), max(label, right)),
        }
        assert _is_loopless_spanning_cycle_signature(
            tuple(sorted(new_edges)),
            tuple(range(label, n + 1)),
        )

        prefixes.append(prefixes[-1] + correction)
        current = inserted

    exact_envelope = sum(
        max(0, label * label - 2) for label in range(m, ell)
    )
    induced_scores = tuple(
        _cyclic_product_sum(
            tuple(label for label in current if label >= threshold)
        )
        for threshold in range(ell, m - 1, -1)
    )

    assert tuple(prefixes) == (0, 14, 21, 23)
    assert induced_scores == tuple(base_score + prefix for prefix in prefixes)
    assert max(prefixes) == exact_envelope == 23


def test_consecutive_tail_block_rejects_two_label_inner_cycle() -> None:
    with pytest.raises(AssertionError):
        _consecutive_tail_block_oracle(1, 5, 4)


def test_lambda9_lower_bound_oracle_covers_all_sixty_tail_classes() -> None:
    orders = _six_label_dihedral_orders_oracle()
    rows = []
    for order in orders:
        s6_score = _cyclic_product_sum(order)
        s5_order = tuple(label for label in order if label != 4)
        s5_score = _cyclic_product_sum(s5_order)
        rows.append((max(s6_score, s5_score), order, s6_score, s5_score))

    assert len(orders) == 60
    assert len(set(orders)) == 60
    assert min(row[0] for row in rows) == 239
    assert [row for row in rows if row[0] == 239] == [
        (239, (9, 4, 7, 6, 8, 5), 239, 238)
    ]
    assert [row for row in rows if row[2] < 239] == [
        (242, (9, 4, 8, 6, 7, 5), 238, 242)
    ]


def test_lambda9_witness_records_every_maximizing_subset_exactly() -> None:
    core_order = (9, 2, 3, 5, 8, 6, 7, 4)
    scores = _literal_induced_label_subset_scores(core_order)
    expected_by_size = {
        1: (81, frozenset({9})),
        2: (144, frozenset({8, 9})),
        3: (191, frozenset({7, 8, 9})),
        4: (225, frozenset({6, 7, 8, 9})),
        5: (238, frozenset({5, 6, 7, 8, 9})),
        6: (239, frozenset({4, 5, 6, 7, 8, 9})),
        7: (236, frozenset({3, 4, 5, 6, 7, 8, 9})),
        8: (233, frozenset({2, 3, 4, 5, 6, 7, 8, 9})),
    }

    assert len(scores) == 2**len(core_order) - 1 == 255
    for subset_size, (expected_score, expected_subset) in expected_by_size.items():
        row = {
            subset: score
            for subset, score in scores.items()
            if len(subset) == subset_size
        }
        row_maximum = max(row.values())
        assert row_maximum == expected_score
        assert {subset for subset, score in row.items() if score == row_maximum} == {
            expected_subset
        }

    maximum = max(scores.values())
    assert maximum == 239
    assert {subset for subset, score in scores.items() if score == maximum} == {
        frozenset({4, 5, 6, 7, 8, 9})
    }
    assert _cyclic_product_sum((9, 5, 8, 6, 7, 4)) == (
        9 * 5 + 5 * 8 + 8 * 6 + 6 * 7 + 7 * 4 + 4 * 9
    ) == 239


def test_lambda9_core_oracle_classifies_all_2520_dihedral_classes() -> None:
    expected_minimizer_orders = (
        (9, 2, 3, 5, 8, 6, 7, 4),
        (9, 2, 4, 7, 3, 6, 8, 5),
        (9, 2, 4, 7, 6, 3, 8, 5),
        (9, 2, 4, 7, 6, 8, 3, 5),
        (9, 2, 4, 7, 6, 8, 5, 3),
        (9, 2, 5, 3, 8, 6, 7, 4),
        (9, 2, 5, 8, 3, 6, 7, 4),
        (9, 2, 5, 8, 6, 3, 7, 4),
        (9, 3, 2, 5, 8, 6, 7, 4),
        (9, 3, 5, 2, 8, 6, 7, 4),
        (9, 3, 5, 8, 2, 6, 7, 4),
        (9, 3, 5, 8, 6, 2, 7, 4),
        (9, 3, 5, 8, 6, 7, 2, 4),
        (9, 4, 2, 7, 3, 6, 8, 5),
        (9, 4, 2, 7, 6, 3, 8, 5),
        (9, 4, 2, 7, 6, 8, 3, 5),
        (9, 4, 7, 2, 3, 6, 8, 5),
        (9, 4, 7, 2, 6, 3, 8, 5),
        (9, 4, 7, 2, 6, 8, 3, 5),
        (9, 4, 7, 3, 2, 6, 8, 5),
        (9, 4, 7, 3, 6, 2, 8, 5),
        (9, 4, 7, 3, 6, 8, 2, 5),
        (9, 4, 7, 6, 2, 3, 8, 5),
        (9, 4, 7, 6, 2, 8, 3, 5),
        (9, 4, 7, 6, 3, 2, 8, 5),
        (9, 4, 7, 6, 3, 8, 2, 5),
        (9, 4, 7, 6, 8, 2, 3, 5),
        (9, 4, 7, 6, 8, 3, 2, 5),
    )
    six_label_subset = (4, 5, 6, 7, 8, 9)
    full_core_subset = (2, 3, 4, 5, 6, 7, 8, 9)
    exceptional_order = (9, 4, 7, 6, 8, 3, 2, 5)

    forced_six_cycle = (9, 5, 8, 6, 7, 4)
    parameterized_orders = []
    for three_gap in range(4):
        seven_cycle = (
            forced_six_cycle[: three_gap + 1]
            + (3,)
            + forced_six_cycle[three_gap + 1 :]
        )
        for two_gap in range(7):
            oriented_order = (
                seven_cycle[: two_gap + 1]
                + (2,)
                + seven_cycle[two_gap + 1 :]
            )
            reflected_order = (
                oriented_order[0],
                *reversed(oriented_order[1:]),
            )
            parameterized_orders.append(
                oriented_order
                if oriented_order[1] < oriented_order[-1]
                else reflected_order
            )

    assert len(parameterized_orders) == len(set(parameterized_orders)) == 28
    assert tuple(sorted(parameterized_orders)) == expected_minimizer_orders
    assert len(parameterized_orders) * 8 == 224

    orders = _nine_core_dihedral_orders_oracle()
    rows = tuple(
        (order, *_literal_score_and_maximizers(order)) for order in orders
    )
    payload = "\n".join(
        ",".join(map(str, order))
        + f"|{score}|"
        + ";".join(",".join(map(str, subset)) for subset in maximizers)
        for order, score, maximizers in rows
    ).encode("ascii")

    assert len(orders) == len(set(orders)) == 2_520
    assert len(rows) * (2**8 - 1) == 642_600
    assert len(payload) == 84_395
    assert hashlib.sha256(payload).hexdigest() == (
        "557226668a82f6489274571148572076e373d49baefaa61e6d1f5a458bb857a2"
    )

    optimum = min(score for _order, score, _maximizers in rows)
    minimizer_rows = tuple(row for row in rows if row[1] == optimum)
    expected_minimizer_rows = tuple(
        (
            order,
            239,
            (
                (six_label_subset, full_core_subset)
                if order == exceptional_order
                else (six_label_subset,)
            ),
        )
        for order in expected_minimizer_orders
    )

    assert optimum == 239
    assert minimizer_rows == expected_minimizer_rows
    assert len(minimizer_rows) == 28
    assert sum(len(maximizers) == 1 for _order, _score, maximizers in rows) == 2_412
    assert sum(len(maximizers) == 2 for _order, _score, maximizers in rows) == 108


def test_lambda10_pairing_equality_branches_and_insertions_are_exact() -> None:
    labels = (5, 6, 7, 8, 9, 10)
    expected_pairings = {
        320: (
            ((5, 10), (5, 10), (6, 9), (6, 9), (7, 8), (7, 8)),
        ),
        321: (
            ((5, 9), (5, 10), (6, 9), (6, 10), (7, 8), (7, 8)),
            ((5, 10), (5, 10), (6, 8), (6, 9), (7, 8), (7, 9)),
            ((5, 10), (5, 10), (6, 9), (6, 9), (7, 7), (8, 8)),
        ),
        322: (
            ((5, 9), (5, 9), (6, 10), (6, 10), (7, 8), (7, 8)),
            ((5, 9), (5, 10), (6, 8), (6, 10), (7, 8), (7, 9)),
            ((5, 9), (5, 10), (6, 9), (6, 10), (7, 7), (8, 8)),
            ((5, 10), (5, 10), (6, 8), (6, 8), (7, 9), (7, 9)),
        ),
    }
    cycle_pairing = expected_pairings[322][1]

    pairing_minimum, near_minimum_pairings = (
        _near_minimum_duplicated_pairings_oracle(labels, ceiling=322)
    )
    assert pairing_minimum == 320
    assert near_minimum_pairings == expected_pairings
    assert tuple(
        (score, signature)
        for score, signatures in near_minimum_pairings.items()
        for signature in signatures
        if _is_loopless_spanning_cycle_signature(signature, labels)
    ) == ((322, cycle_pairing),)

    def edge_corrections(
        cycle: tuple[int, ...],
    ) -> tuple[tuple[tuple[int, int], int], ...]:
        return tuple(
            sorted(
                (
                    tuple(sorted((left, right))),
                    4 * (left + right) - left * right,
                )
                for left, right in zip(
                    cycle,
                    cycle[1:] + cycle[:1],
                    strict=True,
                )
            )
        )

    tail_322 = (10, 5, 9, 7, 8, 6)
    tail_322_corrections = (
        ((5, 9), 11),
        ((5, 10), 10),
        ((6, 8), 8),
        ((6, 10), 4),
        ((7, 8), 4),
        ((7, 9), 1),
    )
    assert _cyclic_product_sum(tail_322) == 322
    assert _undirected_cycle_edge_signature(tail_322) == cycle_pairing
    assert edge_corrections(tail_322) == tail_322_corrections
    assert [
        edge
        for edge, correction in tail_322_corrections
        if max(322, 322 + correction) == 323
    ] == [(7, 9)]

    all_corrections = {
        edge: 4 * sum(edge) - edge[0] * edge[1]
        for edge in itertools.combinations(labels, 2)
    }
    assert all_corrections == {
        (5, 6): 14,
        (5, 7): 13,
        (5, 8): 12,
        (5, 9): 11,
        (5, 10): 10,
        (6, 7): 10,
        (6, 8): 8,
        (6, 9): 6,
        (6, 10): 4,
        (7, 8): 4,
        (7, 9): 1,
        (7, 10): -2,
        (8, 9): -4,
        (8, 10): -8,
        (9, 10): -14,
    }
    assert {
        edge: correction
        for edge, correction in all_corrections.items()
        if correction <= 0
    } == {
        (7, 10): -2,
        (8, 9): -4,
        (8, 10): -8,
        (9, 10): -14,
    }

    fixed_edge_rows = {
        (7, 10): (
            253,
            ((5, 9), (5, 10), (6, 8), (6, 9), (7, 8)),
        ),
        (8, 9): (
            251,
            ((5, 10), (5, 10), (6, 8), (6, 9), (7, 7)),
        ),
        (8, 10): (
            246,
            ((5, 9), (5, 10), (6, 8), (6, 9), (7, 7)),
        ),
        (9, 10): (
            240,
            ((5, 9), (5, 10), (6, 8), (6, 8), (7, 7)),
        ),
    }
    duplicated = [label for label in labels for _copy in range(2)]
    fixed_edge_full_signatures = {}
    for edge, (expected_floor, expected_signature) in fixed_edge_rows.items():
        residual = duplicated.copy()
        residual.remove(edge[0])
        residual.remove(edge[1])
        floor, signatures = _low_pairing_signatures_oracle(
            tuple(residual),
            ceiling=expected_floor,
        )
        assert floor == expected_floor
        assert signatures == {expected_floor: (expected_signature,)}
        fixed_edge_full_signatures[edge] = tuple(
            sorted((*expected_signature, edge))
        )

    assert {
        edge: edge[0] * edge[1] + fixed_edge_rows[edge][0]
        for edge in fixed_edge_rows
    } == {
        (7, 10): 323,
        (8, 9): 323,
        (8, 10): 326,
        (9, 10): 330,
    }
    assert _is_loopless_spanning_cycle_signature(
        fixed_edge_full_signatures[(7, 10)], labels
    )
    assert not _is_loopless_spanning_cycle_signature(
        fixed_edge_full_signatures[(8, 9)], labels
    )

    tail_323 = (10, 5, 9, 6, 8, 7)
    tail_323_corrections = (
        ((5, 9), 11),
        ((5, 10), 10),
        ((6, 8), 8),
        ((6, 9), 6),
        ((7, 8), 4),
        ((7, 10), -2),
    )
    assert _cyclic_product_sum(tail_323) == 323
    assert _undirected_cycle_edge_signature(tail_323) == (
        fixed_edge_full_signatures[(7, 10)]
    )
    assert edge_corrections(tail_323) == tail_323_corrections
    assert [
        edge
        for edge, correction in tail_323_corrections
        if max(323, 323 + correction) == 323
    ] == [(7, 10)]

    equality_orders = (
        ((10, 4, 7, 8, 6, 9, 5), 321, 323),
        ((10, 5, 9, 4, 7, 8, 6), 323, 322),
    )
    assert _undirected_cycle_edge_signature((10, 5, 9, 6, 8, 7, 4)) == (
        _undirected_cycle_edge_signature(equality_orders[0][0])
    )
    for order, expected_s7, expected_s6 in equality_orders:
        tail = tuple(label for label in order if label != 4)
        assert order[0] == 10 and order[1] < order[-1]
        assert _cyclic_product_sum(order) == expected_s7
        assert _cyclic_product_sum(tail) == expected_s6
        assert max(expected_s7, expected_s6) == 323


def test_lambda10_equality_class_oracle_covers_all_360_tail_classes() -> None:
    orders = _seven_label_dihedral_orders_oracle()
    rows = []
    for order in orders:
        s7_score = _cyclic_product_sum(order)
        s6_order = tuple(label for label in order if label != 4)
        s6_score = _cyclic_product_sum(s6_order)
        rows.append((max(s7_score, s6_score), order, s7_score, s6_score))

    assert len(orders) == len(set(orders)) == 360
    assert min(row[0] for row in rows) == 323
    assert [row for row in rows if row[0] == 323] == [
        (323, (10, 4, 7, 8, 6, 9, 5), 321, 323),
        (323, (10, 5, 9, 4, 7, 8, 6), 323, 322),
    ]


def test_lambda10_label_three_insertions_have_exact_shortcut_certificates() -> None:
    """Check the structural certificates without enumerating label subsets."""

    cases = (
        (
            "first",
            (10, 4, 7, 8, 6, 9, 5),
            321,
            (10, 7, 8, 6, 9, 5),
            (
                ((4, 10), 323, 323, ((10, (3, 4), 7, 0),)),
                ((4, 7), 326, 326, ()),
                (
                    (7, 8),
                    310,
                    323,
                    ((10, (4,), 7, 2), (7, (3,), 8, 11)),
                ),
                (
                    (6, 8),
                    315,
                    323,
                    ((10, (4,), 7, 2), (8, (3,), 6, 6)),
                ),
                (
                    (6, 9),
                    312,
                    323,
                    ((10, (4,), 7, 2), (6, (3,), 9, 9)),
                ),
                (
                    (5, 9),
                    318,
                    323,
                    ((10, (4,), 7, 2), (9, (3,), 5, 3)),
                ),
                (
                    (5, 10),
                    316,
                    323,
                    (
                        (10, (4,), 7, 2),
                        (9, (5, 3), 10, 0),
                        (5, (3,), 10, 5),
                    ),
                ),
            ),
        ),
        (
            "second",
            (10, 5, 9, 4, 7, 8, 6),
            323,
            (10, 5, 9, 4, 7, 8, 6),
            (
                (
                    (5, 10),
                    318,
                    323,
                    ((10, (3,), 5, 5), (10, (3, 5), 9, 0)),
                ),
                ((5, 9), 320, 323, ((5, (3,), 9, 3),)),
                ((4, 9), 326, 326, ()),
                ((4, 7), 328, 328, ()),
                ((7, 8), 312, 323, ((7, (3,), 8, 11),)),
                ((6, 8), 317, 323, ((8, (3,), 6, 6),)),
                ((6, 10), 311, 323, ((6, (3,), 10, 12),)),
            ),
        ),
    )

    certificate_rows = []
    for cycle_name, cycle, expected_cycle_score, witness, expected_rows in cases:
        cycle_score = _cyclic_product_sum(cycle)
        witness_score = _cyclic_product_sum(witness)
        assert cycle_score == expected_cycle_score
        assert witness_score == 323
        assert len(expected_rows) == len(cycle) == 7

        actual_rows = []
        for left_position, left in enumerate(cycle):
            right = cycle[(left_position + 1) % len(cycle)]
            gap = tuple(sorted((left, right)))
            inserted_order = (
                cycle[: left_position + 1]
                + (3,)
                + cycle[left_position + 1 :]
            )
            full_score = _cyclic_product_sum(inserted_order)

            insertion_correction = 3 * (left + right) - left * right
            assert full_score == cycle_score + insertion_correction

            # Adjacent endpoints have the trivial gain zero.  The 48 arcs
            # below are every oriented shortcut that skips at least one label.
            nonnegative_gains = []
            for start_position in range(len(inserted_order)):
                for skipped_count in range(1, len(inserted_order) - 1):
                    arc = tuple(
                        inserted_order[
                            (start_position + offset) % len(inserted_order)
                        ]
                        for offset in range(skipped_count + 2)
                    )
                    arc_score = sum(
                        arc_left * arc_right
                        for arc_left, arc_right in zip(
                            arc[:-1], arc[1:], strict=True
                        )
                    )
                    gain = arc[0] * arc[-1] - arc_score
                    if gain >= 0:
                        nonnegative_gains.append(
                            (arc[0], arc[1:-1], arc[-1], gain)
                        )

            positive_gain_total = sum(
                gain
                for _start, _skipped, _end, gain in nonnegative_gains
                if gain > 0
            )
            certificate_upper_bound = max(
                max(label * label for label in inserted_order),
                full_score + positive_gain_total,
            )
            explicit_lower_bound = max(full_score, witness_score)
            assert certificate_upper_bound == explicit_lower_bound

            actual_rows.append(
                (
                    gap,
                    full_score,
                    certificate_upper_bound,
                    tuple(nonnegative_gains),
                )
            )
            certificate_rows.append((cycle_name, gap, certificate_upper_bound))

        assert tuple(actual_rows) == expected_rows

    assert len(certificate_rows) == 14
    excluded = {
        (cycle_name, gap)
        for cycle_name, gap, certified_score in certificate_rows
        if certified_score > 323
    }
    assert excluded == {
        ("first", (4, 7)),
        ("second", (4, 9)),
        ("second", (4, 7)),
    }
    assert all(
        certified_score == 323
        for cycle_name, gap, certified_score in certificate_rows
        if (cycle_name, gap) not in excluded
    )


def test_lambda10_label_three_gap_oracle_checks_all_fourteen_insertions() -> None:
    """Enumerate all subsets test-locally, independently of the certificate."""

    full_subset = (3, 4, 5, 6, 7, 8, 9, 10)
    six_label_subset = (5, 6, 7, 8, 9, 10)
    seven_label_subset = (4, 5, 6, 7, 8, 9, 10)
    expected_rows = (
        (
            "first",
            (4, 10),
            323,
            (six_label_subset, full_subset),
        ),
        ("first", (4, 7), 326, (full_subset,)),
        ("first", (7, 8), 323, (six_label_subset,)),
        ("first", (6, 8), 323, (six_label_subset,)),
        ("first", (6, 9), 323, (six_label_subset,)),
        ("first", (5, 9), 323, (six_label_subset,)),
        ("first", (5, 10), 323, (six_label_subset,)),
        ("second", (5, 10), 323, (seven_label_subset,)),
        ("second", (5, 9), 323, (seven_label_subset,)),
        ("second", (4, 9), 326, (full_subset,)),
        ("second", (4, 7), 328, (full_subset,)),
        ("second", (7, 8), 323, (seven_label_subset,)),
        ("second", (6, 8), 323, (seven_label_subset,)),
        ("second", (6, 10), 323, (seven_label_subset,)),
    )
    cycles = (
        ("first", (10, 4, 7, 8, 6, 9, 5)),
        ("second", (10, 5, 9, 4, 7, 8, 6)),
    )

    rows = []
    inserted_orders = []
    subset_evaluations = 0
    for cycle_name, cycle in cycles:
        for left_position, left in enumerate(cycle):
            right = cycle[(left_position + 1) % len(cycle)]
            gap = tuple(sorted((left, right)))
            inserted_order = (
                cycle[: left_position + 1]
                + (3,)
                + cycle[left_position + 1 :]
            )
            assert set(inserted_order) == set(range(3, 11))
            assert 2 not in inserted_order

            scores = _literal_induced_label_subset_scores(inserted_order)
            assert len(scores) == 2**len(inserted_order) - 1 == 255
            maximum = max(scores.values())
            maximizers = tuple(
                sorted(
                    (
                        tuple(sorted(subset))
                        for subset, score in scores.items()
                        if score == maximum
                    ),
                    key=lambda subset: (len(subset), subset),
                )
            )

            rows.append((cycle_name, gap, maximum, maximizers))
            inserted_orders.append(inserted_order)
            subset_evaluations += len(scores)

    assert len(rows) == len(set(inserted_orders)) == 14
    assert subset_evaluations == 14 * (2**8 - 1) == 3_570
    assert tuple(rows) == expected_rows

    excluded = {
        (cycle_name, gap)
        for cycle_name, gap, score, _maximizers in rows
        if score > 323
    }
    assert excluded == {
        ("first", (4, 7)),
        ("second", (4, 9)),
        ("second", (4, 7)),
    }
    assert all(
        score == 323
        for cycle_name, gap, score, _maximizers in rows
        if (cycle_name, gap) not in excluded
    )


def test_lambda10_label_two_gap_oracle_checks_all_eighty_eight_insertions() -> None:
    """Check every surviving core and argmax without production code."""

    six_label_subset = tuple(range(5, 11))
    seven_label_subset = tuple(range(4, 11))
    eight_label_subset = tuple(range(3, 11))
    full_core_subset = tuple(range(2, 11))
    parent_cases = (
        (
            "first",
            (10, 4, 7, 8, 6, 9, 5),
            {frozenset((4, 7))},
        ),
        (
            "second",
            (10, 5, 9, 4, 7, 8, 6),
            {frozenset((4, 9)), frozenset((4, 7))},
        ),
    )

    surviving_partial_orders = []
    for cycle_name, cycle, excluded_three_gaps in parent_cases:
        for left_position, left in enumerate(cycle):
            right = cycle[(left_position + 1) % len(cycle)]
            three_gap = frozenset((left, right))
            if three_gap in excluded_three_gaps:
                continue
            partial_order = (
                cycle[: left_position + 1]
                + (3,)
                + cycle[left_position + 1 :]
            )
            surviving_partial_orders.append(
                (cycle_name, three_gap, partial_order)
            )

    assert len(surviving_partial_orders) == 11
    assert len({row[2] for row in surviving_partial_orders}) == 11
    assert len(
        {_dihedral_cycle_key_oracle(row[2]) for row in surviving_partial_orders}
    ) == 11

    rows = []
    core_orders = []
    subset_evaluations = 0
    for cycle_name, three_gap, partial_order in surviving_partial_orders:
        for left_position, left in enumerate(partial_order):
            right = partial_order[(left_position + 1) % len(partial_order)]
            two_gap = frozenset((left, right))
            core_order = (
                partial_order[: left_position + 1]
                + (2,)
                + partial_order[left_position + 1 :]
            )
            assert set(core_order) == set(range(2, 11))
            assert 1 not in core_order

            scores = _literal_induced_label_subset_scores(core_order)
            assert len(scores) == 2**len(core_order) - 1 == 511
            maximum = max(scores.values())
            maximizers = tuple(
                sorted(
                    (
                        tuple(sorted(subset))
                        for subset, score in scores.items()
                        if score == maximum
                    ),
                    key=lambda subset: (len(subset), subset),
                )
            )

            exceptional = (
                cycle_name == "first"
                and three_gap == frozenset((4, 10))
                and two_gap == frozenset((3, 4))
            )
            if exceptional:
                assert core_order == (10, 3, 2, 4, 7, 8, 6, 9, 5)
                expected_score = 325
                expected_maximizers = (full_core_subset,)
            elif cycle_name == "first" and three_gap == frozenset((4, 10)):
                expected_score = 323
                expected_maximizers = (six_label_subset, eight_label_subset)
            elif cycle_name == "first":
                expected_score = 323
                expected_maximizers = (six_label_subset,)
            else:
                expected_score = 323
                expected_maximizers = (seven_label_subset,)

            assert maximum == expected_score
            assert maximizers == expected_maximizers
            rows.append(
                (
                    cycle_name,
                    three_gap,
                    two_gap,
                    maximum,
                    maximizers,
                )
            )
            core_orders.append(core_order)
            subset_evaluations += len(scores)

    assert len(rows) == len(core_orders) == 11 * 8 == 88
    assert len(set(core_orders)) == 88
    assert subset_evaluations == 88 * (2**9 - 1) == 44_968

    core_class_keys = tuple(
        _dihedral_cycle_key_oracle(order) for order in core_orders
    )
    assert len(set(core_class_keys)) == 88
    assert sum(score == 325 for _name, _three, _two, score, _args in rows) == 1
    assert sum(score == 323 for _name, _three, _two, score, _args in rows) == 87

    minimizing_core_orders = tuple(
        order
        for order, row in zip(core_orders, rows, strict=True)
        if row[3] == 323
    )
    complete_class_keys = tuple(
        _dihedral_cycle_key_oracle(_insert_one_after(order, left_position))
        for order in minimizing_core_orders
        for left_position in range(len(order))
    )
    assert len(minimizing_core_orders) == 87
    assert len(complete_class_keys) == 87 * 9 == 783
    assert len(set(complete_class_keys)) == 783


def test_lambda10_witness_records_every_maximizing_subset_exactly() -> None:
    core_order = (10, 2, 3, 4, 7, 8, 6, 9, 5)
    scores = _literal_induced_label_subset_scores(core_order)
    expected_by_size = {
        1: (100, frozenset({10})),
        2: (180, frozenset({9, 10})),
        3: (242, frozenset({8, 9, 10})),
        4: (288, frozenset({7, 8, 9, 10})),
        5: (318, frozenset({6, 7, 8, 9, 10})),
        6: (323, frozenset({5, 6, 7, 8, 9, 10})),
        7: (321, frozenset({4, 5, 6, 7, 8, 9, 10})),
        8: (323, frozenset({3, 4, 5, 6, 7, 8, 9, 10})),
        9: (319, frozenset({2, 3, 4, 5, 6, 7, 8, 9, 10})),
    }

    assert len(scores) == 2**len(core_order) - 1 == 511
    for subset_size, (expected_score, expected_subset) in expected_by_size.items():
        row = {
            subset: score
            for subset, score in scores.items()
            if len(subset) == subset_size
        }
        row_maximum = max(row.values())
        assert row_maximum == expected_score
        assert {subset for subset, score in row.items() if score == row_maximum} == {
            expected_subset
        }

    maximum = max(scores.values())
    assert maximum == 323
    assert {subset for subset, score in scores.items() if score == maximum} == {
        frozenset({5, 6, 7, 8, 9, 10}),
        frozenset({3, 4, 5, 6, 7, 8, 9, 10}),
    }
    assert _cyclic_product_sum((10, 7, 8, 6, 9, 5)) == (
        10 * 7 + 7 * 8 + 8 * 6 + 6 * 9 + 9 * 5 + 5 * 10
    ) == 323
    assert _cyclic_product_sum((10, 3, 4, 7, 8, 6, 9, 5)) == (
        10 * 3
        + 3 * 4
        + 4 * 7
        + 7 * 8
        + 8 * 6
        + 6 * 9
        + 9 * 5
        + 5 * 10
    ) == 323


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
