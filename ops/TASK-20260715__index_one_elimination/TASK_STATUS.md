# TASK_STATUS - TASK-20260715__index_one_elimination / Exact Index-One Elimination

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove that deleting label \(1\) from a complete cyclic order
  leaves the exact maximum induced-subset product score unchanged, derive the
  core minimization and product-distance/geometric consequences, and verify
  every bounded core order and insertion for `n=3..8` exactly.
- **Expected output:** an all-order proof with the singleton, two-element, and
  two-core-neighbor cases explicit; exact bounded regression values and
  minimizer counts; synchronized proof note, roadmap, durable memory, current
  status, and dossier.

## Scope

- **In scope:** complete orders of `{1,...,n}` and core orders of `{2,...,n}`
  for `n>=3`; nonempty induced subsets; every canonical core order and every
  insertion gap for `n=3..8`; exact integer/`Fraction` arithmetic; proof,
  tests, roadmap, and durable memory.
- **Out of scope:** production algorithm or API changes; any enumeration past
  the existing `n<=8` cyclic-ratio boundary; product-distance implementation;
  interval backends, certificates, checked artifacts, schemas, examples, or
  certification claims; Git writes.

## Verified Facts

- Startup completed on clean `main` at `9f1239e`; the previous one-wrap task
  is committed and its proof/test foundation is available.
- The accepted theorem already identifies `Lambda(sigma)` with the maximum
  cyclic product sum over all nonempty subsets of the complete order.
- The existing same-order comparison proves
  `Lambda_same(tau) <= m W_same(tau)` for any cyclic order of `m` distinct
  positive labels.
- Exact elimination gives `Lambda(sigma) = K(tau)` for every complete order,
  independently of the insertion gap, and hence
  `Lambda_n = min_tau K(tau)`.
- The same-order comparison gives `Lambda_n <= (n-1) W_n`, and the strict
  global sandwich gives
  `R_2^*(n) < Lambda_n/pi <= (n-1) W_n/pi` for every `n>=3`.
- The bounded test checks 437 core classes and 2,957 insertions, covering all
  2,956 complete classes through `n=8`, with no failure.

## Assumptions / Inferences

- The intended core score `K(tau)` is the maximum induced cyclic product sum
  over all nonempty core subsets, using singleton squares and twice-counted
  two-element products.
- The finite regression is implementation evidence; the all-order result must
  be proved independently of enumeration.

## Decisions And Rationale

- Keep `K` and insertion helpers test-local; the request does not require a
  new production scorer or public contract.
- Treat `n=3` separately because its two-vertex core has two oriented arcs but
  only one rotation/reflection class after insertion.

## Plan And Expected Delta

- Audit the exact elimination proof and edge cases. COMPLETED.
- Add exact all-core/all-insertion tests on the existing bounded domain.
  COMPLETED.
- Synchronize the requested research and durable-memory files. COMPLETED.
- Run focused/full verification, independent review, and diff hygiene.
  COMPLETED.

## Verification

- **Checks:** focused and full pytest; checked-artifact semantic verification;
  targeted Ruff; Python compilation; independent proof, test, and
  documentation audits; final Git status, diff, and whitespace hygiene.
- **Observed result:** focused module passes 25 tests; all 2,957 insertion
  trials pass; full suite passes 198 tests; artifact verification accepts 4
  certificates and 76 local brackets; lint, compilation, independent audits,
  and diff hygiene pass.
- **Limitations:** hosted CI is outside this local task.

## Blockers / Risks

- No current blocker.
- The geometric consequence must remain an upper bound, not an exact optimum
  or matching asymptotic constant.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact theorem, bounded all-insertion regression,
  complete local verification, independent audits, final diff inspection, and
  synchronized durable sources.
- **Files changed:** proof note, test module, project brief, durable knowledge,
  roadmap, current status, and this dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
