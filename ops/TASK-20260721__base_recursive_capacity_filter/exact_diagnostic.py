"""Independent exact diagnostic for the base/recursive capacity filter.

The script imports no project, production, or test helper.  It exhausts all
selected-prefix histories in four small triangle-base rows, checks the
original-edge capacity and the filtered finite inequality history by history,
and audits the normalized piecewise objective on an exact rational grid.  The
bounded checks corroborate, but do not replace, the all-history and
compact-domain proofs.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import factorial, prod


@dataclass(frozen=True)
class Case:
    name: str
    n: int
    r: int
    s: int
    weight: Fraction
    expected_histories: int
    expected_used_base_histogram: tuple[tuple[int, int], ...]
    expected_pairing_floor: int
    expected_g: Fraction
    expected_delta: Fraction
    expected_bound: Fraction
    expected_minimum_objective: int
    expected_minimum_multiplicity: int


CASES = (
    Case(
        name="capacity_saturated_control",
        n=7,
        r=5,
        s=2,
        weight=Fraction(1, 2),
        expected_histories=60,
        expected_used_base_histogram=((1, 18), (2, 36), (3, 6)),
        expected_pairing_floor=106,
        expected_g=Fraction(-26, 3),
        expected_delta=Fraction(17, 3),
        expected_bound=Fraction(80),
        expected_minimum_objective=118,
        expected_minimum_multiplicity=4,
    ),
    Case(
        name="first_capacity_active_row",
        n=7,
        r=5,
        s=1,
        weight=Fraction(1, 2),
        expected_histories=360,
        expected_used_base_histogram=((1, 72), (2, 216), (3, 72)),
        expected_pairing_floor=106,
        expected_g=Fraction(-97, 6),
        expected_delta=Fraction(23, 3),
        expected_bound=Fraction(49),
        expected_minimum_objective=118,
        expected_minimum_multiplicity=24,
    ),
    Case(
        name="first_positive_floor_active_row",
        n=12,
        r=10,
        s=6,
        weight=Fraction(1, 2),
        expected_histories=360,
        expected_used_base_histogram=((1, 72), (2, 216), (3, 72)),
        expected_pairing_floor=361,
        expected_g=Fraction(4, 3),
        expected_delta=Fraction(23, 3),
        expected_bound=Fraction(374),
        expected_minimum_objective=542,
        expected_minimum_multiplicity=1,
    ),
    Case(
        name="two_forced_recursive_splits",
        n=14,
        r=12,
        s=7,
        weight=Fraction(1, 2),
        expected_histories=2_520,
        expected_used_base_histogram=((1, 360), (2, 1_440), (3, 720)),
        expected_pairing_floor=505,
        expected_g=Fraction(1, 2),
        expected_delta=Fraction(10),
        expected_bound=Fraction(1_055, 2),
        expected_minimum_objective=843,
        expected_minimum_multiplicity=1,
    ),
)


def edges(cycle: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Return the oriented edge occurrences of one cyclic tuple."""

    return tuple(
        (cycle[index], cycle[(index + 1) % len(cycle)]) for index in range(len(cycle))
    )


def edge_key(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left < right else (right, left)


def score(cycle: tuple[int, ...]) -> int:
    return sum(left * right for left, right in edges(cycle))


def split(cycle: tuple[int, ...], position: int, label: int) -> tuple[int, ...]:
    return cycle[: position + 1] + (label,) + cycle[position + 1 :]


def contract(cycle: tuple[int, ...], label: int) -> tuple[int, ...]:
    return tuple(entry for entry in cycle if entry != label)


def canonical_cycle(cycle: tuple[int, ...]) -> tuple[int, ...]:
    """Canonicalize an undirected cycle under rotations and reversal."""

    candidates = []
    for oriented in (cycle, tuple(reversed(cycle))):
        candidates.extend(
            oriented[index:] + oriented[:index] for index in range(len(cycle))
        )
    return min(candidates)


def g_floor(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    center = n + r
    return (
        weight
        * (4 * center * label - center * center - 2 * weight * label * label)
        / (2 * (2 - weight))
    )


def j_floor(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    return weight * ((n + r - 1) * label - n * (r - 1))


def audit_literal_case(case: Case) -> tuple[int, Counter[int], Fraction]:
    """Exhaust and audit every selected-prefix history for one case."""

    n, r, s, weight = case.n, case.r, case.s, case.weight
    q = n - r + 1
    k = r - s
    forced_recursive = max(0, k - q)
    labels = tuple(range(r - 1, s - 1, -1))

    assert q == 3
    assert 2 <= r <= n - 2
    assert 1 <= s <= r - 1
    assert len(labels) == k
    assert 0 <= weight <= 1

    # There is one undirected triangle.  This tuple fixes one representative.
    base = (r, n, r + 1)
    assert set(base) == set(range(r, n + 1))
    base_edges = frozenset(edge_key(*edge) for edge in edges(base))
    assert len(base_edges) == q

    center = n + r
    pairing_floor = sum(label * (center - label) for label in range(r, n + 1))
    base_score = score(base)
    base_slack = {edge: Fraction((sum(edge) - center) ** 2, 2) for edge in base_edges}
    assert sum(base_slack.values(), Fraction()) == base_score - pairing_floor

    base_floor = g_floor(n, r, weight, s)
    recursive_floor = j_floor(n, r, weight, s)
    delta = recursive_floor - base_floor
    unfiltered_bound = pairing_floor + k * base_floor
    filtered_bound = unfiltered_bound + forced_recursive * delta

    assert pairing_floor == case.expected_pairing_floor
    assert base_floor == case.expected_g
    assert delta == case.expected_delta > 0
    assert filtered_bound == case.expected_bound
    if forced_recursive:
        assert filtered_bound > unfiltered_bound
    else:
        assert filtered_bound == unfiltered_bound

    history_count = 0
    used_base_histogram: Counter[int] = Counter()
    final_cycles: set[tuple[int, ...]] = set()
    minimum_objective: int | None = None
    minimum_multiplicity = 0
    minimum_margin: Fraction | None = None

    def walk(
        cycle: tuple[int, ...],
        depth: int,
        used_base_edges: frozenset[tuple[int, int]],
        corrections: tuple[int, ...],
        contributions: tuple[Fraction, ...],
        path: tuple[tuple[int, int], ...],
    ) -> None:
        nonlocal history_count
        nonlocal minimum_margin
        nonlocal minimum_multiplicity
        nonlocal minimum_objective

        if depth == k:
            assert set(cycle) == set(range(s, n + 1)), path
            recovered = cycle
            for label in range(s, r):
                recovered = contract(recovered, label)
            assert recovered == base, path

            heights: list[int] = []
            running_height = 0
            for correction in corrections:
                running_height += correction
                heights.append(running_height)
            final_height = running_height
            selected_objective = base_score + max(0, *heights)
            weighted_objective = Fraction(base_score) + weight * final_height
            assert selected_objective >= weighted_objective, path

            unused_base_edges = base_edges - used_base_edges
            unused_slack = sum(
                (base_slack[edge] for edge in unused_base_edges), Fraction()
            )
            weighted_excess = weighted_objective - pairing_floor
            assert weighted_excess == sum(contributions, Fraction()) + unused_slack

            base_count = len(used_base_edges)
            recursive_count = k - base_count
            assert base_count <= q, path
            assert recursive_count >= forced_recursive, path
            assert weighted_excess >= (k * base_floor + recursive_count * delta), path
            assert weighted_excess >= k * base_floor + forced_recursive * delta, path
            assert selected_objective >= filtered_bound, path

            margin = Fraction(selected_objective) - filtered_bound
            if minimum_margin is None or margin < minimum_margin:
                minimum_margin = margin
            if minimum_objective is None or selected_objective < minimum_objective:
                minimum_objective = selected_objective
                minimum_multiplicity = 1
            elif selected_objective == minimum_objective:
                minimum_multiplicity += 1

            used_base_histogram[base_count] += 1
            final_key = canonical_cycle(cycle)
            assert final_key not in final_cycles, path
            final_cycles.add(final_key)
            history_count += 1
            return

        label = labels[depth]
        inserted_labels = frozenset(labels[:depth])
        assert set(cycle) == set(range(label + 1, n + 1)), path
        assert inserted_labels == frozenset(range(label + 1, r)), path

        for left, right in edges(cycle):
            current_edge = edge_key(left, right)
            untouched_base = current_edge in base_edges
            recursive = bool(inserted_labels.intersection(current_edge))
            assert untouched_base != recursive, path

        for position, (left, right) in enumerate(edges(cycle)):
            current_edge = edge_key(left, right)
            correction = label * (left + right) - left * right
            next_cycle = split(cycle, position, label)
            next_path = path + (current_edge,)
            assert contract(next_cycle, label) == cycle, next_path
            assert score(next_cycle) == score(cycle) + correction, next_path

            if current_edge in base_edges:
                assert current_edge not in used_base_edges, next_path
                next_used = used_base_edges | {current_edge}
                contribution = base_slack[current_edge] + weight * correction
                assert contribution >= g_floor(n, r, weight, label)
                assert g_floor(n, r, weight, label) >= base_floor
            else:
                assert inserted_labels.intersection(current_edge), next_path
                next_used = used_base_edges
                contribution = weight * correction
                assert contribution >= j_floor(n, r, weight, label)
                assert j_floor(n, r, weight, label) >= recursive_floor
                assert contribution >= base_floor + delta

            walk(
                next_cycle,
                depth + 1,
                frozenset(next_used),
                corrections + (correction,),
                contributions + (contribution,),
                next_path,
            )

    walk(base, 0, frozenset(), (), (), ())

    expected_histories = prod(q + depth for depth in range(k))
    expected_final_cycles = factorial(q + k - 1) // 2
    assert expected_histories == expected_final_cycles
    assert history_count == len(final_cycles) == expected_histories
    assert history_count == case.expected_histories
    assert used_base_histogram == Counter(dict(case.expected_used_base_histogram))
    assert used_base_histogram[q] > 0  # The capacity lower bound is sharp.
    assert minimum_objective == case.expected_minimum_objective
    assert minimum_multiplicity == case.expected_minimum_multiplicity
    assert minimum_margin is not None and minimum_margin >= 0

    return history_count, used_base_histogram, minimum_margin


def pairing_coefficient(alpha: Fraction) -> Fraction:
    return (1 - alpha) * (alpha * alpha + 4 * alpha + 1) / 6


def g_coefficient(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    return (
        weight
        * (
            4 * (1 + alpha) * beta
            - (1 + alpha) * (1 + alpha)
            - 2 * weight * beta * beta
        )
        / (2 * (2 - weight))
    )


def j_coefficient(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    return weight * ((1 + alpha) * beta - alpha)


def delta_coefficient(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    return j_coefficient(alpha, beta, weight) - g_coefficient(alpha, beta, weight)


def filtered_coefficient(alpha: Fraction, beta: Fraction, weight: Fraction) -> Fraction:
    g_value = g_coefficient(alpha, beta, weight)
    capacity = max(Fraction(), 2 * alpha - beta - 1)
    return (
        pairing_coefficient(alpha)
        + (alpha - beta) * g_value
        + capacity * (j_coefficient(alpha, beta, weight) - g_value)
    )


@dataclass(frozen=True)
class Qsqrt3:
    """An exact element ``rational + radical * sqrt(3)``."""

    rational: Fraction = Fraction()
    radical: Fraction = Fraction()

    def __post_init__(self) -> None:
        object.__setattr__(self, "rational", Fraction(self.rational))
        object.__setattr__(self, "radical", Fraction(self.radical))

    @staticmethod
    def coerce(value: int | Fraction | Qsqrt3) -> Qsqrt3:
        if isinstance(value, Qsqrt3):
            return value
        return Qsqrt3(Fraction(value))

    def __add__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        other = self.coerce(other)
        return Qsqrt3(self.rational + other.rational, self.radical + other.radical)

    __radd__ = __add__

    def __neg__(self) -> Qsqrt3:
        return Qsqrt3(-self.rational, -self.radical)

    def __sub__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        return self.coerce(other) - self

    def __mul__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        other = self.coerce(other)
        return Qsqrt3(
            self.rational * other.rational + 3 * self.radical * other.radical,
            self.rational * other.radical + self.radical * other.rational,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        other = self.coerce(other)
        norm = other.rational * other.rational - 3 * other.radical * other.radical
        assert norm != 0
        return self * Qsqrt3(other.rational / norm, -other.radical / norm)

    def __rtruediv__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        return self.coerce(other) / self


def sign_qsqrt3(value: Qsqrt3) -> int:
    """Return the exact sign using rational signs and one integer square."""

    rational = value.rational
    radical = value.radical
    if radical == 0:
        return (rational > 0) - (rational < 0)
    if rational == 0:
        return (radical > 0) - (radical < 0)
    if rational > 0 and radical > 0:
        return 1
    if rational < 0 and radical < 0:
        return -1
    rational_square = rational * rational
    radical_square = 3 * radical * radical
    if rational_square == radical_square:
        return 0
    if rational > 0:
        return 1 if rational_square > radical_square else -1
    return 1 if radical_square > rational_square else -1


def audit_normalized_objective() -> tuple[int, Fraction, Fraction]:
    """Audit identities, branches, optimizer data, and an exact grid."""

    grid_denominator = 24
    active_maximum = Fraction(13, 48)
    expected_grid_maximum = Fraction(3_941_543, 14_266_368)
    expected_grid_argmax = (
        Fraction(5, 12),
        Fraction(3, 8),
        Fraction(5, 24),
    )

    grid_count = 0
    strict_active_count = 0
    collision_count = 0
    strict_inactive_count = 0
    active_equalities: list[tuple[Fraction, Fraction, Fraction]] = []
    grid_maximum: Fraction | None = None
    grid_argmax: list[tuple[Fraction, Fraction, Fraction]] = []

    c_one = Qsqrt3(Fraction(4, 27), Fraction(2, 27))
    for alpha_numerator in range(grid_denominator + 1):
        alpha = Fraction(alpha_numerator, grid_denominator)
        for beta_numerator in range(alpha_numerator + 1):
            beta = Fraction(beta_numerator, grid_denominator)
            for weight_numerator in range(grid_denominator + 1):
                weight = Fraction(weight_numerator, grid_denominator)
                grid_count += 1

                g_value = g_coefficient(alpha, beta, weight)
                j_value = j_coefficient(alpha, beta, weight)
                delta = delta_coefficient(alpha, beta, weight)
                delta_closed = (
                    weight
                    * (
                        (1 - alpha) * (1 - alpha)
                        + 2 * weight * (alpha - beta) * (1 - beta)
                    )
                    / (2 * (2 - weight))
                )
                assert delta == j_value - g_value == delta_closed >= 0

                capacity_coordinate = 2 * alpha - beta - 1
                value = filtered_coefficient(alpha, beta, weight)
                inactive_value = pairing_coefficient(alpha) + (alpha - beta) * g_value
                active_value = (
                    pairing_coefficient(alpha)
                    + (1 - alpha) * g_value
                    + capacity_coordinate * j_value
                )

                if capacity_coordinate > 0:
                    strict_active_count += 1
                    assert value == active_value
                elif capacity_coordinate < 0:
                    strict_inactive_count += 1
                    assert value == inactive_value
                else:
                    collision_count += 1
                    assert value == inactive_value == active_value

                if capacity_coordinate >= 0:
                    assert value <= active_maximum
                    if value == active_maximum:
                        active_equalities.append((alpha, beta, weight))
                if capacity_coordinate <= 0:
                    assert sign_qsqrt3(c_one - value) > 0

                point = (alpha, beta, weight)
                if grid_maximum is None or value > grid_maximum:
                    grid_maximum = value
                    grid_argmax = [point]
                elif value == grid_maximum:
                    grid_argmax.append(point)

    assert grid_count == 8_125
    assert (strict_active_count, collision_count, strict_inactive_count) == (
        3_900,
        325,
        3_900,
    )
    assert active_equalities == [(Fraction(1, 2), Fraction(), Fraction())]
    assert grid_maximum == expected_grid_maximum
    assert grid_argmax == [expected_grid_argmax]

    # Exact inactive optimizer and coefficient in Q(sqrt(3)).
    sqrt3 = Qsqrt3(Fraction(), Fraction(1))
    alpha_star = 1 - sqrt3 / 3
    beta_star = Fraction(5, 6) - sqrt3 / 4
    weight_star = (88 - 32 * sqrt3) / 73
    assert sign_qsqrt3(alpha_star) > 0
    assert sign_qsqrt3(1 - alpha_star) > 0
    assert sign_qsqrt3(beta_star) > 0
    assert sign_qsqrt3(alpha_star - beta_star) > 0
    assert sign_qsqrt3(weight_star) > 0
    assert sign_qsqrt3(1 - weight_star) > 0
    assert sign_qsqrt3(2 * alpha_star - beta_star - 1) < 0
    assert 3 * alpha_star * alpha_star - 6 * alpha_star + 2 == Qsqrt3()
    assert beta_star == (9 * alpha_star + 1) / 12
    assert weight_star == 8 * (3 * alpha_star - 1) / (9 * alpha_star + 1)

    g_star = (
        weight_star
        * (
            4 * (1 + alpha_star) * beta_star
            - (1 + alpha_star) * (1 + alpha_star)
            - 2 * weight_star * beta_star * beta_star
        )
        / (2 * (2 - weight_star))
    )
    optimizer_value = (1 - alpha_star) * (
        alpha_star * alpha_star + 4 * alpha_star + 1
    ) / 6 + (alpha_star - beta_star) * g_star
    assert optimizer_value == c_one

    # The active compact maximum is strictly below the inactive maximum:
    # C_1 - 13/48 = (32 sqrt(3) - 53)/432, and 3*32^2-53^2=263.
    assert c_one - active_maximum == Qsqrt3(Fraction(-53, 432), Fraction(2, 27))
    assert 3 * 32**2 - 53**2 == 263 > 0
    assert sign_qsqrt3(c_one - active_maximum) > 0

    # Termwise subtraction ties C_AF-C_1 to the numerator
    # 1790 + 36 sqrt(2) - 1058 sqrt(3) over 14283.  The exact rational
    # enclosures 7/5 < sqrt(2) and sqrt(3) < 26/15 leave margin 98/15.
    assert Fraction(434, 1_587) - Fraction(4, 27) == Fraction(1_790, 14_283)
    assert Fraction(4, 1_587) == Fraction(36, 14_283)
    assert -Fraction(2, 27) == -Fraction(1_058, 14_283)
    assert 7**2 < 2 * 5**2
    assert 3 * 15**2 < 26**2
    mixed_radical_lower_margin = (
        Fraction(1_790) + 36 * Fraction(7, 5) - 1_058 * Fraction(26, 15)
    )
    assert mixed_radical_lower_margin == Fraction(98, 15) > 0

    return grid_count, active_maximum, expected_grid_maximum


def audit() -> None:
    if not __debug__:
        raise RuntimeError("exact diagnostic requires assertions; do not use python -O")

    literal_histories = 0
    print("base/recursive capacity selected-prefix histories")
    for case in CASES:
        histories, histogram, minimum_margin = audit_literal_case(case)
        literal_histories += histories
        print(
            f"{case.name}: histories={histories}; "
            f"used_base={dict(sorted(histogram.items()))}; "
            f"minimum_margin={minimum_margin}"
        )

    grid_count, active_maximum, grid_maximum = audit_normalized_objective()
    print(f"selected_prefix_histories_total={literal_histories}")
    print(
        f"normalized_grid: denominator=24; points={grid_count}; "
        f"active_maximum={active_maximum}; grid_maximum={grid_maximum}"
    )
    print("exact comparison: 13/48 < C_1 < C_AF")
    print("base/recursive capacity filter diagnostic: PASS")


if __name__ == "__main__":
    audit()
