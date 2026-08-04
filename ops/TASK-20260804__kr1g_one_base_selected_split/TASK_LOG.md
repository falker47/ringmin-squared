# TASK LOG - TASK-20260804 / KR1G One Base Selected Split

Append-only. Add a new entry to correct previous information.

## 2026-08-04 - STRICT startup and one-base class isolation

- **Action:** read the operating contract, stable memory, current status,
  roadmap, KR1G-91b and KR1G-93--KR1G-98 context, and the fixed-count and
  variable-count dossiers; inspect the Git baseline before task edits.
- **Result:** baseline
  `943a841d46424cf2c22fe3d80be2e88438b32262` was clean. The bounded class
  has \(p=\ell-1\), exactly one selected base split, arbitrary recursive
  parentage and depth, and arbitrary compatible completion.
- **Interpretation:** the task is isolated from the generic \(b=o(n)\),
  growing-\(k\), and geometric directions.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-source-isolation`.
- **Next step:** verify the exact finite specialization and retained-term
  cubic estimate.

## 2026-08-04 - One-base derivation in verification

- **Action:** specialize the finite prefix/Bellman formulation to
  \(p=\ell-1\), then retain the recursive contributions in
  KR1G-93--KR1G-98 instead of applying the positive-base-density
  relaxation.
- **Result:** the current derivation forces the sole selected base split to
  be the first selected label \(t=r-1\), gives exact prefix count
  \(q!\,\ell!/2\) over all unoriented base cycles, and retains KR1G-91b as
  the exact finite residual minimum. Its asymptotic lower quantity currently
  satisfies
  \[
  {K_{k,n}^{1\mathrm B}\over n^3}
  \longrightarrow\Theta_k^{1\mathrm B}>0
  \]
  for every fixed \(k\).
- **Interpretation:** subject to the pending proof and computational audits,
  the one-base class has a positive normalized cubic liminf and therefore
  admits no compatible subcubic counterfamily. No inference is made for
  generic \(b=o(n)\), \(k=k(n)\), or geometry.
- **Evidence:** pending EV-002 in `EVIDENCE.md`; this entry records a result
  in verification, not completed evidence.
- **Next step:** complete the independent proof audit and exact checker.

## 2026-08-04 - One-base theorem and independent proof audit

- **Action:** complete the exact \(p=\ell-1\) specialization of KR1G-91b
  and KR1G-93--KR1G-98; independently audit every off-by-one, finite count,
  denominator, floor/ceiling term, and fixed-\(k\) quantifier.
- **Result:** KR1G-114--KR1G-123 prove the exact prefix/Bellman formulation,
  preserve the full recursive energy, and give
  \[
  \liminf_{n\to\infty}
  {\min_h\mathscr R_{k,n}(h)\over n^3}
  \ge\Theta_k^{(1{\rm B})}>0
  \]
  separately for every fixed \(k\).
- **Interpretation:** the one-base class admits no compatible subcubic
  family. This does not decide generic \(b=o(n)\), growing \(k\), or
  geometry. The preceding in-verification entry is now superseded by this
  audited result.
- **Evidence:**
  `EVIDENCE.md#ev-002---exact-one-base-theorem-and-fixed-k-cubic-decision`.
- **Next step:** execute the fresh finite recursive-topology checker.

## 2026-08-04 - Independent one-base recursive-topology checker

- **Action:** implement and run a standalone exact `Fraction` checker on a
  two-segment BRRR fixture, including fresh lineage, depth-three and
  inserted--inserted targets, every KR1G-93 addend, the deterministic
  recursive sum, the full decomposition, and literal/Bellman completion
  minima; run Ruff lint and format checks.
- **Result:** all 216 prefixes and 39,312 completions pass. The global count
  identity, topology histograms, \(K_{\rm det}=8333/140\), the uniform and
  topology-sensitive bounds, and the literal/Bellman minimum \(3464/35\)
  all agree exactly; Ruff passes.
- **Interpretation:** the finite checker can falsify lineage, recursive-term,
  completion, and bound errors but does not replace the symbolic proof.
- **Evidence:**
  `EVIDENCE.md#ev-003---independent-exact-recursive-topology-checker`.
- **Next step:** run repository-wide and historical KR1G regressions.

## 2026-08-04 - Repository and prior KR1G regressions

- **Action:** run the full repository suite, focused Arb and schema suites,
  checked-artifact verification, and the preceding fixed-count,
  variable-count, and one-recursive exact checkers.
- **Result:** 283 full tests, 3 Arb tests, 4 schema tests, all four checked
  artifacts with 76 local brackets, and every historical KR1G checker pass.
- **Interpretation:** the task-local proof and checker do not disturb the
  production or certification layers and remain consistent with prior KR1G
  finite machinery.
- **Evidence:**
  `EVIDENCE.md#ev-004---repository-and-prior-kr1g-regressions`.
- **Next step:** finish durable alignment and the complete diff audit.

## 2026-08-04 - Final documentation and review handoff

- **Action:** align the authoritative proof, stable memory, roadmap, current
  status, and dossier; inspect the complete tracked diff and all untracked
  files; audit tags, links, encoding, line endings, math balance, whitespace,
  Git status, and `git diff --check`.
- **Result:** 1,090 unique equation tags, all eight task files, both new local
  targets, every math environment, and the complete final diff pass their
  checks. The task is `READY_FOR_REVIEW`.
- **Interpretation:** the bounded STRICT task is complete and awaits user
  review and a manual commit decision. No generic \(b=o(n)\), growing-\(k\),
  or geometric claim was introduced.
- **Evidence:**
  `EVIDENCE.md#ev-005---final-proof-documentation-and-diff-verification`.
- **Next step:** user review and manual commit decision.
