# TASK STATUS - Global CR28bw Optimization

- Task ID: `TASK-20260716__global_cr28bw_optimization`
- Mode: STRICT
- Status: READY_FOR_REVIEW
- Last updated: 2026-07-16
- Blocker: none

## Objective

Optimize the two-prefix coefficient CR28bw globally and exactly on
\[
0<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1,
\]
including an exact ordered-weight reduction, every interior branch,
transition, boundary face, and density collision. Determine the exact global
coefficient and all feasible maximizers without assuming the numerical
candidate.

## Scope Guard

- Research proof, stable-knowledge synchronization, and independent exact
  symbolic/rational test-local diagnostics only.
- No finite rounding theorem for the eventual optimizer.
- No production source, API, artifact, schema, example, verifier, backend,
  certificate, enumerator, or enumeration-limit change.
- No exact residual, convergence, exact geometric leading coefficient, or
  matching upper-bound claim.

## Expected Delta

- Reduce the ordered \(\lambda\)-optimization exactly and classify its six
  possible saturation/interior branches.
- Solve the remaining density optimization on the compact closure, including
  every transition and collision face, and prove global uniqueness in the
  original strict domain if that is the exact outcome.
- Add exact independent arithmetic checks for the stationary equations,
  branch validity, comparisons, radical coordinates, coefficient, and a
  falsifiable rational upper-bound audit.
- Synchronize the authoritative proof, project brief, stable knowledge,
  all-\(n\) summary, roadmap, current status, and this dossier.

## Current Truth

- Startup worktree was clean at
  `b121fa2e0fc4ec1b2c06f10536b82021292c40e7`.
- The focused pre-change test module passed all 89 tests.
- CR28bw and its prior two-prefix charging theorem are unchanged; this task
  optimizes only the already-proved coefficient formula.
- Exact ordered-weight reduction, all six branches, both nontrivial
  transitions, every compact face and density collision, and the global
  comparison are complete.
- The unique maximizer is
  \[
  \left(
  {629-23\sqrt{143}\over829},
  {2286-77\sqrt{143}\over3316},
  {2010-59\sqrt{143}\over3316},
  {6264-288\sqrt{143}\over5281},
  {3888-192\sqrt{143}\over4273}
  \right),
  \]
  with
  \[
  C_{2,*}={491596+6578\sqrt{143}\over2061723}.
  \]
- Independent diagnostics, complete verification, source synchronization,
  final scope inspection, and three read-only audits pass.

## Completion Checklist

- [x] Complete startup protocol and inspect relevant prior STRICT memory.
- [x] Run the focused clean baseline.
- [x] Reduce the ordered weight optimization exactly.
- [x] Classify all reduced branches, transitions, faces, and collisions.
- [x] Prove the exact global maximum and determine all maximizers.
- [x] Add independent symbolic/rational diagnostics.
- [x] Synchronize proof, stable knowledge, status, roadmap, and dossier.
- [x] Run focused and complete verification and inspect the final diff.
- [x] Set task and project status to READY_FOR_REVIEW.

## Handoff

The worktree is ready for user review and a manual commit decision. No next
task will be started in this chat.
