# High-Precision Interval Verifier Semantics For Finite Small-n Certification

Date: 2026-07-11

Status update, 2026-07-14: this file is retained as the historical design
record. The local verifier, finite small-\(n\) aggregation, and checked
\(n=3,4,5,6\) artifacts were implemented after it was written. The proof
obligations in the section below are now discharged authoritatively by
`research/FIXED_ORDER_ANGULAR_STN.md`, which sharpens the verified bracket
notation to \((L,U]\). Statements below about a future implementation or the
absence of checked global brackets describe the 2026-07-11 design state, not
current project status. Checked global brackets now exist, but no exact
geometric threshold value is certified.

## Scope And Classification

This document is a design artifact for a future implementation task. It
establishes no certified quadratic-radii optimum, no theorem for all n, and no
production certificate.

- DEFINITION: a finite small-n interval certificate is a machine-checkable
  artifact for one explicit quadratic-radii instance `(1^2, 2^2, ..., n^2)`.
- DEFINITION: the certificate scope is the finite cyclic-order space modulo
  rotation and reflection for that one n.
- DESIGN DECISION: a `computer_certified_result` claim may be made only after
  an independent verifier regenerates the canonical order space and verifies
  interval lower and upper evidence for every canonical order.
- DESIGN DECISION: ordinary high-precision decimal recomputation, including
  current `mpmath` bisection, remains `numerical_observation` unless the
  verifier uses outward interval enclosures and strict sign checks.
- UNRESOLVED CLAIM: no small-n global optimum has yet been interval-certified
  in this repository.

## Existing Foundation

The current repository already has the numerical foundation:

- `src/power_ringmin/search_small_n.py` regenerates canonical quadratic index
  orders modulo rotation and reflection.
- `src/power_ringmin/evaluator.py` implements the float64 all-pairs STN
  fixed-order evaluator.
- `src/power_ringmin/highprec.py` and root `verify.py` implement high-precision
  fixed-order feasibility checks with `mpmath`.
- Current small-n artifacts are deliberately classified as
  `numerical_observation`.

The missing certification layer is not "more digits" alone. It is a semantic
contract for interval arithmetic, strict feasible/infeasible endpoint proofs,
and global finite-order aggregation.

## Proof Obligations

The verifier design depends on several local proof obligations. They should be
recorded in code comments, schema docs, or a proof note when implemented.

- PROOF OBLIGATION: for positive radii `a,b` and positive central radius `R`,
  the angular constraint
  `theta_R(a,b) = 2 asin(sqrt(a*b / ((R+a)*(R+b))))`
  is the exact minimum angular separation for two peripheral circles tangent
  to the central circle.
- PROOF OBLIGATION: for positive `a,b`, `theta_R(a,b)` is strictly decreasing
  in `R`.
- PROOF OBLIGATION: for one fixed cyclic order, all-pairs angular constraints
  are equivalent to the corresponding STN feasibility problem.
- PROOF OBLIGATION: an STN is infeasible if and only if it has a negative
  directed cycle.

These are elementary mathematical facts, but this design does not promote them
to established project theorems.

## Fixed-Order STN Semantics

For a fixed radius order `r_0, ..., r_{m-1}`, use angular variables
`p_0, ..., p_{m-1}` with `p_0 = 0` and the order interpreted
counterclockwise.

For each pair `0 <= i < j < m`, let `theta_ij = theta_R(r_i, r_j)` and
`tau = 2*pi`. The fixed-order constraints are:

```text
p_j - p_i >= theta_ij
p_j - p_i <= tau - theta_ij
```

Use directed STN edges in the same orientation as the current implementation:

```text
lower edge: j -> i with weight -theta_ij
upper edge: i -> j with weight tau - theta_ij
```

The verifier should name these edge kinds explicitly, for example
`forward_lower` and `wrap_upper`, and should never depend on an implicit edge
ordering in a serialized artifact.

## Interval Angular Oracle

For each requested `(R, a, b)`, the interval layer must return certified
decimal/rational endpoints:

```text
theta_lower <= theta_R(a,b) <= theta_upper
tau_lower <= 2*pi <= tau_upper
```

Required semantics:

- The endpoints must be outward enclosures produced by a documented interval
  backend or by exact rational bounds.
- The artifact must record the backend, precision, rounding policy, and source
  files used to produce the intervals.
- The independent verifier must recompute or validate these intervals. It must
  not trust only stored endpoint values.
- A backend that cannot guarantee outward rounding may be used for exploration
  only; artifacts depending on it remain `numerical_observation`.

## Certified Feasible Upper Endpoint

For one fixed order, a radius `U` is a certified feasible upper bound only if
the verifier checks an explicit witness placement.

The witness should be exact decimal/rational angles `p_i`, with `p_0 = 0`.
For every pair `i < j`, the verifier computes interval upper bounds
`theta_upper(i,j,U)` and a lower bound `tau_lower`, then checks:

```text
p_j - p_i - theta_upper >= 0
tau_lower - theta_upper - (p_j - p_i) >= 0
```

If positions are stored as intervals rather than exact decimals, the verifier
must use the lower bound of each slack interval. Acceptance requires all slack
lower bounds to be nonnegative. Prefer a positive minimum slack in generated
certificates so serialization and backend changes do not sit exactly on zero.

Interpretation:

- VERIFIED FACT after verifier acceptance: the fixed order is feasible at `U`.
- COMPUTER-CERTIFIED RESULT, local scope: the true fixed-order optimum is at
  most `U`.

## Certified Infeasible Lower Endpoint

For one fixed order, a radius `L` is a certified infeasible lower bound only if
the verifier checks a negative cycle in a deliberately relaxed STN.

Use the relaxed interval weights:

```text
lower edge upper weight = -theta_lower(i,j,L)
upper edge upper weight = tau_upper - theta_lower(i,j,L)
```

The artifact should include an explicit directed cycle:

```text
[(node_0, node_1, edge_kind_0), ..., (node_k, node_0, edge_kind_k)]
```

The verifier recomputes each edge upper weight and accepts the lower endpoint
only when the interval upper bound for the total cycle weight is strictly
negative:

```text
cycle_weight_upper < 0
```

This proves even the relaxed STN is infeasible; therefore the true STN is
infeasible at `L`. By monotonicity of `theta_R`, every radius `R <= L` is also
infeasible for that fixed order.

Interpretation:

- VERIFIED FACT after verifier acceptance: the fixed order is infeasible at
  `L`.
- COMPUTER-CERTIFIED RESULT, local scope: the true fixed-order optimum is at
  least `L`.

## Fixed-Order Interval Bracket

A fixed-order interval record should contain:

```text
index_order
radius_order
lower_radius_decimal
upper_radius_decimal
lower_certificate: negative_cycle
upper_certificate: witness_positions
theta_interval_backend
min_upper_witness_slack_lower
lower_negative_cycle_sum_upper
```

Acceptance requires:

- the index order is canonical;
- the radius order equals the quadratic square of the index order;
- `0 < lower_radius_decimal <= upper_radius_decimal`;
- the lower endpoint has a verified negative cycle;
- the upper endpoint has a verified witness;
- the verifier reports no tolerance-based acceptance.

If either endpoint is undecidable because interval signs overlap zero, the
record is not certified. The generator should increase precision, widen the
bracket, or improve the witness/cycle.

## Global Finite Small-n Certificate

For one n, the global verifier must:

1. Regenerate all canonical index orders from n.
2. Confirm the certificate has exactly one fixed-order interval record for
   every canonical order.
3. Verify every fixed-order interval record independently.
4. Compute:

```text
global_lower = min(order.lower_radius for all orders)
global_upper = min(order.upper_radius for all orders)
candidate_orders = {order | order.lower_radius <= global_upper}
excluded_orders = {order | order.lower_radius > global_upper}
```

5. Confirm all claimed global fields match the verifier-computed values.

The weakest certified global claim is:

```text
R_2^*(n) is in [global_lower, global_upper].
```

This can be classified as `computer_certified_result` only for the finite
instance n, provided every local record verifies.

## Winner And Tie Semantics

The certificate should separate value brackets from winner claims.

- Certified interval only: the artifact proves
  `R_2^*(n) in [global_lower, global_upper]`.
- Certified unique winner: one canonical order `w` may be called uniquely best
  only when
  `upper_radius(w) < lower_radius(o)` for every other canonical order `o`,
  with a strictly positive interval-certified separation gap.
- Certified candidate set: if multiple orders satisfy
  `lower_radius <= global_upper`, the artifact may claim only that every
  optimizer lies inside that candidate set, and every excluded order is not
  optimal.
- Exact tie claims require additional equality or overlap semantics and should
  be deferred.

The first certification implementation should target either an interval-only
claim or a unique-winner claim for the smallest n where the separation gap is
easy to verify.

## Artifact Strategy

Do not overload `power-ringmin.small_n_search_result.v1`, because that schema
is intentionally numerical. Add a future schema such as:

```text
power-ringmin.small_n_interval_certificate.v1
```

Required top-level sections:

- `problem`: project, radius model, dimension, and all-pairs constraints.
- `instance`: n and explicit quadratic radius sequence.
- `order_space`: canonicalization rule, equivalence, expected count, and an
  optional hash of the regenerated canonical order list.
- `interval_semantics`: angular oracle, interval backend, rounding policy,
  pi/tau enclosure, and no-tolerance acceptance policy.
- `fixed_order_bounds`: one verified bracket record per canonical order.
- `global_claim`: finite instance scope, global lower/upper bounds, winner or
  candidate set, and exclusion gap when present.
- `provenance`: repository, software, source files, commands, randomness.
- `evidence`: classification, claim scope, checks, and limitations.

Recommended evidence scope:

```text
finite_exhaustive_interval_order_search
```

The artifact should reject `computer_certified_result` unless all fixed-order
records are verified and the order-space regeneration check passes.

## Independent Verifier Algorithm

The future verifier should be separate from the generator. It may share small
pure helpers such as canonical order generation only if those helpers are
simple, tested, and included in provenance.

Verifier outline:

1. Parse JSON and validate decimal strings without converting them to binary
   floats.
2. Regenerate canonical index orders for n.
3. Match artifact records against the regenerated order set.
4. For each record, recompute interval theta enclosures at `L` and `U`.
5. Check the lower negative cycle with relaxed edge upper weights.
6. Check the upper witness with strict all-pairs slack lower bounds.
7. Compute global lower/upper and winner/candidate/exclusion fields.
8. Compare computed values with claimed values.
9. Exit nonzero on missing orders, duplicate orders, noncanonical orders,
   invalid interval signs, tolerance-only evidence, or mismatched claims.

The verifier output should be concise but include enough detail to audit:

```text
small_n_interval_certificate=PASS n=... orders=... global=[L,U] candidates=...
```

Failures should identify the order and endpoint that failed.

## Precision And Rounding Policy

Certification must be based on signs of interval quantities, not configured
STN tolerances.

Allowed:

- using high precision to make interval signs decisive;
- widening a bracket so witness slacks and cycle negativity are separated from
  zero;
- recording diagnostic tolerances for exploratory generators.

Not allowed for `computer_certified_result`:

- accepting `margin >= -tol` as proof;
- accepting a witness with negative interval slack because it is "small";
- accepting a negative cycle whose interval sum contains zero;
- relying on float64 order rankings for global exclusion.

The implementation may still use current float64 or `mpmath` code to propose
orders, witnesses, and brackets. The independent interval verifier is the
authority for certified claims.

## Tests For The Future Implementation

Focused tests should include:

- interval theta enclosures contain ordinary high-precision theta values on
  small fixtures;
- feasible witness verification accepts a known n=3/n=4 upper endpoint with
  positive slack;
- infeasible lower verification accepts a hand-inspected negative cycle;
- mutating one witness angle, one cycle edge, one radius, or one index order
  makes verification fail;
- missing, duplicate, or noncanonical order records fail global validation;
- global unique-winner and candidate-set semantics are computed from intervals,
  not copied from artifact claims;
- `computer_certified_result` is rejected when any local endpoint is undecided;
- current numerical small-n artifacts remain `numerical_observation`.

Full verification for the implementation should include `python -m pytest`,
direct CLI runs for the smallest certified fixture, `git diff --check`, and a
task-dossier evidence record with the exact command output.

## Acceptance Criteria For The Next Implementation Task

A good first implementation task is complete when it provides:

- an interval angular oracle with documented outward-enclosure semantics;
- a fixed-order interval verifier for one bracket record;
- tests for feasible upper and infeasible lower endpoint semantics;
- a clear refusal path for tolerance-only or undecidable evidence;
- no global certificate claim yet unless every canonical order for a tiny n is
  covered by verified records.

The first implementation may target local fixed-order brackets before global
small-n aggregation. That is the smallest safe step toward certification.

## Residual Risks

- Python interval libraries vary in their guarantees for transcendental
  functions; the chosen backend must be documented carefully.
- Negative-cycle certificates near zero may be fragile and should be generated
  with deliberate separation.
- Witness positions recovered from STN closure may sit on tight constraints;
  the generator may need to use `U + eta` for a clean feasible witness.
- A finite certified result for n remains finite only. It is not a theorem for
  all n and must not be used as asymptotic evidence without that limitation.
