# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** exact global optimization of the three-prefix
  linear-block coefficient.
- **Current task:** extend CR28br--CR28bw to three selected prefixes, prove
  one-use charging through every recursive split, and determine \(C_{3,*}\)
  on the compact closure.
- **Task dossier:** ops/TASK-20260716__three_prefix_linear_block/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- Combined three selected heights before assigning any edge slack.
- Proved one global base-slack partition across all three split segments.
- Retained every recursive child edge, including fully nested histories
  crossing both segment boundaries and edges with two inserted endpoints.
- Reduced the three ordered weights exactly through their clipped individual
  optima.
- Proved the unique global maximum on the full compact closure without
  assuming the supplied normalized point.
- Added independent exact rational and quadratic-surd diagnostics.
- Kept finite optimizer rounding, production code, artifacts, schemas,
  backends, certificates, enumerators, and enumeration limits outside scope.

## Three-Prefix Charging Theorem

For
\[
0<\beta_3<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_3\le\lambda_2\le\lambda_1\le1,
\]
the exact weighted-height step is
\[
\max(0,H_1,H_2,H_3)
\ge
(\lambda_1-\lambda_2)H_1
+(\lambda_2-\lambda_3)H_2+\lambda_3H_3.
\]
Expanding before charging assigns weights \(\lambda_1,\lambda_2,\lambda_3\)
to the three disjoint split segments. Every original base slack is then used
once, while every recursive current edge retains the established local floor.
The limiting coefficient is
\[
C_3=p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)
+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)
+(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3).
\]

## Exact Weight Reduction

For \(s=1+\alpha\), each individual optimum is the clipped function
\[
\psi_s(\beta)=
\begin{cases}
0,&\beta\le s/4,\\
4-s/\beta,&s/4<\beta<s/3,\\
1,&\beta\ge s/3.
\end{cases}
\]
It is nondecreasing, so
\(\psi_s(\beta_3)\le\psi_s(\beta_2)\le\psi_s(\beta_1)\); the separate
maxima already satisfy the ordered-weight constraint. The compact reduction
is therefore
\[
\overline C_3
=p(\alpha)+(\alpha-\beta_1)\Phi_s(\beta_1)
+(\beta_1-\beta_2)\Phi_s(\beta_2)
+(\beta_2-\beta_3)\Phi_s(\beta_3).
\]
The ten clipped regimes and every weight/density collision face are covered.
Unused weights on zero-length segments can be nonunique but do not create
another global maximizer.

## Unique Compact-Closure Maximum

For \(A=3\alpha-1\) and active
\(X_i=4\beta_i-(1+\alpha)\), the normalized residual is bounded by
\[
{A^3\over8}
\left((1-x)x^2+(x-y)y^2+(y-z)z^2\right),
\qquad
(x,y,z)=\left({X_1\over A},{X_2\over A},{X_3\over A}\right).
\]
An exact three-term nonnegative factorization gives the unique simplex point
\[
\boxed{
(x,y,z)
=\left({1058\over1263},{276\over421},{184\over421}\right).
}
\]
The one-variable envelope is
\[
E_3(\alpha)
=p(\alpha)+{279841\over9571014}(3\alpha-1)^3,
\]
with unique global maximizing density
\[
\boxed{
\alpha_*={685623-421\sqrt{377823}\over993423}.
}
\]
The second critical point in \([1/3,1]\) is a local minimum and the endpoint
\(\alpha=1\) is strictly lower. At \(\alpha_*\), all densities and weights
are strictly ordered in the middle clipped branch, so every relaxation is
attained.

## Exact Coefficient And Consequence

The exact three-prefix template optimum is
\[
\boxed{
C_{3,*}
={753972193324+106042322\sqrt{377823}\over2960667770787}
}
=0.2766786474619455709\ldots .
\]
It satisfies
\[
79938029811249C_{3,*}^2
-40714498439496C_{3,*}+5145490327924=0
\]
and
\[
{276678647461\over10^{12}}
<C_{3,*}
<{276678647462\over10^{12}}.
\]
Exact extension of the strict two-prefix optimizer proves
\[
C_{3,*}>C_{2,*}.
\]
Consequently
\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{3,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{3,*}\over\pi}.
\]

## Independent Diagnostics

- A rational oracle exhausts all 46,620 depth-three histories from one
  \(n=59\) base cycle.
- The histories include 70 distinct recursive second-step prefixes (2,590
  full-history occurrences), 4,970 recursive third splits, and 70 fully
  nested third splits on the edge formed by the two earlier labels.
- Exact grids verify the ordered-weight tetrahedron, all ten clipped regimes,
  the compact density closure, and the nonnegative simplex factorization.
- Test-local \(\mathbb Q(\sqrt{377823})\) arithmetic verifies the strict
  optimizer domain, coefficient reconstruction, coefficient polynomial,
  rational isolation, and strict comparison with \(C_{2,*}\).
- An explicit negative regression shows that three separately slack-charged
  prefix copies overdraw one base edge by twice its slack.

## Verification

- Focused three-prefix selection: 7 passed.
- Complete fixed-order-cycle-ratio module: 101 passed.
- Complete local suite: 277 passed.
- Checked-artifact verifier: all 4 certificates, 76 local brackets, and the
  \(n=3,4,5,6\) summary verified.
- Checked-artifact schema selection: 4 passed.
- Ruff on the changed test module: passed.
- Repository-wide Ruff retains exactly four known findings in untouched
  files; none belongs to this task.
- git diff --check, equation-tag uniqueness, delimiter-delta checks,
  changed-path inspection, and the protected-scope audit pass.
- Three independent read-only audits passed for final algebra,
  charging/test coverage, synchronization, and scope; their two wording
  clarifications were applied.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- research/FIXED_ORDER_CYCLE_RATIO.md: exact three-prefix charging, ordered
  weight reduction, compact proof, optimizer, and coefficient.
- tests/test_fixed_order_cycle_ratio.py: independent exact diagnostics only.
- research/ALL_N_LOWER_BOUND.md, start.md, PROJECT_KNOWLEDGE.md, and
  research/NEXT_RESEARCH_STEPS.md: synchronized authoritative consequences.
- CURRENT_STATUS.md and the new STRICT task dossier: durable handoff.

## Residual Limitations

- No finite floor/ceiling rounding theorem or threshold for the irrational
  three-prefix optimizer was derived.
- The rational two-prefix witness \(72825421/263424000\) remains the current
  explicit finite-\(n\) theorem from \(n=59\).
- No production, API, artifact, schema, example, verifier, backend,
  certificate, enumerator, or enumeration-limit path changed.
- No exact block residual, convergence theorem, matching upper bound, or
  exact geometric leading coefficient follows.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh STRICT task, derive an explicit finite floor/ceiling theorem for
the exact irrational three-prefix optimizer, including a minimal or
rigorously sufficient uniform threshold, without changing production,
artifacts, schemas, backends, certificates, or enumeration limits.
