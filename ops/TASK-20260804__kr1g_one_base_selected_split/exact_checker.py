"""Independent exact checker for the one-base selected KR1G class.

The checker is deliberately task-local and imports only the Python standard
library.  Its theorem-domain fixture fixes one nonmonotone cycle on ``q=9``
consecutive labels, uses ``ell=4``, ``p=ell-1=3``, ``s=3``, and assigns two
rational selected-window weights.  Thus every retained selected prefix has
type ``BRRR``: label ``r-1`` makes the unique base split and the remaining
selected labels split arbitrary recursive descendants.

All ``q*ell! = 216`` selected prefixes on that one fixed base cycle and all
39,312 arbitrary completions through labels 2 and 1 are enumerated.  The
checker does not enumerate the other unoriented base cycles; it separately
checks the global arithmetic identity
``((q-1)!/2)*(q*ell!) = q!*ell!/2``.  Fresh edge-lineage metadata audits roots,
branches, ancestry, direct parents, depths, sibling/balanced histories, and
targets with two inserted endpoints.  Exact :class:`fractions.Fraction`
arithmetic checks every term of KR1G-93 separately, the KR1G-118/119
deterministic sum, the full KR1G-94 decomposition, the one-base specialization
of KR1G-98 while retaining the entire recursive sum, and the KR1G-91b Bellman
minimum against literal completion enumeration.

This bounded rational fixture corroborates the finite identities and recursive
topologies.  It is not an irrational all-middle row and does not replace the
general proof or its asymptotic argument.
"""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import factorial


EdgeKey = tuple[int, int]
PlainEdge = tuple[int, int]
PlainState = tuple[PlainEdge, ...]


@dataclass(frozen=True)
class EdgeState:
    """One oriented edge with original root, ancestry, and root branch."""

    u: int
    v: int
    root: EdgeKey
    ancestry: tuple[int, ...]
    branch: int | None


State = tuple[EdgeState, ...]


@dataclass(frozen=True)
class Fixture:
    """The single finite theorem-domain fixture."""

    q: int
    ell: int
    p: int
    s: int
    cutoffs: tuple[int, ...]
    weights: tuple[Fraction, ...]
    base_offsets: tuple[int, ...]

    @property
    def r(self) -> int:
        return self.s + self.ell

    @property
    def n(self) -> int:
        return self.r + self.q - 1


@dataclass(frozen=True)
class Parameters:
    """History-independent exact ``B``, ``T``, and ``Q`` data."""

    weights_by_label: dict[int, Fraction]
    cutoffs_by_label: dict[int, int]
    bound: Fraction
    total_shift: Fraction
    reciprocal_weight: Fraction


@dataclass(frozen=True)
class Record:
    """One selected insertion and its target before the split."""

    label: int
    edge: EdgeState
    weight: Fraction
    cutoff: int
    kind: str


@dataclass(frozen=True)
class SelectedAudit:
    """Completion-independent exact audit values for one selected prefix."""

    base_score: int
    weighted_height: Fraction
    static_decomposition: Fraction
    recursive_loss: Fraction
    coverage_sum: Fraction
    deterministic_recursive: Fraction
    retained_ratio: Fraction
    optimized_bound: Fraction
    recursive_components: tuple[tuple[Fraction, Fraction, Fraction], ...]


FIXTURE = Fixture(
    q=9,
    ell=4,
    p=3,
    s=3,
    cutoffs=(5, 3),
    weights=(Fraction(3, 4), Fraction(1, 4)),
    base_offsets=(0, 7, 1, 6, 2, 5, 3, 4, 8),
)


def edge_key(u: int, v: int) -> EdgeKey:
    """Return a stable unordered edge key."""
    return (u, v) if u < v else (v, u)


def initial_state(vertices: tuple[int, ...]) -> State:
    """Construct the oriented original cycle with empty lineage."""
    return tuple(
        EdgeState(
            u,
            vertices[(index + 1) % len(vertices)],
            edge_key(u, vertices[(index + 1) % len(vertices)]),
            (),
            None,
        )
        for index, u in enumerate(vertices)
    )


def split_state(state: State, index: int, label: int) -> State:
    """Split one edge and preserve its literal original-root lineage."""
    edge = state[index]
    ancestry = (*edge.ancestry, label)
    if edge.ancestry:
        left_branch = right_branch = edge.branch
    else:
        left_branch, right_branch = 0, 1
    children = (
        EdgeState(edge.u, label, edge.root, ancestry, left_branch),
        EdgeState(label, edge.v, edge.root, ancestry, right_branch),
    )
    return (*state[:index], *children, *state[index + 1 :])


def plain_state(state: State) -> PlainState:
    """Drop all lineage metadata for the independent Bellman recursion."""
    return tuple((edge.u, edge.v) for edge in state)


def split_plain(state: PlainState, index: int, label: int) -> PlainState:
    """Split one plain oriented edge."""
    u, v = state[index]
    return (*state[:index], (u, label), (label, v), *state[index + 1 :])


def correction(label: int, u: int, v: int) -> int:
    """Return the exact adjacent-product change for one insertion."""
    return label * (u + v) - u * v


def state_score(state: State) -> int:
    """Return the cyclic adjacent-product score from its oriented edges."""
    return sum(edge.u * edge.v for edge in state)


def pairing_floor(n: int, r: int) -> int:
    """Evaluate the complementary-pairing floor directly."""
    return sum(label * (n + r - label) for label in range(r, n + 1))


def original_slack(n: int, r: int, u: int, v: int) -> Fraction:
    """Return the quadratic slack of one original edge."""
    return Fraction((u + v - n - r) ** 2, 2)


def local_floor(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    """Evaluate ``G_{n,weight}(label)`` from its defining polynomial."""
    total = n + r
    numerator = weight * (4 * total * label - total**2 - 2 * weight * label**2)
    return numerator / (2 * (2 - weight))


def recursive_floor(n: int, r: int, weight: Fraction, label: int) -> Fraction:
    """Evaluate ``J_{n,weight}(label)`` directly."""
    return weight * ((n + r - 1) * label - n * (r - 1))


def displacement(n: int, r: int, label: int, weight: Fraction) -> Fraction:
    """Return the positive square-center displacement ``d_label``."""
    return weight * (n + r - 2 * label) / (2 - weight)


def build_parameters(fixture: Fixture) -> Parameters:
    """Build the exact selected segments and finite ``B``, ``T``, ``Q``."""
    if len(fixture.cutoffs) != len(fixture.weights):
        raise AssertionError("cutoff/weight length mismatch")
    if fixture.cutoffs[-1] != fixture.s:
        raise AssertionError("last cutoff is not s")
    if tuple(sorted(fixture.weights, reverse=True)) != fixture.weights:
        raise AssertionError("weights are not nonincreasing")
    if not all(Fraction() < weight < 1 for weight in fixture.weights):
        raise AssertionError("weights are outside (0,1)")

    weights_by_label: dict[int, Fraction] = {}
    cutoffs_by_label: dict[int, int] = {}
    selected_floor = Fraction()
    upper = fixture.r
    for cutoff, weight in zip(fixture.cutoffs, fixture.weights, strict=True):
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
        raise AssertionError("selected segments do not partition the window")
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
        weights_by_label,
        cutoffs_by_label,
        bound,
        total_shift,
        reciprocal_weight,
    )


def deterministic_recursive_sum(fixture: Fixture) -> Fraction:
    """Evaluate the exact segment sum ``K_det`` from KR1G-118."""
    result = Fraction()
    upper = fixture.r
    recursive_count = 0
    for index, (cutoff, weight) in enumerate(
        zip(fixture.cutoffs, fixture.weights, strict=True)
    ):
        count = upper - cutoff - int(index == 0)
        if count < 0:
            raise AssertionError("negative segment recursive count")
        segment_j = recursive_floor(
            fixture.n,
            fixture.r,
            weight,
            cutoff,
        ) - local_floor(fixture.n, fixture.r, weight, cutoff)
        if segment_j <= 0:
            raise AssertionError("nonpositive KR1G-118 segment J")
        result += count * segment_j
        result += weight * (fixture.n + fixture.r - 1) * count * (count - 1) / 2
        recursive_count += count
        upper = cutoff
    if recursive_count != fixture.ell - 1:
        raise AssertionError("KR1G-118 segment counts do not cover recursive labels")
    return result


@lru_cache(maxsize=None)
def completion_excursion(state: PlainState, label: int) -> Fraction:
    """Return the least future positive excursion by KR1G-91a Bellman."""
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


def check_selected_history(
    fixture: Fixture,
    parameters: Parameters,
    base_state: State,
    records: tuple[Record, ...],
) -> SelectedAudit:
    """Check lineage and every completion-independent KR1G identity."""
    n, r = fixture.n, fixture.r
    total = n + r
    base_score = state_score(base_state)
    pairing = pairing_floor(n, r)
    base_slack = sum(
        (original_slack(n, r, edge.u, edge.v) for edge in base_state),
        Fraction(),
    )
    if Fraction(base_score - pairing) != base_slack:
        raise AssertionError("base score/slack identity failed")

    if len(records) != fixture.ell:
        raise AssertionError("selected record count changed")
    if "".join(record.kind for record in records) != "BRRR":
        raise AssertionError("selected word is not BRRR")
    base_record = records[0]
    recursive_records = records[1:]
    if base_record.label != r - 1 or len(recursive_records) != fixture.p:
        raise AssertionError("unique base coordinate changed")
    if base_record.edge.ancestry or base_record.edge.branch is not None:
        raise AssertionError("base target is not an untouched original edge")

    base_root = base_record.edge.root
    seen_labels = {base_record.label}
    for record in recursive_records:
        edge = record.edge
        if edge.root != base_root or not edge.ancestry:
            raise AssertionError("recursive target left the unique base root")
        if edge.branch not in (0, 1):
            raise AssertionError("recursive target lost its root branch")
        if edge.ancestry[0] != base_record.label:
            raise AssertionError("recursive ancestry lost the base insertion")
        if not set(edge.ancestry).issubset(seen_labels):
            raise AssertionError("recursive ancestry contains a future label")
        if not all(
            parent > child for parent, child in zip(edge.ancestry, edge.ancestry[1:])
        ):
            raise AssertionError("recursive ancestry is not descending")
        if edge.ancestry[-1] <= record.label:
            raise AssertionError("direct recursive parent was not inserted earlier")
        if not (record.label < edge.u and record.label < edge.v):
            raise AssertionError("recursive target endpoints are not earlier labels")
        if not (edge.u < r or edge.v < r):
            raise AssertionError("recursive target lacks an inserted endpoint")
        seen_labels.add(record.label)

    unused_edges = tuple(edge for edge in base_state if edge.root != base_root)
    unused_count = fixture.q - fixture.ell + fixture.p
    if unused_count != fixture.q - 1 or len(unused_edges) != unused_count:
        raise AssertionError("one-base unused-edge count failed")
    unused = sum(
        (original_slack(n, r, edge.u, edge.v) for edge in unused_edges),
        Fraction(),
    )
    unused_delta = sum(
        (Fraction(edge.u + edge.v - total) for edge in unused_edges),
        Fraction(),
    )

    weighted_height = sum(
        (
            record.weight * correction(record.label, record.edge.u, record.edge.v)
            for record in records
        ),
        Fraction(),
    )

    edge = base_record.edge
    base_delta = Fraction(edge.u + edge.v - total)
    base_center = displacement(n, r, base_record.label, base_record.weight)
    base_product = base_record.weight * Fraction((edge.u - edge.v) ** 2, 4)
    base_square = (2 - base_record.weight) * (base_delta - base_center) ** 2 / 4
    base_monotonicity = local_floor(
        n,
        r,
        base_record.weight,
        base_record.label,
    ) - local_floor(n, r, base_record.weight, base_record.cutoff)
    base_direct = (
        original_slack(n, r, edge.u, edge.v)
        + base_record.weight * correction(base_record.label, edge.u, edge.v)
        - local_floor(n, r, base_record.weight, base_record.cutoff)
    )
    if base_direct != base_product + base_square + base_monotonicity:
        raise AssertionError("base local decomposition failed")
    if min(base_product, base_square, base_monotonicity) < 0:
        raise AssertionError("negative base local term")

    recursive_components = []
    recursive_loss = Fraction()
    recursive_direct = Fraction()
    for record in recursive_records:
        target = record.edge
        coverage = record.weight * (
            (r - 1 - record.label) * (n - record.label)
            - (target.u - record.label) * (target.v - record.label)
        )
        jg_loss = recursive_floor(
            n,
            r,
            record.weight,
            record.label,
        ) - local_floor(n, r, record.weight, record.label)
        monotonicity = local_floor(
            n,
            r,
            record.weight,
            record.label,
        ) - local_floor(n, r, record.weight, record.cutoff)
        direct = record.weight * correction(
            record.label, target.u, target.v
        ) - local_floor(n, r, record.weight, record.cutoff)
        if direct != coverage + jg_loss + monotonicity:
            raise AssertionError("KR1G-93 recursive local identity failed")
        if coverage < 0:
            raise AssertionError("negative KR1G-93 coverage term")
        if jg_loss < 0:
            raise AssertionError("negative KR1G-93 J-G term")
        if monotonicity < 0:
            raise AssertionError("negative KR1G-93 monotonicity term")
        recursive_components.append((coverage, jg_loss, monotonicity))
        recursive_loss += coverage + jg_loss + monotonicity
        recursive_direct += direct

    coverage_sum = sum(
        (coverage for coverage, _, _ in recursive_components),
        Fraction(),
    )
    deterministic_from_records = sum(
        (jg_loss + monotonicity for _, jg_loss, monotonicity in recursive_components),
        Fraction(),
    )
    deterministic_recursive = deterministic_recursive_sum(fixture)
    if deterministic_from_records != deterministic_recursive:
        raise AssertionError("KR1G-118 deterministic sum changed across prefixes")
    if recursive_loss != coverage_sum + deterministic_recursive:
        raise AssertionError("KR1G-119 recursive split failed")

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
    direct_shift = displacement(n, r, base_record.label, base_record.weight)
    direct_reciprocal = Fraction(4, 1) / (2 - base_record.weight)
    if retained_shift != direct_shift or retained_reciprocal != direct_reciprocal:
        raise AssertionError("one-base T/Q coordinate removal failed")
    if retained_shift != 6 or retained_reciprocal != Fraction(16, 5):
        raise AssertionError("changed one-base retained T/Q constants")

    linear_sum = retained_shift - base_delta - unused_delta
    if linear_sum != retained_shift:
        raise AssertionError("combined-Cauchy linear sum failed")
    retained_energy = unused + base_square
    retained_denominator = retained_reciprocal + 2 * unused_count
    if retained_denominator != Fraction(96, 5):
        raise AssertionError("changed one-base KR1G-98 denominator")
    if retained_energy * retained_denominator < retained_shift**2:
        raise AssertionError("one-base combined Cauchy failed")
    retained_ratio = retained_shift**2 / retained_denominator
    if retained_ratio != Fraction(15, 8):
        raise AssertionError("changed one-base KR1G-98 scalar term")

    static_decomposition = (
        unused + base_product + base_square + base_monotonicity + recursive_loss
    )
    direct_static = unused + base_direct + recursive_direct
    if static_decomposition != direct_static:
        raise AssertionError("KR1G-94 static decomposition failed")
    optimized_bound = recursive_loss + retained_ratio
    return SelectedAudit(
        base_score,
        weighted_height,
        static_decomposition,
        recursive_loss,
        coverage_sum,
        deterministic_recursive,
        retained_ratio,
        optimized_bound,
        tuple(recursive_components),
    )


def check_complete_peak(
    parameters: Parameters,
    audit: SelectedAudit,
    complete_peak: Fraction,
) -> Fraction:
    """Check KR1G-94 and the recursive-term-preserving KR1G-98 bound."""
    height_loss = complete_peak - audit.weighted_height
    if height_loss < 0:
        raise AssertionError("negative height-telescope term")
    residual = Fraction(audit.base_score) + complete_peak - parameters.bound
    decomposition = height_loss + audit.static_decomposition
    if residual != decomposition:
        raise AssertionError("full KR1G-94 decomposition failed")
    if residual < audit.optimized_bound:
        raise AssertionError("recursive-term-preserving KR1G-98 failed")
    uniform_bound = audit.deterministic_recursive + audit.retained_ratio
    if residual < uniform_bound:
        raise AssertionError("uniform KR1G-120 bound failed")
    if audit.optimized_bound != audit.recursive_loss + Fraction(15, 8):
        raise AssertionError("recursive KR1G-98 specialization changed")
    if audit.optimized_bound != (
        audit.coverage_sum + audit.deterministic_recursive + Fraction(15, 8)
    ):
        raise AssertionError("topology-sensitive KR1G-120 bound changed")
    return residual


def verify_fixture() -> None:
    """Exhaust every BRRR prefix and every compatible completion."""
    fixture = FIXTURE
    if fixture.p != fixture.ell - 1:
        raise AssertionError("fixture is not the one-base selected class")
    if not fixture.ell < (fixture.q + 1) // 2:
        raise AssertionError("fixture is outside ell < ceil(q/2)")
    if sorted(fixture.base_offsets) != list(range(fixture.q)):
        raise AssertionError("base offsets are not a permutation")
    if fixture.base_offsets in (
        tuple(range(fixture.q)),
        tuple(reversed(range(fixture.q))),
    ):
        raise AssertionError("base cycle is not nonmonotone")

    vertices = tuple(fixture.r + offset for offset in fixture.base_offsets)
    base_state = initial_state(vertices)
    parameters = build_parameters(fixture)
    selected_labels = tuple(range(fixture.r - 1, fixture.s - 1, -1))
    if selected_labels != (6, 5, 4, 3):
        raise AssertionError("selected labels changed")

    expected_selected = fixture.q * factorial(fixture.ell)
    unoriented_base_cycles = factorial(fixture.q - 1) // 2
    global_prefix_count = unoriented_base_cycles * expected_selected
    closed_global_prefix_count = factorial(fixture.q) * factorial(fixture.ell) // 2
    if global_prefix_count != closed_global_prefix_count:
        raise AssertionError("global KR1G-116 prefix-count identity failed")
    if unoriented_base_cycles != 20_160 or global_prefix_count != 4_354_560:
        raise AssertionError("changed global one-base prefix counts")
    completion_factor = 1
    for offset in range(fixture.s - 1):
        completion_factor *= fixture.q + fixture.ell + offset
    expected_complete = expected_selected * completion_factor
    if expected_selected != 216 or completion_factor != 182:
        raise AssertionError("changed exact finite factors")
    if expected_complete != 39_312:
        raise AssertionError("changed exact completion count")

    selected_count = 0
    complete_count = 0
    type_counts: Counter[str] = Counter()
    depth_counts: Counter[int] = Counter()
    two_inserted_records = 0
    two_inserted_histories = 0
    second_sibling_histories = 0
    balanced_histories = 0
    depth_three_histories = 0
    recursive_component_occurrences = Counter()
    minimum_residual: Fraction | None = None
    minimum_bellman_residual: Fraction | None = None
    minimum_recursive_bound: Fraction | None = None
    deterministic_recursive = deterministic_recursive_sum(fixture)

    def finish_selected(
        state: State,
        height: Fraction,
        peak: Fraction,
        records: tuple[Record, ...],
    ) -> None:
        nonlocal balanced_histories
        nonlocal complete_count
        nonlocal depth_three_histories
        nonlocal minimum_bellman_residual
        nonlocal minimum_recursive_bound
        nonlocal minimum_residual
        nonlocal second_sibling_histories
        nonlocal selected_count
        nonlocal two_inserted_histories
        nonlocal two_inserted_records

        selected_count += 1
        type_word = "".join(record.kind for record in records)
        type_counts[type_word] += 1
        if type_word != "BRRR" or len(state) != fixture.q + fixture.ell:
            raise AssertionError("changed terminal selected prefix")

        recursive = records[1:]
        for record in recursive:
            depth = len(record.edge.ancestry)
            depth_counts[depth] += 1
            if record.edge.u < fixture.r and record.edge.v < fixture.r:
                two_inserted_records += 1
        has_two_inserted = any(
            record.edge.u < fixture.r and record.edge.v < fixture.r
            for record in recursive
        )
        two_inserted_histories += int(has_two_inserted)
        second_sibling_histories += int(
            recursive[1].edge.branch != recursive[0].edge.branch
        )
        balanced_histories += int(
            len({record.edge.branch for record in recursive}) == 2
        )
        depth_three_histories += int(
            any(len(record.edge.ancestry) == 3 for record in recursive)
        )

        audit = check_selected_history(fixture, parameters, base_state, records)
        minimum_recursive_bound = (
            audit.optimized_bound
            if minimum_recursive_bound is None
            else min(minimum_recursive_bound, audit.optimized_bound)
        )
        for coverage, jg_loss, monotonicity in audit.recursive_components:
            recursive_component_occurrences["coverage"] += int(coverage >= 0)
            recursive_component_occurrences["jg"] += int(jg_loss >= 0)
            recursive_component_occurrences["monotonicity"] += int(monotonicity >= 0)

        literal_minimum_peak: Fraction | None = None

        def exhaust_completion(
            completion_state: State,
            label: int,
            completion_height: Fraction,
            completion_peak: Fraction,
        ) -> None:
            nonlocal complete_count
            nonlocal literal_minimum_peak
            nonlocal minimum_residual

            if label == 0:
                complete_count += 1
                residual = check_complete_peak(parameters, audit, completion_peak)
                literal_minimum_peak = (
                    completion_peak
                    if literal_minimum_peak is None
                    else min(literal_minimum_peak, completion_peak)
                )
                minimum_residual = (
                    residual
                    if minimum_residual is None
                    else min(minimum_residual, residual)
                )
                return

            for edge_index, edge in enumerate(completion_state):
                child = split_state(completion_state, edge_index, label)
                value = Fraction(correction(label, edge.u, edge.v))
                if state_score(child) - state_score(completion_state) != value:
                    raise AssertionError("completion score correction failed")
                next_height = completion_height + value
                exhaust_completion(
                    child,
                    label - 1,
                    next_height,
                    max(completion_peak, next_height),
                )

        exhaust_completion(state, fixture.s - 1, height, peak)
        bellman_peak = max(
            peak,
            height + completion_excursion(plain_state(state), fixture.s - 1),
        )
        if literal_minimum_peak != bellman_peak:
            raise AssertionError("literal completion and KR1G-91a disagree")
        bellman_residual = Fraction(audit.base_score) + bellman_peak - parameters.bound
        minimum_bellman_residual = (
            bellman_residual
            if minimum_bellman_residual is None
            else min(minimum_bellman_residual, bellman_residual)
        )

    def exhaust_recursive(
        state: State,
        index: int,
        height: Fraction,
        peak: Fraction,
        records: tuple[Record, ...],
        selected_root: EdgeKey,
    ) -> None:
        if index == len(selected_labels):
            finish_selected(state, height, peak, records)
            return

        label = selected_labels[index]
        candidates = tuple(
            (edge_index, edge)
            for edge_index, edge in enumerate(state)
            if edge.ancestry and edge.root == selected_root
        )
        if len(candidates) != index + 1:
            raise AssertionError("recursive edge count does not give ell! factor")
        for edge_index, edge in candidates:
            child = split_state(state, edge_index, label)
            value = Fraction(correction(label, edge.u, edge.v))
            if state_score(child) - state_score(state) != value:
                raise AssertionError("recursive selected score correction failed")
            next_height = height + value
            exhaust_recursive(
                child,
                index + 1,
                next_height,
                max(peak, next_height),
                (
                    *records,
                    Record(
                        label,
                        edge,
                        parameters.weights_by_label[label],
                        parameters.cutoffs_by_label[label],
                        "R",
                    ),
                ),
                selected_root,
            )

    base_label = selected_labels[0]
    if len(base_state) != fixture.q:
        raise AssertionError("base cycle edge count changed")
    for edge_index, edge in enumerate(base_state):
        child = split_state(base_state, edge_index, base_label)
        value = Fraction(correction(base_label, edge.u, edge.v))
        if state_score(child) - state_score(base_state) != value:
            raise AssertionError("base selected score correction failed")
        exhaust_recursive(
            child,
            1,
            value,
            max(Fraction(), value),
            (
                Record(
                    base_label,
                    edge,
                    parameters.weights_by_label[base_label],
                    parameters.cutoffs_by_label[base_label],
                    "B",
                ),
            ),
            edge.root,
        )

    if selected_count != expected_selected:
        raise AssertionError("q*ell! selected-prefix count failed")
    if complete_count != expected_complete:
        raise AssertionError("arbitrary completion count failed")
    if type_counts != Counter({"BRRR": 216}):
        raise AssertionError(f"changed type counts: {type_counts}")
    if depth_counts != Counter({1: 324, 2: 252, 3: 72}):
        raise AssertionError(f"changed recursive depth counts: {depth_counts}")
    if two_inserted_records != 180 or two_inserted_histories != 144:
        raise AssertionError("changed inserted-inserted topology counts")
    if second_sibling_histories != 72:
        raise AssertionError("changed sibling-history count")
    if balanced_histories != 108:
        raise AssertionError("changed balanced-history count")
    if depth_three_histories != 72:
        raise AssertionError("changed depth-three-history count")
    expected_component_occurrences = Counter(
        {"coverage": 648, "jg": 648, "monotonicity": 648}
    )
    if recursive_component_occurrences != expected_component_occurrences:
        raise AssertionError("not every KR1G-93 component was audited")
    if minimum_residual != minimum_bellman_residual:
        raise AssertionError("literal minimum and finite KR1G-91b minimum disagree")
    if minimum_residual is None or minimum_recursive_bound is None:
        raise AssertionError("empty finite minima")
    if minimum_residual != Fraction(3464, 35):
        raise AssertionError("changed exact fixture-global residual minimum")
    if minimum_recursive_bound != Fraction(18591, 280):
        raise AssertionError("changed recursive-term-preserving bound minimum")
    if deterministic_recursive <= 0:
        raise AssertionError("nonpositive KR1G-118 deterministic sum")
    if deterministic_recursive != Fraction(8333, 140):
        raise AssertionError("changed exact KR1G-118 deterministic sum")
    if deterministic_recursive + Fraction(15, 8) != Fraction(17191, 280):
        raise AssertionError("changed uniform KR1G-120 fixture bound")

    print(
        "one-base-BRRR: "
        f"fixed_cycles=1/{unoriented_base_cycles} prefixes={selected_count} "
        f"global_prefix_formula={global_prefix_count} completions={complete_count} "
        "depths={1:324,2:252,3:72} sibling=72 balanced=108 "
        f"two_inserted=180 K_det={deterministic_recursive} "
        f"uniform={deterministic_recursive + Fraction(15, 8)} "
        f"min_residual={minimum_residual} "
        f"min_E_plus_15/8={minimum_recursive_bound}: PASS"
    )
    print(
        "PASS: KR1G-91b Bellman, KR1G-93 components, KR1G-94, and "
        "recursive-term-preserving one-base KR1G-98 agree"
    )


def main() -> None:
    """Run the exact bounded theorem-domain audit."""
    verify_fixture()


if __name__ == "__main__":
    main()
