"""Independent exact checker for the distinct-original-edge KR1G residual.

The checker imports no project, production, test, artifact, or earlier
dossier helper.  It uses only standard-library ``Fraction`` arithmetic.

The broad sweep enumerates every Hamiltonian base cycle modulo rotation and
reversal, every target subset in the eventual all-middle domain
``1 <= ell < ceil(q / 2)``, and every assignment of the selected labels for
``3 <= q <= 8``.  It applies no KR1G-24 equality filter.  A separate
two-segment fixture exhausts every compatible two-label completion.

For every resulting history the checker evaluates the complete residual
directly and verifies:

* the base-slack identity and the full KR1G-6 decomposition;
* the exact selected/unused deviation identity;
* ``(sum delta)**2 <= 2*m*U``;
* weighted Cauchy for the selected square-center terms;
* the bound containing ``sqrt(2*m*U)`` by an exact quadratic-surd sign test;
* the optimized rational bound ``T**2 / (Q + 2*m)``;
* the direct combined-Cauchy version of the optimized bound.

These bounded synthetic rational fixtures corroborate the finite algebra.
They are not rounded instances of the irrational all-middle tuple and do
not prove the all-q or asymptotic theorem.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial


Cycle = tuple[int, ...]
Edge = frozenset[int]
Record = tuple[int, int, int, Fraction, int, Edge]

MIN_Q = 3
MAX_Q = 8


@dataclass(frozen=True)
class Fixture:
    """One exact finite selected-prefix/completion instance."""

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
    """History-independent quantities for one fixture."""

    weights_by_label: dict[int, Fraction]
    cutoffs_by_label: dict[int, int]
    bound: Fraction
    total_shift: Fraction
    reciprocal_weight: Fraction


@dataclass(frozen=True)
class FixtureResult:
    """Exact enumeration counts and minimum residual for one fixture."""

    pairs: int
    assignments: int
    histories: int
    equality_histories: int
    nonequality_histories: int
    minimum_residual: Fraction


def canonical_cycles(q: int):
    """Yield cycles on ``range(q)`` once modulo rotation and reversal."""
    for tail in permutations(range(1, q)):
        if tail[0] < tail[-1]:
            yield (0, *tail)


def oriented_edges(cycle: Cycle) -> tuple[tuple[int, int], ...]:
    """Return cyclic oriented edges in tuple order."""
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


def split_edge(cycle: Cycle, target: Edge, label: int) -> tuple[Cycle, int, int]:
    """Split one named edge and return its oriented endpoints."""
    matches = [
        (index, u, v)
        for index, (u, v) in enumerate(oriented_edges(cycle))
        if edge_key(u, v) == target
    ]
    if len(matches) != 1:
        raise AssertionError(f"edge {sorted(target)} occurs {len(matches)} times")
    index, u, v = matches[0]
    return split_at(cycle, index, label), u, v


def cycle_score(cycle: Cycle) -> int:
    """Return the cyclic product score."""
    return sum(u * v for u, v in oriented_edges(cycle))


def correction(label: int, u: int, v: int) -> int:
    """Return the exact product-score change caused by one split."""
    return label * (u + v) - u * v


def slack(n: int, r: int, u: int, v: int) -> Fraction:
    """Return one translated original-edge slack."""
    return Fraction((u + v - n - r) ** 2, 2)


def pairing_floor(n: int, r: int) -> int:
    """Return ``P_{r,n}`` independently from a closed polynomial."""
    return sum(label * (n + r - label) for label in range(r, n + 1))


def local_floor(
    n: int,
    r: int,
    weight: Fraction,
    label: int,
) -> Fraction:
    """Return ``G_{n,weight}(label)`` from its defining formula."""
    total = n + r
    return (
        weight
        * (4 * total * label - total**2 - 2 * weight * label**2)
        / (2 * (2 - weight))
    )


def selected_parameters(fixture: Fixture) -> Parameters:
    """Build exact segment maps and the history-independent ``B,T,Q``."""
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
    """Decide ``a + b*sqrt(x) >= 0`` exactly for rational ``a,b,x``."""
    if radicand < 0:
        raise AssertionError("negative radicand")
    if sqrt_coefficient == 0 or radicand == 0:
        return rational_part >= 0
    squared_term = sqrt_coefficient**2 * radicand
    if sqrt_coefficient > 0:
        return rational_part >= 0 or squared_term >= rational_part**2
    return rational_part >= 0 and rational_part**2 >= squared_term


def check_radical_chain(
    residual: Fraction,
    unused: Fraction,
    total_shift: Fraction,
    reciprocal_weight: Fraction,
    m: int,
) -> None:
    """Check the radical envelope and its optimized bound exactly."""
    radicand = 2 * m * unused
    optimized = total_shift**2 / (reciprocal_weight + 2 * m)

    if radicand >= total_shift**2:
        if residual < unused:
            raise AssertionError("inactive radical-chain bound failed")
        if unused < optimized:
            raise AssertionError("inactive scalar optimization failed")
    else:
        residual_difference = (
            residual - unused - (total_shift**2 + radicand) / reciprocal_weight
        )
        radical_coefficient = 2 * total_shift / reciprocal_weight
        if not surd_nonnegative(
            residual_difference,
            radical_coefficient,
            radicand,
        ):
            raise AssertionError("active radical-chain bound failed")

        envelope_difference = (
            unused + (total_shift**2 + radicand) / reciprocal_weight - optimized
        )
        if not surd_nonnegative(
            envelope_difference,
            -radical_coefficient,
            radicand,
        ):
            raise AssertionError("active scalar optimization failed")

    if residual < optimized:
        raise AssertionError("optimized finite bound failed")


def check_complete_history(
    fixture: Fixture,
    parameters: Parameters,
    base_cycle: Cycle,
    targets: tuple[Edge, ...],
    records: tuple[Record, ...],
    selected_height: Fraction,
    selected_peak: Fraction,
    completion_peak: Fraction,
) -> Fraction:
    """Evaluate and verify one literal complete history."""
    n = fixture.n
    r = fixture.r
    m = fixture.q - fixture.ell
    base_oriented = oriented_edges(base_cycle)
    base_edges = tuple(edge_key(u, v) for u, v in base_oriented)
    base_score = cycle_score(base_cycle)
    base_slack = sum(
        (slack(n, r, u, v) for u, v in base_oriented),
        Fraction(),
    )
    if Fraction(base_score - pairing_floor(n, r)) != base_slack:
        raise AssertionError("base-slack identity failed")

    target_set = set(targets)
    unused_records = tuple(
        (u, v)
        for key, (u, v) in zip(base_edges, base_oriented)
        if key not in target_set
    )
    if len(unused_records) != m:
        raise AssertionError("wrong unused-original-edge count")
    unused = sum(
        (slack(n, r, u, v) for u, v in unused_records),
        Fraction(),
    )

    selected_delta = sum(u + v - n - r for _, u, v, _, _, _ in records)
    unused_delta = sum(u + v - n - r for u, v in unused_records)
    if selected_delta != -unused_delta:
        raise AssertionError("selected/unused deviation identity failed")
    if selected_delta**2 > 2 * m * unused:
        raise AssertionError("deviation Cauchy bound failed")

    full_peak = max(selected_peak, selected_height + completion_peak)
    residual = Fraction(base_score) + full_peak - parameters.bound

    weighted_height = sum(
        (weight * correction(label, u, v) for label, u, v, weight, _, _ in records),
        Fraction(),
    )
    height_loss = full_peak - weighted_height
    product_loss = Fraction()
    square_loss = Fraction()
    monotonicity_loss = Fraction()
    selected_center_sum = Fraction()
    for label, u, v, weight, cutoff, _ in records:
        product_loss += weight * Fraction((u - v) ** 2, 4)
        delta = Fraction(u + v - n - r)
        displacement = weight * (n + r - 2 * label) / (2 - weight)
        square_loss += (2 - weight) * (delta - displacement) ** 2 / 4
        monotonicity_loss += local_floor(
            n,
            r,
            weight,
            label,
        ) - local_floor(n, r, weight, cutoff)
        selected_center_sum += displacement - delta

    decomposition = (
        height_loss + unused + product_loss + square_loss + monotonicity_loss
    )
    if residual != decomposition:
        raise AssertionError(
            f"full KR1G decomposition failed: {residual} != {decomposition}"
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

    total_shift = parameters.total_shift
    reciprocal_weight = parameters.reciprocal_weight
    if selected_center_sum != total_shift - selected_delta:
        raise AssertionError("selected square-center sum failed")
    if square_loss * reciprocal_weight < selected_center_sum**2:
        raise AssertionError("selected weighted Cauchy failed")

    combined_linear_sum = selected_center_sum - unused_delta
    if combined_linear_sum != total_shift:
        raise AssertionError("combined-Cauchy linear identity failed")
    optimized = total_shift**2 / (reciprocal_weight + 2 * m)
    if unused + square_loss < optimized:
        raise AssertionError("direct combined-Cauchy bound failed")
    if residual < unused + square_loss:
        raise AssertionError("residual below retained energy")

    check_radical_chain(
        residual,
        unused,
        total_shift,
        reciprocal_weight,
        m,
    )
    return residual


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


def verify_fixture(
    fixture: Fixture,
    raw_cycles: tuple[Cycle, ...],
) -> FixtureResult:
    """Enumerate and verify every history represented by one fixture."""
    if not 1 <= fixture.ell < (fixture.q + 1) // 2:
        raise AssertionError("fixture is outside the positive branch")
    parameters = selected_parameters(fixture)
    selected_labels = tuple(range(fixture.r - 1, fixture.s - 1, -1))
    relaxed_minimum = Fraction((fixture.q + 1) // 2 - fixture.ell, 2)

    pair_count = 0
    assignment_count = 0
    history_count = 0
    equality_histories = 0
    nonequality_histories = 0
    global_minimum: Fraction | None = None

    for raw_cycle in raw_cycles:
        base_cycle = tuple(fixture.r + value for value in raw_cycle)
        base_oriented = oriented_edges(base_cycle)
        base_edges = tuple(edge_key(u, v) for u, v in base_oriented)

        for used_indices in combinations(range(fixture.q), fixture.ell):
            pair_count += 1
            targets = tuple(base_edges[index] for index in used_indices)
            if len(set(targets)) != fixture.ell:
                raise AssertionError("selected original edges are not distinct")

            target_set = set(targets)
            unused = sum(
                (
                    slack(fixture.n, fixture.r, u, v)
                    for key, (u, v) in zip(base_edges, base_oriented)
                    if key not in target_set
                ),
                Fraction(),
            )
            if unused < relaxed_minimum:
                raise AssertionError("literal unused slack beat KR1G-24")
            is_equality = unused == relaxed_minimum

            for assignment in permutations(targets):
                assignment_count += 1
                cycle = base_cycle
                selected_height = Fraction()
                selected_peak = Fraction()
                records: list[Record] = []

                for label, target in zip(selected_labels, assignment):
                    parent = cycle
                    cycle, u, v = split_edge(cycle, target, label)
                    value = Fraction(correction(label, u, v))
                    if cycle_score(cycle) - cycle_score(parent) != value:
                        raise AssertionError("selected score correction failed")
                    selected_height += value
                    selected_peak = max(selected_peak, selected_height)
                    records.append(
                        (
                            label,
                            u,
                            v,
                            parameters.weights_by_label[label],
                            parameters.cutoffs_by_label[label],
                            target,
                        )
                    )

                literal_minimum_peak: Fraction | None = None

                def exhaust_completion(
                    current: Cycle,
                    label: int,
                    completion_height: Fraction,
                    completion_peak: Fraction,
                ) -> None:
                    nonlocal equality_histories
                    nonlocal global_minimum
                    nonlocal history_count
                    nonlocal literal_minimum_peak
                    nonlocal nonequality_histories

                    if label == 0:
                        history_count += 1
                        if is_equality:
                            equality_histories += 1
                        else:
                            nonequality_histories += 1
                        residual = check_complete_history(
                            fixture,
                            parameters,
                            base_cycle,
                            targets,
                            tuple(records),
                            selected_height,
                            selected_peak,
                            completion_peak,
                        )
                        full_peak = max(
                            selected_peak,
                            selected_height + completion_peak,
                        )
                        literal_minimum_peak = (
                            full_peak
                            if literal_minimum_peak is None
                            else min(literal_minimum_peak, full_peak)
                        )
                        global_minimum = (
                            residual
                            if global_minimum is None
                            else min(global_minimum, residual)
                        )
                        return

                    for index, (u, v) in enumerate(oriented_edges(current)):
                        child = split_at(current, index, label)
                        value = Fraction(correction(label, u, v))
                        if cycle_score(child) - cycle_score(current) != value:
                            raise AssertionError("completion score correction failed")
                        next_height = completion_height + value
                        exhaust_completion(
                            child,
                            label - 1,
                            next_height,
                            max(completion_peak, next_height),
                        )

                exhaust_completion(
                    cycle,
                    fixture.s - 1,
                    Fraction(),
                    Fraction(),
                )
                if fixture.s == 1:
                    expected_peak = selected_peak
                else:
                    expected_peak = max(
                        selected_peak,
                        selected_height + completion_excursion(cycle, fixture.s - 1),
                    )
                if literal_minimum_peak != expected_peak:
                    raise AssertionError(
                        "literal completions and independent DP disagree"
                    )

    expected_pairs = len(raw_cycles) * comb(fixture.q, fixture.ell)
    expected_assignments = expected_pairs * factorial(fixture.ell)
    completion_count = 1
    current_size = fixture.q + fixture.ell
    for _ in range(fixture.s - 1):
        completion_count *= current_size
        current_size += 1
    expected_histories = expected_assignments * completion_count
    if pair_count != expected_pairs:
        raise AssertionError("target-pair count mismatch")
    if assignment_count != expected_assignments:
        raise AssertionError("assignment count mismatch")
    if history_count != expected_histories:
        raise AssertionError("history count mismatch")
    if equality_histories + nonequality_histories != history_count:
        raise AssertionError("equality partition count mismatch")
    if nonequality_histories == 0:
        raise AssertionError("fixture contains no nonequality history")
    if global_minimum is None:
        raise AssertionError("fixture contains no histories")

    print(
        f"{fixture.name}: q={fixture.q} ell={fixture.ell} "
        f"pairs={pair_count} assignments={assignment_count} "
        f"histories={history_count} equality={equality_histories} "
        f"nonequality={nonequality_histories} "
        f"min_residual={global_minimum}: PASS"
    )
    return FixtureResult(
        pairs=pair_count,
        assignments=assignment_count,
        histories=history_count,
        equality_histories=equality_histories,
        nonequality_histories=nonequality_histories,
        minimum_residual=global_minimum,
    )


def verify_explicit_nonequality_goldens() -> None:
    """Check two named nonequality histories, including an active radical."""
    single = Fixture(
        q=3,
        ell=1,
        s=2,
        cutoffs=(2,),
        weights=(Fraction(1, 2),),
        name="golden-inactive",
    )
    single_parameters = selected_parameters(single)
    single_base = (3, 4, 5)
    single_cycle, u, v = split_edge(single_base, edge_key(3, 5), 2)
    single_record: Record = (
        2,
        u,
        v,
        Fraction(1, 2),
        2,
        edge_key(3, 5),
    )
    single_selected_height = Fraction(correction(2, u, v))
    single_selected_peak = max(Fraction(), single_selected_height)
    _, u, v = split_edge(single_cycle, edge_key(2, 3), 1)
    single_completion = Fraction(correction(1, u, v))
    single_completion_peak = max(Fraction(), single_completion)
    single_residual = check_complete_history(
        single,
        single_parameters,
        single_base,
        (edge_key(3, 5),),
        (single_record,),
        single_selected_height,
        single_selected_peak,
        single_completion_peak,
    )
    single_optimized = single_parameters.total_shift**2 / (
        single_parameters.reciprocal_weight + 2 * (single.q - single.ell)
    )
    single_unused = sum(
        (
            slack(single.n, single.r, u, v)
            for u, v in oriented_edges(single_base)
            if edge_key(u, v) != edge_key(3, 5)
        ),
        Fraction(),
    )
    if (
        single_residual != Fraction(8, 3)
        or single_unused != 1
        or single_parameters.total_shift != Fraction(4, 3)
        or single_parameters.reciprocal_weight != Fraction(8, 3)
        or single_optimized != Fraction(4, 15)
    ):
        raise AssertionError("inactive nonequality golden changed")

    deep = Fixture(
        q=5,
        ell=2,
        s=3,
        cutoffs=(4, 3),
        weights=(Fraction(3, 4), Fraction(1, 4)),
        name="golden-active",
    )
    deep_parameters = selected_parameters(deep)
    deep_base = (5, 8, 6, 7, 9)
    deep_targets = (edge_key(7, 9), edge_key(6, 8))
    deep_cycle = deep_base
    deep_height = Fraction()
    deep_peak = Fraction()
    deep_records: list[Record] = []
    for label, target in zip((4, 3), deep_targets):
        deep_cycle, u, v = split_edge(deep_cycle, target, label)
        value = Fraction(correction(label, u, v))
        deep_height += value
        deep_peak = max(deep_peak, deep_height)
        deep_records.append(
            (
                label,
                u,
                v,
                deep_parameters.weights_by_label[label],
                deep_parameters.cutoffs_by_label[label],
                target,
            )
        )

    completion_height = Fraction()
    completion_peak = Fraction()
    for label, target in ((2, edge_key(5, 8)), (1, edge_key(5, 2))):
        deep_cycle, u, v = split_edge(deep_cycle, target, label)
        completion_height += Fraction(correction(label, u, v))
        completion_peak = max(completion_peak, completion_height)

    deep_residual = check_complete_history(
        deep,
        deep_parameters,
        deep_base,
        deep_targets,
        tuple(deep_records),
        deep_height,
        deep_peak,
        completion_peak,
    )
    deep_optimized = deep_parameters.total_shift**2 / (
        deep_parameters.reciprocal_weight + 2 * (deep.q - deep.ell)
    )
    deep_target_set = set(deep_targets)
    deep_unused = sum(
        (
            slack(deep.n, deep.r, u, v)
            for u, v in oriented_edges(deep_base)
            if edge_key(u, v) not in deep_target_set
        ),
        Fraction(),
    )
    deep_selected_delta = sum(
        u + v - deep.n - deep.r for _, u, v, _, _, _ in deep_records
    )
    if (
        deep_residual != Fraction(717, 140)
        or deep_unused != 1
        or deep_selected_delta != 2
        or 2 * (deep.q - deep.ell) * deep_unused >= deep_parameters.total_shift**2
        or deep_parameters.total_shift != Fraction(166, 35)
        or deep_parameters.reciprocal_weight != Fraction(192, 35)
        or deep_optimized != Fraction(13778, 7035)
    ):
        raise AssertionError("active nonequality golden changed")

    print(
        "named nonequality goldens: "
        "inactive residual=8/3 bound=4/15; "
        "active residual=717/140 bound=13778/7035: PASS"
    )


def main() -> None:
    """Run the broad exact sweep, deep completion fixture, and goldens."""
    catalogues: dict[int, tuple[Cycle, ...]] = {}
    total_cycles = 0
    for q in range(MIN_Q, MAX_Q + 1):
        cycles = tuple(canonical_cycles(q))
        expected_cycles = factorial(q - 1) // 2
        if len(cycles) != expected_cycles:
            raise AssertionError(
                f"q={q}: got {len(cycles)} cycles, expected {expected_cycles}"
            )
        catalogues[q] = cycles
        total_cycles += len(cycles)
    if total_cycles != 2_956:
        raise AssertionError(f"unexpected canonical-cycle count {total_cycles}")

    broad_pairs = 0
    broad_assignments = 0
    broad_histories = 0
    broad_equality_histories = 0
    broad_nonequality_histories = 0
    for q in range(MIN_Q, MAX_Q + 1):
        for ell in range(1, (q + 1) // 2):
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
            broad_pairs += result.pairs
            broad_assignments += result.assignments
            broad_histories += result.histories
            broad_equality_histories += result.equality_histories
            broad_nonequality_histories += result.nonequality_histories

    if broad_pairs != 255_975:
        raise AssertionError(f"unexpected broad pair count {broad_pairs}")
    if broad_assignments != 1_103_715 or broad_histories != 1_103_715:
        raise AssertionError(
            "unexpected broad assignment/history counts: "
            f"{broad_assignments}, {broad_histories}"
        )
    if broad_equality_histories != 580:
        raise AssertionError(
            f"unexpected broad equality count {broad_equality_histories}"
        )
    if broad_nonequality_histories != 1_103_135:
        raise AssertionError(
            f"unexpected broad nonequality count {broad_nonequality_histories}"
        )

    deep = verify_fixture(
        Fixture(
            q=5,
            ell=2,
            s=3,
            cutoffs=(4, 3),
            weights=(Fraction(3, 4), Fraction(1, 4)),
            name="two-segment",
        ),
        catalogues[5],
    )
    if (
        deep.pairs != 120
        or deep.assignments != 240
        or deep.histories != 13_440
        or deep.equality_histories != 672
        or deep.nonequality_histories != 12_768
    ):
        raise AssertionError(f"unexpected deep counts {deep}")

    verify_explicit_nonequality_goldens()
    print(
        "PASS: "
        f"{total_cycles} canonical cycles, {broad_pairs} broad target pairs, "
        f"{broad_histories} broad histories "
        f"({broad_nonequality_histories} nonequality), plus "
        f"{deep.histories} two-segment completion histories "
        f"({deep.nonequality_histories} nonequality); "
        "full residual, exact radical chain, optimized bound, combined "
        "Cauchy, and completion DP all pass"
    )


if __name__ == "__main__":
    main()
