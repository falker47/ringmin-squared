# TASK_STATUS - TASK-20260715__lambda9_exact_finite_value / Exact Finite Value of Lambda_9

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove the finite exact value \(\Lambda_9=239\) from the
  accepted reduction \(\Lambda_9=\min_\tau K(\tau)\), without enlarging the
  public enumerator.
- **Expected output:** a human-checkable six-label lower-bound lemma; an
  independent test-only oracle over the 60 dihedral classes; an exact witness
  verification with every maximizing subset recorded; synchronized proof,
  roadmap, current status, and task evidence.

## Scope

- **In scope:** cyclic orders induced on \(S_6=\{4,\ldots,9\}\) and
  \(S_5=\{5,\ldots,9\}\); the core order
  \((9,2,3,5,8,6,7,4)\); exact integer subset scoring; proof, tests,
  roadmap, current status, and this dossier.
- **Out of scope:** expanding or changing the production enumerator; public
  API or scorer changes; exact geometry, \(R_2^*(9)\), all-\(n\) formulas,
  asymptotic claims, certificates, schemas, examples, or Git writes.

## Verified Facts

- Startup completed on a clean worktree.
- The accepted index-one theorem gives
  \(\Lambda_9=\min_\tau K(\tau)\).
- The finite six-label lemma proves
  \(\max\{P_\omega(S_6),P_\omega(S_5)\}\ge239\) for every cyclic order
  \(\omega\) on \(S_6\).
- The supplied core witness has exact score 239 and unique maximizing subset
  \(S_6\), so the accepted reduction gives \(\Lambda_9=239\).
- Test-only literal enumeration checks all 60 six-label classes and all 255
  witness subsets without calling the public enumerator or production scorer.

## Assumptions / Inferences

- The result must remain classified as a finite exact combinatorial fact,
  not a geometric or all-\(n\) theorem.

## Decisions And Rationale

- Keep both new enumerations test-only and independent of the public
  canonical enumerator and production Karp scorer.
- Do not update `start.md`, `PROJECT_KNOWLEDGE.md`, production source, or any
  checked artifact because the user limited the delta to proof, test,
  roadmap, status, and necessary dossier files.

## Plan And Expected Delta

- Formalize the six-label lower-bound lemma. COMPLETED.
- Add the 60-class oracle and 255-subset witness regression. COMPLETED.
- Synchronize the proof note, roadmap, status, and dossier. COMPLETED.
- Run focused/full verification and final diff hygiene. COMPLETED.

## Verification

- **Checks:** focused and full pytest; checked-artifact semantic verification;
  targeted Ruff; Python compilation; independent mathematical, test, and
  documentation audits; final Git status, diff, and whitespace hygiene.
- **Observed result:** all 27 focused and all 200 repository tests pass; the
  60-class and 255-subset checks pass; artifact verification accepts 4
  certificates and 76 local brackets; lint, compilation, audits, and diff
  hygiene pass.
- **Limitations:** hosted CI is outside this local task.

## Blockers / Risks

- No current blocker.
- A finite exact value of \(\Lambda_9\) must not be described as an exact
  geometric value or extrapolated beyond \(n=9\).

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** finite proof, independent bounded oracles, full
  local verification, independent audits, and final hygiene pass.
- **Files changed:** proof note, focused test module, roadmap, current status,
  and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
