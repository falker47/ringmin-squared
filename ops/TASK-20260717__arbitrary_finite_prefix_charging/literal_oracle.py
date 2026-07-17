"""Bounded exact oracle for the first case beyond the old five-prefix proof.

The script is dossier-local and imports no project, production, or test helper.
It exhausts every six-split history of one six-edge base and checks the
six-prefix convex identity, canonical one-use original-edge partition,
boundary-independent recursive invariant, local floors, and finite bound.
This finite computation corroborates but does not prove the arbitrary
finite-prefix theorem.
"""

from collections import Counter
from fractions import Fraction


N = 20
R = 15
CENTER = N + R
ALPHA = Fraction(3, 4)
CUTOFFS = (14, 13, 12, 11, 10, 9)
BETAS = tuple(Fraction(cutoff, N) for cutoff in CUTOFFS)
WEIGHTS = tuple(Fraction(numerator, 7) for numerator in range(6, 0, -1))
BASE = (15, 20, 16, 19, 17, 18)


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
    condition: bool, message: str, path: tuple[tuple[int, int], ...] = ()
) -> None:
    if not condition:
        raise AssertionError(f"{message}; path={path!r}")


def audit() -> None:
    require(floor_fraction(ALPHA * N) == R, "incorrect rounded block endpoint")
    require(
        tuple(ceil_fraction(beta * N) for beta in BETAS) == CUTOFFS,
        "incorrect rounded cutoffs",
    )
    require(
        0
        < BETAS[-1]
        < BETAS[-2]
        < BETAS[-3]
        < BETAS[-4]
        < BETAS[-5]
        < BETAS[-6]
        < ALPHA
        < 1,
        "density order failed",
    )
    require(
        0
        <= WEIGHTS[-1]
        <= WEIGHTS[-2]
        <= WEIGHTS[-3]
        <= WEIGHTS[-4]
        <= WEIGHTS[-5]
        <= WEIGHTS[-6]
        <= 1,
        "weight order failed",
    )
    require(2 <= R <= N - 2, "inadmissible base block")
    require(
        1
        <= CUTOFFS[-1]
        < CUTOFFS[-2]
        < CUTOFFS[-3]
        < CUTOFFS[-4]
        < CUTOFFS[-5]
        < CUTOFFS[-6]
        <= R - 1,
        "inadmissible finite cutoffs",
    )

    convex_coefficients = (
        (1 - WEIGHTS[0],)
        + tuple(
            WEIGHTS[index] - WEIGHTS[index + 1] for index in range(len(WEIGHTS) - 1)
        )
        + (WEIGHTS[-1],)
    )
    require(
        convex_coefficients == (Fraction(1, 7),) * 7,
        "unexpected convex coefficients",
    )
    require(sum(convex_coefficients) == 1, "convex coefficients do not sum to one")

    base_edges = frozenset(edges(BASE))
    require(
        len(BASE) == len(CUTOFFS) == 6,
        "base is not minimal for six simultaneous original-edge charges",
    )
    require(len(base_edges) == len(BASE), "base is not a loopless simple cycle")
    require(set(BASE) == set(range(R, N + 1)), "base has the wrong labels")
    base_score = score(BASE)
    pairing_floor = sum(label * (CENTER - label) for label in range(R, N + 1))
    base_slack = {edge: Fraction((sum(edge) - CENTER) ** 2, 2) for edge in base_edges}
    require(base_score == 1823, "unexpected base score")
    require(pairing_floor == 1820, "unexpected pairing floor")
    require(
        sum(base_slack.values()) == base_score - pairing_floor == 3,
        "base-slack identity failed",
    )
    require(
        Counter(base_slack.values())
        == Counter({Fraction(): 3, Fraction(1, 2): 2, Fraction(2): 1}),
        "unexpected base-slack distribution",
    )

    segment_lengths = (R - CUTOFFS[0],) + tuple(
        CUTOFFS[index - 1] - CUTOFFS[index] for index in range(1, len(CUTOFFS))
    )
    require(segment_lengths == (1,) * 6, "unexpected segment lengths")
    segment_floors = tuple(
        g_floor(weight, cutoff) for weight, cutoff in zip(WEIGHTS, CUTOFFS)
    )
    recursive_floors = tuple(
        j_floor(weight, cutoff) for weight, cutoff in zip(WEIGHTS, CUTOFFS)
    )
    require(
        segment_floors
        == (
            Fraction(1197, 8),
            Fraction(1375, 14),
            Fraction(2033, 35),
            Fraction(4437, 154),
            Fraction(275, 28),
            Fraction(83, 182),
        ),
        "unexpected segment floors",
    )
    require(
        recursive_floors
        == (
            Fraction(168),
            Fraction(810, 7),
            Fraction(512, 7),
            Fraction(282, 7),
            Fraction(120, 7),
            Fraction(26, 7),
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
    require(all(floor > 0 for floor in segment_floors), "nonpositive local floor")
    floor_sum = sum(segment_floors, Fraction())
    lower_bound = pairing_floor + floor_sum
    require(floor_sum == Fraction(1973481, 5720), "unexpected floor sum")
    require(lower_bound == Fraction(12383881, 5720), "unexpected finite bound")

    base_counts = [0] * 6
    recursive_counts = [0] * 6
    inserted_pair_counts = [0] * 6
    used_base_histogram: Counter[int] = Counter()
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
        path: tuple[tuple[int, int], ...],
    ) -> None:
        nonlocal history_count
        nonlocal minimum_selected_count
        nonlocal minimum_selected_excess
        nonlocal minimum_weighted_excess

        if depth == len(CUTOFFS):
            require(
                set(cycle) == set(range(CUTOFFS[-1], N + 1)),
                "final cycle has the wrong labels",
                path,
            )
            recovered = cycle
            for label in reversed(CUTOFFS):
                recovered = contract(recovered, label)
            require(recovered == BASE, "reverse contraction did not recover base", path)

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
                "convex-to-segment telescope failed",
                path,
            )
            require(
                max(0, *heights) >= convex_height,
                "convex height exceeds selected maximum",
                path,
            )

            unused_edges = base_edges - used_base_edges
            require(
                not (used_base_edges & unused_edges)
                and used_base_edges | unused_edges == base_edges,
                "canonical charged/unused partition failed",
                path,
            )
            unused_slack = sum(
                (base_slack[edge] for edge in unused_edges),
                Fraction(),
            )
            local_sum = sum(contributions, Fraction())
            weighted_excess = base_score - pairing_floor + segmented_height
            require(
                weighted_excess == local_sum + unused_slack,
                "one-use slack identity failed",
                path,
            )
            require(local_sum >= floor_sum, "local floors miss finite sum", path)

            selected_excess = Fraction(base_score - pairing_floor + max(0, *heights))
            require(
                selected_excess >= weighted_excess >= floor_sum,
                "six-segment lower bound failed",
                path,
            )
            require(
                base_score + max(0, *heights) >= lower_bound,
                "selected objective misses finite bound",
                path,
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
        require(
            set(cycle) == set(range(label + 1, N + 1)),
            "current cycle has the wrong labels",
            path,
        )
        require(
            inserted_labels == frozenset(range(label + 1, R)),
            "inserted-label frontier is inconsistent",
            path,
        )

        for current_edge in edges(cycle):
            untouched_base = current_edge in base_edges
            recursive = bool(inserted_labels.intersection(current_edge))
            require(
                untouched_base != recursive,
                "base/recursive invariant failed",
                path,
            )

        for position, left in enumerate(cycle):
            right = cycle[(position + 1) % len(cycle)]
            current_edge = tuple(sorted((left, right)))
            correction = label * (left + right) - left * right
            next_cycle = split(cycle, position, label)
            next_path = path + (current_edge,)
            require(
                contract(next_cycle, label) == cycle,
                "literal split does not contract to parent",
                next_path,
            )
            require(
                score(next_cycle) == score(cycle) + correction,
                "literal score update failed",
                next_path,
            )

            if current_edge in base_edges:
                require(
                    current_edge not in used_base_edges,
                    "original edge charged twice",
                    next_path,
                )
                next_used_base_edges = used_base_edges | {current_edge}
                contribution = base_slack[current_edge] + weight * correction
                base_counts[depth] += 1
            else:
                require(
                    bool(inserted_labels.intersection(current_edge)),
                    "recursive edge lacks an inserted endpoint",
                    next_path,
                )
                next_used_base_edges = used_base_edges
                contribution = weight * correction
                recursive_counts[depth] += 1
                if left < R and right < R:
                    inserted_pair_counts[depth] += 1

            require(
                contribution >= g_floor(weight, label) >= segment_floors[depth],
                "local segment floor failed",
                next_path,
            )
            if current_edge not in base_edges:
                require(
                    contribution >= j_floor(weight, label) >= segment_floors[depth],
                    "recursive floor comparison failed",
                    next_path,
                )

            walk(
                next_cycle,
                depth + 1,
                frozenset(next_used_base_edges),
                corrections + (correction,),
                contributions + (contribution,),
                next_path,
            )

    walk(BASE, 0, frozenset(), (), (), ())

    require(history_count == 332640, "unexpected history count")
    require(
        tuple(base_counts) == (6, 30, 180, 1260, 10080, 90720),
        "unexpected base-split counts",
    )
    require(
        tuple(recursive_counts) == (0, 12, 156, 1764, 20160, 241920),
        "unexpected recursive-split counts",
    )
    require(
        tuple(inserted_pair_counts) == (0, 0, 12, 252, 4032, 60480),
        "unexpected inserted-pair counts",
    )
    require(
        used_base_histogram
        == Counter({1: 4320, 2: 54000, 3: 144000, 4: 108000, 5: 21600, 6: 720}),
        "unexpected used-base-edge histogram",
    )
    require(minimum_selected_excess == 586, "unexpected selected minimum")
    require(minimum_selected_count == 12, "unexpected selected multiplicity")
    require(
        minimum_weighted_excess == Fraction(2668, 7),
        "unexpected weighted minimum",
    )

    print("six-prefix literal oracle: PASS")
    print(f"histories={history_count}")
    print(
        f"base_splits={tuple(base_counts)}; recursive_splits={tuple(recursive_counts)}"
    )
    print(f"inserted_pair_splits={tuple(inserted_pair_counts)}")
    print(f"used_base_histogram={dict(sorted(used_base_histogram.items()))}")
    print(f"segment_floors={segment_floors}; floor_sum={floor_sum}")
    print(f"six_segment_lower_bound={lower_bound}")
    print(
        "minimum_selected_excess="
        f"{minimum_selected_excess}; multiplicity={minimum_selected_count}"
    )
    print(f"minimum_weighted_excess={minimum_weighted_excess}")


if __name__ == "__main__":
    audit()
