# TASK_STATUS - TASK-20260714__global_surrogate_classification / Global Surrogate Classification

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** combine the exact `n=3..11` table with the residue-class
  theorem for `n>=9` and prove
  \(W_n^{(\le2)}=B_n=W_n\) for every \(n\ge3\).
- **Expected output:** a self-contained global consequence in the primary
  proof note; coherent project memory and roadmap; corrected Ruff provenance;
  unchanged tests green; no new generator, residue formula, enumeration,
  artifact, or STN documentation.

## Scope

- **In scope:** the already verified bounded table, the accepted residue-class
  formula, their overlapping-domain cover, the distinction between objective
  and minimizer-set equality, one unused test assignment, requested durable
  documentation, and reproducible default Ruff evidence.
- **Out of scope:** changing generators or residue formulas; extending
  canonical enumeration; adding artifacts, schemas, CLIs, certificates, or
  STN documentation; geometric-optimum claims; Git writes or upstream changes.

## Verified Facts

- The mandatory startup files, relevant predecessor dossiers, primary proof,
  exact source/tests, requested research notes, and initially clean worktree
  were inspected.
- The finite theorem covers `3<=n<=11`; the residue-class theorem covers
  every `n>=9`. Their union is every `n>=3`.
- The unused assignment is in the test helper for terminal-high boundary
  arithmetic; the identically named production assignment is used.
- The primary proof and requested project memory now state the global theorem,
  the all-\(q\ge2\) value corollary, the all-\(n\) minimizer inclusion, and the
  correctly bounded open minimizer-set question.
- The unused test assignment was removed; no generator or residue formula was
  changed.
- Three independent final audits pass the mathematics, cross-document
  consistency, and exact two-file Ruff provenance.

## Assumptions / Inferences

- None. The global objective equality is a direct logical consequence of two
  accepted exact results, not a finite extrapolation.

## Decisions And Rationale

- State the domain-cover proof explicitly and retain the exact evidence labels
  of its two ingredients.
- Keep the minimizer-set conclusion bounded to `3<=n<=11`; for `n>=12`, ask
  only whether distances at least three remove some distance-two minimizers.

## Plan And Expected Delta

- Complete independent mathematical, documentation, and Ruff audits.
  COMPLETE.
- Patch the proof note, requested durable memory, finite-results warning, and
  the unused test assignment. COMPLETE.
- Run default Ruff without ignores, focused and full tests, checked-artifact
  verification, text/proof hygiene, and complete diff inspection. COMPLETE.
- Record exact command evidence and set `READY_FOR_REVIEW`. COMPLETE.

## Verification

- **Checks:** default Ruff rules with no ignores on the explicit two-file
  provenance scope; focused and full pytest; checked-artifact semantic
  verification; three independent final audits; strict UTF-8, line endings,
  tabs, trailing whitespace, math delimiters, proof tags, changed-path scope,
  complete diff, and `git diff --check`.
- **Observed result:** Ruff `0.11.12` without ignores reports
  `All checks passed!`; focused tests `41/41`; full suite `169/169`; checked
  artifacts accept 4 certificates, 76 local brackets, and summary values
  `3,4,5,6`; all audits and final hygiene PASS on ten intended paths after
  aligning the proposed next task with the existing roadmap priority.
- **Limitations:** hosted CI will not be inferred from local checks.

## Blockers / Risks

- No current blocker.
- Objective equality alone does not imply equality of the two minimizer sets.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** theorem, requested memory, exact Ruff provenance,
  all local verification, independent audits, and final hygiene pass.
- **Files changed:** `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `start.md`,
  three requested research notes, one test lint correction, and this
  three-file task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `PROJECT_KNOWLEDGE.md`, and `research/NEXT_RESEARCH_STEPS.md`.
