# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** exact global optimization of the two-prefix CR28bw
  coefficient.
- **Current task:** reduce the ordered weights, classify every internal
  branch, transition, compact face, and density collision, and determine the
  exact global coefficient.
- **Task dossier:** `ops/TASK-20260716__global_cr28bw_optimization/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- Reduced the ordered \(\lambda\)-optimization exactly.
- Classified all six reduced branches, both nontrivial fixed-density
  transitions, the endpoint faces, the order diagonal, and every density
  collision.
- Proved the unique global maximizer and exact coefficient without assuming
  the supplied numerical point.
- Added independent rational and \(\mathbb Q(\sqrt{143})\) diagnostics.
- Kept finite rounding at the irrational optimizer, production code,
  artifacts, schemas, backends, certificates, enumerators, and enumeration
  limits outside scope.

## Exact Ordered-Weight Reduction

With \(s=1+\alpha\), each weight summand is strictly concave and has unique
optimum
\[
\psi_s(\beta)=
\begin{cases}
0,&\beta\le s/4,\\
4-s/\beta,&s/4<\beta<s/3,\\
1,&\beta\ge s/3.
\end{cases}
\]
Since \(\psi_s\) is nondecreasing,
\(\beta_2<\beta_1\) automatically gives
\(\lambda_{\rm lo}\le\lambda_{\rm hi}\). There is no pooled interior KKT
branch. The exact reduced floor is
\[
\Phi_s(\beta)=
\begin{cases}
0,&\beta\le s/4,\\
(4\beta-s)^2/2,&s/4\le\beta\le s/3,\\
(4s\beta-s^2-2\beta^2)/2,&\beta\ge s/3,
\end{cases}
\]
and
\[
\overline C_2
=p(\alpha)+(\alpha-\beta_1)\Phi_s(\beta_1)
+(\beta_1-\beta_2)\Phi_s(\beta_2).
\]

## Branches And Transitions

The six exhaustive branches are `00`, `M0`, `H0`, `MM`, `HM`, and `HH`.
For the fixed-\(\alpha\) global density envelope:
\[
\begin{array}{c|c}
\alpha\text{ range}&\text{branch}\\ \hline
[0,1/3]&00\\
(1/3,77/139)&MM\\
(77/139,301/419)&HM\\
(301/419,1)&HH.
\end{array}
\]
The nontrivial junctions are
\[
\left({77\over139},{72\over139},{66\over139},1,{8\over11}\right),
\qquad
\left({301\over419},{270\over419},{240\over419},1,1\right),
\]
in the order
\((\alpha,\beta_1,\beta_2,\lambda_{\rm hi},\lambda_{\rm lo})\).

The exact closure maxima of the six branches are
\[
\begin{array}{c|cccccc}
&00&M0&H0&MM&HM&HH\\ \hline
\max C_2&
2(\sqrt2-1)/3&
(4+2\sqrt3)/27&
13/48&
C_{2,*}&
59/216&
13/48.
\end{array}
\]
Every density collision
\(\beta_2=0\), \(\beta_2=\beta_1\), or \(\beta_1=\alpha\) reduces to the
one-prefix problem. Vanishing segment lengths make the corresponding weight
nonunique but create no further global maximizer.

## Unique Global Maximizer

The exact global point is
\[
\boxed{
\begin{aligned}
\alpha_*&={629-23\sqrt{143}\over829},\\
\beta_{1,*}&={2286-77\sqrt{143}\over3316},\\
\beta_{2,*}&={2010-59\sqrt{143}\over3316},\\
\lambda_{{\rm hi},*}&={6264-288\sqrt{143}\over5281},\\
\lambda_{{\rm lo},*}&={3888-192\sqrt{143}\over4273}.
\end{aligned}}
\]
The exact coefficient is
\[
\boxed{
C_{2,*}={491596+6578\sqrt{143}\over2061723}
}
=0.276592655350947\ldots .
\]
The point reproduces the supplied decimals but was derived independently.
It satisfies
\[
829\alpha_*^2-1258\alpha_*+386=0,
\]
\[
6185169C_{2,*}^2-2949576C_{2,*}+342644=0.
\]

## Global Proof And Consequence

For \(A=3\alpha-1\), \(X=4\beta_1-s\), and \(Y=4\beta_2-s\),
\[
\Phi_s(\beta)\le{(4\beta-s)^2\over2},
\qquad
R\le{(A-X)X^2+(X-Y)Y^2\over8}.
\]
The normalized simplex has the unique maximum
\((X/A,Y/A)=(18/23,12/23)\), giving
\[
C_2\le
p(\alpha)+{27(3\alpha-1)^3\over1058}.
\]
The unique relevant critical point of this cubic is \(\alpha_*\), and the
upper bound is attained there on `MM`. Therefore
\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{2,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{2,*}\over\pi}.
\]
This is a method-specific template optimum, not an exact residual, limit, or
geometric leading coefficient.

## Independent Diagnostics

- Exact rational ordered-weight scans realize all six branches and verify
  the clipped optima against an ordered weight grid.
- Rational branch checks verify the transition values
  \(77/139\) and \(301/419\).
- A denominator-46 simplex scan has the unique maximum
  \((18/23,12/23)\).
- A denominator-32 compact-closure grid lies below the exact surd
  coefficient.
- \(\mathbb Q(\sqrt{143})\) arithmetic verifies the five coordinates, their
  minimal polynomials, strict domain inequalities, coefficient equation, and
  rational isolating intervals.
- The rational separator \(553/2000\) distinguishes \(C_{2,*}\) from every
  competing branch maximum using pure-integer square differences.

## Verification

- Global-optimization selection: 5 passed.
- Complete fixed-order-cycle-ratio module: 94 passed.
- Complete local suite: 270 passed.
- Checked-artifact verifier: all 4 certificates, 76 local brackets, and the
  \(n=3,4,5,6\) summary verified.
- Checked-artifact schema selection: 4 passed.
- Ruff on the changed test module: passed.
- Repository-wide Ruff retains exactly four known findings in untouched
  files; none belongs to this task.
- `git diff --check`, mathematical-delimiter checks, changed-path inspection,
  and the protected-scope audit pass.
- Three independent read-only audits found no remaining mathematical,
  formatting, synchronization, or scope defect.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md`: exact ordered-weight reduction, six
  branches, transitions, faces/collisions, global proof, optimizer, and
  coefficient.
- `tests/test_fixed_order_cycle_ratio.py`: independent rational and
  \(\mathbb Q(\sqrt{143})\) diagnostics only.
- `research/ALL_N_LOWER_BOUND.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, and `research/NEXT_RESEARCH_STEPS.md`:
  synchronized authoritative consequences and roadmap.
- `CURRENT_STATUS.md` and the new STRICT task dossier: durable handoff.

## Residual Limitations

- No finite floor/ceiling rounding theorem or threshold for the irrational
  optimizer was derived.
- The rational witness \(72825421/263424000\) remains the explicit
  finite-\(n\) theorem from \(n=59\).
- No production, API, artifact, schema, example, verifier, backend,
  certificate, enumerator, or enumeration-limit path changed.
- No exact block residual, convergence theorem, matching upper bound, or
  exact geometric leading coefficient follows.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh STRICT task, derive an explicit finite floor/ceiling theorem for
the irrational CR28bw optimizer, including a minimal or rigorously sufficient
uniform threshold, without changing production, artifacts, schemas, backends,
or enumeration limits.
