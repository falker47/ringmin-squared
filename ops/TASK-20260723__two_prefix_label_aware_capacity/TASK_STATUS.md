# TASK_STATUS - TASK-20260723 / Two-Prefix Label-Aware Capacity

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** formulate and close the two-prefix label-aware refinement of
  lower-bound charging while retaining the two nested capacity rows.
- **Expected output:** one exact no-double-charging finite theorem, exact
  compact normalized objective and no-go/improvement decision against
  \(C_{\rm AF}\), one small independent finite-row diagnostic, and synchronized
  durable sources.

## Scope

- **In scope:** CR28ds--CR28dw68; two nested selected cutoffs; separate prefix
  and total original-edge capacities; label-dependent \(G,J,\Delta\); exact
  integer allocation and discriminant collisions; full compact closure; one
  task-local standard-library diagnostic.
- **Out of scope:** production source, tests, schemas, checked artifacts,
  enumerators, enumeration limits, geometric claims, and upper bounds on
  \(\Lambda_n\).

## Verified Facts

- The exact finite allocation keeps both nested capacity inequalities and
  minimizes one coupled discrete-convex integer cost; its first difference
  is strict unless both ordered weights vanish.
- The normalized objective is continuous on its whole compact closure.
- Exact compact estimates give a strict improvement over the one-prefix
  label-aware coefficient and a strict no-go against \(C_{\rm AF}\).

## Assumptions / Inferences

- Sharpness is for the retained binary floor data; it does not assert
  simultaneous equality in every geometric local inequality.
- The compact no-go is method-specific and has no geometric interpretation.

## Decisions And Rationale

- Use the accepted \(k=2\) instance of arbitrary-finite-prefix charging once,
  with one common slack partition.
- Retain the upper-prefix and total-prefix capacity rows simultaneously.
- Use the exact discrete first difference and its discriminant rather than
  scanning allocations.

## Plan And Expected Delta

- [x] Complete STRICT startup on a clean worktree.
- [x] Derive the finite coupled allocation theorem.
- [x] Derive and classify the complete compact objective.
- [x] Run the independent diagnostic and repository verification.
- [x] Synchronize all durable files and set `READY_FOR_REVIEW`.

## Verification

- **Checks:** independent finite diagnostic; Ruff lint and format; full
  pytest; focused schema regression; checked-artifact verifier; equation-tag,
  display-math, control-character, protected-scope, complete-diff, and
  whitespace audits.
- **Observed result:** diagnostic PASS on six discriminant rows and 208
  admissible type histories; Ruff PASS; 283 pytest tests PASS; 4 schema tests
  PASS; 4 certificates and 76 local brackets PASS; 965 equation tags are
  unique; display delimiters balance 1,477/1,477; scope, diff, and whitespace
  audits PASS.
- **Limitations:** bounded finite rows corroborate but do not replace the
  all-history proof; hosted CI cannot inspect an uncommitted diff.

## Blockers / Risks

- No blocker.
- Residual risk is human review of the exact active-side Bernstein table.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact theorem, compact no-go, independent
  diagnostic, repository regressions, and final source audits all pass.
- **Files changed:** authoritative proof and synopsis, stable knowledge,
  roadmap, current status, and this task-local dossier with one diagnostic.
- **Files to read first:** the two-prefix label-aware section in
  `research/FIXED_ORDER_CYCLE_RATIO.md`.
