# TASK STATUS - TASK-20260723 / KR1G Distinct Original-Edge Residual

Last update: 2026-07-24

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** extend the complete KR1G residual theorem from the
  KR1G-24 equality subclass to every history in which the selected labels
  split exactly \(\ell\) distinct original edges, without changing the
  all-middle tuple or the fixed-\(k\), \(n\to\infty\), then
  \(k\to\infty\) order.
- **Expected output:** a rigorous finite inequality and exact optimized
  limiting coefficient or a precise counterexample; an independent exact
  small-\(q\) checker containing nonequality pairs; and authoritative proof,
  stable-memory, roadmap, status, and dossier updates.

## Scope

- **In scope:** all base cycles and selected-edge assignments for which all
  \(r-1,\ldots,s_k\) split distinct original edges; arbitrary compatible
  completion below \(s_k\); exact domain, rounding, nonemptiness, scalar
  optimization, and separated asymptotic limits.
- **Out of scope:** any selected recursive split, a growing prefix count,
  production code, public tests, schemas, artifacts, minimizing-order
  claims, and the original geometry.

## Verified Facts

- With \(U=E_{\rm unused}\) and \(m=q-\ell\), the selected deviations obey
  \[
  \left|\sum_t\delta_t\right|\le\sqrt{2mU}.
  \]
- The exact KR1G-6 decomposition and weighted Cauchy give
  \[
  \mathscr R_{k,n}(h)\ge
  U+\frac{[T_{k,n}-\sqrt{2mU}]_+^2}{Q_{k,n}}
  \ge\frac{T_{k,n}^2}{Q_{k,n}+2m}.
  \]
- The second bound is the exact minimum of the continuous scalar envelope,
  not an attainment claim for discrete histories.
- The fixed-\(k\) coefficient is
  \(\tau_k^2/(\chi_k+2\mu_k)\), where
  \(\mu_k=1-2a+\beta_k^{(k)}\).
- Its exact subsequent \(k\to\infty\) limit is
  \[
  C_{\rm dist}
  =
  \frac{2833-1968\sqrt2}
  {12167[
  2(18-\sqrt2)\log(2-\sqrt2/2)+4+10\sqrt2]}
  =0.0001535935517989924090\ldots>0.
  \]
- The independent checker passes 1,103,715 broad exact histories,
  including 1,103,135 nonequality histories, plus 13,440 two-segment
  completion histories, including 12,768 nonequality histories.

## Assumptions / Inferences

- All finite admissibility statements are eventual for each fixed
  all-middle tuple. The threshold may depend on \(k\).
- Synthetic rational fixtures verify finite identities and implementation
  independence; they are not literal rounded irrational all-middle rows and
  do not replace the proof.

## Decisions And Rationale

- Preserve the stronger \(C_{\rm eq}\) result on the equality subclass and
  add the all-distinct-original-edge theorem as a strict extension.
- Optimize over continuous \(U\ge0\) only after retaining \(U\) jointly with
  the square-center energy.
- Keep the checker task-local, standard-library-only, exact, and free of any
  equality-classification predicate or project import.

## Plan And Expected Delta

- [x] Complete STRICT startup on a clean worktree at `9160631`.
- [x] Prove the finite deviation and residual chain.
- [x] Optimize the scalar envelope and derive the exact ordered-limit
  coefficient.
- [x] Add and run an independent nonequality checker.
- [x] Update stable memory, roadmap, and current status.
- [x] Complete mathematical review, repository regressions, and final diff
  audits.
- [x] Set all task memory to `READY_FOR_REVIEW`.

## Verification

- **Checks:** independent mathematical audits; exact exhaustive checker;
  Ruff; exact symbolic algebra; repository tests and artifact verification;
  source, link, encoding, whitespace, and diff audits.
- **Observed result:** three read-only audits report no counterexample and
  approve the proof, checker, and final documentation after minor state
  corrections. The final exact checker and its named nonequality goldens,
  Ruff, 283 repository tests, all four checked artifacts, four schema tests,
  exact symbolic identities, and final source/diff audits pass.
- **Limitations:** bounded fixtures and regressions do not replace the
  symbolic all-\(q\) theorem.

## Blockers / Risks

- No blocker.
- Residual risk is final human review of the new joint-energy argument and
  exact ordered-limit coefficient.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** finite theorem, exact optimized coefficient,
  final exhaustive checker, complete repository regressions, and source/diff
  audits all pass.
- **Files changed:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `PROJECT_KNOWLEDGE.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `CURRENT_STATUS.md`, and this task dossier; no production or public test
  file.
- **Files to read first:** the KR1G-81--KR1G-88 extension in
  `research/FIXED_ORDER_CYCLE_RATIO.md` and `EVIDENCE.md`.
