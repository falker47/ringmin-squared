# TASK_STATUS - TASK-20260715__lambda10_label3_insertion_gap_classification / Lambda_10 Label-Three Insertion-Gap Classification

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** classify exactly which gaps in the two proved `n=10`
  seven-label equality cycles can retain partial induced-subset score at most
  323 after label `3` is inserted, while leaving label `2` unplaced.
- **Expected output:** an exact insertion formula and shortcut-gain proof for
  all 14 gaps; a separate independent test-only oracle over all 255 nonempty
  subsets of each inserted order; synchronized authoritative memory; no
  production or public-boundary change.

## Scope

- **In scope:** the cycles `(10,4,7,8,6,9,5)` and
  `(10,5,9,4,7,8,6)`; insertion of label `3` into each of their seven
  labelled gaps; the partial score over labels `3..10`; exact argmax subsets;
  proof, tests, authoritative summaries, and this dossier.
- **Out of scope:** placing label `2`; claiming that every surviving partial
  order extends to a minimizing full core; enumerating, classifying, or
  counting all `n=10` core minimizers; production scorer, API, canonicalizer,
  or public-limit changes; geometry, artifacts, schemas, all-`n` formulas,
  asymptotics, or Git writes.

## Verified Facts

- Startup completed on a clean worktree at `db881793a438`.
- The accepted seven-label equality classification leaves exactly the two
  displayed cycles.
- The exact insertion formula is
  \(\Delta_3(a,b)=3(a+b)-ab=9-(a-3)(b-3)\).
- The first equality cycle has partial score 326 on `{4,7}` and 323 on every
  other gap. The second has score 326 on `{4,9}`, 328 on `{4,7}`, and 323 on
  every other gap.
- Complete shortcut-gain certificates prove all 14 values and every argmax;
  no subset sweep is used in the proof.
- Independent test-only arithmetic checks all 14 orders and all 255 nonempty
  subsets of each, for 3,570 literal subset evaluations.

## Assumptions / Inferences

- The partial score on labels `3..10` is a necessary obstruction for any
  later full-core extension, not a sufficient extension theorem.
- Exhaustive subset arithmetic will audit the proof but will not supply it.

## Decisions And Rationale

- Write the partial score as `K_{>=3}` so it cannot be confused with the
  existing full-core `K` before label `2` is placed.
- Record every partial argmax because it is the required input to a possible
  later label-two task.
- Keep structural shortcut checks and literal subset enumeration in separate
  test functions.

## Plan And Expected Delta

- Add the exact insertion and shortcut-gain proof. COMPLETED.
- Add independent structural and exhaustive test-only checks. COMPLETED.
- Synchronize only the authoritative summaries required by the result.
  COMPLETED.
- Run proportional verification and final diff hygiene. COMPLETED.

## Verification

- **Checks:** focused/module/full pytest, checked-artifact regressions, Ruff,
  compilation, three independent mathematical/test/documentation audits, and
  final Git/diff/whitespace/scope inspection.
- **Observed result:** focused tests pass 2/2, the cyclic-ratio module passes
  33/33, and the complete suite passes 209/209 after an initial sandbox-only
  temporary-directory permission failure was rerun successfully. Schema
  validation passes 4/4; the semantic verifier accepts 4 certificates and 76
  local brackets; Ruff, compilation, and all three independent audits pass.
  The complete diff, whitespace, scope, staged state, production boundary,
  and task-created temporary paths also pass final inspection.
- **Limitations:** local execution used Python 3.14.3. Python 3.11
  compatibility was audited statically but not executed locally. Hosted CI
  was not run or independently inspected.

## Blockers / Risks

- No current blocker.
- A surviving gap must not be described as a proved full-core minimizer before
  label `2` is analyzed.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact structural proof, separate 14-by-255 oracle,
  full local suite, artifact regressions, lint, compilation, and three
  independent audits pass; final diff and worktree hygiene also pass.
- **Files changed:** proof note, focused test module, project brief, durable
  knowledge, roadmap, current status, and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
