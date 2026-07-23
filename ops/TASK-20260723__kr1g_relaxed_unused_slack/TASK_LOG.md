# TASK LOG - TASK-20260723 / KR1G Relaxed Unused Slack

Append-only. Add a new entry to correct previous information.

## 2026-07-23 - STRICT startup and task isolation

- **Action:** read the operating contract, stable memory, current status,
  roadmap, CR28ax, the complete KR1G audit, its prior dossier, and Git state.
- **Result:** clean `main` worktree at
  `cb9c8ff29db9a42da558c776a3b728ca6f2a6f6e`; the bounded task concerns only
  the unused-original-edge projection.
- **Interpretation:** the task can proceed without production, test, schema,
  artifact, or enumeration-limit changes.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-source-isolation`.
- **Next step:** solve the relaxed cycle/edge-set minimum.

## 2026-07-23 - Exact relaxed minimum

- **Action:** translate the interval to \(\{0,\ldots,q-1\}\), classify
  zero-slack edges as a complementary matching, and construct parity-explicit
  zigzag cycles.
- **Result:** for every \(q\ge3\), \(\ell\ge1\), the exact minimum is
  \(\frac12[\lceil q/2\rceil-\ell]_+\). At the fixed KR1G densities it is
  \((2+5\sqrt2)n/92+O(1)\).
- **Interpretation:** the requested \(n^3\)-normalized limit is zero, with a
  stronger exact linear asymptotic.
- **Evidence:** `EVIDENCE.md#ev-002---exact-relaxed-slack-theorem`.
- **Next step:** audit what survives compatible-history constraints.

## 2026-07-23 - Compatible-history scope

- **Action:** project a literal history to its base cycle and distinct
  original edges charged by base splits; conversely lift an optimal deleted
  edge set by successive edge subdivision.
- **Result:** the relaxed value is the sharp uniform minimum of
  \(E_{\rm unused}\) over histories for that term alone, and every KR1G-6
  residual receives the additive linear lower bound. The lift controls none
  of the other nonnegative remainders.
- **Interpretation:** no positive cubic coefficient transfers from unused-
  edge cardinality, but no subcubic statement about the full history residual
  follows.
- **Evidence:** `EVIDENCE.md#ev-002---exact-relaxed-slack-theorem`.
- **Next step:** add an independent bounded oracle.

## 2026-07-23 - Independent exact oracle

- **Action:** enumerate Hamiltonian cycles canonically modulo rotation and
  reversal, optimize every deletion budget exactly, and separately check the
  full zigzag profiles.
- **Result:** all 204,556 cycles and 52 \((q,\ell)\) cases for
  \(3\le q\le10\) agree with the formula; Ruff lint and format pass.
- **Interpretation:** bounded exact computation independently corroborates
  both the optimum and the explicit family.
- **Evidence:** `EVIDENCE.md#ev-003---bounded-exact-oracle`.
- **Next step:** run repository regressions and final source/diff audits.

## 2026-07-23 - Final verification and handoff

- **Action:** run the complete repository regression, checked-artifact and
  schema verifiers, final oracle and Ruff checks, equation-tag and Markdown
  structure audits, UTF-8/LF and link checks, full diff inspection, Git
  status, and whitespace validation.
- **Result:** 283 tests, four checked artifacts, four focused schema tests,
  204,556 oracle cycles, Ruff, 998 unique equation tags, balanced displays
  and aligned environments, all changed-file encoding checks, links, and
  `git diff --check` pass.
- **Interpretation:** the exact linear minimum, null cubic normalization, and
  compatible-history scope are ready for manual review.
- **Evidence:** `EVIDENCE.md#ev-004---repository-and-final-diff-verification`.
- **Next step:** user review and manual commit decision.
