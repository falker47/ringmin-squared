"""Independent exact oracle for bounded five-prefix split histories.

The script imports no project, production, or test helper.  Starting from the
smallest cyclic base that permits five distinct original-edge charges in one
history (a pentagon), it literally splits every current edge for exactly five
consecutive labels.  It audits linkage, the five-prefix convex identity, the
canonical one-use original-edge partition, the recursive-edge invariant
across all four boundaries, all five local floors, and the resulting finite
five-segment inequality with ``Fraction`` arithmetic.
"""

from collections import Counter
from fractions import Fraction


N = 17
ALPHA = Fraction(13, 17)
R = 13
CENTER = N + R
BETAS = (
    Fraction(12, 17),
    Fraction(11, 17),
    Fraction(10, 17),
    Fraction(9, 17),
    Fraction(8, 17),
)
CUTOFFS = (12, 11, 10, 9, 8)
WEIGHTS = (
    Fraction(5, 6),
    Fraction(2, 3),
    Fraction(1, 2),
    Fraction(1, 3),
    Fraction(1, 6),
)
BASE = (13, 17, 14, 16, 15)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def edges(cycle: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        tuple(sorted((cycle[index], cycle[(index + 1) % len(cycle)])))
        for index in range(len(cycle))
    )


def score(cycle: tuple[int, ...]) -> int:
    return sum(
        cycle[index] * cycle[(index + 1) % len(cycle)] for index in range(len(cycle))
    )


def split(
    cycle: tuple[int, ...],
    position: int,
    label: int,
) -> tuple[int, ...]:
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
    history: tuple[tuple[object, ...], ...] = (),
) -> None:
    if not condition:
        raise AssertionError(f"{message}; history={history!r}")


def audit() -> None:
    require(floor_fraction(ALPHA * N) == R, "incorrect rounded block endpoint")
    require(
        tuple(ceil_fraction(beta * N) for beta in BETAS) == CUTOFFS,
        "incorrect rounded prefix cutoffs",
    )
    require(
        0 < BETAS[4] < BETAS[3] < BETAS[2] < BETAS[1] < BETAS[0] < ALPHA < 1,
        "density order failed",
    )
    require(
        0 <= WEIGHTS[4] <= WEIGHTS[3] <= WEIGHTS[2] <= WEIGHTS[1] <= WEIGHTS[0] <= 1,
        "weight order failed",
    )
    require(2 <= R <= N - 2, "inadmissible base block")
    require(
        1 <= CUTOFFS[4] < CUTOFFS[3] < CUTOFFS[2] < CUTOFFS[1] < CUTOFFS[0] <= R - 1,
        "inadmissible finite cutoffs",
    )

    convex_coefficients = (
        1 - WEIGHTS[0],
        WEIGHTS[0] - WEIGHTS[1],
        WEIGHTS[1] - WEIGHTS[2],
        WEIGHTS[2] - WEIGHTS[3],
        WEIGHTS[3] - WEIGHTS[4],
        WEIGHTS[4],
    )
    require(
        convex_coefficients == (Fraction(1, 6),) * 6,
        "unexpected convex coefficients",
    )
    require(sum(convex_coefficients) == 1, "convex coefficients do not sum to one")

    base_edges = frozenset(edges(BASE))
    # Each original edge is destroyed by its first split and never recreated.
    # Thus five base splits in one history require at least five original
    # edges; a simple q-cycle has q edges, and this pentagon attains q = 5.
    require(
        len(BASE) == len(CUTOFFS) == 5,
        "base is not minimal for five simultaneous original-edge charges",
    )
    require(len(base_edges) == len(BASE), "base is not a loopless simple cycle")
    require(set(BASE) == set(range(R, N + 1)), "base has the wrong labels")
    base_score = score(BASE)
    pairing_floor = sum(label * (CENTER - label) for label in range(R, N + 1))
    base_slack = {edge: Fraction((sum(edge) - CENTER) ** 2, 2) for edge in base_edges}
    require(base_score == 1118, "unexpected base score")
    require(pairing_floor == 1115, "unexpected pairing floor")
    require(
        sum(base_slack.values()) == base_score - pairing_floor == 3,
        "base-slack identity failed",
    )
    require(
        Counter(base_slack.values())
        == Counter({Fraction(): 2, Fraction(1, 2): 2, Fraction(2): 1}),
        "unexpected base-slack distribution",
    )

    segment_lengths = (
        R - CUTOFFS[0],
        CUTOFFS[0] - CUTOFFS[1],
        CUTOFFS[1] - CUTOFFS[2],
        CUTOFFS[2] - CUTOFFS[3],
        CUTOFFS[3] - CUTOFFS[4],
    )
    require(segment_lengths == (1, 1, 1, 1, 1), "unexpected segment lengths")
    segment_floors = tuple(
        g_floor(weight, cutoff) for weight, cutoff in zip(WEIGHTS, CUTOFFS)
    )
    recursive_floors = tuple(
        j_floor(weight, cutoff) for weight, cutoff in zip(WEIGHTS, CUTOFFS)
    )
    require(
        segment_floors
        == (
            Fraction(750, 7),
            Fraction(194, 3),
            Fraction(100, 3),
            Fraction(63, 5),
            Fraction(58, 33),
        ),
        "unexpected base floors",
    )
    require(
        recursive_floors
        == (
            Fraction(120),
            Fraction(230, 3),
            Fraction(43),
            Fraction(19),
            Fraction(14, 3),
        ),
        "unexpected recursive floors",
    )
    require(
        all(
            recursive > base
            for recursive, base in zip(recursive_floors, segment_floors)
        ),
        "recursive floor does not dominate the base floor",
    )
    require(
        all(floor > 0 for floor in segment_floors),
        "nonpositive local floor",
    )
    floor_sum = sum(
        (length * floor for length, floor in zip(segment_lengths, segment_floors)),
        Fraction(),
    )
    lower_bound = pairing_floor + floor_sum
    require(floor_sum == Fraction(253523, 1155), "unexpected floor sum")
    require(lower_bound == Fraction(1541348, 1155), "unexpected five-segment bound")

    base_counts = [0, 0, 0, 0, 0]
    recursive_counts = [0, 0, 0, 0, 0]
    inserted_pair_counts = [0, 0, 0, 0, 0]
    inserted_pair_edges = [Counter() for _ in CUTOFFS]
    used_base_histogram: Counter[int] = Counter()
    final_cycles: set[tuple[int, ...]] = set()
    history_count = 0
    minimum_selected_excess: Fraction | None = None
    minimum_selected_count = 0
    minimum_weighted_excess: Fraction | None = None

    def walk(
        cycle: tuple[int, ...],
        depth: int,
        used_base_edges: frozenset[tuple[int, int]],
        corrections: tuple[int, ...],
        contributions: tuple[Fraction, ...],
        history: tuple[tuple[object, ...], ...],
    ) -> None:
        nonlocal history_count
        nonlocal minimum_selected_count
        nonlocal minimum_selected_excess
        nonlocal minimum_weighted_excess

        if depth == len(CUTOFFS):
            require(
                set(cycle) == set(range(CUTOFFS[-1], N + 1)),
                "final cycle has the wrong labels",
                history,
            )
            require(
                len(edges(cycle)) == len(set(edges(cycle))),
                "final cycle is not simple",
                history,
            )
            require(cycle not in final_cycles, "duplicate final cycle", history)
            final_cycles.add(cycle)

            heights: list[int] = []
            running_height = 0
            for correction in corrections:
                running_height += correction
                heights.append(running_height)

            convex_height = sum(
                coefficient * height
                for coefficient, height in zip(convex_coefficients[1:], heights)
            )
            segmented_height = sum(
                weight * correction for weight, correction in zip(WEIGHTS, corrections)
            )
            require(
                convex_height == segmented_height,
                "convex-to-segment telescoping identity failed",
                history,
            )
            require(
                max(0, *heights) >= convex_height,
                "convex height exceeds the selected-prefix maximum",
                history,
            )

            charged_edges = tuple(
                record[2] for record in history if record[4] == "base"
            )
            require(
                len(charged_edges) == len(set(charged_edges)),
                "canonical original-edge map is not injective",
                history,
            )
            require(
                frozenset(charged_edges) == used_base_edges <= base_edges,
                "charged original-edge set is inconsistent",
                history,
            )
            unused_edges = base_edges - used_base_edges
            require(
                not (used_base_edges & unused_edges)
                and used_base_edges | unused_edges == base_edges,
                "canonical charged/unused partition failed",
                history,
            )
            unused_slack = sum(
                (base_slack[edge] for edge in unused_edges),
                Fraction(),
            )
            local_sum = sum(contributions, Fraction())
            weighted_excess = base_score - pairing_floor + segmented_height
            require(
                weighted_excess == local_sum + unused_slack,
                "unique original-edge slack identity failed",
                history,
            )
            require(
                local_sum >= floor_sum,
                "local contributions miss the five segment floors",
                history,
            )

            selected_excess = Fraction(base_score - pairing_floor + max(0, *heights))
            require(
                selected_excess >= weighted_excess >= floor_sum,
                "five-segment lower bound failed",
                history,
            )
            require(
                base_score + max(0, *heights) >= lower_bound,
                "literal selected-prefix objective misses the lower bound",
                history,
            )

            if (
                minimum_selected_excess is None
                or selected_excess < minimum_selected_excess
            ):
                minimum_selected_excess = selected_excess
                minimum_selected_count = 1
            elif selected_excess == minimum_selected_excess:
                minimum_selected_count += 1
            if (
                minimum_weighted_excess is None
                or weighted_excess < minimum_weighted_excess
            ):
                minimum_weighted_excess = weighted_excess

            used_base_histogram[len(used_base_edges)] += 1
            history_count += 1
            return

        label = CUTOFFS[depth]
        weight = WEIGHTS[depth]
        inserted_labels = frozenset(CUTOFFS[:depth])
        expected_labels = set(range(label + 1, N + 1))
        require(
            set(cycle) == expected_labels,
            "current cycle has the wrong labels",
            history,
        )
        require(
            inserted_labels == frozenset(range(label + 1, R)),
            "inserted-label frontier is inconsistent",
            history,
        )

        for current_edge in edges(cycle):
            untouched_base = current_edge in base_edges
            recursive = bool(inserted_labels.intersection(current_edge))
            require(
                untouched_base != recursive,
                "current edge violates the base/recursive invariant",
                history,
            )
            if untouched_base:
                require(
                    current_edge not in used_base_edges,
                    "used original edge was recreated",
                    history,
                )

        for position, left in enumerate(cycle):
            right = cycle[(position + 1) % len(cycle)]
            current_edge = tuple(sorted((left, right)))
            correction = label * (left + right) - left * right
            next_cycle = split(cycle, position, label)
            split_kind = "base" if current_edge in base_edges else "recursive"
            next_history = history + (
                (label, position, current_edge, correction, split_kind, next_cycle),
            )
            require(
                contract(next_cycle, label) == cycle,
                "literal split does not contract to its parent",
                next_history,
            )
            require(
                score(next_cycle) == score(cycle) + correction,
                "literal score update failed",
                next_history,
            )
            child_edges = {
                tuple(sorted((left, label))),
                tuple(sorted((label, right))),
            }
            require(
                current_edge not in edges(next_cycle)
                and child_edges <= set(edges(next_cycle)),
                "literal edge replacement failed",
                next_history,
            )

            if current_edge in base_edges:
                require(
                    current_edge not in used_base_edges,
                    "original edge charged twice",
                    next_history,
                )
                next_used_base_edges = used_base_edges | {current_edge}
                contribution = base_slack[current_edge] + weight * correction
                base_counts[depth] += 1
            else:
                require(
                    bool(inserted_labels.intersection(current_edge)),
                    "recursive edge lacks a previously inserted endpoint",
                    next_history,
                )
                next_used_base_edges = used_base_edges
                contribution = weight * correction
                recursive_counts[depth] += 1
                if left < R and right < R:
                    inserted_pair_counts[depth] += 1
                    inserted_pair_edges[depth][current_edge] += 1

            require(
                contribution >= g_floor(weight, label) >= segment_floors[depth],
                "local segment floor failed",
                next_history,
            )
            if current_edge not in base_edges:
                require(
                    contribution >= j_floor(weight, label) >= segment_floors[depth],
                    "recursive-to-base floor comparison failed",
                    next_history,
                )

            walk(
                next_cycle,
                depth + 1,
                frozenset(next_used_base_edges),
                corrections + (correction,),
                contributions + (contribution,),
                next_history,
            )

    walk(BASE, 0, frozenset(), (), (), ())

    require(history_count == 15120, "unexpected history count")
    require(len(final_cycles) == 15120, "unexpected distinct final-cycle count")
    require(
        tuple(base_counts) == (5, 20, 100, 600, 4200),
        "unexpected base-split counts",
    )
    require(
        tuple(recursive_counts) == (0, 10, 110, 1080, 10920),
        "unexpected recursive-split counts",
    )
    require(
        tuple(inserted_pair_counts) == (0, 0, 10, 180, 2520),
        "unexpected inserted-pair recursive counts",
    )
    require(
        inserted_pair_edges[2] == Counter({(11, 12): 10}),
        "unexpected third-level inserted-pair distribution",
    )
    require(
        inserted_pair_edges[3] == Counter({(10, 11): 60, (10, 12): 60, (11, 12): 60}),
        "unexpected fourth-level inserted-pair distribution",
    )
    require(
        inserted_pair_edges[4]
        == Counter(
            {
                (9, 10): 420,
                (9, 11): 420,
                (9, 12): 420,
                (10, 11): 420,
                (10, 12): 420,
                (11, 12): 420,
            }
        ),
        "unexpected fifth-level inserted-pair distribution",
    )
    require(
        used_base_histogram == Counter({1: 600, 2: 4800, 3: 7200, 4: 2400, 5: 120}),
        "unexpected used-base-edge histogram",
    )
    require(minimum_selected_excess == 378, "unexpected selected-excess minimum")
    require(minimum_selected_count == 4, "unexpected selected-minimum multiplicity")
    require(
        minimum_weighted_excess == Fraction(1445, 6),
        "unexpected weighted-excess minimum",
    )

    print("five-prefix literal oracle: PASS")
    print(f"histories={history_count}; distinct_final_cycles={len(final_cycles)}")
    print(
        f"base_splits={tuple(base_counts)}; recursive_splits={tuple(recursive_counts)}"
    )
    print(f"inserted_pair_splits={tuple(inserted_pair_counts)}")
    print(f"used_base_histogram={dict(sorted(used_base_histogram.items()))}")
    print(f"segment_floors={segment_floors}; floor_sum={floor_sum}")
    print(f"five_segment_lower_bound={lower_bound}")
    print(
        "minimum_selected_excess="
        f"{minimum_selected_excess}; multiplicity={minimum_selected_count}"
    )
    print(f"minimum_weighted_excess={minimum_weighted_excess}")


if __name__ == "__main__":
    audit()
