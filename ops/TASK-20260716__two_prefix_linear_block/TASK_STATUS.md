# TASK STATUS - Two-Prefix Linear Block

- Task ID: `TASK-20260716__two_prefix_linear_block`
- Mode: STRICT
- Status: READY_FOR_REVIEW
- Last updated: 2026-07-16
- Blocker: none

## Objective

Generalize CR28ax--CR28bg to two selected prefixes with
\(r_n=\lfloor\alpha n\rfloor\),
\(s_{1,n}=\lceil\beta_1n\rceil\),
\(s_{2,n}=\lceil\beta_2n\rceil\), and
\(0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1\); audit one-use base-edge
charging and every recursive split, derive the resulting coefficient, and
verify the supplied rational witness with a uniform finite theorem and a
global lower corollary.

## Scope Guard

- Research proof, synchronized authoritative notes, and independent
  test-local exact diagnostics only.
- No five-parameter global optimization.
- No production, API, artifact, schema, example, verifier, backend,
  certificate, enumeration implementation, or enumeration-limit changes.
- No exact residual, exact leading coefficient, convergence, or matching
  upper-bound claim.

## Expected Delta

- Add the exact two-prefix weighted-prefix and charging theorem after the
  existing one-prefix certificate.
- Prove or refute the supplied witness in rational arithmetic.
- If valid, add its exact floor/ceiling statement, uniform threshold, global
  corollary, and independent base/recursive split diagnostics.
- Synchronize stable project memory and finish at `READY_FOR_REVIEW` after
  complete verification and final diff inspection.

## Current Truth

- Startup worktree was clean and the focused baseline passed 69 tests.
- Independent derivations agree that the one-use charging transfer
  is valid only after the two selected prefixes are combined into one weighted
  split sum; applying two separate copies of CR28be would duplicate base
  slack and is not allowed.
- The combined charging transfer is proved exactly; every base slack has
  multiplicity at most one and every recursive split is covered.
- The witness coefficient is
  \[
  C_2={72825421\over263424000}>{4+2\sqrt3\over27}.
  \]
- The minimal uniform threshold is \(n=59\), and for every \(n\ge59\),
  \[
  \Lambda_n\ge C_2n^3,
  \qquad
  R_2^*(n)>{C_2\over\pi}n^3-n^2.
  \]
- Independent diagnostics, complete verification, synchronization, and final
  scope/diff audits pass. The task is ready for user review and a manual
  commit decision.

## Completion Checklist

- [x] Inspect the prior proof, dossiers, and independent diagnostics.
- [x] Prove the exact two-prefix weighted-prefix inequality and charging
  partition.
- [x] Prove single-use base slack and recursive child-edge coverage.
- [x] Derive the exact coefficient and verify the rational witness.
- [x] Derive the minimal uniform threshold and finite/global corollaries.
- [x] Add independent exact base, recursive, nested, and negative-route tests.
- [x] Synchronize authoritative proof and durable project memory.
- [x] Run focused/full verification and inspect the final diff.
- [x] Set task and project status to READY_FOR_REVIEW.

## Handoff

The user reviews the worktree and decides whether to commit manually. A fresh
STRICT task may optimize the five two-prefix parameters globally; that work
was deliberately not started here.
