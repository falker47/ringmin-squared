# TASK_STATUS - TASK-20260718 / Canonical 8/25 Core-Order K

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine exactly the induced-subset objective K for the
  canonical eight-twenty-fifths core order on its entire public domain,
  classify all maximizing subsets, and transfer the result to Lambda and the
  geometric sandwich.
- **Expected output:** an all-parameter shortcut/block proof, exact formula,
  bounded independent local diagnostic, synchronized authoritative notes, and
  complete verification evidence.

## Scope

- **In scope:** the symbolic core order and its fourteen explicit initial
  rows; shortcut gains; exact block sums; unique maximizing subsets; the
  consequences for fixed-order and global Lambda and geometric bounds.
- **Out of scope:** modifying production or tests, enumerating subsets or
  permutations, proving global optimality of the core order, or proving
  convergence/exact geometric leading constants.

## Verified Facts

- The repository was clean at startup on main at
  `1ec6e0b7fca85b9ed1bb81636c87934564994e97`.
- On symbolic rows, with d=4v+e and n=5v+e-1, the unique maximizer is the
  tail from 2v+1; connector 2v+2 is additionally omitted exactly for
  e=6,7,8.
- The exact formula (K825-4) has leading term 143 n^3 / 500.
- The fourteen explicit public rows have the unique maximizing tails and
  exact K values recorded in the proof note.
- The bounded independent diagnostic passes n=9..120 using max-plus paths
  and oriented shortcut budgets and checks the direct score formula through
  n=1000, without subset or permutation enumeration.

## Assumptions / Inferences

- Cyclic rotation and reflection leave K invariant, so the public generator's
  displayed cut does not affect the theorem.
- The current lower coefficient C_AF is used only through its already-proved
  authoritative theorem.

## Decisions And Rationale

- Use a general isolated-hole shortcut-budget lemma so one symbolic proof
  controls every subset simultaneously.
- Treat the ten r=0 symbolic rows, the single generic inequality exception
  n=47, and the fourteen explicit rows by exact bounded local margins only.
- Keep the diagnostic dossier-local and standard-library-only; no production
  API is required by the theorem.

## Plan And Expected Delta

- Add the exact theorem and proof to
  `research/FIXED_ORDER_CYCLE_RATIO.md`.
- Cross-reference the sharper consequence from the construction and lower-
  bound notes; synchronize `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, and the roadmap.
- Add only `exact_diagnostic.py` as executable diagnostic scope.

## Verification

- **Checks:** exact diagnostic; Ruff lint/format; full pytest; checked-artifact
  verifier; focused schema tests; strict Markdown/source structure; three
  independent read-only audits; complete diff inspection; `git diff --check`.
- **Observed result:** all final checks pass. The diagnostic covers 112 full
  certificate rows, 8,495,284 max-plus transitions, 561,568 oriented arcs,
  and 880 further formula-only rows; pytest passes 283 tests; four checked
  certificates and 76 local brackets verify; four schema tests pass; all 26
  K825 tags are unique.
- **Limitations:** bounded computation corroborates the written infinite-
  parameter proof and does not replace it.

## Blockers / Risks

- No blocker. The result remains construction-specific and does not close the
  global coefficient gap or classify global minimizers.

## Next Atomic Action

- User manual review and commit decision.

## Handoff

- **Last verified result:** final diagnostic, full regressions, artifact/schema
  checks, independent audits, source structure, status/diff inspection, and
  diff hygiene all PASS.
- **Files changed:** authoritative research/status notes plus this four-file
  dossier; no production or test path.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`, then
  `EVIDENCE.md`.
