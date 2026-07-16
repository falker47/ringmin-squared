# TASK STATUS - Joint Linear-Block Optimization

- Task ID: `TASK-20260716__joint_linear_block_optimization`
- Mode: STRICT
- Status: READY_FOR_REVIEW
- Last updated: 2026-07-16
- Blocker: none

## Objective

Generalize CR28ax--CR28bg from
\(r_n=\lfloor(\sqrt2-1)n\rfloor\) to
\(r_n=\lfloor\alpha n\rfloor\), keep \(m=1\), derive the exact joint
pairing/residual coefficient for \(s_n=\lceil\beta n\rceil\) and weight
\(\lambda\), solve the maximin globally with complete boundary analysis, and
provide a uniform finite floor/ceil theorem plus independent test-local
diagnostics.

## Scope Guard

- Research proof, synchronized authoritative notes, and test-only diagnostics.
- No production, artifact, schema, example, verifier, backend, enumeration
  implementation, or enumeration-limit changes.
- No claim of an exact residual, convergence, exact leading coefficient, or
  exact geometric constant.

## Current Truth

- The candidate supplied in the task is confirmed exactly and is the unique
  global maximizer of this certificate template:
  \[
  (\alpha_*,\beta_*,\lambda_*)
  =\left(1-{\sqrt3\over3},
          {5\over6}-{\sqrt3\over4},
          {88-32\sqrt3\over73}\right).
  \]
- The template-optimal global lower coefficient is
  \(C_*=(4+2\sqrt3)/27\).
- The exact finite floor/ceil statement is uniform from \(n=86\); the simpler
  polynomial statement is valid from \(n=90\).
- The proof, diagnostics, authoritative-source synchronization, complete
  verification, and independent reviews are complete.

## Completion Checklist

- [x] Inspect prior certificate and independent diagnostics.
- [x] Derive the general coefficient and admissible region.
- [x] Solve all interior branches and boundary faces exactly.
- [x] Prove global uniqueness and confirm the proposed candidate.
- [x] Derive the explicit finite rounded theorem and uniform domain.
- [x] Add independent exact bounded diagnostics.
- [x] Synchronize primary research sources and durable knowledge.
- [x] Run complete verification and inspect the final diff.
- [x] Set task and project status to READY_FOR_REVIEW.

## Handoff Condition

After all checks pass, the user reviews the worktree and decides whether to
commit manually.
