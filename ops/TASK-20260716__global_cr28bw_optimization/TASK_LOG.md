# TASK LOG - Global CR28bw Optimization

## 2026-07-16 - Startup And Exact Weight Reduction

- Read the operating contract, project brief, stable knowledge, current
  status, the prior two-prefix and joint-optimization STRICT dossiers,
  CR28ax--CR28cc, and the existing independent test-local diagnostics.
- Confirmed a clean worktree on `main` at
  `b121fa2e0fc4ec1b2c06f10536b82021292c40e7`.
- Ran `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`; all 89
  pre-task tests passed.
- Classified the task as STRICT and fixed the scope to exact optimization,
  proof, test-local arithmetic, and durable-memory synchronization.
- Differentiated the two weight terms exactly. Strict concavity and monotonic
  ordering of their clipped individual optima show that the order constraint
  never requires pooling; the resulting density envelope has six exhaustive
  branches.

## 2026-07-16 - Global Density Classification In Progress

- Began independent handwritten and symbolic derivations of every smooth
  density branch and every closure face.
- Did not assume the supplied numerical point; it emerged from the
  middle--middle stationary equations and is now being compared against the
  full compact closure.

## 2026-07-16 - Exact Branch And Boundary Closure

- Reduced the ordered weight triangle to the six branches `00`, `M0`, `H0`,
  `MM`, `HM`, and `HH`; proved that an open diagonal point always has a
  feasible improving normal direction.
- Normalized the densities by \(1+\alpha\) and classified the fixed-\(\alpha\)
  global sequence
  \[
  00\longrightarrow MM\longrightarrow HM\longrightarrow HH
  \]
  at the exact transitions
  \(\alpha=1/3,77/139,301/419\).
- Classified the nonwinning one-prefix strata, every density transition,
  \(\alpha=0,1\), all three density collisions, all ordered-weight faces, and
  the nonunique weights attached to zero-length segments.
- Recorded exact closure maxima for all six reduced branches and used the
  rational separator \(553/2000\) to exclude every non-`MM` branch.

## 2026-07-16 - Global Maximum And Independent Arithmetic

- Derived the universal residual bound
  \[
  R\le{(A-X)X^2+(X-Y)Y^2\over8},
  \qquad A=3\alpha-1,
  \]
  whose normalized simplex maximum is uniquely
  \((X/A,Y/A)=(18/23,12/23)\).
- Reduced the equality envelope to
  \[
  E(\alpha)
  ={829\alpha^3-1887\alpha^2+1158\alpha+224\over1587}
  \]
  and obtained the unique relevant critical point
  \(\alpha_*=(629-23\sqrt{143})/829\).
- Evaluated every coordinate and the exact coefficient in
  \(\mathbb Q(\sqrt{143})\), recovering the supplied decimals without using
  them as premises.
- Added independent rational weight/branch scans, transition checks,
  branch-face checks, the exact simplex oracle, a compact-closure grid,
  quadratic-surd minimal-polynomial checks, rational isolating intervals,
  the \(\alpha=1\) quartic audit, and the \(\lambda_{\rm hi}=1\) face
  derivative identity.

## 2026-07-16 - Synchronization, Verification, And Handoff

- Synchronized the authoritative proof, all-\(n\) lower-bound note, project
  brief, stable knowledge, roadmap, current status, and this dossier.
- Preserved the exact distinction between the optimized asymptotic lower
  coefficient and the older rational finite theorem from \(n=59\).
- `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`: 94 passed.
- `python -m pytest`: 270 passed.
- Checked-artifact verification passed all 4 certificates and 76 local
  brackets; the schema selection passed 4 tests.
- Ruff passed on the changed test module. Repository-wide Ruff retained
  exactly four known findings in untouched files.
- `git diff --check`, mathematical-delimiter checks, changed-path inspection,
  and the protected-scope audit pass.
- Three independent read-only audits found no remaining mathematical,
  formatting, synchronization, or scope defect. Set the task to
  READY_FOR_REVIEW for user inspection and a manual commit decision.
