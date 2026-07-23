"""Independent exact checker for the zigzag-witness history class.

The checker imports no project, production, test, or artifact helper.  It
does two independent jobs:

1. exhaust every target-connector subset, every selected-label assignment,
   and every literal completion in several small rational fixtures;
2. reconstruct the all-middle scalar recurrence in Q(sqrt(2)) and verify the
   exact positive limiting lower-bound coefficient.

The small fixtures are structural checks.  They deliberately do not pretend
to realize the eventual irrational floor/ceiling rows, whose first admissible
instances are already too large for literal exhaustive enumeration.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial, sqrt


Edge = frozenset[int]
Cycle = tuple[int, ...]


@dataclass(frozen=True)
class Radical2:
    """An exact element ``rational + rational * sqrt(2)``."""

    rational: Fraction
    radical: Fraction = Fraction()

    @staticmethod
    def coerce(value: "Radical2 | Fraction | int") -> "Radical2":
        if isinstance(value, Radical2):
            return value
        return Radical2(Fraction(value))

    def __add__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        rhs = self.coerce(other)
        return Radical2(
            self.rational + rhs.rational,
            self.radical + rhs.radical,
        )

    def __radd__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        return self + other

    def __neg__(self) -> "Radical2":
        return Radical2(-self.rational, -self.radical)

    def __sub__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        return self + (-self.coerce(other))

    def __rsub__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        return self.coerce(other) - self

    def __mul__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        rhs = self.coerce(other)
        return Radical2(
            self.rational * rhs.rational + 2 * self.radical * rhs.radical,
            self.rational * rhs.radical + self.radical * rhs.rational,
        )

    def __rmul__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        return self * other

    def __truediv__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        rhs = self.coerce(other)
        denominator = rhs.rational**2 - 2 * rhs.radical**2
        if denominator == 0:
            raise ZeroDivisionError
        return self * Radical2(
            rhs.rational / denominator,
            -rhs.radical / denominator,
        )

    def __rtruediv__(self, other: "Radical2 | Fraction | int") -> "Radical2":
        return self.coerce(other) / self

    def __pow__(self, exponent: int) -> "Radical2":
        if exponent < 0:
            return (1 / self) ** (-exponent)
        result = Radical2(Fraction(1))
        for _ in range(exponent):
            result *= self
        return result

    def sign(self) -> int:
        """Return the exact sign, using irrationality of sqrt(2)."""
        p = self.rational
        q = self.radical
        if q == 0:
            return (p > 0) - (p < 0)
        if p == 0:
            return (q > 0) - (q < 0)
        if p > 0 and q > 0:
            return 1
        if p < 0 and q < 0:
            return -1
        comparison = p * p - 2 * q * q
        if p > 0:
            return 1 if comparison > 0 else -1
        return 1 if comparison < 0 else -1

    def decimal(self) -> float:
        """Return a display-only approximation; assertions remain exact."""
        return float(self.rational) + float(self.radical) * sqrt(2)


@dataclass(frozen=True)
class Fixture:
    n: int
    r: int
    cutoffs: tuple[int, ...]
    weights: tuple[Fraction, ...]
    expected_histories: int | None = None
    expected_minimum_height: Fraction | None = None
    expected_minimum_residual: Fraction | None = None


FIXTURES = (
    Fixture(
        n=10,
        r=6,
        cutoffs=(5, 3),
        weights=(Fraction(3, 4), Fraction(1, 4)),
        expected_histories=432,
        expected_minimum_height=Fraction(13),
        expected_minimum_residual=Fraction(2497, 140),
    ),
    Fixture(
        n=11,
        r=5,
        cutoffs=(4, 3),
        weights=(Fraction(2, 3), Fraction(1, 3)),
    ),
    Fixture(
        n=13,
        r=6,
        cutoffs=(5,),
        weights=(Fraction(1, 2),),
    ),
    Fixture(
        n=14,
        r=6,
        cutoffs=(5, 4, 3),
        weights=(Fraction(3, 4), Fraction(1, 2), Fraction(1, 4)),
    ),
)


def zigzag_cycle(q: int, shift: int) -> Cycle:
    """Return the translated parity-uniform zigzag cycle."""
    raw: list[int] = []
    for low in range(q // 2):
        raw.extend((low, q - 1 - low))
    if q % 2:
        raw.append(q // 2)
    return tuple(shift + value for value in raw)


def oriented_edges(cycle: Cycle) -> tuple[tuple[int, int], ...]:
    """Return the cyclic oriented edges in tuple order."""
    return tuple(
        (cycle[index], cycle[(index + 1) % len(cycle)]) for index in range(len(cycle))
    )


def edge_key(u: int, v: int) -> Edge:
    return frozenset((u, v))


def split_at(cycle: Cycle, index: int, label: int) -> Cycle:
    """Insert ``label`` into the edge beginning at ``index``."""
    if index == len(cycle) - 1:
        return (*cycle, label)
    return (*cycle[: index + 1], label, *cycle[index + 1 :])


def split_edge(cycle: Cycle, edge: Edge, label: int) -> tuple[Cycle, int, int]:
    """Split one named unordered edge and return its oriented endpoints."""
    matches = [
        (index, u, v)
        for index, (u, v) in enumerate(oriented_edges(cycle))
        if edge_key(u, v) == edge
    ]
    if len(matches) != 1:
        raise AssertionError(f"edge {sorted(edge)} occurs {len(matches)} times")
    index, u, v = matches[0]
    return split_at(cycle, index, label), u, v


def cycle_score(cycle: Cycle) -> int:
    return sum(u * v for u, v in oriented_edges(cycle))


def correction(label: int, u: int, v: int) -> int:
    return label * (u + v) - u * v


def slack(n: int, r: int, u: int, v: int) -> Fraction:
    return Fraction((u + v - n - r) ** 2, 2)


def pairing_floor(n: int, r: int) -> int:
    return sum(label * (n + r - label) for label in range(r, n + 1))


def local_floor(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    total = n + r
    return (
        weight
        * (4 * total * label - total**2 - 2 * weight * label**2)
        / (2 * (2 - weight))
    )


def selected_parameters(
    fixture: Fixture,
) -> tuple[dict[int, Fraction], dict[int, int], Fraction]:
    """Return label weights, label cutoffs, and the exact B value."""
    if len(fixture.cutoffs) != len(fixture.weights):
        raise AssertionError("cutoff/weight length mismatch")
    if tuple(sorted(fixture.cutoffs, reverse=True)) != fixture.cutoffs:
        raise AssertionError("cutoffs are not strictly descending")
    if tuple(sorted(fixture.weights, reverse=True)) != fixture.weights:
        raise AssertionError("weights are not nonincreasing")

    weights_by_label: dict[int, Fraction] = {}
    cutoffs_by_label: dict[int, int] = {}
    upper = fixture.r
    residual = Fraction()
    for cutoff, weight in zip(fixture.cutoffs, fixture.weights):
        if not 1 <= cutoff < upper:
            raise AssertionError("invalid cutoff")
        for label in range(cutoff, upper):
            weights_by_label[label] = weight
            cutoffs_by_label[label] = cutoff
        residual += (upper - cutoff) * local_floor(
            fixture.n,
            fixture.r,
            weight,
            cutoff,
        )
        upper = cutoff

    s = fixture.cutoffs[-1]
    if set(weights_by_label) != set(range(s, fixture.r)):
        raise AssertionError("selected labels are not partitioned exactly")
    return (
        weights_by_label,
        cutoffs_by_label,
        Fraction(pairing_floor(fixture.n, fixture.r)) + residual,
    )


@lru_cache(maxsize=None)
def completion_excursion(cycle: Cycle, label: int) -> Fraction:
    """Exact DP (KR1G-35) for the future positive excursion."""
    if label == 0:
        return Fraction()
    candidates: list[Fraction] = []
    for index, (u, v) in enumerate(oriented_edges(cycle)):
        child = split_at(cycle, index, label)
        candidates.append(
            max(
                Fraction(),
                Fraction(correction(label, u, v))
                + completion_excursion(child, label - 1),
            )
        )
    return min(candidates)


def verify_all_middle_scalar_bound(rows: int = 12) -> None:
    """Check the fixed-k scalar lower bounds exactly in Q(sqrt(2))."""
    a = Radical2(Fraction(13, 23), Fraction(-2, 23))
    total = 1 + a
    active = 3 * a - 1
    delta_infinity = active**2 * (7 - 9 * a) / 96
    expected = Radical2(Fraction(470, 73002), Fraction(-159, 73002))
    if delta_infinity != expected:
        raise AssertionError((delta_infinity, expected))
    if delta_infinity.sign() <= 0:
        raise AssertionError("limiting coefficient is not positive")
    if 470**2 - 2 * 159**2 != 170338:
        raise AssertionError("radical square margin mismatch")

    simplex = Fraction()
    for k in range(1, rows + 1):
        ratio = Fraction(2, 3) / (1 - simplex)
        simplex = ratio**2 / 3
        if not simplex < Fraction(1, 3):
            raise AssertionError(f"k={k}: simplex value reached 1/3")
        delta_k = total * active**2 / 32 - active**3 * simplex / 8
        difference = delta_k - delta_infinity
        if difference.sign() <= 0:
            raise AssertionError(f"k={k}: fixed-k bound lost strict margin")

    print(
        f"Q(sqrt(2)): k=1..{rows} exact scalar bounds PASS; "
        f"delta_infinity={delta_infinity.decimal():.18f}"
    )


def verify_fixture(fixture: Fixture) -> tuple[int, Fraction, Fraction]:
    """Exhaust one complete small history class with exact arithmetic."""
    n = fixture.n
    r = fixture.r
    s = fixture.cutoffs[-1]
    q = n - r + 1
    ell = r - s
    base_cycle = zigzag_cycle(q, r)
    base_edges = {edge_key(u, v): (u, v) for u, v in oriented_edges(base_cycle)}
    closing = edge_key(base_cycle[-1], base_cycle[0])
    connectors = tuple(edge_key(r + x, n + 1 - x) for x in range(1, (q - 1) // 2 + 1))
    if closing in connectors:
        raise AssertionError("closing edge misclassified as connector")
    if ell < 1 or ell - 1 > len(connectors):
        raise AssertionError("fixture has no zigzag witness target set")

    weights_by_label, cutoffs_by_label, bound = selected_parameters(fixture)
    base_score = cycle_score(base_cycle)
    pair_floor = pairing_floor(n, r)
    base_slack = sum(
        (slack(n, r, u, v) for u, v in oriented_edges(base_cycle)),
        Fraction(),
    )
    if Fraction(base_score - pair_floor) != base_slack:
        raise AssertionError("base-slack identity failed")

    edge_sum_cap = n + r + 1
    d = (edge_sum_cap + 3) // 4
    height_barrier = sum(
        (
            Fraction(edge_sum_cap * label) - Fraction(edge_sum_cap**2, 4)
            for label in range(d, r)
        ),
        Fraction(),
    )
    finite_lower_bound = base_slack + height_barrier - (bound - pair_floor)

    total_histories = 0
    minimum_height: Fraction | None = None
    minimum_residual: Fraction | None = None
    target_set_count = 0
    assignment_count = 0

    for connector_subset in combinations(connectors, ell - 1):
        target_set_count += 1
        targets = (closing, *connector_subset)
        for assignment in permutations(targets):
            assignment_count += 1
            selected_cycle = base_cycle
            selected_height = Fraction()
            selected_peak = Fraction()
            selected_records: list[tuple[int, int, int, Fraction, int, Edge]] = []

            for label, target in zip(range(r - 1, s - 1, -1), assignment):
                parent_cycle = selected_cycle
                selected_cycle, u, v = split_edge(selected_cycle, target, label)
                value = Fraction(correction(label, u, v))
                universal = Fraction(edge_sum_cap * label) - Fraction(
                    edge_sum_cap**2, 4
                )
                if value < universal:
                    raise AssertionError("selected correction bound failed")
                if cycle_score(selected_cycle) - cycle_score(parent_cycle) != value:
                    raise AssertionError("selected score correction failed")
                selected_height += value
                selected_peak = max(selected_peak, selected_height)
                selected_records.append(
                    (
                        label,
                        u,
                        v,
                        weights_by_label[label],
                        cutoffs_by_label[label],
                        target,
                    )
                )
                if max(x + y for x, y in oriented_edges(selected_cycle)) > edge_sum_cap:
                    raise AssertionError("edge-sum cap failed during selected splits")

            dp_excursion = completion_excursion(selected_cycle, s - 1)
            assignment_minimum_height: Fraction | None = None
            assignment_minimum_excursion: Fraction | None = None

            def exhaust_completion(
                cycle: Cycle,
                label: int,
                completion_height: Fraction,
                completion_peak: Fraction,
            ) -> None:
                nonlocal total_histories
                nonlocal minimum_height
                nonlocal minimum_residual
                nonlocal assignment_minimum_height
                nonlocal assignment_minimum_excursion

                if label == 0:
                    total_histories += 1
                    full_peak = max(
                        selected_peak,
                        selected_height + completion_peak,
                    )
                    residual = Fraction(base_score) + full_peak - bound

                    weighted_height = sum(
                        (
                            weight * correction(t, u, v)
                            for t, u, v, weight, _, _ in selected_records
                        ),
                        Fraction(),
                    )
                    height_loss = full_peak - weighted_height
                    unused = sum(
                        (
                            slack(n, r, u, v)
                            for key, (u, v) in base_edges.items()
                            if key not in targets
                        ),
                        Fraction(),
                    )
                    product_loss = Fraction()
                    square_loss = Fraction()
                    monotonicity_loss = Fraction()
                    total_label = n + r
                    for t, u, v, weight, cutoff, _ in selected_records:
                        product_loss += weight * Fraction((u - v) ** 2, 4)
                        center = Fraction(u + v) - 2 * (
                            Fraction(total_label) - weight * t
                        ) / (2 - weight)
                        square_loss += (2 - weight) * center**2 / 4
                        monotonicity_loss += local_floor(n, r, weight, t) - local_floor(
                            n, r, weight, cutoff
                        )

                    decomposition = (
                        height_loss
                        + unused
                        + product_loss
                        + square_loss
                        + monotonicity_loss
                    )
                    if residual != decomposition:
                        raise AssertionError(
                            f"KR1G decomposition failed: {residual} != {decomposition}"
                        )
                    if (
                        min(
                            height_loss,
                            unused,
                            product_loss,
                            square_loss,
                            monotonicity_loss,
                        )
                        < 0
                    ):
                        raise AssertionError("negative decomposition term")
                    if full_peak < height_barrier:
                        raise AssertionError("height barrier failed")
                    if residual < finite_lower_bound:
                        raise AssertionError("finite residual bound failed")

                    minimum_height = (
                        full_peak
                        if minimum_height is None
                        else min(minimum_height, full_peak)
                    )
                    minimum_residual = (
                        residual
                        if minimum_residual is None
                        else min(minimum_residual, residual)
                    )
                    assignment_minimum_height = (
                        full_peak
                        if assignment_minimum_height is None
                        else min(assignment_minimum_height, full_peak)
                    )
                    assignment_minimum_excursion = (
                        completion_peak
                        if assignment_minimum_excursion is None
                        else min(assignment_minimum_excursion, completion_peak)
                    )
                    return

                for index, (u, v) in enumerate(oriented_edges(cycle)):
                    value = Fraction(correction(label, u, v))
                    universal = Fraction(edge_sum_cap * label) - Fraction(
                        edge_sum_cap**2, 4
                    )
                    if value < universal:
                        raise AssertionError("pointwise correction bound failed")
                    child = split_at(cycle, index, label)
                    if cycle_score(child) - cycle_score(cycle) != value:
                        raise AssertionError("completion score correction failed")
                    if max(x + y for x, y in oriented_edges(child)) > edge_sum_cap:
                        raise AssertionError("edge-sum cap failed in completion")
                    next_height = completion_height + value
                    exhaust_completion(
                        child,
                        label - 1,
                        next_height,
                        max(completion_peak, next_height),
                    )

            exhaust_completion(
                selected_cycle,
                s - 1,
                Fraction(),
                Fraction(),
            )
            if assignment_minimum_excursion != dp_excursion:
                raise AssertionError(
                    "literal completion and independent DP disagree: "
                    f"{assignment_minimum_excursion} != {dp_excursion}"
                )
            expected_assignment_height = max(
                selected_peak,
                selected_height + dp_excursion,
            )
            if assignment_minimum_height != expected_assignment_height:
                raise AssertionError(
                    "selected-root peak reconstruction failed: "
                    f"{assignment_minimum_height} != {expected_assignment_height}"
                )

    completion_count = factorial(n - 1) // factorial(n - s)
    expected_histories = (
        comb(len(connectors), ell - 1) * factorial(ell) * completion_count
    )
    if target_set_count != comb(len(connectors), ell - 1):
        raise AssertionError("target-set count mismatch")
    if assignment_count != target_set_count * factorial(ell):
        raise AssertionError("assignment count mismatch")
    if total_histories != expected_histories:
        raise AssertionError(
            f"got {total_histories} histories, expected {expected_histories}"
        )
    if fixture.expected_histories is not None:
        if total_histories != fixture.expected_histories:
            raise AssertionError("golden history count mismatch")
    if minimum_height is None or minimum_residual is None:
        raise AssertionError("empty fixture")
    if fixture.expected_minimum_height is not None:
        if minimum_height != fixture.expected_minimum_height:
            raise AssertionError(
                f"golden height mismatch: {minimum_height} != "
                f"{fixture.expected_minimum_height}"
            )
    if fixture.expected_minimum_residual is not None:
        if minimum_residual != fixture.expected_minimum_residual:
            raise AssertionError(
                f"golden residual mismatch: {minimum_residual} != "
                f"{fixture.expected_minimum_residual}"
            )

    print(
        f"n={n:2d} r={r:2d} s={s:2d} ell={ell} "
        f"targets={target_set_count:2d} assignments={assignment_count:3d} "
        f"histories={total_histories:6d} min_M={minimum_height} "
        f"min_residual={minimum_residual}: PASS"
    )
    return total_histories, minimum_height, minimum_residual


def main() -> None:
    verify_all_middle_scalar_bound()
    total = 0
    for fixture in FIXTURES:
        histories, _, _ = verify_fixture(fixture)
        total += histories
    print(
        f"PASS: {len(FIXTURES)} fixtures, {total} literal histories, "
        "all target subsets and assignments, exact DP agreement, "
        "KR1G decomposition, edge-sum invariant, and cubic barrier"
    )


if __name__ == "__main__":
    main()
