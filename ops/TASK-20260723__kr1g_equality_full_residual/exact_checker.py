"""Independent exact checker for the full KR1G equality residual.

The checker imports no project, production, test, artifact, or earlier
dossier helper.  For each small fixture it:

* enumerates Hamiltonian base cycles modulo rotation and reversal;
* detects positive-branch equality deletion sets from the literal retained
  slack, without using the KR1G-45 classification predicate;
* tries every assignment of the selected labels to the deleted edges;
* tries every compatible completion below the last cutoff;
* evaluates ``P(C0) + M_h - B`` directly in exact ``Fraction`` arithmetic;
* checks the complete KR1G decomposition and the new finite square bound;
* compares literal completion minima with an independently memoized DP.

The broad sweep uses one rational segment and ``s=2`` for every
``3 <= q <= 10`` and every positive-branch ``ell``.  A separate fixture has
two selected segments and a two-label completion.  These are finite
structural checks, not realizations of the eventual irrational all-middle
rows and not proofs of the all-q or asymptotic statements.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial


Cycle = tuple[int, ...]
Edge = frozenset[int]

MIN_Q = 3
MAX_Q = 10


@dataclass(frozen=True)
class Fixture:
    """One exact finite prefix/completion instance."""

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
    """Insert ``label`` in the oriented edge beginning at ``index``."""
    if index == len(cycle) - 1:
        return (*cycle, label)
    return (*cycle[: index + 1], label, *cycle[index + 1 :])


def split_edge(cycle: Cycle, target: Edge, label: int) -> tuple[Cycle, int, int]:
    """Split one named original edge and return its oriented endpoints."""
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
    """Return the exact score change caused by one split."""
    return label * (u + v) - u * v


def doubled_raw_slacks(cycle: Cycle) -> tuple[int, ...]:
    """Return ``2 Delta`` on the untranslated cycle."""
    target = len(cycle) - 1
    return tuple((u + v - target) ** 2 for u, v in oriented_edges(cycle))


def slack(n: int, r: int, u: int, v: int) -> Fraction:
    """Return the translated original-edge slack."""
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


def selected_parameters(
    fixture: Fixture,
) -> tuple[dict[int, Fraction], dict[int, int], Fraction]:
    """Map selected labels to weights/cutoffs and compute the exact B."""
    if len(fixture.cutoffs) != len(fixture.weights):
        raise AssertionError("cutoff/weight length mismatch")
    if fixture.cutoffs[-1] != fixture.s:
        raise AssertionError("last cutoff is not s")
    if tuple(sorted(fixture.cutoffs, reverse=True)) != fixture.cutoffs:
        raise AssertionError("cutoffs are not strictly descending")
    if tuple(sorted(fixture.weights, reverse=True)) != fixture.weights:
        raise AssertionError("weights are not nonincreasing")
    if not all(Fraction() < weight < 1 for weight in fixture.weights):
        raise AssertionError("weights must lie strictly between zero and one")

    weights_by_label: dict[int, Fraction] = {}
    cutoffs_by_label: dict[int, int] = {}
    upper = fixture.r
    selected_floor = Fraction()
    for cutoff, weight in zip(fixture.cutoffs, fixture.weights):
        if not 1 <= cutoff < upper:
            raise AssertionError("invalid cutoff")
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

    labels = set(range(fixture.s, fixture.r))
    if set(weights_by_label) != labels:
        raise AssertionError("selected labels are not partitioned exactly")
    bound = Fraction(pairing_floor(fixture.n, fixture.r)) + selected_floor
    return weights_by_label, cutoffs_by_label, bound


def equality_catalogue(
    q: int,
) -> tuple[dict[int, tuple[tuple[Cycle, tuple[int, ...]], ...]], int, int]:
    """Find equality pairs from literal retained slack only."""
    c = (q + 1) // 2
    rows: dict[int, list[tuple[Cycle, tuple[int, ...]]]] = {
        ell: [] for ell in range(1, c)
    }
    cycle_count = 0
    deletion_checks = 0

    for cycle in canonical_cycles(q):
        cycle_count += 1
        doubled = doubled_raw_slacks(cycle)
        ordered = sorted(doubled)
        total = sum(doubled)

        for ell in range(1, c):
            target = c - ell
            for smaller in range(ell):
                minimum = sum(ordered[: q - smaller])
                if minimum <= target:
                    raise AssertionError(
                        "literal equality attained with too few deletions"
                    )

            minimum = sum(ordered[: q - ell])
            if minimum < target:
                raise AssertionError("retained slack beat KR1G-24")
            if minimum > target:
                continue

            for deleted in combinations(range(q), ell):
                deletion_checks += 1
                deleted_slack = sum(doubled[index] for index in deleted)
                if total - deleted_slack == target:
                    rows[ell].append((cycle, deleted))

    expected_cycles = factorial(q - 1) // 2
    if cycle_count != expected_cycles:
        raise AssertionError(
            f"q={q}: got {cycle_count} cycles, expected {expected_cycles}"
        )
    return (
        {ell: tuple(pairs) for ell, pairs in rows.items()},
        cycle_count,
        deletion_checks,
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


def verify_fixture(
    fixture: Fixture,
    equality_pairs: tuple[tuple[Cycle, tuple[int, ...]], ...],
) -> tuple[int, int, Fraction]:
    """Evaluate every history represented by one fixture."""
    n = fixture.n
    r = fixture.r
    s = fixture.s
    ell = fixture.ell
    c = (fixture.q + 1) // 2
    weights, cutoffs, bound = selected_parameters(fixture)
    selected_labels = tuple(range(r - 1, s - 1, -1))

    pair_count = 0
    assignment_count = 0
    history_count = 0
    global_minimum: Fraction | None = None

    for raw_cycle, deleted_indices in equality_pairs:
        pair_count += 1
        base_cycle = tuple(r + value for value in raw_cycle)
        base_oriented = oriented_edges(base_cycle)
        base_edges = tuple(edge_key(u, v) for u, v in base_oriented)
        targets = tuple(base_edges[index] for index in deleted_indices)
        if len(set(targets)) != ell:
            raise AssertionError("deleted original edges are not distinct")

        base_score = cycle_score(base_cycle)
        base_slack = sum(
            (slack(n, r, u, v) for u, v in base_oriented),
            Fraction(),
        )
        if Fraction(base_score - pairing_floor(n, r)) != base_slack:
            raise AssertionError("base-slack identity failed")

        all_deviation = sum(u + v - n - r for u, v in base_oriented)
        if all_deviation != 0:
            raise AssertionError("cycle deviations do not sum to zero")

        for assignment in permutations(targets):
            assignment_count += 1
            cycle = base_cycle
            selected_height = Fraction()
            selected_peak = Fraction()
            records: list[tuple[int, int, int, Fraction, int, Edge]] = []

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
                        weights[label],
                        cutoffs[label],
                        target,
                    )
                )

            selected_delta = sum(u + v - n - r for _, u, v, _, _, _ in records)
            if abs(selected_delta) > c - ell:
                raise AssertionError("selected deviation-sum bound failed")

            total_shift = Fraction()
            reciprocal_weight = Fraction()
            for label, _, _, weight, _, _ in records:
                total_shift += weight * (n + r - 2 * label) / (2 - weight)
                reciprocal_weight += 4 / (2 - weight)
            finite_bound = (
                max(total_shift - (c - ell), Fraction()) ** 2 / reciprocal_weight
            )

            dp_excursion = completion_excursion(cycle, s - 1)
            literal_minimum_peak: Fraction | None = None

            def exhaust_completion(
                current: Cycle,
                label: int,
                completion_height: Fraction,
                completion_peak: Fraction,
            ) -> None:
                nonlocal history_count
                nonlocal global_minimum
                nonlocal literal_minimum_peak

                if label == 0:
                    history_count += 1
                    full_peak = max(
                        selected_peak,
                        selected_height + completion_peak,
                    )
                    residual = Fraction(base_score) + full_peak - bound
                    selected_floor = bound - pairing_floor(n, r)
                    if residual != base_slack + full_peak - selected_floor:
                        raise AssertionError("direct residual identity failed")

                    weighted_height = sum(
                        (
                            weight * correction(t, u, v)
                            for t, u, v, weight, _, _ in records
                        ),
                        Fraction(),
                    )
                    height_loss = full_peak - weighted_height
                    unused = sum(
                        (
                            slack(n, r, u, v)
                            for key, (u, v) in zip(base_edges, base_oriented)
                            if key not in targets
                        ),
                        Fraction(),
                    )
                    product_loss = Fraction()
                    square_loss = Fraction()
                    monotonicity_loss = Fraction()
                    for t, u, v, weight, cutoff, _ in records:
                        product_loss += weight * Fraction((u - v) ** 2, 4)
                        delta = Fraction(u + v - n - r)
                        displacement = weight * (n + r - 2 * t) / (2 - weight)
                        square_loss += (2 - weight) * (delta - displacement) ** 2 / 4
                        monotonicity_loss += local_floor(
                            n,
                            r,
                            weight,
                            t,
                        ) - local_floor(n, r, weight, cutoff)

                    decomposition = (
                        height_loss
                        + unused
                        + product_loss
                        + square_loss
                        + monotonicity_loss
                    )
                    if residual != decomposition:
                        raise AssertionError(
                            f"full KR1G decomposition failed: "
                            f"{residual} != {decomposition}"
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
                    if unused != Fraction(c - ell, 2):
                        raise AssertionError("equality unused slack mismatch")
                    if square_loss < finite_bound:
                        raise AssertionError("finite square bound failed")
                    if residual < square_loss:
                        raise AssertionError("full residual below square term")

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
                s - 1,
                Fraction(),
                Fraction(),
            )
            expected_peak = max(
                selected_peak,
                selected_height + dp_excursion,
            )
            if literal_minimum_peak != expected_peak:
                raise AssertionError("literal completions and independent DP disagree")

    if pair_count != len(equality_pairs):
        raise AssertionError("equality-pair count mismatch")
    if global_minimum is None:
        raise AssertionError("fixture has no histories")

    print(
        f"{fixture.name}: q={fixture.q:2d} ell={ell} "
        f"pairs={pair_count:4d} assignments={assignment_count:6d} "
        f"histories={history_count:7d} min_residual={global_minimum}: PASS"
    )
    return assignment_count, history_count, global_minimum


def main() -> None:
    catalogues: dict[int, dict[int, tuple[tuple[Cycle, tuple[int, ...]], ...]]] = {}
    total_cycles = 0
    total_deletion_checks = 0
    total_pairs = 0
    for q in range(MIN_Q, MAX_Q + 1):
        catalogue, cycles, deletion_checks = equality_catalogue(q)
        catalogues[q] = catalogue
        total_cycles += cycles
        total_deletion_checks += deletion_checks
        total_pairs += sum(len(pairs) for pairs in catalogue.values())

    if total_cycles != 204_556:
        raise AssertionError(f"unexpected canonical-cycle count {total_cycles}")
    if total_deletion_checks != 96_887:
        raise AssertionError(
            f"unexpected literal deletion-check count {total_deletion_checks}"
        )
    if total_pairs != 1_066:
        raise AssertionError(f"unexpected equality-pair count {total_pairs}")

    sweep_assignments = 0
    sweep_histories = 0
    q10_minima: dict[int, Fraction] = {}
    for q in range(MIN_Q, MAX_Q + 1):
        c = (q + 1) // 2
        for ell in range(1, c):
            fixture = Fixture(
                q=q,
                ell=ell,
                s=2,
                cutoffs=(2,),
                weights=(Fraction(1, 2),),
                name="single",
            )
            assignments, histories, minimum = verify_fixture(
                fixture,
                catalogues[q][ell],
            )
            sweep_assignments += assignments
            sweep_histories += histories
            if q == 10:
                q10_minima[ell] = minimum

    expected_q10 = {
        1: Fraction(169, 6),
        2: Fraction(181, 3),
        3: Fraction(227, 2),
        4: Fraction(575, 3),
    }
    if q10_minima != expected_q10:
        raise AssertionError(
            f"q=10 golden minima changed: {q10_minima} != {expected_q10}"
        )
    if sweep_assignments != 17_188:
        raise AssertionError(f"unexpected sweep-assignment count {sweep_assignments}")
    if sweep_histories != 230_252:
        raise AssertionError(f"unexpected sweep-history count {sweep_histories}")

    deep = Fixture(
        q=7,
        ell=3,
        s=3,
        cutoffs=(5, 3),
        weights=(Fraction(3, 4), Fraction(1, 4)),
        name="two-segment",
    )
    deep_assignments, deep_histories, _ = verify_fixture(
        deep,
        catalogues[deep.q][deep.ell],
    )
    if deep_assignments != 192:
        raise AssertionError(f"unexpected deep-assignment count {deep_assignments}")
    if deep_histories != 21_120:
        raise AssertionError(f"unexpected deep-history count {deep_histories}")

    print(
        f"PASS: {total_cycles} canonical cycles, "
        f"{total_deletion_checks} literal deletion checks, "
        f"{total_pairs} equality pairs; sweep assignments="
        f"{sweep_assignments}, sweep histories={sweep_histories}; "
        f"deep assignments={deep_assignments}, "
        f"deep histories={deep_histories}; full residual, complete "
        "decomposition, square bound, and completion DP all exact"
    )


if __name__ == "__main__":
    main()
