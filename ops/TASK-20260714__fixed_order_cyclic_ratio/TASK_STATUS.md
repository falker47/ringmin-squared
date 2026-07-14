# TASK_STATUS - TASK-20260714__fixed_order_cyclic_ratio / Fixed-Order Cyclic Ratio

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** formalize the exact maximum cyclic ratio of the complete
  fixed-order STN, prove its two-sided relation to the fixed-order and global
  geometric thresholds, implement an exact scorer, and test the bounded
  `n=3..8` prediction independently.
- **Expected output:** one authoritative proof note; one exact `Fraction`
  scorer using a documented polynomial dynamic program; a test-only simple
  cycle oracle; bounded exhaustive results for `n=3..8`; synchronized durable
  memory; complete local verification.

## Scope

- **In scope:** complete orders of `{1,...,n}` with `n>=3`; exact STN edge
  multiplicities; the quantities `q(C)`, `S(C)`, `Lambda(sigma)`, and
  `Lambda_n`; fixed-order and global sandwiches; endpoint strictness;
  comparison with the distinct core surrogate `W`; exact bounded canonical
  enumeration through `n=8`; tests, documentation, and durable memory.
- **Out of scope:** interval backends; interval verifiers; certificates,
  checked artifacts, examples, or schemas; order enumeration beyond `n=8`;
  a general formula for `Lambda_n`; a new asymptotic constant; unrelated lint
  cleanup; Git writes.

## Verified Facts

- Mandatory startup sources, relevant prior task memory, both source proof
  notes, current order enumerators, exact surrogate code, tests, workflow, and
  initially clean Git status were inspected.
- The exact definition counts every edge occurrence. Every closed walk has
  `q>=1`, and closed-walk decomposition reduces the maximum ratio to simple
  cycles.
- The requested weak sandwich is proved, together with the stronger strict
  form and the exact global additive relation
  `0 < Lambda_n - pi*R_2^*(n) < pi*n^2`.
- The production descending-path/Karp scorer is exact, float-free, and
  independent of direct cycle enumeration. The global enumerator rejects
  `n>8` and insufficient work ceilings before permutation generation.
- Exact bounded enumeration reproduces `(12,26,47,77,118,172)` on all 2,956
  canonical complete orders, with no counterexample.
- The proof and finite examples distinguish the full-order cycle score
  `Lambda` from the core regular-direction pair score `W`.

## Assumptions / Inferences

- The theorems use only the exact real-arithmetic fixed-order STN semantics and
  angular comparisons already proved in the cited research notes.
- Existing checked artifacts retain their separate guarded `mpmath.iv` trust
  premise; this task neither strengthens nor weakens it.

## Decisions And Rationale

- Use descending-path compression and Karp's maximum-cycle-mean formula in
  production; keep direct simple-cycle enumeration solely as an independent
  small-test oracle.
- Reuse the existing canonical full-order convention while imposing a new
  hard `3<=n<=8` boundary and explicit 2,520-order ceiling.
- Record the strict endpoint refinement while displaying the requested weak
  sandwich explicitly.
- Compare `Lambda` and `W` only after stating their different full/core domains
  and objectives; do not infer all-`n` behavior from the finite table.
- Preserve four repository-wide Ruff findings in unrelated committed files
  rather than mixing a lint-cleanup task into this bounded research change.

## Plan And Expected Delta

- Write the exact proof and algorithm note. COMPLETED.
- Implement the scorer, bounded enumerator, and independent tests. COMPLETED.
- Run and record the bounded `n=3..8` experiment. COMPLETED.
- Synchronize authoritative memory and run complete verification, lint, and
  hygiene. COMPLETED.

## Verification

- **Checks:** production experiment; test-only simple-cycle oracle; focused
  and integrated pytest; full pytest; Python compilation; task-scoped and
  repository-wide Ruff; checked-artifact semantic verifier; schema tests;
  independent mathematical/algorithm/implementation/documentation audits;
  final text, path, diff, and Git hygiene.
- **Observed result:** exact values and counts match the supplied prediction;
  21 focused, 82 integrated, and 194 full tests pass; compilation and
  task-scoped Ruff pass; 4 certificates, 76 local brackets, the finite summary,
  and all 4 schema tests verify; independent reviews pass. Repository-wide
  Ruff reports four pre-existing F401/F841 findings in three untouched files.
- **Limitations:** hosted CI was not run; the global Ruff baseline remains
  non-clean for findings outside this task.

## Blockers / Risks

- No current blocker.
- The finite `n=3..8` table must remain a finite exact computation, not an
  all-`n` formula or an asymptotic conjecture promoted to theorem.
- A `Lambda`-maximizing cycle need not be a critical exact-STN cycle at the
  geometric threshold.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** theorem, implementation, bounded experiment,
  authoritative synchronization, complete local tests, task-scoped lint,
  artifact verification, independent reviews, and final hygiene pass.
- **Files changed:** one proof note; one source module; one test module;
  synchronized project brief, durable knowledge, source STN note, roadmap,
  current status; and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `src/power_ringmin/fixed_order_cycle_ratio.py`,
  `tests/test_fixed_order_cycle_ratio.py`, and this dossier.
