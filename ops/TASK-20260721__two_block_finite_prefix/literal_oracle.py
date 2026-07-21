"""Bounded exact oracle for the two-block finite-prefix accounting.

This dossier-local script imports no project, production, or test helper. It
exhausts every four-split history of one four-edge base, with two labels in
each block. Exact Fraction arithmetic checks the bridge identity, the
history-relative disjoint slack pools, original-root inheritance through
recursive child edges, charge multiplicity zero or one, all local floors, and
the resulting finite inequality.

The computation corroborates but does not prove the all-history theorem.
"""

from collections import Counter
from fractions import Fraction


N = 14
R = 11
SEPARATOR = 9
CENTER = N + R
BASE = (11, 12, 14, 13)
LABELS = (10, 9, 8, 7)
BLOCKS = ("upper", "upper", "lower", "lower")
BRIDGE = Fraction(1, 2)
UPPER_RAW = (Fraction(3, 5), Fraction(1, 5))
LOWER_RAW = (Fraction(4, 5), Fraction(2, 5))
WEIGHTS = tuple(BRIDGE + (1 - BRIDGE) * weight for weight in UPPER_RAW) + tuple(
    BRIDGE * weight for weight in LOWER_RAW
)
TARGET_PATH = ((11, 12), (12, 14), (9, 14), (8, 14))


def edges(cycle: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        tuple(sorted((cycle[index], cycle[(index + 1) % len(cycle)])))
        for index in range(len(cycle))
    )


def score(cycle: tuple[int, ...]) -> int:
    return sum(
        cycle[index] * cycle[(index + 1) % len(cycle)] for index in range(len(cycle))
    )


def split(cycle: tuple[int, ...], position: int, label: int) -> tuple[int, ...]:
    return cycle[: position + 1] + (label,) + cycle[position + 1 :]


def contract(cycle: tuple[int, ...], label: int) -> tuple[int, ...]:
    return tuple(entry for entry in cycle if entry != label)


def g_floor(weight: Fraction, label: int) -> Fraction:
    return (
        weight
        * (4 * CENTER * label - CENTER * CENTER - 2 * weight * label * label)
        / (2 * (2 - weight))
    )


def j_floor(weight: Fraction, label: int) -> Fraction:
    return weight * ((CENTER - 1) * label - N * (R - 1))


def require(
    condition: bool,
    message: str,
    path: tuple[tuple[int, int], ...] = (),
) -> None:
    if not condition:
        raise AssertionError(f"{message}; path={path!r}")


def audit() -> None:
    require(
        LABELS[:2] == tuple(range(R - 1, SEPARATOR - 1, -1)),
        "upper block is not contiguous",
    )
    require(
        LABELS[2:] == tuple(range(SEPARATOR - 1, LABELS[-1] - 1, -1)),
        "lower block is not contiguous",
    )
    require(set(LABELS[:2]).isdisjoint(LABELS[2:]), "blocks overlap")
    require(
        WEIGHTS == (Fraction(4, 5), Fraction(3, 5), Fraction(2, 5), Fraction(1, 5)),
        "unexpected effective weights",
    )
    require(
        1 >= WEIGHTS[0] >= WEIGHTS[1] >= BRIDGE >= WEIGHTS[2] >= WEIGHTS[3] >= 0,
        "bridge does not order the effective weights",
    )

    base_edges = frozenset(edges(BASE))
    require(len(BASE) == 4, "base is not minimal for two charges in each pool")
    require(len(base_edges) == len(BASE), "base is not a simple four-cycle")
    require(set(BASE) == set(range(R, N + 1)), "base has the wrong labels")
    base_score = score(BASE)
    pairing_floor = sum(label * (CENTER - label) for label in range(R, N + 1))
    base_slack = {edge: Fraction((sum(edge) - CENTER) ** 2, 2) for edge in base_edges}
    require(base_score == 625, "unexpected base score")
    require(pairing_floor == 620, "unexpected pairing floor")
    require(
        sum(base_slack.values()) == base_score - pairing_floor == 5,
        "base-slack identity failed",
    )
    require(
        Counter(base_slack.values()) == Counter({Fraction(2): 2, Fraction(1, 2): 2}),
        "unexpected base-slack distribution",
    )

    segment_floors = tuple(
        g_floor(weight, label) for weight, label in zip(WEIGHTS, LABELS, strict=True)
    )
    recursive_floors = tuple(
        j_floor(weight, label) for weight, label in zip(WEIGHTS, LABELS, strict=True)
    )
    require(
        segment_floors
        == (
            Fraction(215, 3),
            Fraction(381, 10),
            Fraction(619, 40),
            Fraction(277, 90),
        ),
        "unexpected segment floors",
    )
    require(
        recursive_floors
        == (
            Fraction(80),
            Fraction(228, 5),
            Fraction(104, 5),
            Fraction(28, 5),
        ),
        "unexpected recursive floors",
    )
    require(
        all(
            recursive > base
            for recursive, base in zip(recursive_floors, segment_floors, strict=True)
        ),
        "recursive floor does not dominate the base floor",
    )
    floor_sum = sum(segment_floors, Fraction())
    finite_bound = pairing_floor + floor_sum
    require(floor_sum == Fraction(9239, 72), "unexpected floor sum")
    require(finite_bound == Fraction(53879, 72), "unexpected finite bound")

    base_counts = [0, 0, 0, 0]
    recursive_counts = [0, 0, 0, 0]
    inserted_pair_counts = [0, 0, 0, 0]
    rooted_upper_counts = [0, 0, 0, 0]
    rooted_lower_counts = [0, 0, 0, 0]
    pool_histogram: Counter[tuple[int, int, int]] = Counter()
    final_cycles: set[tuple[int, ...]] = set()
    history_count = 0
    both_pool_count = 0
    all_charged_count = 0
    deep_cross_count = 0
    target_seen = False
    minima: dict[str, Fraction | None] = {
        "maximum": None,
        "mixed_maximum": None,
        "linear": None,
        "local": None,
        "weighted_excess": None,
        "selected_excess": None,
    }

    def record_minimum(name: str, value: Fraction) -> None:
        current = minima[name]
        if current is None or value < current:
            minima[name] = value

    def walk(
        cycle: tuple[int, ...],
        depth: int,
        edge_roots: dict[tuple[int, int], tuple[int, int]],
        charge_counts: dict[tuple[int, int], int],
        root_pools: dict[tuple[int, int], str],
        corrections: tuple[int, ...],
        contributions: tuple[Fraction, ...],
        path: tuple[tuple[int, int], ...],
        history: tuple[tuple[object, ...], ...],
    ) -> None:
        nonlocal all_charged_count
        nonlocal both_pool_count
        nonlocal deep_cross_count
        nonlocal history_count
        nonlocal target_seen

        current_edges = frozenset(edges(cycle))
        require(
            frozenset(edge_roots) == current_edges,
            "edge-root map does not cover the current cycle",
            path,
        )
        inserted_labels = frozenset(LABELS[:depth])
        for current_edge in current_edges:
            root = edge_roots[current_edge]
            require(root in base_edges, "edge has a non-original root", path)
            untouched = current_edge in base_edges
            recursive = bool(inserted_labels.intersection(current_edge))
            require(
                untouched != recursive,
                "global base/recursive invariant failed",
                path,
            )
            if untouched:
                require(root == current_edge, "untouched edge changed root", path)
                require(
                    charge_counts[root] == 0 and root not in root_pools,
                    "charged original edge was recreated",
                    path,
                )
            else:
                require(
                    charge_counts[root] == 1 and root in root_pools,
                    "recursive child lacks one charged original root",
                    path,
                )

        if depth == len(LABELS):
            history_count += 1
            require(
                set(cycle) == set(range(LABELS[-1], N + 1)),
                "final cycle has the wrong labels",
                path,
            )
            require(cycle not in final_cycles, "duplicate final cycle", path)
            final_cycles.add(cycle)
            recovered = cycle
            for label in reversed(LABELS):
                recovered = contract(recovered, label)
            require(recovered == BASE, "reverse contraction did not recover base", path)

            a10, a9, a8, a7 = corrections
            h10 = a10
            h9 = a10 + a9
            h8 = h9 + a8
            h7 = h8 + a7
            upper_maximum = max(0, h10, h9)
            lower_relative_maximum = max(0, a8, a8 + a7)
            lower_maximum = h9 + lower_relative_maximum
            selected_maximum = max(0, h10, h9, h8, h7)
            require(
                selected_maximum == max(upper_maximum, lower_maximum),
                "two-block maximum decomposition failed",
                path,
            )

            upper_linear = UPPER_RAW[0] * a10 + UPPER_RAW[1] * a9
            lower_linear = LOWER_RAW[0] * a8 + LOWER_RAW[1] * a7
            require(
                upper_maximum >= upper_linear,
                "upper finite-prefix inequality failed",
                path,
            )
            require(
                lower_relative_maximum >= lower_linear,
                "lower finite-prefix inequality failed",
                path,
            )
            mixed_maximum = (1 - BRIDGE) * upper_maximum + BRIDGE * lower_maximum
            linear = (1 - BRIDGE) * upper_linear + BRIDGE * (h9 + lower_linear)
            effective_linear = sum(
                weight * correction
                for weight, correction in zip(WEIGHTS, corrections, strict=True)
            )
            require(
                selected_maximum >= mixed_maximum >= linear,
                "bridge inequality failed",
                path,
            )
            require(
                linear == effective_linear == Fraction(h10 + h9 + h8 + h7, 5),
                "bridge-to-concatenated telescope failed",
                path,
            )

            upper_pool = frozenset(
                root for root, pool in root_pools.items() if pool == "upper"
            )
            lower_pool = frozenset(
                root for root, pool in root_pools.items() if pool == "lower"
            )
            unused_pool = base_edges - upper_pool - lower_pool
            require(
                not (upper_pool & lower_pool)
                and not (upper_pool & unused_pool)
                and not (lower_pool & unused_pool)
                and upper_pool | lower_pool | unused_pool == base_edges,
                "three-way original-edge partition failed",
                path,
            )
            require(
                all(count in (0, 1) for count in charge_counts.values()),
                "an original edge was charged more than once",
                path,
            )
            require(
                {root for root, count in charge_counts.items() if count == 1}
                == upper_pool | lower_pool,
                "charge counts disagree with the two pools",
                path,
            )
            if upper_pool and lower_pool:
                both_pool_count += 1
            if not unused_pool:
                all_charged_count += 1
            pool_histogram[(len(upper_pool), len(lower_pool), len(unused_pool))] += 1

            local_sum = sum(contributions, Fraction())
            unused_slack = sum((base_slack[root] for root in unused_pool), Fraction())
            weighted_excess = Fraction(base_score - pairing_floor) + linear
            selected_excess = Fraction(base_score - pairing_floor) + selected_maximum
            require(
                weighted_excess == local_sum + unused_slack,
                "two-pool one-use slack identity failed",
                path,
            )
            require(local_sum >= floor_sum, "local floors miss their sum", path)
            require(
                selected_excess >= weighted_excess >= floor_sum,
                "two-block finite inequality failed",
                path,
            )
            require(
                base_score + selected_maximum >= finite_bound,
                "literal objective misses the finite bound",
                path,
            )

            record_minimum("maximum", Fraction(selected_maximum))
            record_minimum("mixed_maximum", mixed_maximum)
            record_minimum("linear", linear)
            record_minimum("local", local_sum)
            record_minimum("weighted_excess", weighted_excess)
            record_minimum("selected_excess", selected_excess)

            if path == TARGET_PATH:
                target_seen = True
                require(
                    history[2][2] == history[3][2] == (12, 14),
                    "target descendants lost their upper original root",
                    path,
                )
                require(
                    history[2][3] == history[3][3] == "upper",
                    "target descendants changed root pool",
                    path,
                )
                require(
                    not frozenset(path[3]).intersection(LABELS[:2]),
                    "target deep child still touches an upper label",
                    path,
                )
            return

        label = LABELS[depth]
        block = BLOCKS[depth]
        weight = WEIGHTS[depth]
        require(
            set(cycle) == set(range(label + 1, N + 1)),
            "current cycle has the wrong labels",
            path,
        )

        for position, left in enumerate(cycle):
            right = cycle[(position + 1) % len(cycle)]
            current_edge = tuple(sorted((left, right)))
            root = edge_roots[current_edge]
            correction = label * (left + right) - left * right
            next_cycle = split(cycle, position, label)
            next_path = path + (current_edge,)
            require(
                contract(next_cycle, label) == cycle,
                "literal split does not contract to its parent",
                next_path,
            )
            require(
                score(next_cycle) == score(cycle) + correction,
                "literal score update failed",
                next_path,
            )

            child_edges = {
                tuple(sorted((left, label))),
                tuple(sorted((label, right))),
            }
            require(
                current_edge not in edges(next_cycle)
                and child_edges <= set(edges(next_cycle)),
                "literal child-edge replacement failed",
                next_path,
            )
            next_edge_roots = dict(edge_roots)
            del next_edge_roots[current_edge]
            for child in child_edges:
                next_edge_roots[child] = root

            next_charge_counts = dict(charge_counts)
            next_root_pools = dict(root_pools)
            if current_edge in base_edges:
                require(
                    root == current_edge and next_charge_counts[root] == 0,
                    "original edge was charged twice",
                    next_path,
                )
                next_charge_counts[root] += 1
                next_root_pools[root] = block
                contribution = base_slack[root] + weight * correction
                base_counts[depth] += 1
                split_kind = "base"
            else:
                require(
                    bool(inserted_labels.intersection(current_edge)),
                    "recursive edge lacks a previously inserted endpoint",
                    next_path,
                )
                root_pool = next_root_pools[root]
                contribution = weight * correction
                recursive_counts[depth] += 1
                if root_pool == "upper":
                    rooted_upper_counts[depth] += 1
                else:
                    rooted_lower_counts[depth] += 1
                if left < R and right < R:
                    inserted_pair_counts[depth] += 1
                if (
                    block == "lower"
                    and root_pool == "upper"
                    and not frozenset(current_edge).intersection(LABELS[:2])
                ):
                    deep_cross_count += 1
                split_kind = "recursive"

            require(
                contribution >= g_floor(weight, label) >= segment_floors[depth],
                "local segment floor failed",
                next_path,
            )
            if split_kind == "recursive":
                require(
                    contribution >= j_floor(weight, label) >= segment_floors[depth],
                    "recursive floor comparison failed",
                    next_path,
                )

            walk(
                next_cycle,
                depth + 1,
                next_edge_roots,
                next_charge_counts,
                next_root_pools,
                corrections + (correction,),
                contributions + (contribution,),
                next_path,
                history + ((label, current_edge, root, next_root_pools[root]),),
            )

    initial_roots = {edge: edge for edge in base_edges}
    initial_charges = {edge: 0 for edge in base_edges}
    walk(BASE, 0, initial_roots, initial_charges, {}, (), (), (), ())

    require(history_count == 840, "unexpected history count")
    require(len(final_cycles) == 840, "unexpected distinct final-cycle count")
    require(tuple(base_counts) == (4, 12, 48, 240), "unexpected base counts")
    require(
        tuple(recursive_counts) == (0, 8, 72, 600),
        "unexpected recursive counts",
    )
    require(
        tuple(inserted_pair_counts) == (0, 0, 8, 120),
        "unexpected inserted-pair counts",
    )
    require(
        tuple(rooted_upper_counts) == (0, 8, 72, 504),
        "unexpected upper-rooted recursive counts",
    )
    require(
        tuple(rooted_lower_counts) == (0, 0, 0, 96),
        "unexpected lower-rooted recursive counts",
    )
    require(deep_cross_count == 64, "unexpected deep cross-boundary count")
    require(
        pool_histogram
        == Counter(
            {
                (1, 0, 3): 96,
                (1, 1, 2): 192,
                (1, 2, 1): 48,
                (2, 0, 2): 240,
                (2, 1, 1): 240,
                (2, 2, 0): 24,
            }
        ),
        "unexpected two-pool histogram",
    )
    require(both_pool_count == 504, "unexpected both-pool history count")
    require(all_charged_count == 24, "unexpected all-charged history count")
    require(target_seen, "target deep cross-boundary history was not visited")
    require(minima["maximum"] == 218, "unexpected selected maximum")
    require(
        minima["mixed_maximum"] == Fraction(381, 2),
        "unexpected mixed maximum",
    )
    require(minima["linear"] == Fraction(676, 5), "unexpected linear minimum")
    require(minima["local"] == Fraction(691, 5), "unexpected local minimum")
    require(
        minima["weighted_excess"] == Fraction(701, 5),
        "unexpected weighted-excess minimum",
    )
    require(minima["selected_excess"] == 223, "unexpected selected excess")

    print("two-block literal oracle: PASS")
    print(f"histories={history_count}; distinct_final_cycles={len(final_cycles)}")
    print(
        f"base_splits={tuple(base_counts)}; recursive_splits={tuple(recursive_counts)}"
    )
    print(f"inserted_pair_splits={tuple(inserted_pair_counts)}")
    print(
        "rooted_recursive="
        f"upper{tuple(rooted_upper_counts)},lower{tuple(rooted_lower_counts)}"
    )
    print(f"deep_cross_boundary={deep_cross_count}")
    print(f"pool_histogram={dict(sorted(pool_histogram.items()))}")
    print(
        f"both_pools={both_pool_count}; all_original_edges_charged={all_charged_count}"
    )
    print(f"segment_floors={segment_floors}; floor_sum={floor_sum}")
    print(f"finite_bound={finite_bound}")
    print(f"minima={minima}")


if __name__ == "__main__":
    audit()
