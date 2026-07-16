"""Independent exact oracle for bounded four-prefix split histories.

The script imports no project, production, or test helper.  It literally
splits every current cyclic edge for four consecutive labels and audits the
four-prefix convex identity, the original-edge slack partition, the recursive
edge invariant, and all local lower floors with ``Fraction`` arithmetic.
"""

from collections import Counter
from fractions import Fraction


N = 14
ALPHA = Fraction(11, 14)
R = 11
CENTER = N + R
BETAS = (Fraction(5, 7), Fraction(9, 14), Fraction(4, 7), Fraction(1, 2))
CUTOFFS = (10, 9, 8, 7)
WEIGHTS = (Fraction(4, 5), Fraction(3, 5), Fraction(2, 5), Fraction(1, 5))
BASE = (11, 14, 12, 13)


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
        0 < BETAS[3] < BETAS[2] < BETAS[1] < BETAS[0] < ALPHA < 1,
        "density order failed",
    )
    require(
        0 <= WEIGHTS[3] <= WEIGHTS[2] <= WEIGHTS[1] <= WEIGHTS[0] <= 1,
        "weight order failed",
    )

    convex_coefficients = (
        1 - WEIGHTS[0],
        WEIGHTS[0] - WEIGHTS[1],
        WEIGHTS[1] - WEIGHTS[2],
        WEIGHTS[2] - WEIGHTS[3],
        WEIGHTS[3],
    )
    require(
        convex_coefficients == (Fraction(1, 5),) * 5,
        "unexpected convex coefficients",
    )
    require(sum(convex_coefficients) == 1, "convex coefficients do not sum to one")

    base_edges = frozenset(edges(BASE))
    require(len(base_edges) == len(BASE), "base is not a loopless simple cycle")
    base_score = score(BASE)
    pairing_floor = sum(label * (CENTER - label) for label in range(R, N + 1))
    base_slack = {edge: Fraction((sum(edge) - CENTER) ** 2, 2) for edge in base_edges}
    require(base_score == 621, "unexpected base score")
    require(pairing_floor == 620, "unexpected pairing floor")
    require(
        sum(base_slack.values()) == base_score - pairing_floor == 1,
        "base-slack identity failed",
    )

    segment_floors = tuple(
        g_floor(weight, cutoff) for weight, cutoff in zip(WEIGHTS, CUTOFFS)
    )
    recursive_floors = tuple(
        j_floor(weight, cutoff) for weight, cutoff in zip(WEIGHTS, CUTOFFS)
    )
    require(
        segment_floors
        == (
            Fraction(215, 3),
            Fraction(381, 10),
            Fraction(619, 40),
            Fraction(277, 90),
        ),
        "unexpected base floors",
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
            for recursive, base in zip(recursive_floors, segment_floors)
        ),
        "recursive floor does not dominate the base floor",
    )
    floor_sum = sum(segment_floors, Fraction())
    lower_bound = pairing_floor + floor_sum
    require(floor_sum == Fraction(9239, 72), "unexpected floor sum")
    require(lower_bound == Fraction(53879, 72), "unexpected four-segment bound")

    base_counts = [0, 0, 0, 0]
    recursive_counts = [0, 0, 0, 0]
    inserted_pair_counts = [0, 0, 0, 0]
    fourth_inserted_pairs: Counter[tuple[int, int]] = Counter()
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

            unused_slack = sum(
                (
                    slack
                    for edge, slack in base_slack.items()
                    if edge not in used_base_edges
                ),
                Fraction(),
            )
            local_sum = sum(contributions, Fraction())
            weighted_excess = base_score - pairing_floor + segmented_height
            require(
                weighted_excess == local_sum + unused_slack,
                "unique original-edge slack partition failed",
                history,
            )
            require(
                local_sum >= floor_sum,
                "local contributions miss the four segment floors",
                history,
            )

            selected_excess = Fraction(base_score - pairing_floor + max(0, *heights))
            require(
                selected_excess >= weighted_excess >= floor_sum,
                "four-segment lower bound failed",
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
            set(cycle) == expected_labels, "current cycle has the wrong labels", history
        )

        for current_edge in edges(cycle):
            untouched_base = current_edge in base_edges
            recursive = bool(inserted_labels.intersection(current_edge))
            require(
                untouched_base != recursive,
                "current edge violates the base/recursive dichotomy",
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
            next_history = history + (
                (label, position, current_edge, correction, next_cycle),
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
                recursive_lower = (CENTER - 1) * label - N * (R - 1)
                require(
                    correction >= recursive_lower,
                    "recursive correction floor failed",
                    next_history,
                )
                next_used_base_edges = used_base_edges
                contribution = weight * correction
                recursive_counts[depth] += 1
                if left < R and right < R:
                    inserted_pair_counts[depth] += 1
                    if depth == 3:
                        fourth_inserted_pairs[current_edge] += 1

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

    require(history_count == 840, "unexpected history count")
    require(len(final_cycles) == 840, "unexpected distinct final-cycle count")
    require(tuple(base_counts) == (4, 12, 48, 240), "unexpected base-split counts")
    require(
        tuple(recursive_counts) == (0, 8, 72, 600),
        "unexpected recursive-split counts",
    )
    require(
        tuple(inserted_pair_counts) == (0, 0, 8, 120),
        "unexpected inserted-pair recursive counts",
    )
    require(
        fourth_inserted_pairs == Counter({(8, 9): 40, (8, 10): 40, (9, 10): 40}),
        "unexpected fourth-level inserted-pair distribution",
    )
    require(
        used_base_histogram == Counter({1: 96, 2: 432, 3: 288, 4: 24}),
        "unexpected used-base-edge histogram",
    )
    require(minimum_selected_excess == 227, "unexpected selected-excess minimum")
    require(minimum_selected_count == 2, "unexpected selected-minimum multiplicity")
    require(
        minimum_weighted_excess == Fraction(696, 5),
        "unexpected weighted-excess minimum",
    )

    print("four-prefix literal oracle: PASS")
    print(f"histories={history_count}; distinct_final_cycles={len(final_cycles)}")
    print(
        f"base_splits={tuple(base_counts)}; recursive_splits={tuple(recursive_counts)}"
    )
    print(f"inserted_pair_splits={tuple(inserted_pair_counts)}")
    print(f"used_base_histogram={dict(sorted(used_base_histogram.items()))}")
    print(f"segment_floors={segment_floors}; floor_sum={floor_sum}")
    print(f"four_segment_lower_bound={lower_bound}")
    print(
        "minimum_selected_excess="
        f"{minimum_selected_excess}; multiplicity={minimum_selected_count}"
    )
    print(f"minimum_weighted_excess={minimum_weighted_excess}")


if __name__ == "__main__":
    audit()
