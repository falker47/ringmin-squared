"""Independent bounded oracle for the KR1G relaxed-equality classification.

The oracle uses only exact integer arithmetic and the Python standard library.
It enumerates every Hamiltonian cycle on ``{0, ..., q - 1}``, once modulo
rotation and reversal, for ``3 <= q <= 10``.  It verifies the symbolic
classification of every equality pair ``(C, E')`` in the positive branch.

This script deliberately checks only the finite equality classification.  It
does not import project code, simulate KR1G histories, or serve as evidence
for the all-q proof or the asymptotic selected-prefix theorem.
"""

from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


Edge = tuple[int, int]
Cycle = tuple[int, ...]


GOLDEN_ROWS = {
    3: ((1, 1, 2),),
    4: ((1, 1, 2),),
    5: ((1, 2, 2), (2, 4, 6)),
    6: ((1, 2, 2), (2, 6, 8)),
    7: ((1, 2, 2), (2, 10, 14), (3, 20, 32)),
    8: ((1, 2, 2), (2, 12, 16), (3, 34, 48)),
    9: ((1, 2, 2), (2, 16, 22), (3, 74, 112), (4, 148, 240)),
    10: ((1, 2, 2), (2, 18, 24), (3, 102, 144), (4, 262, 384)),
}

GOLDEN_BAD_EDGE_HISTOGRAMS = {
    3: {0: 1},
    4: {0: 1, 2: 1},
    5: {1: 2, 2: 2},
    6: {1: 2, 2: 4, 3: 2},
    7: {1: 2, 2: 8, 3: 10, 4: 4},
    8: {1: 2, 2: 10, 3: 22, 4: 14},
    9: {1: 2, 2: 14, 3: 58, 4: 74, 5: 44},
    10: {1: 2, 2: 16, 3: 84, 4: 160, 5: 122},
}


def edge(u: int, v: int) -> Edge:
    """Return one canonical unordered edge."""
    if u == v:
        raise AssertionError("loops are not cycle edges")
    return (u, v) if u < v else (v, u)


def cycle_edges(cycle: Cycle) -> tuple[Edge, ...]:
    """Return the distinct cyclic edges in tuple order."""
    result = tuple(
        edge(cycle[index], cycle[(index + 1) % len(cycle)])
        for index in range(len(cycle))
    )
    if len(set(result)) != len(cycle):
        raise AssertionError("cycle has a repeated unordered edge")
    return result


def canonical_cycles(q: int):
    """Yield every labelled Hamiltonian cycle once modulo dihedral symmetry."""
    for tail in permutations(range(1, q)):
        if tail[0] < tail[-1]:
            yield (0, *tail)


def complementary_matching(q: int) -> frozenset[Edge]:
    """Return all distinct zero-deviation edges."""
    return frozenset(edge(index, q - 1 - index) for index in range(q // 2))


def unit_connectors(q: int) -> dict[Edge, tuple[int, int]]:
    """Map each deviation-one connector to its block index and sign."""
    block_count = (q + 1) // 2
    result: dict[Edge, tuple[int, int]] = {}
    for index in range(block_count - 1):
        positive = edge(index + 1, q - 1 - index)
        negative = edge(index, q - 2 - index)
        if positive in result or negative in result or positive == negative:
            raise AssertionError("unit connector collision")
        result[positive] = (index, 1)
        result[negative] = (index, -1)
    return result


def doubled_slack(q: int, item: Edge) -> int:
    """Return twice the relaxed slack, an exact integer square."""
    u, v = item
    return (u + v - (q - 1)) ** 2


def equality_predicate(
    q: int,
    ell: int,
    edges: frozenset[Edge],
    deleted: frozenset[Edge],
) -> bool:
    """Evaluate the symbolic iff classification."""
    matching = complementary_matching(q)
    units = frozenset(unit_connectors(q))
    retained = edges - deleted
    return (
        len(deleted) == ell
        and deleted <= edges
        and matching <= retained
        and retained - matching <= units
    )


def block_index(q: int, vertex: int) -> int:
    """Return the complementary block containing one vertex."""
    return min(vertex, q - 1 - vertex)


def verify_interval_components(
    q: int,
    ell: int,
    retained_units: frozenset[Edge],
) -> None:
    """Check the interval-path and constant-sign form of retained connectors."""
    block_count = (q + 1) // 2
    unit_data = unit_connectors(q)
    adjacency: list[set[int]] = [set() for _ in range(block_count)]
    signs: dict[tuple[int, int], int] = {}

    for item in retained_units:
        index, sign = unit_data[item]
        left = block_index(q, item[0])
        right = block_index(q, item[1])
        if {left, right} != {index, index + 1}:
            raise AssertionError("unit connector has incorrect blocks")
        key = (index, index + 1)
        if key in signs:
            raise AssertionError("parallel retained unit connectors")
        signs[key] = sign
        adjacency[index].add(index + 1)
        adjacency[index + 1].add(index)

    if len(retained_units) != block_count - ell:
        raise AssertionError("incorrect retained-unit cardinality")

    unseen = set(range(block_count))
    components: list[tuple[int, ...]] = []
    while unseen:
        root = min(unseen)
        stack = [root]
        component: set[int] = set()
        while stack:
            vertex = stack.pop()
            if vertex in component:
                continue
            component.add(vertex)
            unseen.discard(vertex)
            stack.extend(adjacency[vertex] - component)
        ordered = tuple(sorted(component))
        if ordered != tuple(range(ordered[0], ordered[-1] + 1)):
            raise AssertionError("retained component is not an interval")
        component_signs = {
            signs[(index, index + 1)] for index in range(ordered[0], ordered[-1])
        }
        if len(component_signs) > 1:
            raise AssertionError("retained interval changes sign")
        components.append(ordered)

    if len(components) != ell:
        raise AssertionError("incorrect number of retained interval components")


def predicted_pair_count(q: int, ell: int, edges: frozenset[Edge]) -> int:
    """Count equality edge sets from the symbolic formula for one cycle."""
    matching = complementary_matching(q)
    units = frozenset(unit_connectors(q))
    if not matching <= edges:
        return 0
    bad_count = len(edges - matching - units)
    connector_count = (q + 1) // 2
    if bad_count > ell:
        return 0
    return comb(connector_count - bad_count, ell - bad_count)


def verify_q(q: int) -> tuple[int, int, int, int]:
    """Exhaust every positive-branch row for one q."""
    block_count = (q + 1) // 2
    matching = complementary_matching(q)
    units = frozenset(unit_connectors(q))
    rows: list[tuple[int, int, int]] = []
    cycle_count = 0
    minimum_checks = 0
    subset_checks = 0
    histogram: Counter[int] = Counter()

    row_cycles = [0] * block_count
    row_pairs = [0] * block_count

    for cycle in canonical_cycles(q):
        cycle_count += 1
        ordered_edges = cycle_edges(cycle)
        edges = frozenset(ordered_edges)
        if len(edges) != q:
            raise AssertionError("Hamiltonian cycle edge count failed")
        if matching <= edges:
            histogram[len(edges - matching - units)] += 1

        weights = {item: doubled_slack(q, item) for item in ordered_edges}
        sorted_weights = sorted(weights.values())
        for ell in range(1, block_count):
            minimum_checks += 1
            target = block_count - ell
            fixed_cycle_minimum = sum(sorted_weights[: q - ell])
            if fixed_cycle_minimum < target:
                raise AssertionError("matching lower bound failed")

            formula_count = predicted_pair_count(q, ell, edges)
            if (fixed_cycle_minimum == target) != (formula_count > 0):
                raise AssertionError("cycle-level equality prediction failed")
            if formula_count == 0:
                continue

            row_cycles[ell] += 1
            direct_count = 0
            for deleted_count in range(ell + 1):
                for deleted_tuple in combinations(ordered_edges, deleted_count):
                    subset_checks += 1
                    deleted = frozenset(deleted_tuple)
                    retained_cost = sum(
                        value for item, value in weights.items() if item not in deleted
                    )
                    actual = retained_cost == target
                    predicted = equality_predicate(q, ell, edges, deleted)
                    if actual != predicted:
                        raise AssertionError(
                            f"q={q}, ell={ell}: pair classification failed"
                        )
                    if actual:
                        direct_count += 1
                        retained_units = (edges - deleted) - matching
                        verify_interval_components(q, ell, retained_units)

            if direct_count != formula_count:
                raise AssertionError("binomial equality-pair count failed")
            row_pairs[ell] += direct_count

    expected_cycles = factorial(q - 1) // 2
    if cycle_count != expected_cycles:
        raise AssertionError((q, cycle_count, expected_cycles))

    expected_matching_cycles = 2 ** (q // 2 - 1) * factorial(block_count - 1)
    if sum(histogram.values()) != expected_matching_cycles:
        raise AssertionError("complementary-matching cycle count failed")
    if dict(sorted(histogram.items())) != GOLDEN_BAD_EDGE_HISTOGRAMS[q]:
        raise AssertionError((q, histogram, GOLDEN_BAD_EDGE_HISTOGRAMS[q]))

    for ell in range(1, block_count):
        rows.append((ell, row_cycles[ell], row_pairs[ell]))
    if tuple(rows) != GOLDEN_ROWS[q]:
        raise AssertionError((q, rows, GOLDEN_ROWS[q]))

    for ell, equality_cycles, equality_pairs in rows:
        print(
            f"q={q:2d}, ell={ell}: cycles={cycle_count:6d}, "
            f"equality_cycles={equality_cycles:3d}, "
            f"equality_pairs={equality_pairs:3d} PASS"
        )
    return cycle_count, minimum_checks, subset_checks, sum(row_pairs)


def main() -> None:
    """Run the complete bounded classification oracle."""
    totals = [0, 0, 0, 0]
    row_count = 0
    equality_cycle_rows = 0
    for q in range(3, 11):
        result = verify_q(q)
        totals = [left + right for left, right in zip(totals, result, strict=True)]
        row_count += len(GOLDEN_ROWS[q])
        equality_cycle_rows += sum(row[1] for row in GOLDEN_ROWS[q])

    cycles, minimum_checks, subset_checks, equality_pairs = totals
    if cycles != 204_556:
        raise AssertionError(cycles)
    if row_count != 20 or minimum_checks != 815_188:
        raise AssertionError((row_count, minimum_checks))
    if equality_cycle_rows != 720 or equality_pairs != 1_066:
        raise AssertionError((equality_cycle_rows, equality_pairs))

    print(
        "PASS: "
        f"{cycles:,} canonical cycles, {row_count} positive-branch rows, "
        f"{minimum_checks:,} cycle minima, {equality_cycle_rows:,} "
        f"equality-cycle rows, {equality_pairs:,} equality pairs, and "
        f"{subset_checks:,} literal deletion subsets"
    )


if __name__ == "__main__":
    main()
