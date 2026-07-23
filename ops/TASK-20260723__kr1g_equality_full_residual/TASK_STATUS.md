# TASK STATUS - TASK-20260723 / KR1G Equality Full Residual

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** minimize the complete KR1G residual over every
  positive-branch equality pair in KR1G-24, every selected-label assignment,
  and every compatible completion, while retaining the all-middle cutoffs
  and the fixed-\(k\), \(n\to\infty\), then \(k\to\infty\) order.
- **Expected output:** one explicit uniform cubic lower bound or one explicit
  counterfamily, an independent exact small-\(q,n\) full-residual checker,
  and proof, stable-memory, roadmap, status, and dossier updates.

## Scope

- **In scope:** KR1G-6 and KR1G-44--KR1G-68; every equality pair with
  \(1\le\ell<\lceil q/2\rceil\); every bijection from the selected labels to
  the deleted edges; every compatible completion below the last cutoff; the
  unchanged all-middle tuple; exact finite and separated asymptotic bounds.
- **Out of scope:** nonequality histories, production code, public tests,
  schemas, artifacts, enumeration-limit changes, and consequences outside
  the declared KR1G residual problem.

## Verified Facts

- Every selected edge in an equality pair is a distinct original base edge,
  and the retained original slack is exactly \((c-\ell)/2\).
- The selected deviations obey
  \(\left|\sum_t\delta_t\right|\le c-\ell\).
- The complete residual satisfies the exact finite uniform bound
  \[
  P(C_0)+M_h-B_{h,n}
  \ge{[T_{k,n}-(c-\ell)]_+^2\over Q_{k,n}}.
  \]
- With fixed \(k\), then \(n\to\infty\), then \(k\to\infty\),
  \[
  \liminf_{k\to\infty}\liminf_{n\to\infty}
  {\min_h(P(C_0)+M_h-B_{h,n})\over n^3}
  \ge C_{\rm eq}
  =0.0008596674036945946006\ldots
  >{786-473\sqrt2\over170338}>0.
  \]
- The independent checker passes 204,556 canonical cycles, 1,066 equality
  pairs, 17,188 assignments, and 230,252 one-segment full histories, plus
  192 assignments and 21,120 histories in a two-segment fixture.

## Assumptions / Inferences

- Integer admissibility and nonemptiness are eventual for each fixed
  all-middle tuple; the threshold may depend on \(k\).
- The synthetic exact fixtures corroborate finite structure and arithmetic;
  they are not actual rounded irrational all-middle rows and do not replace
  the symbolic proof.

## Decisions And Rationale

- Use the square-center term \(E_{\square}\) from the exact KR1G-6
  decomposition; completion can only alter the separate nonnegative height
  term.
- Sum the selected endpoint deviations around the equality cycle and apply
  weighted Cauchy. This keeps the proof independent of the equality block
  parametrization after KR1G-45.
- Discover finite equality pairs in the checker from literal retained slack,
  not from the previous classification predicate.
- Keep the checker task-local, standard-library-only, and exact.

## Plan And Expected Delta

- [x] Complete STRICT startup on a clean worktree.
- [x] Derive the exact finite complete-residual lower bound.
- [x] Take the fixed-\(k\), \(n\), and \(k\) limits in the required order.
- [x] Add and run the independent full-residual checker.
- [x] Update the authoritative proof, stable memory, roadmap, and status.
- [x] Complete repository regressions and final source/diff audits.
- [x] Set all task memory to `READY_FOR_REVIEW`.

## Verification

- **Checks:** exact exhaustive checker; Ruff lint and formatting; exact SymPy
  algebra; independent mathematical and checker reviews; full repository
  tests; checked-artifact and schema verification; source, link, encoding,
  Git diff, and whitespace audits.
- **Observed result:** the checker passes all 251,372 full histories; Ruff and
  exact symbolic identities pass; two mathematical reviews and one checker
  review report `PASS`; 283 repository tests, all four checked artifacts,
  and four focused schema tests pass; all final source and diff audits pass.
  Ruff requested mechanical formatting after checker edits; counts and
  minima were unchanged and the final format check passes.
- **Limitations:** finite fixtures do not prove the all-\(q\) or asymptotic
  theorem, and the theorem supplies a lower bound rather than the exact
  residual infimum coefficient.

## Blockers / Risks

- No blocker.
- Residual risk is final human review of the square-center specialization and
  the strict order of the two nested asymptotic liminfs.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact finite square-center bound, positive
  all-middle cubic coefficient, passing exhaustive exact checker, complete
  repository regressions, and final source/diff audits.
- **Files changed:** authoritative proof, stable memory, roadmap, current
  status, and this new task dossier; no production or public test file.
- **Files to read first:** the new full-equality-residual subsection in
  `research/FIXED_ORDER_CYCLE_RATIO.md` and `EVIDENCE.md`.
