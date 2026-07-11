# Radius-Sequence-Aware Small-n Cyclic-Order Search Design

Date: 2026-07-11

## Scope And Classification

This document is a design artifact for a future implementation task. It
establishes no quadratic-radii optimum, no certificate, and no theorem.

- DEFINITION: a small-n cyclic-order search means a deterministic search over
  cyclic orders of the explicit quadratic radius sequence
  `(1^2, 2^2, ..., n^2)`, modulo rotation and reflection.
- DESIGN DECISION: the search layer should work with index labels and explicit
  radius values as separate data. It should not treat `n` alone as enough
  result provenance.
- DESIGN DECISION: the first implementation should be exhaustive and
  float64-backed for small n, with high-precision rechecks for the incumbent
  and ties. Certified global claims require a later independent verifier and
  interval evidence for the whole order space.
- UNRESOLVED CLAIM: any pruned or frontier-certified search based on
  subset-chain lower bounds needs a local proof and verifier before it can
  support `computer_certified_result` claims.

## Existing Foundation

The current package already supplies the fixed-order layer needed by the
search:

- `power_ringmin.geometry.quadratic_radii(n)` returns the explicit quadratic
  radius sequence.
- `power_ringmin.evaluator.full_radius(order)` evaluates one fixed cyclic
  radius order by all-pairs STN feasibility and Cartesian validation.
- `power_ringmin.highprec.full_radius_mp(order)` and root `verify.py` provide
  high-precision fixed-order checks.
- `power-ringmin-export-fixed-order-batch` can export fixed-order artifacts for
  explicitly supplied orders.

The missing layer is a radius-sequence-aware generator and runner that owns the
global order-space claim.

## Order Model

Represent every order by both labels and radii:

```text
index_order = (n, i_2, ..., i_n)
radius_order = tuple(i * i for i in index_order)
radius_sequence = {
  formula: "k^2",
  indices: (1, 2, ..., n),
  radii: (1, 4, ..., n^2)
}
```

The canonical order generator should fix the largest index at position `0` and
remove reflection duplicates by requiring `index_order[1] < index_order[-1]`.
For n >= 3 this gives `(n - 1)! / 2` canonical cyclic orders.

Proposed APIs:

```python
def canonical_index_orders(n: int) -> Iterator[tuple[int, ...]]:
    """Yield cyclic index orders modulo rotation and reflection."""

def canonicalize_index_order(order: Sequence[int]) -> tuple[int, ...]:
    """Return the canonical representative of one index cycle."""

def index_order_to_radius_order(order: Sequence[int]) -> tuple[int, ...]:
    """Map quadratic indices to explicit radii."""
```

The generic future extension should accept explicit `(label, radius)` pairs,
but the first quadratic implementation should keep the narrower index API to
avoid pretending arbitrary radius families have been designed.

## Search Modes

### Mode 1: Exhaustive Float64 Baseline

Purpose: fast deterministic numerical order-space exploration for small n.

Algorithm:

1. Build `radii = quadratic_radii(n)`.
2. Enumerate every canonical `index_order`.
3. Convert to `radius_order`.
4. Run `full_radius(radius_order)`.
5. Track the incumbent, ties within an explicit tolerance, and top-k records.
6. Recheck the incumbent and any tie candidates with `full_radius_mp` or root
   `verify.py`.
7. Emit a search summary artifact classified as `numerical_observation`.

This mode may say "exhaustively enumerated the canonical order space in
float64". It must not say "certified optimum".

### Mode 2: Exhaustive High-Precision Certification Candidate

Purpose: create the raw material for a finite computer certificate for very
small n.

Required additions before certification:

- a high-precision fixed-order function that returns an interval
  `[lower_infeasible, upper_feasible]`, not just one upper value;
- a search verifier that regenerates all canonical orders independently from
  `n`, recomputes or validates each interval, and checks
  `winner_upper <= every_nonwinner_lower`;
- explicit tie handling when intervals overlap;
- artifact evidence with `global_instance_claim` scope only when the verifier
  passes.

Until those additions exist, high-precision exhaustive output remains
high-confidence numerical evidence, not a certificate.

### Mode 3: Pruned Search Or Frontier Search

Purpose: extend beyond the n values where exhaustive full-order evaluation is
comfortable.

Candidate lower bounds may include:

- the adjacent-chain relaxation for the full order;
- adjacent-chain relaxations on induced subsequences after removing selected
  candidate floating indices;
- best-known incumbent upper bounds from pattern orders and heuristic search.

These lower bounds should be implemented only after recording the mathematical
proof obligation and verifier semantics. The upstream original-radii `lb3`
choice removed `{1}` and `{1, 2}`; the quadratic version must choose removal
sets explicitly, such as `{1^2}` and `{1^2, 2^2}`, or a documented general
candidate-floating policy. That decision is not a mechanical port.

## Data Structures

Proposed dataclasses:

```python
@dataclass(frozen=True)
class OrderSearchRecord:
    index_order: tuple[int, ...]
    radius_order: tuple[int, ...]
    R_chain: float
    R_full: float
    feasible: bool

@dataclass(frozen=True)
class SmallNSearchResult:
    n: int
    radius_sequence: tuple[int, ...]
    mode: Literal["exhaustive_float64", "exhaustive_mpmath", "pruned"]
    order_equivalence: Literal["rotation_reflection"]
    expected_canonical_count: int
    enumerated_count: int
    evaluated_full_count: int
    best: OrderSearchRecord
    ties: tuple[OrderSearchRecord, ...]
    top_records: tuple[OrderSearchRecord, ...]
    evidence_classification: str
```

`best` should store the index order as the primary identity. The corresponding
`FullResult` can remain an internal or optional payload because existing
fixed-order artifact code already knows how to serialize one order.

## Artifact Strategy

Do not overload the v1 fixed-order artifact as a global result. Add a future
search schema, for example `power-ringmin.small_n_search_result.v1`, with:

- explicit `problem` and `radius_sequence` metadata;
- `order_space` metadata: equivalence, canonicalization rule, expected count,
  enumerated count, and optional hash of canonical index orders;
- `search_method`: mode, backend, precision, tolerances, worker count, and
  randomness;
- `result`: best index/radius order, radius value, tie policy, top-k summary;
- `fixed_order_artifacts`: optional relative paths for winner/tie artifacts;
- `evidence`: classification, claim scope, checks, and limitations.

For review-grade runs, generate fixed-order artifacts for the incumbent and
ties with the existing exporter, then reference those paths from the search
artifact.

## CLI Shape

First implementation:

```powershell
python -m power_ringmin.search_small_n --n 6 --backend float64 --top-k 20 --output result.json
```

Likely options:

- `--n`: quadratic instance size, minimum 3;
- `--backend float64|mpmath`;
- `--digits`: high-precision digits when using `mpmath`;
- `--top-k`: number of best records to keep;
- `--tie-abs-tol` and `--tie-rel-tol`;
- `--output`: search summary JSON path;
- `--fixed-order-output-dir`: optional directory for incumbent/tie artifacts;
- `--created-at-utc`: deterministic tests and reproducibility;
- `--workers`: optional later parallel evaluation.

The first CLI should omit checkpointing and pruning. Those belong to a later
task after the baseline result contract is stable.

## Tests And Verification

Implementation tests should include:

- canonical counts for n = 3 through at least n = 8 equal `(n - 1)! / 2`;
- no two generated orders are rotation/reflection equivalent;
- every generated order is a permutation of indices `1..n`, starts with `n`,
  and satisfies the reflection breaker;
- `index_order_to_radius_order((4, 1, 3, 2)) == (16, 1, 9, 4)`;
- the n = 3 exhaustive search evaluates exactly one canonical order and agrees
  with `full_radius(quadratic_radii(3))`;
- rotation/reflection variants canonicalize to the same representative;
- search artifacts reject mismatched `n`, index order, and radius order;
- the CLI writes deterministic output on a tiny n fixture.

Verification for a design-only task is source inspection and documentation
review. Verification for the future implementation should include
`python -m pytest`, `python -m pytest tests/<new search tests>`, `git diff
--check`, and at least one direct CLI run on n = 3 or n = 4.

## Acceptance Criteria For First Implementation Task

A good first implementation is complete when it provides:

- canonical index-order enumeration and canonicalization;
- exhaustive float64 small-n search over quadratic radii;
- deterministic dataclass or JSON summary output;
- high-precision recheck for the incumbent, or a clearly deferred TODO if kept
  out of scope;
- tests for enumeration, conversion, exhaustive n = 3 behavior, and CLI output;
- documentation that output is a finite numerical observation, not a global
  certificate.

## Residual Risks

- Float64 ties may be artifacts of tolerance or near-degeneracy.
- Exhaustive enumeration grows as `(n - 1)! / 2`; the baseline should make the
  intended n range explicit.
- A future certified search needs interval lower bounds for every canonical
  order, not only a feasible upper bound for the winner.
- Pruned search lower bounds are promising, but not yet established in this
  repository as Power-Ringmin proof assets.
