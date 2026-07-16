# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** exact four-prefix one-use charging established.
- **Current task:** determine whether CR28ce--CR28cg extends exactly to four
  selected prefixes.
- **Task dossier:** ops/TASK-20260716__four_prefix_charging/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Four-Prefix Theorem

Fix
\[
0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
\]
Put \(r=\lfloor\alpha n\rfloor\),
\(s_i=\lceil\beta_i n\rceil\), \(s_0=r\), and
\(F_{i,n}=G_{n,\lambda_i}(s_i)\). Whenever
\[
2\le r\le n-2,
\qquad
1\le s_4<s_3<s_2<s_1\le r-1,
\]
the five coefficients
\[
1-\lambda_1,\quad
\lambda_1-\lambda_2,\quad
\lambda_2-\lambda_3,\quad
\lambda_3-\lambda_4,\quad
\lambda_4
\]
give the exact all-height convex region and telescope to four disjoint
weighted split segments. One canonical edge-indexed partition assigns each
original base edge to its unique selected intact split or to the unused set.
The recursive invariant survives all three boundaries and every nesting
depth. Therefore
\[
\boxed{
\begin{aligned}
\gamma^{(r)}_{1,n}\ge{}&P_{r,n}
+(r-s_1)F_{1,n}
+(s_1-s_2)F_{2,n}\\
&+(s_2-s_3)F_{3,n}
+(s_3-s_4)F_{4,n}.
\end{aligned}
}
\]

For fixed admissible parameters, this yields the unoptimized coefficient
\[
\begin{aligned}
C_4={}&p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)\\
&+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)\\
&+(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3)\\
&+(\beta_3-\beta_4)g(\alpha,\beta_4,\lambda_4),
\end{aligned}
\]
with
\[
\liminf{\Lambda_n\over n^3}\ge C_4,
\qquad
\liminf{R_2^*(n)\over n^3}\ge{C_4\over\pi}.
\]

## Independent Bounded Oracle

The standalone standard-library Fraction oracle uses
\[
(n,r,C_0)=(14,11,(11,14,12,13)),
\quad
(s_1,s_2,s_3,s_4)=(10,9,8,7),
\]
\[
(\lambda_1,\lambda_2,\lambda_3,\lambda_4)
=(4/5,3/5,2/5,1/5).
\]
It passes all \(4\cdot5\cdot6\cdot7=840\) literal current-edge histories and
finds 840 distinct final cycles. Recursive search-tree split counts are
\((0,8,72,600)\), with 120 fourth splits between two previously inserted
endpoints. The exact local floors sum to \(9239/72\), giving the checked
four-segment lower bound \(53879/72\) on this base.

## Evidence Classification

- EXACT METHOD-SPECIFIC THEOREM: convex height combination, canonical
  original-edge slack partition, all-recursive invariant, finite
  four-segment bound, and unoptimized fixed-parameter consequence.
- VERIFIED BOUNDED EXACT COMPUTATION: independent 840-history literal oracle.
- LIMITATION: bounded computation corroborates but does not prove the
  all-history theorem.
- LIMITATION: the best optimized numerical lower coefficient remains
  \(C_{3,*}\); \(C_4\) was not optimized or compared numerically.

## Verification

- Clean startup baseline: six focused historical three-prefix tests passed.
- Standalone oracle: passed all 840 histories.
- Oracle Ruff check and format check: passed after one mechanical format
  correction.
- Complete fixed-order-cycle-ratio module: 101 passed.
- Complete local suite: 277 passed.
- Checked-artifact semantic verification: 4 certificates and 76 local
  brackets passed.
- Checked-artifact schema selection: 4 passed.
- Equation-tag audit: 296 tags, all unique.
- Display-math and aligned/array environments are balanced in every changed
  Markdown file.
- Three independent read-only audits checked the mathematics, oracle,
  authoritative synchronization, Markdown, and protected scope. Their one
  finite-domain omission and two documentary ambiguities were corrected; the
  stable reaudit found no remaining defect.
- Final changed-path inspection, protected-scope inspection,
  git diff --check, and final diff review passed.

## Files Changed

- research/FIXED_ORDER_CYCLE_RATIO.md: primary exact theorem and oracle
  evidence.
- research/ALL_N_LOWER_BOUND.md and
  research/NEXT_RESEARCH_STEPS.md: synchronized consequences and roadmap.
- start.md, PROJECT_KNOWLEDGE.md, and this file: synchronized authoritative
  project memory.
- ops/TASK-20260716__four_prefix_charging/: STRICT dossier and independent
  literal oracle.

## Protected Limitations

- No optimization of \(\alpha,\beta_i,\lambda_i\).
- No finite rounding theorem and no \(k\to\infty\) passage.
- No charging claim for \(k\ge5\).
- No production, test, artifact, schema, backend, certificate, enumerator, or
  enumeration-limit change.
- No exact residual, convergence theorem, matching upper bound, exact
  geometric leading coefficient, or exact value of \(\Lambda_n\) or
  \(R_2^*(n)\).

## Proposed Next Task

In a fresh STRICT task, analyze one explicit parametric perturbation of the
current \(8/25\) product-distance upper construction and prove either a strict
symbolic improvement or a precise obstruction, without extending cyclic-order
enumeration.
