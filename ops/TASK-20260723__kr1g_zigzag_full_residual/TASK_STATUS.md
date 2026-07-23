# TASK STATUS - TASK-20260723 / KR1G Zigzag Full Residual

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** decide whether the complete KR1G residual is subcubic or
  cubically positive in the history class obtained from the exact zigzag
  unused-slack witness, using the existing fixed-\(k\) all-middle parameters
  without modification.
- **Expected output:** one explicit subcubic family or one cubic lower bound
  for the entire declared class, with fixed-\(k\), \(n\), and \(k\) limits
  separated; an independent exact checker; proof, stable memory, roadmap,
  and dossier updates.

## Scope

- **In scope:** the translated \(Z_{n-r+1}\) base; the closing edge and
  \(r-s_k-1\) slack-\(1/2\) connector targets; every target-label
  assignment; every compatible completion below \(s_k\); the unchanged
  all-middle tuple from CR28dw1--CR28dw5; exact finite DP and a
  history-uniform cubic lower bound.
- **Out of scope:** arbitrary base cycles, all compatible histories, exact
  minimizer classification, a growing \(k=k(n)\) theorem, production code,
  public tests, schemas, artifacts, global cyclic-order conclusions, and
  geometry.

## Verified Facts

- The maximum endpoint sum starts at \(\mathsf{U}_n=n+r+1\) and strictly
  decreases along either child of every split, so it is a history invariant
  upper bound.
- Every correction satisfies
  \(A_t\ge\mathsf{U}_n\,t-\mathsf{U}_n^2/4\). The labels from
  \(r-1\) down to \(\lceil\mathsf{U}_n/4\rceil\) therefore force a cubic
  nonnegative prefix in every target assignment and completion.
- For each fixed \(k\), the normalized residual is bounded below by
  \[
  \delta_k
  ={(3a-1)^2\over32}
  \bigl(1+a-4(3a-1)M_k\bigr).
  \]
- Taking \(n\to\infty\) first for each fixed \(k\), and only then using
  \(M_k\uparrow1/3\), gives the strict class-uniform lower bound
  \[
  \liminf_{k\to\infty}\liminf_{n\to\infty}
  {\min_h(P(C_0)+M_h-B_{h,n})\over n^3}
  \ge {470-159\sqrt2\over73002}>0.
  \]

## Assumptions / Inferences

- The connector set is allowed to vary over every exact-witness choice. This
  enlarges the class, so the lower bound also covers any one connector set
  fixed in advance.
- The lower-bound theorem excludes the zero alternative but does not prove
  existence or the exact value of the outer limit written in the question.

## Decisions And Rationale

- Use the endpoint-sum invariant because it survives every arbitrary
  completion and avoids assuming that the unused-edge lift freezes the
  history maximum.
- State the strongest always-defined conclusion as an outer liminf.
- Add an exact finite DP to characterize the completion optimization, while
  using the simpler uniform barrier for the theorem.
- Keep the checker task-local, standard-library-only, and independent of
  project helpers.

## Plan And Expected Delta

- [x] Complete STRICT startup on a clean worktree.
- [x] Reconstruct KR1G-6 and the unchanged all-middle parameters.
- [x] Derive the exact completion DP and cubic history-uniform barrier.
- [x] Add the independent exact checker.
- [x] Update the authoritative proof, stable memory, and roadmap.
- [x] Complete repository verification and final diff review.
- [x] Set all task memory to `READY_FOR_REVIEW`.

## Verification

- **Checks:** task-local exhaustive checker; exact
  \(\mathbb Q(\sqrt2)\) scalar checks; Ruff lint and format; focused proof
  audits; full repository tests; checked-artifact and schema verification;
  final Git diff and whitespace checks.
- **Observed result:** 18,468 literal histories and twelve exact scalar rows
  pass; Ruff lint and format pass; 283 repository tests pass; all four
  checked artifacts and four focused schema tests pass; 1,008 equation tags
  are unique; 1,544 display delimiters and 190 aligned environments balance
  on each side; encoding, links, complete diff, and whitespace checks pass.
- **Limitations:** bounded synthetic fixtures corroborate structure but do
  not replace the symbolic proof or realize the eventual irrational cutoff
  rows.

## Blockers / Risks

- No blocker.
- Residual risk is final human review of quantifier order and the distinction
  between a positive lower bound and an exact outer limit.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact symbolic cubic lower bound, passing
  18,468-history checker, complete regression, and final source/diff audits.
- **Files changed:** authoritative proof, stable memory, roadmap, current
  task dossier, and one task-local checker.
- **Files to read first:** the new full-residual subsection in
  `research/FIXED_ORDER_CYCLE_RATIO.md` and `EVIDENCE.md`.
