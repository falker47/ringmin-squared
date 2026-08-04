"""Independent exact checker for one selected recursive KR1G split.

The checker imports no project module and no earlier dossier helper.  It uses
only standard-library ``Fraction`` arithmetic.

For every admitted synthetic fixture it enumerates Hamiltonian base cycles
modulo rotation and reversal, every selected history having exactly one
recursive split, and every permitted position and direct parent of that
split.  All other selected splits use distinct untouched original edges.  A
separate two-segment fixture exhausts every compatible completion below the
selected window.

For each complete history the checker independently evaluates the direct
residual and verifies the specialized KR1G-6 decomposition, the parent-child
classification, the base/unused deviation identity, the radical finite
envelope, the position-dependent optimized rational bound, and the
position-uniform finite bound.  These bounded rational fixtures corroborate
the finite algebra; they are not rounded rows of the irrational all-middle
tuple and do not prove the all-q or asymptotic theorem.
"""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial


Cycle = tuple[int, ...]
Edge = frozenset[int]

MIN_Q = 5
MAX_Q = 7


@dataclass(frozen=True)
class Fixture:
    """One exact selected-window and completion instance."""

    q: int
    ell: int
    s: int
    cutoffs: tuple[int, ...]
    weights: tuple[Fraction, ...]
    name: str

    @property
    def r(self) -> int:
        return self.s + self.ell

    @property
    def n(self) -> int:
        return self.r + self.q - 1


@dataclass(frozen=True)
class Parameters:
    """History-independent finite quantities for a fixture."""

    weights_by_label: dict[int, Fraction]
    cutoffs_by_label: dict[int, int]
    bound: Fraction
    total_shift: Fraction
    reciprocal_weight: Fraction


@dataclass(frozen=True)
class Record:
    """One selected split."""

    label: int
    u: int
    v: int
    weight: Fraction
    cutoff: int
    kind: str
    original_edge: Edge | None


@dataclass(frozen=True)
class CheckResult:
    """Selected values returned by one complete-history check."""

    residual: Fraction
    optimized_bound: Fraction
    recursive_label: int
    coverage_loss: Fraction


@dataclass(frozen=True)
class FixtureResult:
    """Enumeration totals and exact extrema for one fixture."""

    selected_histories: int
    complete_histories: int
    recursive_positions: tuple[tuple[int, int], ...]
    zero_coverage_histories: int
    two_inserted_completion_histories: int
    minimum_residual: Fraction
    minimum_optimized_bound: Fraction


def canonical_cycles(q: int):
    """Yield cycles on ``range(q)`` once modulo rotation and reversal."""
    for tail in permutations(range(1, q)):
        if tail[0] < tail[-1]:
            yield (0, *tail)


def oriented_edges(cycle: Cycle) -> tuple[tuple[int, int], ...]:
    """Return the cyclic oriented edges in tuple order."""
    return tuple(
        (cycle[index], cycle[(index + 1) % len(cycle)]) for index in range(len(cycle))
    )


def edge_key(u: int, v: int) -> Edge:
    """Return an unordered edge key."""
    return frozenset((u, v))


def split_at(cycle: Cycle, index: int, label: int) -> Cycle:
    """Insert ``label`` into the oriented edge beginning at ``index``."""
    if index == len(cycle) - 1:
        return (*cycle, label)
    return (*cycle[: index + 1], label, *cycle[index + 1 :])


def cycle_score(cycle: Cycle) -> int:
    """Return the cyclic adjacent-product score."""
    return sum(u * v for u, v in oriented_edges(cycle))


def correction(label: int, u: int, v: int) -> int:
    """Return the exact score change from splitting ``{u,v}`` at ``label``."""
    return label * (u + v) - u * v


def original_slack(n: int, r: int, u: int, v: int) -> Fraction:
    """Return the quadratic slack of one original edge."""
    return Fraction((u + v - n - r) ** 2, 2)


def pairing_floor(n: int, r: int) -> int:
    """Compute ``P_{r,n}`` directly from the complementary matching."""
    return sum(label * (n + r - label) for label in range(r, n + 1))


def local_floor(
    n: int,
    r: int,
    weight: Fraction,
    label: int,
) -> Fraction:
    """Return ``G_{n,weight}(label)`` from its defining expression."""
    total = n + r
    return (
        weight
        * (4 * total * label - total**2 - 2 * weight * label**2)
        / (2 * (2 - weight))
    )


def recursive_floor(
    n: int,
    r: int,
    weight: Fraction,
    label: int,
) -> Fraction:
    """Return ``J_{n,weight}(label)`` from its defining expression."""
    return weight * ((n + r - 1) * label - n * (r - 1))


def selected_parameters(fixture: Fixture) -> Parameters:
    """Build segment maps and the exact finite ``B,T,Q`` quantities."""
    if len(fixture.cutoffs) != len(fixture.weights):
        raise AssertionError("cutoff/weight length mismatch")
    if not fixture.cutoffs or fixture.cutoffs[-1] != fixture.s:
        raise AssertionError("last cutoff is not s")
    if tuple(sorted(fixture.weights, reverse=True)) != fixture.weights:
        raise AssertionError("weights are not nonincreasing")
    if not all(Fraction() < weight < 1 for weight in fixture.weights):
        raise AssertionError("weights must lie strictly between zero and one")

    weights_by_label: dict[int, Fraction] = {}
    cutoffs_by_label: dict[int, int] = {}
    selected_floor = Fraction()
    upper = fixture.r
    for cutoff, weight in zip(fixture.cutoffs, fixture.weights):
        if not 1 <= cutoff < upper:
            raise AssertionError("cutoffs are not strictly descending")
        for label in range(cutoff, upper):
            weights_by_label[label] = weight
            cutoffs_by_label[label] = cutoff
        selected_floor += (upper - cutoff) * local_floor(
            fixture.n,
            fixture.r,
            weight,
            cutoff,
        )
        upper = cutoff

    selected_labels = set(range(fixture.s, fixture.r))
    if set(weights_by_label) != selected_labels:
        raise AssertionError("selected labels are not partitioned exactly")

    total = fixture.n + fixture.r
    total_shift = sum(
        (
            weights_by_label[label]
            * (total - 2 * label)
            / (2 - weights_by_label[label])
            for label in selected_labels
        ),
        Fraction(),
    )
    reciprocal_weight = sum(
        (4 / (2 - weights_by_label[label]) for label in selected_labels),
        Fraction(),
    )
    if total_shift <= 0 or reciprocal_weight <= 0:
        raise AssertionError("T and Q must be positive")

    return Parameters(
        weights_by_label=weights_by_label,
        cutoffs_by_label=cutoffs_by_label,
        bound=Fraction(pairing_floor(fixture.n, fixture.r)) + selected_floor,
        total_shift=total_shift,
        reciprocal_weight=reciprocal_weight,
    )


def surd_nonnegative(
    rational_part: Fraction,
    sqrt_coefficient: Fraction,
    radicand: Fraction,
) -> bool:
    """Decide ``a + b*sqrt(x) >= 0`` exactly."""
    if radicand < 0:
        raise AssertionError("negative radicand")
    if sqrt_coefficient == 0 or radicand == 0:
        return rational_part >= 0
    squared_term = sqrt_coefficient**2 * radicand
    if sqrt_coefficient > 0:
        return rational_part >= 0 or squared_term >= rational_part**2
    return rational_part >= 0 and rational_part**2 >= squared_term


def check_radical_chain(
    retained_residual: Fraction,
    unused: Fraction,
    total_shift: Fraction,
    reciprocal_weight: Fraction,
    unused_count: int,
) -> None:
    """Check the radical envelope and its scalar optimum exactly."""
    radicand = 2 * unused_count * unused
    optimized = total_shift**2 / (reciprocal_weight + 2 * unused_count)

    if radicand >= total_shift**2:
        if retained_residual < unused:
            raise AssertionError("inactive radical envelope failed")
        if unused < optimized:
            raise AssertionError("inactive scalar optimum failed")
    else:
        residual_difference = (
            retained_residual - unused - (total_shift**2 + radicand) / reciprocal_weight
        )
        radical_coefficient = 2 * total_shift / reciprocal_weight
        if not surd_nonnegative(
            residual_difference,
            radical_coefficient,
            radicand,
        ):
            raise AssertionError("active radical envelope failed")

        envelope_difference = (
            unused + (total_shift**2 + radicand) / reciprocal_weight - optimized
        )
        if not surd_nonnegative(
            envelope_difference,
            -radical_coefficient,
            radicand,
        ):
            raise AssertionError("active scalar optimum failed")

    if retained_residual < optimized:
        raise AssertionError("optimized finite bound failed")


def displacement(
    n: int,
    r: int,
    label: int,
    weight: Fraction,
) -> Fraction:
    """Return the positive square-center displacement ``d_t``."""
    return weight * (n + r - 2 * label) / (2 - weight)


def check_complete_history(
    fixture: Fixture,
    parameters: Parameters,
    base_cycle: Cycle,
    records: tuple[Record, ...],
    complete_peak: Fraction,
) -> CheckResult:
    """Compare direct residual, decomposition, and both finite bounds."""
    n = fixture.n
    r = fixture.r
    total = n + r
    base_oriented = oriented_edges(base_cycle)
    base_edges = tuple(edge_key(u, v) for u, v in base_oriented)
    base_score = cycle_score(base_cycle)
    base_slack = sum(
        (original_slack(n, r, u, v) for u, v in base_oriented),
        Fraction(),
    )
    if Fraction(base_score - pairing_floor(n, r)) != base_slack:
        raise AssertionError("base-slack identity failed")

    recursive_records = tuple(
        record for record in records if record.kind == "recursive"
    )
    base_records = tuple(record for record in records if record.kind == "base")
    if len(recursive_records) != 1 or len(base_records) != fixture.ell - 1:
        raise AssertionError("wrong selected split-type counts")
    recursive_record = recursive_records[0]
    if recursive_record.label == r - 1:
        raise AssertionError("the first selected split cannot be recursive")

    base_targets = tuple(record.original_edge for record in base_records)
    if any(target is None for target in base_targets):
        raise AssertionError("base split without original target")
    if len(set(base_targets)) != fixture.ell - 1:
        raise AssertionError("base targets are not distinct")
    target_set = set(base_targets)
    unused_records = tuple(
        (u, v)
        for key, (u, v) in zip(base_edges, base_oriented)
        if key not in target_set
    )
    unused_count = fixture.q - fixture.ell + 1
    if len(unused_records) != unused_count:
        raise AssertionError("wrong unused-original-edge count")
    unused = sum(
        (original_slack(n, r, u, v) for u, v in unused_records),
        Fraction(),
    )

    inserted_endpoints = tuple(
        endpoint
        for endpoint in (recursive_record.u, recursive_record.v)
        if endpoint < r
    )
    original_endpoints = tuple(
        endpoint
        for endpoint in (recursive_record.u, recursive_record.v)
        if endpoint >= r
    )
    if len(inserted_endpoints) != 1 or len(original_endpoints) != 1:
        raise AssertionError("selected recursive edge is not a direct child")
    parent_label = inserted_endpoints[0]
    child_original_endpoint = original_endpoints[0]
    if parent_label <= recursive_record.label:
        raise AssertionError("recursive parent was not inserted earlier")
    parent_records = tuple(
        record for record in base_records if record.label == parent_label
    )
    if len(parent_records) != 1:
        raise AssertionError("recursive edge has no unique base parent")
    parent_target = parent_records[0].original_edge
    if parent_target is None or child_original_endpoint not in parent_target:
        raise AssertionError("recursive child is not incident to its parent edge")

    base_delta = sum(record.u + record.v - total for record in base_records)
    unused_delta = sum(u + v - total for u, v in unused_records)
    if base_delta != -unused_delta:
        raise AssertionError("base/unused deviation identity failed")
    if base_delta**2 > 2 * unused_count * unused:
        raise AssertionError("unused-edge deviation Cauchy failed")

    residual = Fraction(base_score) + complete_peak - parameters.bound
    weighted_height = sum(
        (
            record.weight * correction(record.label, record.u, record.v)
            for record in records
        ),
        Fraction(),
    )
    height_loss = complete_peak - weighted_height

    product_loss = Fraction()
    square_loss = Fraction()
    monotonicity_loss = Fraction()
    selected_center_sum = Fraction()
    for record in base_records:
        delta = Fraction(record.u + record.v - total)
        center = displacement(
            n,
            r,
            record.label,
            record.weight,
        )
        product_loss += record.weight * Fraction(
            (record.u - record.v) ** 2,
            4,
        )
        square_loss += (2 - record.weight) * (delta - center) ** 2 / 4
        monotonicity_loss += local_floor(
            n,
            r,
            record.weight,
            record.label,
        ) - local_floor(
            n,
            r,
            record.weight,
            record.cutoff,
        )
        selected_center_sum += center - delta

    recursive_weight = recursive_record.weight
    recursive_label = recursive_record.label
    inserted_parent = parent_label
    original_child = child_original_endpoint
    coverage_loss = recursive_weight * (
        (r - 1 - recursive_label) * (n - recursive_label)
        - (inserted_parent - recursive_label) * (original_child - recursive_label)
    )
    jg_loss = recursive_floor(
        n,
        r,
        recursive_weight,
        recursive_label,
    ) - local_floor(
        n,
        r,
        recursive_weight,
        recursive_label,
    )
    closed_jg_loss = (
        recursive_weight
        * (
            (n - r) ** 2
            + 4 * (n - recursive_label)
            + 2 * recursive_weight * (r - 1 - recursive_label) * (n - recursive_label)
        )
        / (2 * (2 - recursive_weight))
    )
    if jg_loss != closed_jg_loss:
        raise AssertionError("J-G closed form failed")
    recursive_monotonicity = local_floor(
        n,
        r,
        recursive_weight,
        recursive_label,
    ) - local_floor(
        n,
        r,
        recursive_weight,
        recursive_record.cutoff,
    )
    recursive_loss = coverage_loss + jg_loss + recursive_monotonicity

    decomposition = (
        height_loss
        + unused
        + product_loss
        + square_loss
        + monotonicity_loss
        + recursive_loss
    )
    if residual != decomposition:
        raise AssertionError(
            f"KR1G-6 decomposition failed: {residual} != {decomposition}"
        )
    if (
        min(
            height_loss,
            unused,
            product_loss,
            square_loss,
            monotonicity_loss,
            coverage_loss,
            jg_loss,
            recursive_monotonicity,
        )
        < 0
    ):
        raise AssertionError("negative KR1G decomposition term")

    omitted_center = displacement(
        n,
        r,
        recursive_label,
        recursive_weight,
    )
    omitted_reciprocal = 4 / (2 - recursive_weight)
    base_shift = parameters.total_shift - omitted_center
    base_reciprocal = parameters.reciprocal_weight - omitted_reciprocal
    if base_shift <= 0 or base_reciprocal <= 0:
        raise AssertionError("empty base square-center family")
    if selected_center_sum != base_shift - base_delta:
        raise AssertionError("base square-center sum failed")
    if square_loss * base_reciprocal < selected_center_sum**2:
        raise AssertionError("base weighted Cauchy failed")

    combined_linear_sum = selected_center_sum - unused_delta
    if combined_linear_sum != base_shift:
        raise AssertionError("combined-Cauchy linear identity failed")
    optimized_bound = recursive_loss + base_shift**2 / (
        base_reciprocal + 2 * unused_count
    )
    if unused + square_loss < base_shift**2 / (base_reciprocal + 2 * unused_count):
        raise AssertionError("direct combined-Cauchy bound failed")
    if residual < optimized_bound:
        raise AssertionError("position-parent optimized bound failed")

    check_radical_chain(
        residual - recursive_loss,
        unused,
        base_shift,
        base_reciprocal,
        unused_count,
    )

    eligible_recursive_labels = range(fixture.s, fixture.r - 1)
    maximum_omitted_center = max(
        displacement(
            n,
            r,
            label,
            parameters.weights_by_label[label],
        )
        for label in eligible_recursive_labels
    )
    m = fixture.q - fixture.ell
    if base_reciprocal + 2 * unused_count > parameters.reciprocal_weight + 2 * m:
        raise AssertionError("uniform denominator comparison failed")
    uniform_bound = (parameters.total_shift - maximum_omitted_center) ** 2 / (
        parameters.reciprocal_weight + 2 * m
    )
    if residual < uniform_bound:
        raise AssertionError("position-uniform finite bound failed")

    return CheckResult(
        residual=residual,
        optimized_bound=optimized_bound,
        recursive_label=recursive_label,
        coverage_loss=coverage_loss,
    )


@lru_cache(maxsize=None)
def completion_excursion(cycle: Cycle, label: int) -> Fraction:
    """Return the exact minimum future positive excursion."""
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


def falling_factorial(n: int, length: int) -> int:
    """Return ``n*(n-1)*...`` with ``length`` factors."""
    return factorial(n) // factorial(n - length)


def verify_fixture(
    fixture: Fixture,
    raw_cycles: tuple[Cycle, ...],
) -> FixtureResult:
    """Enumerate and check every declared history for one fixture."""
    if not 2 <= fixture.ell < (fixture.q + 1) // 2:
        raise AssertionError("fixture is outside the one-recursive domain")
    parameters = selected_parameters(fixture)
    selected_labels = tuple(range(fixture.r - 1, fixture.s - 1, -1))
    recursive_labels = selected_labels[1:]

    selected_histories = 0
    complete_histories = 0
    recursive_positions: Counter[int] = Counter()
    zero_coverage_histories = 0
    two_inserted_completion_histories = 0
    minimum_residual: Fraction | None = None
    minimum_optimized_bound: Fraction | None = None

    for raw_cycle in raw_cycles:
        base_cycle = tuple(fixture.r + value for value in raw_cycle)
        original_edge_set = {edge_key(u, v) for u, v in oriented_edges(base_cycle)}

        for designated_recursive_label in recursive_labels:

            def exhaust_selected(
                current: Cycle,
                index: int,
                height: Fraction,
                peak: Fraction,
                records: tuple[Record, ...],
            ) -> None:
                nonlocal complete_histories
                nonlocal minimum_optimized_bound
                nonlocal minimum_residual
                nonlocal selected_histories
                nonlocal two_inserted_completion_histories
                nonlocal zero_coverage_histories

                if index == len(selected_labels):
                    selected_histories += 1
                    position = selected_labels.index(designated_recursive_label)
                    recursive_positions[position] += 1
                    literal_minimum_peak: Fraction | None = None

                    def exhaust_completion(
                        completion_cycle: Cycle,
                        label: int,
                        completion_height: Fraction,
                        completion_peak: Fraction,
                        used_two_inserted_edge: bool,
                    ) -> None:
                        nonlocal complete_histories
                        nonlocal literal_minimum_peak
                        nonlocal minimum_optimized_bound
                        nonlocal minimum_residual
                        nonlocal two_inserted_completion_histories
                        nonlocal zero_coverage_histories

                        if label == 0:
                            complete_histories += 1
                            if used_two_inserted_edge:
                                two_inserted_completion_histories += 1
                            result = check_complete_history(
                                fixture,
                                parameters,
                                base_cycle,
                                records,
                                completion_peak,
                            )
                            if result.coverage_loss == 0:
                                zero_coverage_histories += 1
                            literal_minimum_peak = (
                                completion_peak
                                if literal_minimum_peak is None
                                else min(
                                    literal_minimum_peak,
                                    completion_peak,
                                )
                            )
                            minimum_residual = (
                                result.residual
                                if minimum_residual is None
                                else min(
                                    minimum_residual,
                                    result.residual,
                                )
                            )
                            minimum_optimized_bound = (
                                result.optimized_bound
                                if minimum_optimized_bound is None
                                else min(
                                    minimum_optimized_bound,
                                    result.optimized_bound,
                                )
                            )
                            return

                        for edge_index, (u, v) in enumerate(
                            oriented_edges(completion_cycle)
                        ):
                            child = split_at(
                                completion_cycle,
                                edge_index,
                                label,
                            )
                            next_height = completion_height + Fraction(
                                correction(label, u, v)
                            )
                            exhaust_completion(
                                child,
                                label - 1,
                                next_height,
                                max(completion_peak, next_height),
                                used_two_inserted_edge
                                or (u < fixture.r and v < fixture.r),
                            )

                    exhaust_completion(
                        current,
                        fixture.s - 1,
                        height,
                        peak,
                        False,
                    )
                    expected_minimum_peak = max(
                        peak,
                        height
                        + completion_excursion(
                            current,
                            fixture.s - 1,
                        ),
                    )
                    if literal_minimum_peak != expected_minimum_peak:
                        raise AssertionError(
                            "literal completion and independent DP disagree"
                        )
                    return

                label = selected_labels[index]
                want_recursive = label == designated_recursive_label
                for edge_index, (u, v) in enumerate(oriented_edges(current)):
                    target = edge_key(u, v)
                    is_original = target in original_edge_set
                    if want_recursive == is_original:
                        continue
                    if want_recursive:
                        inserted_count = int(u < fixture.r) + int(v < fixture.r)
                        if inserted_count != 1:
                            raise AssertionError(
                                "selected recursive edge is not direct"
                            )

                    child = split_at(current, edge_index, label)
                    value = Fraction(correction(label, u, v))
                    if cycle_score(child) - cycle_score(current) != value:
                        raise AssertionError("score correction failed")
                    record = Record(
                        label=label,
                        u=u,
                        v=v,
                        weight=parameters.weights_by_label[label],
                        cutoff=parameters.cutoffs_by_label[label],
                        kind="recursive" if want_recursive else "base",
                        original_edge=None if want_recursive else target,
                    )
                    next_height = height + value
                    exhaust_selected(
                        child,
                        index + 1,
                        next_height,
                        max(peak, next_height),
                        (*records, record),
                    )

            exhaust_selected(
                base_cycle,
                0,
                Fraction(),
                Fraction(),
                (),
            )

    cycle_count = len(raw_cycles)
    base_sequences = falling_factorial(fixture.q, fixture.ell - 1)
    expected_selected = cycle_count * base_sequences * fixture.ell * (fixture.ell - 1)
    if selected_histories != expected_selected:
        raise AssertionError(
            f"selected count {selected_histories} != {expected_selected}"
        )
    for position in range(1, fixture.ell):
        expected_position_count = cycle_count * base_sequences * 2 * position
        if recursive_positions[position] != expected_position_count:
            raise AssertionError(
                "recursive-position count mismatch at "
                f"{position}: {recursive_positions[position]} "
                f"!= {expected_position_count}"
            )

    completion_count = 1
    current_size = fixture.q + fixture.ell
    for _ in range(fixture.s - 1):
        completion_count *= current_size
        current_size += 1
    expected_complete = expected_selected * completion_count
    if complete_histories != expected_complete:
        raise AssertionError(
            f"complete count {complete_histories} != {expected_complete}"
        )
    if zero_coverage_histories == 0:
        raise AssertionError("fixture has no sharp zero-coverage parent")
    if fixture.s > 1 and two_inserted_completion_histories == 0:
        raise AssertionError("completion never used a two-inserted edge")
    if minimum_residual is None or minimum_optimized_bound is None:
        raise AssertionError("fixture has no complete history")

    print(
        f"{fixture.name}: q={fixture.q} ell={fixture.ell} "
        f"selected={selected_histories} complete={complete_histories} "
        f"positions={dict(sorted(recursive_positions.items()))} "
        f"zero_cov={zero_coverage_histories} "
        f"two_inserted_completion={two_inserted_completion_histories} "
        f"min_residual={minimum_residual} "
        f"min_bound={minimum_optimized_bound}: PASS"
    )
    return FixtureResult(
        selected_histories=selected_histories,
        complete_histories=complete_histories,
        recursive_positions=tuple(sorted(recursive_positions.items())),
        zero_coverage_histories=zero_coverage_histories,
        two_inserted_completion_histories=(two_inserted_completion_histories),
        minimum_residual=minimum_residual,
        minimum_optimized_bound=minimum_optimized_bound,
    )


def main() -> None:
    """Run the broad one-recursive sweep and deep completion fixture."""
    catalogues: dict[int, tuple[Cycle, ...]] = {}
    total_cycles = 0
    for q in range(MIN_Q, MAX_Q + 1):
        cycles = tuple(canonical_cycles(q))
        expected_cycles = factorial(q - 1) // 2
        if len(cycles) != expected_cycles:
            raise AssertionError(
                f"q={q}: got {len(cycles)}, expected {expected_cycles}"
            )
        catalogues[q] = cycles
        total_cycles += len(cycles)
    if total_cycles != 432:
        raise AssertionError(f"unexpected canonical-cycle count {total_cycles}")

    broad_selected = 0
    broad_complete = 0
    broad_zero_coverage = 0
    expected_broad_extrema = {
        (5, 2): (Fraction(67, 3), Fraction(193, 24)),
        (6, 2): (Fraction(28), Fraction(1189, 114)),
        (7, 2): (Fraction(106, 3), Fraction(434, 33)),
        (7, 3): (Fraction(147, 2), Fraction(399, 23)),
    }
    for q in range(MIN_Q, MAX_Q + 1):
        for ell in range(2, (q + 1) // 2):
            result = verify_fixture(
                Fixture(
                    q=q,
                    ell=ell,
                    s=1,
                    cutoffs=(1,),
                    weights=(Fraction(1, 2),),
                    name="broad",
                ),
                catalogues[q],
            )
            broad_selected += result.selected_histories
            broad_complete += result.complete_histories
            broad_zero_coverage += result.zero_coverage_histories
            expected_extrema = expected_broad_extrema[(q, ell)]
            if (
                result.minimum_residual,
                result.minimum_optimized_bound,
            ) != expected_extrema:
                raise AssertionError(
                    f"changed broad extrema for q={q}, ell={ell}: {result}"
                )

    if broad_selected != 96_600 or broad_complete != 96_600:
        raise AssertionError(
            f"unexpected broad totals {broad_selected}, {broad_complete}"
        )
    if broad_zero_coverage != 9_504:
        raise AssertionError(
            f"unexpected broad zero-coverage count {broad_zero_coverage}"
        )

    deep = verify_fixture(
        Fixture(
            q=5,
            ell=2,
            s=3,
            cutoffs=(4, 3),
            weights=(Fraction(3, 4), Fraction(1, 4)),
            name="two-segment-completion",
        ),
        catalogues[5],
    )
    if deep.selected_histories != 120 or deep.complete_histories != 6_720:
        raise AssertionError(f"unexpected deep totals {deep}")
    if (
        deep.zero_coverage_histories != 1_344
        or deep.two_inserted_completion_histories != 1_920
        or deep.minimum_residual != Fraction(1137, 140)
        or deep.minimum_optimized_bound != Fraction(148, 35)
    ):
        raise AssertionError(f"changed deep exact goldens {deep}")

    print(
        "PASS: "
        f"{total_cycles} canonical cycles, "
        f"{broad_selected} broad genuinely recursive histories, plus "
        f"{deep.complete_histories} arbitrary-completion histories; "
        "direct residual, KR1G-6 decomposition, parentage, radical "
        "envelope, optimized bound, uniform bound, and completion DP agree"
    )


if __name__ == "__main__":
    main()
