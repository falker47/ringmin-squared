# TASK STATUS - TASK-20260723 / KR1 Finite-Prefix Gap Decomposition

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** decompose exactly, on the existing KR1 upper family, the
  asymptotic gap between \(K_{\rm R1}\) and the accepted
  arbitrary-finite-prefix lower functional \(C_{\rm AF}\).
- **Expected output:** one exact finite nonnegative slack identity, a complete
  cubic classification of every charging step on KR1, one explicit positive
  structural term or a tightness theorem, and one small independent
  discriminating diagnostic.

## Scope

- **In scope:** the existing KR1 order; CR28ax--CR28dw; fixed-finite-prefix
  consequences followed by their accepted supremum; local floors,
  original-edge slack, child-edge coverage, heights, and history
  minimization; exact algebra and one task-local diagnostic.
- **Out of scope:** a new optimized fixed prefix count; a growing-prefix
  theorem; new order families; production code, tests, schemas, artifacts, or
  enumeration limits; global minimizing-order and geometric claims.

## Verified Facts

- The finite charging slack is an exact sum of nonnegative height, unused
  original-edge, base-floor, recursive-floor, coverage, and segment-floor
  terms.
- In the active \(C_{\rm AF}\) window, every KR1 insertion splits a distinct
  original edge; recursive and child-edge terms vanish identically.
- The discarded unused-original-edge coefficient is
  \[
  {4614125\sqrt2-5527598\over146004000}>0.
  \]
- Together with the positive convex-height, product-relaxation, and
  square-center coefficients, this term sums exactly to
  \(857/3000-C_{\rm AF}\).

## Assumptions / Inferences

- The sequential limit retains the accepted quantifier order: first
  \(n\to\infty\) for each fixed finite tuple, then the supremum over finite
  tuples.
- The dense integer-cutoff diagnostic is only a Riemann-sum audit; it is not
  used to justify a uniform \(k(n)\) theorem.
- The pointwise KR1 decomposition does not determine the minimum over all
  compatible histories.

## Decisions And Rationale

- Separate the exact telescope and slack partition from the later
  nonnegative discards.
- Refine the base floor into its product and square-center terms.
- Use the existing KR1 block word to rule out recursive splits before taking
  limits.
- Record minimization as an external unclassified split of the already
  decomposed gap, not as an invented residual.

## Plan And Expected Delta

- [x] Complete STRICT startup on a clean worktree.
- [x] Reconstruct the finite charging chain and KR1 tail history.
- [x] Derive all exact cubic coefficients and their sum.
- [x] Add and run the independent exact diagnostic.
- [x] Complete repository verification, source audits, and final diff review.

## Verification

- **Checks:** exact diagnostic; Ruff lint and format; equation-tag and
  Markdown structure audits; full pytest; checked-artifact verifier; focused
  schema tests; complete Git diff and whitespace checks.
- **Observed result:** exact diagnostic PASS on six rows covering both KR1
  parity branches through \(n=100006\), with 8,168 selected original edges
  and zero recursive splits on the largest row; 283 tests, four checked
  artifacts, four focused schema tests, Ruff, source-structure audits, UTF-8
  audit, final diff inspection, and `git diff --check` all pass.
- **Limitations:** bounded computation corroborates but does not replace the
  symbolic all-row and sequential-limit proof.

## Blockers / Risks

- No blocker.
- Residual risk is final human review of the endpoint classification and
  logarithmic exact forms.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact mathematical decomposition, bounded finite
  diagnostic, full repository regression, and final source/diff audits.
- **Files changed:** authoritative proof and synopsis, stable knowledge,
  roadmap, current status, and this task dossier.
- **Files to read first:** the KR1 gap-audit subsection in
  `research/FIXED_ORDER_CYCLE_RATIO.md` and `EVIDENCE.md`.
