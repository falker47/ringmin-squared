# TASK STATUS - Four-Prefix One-Use Charging

- Task ID: `TASK-20260716__four_prefix_charging`
- Mode: STRICT
- Status: READY_FOR_REVIEW
- Last updated: 2026-07-16
- Blocker: none

## Objective

Determine whether the one-use charging theorem CR28ce--CR28cg extends
exactly to four selected prefixes under
\[
0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
\]
If it does, prove the four-height convex combination, the unique partition of
the original base-edge slack, the invariant for every recursive edge split,
and the lower bound with four disjoint segments. If it does not, record one
exact reproducible split history locating the failure.

## Scope Guard

- In scope: exact proof or exact obstruction; one small standalone bounded
  literal-history oracle; pertinent authoritative-source synchronization only
  after a complete result.
- Out of scope: optimization of \(\alpha,\beta_i,\lambda_i\); finite rounding;
  any \(k\to\infty\) passage; production, artifact, schema, backend,
  certificate, enumerator, or enumeration-limit changes.

## Expected Delta

- Establish or refute the precise four-prefix analogue of CR28ce--CR28cg.
- Independently exercise literal intact-base and recursive child-edge splits
  through all three selected-prefix boundaries using exact arithmetic.
- Preserve all failed checks and distinguish the written all-history theorem
  from bounded computational corroboration.
- Finish with proportional verification, final diff inspection, and status
  `READY_FOR_REVIEW` if the bounded task is complete.

## Current Truth

- Repository root: `C:/Users/Falker/Desktop/Code/circle/ringmin-squared`.
- Startup branch: clean `main` tracking `origin/main`.
- Startup commit: `59d152ee0308702fef1a2dfdafaafb6af3f6ebe0`.
- CR28ce--CR28cg proves one-use charging through three selected prefixes and
  explicitly left four-prefix charging open before this task.
- The extension is true. The five ordered convex coefficients telescope to
  four disjoint weighted segments.
- Relative to each literal split history, original edges have one canonical
  charged/unused partition; every selected intact edge is charged once.
- The recursive invariant is independent of all three segment boundaries and
  covers arbitrary nesting, including edges with two inserted endpoints.
- The exact finite four-segment lower bound and the unoptimized
  fixed-parameter coefficient \(C_4\) are proved in
  research/FIXED_ORDER_CYCLE_RATIO.md.
- The standalone exact oracle passes all 840 bounded literal histories.

## Verification

- Focused pre-change three-prefix baseline: 6 passed.
- Independent literal oracle: 840 histories and 840 distinct final cycles
  passed.
- Oracle Ruff check and format check: passed after one recorded mechanical
  format correction.
- Fixed-order-cycle-ratio module: 101 passed.
- Complete local suite: 277 passed.
- Checked artifacts: 4 certificates and 76 local brackets passed; schema
  selection: 4 passed.
- Equation tags: 296 unique; changed Markdown delimiters and environments are
  balanced.
- Three independent read-only audits found no remaining mathematical, oracle,
  synchronization, Markdown, or scope defect after their corrections.
- Final changed-path, protected-scope, whitespace, and diff inspections pass.

## Completion Checklist

- [x] Complete STRICT startup and clean baseline.
- [x] Prove or refute exact four-prefix one-use charging.
- [x] Add and run an independent bounded literal oracle.
- [x] Synchronize only the pertinent authoritative sources.
- [x] Run proportional regression and independent audits.
- [x] Inspect the final diff and set READY_FOR_REVIEW.

## Next Atomic Action

User review and manual commit decision.

## Handoff

- Last verified result: exact four-prefix theorem and 840-history oracle pass.
- Files changed: primary proof, five synchronized authoritative summaries,
  and this task dossier.
- Suggested manual commit message:
  Prove exact four-prefix one-use charging.
