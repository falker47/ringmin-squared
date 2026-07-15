# TASK_STATUS - TASK-20260715__lambda9_core_minimizer_classification / Lambda_9 Core Minimizer Classification

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** classify exactly every dihedral core order on
  \(\{2,\ldots,9\}\) with \(K=239\), count the corresponding complete
  minimizer classes through exact label-one elimination/insertion, and add an
  independent test-only oracle over all 2,520 core classes.
- **Expected output:** a human-checkable equality-case and shortcut-gain
  parametrization of the 28 core classes; the exact complete count 224; a
  literal 255-subset oracle recording every maximizing subset on every core
  class; synchronized proof, roadmap, project memory, current status, and
  dossier evidence.

## Scope

- **In scope:** the finite core set \(\{2,\ldots,9\}\); equality cases of the
  accepted \(S_6/S_5\) lemma; exact shortcut gains; placements of labels `2`
  and `3`; direct test-local generation of \(7!/2=2{,}520\) dihedral core
  classes; all 255 nonempty core subsets; exact integer arithmetic; insertion
  of label `1`; proof, tests, roadmap, durable memory, and task evidence.
- **Out of scope:** changing the production scorer or its public `n<=8`
  enumeration domain; enumerating all complete `n=9` orders in production;
  exact geometry, \(R_2^*(9)\), interval backends, certificates, checked
  artifacts, schemas, examples, all-`n` formulas, or asymptotic claims; Git
  writes.

## Verified Facts

- Startup completed on clean `main` at `849ff6b`; the accepted prior task
  proves \(\Lambda_9=239\) but explicitly leaves the minimizer classification
  open.
- Equality in the six-label lower lemma forces the induced \(S_6\) order,
  up to dihedral symmetry, to be `(9,5,8,6,7,4)`.
- In that orientation, label `3` must occupy one of the four gaps not incident
  to label `4`, and label `2` may then occupy any of the seven resulting gaps.
  This parametrizes 28 dihedral core classes.
- Exact label-one elimination makes all eight insertions into each minimizing
  core minimizing complete orders, giving 224 complete dihedral classes.

## Assumptions / Inferences

- The result is a finite exact combinatorial classification. It is not an
  exact geometric optimum, finite geometric certificate, or all-`n` theorem.
- The 2,520-class test-only core sweep is distinct from the production
  enumerator, whose public complete-order domain remains `3<=n<=8`.

## Decisions And Rationale

- Use the orientation `(9,5,8,6,7,4)` already present in the accepted
  shortcut-gain witness so that the placement rule is directly auditable.
- Generate the `n=9` core space directly inside the focused test module and
  score subsets literally, without calling repository canonicalizers, the
  public enumerator, or the production Karp scorer.
- Record all maximizing subsets in each oracle row, hard-code the 28 expected
  canonical minimizers, and lock the complete 2,520-row record with a
  deterministic checksum.

## Plan And Expected Delta

- Add the direct core generator and literal all-subset oracle. COMPLETED.
- Prove the equality-tail and placement classification. COMPLETED.
- Synchronize project and task memory. COMPLETED.
- Run focused/full verification and final diff hygiene. COMPLETED.

## Verification

- **Checks:** focused and full pytest; checked-artifact semantic verification;
  explicit schema-validation regression; targeted Ruff and Python compilation;
  independent mathematical/test/documentation audits; final Git status, diff,
  whitespace scan, and `git diff --check`.
- **Observed result:** the focused module passes all 28 tests and the complete
  repository suite passes all 201 tests. Explicit schema validation passes 4
  tests; checked-artifact semantic verification accepts 4 certificates, 76
  local brackets, and the `n=3..6` summary. Targeted Ruff, compilation, final
  diff inspection, changed-file whitespace scanning, and `git diff --check`
  pass. Independent mathematical, oracle, and documentation audits agree with
  the proof, list, checksum, and stated boundaries. The new oracle covers
  2,520 core classes, 642,600 literal subset evaluations, the exact 28
  minimizers, and every maximizing-subset record.
- **Limitations:** hosted GitHub Actions is outside the local worktree unless a
  specific run is independently inspected.

## Blockers / Risks

- No current blocker.
- The coincident number 2,520 must not be described as an enlarged public
  `n=9` complete-order enumeration.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the equality/placement proof and independent
  2,520-core oracle agree exactly; all 28 focused tests and all 201 repository
  tests pass locally, with final diff hygiene clean.
- **Files changed:** proof note, focused test, project brief, durable
  knowledge, current status, roadmap, and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
