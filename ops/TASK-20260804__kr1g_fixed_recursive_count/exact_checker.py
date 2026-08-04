"""Independent exact checker for the fixed-recursive-count KR1G extension.

This file imports no project module and no earlier dossier helper.  It uses
only standard-library :class:`fractions.Fraction` arithmetic and a fresh edge
lineage representation.

The completion fixture has ``q=7``, ``ell=3``, ``p=2``, ``s=2`` and two
rational selected segments.  It enumerates all 360 Hamiltonian base cycles
modulo rotation and reversal, all 181,440 three-insertion selected histories,
the 15,120 histories with exactly two recursive selected splits, and all
151,200 compatible completions below ``s``.  A second ``q=4``, ``ell=4``,
``p=2``, ``s=1`` position sweep has two distinct original base targets and
exhausts all placements of the two recursive coordinates.  Together the
fixtures include sibling recursive targets, nested targets, different-root
targets, selected targets with two inserted endpoints, and completion targets
with two inserted endpoints.

For every retained selected history the checker independently verifies the
local base and recursive identities, the full generalized KR1G-6
decomposition, nonnegativity, the original-edge deviation partition, removal
of the two recursive ``T`` and ``Q`` coordinates, the radical and combined
Cauchy bounds, and the finite uniform ``[T-pD]_+`` bound.  Literal completion
enumeration is also compared with a separately memoized Bellman recursion.
The rational fixture checks the finite algebra and topology; it is not a
rounded instance of the irrational all-middle tuple and is not an asymptotic
proof.
"""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial


EdgeKey = tuple[int, int]
PlainEdge = tuple[int, int]
PlainState = tuple[PlainEdge, ...]


@dataclass(frozen=True)
class EdgeState:
    """One oriented current edge and its literal original-edge lineage."""

    u: int
    v: int
    root: EdgeKey
    ancestry: tuple[int, ...]


State = tuple[EdgeState, ...]


@dataclass(frozen=True)
class Fixture:
    """One finite selected-window fixture."""

    q: int
    ell: int
    p: int
    s: int
    cutoffs: tuple[int, ...]
    weights: tuple[Fraction, ...]

    @property
    def r(self) -> int:
        return self.s + self.ell

    @property
    def n(self) -> int:
        return self.r + self.q - 1


@dataclass(frozen=True)
class Parameters:
    """History-independent exact quantities for a fixture."""

    weights_by_label: dict[int, Fraction]
    cutoffs_by_label: dict[int, int]
    bound: Fraction
    total_shift: Fraction
    reciprocal_weight: Fraction


@dataclass(frozen=True)
class Record:
    """One selected insertion record."""

    label: int
    edge: EdgeState
    weight: Fraction
    cutoff: int
    kind: str


@dataclass(frozen=True)
class SelectedAudit:
    """Completion-independent exact audit data for one selected history."""

    base_score: int
    weighted_height: Fraction
    static_decomposition: Fraction
    optimized_bound: Fraction
    uniform_bound: Fraction
    recursive_loss: Fraction
    zero_coverage_count: int


FIXTURE = Fixture(
    q=7,
    ell=3,
    p=2,
    s=2,
    cutoffs=(3, 2),
    weights=(Fraction(3, 4), Fraction(1, 4)),
)

POSITION_FIXTURE = Fixture(
    q=4,
    ell=4,
    p=2,
    s=1,
    cutoffs=(1,),
    weights=(Fraction(1, 2),),
)


def edge_key(u: int, v: int) -> EdgeKey:
    """Return a stable unordered two-endpoint key."""
    return (u, v) if u < v else (v, u)


def canonical_vertex_cycles(q: int):
    """Yield vertex cycles on ``range(q)`` modulo rotation and reversal."""
    for tail in permutations(range(1, q)):
        if tail[0] < tail[-1]:
            yield (0, *tail)


def initial_state(vertices: tuple[int, ...]) -> State:
    """Build a lineage-bearing oriented edge state from one vertex cycle."""
    result = []
    for index, u in enumerate(vertices):
        v = vertices[(index + 1) % len(vertices)]
        result.append(EdgeState(u, v, edge_key(u, v), ()))
    return tuple(result)


def split_state(state: State, index: int, label: int) -> State:
    """Split one oriented edge while preserving its original root."""
    edge = state[index]
    ancestry = (*edge.ancestry, label)
    children = (
        EdgeState(edge.u, label, edge.root, ancestry),
        EdgeState(label, edge.v, edge.root, ancestry),
    )
    return (*state[:index], *children, *state[index + 1 :])


def plain_state(state: State) -> PlainState:
    """Discard lineage metadata for the independent completion recursion."""
    return tuple((edge.u, edge.v) for edge in state)


def split_plain(state: PlainState, index: int, label: int) -> PlainState:
    """Split one plain oriented edge."""
    u, v = state[index]
    return (*state[:index], (u, label), (label, v), *state[index + 1 :])


def correction(label: int, u: int, v: int) -> int:
    """Return the exact adjacent-product change of one insertion."""
    return label * (u + v) - u * v


def state_score(state: State) -> int:
    """Return the cyclic adjacent-product score from the oriented edges."""
    return sum(edge.u * edge.v for edge in state)


def pairing_floor(n: int, r: int) -> int:
    """Evaluate the complementary-pairing floor directly."""
    return sum(label * (n + r - label) for label in range(r, n + 1))


def original_slack(n: int, r: int, u: int, v: int) -> Fraction:
    """Return the quadratic slack assigned to one original edge."""
    return Fraction((u + v - n - r) ** 2, 2)


def local_floor(
    n: int,
    r: int,
    weight: Fraction,
    label: int,
) -> Fraction:
    """Evaluate ``G_{n,weight}(label)`` from its defining polynomial."""
    total = n + r
    numerator = weight * (4 * total * label - total**2 - 2 * weight * label**2)
    return numerator / (2 * (2 - weight))


def recursive_floor(
    n: int,
    r: int,
    weight: Fraction,
    label: int,
) -> Fraction:
    """Evaluate ``J_{n,weight}(label)`` directly."""
    return weight * ((n + r - 1) * label - n * (r - 1))


def displacement(
    n: int,
    r: int,
    label: int,
    weight: Fraction,
) -> Fraction:
    """Return the positive square-center displacement ``d_label``."""
    return weight * (n + r - 2 * label) / (2 - weight)


def build_parameters(fixture: Fixture) -> Parameters:
    """Construct the exact segment maps and the finite ``B,T,Q`` data."""
    if len(fixture.cutoffs) != len(fixture.weights):
        raise AssertionError("cutoff/weight length mismatch")
    if not fixture.cutoffs or fixture.cutoffs[-1] != fixture.s:
        raise AssertionError("last cutoff is not s")
    if tuple(sorted(fixture.weights, reverse=True)) != fixture.weights:
        raise AssertionError("weights are not nonincreasing")
    if not all(Fraction() < weight < 1 for weight in fixture.weights):
        raise AssertionError("weights are outside (0,1)")

    weights_by_label: dict[int, Fraction] = {}
    cutoffs_by_label: dict[int, int] = {}
    selected_floor = Fraction()
    upper = fixture.r
    for cutoff, weight in zip(fixture.cutoffs, fixture.weights):
        if not fixture.s <= cutoff < upper:
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

    total_shift = sum(
        (
            displacement(
                fixture.n,
                fixture.r,
                label,
                weights_by_label[label],
            )
            for label in selected_labels
        ),
        Fraction(),
    )
    reciprocal_weight = sum(
        (Fraction(4, 1) / (2 - weights_by_label[label]) for label in selected_labels),
        Fraction(),
    )
    bound = Fraction(pairing_floor(fixture.n, fixture.r)) + selected_floor

    return Parameters(
        weights_by_label=weights_by_label,
        cutoffs_by_label=cutoffs_by_label,
        bound=bound,
        total_shift=total_shift,
        reciprocal_weight=reciprocal_weight,
    )


@lru_cache(maxsize=None)
def topology_factor(length: int, recursive_count: int) -> int:
    """Return the exact selected-prefix topology factor ``S[length,p]``."""
    if length == 0:
        return int(recursive_count == 0)
    if recursive_count < 0 or recursive_count >= length:
        return 0
    return topology_factor(length - 1, recursive_count) + (
        2 * length - recursive_count - 1
    ) * topology_factor(length - 1, recursive_count - 1)


def falling_factorial(value: int, length: int) -> int:
    """Return a falling factorial with ``length`` factors."""
    return factorial(value) // factorial(value - length)


def rising_factorial(value: int, length: int) -> int:
    """Return a rising factorial with ``length`` factors."""
    result = 1
    for offset in range(length):
        result *= value + offset
    return result


@lru_cache(maxsize=None)
def completion_excursion(state: PlainState, label: int) -> Fraction:
    """Return the least future positive excursion by Bellman recursion."""
    if label == 0:
        return Fraction()
    candidates = []
    for index, (u, v) in enumerate(state):
        child = split_plain(state, index, label)
        candidates.append(
            max(
                Fraction(),
                Fraction(correction(label, u, v))
                + completion_excursion(child, label - 1),
            )
        )
    return min(candidates)


def surd_nonnegative(
    rational_part: Fraction,
    radical_coefficient: Fraction,
    radicand: Fraction,
) -> bool:
    """Decide ``a + b*sqrt(x) >= 0`` using exact rational comparisons."""
    if radicand < 0:
        raise AssertionError("negative radicand")
    if radical_coefficient == 0 or radicand == 0:
        return rational_part >= 0
    squared_radical = radical_coefficient**2 * radicand
    if radical_coefficient > 0:
        return rational_part >= 0 or squared_radical >= rational_part**2
    return rational_part >= 0 and rational_part**2 >= squared_radical


def check_radical_bound(
    retained_energy: Fraction,
    unused: Fraction,
    shift: Fraction,
    reciprocal_weight: Fraction,
    unused_count: int,
) -> None:
    """Check the radical envelope and its rational Cauchy consequence."""
    radicand = 2 * unused_count * unused
    rational_bound = shift**2 / (reciprocal_weight + 2 * unused_count)

    if radicand >= shift**2:
        if retained_energy < unused:
            raise AssertionError("inactive radical envelope failed")
        if unused < rational_bound:
            raise AssertionError("inactive rational consequence failed")
    else:
        envelope_gap_rational = (
            retained_energy - unused - (shift**2 + radicand) / reciprocal_weight
        )
        envelope_gap_radical = 2 * shift / reciprocal_weight
        if not surd_nonnegative(
            envelope_gap_rational,
            envelope_gap_radical,
            radicand,
        ):
            raise AssertionError("active radical envelope failed")

        scalar_gap_rational = (
            unused + (shift**2 + radicand) / reciprocal_weight - rational_bound
        )
        if not surd_nonnegative(
            scalar_gap_rational,
            -envelope_gap_radical,
            radicand,
        ):
            raise AssertionError("active rational consequence failed")

    if retained_energy < rational_bound:
        raise AssertionError("combined-Cauchy rational bound failed")


def classify_recursive_relation(
    records: tuple[Record, ...],
    fixture: Fixture,
) -> tuple[str, bool]:
    """Classify the second recursive target and its endpoint type."""
    recursive = tuple(record for record in records if record.kind == "R")
    if len(recursive) != 2:
        raise AssertionError("topology classifier did not receive p=2")
    first, second = recursive
    two_inserted = second.edge.u < fixture.r and second.edge.v < fixture.r
    if first.edge.root != second.edge.root:
        return "different_root", two_inserted
    if first.label in second.edge.ancestry:
        return "nested", two_inserted
    return "sibling", two_inserted


def classify_completion_topology(
    records: tuple[Record, ...],
    fixture: Fixture,
) -> str:
    """Refine the one-base completion fixture into its three topologies."""
    relation, two_inserted = classify_recursive_relation(records, fixture)
    if relation == "different_root":
        raise AssertionError("single-base fixture changed original root")
    if relation == "sibling":
        return relation
    return "nested_two_inserted" if two_inserted else "nested_outer"


def check_selected_history(
    fixture: Fixture,
    parameters: Parameters,
    base_state: State,
    records: tuple[Record, ...],
) -> SelectedAudit:
    """Audit all completion-independent identities and lower bounds."""
    n = fixture.n
    r = fixture.r
    total = n + r
    base_score = state_score(base_state)
    pairing = pairing_floor(n, r)
    base_slack = sum(
        (original_slack(n, r, edge.u, edge.v) for edge in base_state),
        Fraction(),
    )
    if Fraction(base_score - pairing) != base_slack:
        raise AssertionError("base score/slack identity failed")

    base_records = tuple(record for record in records if record.kind == "B")
    recursive_records = tuple(record for record in records if record.kind == "R")
    if len(base_records) != fixture.ell - fixture.p:
        raise AssertionError("wrong base-record count")
    if len(recursive_records) != fixture.p:
        raise AssertionError("wrong recursive-record count")
    if records[0].kind != "B":
        raise AssertionError("first selected insertion was recursive")

    base_roots = tuple(record.edge.root for record in base_records)
    if len(set(base_roots)) != len(base_roots):
        raise AssertionError("base targets are not distinct")
    unused_edges = tuple(
        edge for edge in base_state if edge.root not in set(base_roots)
    )
    unused_count = fixture.q - fixture.ell + fixture.p
    if len(unused_edges) != unused_count:
        raise AssertionError("m_p does not equal the unused-edge count")
    unused = sum(
        (original_slack(n, r, edge.u, edge.v) for edge in unused_edges),
        Fraction(),
    )

    weighted_height = sum(
        (
            record.weight * correction(record.label, record.edge.u, record.edge.v)
            for record in records
        ),
        Fraction(),
    )

    base_product_loss = Fraction()
    base_square_loss = Fraction()
    base_monotonicity_loss = Fraction()
    base_direct = Fraction()
    base_delta = Fraction()
    for record in base_records:
        edge = record.edge
        if edge.ancestry or edge_key(edge.u, edge.v) != edge.root:
            raise AssertionError("base record is not an untouched original edge")
        delta = Fraction(edge.u + edge.v - total)
        center = displacement(n, r, record.label, record.weight)
        product_loss = record.weight * Fraction((edge.u - edge.v) ** 2, 4)
        square_loss = (2 - record.weight) * (delta - center) ** 2 / 4
        monotonicity_loss = local_floor(
            n,
            r,
            record.weight,
            record.label,
        ) - local_floor(n, r, record.weight, record.cutoff)
        direct = (
            original_slack(n, r, edge.u, edge.v)
            + record.weight * correction(record.label, edge.u, edge.v)
            - local_floor(n, r, record.weight, record.cutoff)
        )
        if direct != product_loss + square_loss + monotonicity_loss:
            raise AssertionError("base local decomposition failed")
        if min(product_loss, square_loss, monotonicity_loss) < 0:
            raise AssertionError("negative base local term")
        base_product_loss += product_loss
        base_square_loss += square_loss
        base_monotonicity_loss += monotonicity_loss
        base_direct += direct
        base_delta += delta

    recursive_loss = Fraction()
    recursive_direct = Fraction()
    zero_coverage_count = 0
    for record in recursive_records:
        edge = record.edge
        if not edge.ancestry or edge_key(edge.u, edge.v) == edge.root:
            raise AssertionError("recursive lineage disagrees with endpoints")
        if not (record.label < edge.u and record.label < edge.v):
            raise AssertionError("recursive endpoints were not inserted earlier")
        if not (edge.u < r or edge.v < r):
            raise AssertionError("recursive target has no inserted endpoint")

        coverage = record.weight * (
            (r - 1 - record.label) * (n - record.label)
            - (edge.u - record.label) * (edge.v - record.label)
        )
        jg_loss = recursive_floor(
            n,
            r,
            record.weight,
            record.label,
        ) - local_floor(n, r, record.weight, record.label)
        monotonicity_loss = local_floor(
            n,
            r,
            record.weight,
            record.label,
        ) - local_floor(n, r, record.weight, record.cutoff)
        direct = record.weight * correction(record.label, edge.u, edge.v) - local_floor(
            n, r, record.weight, record.cutoff
        )
        if direct != coverage + jg_loss + monotonicity_loss:
            raise AssertionError("recursive local decomposition failed")
        if min(coverage, jg_loss, monotonicity_loss) < 0:
            raise AssertionError("negative recursive local term")
        zero_coverage_count += int(coverage == 0)
        recursive_loss += coverage + jg_loss + monotonicity_loss
        recursive_direct += direct

    unused_delta = sum(
        (Fraction(edge.u + edge.v - total) for edge in unused_edges),
        Fraction(),
    )
    if base_delta + unused_delta != 0:
        raise AssertionError("original-edge deviation partition failed")
    if unused != sum(
        (Fraction((edge.u + edge.v - total) ** 2, 2) for edge in unused_edges),
        Fraction(),
    ):
        raise AssertionError("unused quadratic deviation identity failed")
    if base_delta**2 > 2 * unused_count * unused:
        raise AssertionError("unused-edge deviation Cauchy failed")

    removed_shift = sum(
        (
            displacement(n, r, record.label, record.weight)
            for record in recursive_records
        ),
        Fraction(),
    )
    removed_reciprocal = sum(
        (Fraction(4, 1) / (2 - record.weight) for record in recursive_records),
        Fraction(),
    )
    retained_shift = parameters.total_shift - removed_shift
    retained_reciprocal = parameters.reciprocal_weight - removed_reciprocal
    direct_retained_shift = sum(
        (displacement(n, r, record.label, record.weight) for record in base_records),
        Fraction(),
    )
    direct_retained_reciprocal = sum(
        (Fraction(4, 1) / (2 - record.weight) for record in base_records),
        Fraction(),
    )
    if retained_shift != direct_retained_shift:
        raise AssertionError("T coordinate removal failed")
    if retained_reciprocal != direct_retained_reciprocal:
        raise AssertionError("Q coordinate removal failed")
    if retained_shift <= 0 or retained_reciprocal <= 0:
        raise AssertionError("removed all base square coordinates")

    linear_sum = (
        sum(
            (
                displacement(n, r, record.label, record.weight)
                - Fraction(record.edge.u + record.edge.v - total)
                for record in base_records
            ),
            Fraction(),
        )
        - unused_delta
    )
    if linear_sum != retained_shift:
        raise AssertionError("combined-Cauchy linear sum failed")
    retained_energy = unused + base_square_loss
    retained_denominator = retained_reciprocal + 2 * unused_count
    if retained_energy * retained_denominator < retained_shift**2:
        raise AssertionError("combined-Cauchy cross product failed")
    check_radical_bound(
        retained_energy,
        unused,
        retained_shift,
        retained_reciprocal,
        unused_count,
    )

    optimized_bound = recursive_loss + retained_shift**2 / retained_denominator

    eligible_recursive_labels = range(fixture.s, fixture.r - 1)
    maximum_displacement = max(
        displacement(
            n,
            r,
            label,
            parameters.weights_by_label[label],
        )
        for label in eligible_recursive_labels
    )
    uniform_shift = max(
        Fraction(),
        parameters.total_shift - fixture.p * maximum_displacement,
    )
    m = fixture.q - fixture.ell
    uniform_denominator = parameters.reciprocal_weight + 2 * m
    recursive_denominator_correction = sum(
        (2 * record.weight / (2 - record.weight) for record in recursive_records),
        Fraction(),
    )
    if retained_denominator != (uniform_denominator - recursive_denominator_correction):
        raise AssertionError("uniform denominator identity failed")
    if retained_denominator > uniform_denominator:
        raise AssertionError("uniform denominator comparison failed")
    uniform_bound = uniform_shift**2 / uniform_denominator

    static_decomposition = (
        unused
        + base_product_loss
        + base_square_loss
        + base_monotonicity_loss
        + recursive_loss
    )
    direct_static = unused + base_direct + recursive_direct
    if static_decomposition != direct_static:
        raise AssertionError("static KR1G-6 decomposition failed")
    if (
        min(
            unused,
            base_product_loss,
            base_square_loss,
            base_monotonicity_loss,
            recursive_loss,
        )
        < 0
    ):
        raise AssertionError("negative generalized KR1G-6 term")

    return SelectedAudit(
        base_score=base_score,
        weighted_height=weighted_height,
        static_decomposition=static_decomposition,
        optimized_bound=optimized_bound,
        uniform_bound=uniform_bound,
        recursive_loss=recursive_loss,
        zero_coverage_count=zero_coverage_count,
    )


def check_complete_peak(
    parameters: Parameters,
    audit: SelectedAudit,
    complete_peak: Fraction,
) -> Fraction:
    """Check the direct residual against the full generalized decomposition."""
    height_loss = complete_peak - audit.weighted_height
    if height_loss < 0:
        raise AssertionError("negative height-telescope term")
    residual = Fraction(audit.base_score) + complete_peak - parameters.bound
    decomposition = height_loss + audit.static_decomposition
    if residual != decomposition:
        raise AssertionError(
            f"generalized KR1G-6 failed: {residual} != {decomposition}"
        )
    if residual < audit.optimized_bound:
        raise AssertionError("position-sensitive finite bound failed")
    if residual < audit.uniform_bound:
        raise AssertionError("uniform [T-pD]_+ bound failed")
    return residual


def verify_completion_fixture() -> None:
    """Exhaust the p=2 two-segment fixture and every completion."""
    fixture = FIXTURE
    parameters = build_parameters(fixture)
    if parameters.bound != Fraction(5099, 14):
        raise AssertionError(f"changed completion-fixture B: {parameters.bound}")
    if parameters.total_shift != Fraction(438, 35):
        raise AssertionError(f"changed completion-fixture T: {parameters.total_shift}")
    if parameters.reciprocal_weight != Fraction(304, 35):
        raise AssertionError(
            f"changed completion-fixture Q: {parameters.reciprocal_weight}"
        )
    raw_cycles = tuple(canonical_vertex_cycles(fixture.q))
    cycle_count = factorial(fixture.q - 1) // 2
    if len(raw_cycles) != cycle_count or cycle_count != 360:
        raise AssertionError("changed canonical-cycle count")

    factor = topology_factor(fixture.ell, fixture.p)
    if factor != 6:
        raise AssertionError(f"changed p=2 topology recurrence: {factor}")
    expected_selected = (
        cycle_count * falling_factorial(fixture.q, fixture.ell - fixture.p) * factor
    )
    expected_raw_selected = cycle_count * rising_factorial(
        fixture.q,
        fixture.ell,
    )
    completion_factor = rising_factorial(
        fixture.q + fixture.ell,
        fixture.s - 1,
    )
    expected_complete = expected_selected * completion_factor
    if expected_raw_selected != 181_440:
        raise AssertionError("changed raw selected-prefix count")
    if expected_selected != 15_120:
        raise AssertionError("changed p=2 selected-prefix count")
    if completion_factor != 10 or expected_complete != 151_200:
        raise AssertionError("changed exact completion count")

    raw_selected_histories = 0
    selected_histories = 0
    complete_histories = 0
    selected_types: Counter[str] = Counter()
    selected_topologies: Counter[str] = Counter()
    complete_topologies: Counter[str] = Counter()
    recursive_target_depths: Counter[int] = Counter()
    selected_two_inserted_histories = 0
    completion_two_inserted: Counter[str] = Counter()
    zero_coverage_records = 0
    zero_coverage_histories = 0
    minimum_residual: Fraction | None = None
    minimum_optimized_bound: Fraction | None = None
    minimum_uniform_bound: Fraction | None = None

    selected_labels = tuple(range(fixture.r - 1, fixture.s - 1, -1))

    for raw_cycle in raw_cycles:
        vertices = tuple(fixture.r + vertex for vertex in raw_cycle)
        base_state = initial_state(vertices)
        original_roots = {edge.root for edge in base_state}

        def exhaust_selected(
            state: State,
            index: int,
            height: Fraction,
            peak: Fraction,
            records: tuple[Record, ...],
        ) -> None:
            nonlocal complete_histories
            nonlocal minimum_optimized_bound
            nonlocal minimum_residual
            nonlocal minimum_uniform_bound
            nonlocal raw_selected_histories
            nonlocal selected_histories
            nonlocal selected_two_inserted_histories
            nonlocal zero_coverage_histories
            nonlocal zero_coverage_records

            if index == len(selected_labels):
                raw_selected_histories += 1
                recursive_records = tuple(
                    record for record in records if record.kind == "R"
                )
                if len(recursive_records) != fixture.p:
                    return

                selected_histories += 1
                type_word = "".join(record.kind for record in records)
                selected_types[type_word] += 1
                topology = classify_completion_topology(records, fixture)
                selected_topologies[topology] += 1
                for record in recursive_records:
                    recursive_target_depths[len(record.edge.ancestry)] += 1
                if any(
                    record.edge.u < fixture.r and record.edge.v < fixture.r
                    for record in recursive_records
                ):
                    selected_two_inserted_histories += 1

                audit = check_selected_history(
                    fixture,
                    parameters,
                    base_state,
                    records,
                )
                zero_coverage_records += audit.zero_coverage_count
                zero_coverage_histories += int(audit.zero_coverage_count > 0)
                minimum_optimized_bound = (
                    audit.optimized_bound
                    if minimum_optimized_bound is None
                    else min(minimum_optimized_bound, audit.optimized_bound)
                )
                minimum_uniform_bound = (
                    audit.uniform_bound
                    if minimum_uniform_bound is None
                    else min(minimum_uniform_bound, audit.uniform_bound)
                )

                literal_minimum_peak: Fraction | None = None
                completion_label = fixture.s - 1
                for completion_index, edge in enumerate(state):
                    child = split_state(state, completion_index, completion_label)
                    value = Fraction(correction(completion_label, edge.u, edge.v))
                    complete_peak = max(peak, height + value)
                    complete_histories += 1
                    complete_topologies[topology] += 1
                    if edge.u < fixture.r and edge.v < fixture.r:
                        completion_two_inserted[topology] += 1
                    residual = check_complete_peak(
                        parameters,
                        audit,
                        complete_peak,
                    )
                    if state_score(child) - state_score(state) != value:
                        raise AssertionError("completion score correction failed")
                    literal_minimum_peak = (
                        complete_peak
                        if literal_minimum_peak is None
                        else min(literal_minimum_peak, complete_peak)
                    )
                    minimum_residual = (
                        residual
                        if minimum_residual is None
                        else min(minimum_residual, residual)
                    )

                expected_minimum_peak = max(
                    peak,
                    height
                    + completion_excursion(
                        plain_state(state),
                        completion_label,
                    ),
                )
                if literal_minimum_peak != expected_minimum_peak:
                    raise AssertionError(
                        "literal completions and Bellman recursion disagree"
                    )
                return

            label = selected_labels[index]
            for edge_index, edge in enumerate(state):
                endpoint_original = edge_key(edge.u, edge.v) in original_roots
                lineage_original = not edge.ancestry
                if endpoint_original != lineage_original:
                    raise AssertionError("endpoint and lineage types disagree")
                kind = "B" if lineage_original else "R"
                child = split_state(state, edge_index, label)
                value = Fraction(correction(label, edge.u, edge.v))
                if state_score(child) - state_score(state) != value:
                    raise AssertionError("selected score correction failed")
                record = Record(
                    label=label,
                    edge=edge,
                    weight=parameters.weights_by_label[label],
                    cutoff=parameters.cutoffs_by_label[label],
                    kind=kind,
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
            base_state,
            0,
            Fraction(),
            Fraction(),
            (),
        )

    if raw_selected_histories != expected_raw_selected:
        raise AssertionError(
            f"raw selected count {raw_selected_histories} != {expected_raw_selected}"
        )
    if selected_histories != expected_selected:
        raise AssertionError(
            f"p=2 selected count {selected_histories} != {expected_selected}"
        )
    if complete_histories != expected_complete:
        raise AssertionError(
            f"complete count {complete_histories} != {expected_complete}"
        )

    expected_selected_types = Counter({"BRR": 15_120})
    expected_selected_topologies = Counter(
        {
            "sibling": 5_040,
            "nested_outer": 5_040,
            "nested_two_inserted": 5_040,
        }
    )
    expected_complete_topologies = Counter(
        {
            "sibling": 50_400,
            "nested_outer": 50_400,
            "nested_two_inserted": 50_400,
        }
    )
    expected_depths = Counter({1: 20_160, 2: 10_080})
    expected_completion_two_inserted = Counter(
        {
            "sibling": 10_080,
            "nested_outer": 10_080,
            "nested_two_inserted": 10_080,
        }
    )
    if selected_types != expected_selected_types:
        raise AssertionError(f"changed selected type counts: {selected_types}")
    if selected_topologies != expected_selected_topologies:
        raise AssertionError(f"changed selected topologies: {selected_topologies}")
    if complete_topologies != expected_complete_topologies:
        raise AssertionError(f"changed complete topologies: {complete_topologies}")
    if recursive_target_depths != expected_depths:
        raise AssertionError(f"changed recursive depths: {recursive_target_depths}")
    if selected_two_inserted_histories != 5_040:
        raise AssertionError("changed selected two-inserted-edge count")
    if completion_two_inserted != expected_completion_two_inserted:
        raise AssertionError(
            f"changed completion two-inserted counts: {completion_two_inserted}"
        )
    if sum(completion_two_inserted.values()) != 30_240:
        raise AssertionError("changed total completion two-inserted count")
    if zero_coverage_records != 2_880 or zero_coverage_histories != 2_880:
        raise AssertionError(
            "changed zero-coverage counts: "
            f"records={zero_coverage_records}, histories={zero_coverage_histories}"
        )

    if minimum_residual != Fraction(823, 14):
        raise AssertionError(f"changed minimum residual: {minimum_residual}")
    if minimum_optimized_bound != Fraction(21148, 665):
        raise AssertionError(
            f"changed minimum optimized bound: {minimum_optimized_bound}"
        )
    if minimum_uniform_bound != Fraction(81, 5110):
        raise AssertionError(f"changed minimum uniform bound: {minimum_uniform_bound}")

    print(
        "p2-two-segment: "
        f"cycles={cycle_count} raw_selected={raw_selected_histories} "
        f"selected={selected_histories} complete={complete_histories} "
        f"topologies={dict(sorted(selected_topologies.items()))} "
        f"depths={dict(sorted(recursive_target_depths.items()))} "
        f"selected_two_inserted={selected_two_inserted_histories} "
        f"completion_two_inserted={sum(completion_two_inserted.values())} "
        f"min_residual={minimum_residual} "
        f"min_bound={minimum_optimized_bound} "
        f"uniform={minimum_uniform_bound}: PASS"
    )


def verify_position_fixture() -> None:
    """Exhaust every p=2 position with two distinct original base targets."""
    fixture = POSITION_FIXTURE
    parameters = build_parameters(fixture)
    if parameters.bound != Fraction(256, 3):
        raise AssertionError(f"changed position-fixture B: {parameters.bound}")
    if parameters.total_shift != Fraction(32, 3):
        raise AssertionError(f"changed position-fixture T: {parameters.total_shift}")
    if parameters.reciprocal_weight != Fraction(32, 3):
        raise AssertionError(
            f"changed position-fixture Q: {parameters.reciprocal_weight}"
        )

    raw_cycles = tuple(canonical_vertex_cycles(fixture.q))
    cycle_count = factorial(fixture.q - 1) // 2
    if len(raw_cycles) != cycle_count or cycle_count != 3:
        raise AssertionError("changed position-fixture cycle count")

    factor = topology_factor(fixture.ell, fixture.p)
    if factor != 36:
        raise AssertionError(f"changed ell=4,p=2 topology recurrence: {factor}")
    expected_selected = (
        cycle_count * falling_factorial(fixture.q, fixture.ell - fixture.p) * factor
    )
    expected_raw_selected = cycle_count * rising_factorial(
        fixture.q,
        fixture.ell,
    )
    if expected_raw_selected != 2_520 or expected_selected != 1_296:
        raise AssertionError("changed position-fixture enumeration formulas")

    raw_selected_histories = 0
    selected_histories = 0
    selected_types: Counter[str] = Counter()
    recursive_relations: Counter[str] = Counter()
    type_relations: Counter[tuple[str, str]] = Counter()
    recursive_target_depths: Counter[int] = Counter()
    two_inserted_by_type: Counter[str] = Counter()
    minimum_residual: Fraction | None = None
    minimum_optimized_bound: Fraction | None = None
    minimum_uniform_bound: Fraction | None = None

    selected_labels = tuple(range(fixture.r - 1, fixture.s - 1, -1))

    for raw_cycle in raw_cycles:
        vertices = tuple(fixture.r + vertex for vertex in raw_cycle)
        base_state = initial_state(vertices)
        original_roots = {edge.root for edge in base_state}

        def exhaust_selected(
            state: State,
            index: int,
            height: Fraction,
            peak: Fraction,
            records: tuple[Record, ...],
        ) -> None:
            nonlocal minimum_optimized_bound
            nonlocal minimum_residual
            nonlocal minimum_uniform_bound
            nonlocal raw_selected_histories
            nonlocal selected_histories

            if index == len(selected_labels):
                raw_selected_histories += 1
                recursive_records = tuple(
                    record for record in records if record.kind == "R"
                )
                if len(recursive_records) != fixture.p:
                    return

                selected_histories += 1
                type_word = "".join(record.kind for record in records)
                selected_types[type_word] += 1
                relation, two_inserted = classify_recursive_relation(
                    records,
                    fixture,
                )
                recursive_relations[relation] += 1
                type_relations[(type_word, relation)] += 1
                for record in recursive_records:
                    recursive_target_depths[len(record.edge.ancestry)] += 1
                if two_inserted:
                    two_inserted_by_type[type_word] += 1

                base_roots = tuple(
                    record.edge.root for record in records if record.kind == "B"
                )
                if len(base_roots) != 2 or len(set(base_roots)) != 2:
                    raise AssertionError(
                        "position fixture lost its two distinct base targets"
                    )

                audit = check_selected_history(
                    fixture,
                    parameters,
                    base_state,
                    records,
                )
                residual = check_complete_peak(parameters, audit, peak)
                if completion_excursion(plain_state(state), 0) != 0:
                    raise AssertionError("s=1 completion base case failed")
                minimum_residual = (
                    residual
                    if minimum_residual is None
                    else min(minimum_residual, residual)
                )
                minimum_optimized_bound = (
                    audit.optimized_bound
                    if minimum_optimized_bound is None
                    else min(minimum_optimized_bound, audit.optimized_bound)
                )
                minimum_uniform_bound = (
                    audit.uniform_bound
                    if minimum_uniform_bound is None
                    else min(minimum_uniform_bound, audit.uniform_bound)
                )
                return

            label = selected_labels[index]
            for edge_index, edge in enumerate(state):
                endpoint_original = edge_key(edge.u, edge.v) in original_roots
                lineage_original = not edge.ancestry
                if endpoint_original != lineage_original:
                    raise AssertionError("position endpoint/lineage types disagree")
                kind = "B" if lineage_original else "R"
                child = split_state(state, edge_index, label)
                value = Fraction(correction(label, edge.u, edge.v))
                if state_score(child) - state_score(state) != value:
                    raise AssertionError("position-fixture score correction failed")
                next_height = height + value
                exhaust_selected(
                    child,
                    index + 1,
                    next_height,
                    max(peak, next_height),
                    (
                        *records,
                        Record(
                            label=label,
                            edge=edge,
                            weight=parameters.weights_by_label[label],
                            cutoff=parameters.cutoffs_by_label[label],
                            kind=kind,
                        ),
                    ),
                )

        exhaust_selected(
            base_state,
            0,
            Fraction(),
            Fraction(),
            (),
        )

    if raw_selected_histories != expected_raw_selected:
        raise AssertionError(
            f"position raw count {raw_selected_histories} != {expected_raw_selected}"
        )
    if selected_histories != expected_selected:
        raise AssertionError(
            f"position p=2 count {selected_histories} != {expected_selected}"
        )

    expected_types = Counter({"BBRR": 720, "BRBR": 360, "BRRB": 216})
    expected_relations = Counter({"nested": 576, "different_root": 432, "sibling": 288})
    expected_type_relations = Counter(
        {
            ("BBRR", "nested"): 288,
            ("BBRR", "different_root"): 288,
            ("BBRR", "sibling"): 144,
            ("BRBR", "nested"): 144,
            ("BRBR", "different_root"): 144,
            ("BRBR", "sibling"): 72,
            ("BRRB", "nested"): 144,
            ("BRRB", "sibling"): 72,
        }
    )
    expected_depths = Counter({1: 2_016, 2: 576})
    expected_two_inserted = Counter({"BBRR": 144, "BRBR": 72, "BRRB": 72})
    if selected_types != expected_types:
        raise AssertionError(f"changed position type counts: {selected_types}")
    if recursive_relations != expected_relations:
        raise AssertionError(f"changed recursive relations: {recursive_relations}")
    if type_relations != expected_type_relations:
        raise AssertionError(f"changed type/relation counts: {type_relations}")
    if recursive_target_depths != expected_depths:
        raise AssertionError(f"changed position depths: {recursive_target_depths}")
    if two_inserted_by_type != expected_two_inserted:
        raise AssertionError(
            f"changed position two-inserted counts: {two_inserted_by_type}"
        )

    if minimum_residual != Fraction(260, 3):
        raise AssertionError(f"changed position minimum residual: {minimum_residual}")
    if minimum_optimized_bound != Fraction(589, 21):
        raise AssertionError(
            f"changed position minimum bound: {minimum_optimized_bound}"
        )
    if minimum_uniform_bound != Fraction(25, 24):
        raise AssertionError(f"changed position uniform bound: {minimum_uniform_bound}")

    print(
        "p2-position-sweep: "
        f"cycles={cycle_count} raw_selected={raw_selected_histories} "
        f"selected={selected_histories} types={dict(sorted(selected_types.items()))} "
        f"relations={dict(sorted(recursive_relations.items()))} "
        f"depths={dict(sorted(recursive_target_depths.items()))} "
        f"two_inserted={sum(two_inserted_by_type.values())} "
        f"min_residual={minimum_residual} "
        f"min_bound={minimum_optimized_bound} "
        f"uniform={minimum_uniform_bound}: PASS"
    )


def main() -> None:
    """Run both exhaustive p=2 fixtures."""
    verify_completion_fixture()
    verify_position_fixture()
    print(
        "PASS: exact topology recurrence, arbitrary p=2 positions and "
        "parentage, generalized KR1G-6, radical/combined Cauchy, "
        "[T-pD]_+ uniform bound, and completion Bellman recursion agree"
    )


if __name__ == "__main__":
    main()
