# TASK_STATUS - TASK-20260715__optimize_linear_block_certificate / Optimize Linear-Block Certificate

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** optimize the CR28ax--CR28bg certificate for
  (m=1), (r_n=\lfloor(\sqrt2-1)n\rfloor) over the cutoff
  (s_n=\lceil\beta n\rceil) and prefix weight \(\lambda\).
- **Expected output:** exact admissible parameter regions, literal finite
  base/recursive floors, an exact maximin solution, explicit finite bounds,
  independent bounded test-local diagnostics, and synchronized research
  memory without production or enumeration-limit changes.

## Scope

- **In scope:** `research/FIXED_ORDER_CYCLE_RATIO.md`, its bounded test-local
  diagnostics, the all-`n` lower-bound note, project brief, stable knowledge,
  roadmap, current status, and this task dossier.
- **Out of scope:** production source, APIs, scorers, canonicalizers,
  enumerators, limits, artifacts, schemas, certificate contracts, exact
  residual claims, exact geometric leading coefficients, and convergence
  claims.

## Verified Facts

- Startup tree was clean on `main` at `f0ad789`.
- The focused baseline `python -m pytest tests/test_fixed_order_cycle_ratio.py
  -q` reports 57 passed.
- The exact proof-valid region is
  \(0<\beta<\sqrt2-1\), \(0\le\lambda\le1\); at fixed \(n\), the exact
  cutoff condition is
  \(1\le\lceil\beta n\rceil\le\lfloor(\sqrt2-1)n\rfloor-1\).
- The strictly positive cubic region is
  \[
  {\sqrt2\over4}<\beta<\sqrt2-1,
  \qquad
  0<\lambda<{2\sqrt2\beta-1\over\beta^2}.
  \]
- With \(S=n+r_n\), the literal base and recursive floors are
  \[
  G_{n,\lambda}(t)=
  {\lambda(4St-S^2-2\lambda t^2)\over2(2-\lambda)},
  \qquad
  J_{n,\lambda}(t)=
  \lambda\bigl((S-1)t-n(r_n-1)\bigr).
  \]
  The charging identity keeps every original base edge at multiplicity at
  most one, and exact algebra proves \(J_{n,\lambda}(t)>G_{n,\lambda}(t)\)
  for \(\lambda>0\) and \(t\le r_n-1\).
- The exact maximin optimizer and certified template coefficient are
  \[
  \beta_*={9\sqrt2-8\over12},\qquad
  \lambda_*={88-48\sqrt2\over49},\qquad
  c_*={99\sqrt2-140\over27}.
  \]
  This strictly improves
  \((389-275\sqrt2)/375\) within the same template.
- For \(s_n^*=\lceil\beta_*n\rceil\), the proof retains the explicit finite
  floor
  \[
  F_n^*={\lambda_*\bigl(4(n+r_n)s_n^*-(n+r_n)^2
  -2\lambda_*(s_n^*)^2\bigr)\over2(2-\lambda_*)}.
  \]
  It yields the stated exact finite residual inequality, an explicit
  cubic-minus-quadratic form for \(n\ge99\), and positivity for \(n\ge572\).
- Three independent read-only audits agree on the algebra, literal linkage,
  charging, maximin, finite thresholds, and synchronization.

## Assumptions / Inferences

- Bounded diagnostics corroborate arithmetic and literal linkage only;
  the all-`n` result must rest on the written exact proof.

## Decisions And Rationale

- Distinguish the full proof-valid parameter region from the smaller region
  producing a strictly positive cubic certificate.
- Keep the recursive floor even though exact algebra shows it is never the
  active branch; this preserves the literal child-edge audit.
- State every optimized coefficient as a certified lower coefficient of this
  template, not as an exact residual or geometric limit.

## Plan And Expected Delta

- Completed: integrated the exact parameterized proof and maximin solution.
- Completed: added independent exact diagnostics, synchronized durable memory,
  ran complete verification, inspected the final diff, and prepared the
  manual-review handoff.

## Verification

- **Checks completed:** focused diagnostics, complete fixed-cycle test file,
  full test suite, checked-artifact verifier, schema tests, Ruff on the changed
  test, repository-wide Ruff audit, three independent reviews, Git status,
  final diff inspection, `git diff --check`, and a protected-path audit.
- **Observed result:** focused diagnostics 19 passed; fixed-cycle file 66
  passed; full suite 242 passed; checked-artifact verifier passed all four
  certificates, 76 local brackets, and the \(n=3,4,5,6\) summary; schema
  tests 4 passed; changed-test Ruff check passed; final diff hygiene and
  protected-path audit passed.
- **Known unrelated result:** repository-wide Ruff still reports four
  pre-existing findings in untouched files.
- **Limitations:** the diagnostics are finite corroboration, not the proof of
  the all-\(n\) statement. The optimized coefficient is a certified lower
  coefficient of this proof template, not an exact residual, geometric limit,
  or convergence theorem.

## Blockers / Risks

- No current blocker.
- The optimized lower coefficient must not be described as an exact residual,
  exact leading coefficient, geometric limit, or proof of convergence.

## Next Atomic Action

- In a fresh task, add an independent test-only Arb cross-check for the
  \(n=4\) checked artifact, as already listed in the roadmap.

## Handoff

- **Last verified result:** complete verification, independent reviews, and
  final diff/protected-path audits pass.
- **Files changed:** the fixed-order proof note, all-\(n\) note, bounded
  diagnostics, project brief, stable knowledge, roadmap, current status, and
  this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
