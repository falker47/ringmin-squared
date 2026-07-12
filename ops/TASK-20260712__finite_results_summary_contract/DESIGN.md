# DESIGN - Finite Results Summary Contract

## Decision

Create a separate derived artifact contract:

```text
power-ringmin.finite_results_summary.v1
```

Do not mutate `power-ringmin.small_n_interval_certificate.v1` in this task.

## Primary Certificate Versus Derived Analysis

- Primary certificates record finite global interval evidence for one `n`: canonical order-space coverage, embedded local interval brackets, verified lower endpoints, feasible upper endpoints, provenance, and certificate evidence.
- The finite-results summary records derived analysis across already checked certificates: candidate sets, excluded-order counts, exclusion gaps, identical serialized bracket groups, and exploratory finite-`n` ratios.
- The summary is not a replacement for source certificates. Its validator must reload and semantically revalidate every source certificate through the existing certificate loader.

## Candidate-Set Semantics

- For one checked source certificate, let `U` be the verified global feasible upper endpoint.
- For each canonical order `sigma`, let `L_sigma` be that order's verified strict lower endpoint from the source certificate.
- The candidate set is `C = {sigma : L_sigma <= U}`.
- Candidate-set membership is a computer-certified finite conclusion under the same backend contract as the source certificate, because it uses verified source lower endpoints and the verified global upper endpoint.
- Candidate-set size `1` means a unique certified candidate modulo the current rotation/reflection canonicalization convention.

## Exclusion-Gap Semantics

- An order with `L_sigma > U` is certified excluded from global optimality under the checked finite certificate semantics.
- If at least one order is excluded, the exclusion gap is `min(L_sigma - U)` over excluded orders.
- The exclusion gap is computer-certified only when recomputed from verified source lower bounds and the verified global upper bound.
- If no order is excluded, the exclusion gap is `null` and must not be encoded as zero.

## Multiple Candidate Orders

- Multiple candidates mean the current source brackets do not exclude those orders.
- Multiplicity is not an exact tie theorem.
- The artifact must carry an explicit warning/classification for multiple candidate sets.

## Identical Serialized Brackets

- Identical serialized lower/upper bracket strings may be grouped as a derived representation fact.
- Such groups do not prove exact equality of fixed-order optima.
- The validator must treat identical serialized brackets as string identity plus source validation, not as a mathematical equality theorem.

## Evidence Classifications

- Candidate-set membership: `computer_certified_result`.
- Excluded-order count and exclusion gap, when present: `computer_certified_result`.
- Identical serialized bracket groups: `verified_fact` about the serialized checked sources, with an explicit no-exact-equality warning.
- Ratios to `n^3/(6*pi)`: `numerical_observation`.
- Trends across `n=3..6`: `empirical_pattern`.
- Limitations and open scope statements: `unresolved_claim` where they mention absent exact/all-`n`/asymptotic results.

## Provenance Requirements

- Each source certificate entry records the relative path, artifact type, schema version, `n`, source provenance commit/dirty flag, and a SHA-256 hash of the exact source artifact bytes used for generation.
- The summary records its own generation provenance, including generator name, command or API call summary, repository state, relevant source files, software, and no randomness.
- Semantic validation must recompute source hashes, reload source certificates, rederive every summary value, and reject stale summaries when a source artifact hash or relevant certificate content differs.

## Migration And Compatibility

- `power-ringmin.small_n_interval_certificate.v1` remains the strict primary evidence contract.
- No certificate schema version bump is made because candidate sets, exclusion gaps, bracket groups, cross-`n` comparisons, and asymptotic ratios are derived analysis rather than primary per-certificate evidence.
- Existing checked certificate artifacts remain compatible and unchanged.
- The prior task-scoped summary format `power-ringmin.task_scoped_finite_results_summary.v1` is superseded for durable checked examples by `power-ringmin.finite_results_summary.v1`.
