# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

- **Current phase:** exact global optimization of the direct four-prefix
  asymptotic coefficient.
- **Current task:** classify the full compact four-prefix parameter problem
  and prove its global maximum.
- **Task dossier:**
  ops/TASK-20260717__global_four_prefix_optimization/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Global Four-Prefix Result

The four ordered weights reduce independently to their clipped optima on

\[
0\le\beta_4\le\beta_3\le\beta_2\le\beta_1\le\alpha\le1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
\]

There are exactly fifteen clipping regimes
\(H^hM^m0^{4-h-m}\). At fixed \(\alpha\), the winner moves through

\[
0000\longrightarrow MMMM\longrightarrow HMMM
\longrightarrow HHMM\longrightarrow HHHM;
\]

the formal transition to `HHHH` lies beyond \(\alpha=1\). Every clipping
transition, density collision, zero-length degeneracy, and compact facet is
audited.

The unique global point lies strictly in `MMMM`. With

\[
\alpha_*={18170840871749-3666143\sqrt{2903456040383}
 \over27631313622349},
\qquad A_*=3\alpha_*-1,
\]

\[
(x_1,x_2,x_3,x_4)
={1\over3666143}(3190338,2672508,2091528,1394352),
\]

the unique remaining parameters are

\[
\beta_{i,*}={1+\alpha_*+x_iA_*\over4},
\qquad
\lambda_{i,*}={x_iA_*\over\beta_{i,*}}.
\]

The exact coefficient is

\[
\boxed{
C_{4,*}
={597580022071777213687318156
 +21288970076515705538\sqrt{2903456040383}
 \over2290468477489828247376833403}
=0.2767361498609895101\ldots .
}
\]

It satisfies the strict comparison

\[
C_{3,*}<{2767\over10000}<C_{4,*},
\]

and therefore

\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{4,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{4,*}\over\pi}.
\]

## Independent Diagnostic

The standalone standard-library diagnostic checks exact clipping-gap
factorizations on rational grids, both \(C^1\) joins, all fifteen branch
witnesses, exact transition weights and collision reductions, the specialized
nonnegative \(k=4\) simplex identity, end-to-end original-objective evaluation
at the surd optimizer, its primitive irreducible polynomial and isolating
interval, and both exact squared comparisons with the rational separator. The
strengthened run passes.

## Protected Scope

- No finite rounding in \(n\).
- No five-prefix charging or optimization.
- No production source, public API, artifact, schema, verifier, backend,
  certificate, enumerator, or enumeration-limit change.
- No exact residual, convergence theorem, or geometric leading constant.

## Verification

- Strengthened standalone exact diagnostic: PASS.
- Focused fixed-order proof-note regression: 101 tests passed.
- Complete local suite: 283 tests passed.
- Checked-artifact semantic verifier: 4 certificates and 76 local brackets.
- Schema-selection regression: 4 tests passed, with one non-failing cache
  warning.
- Historical four-prefix literal oracle: PASS over 840 histories.
- Historical normalized-simplex diagnostic: PASS through \(k=8\) and 203,489
  grid states.
- Ruff lint/format, Markdown structure, exact-value consistency, protected
  scope, full diff inspection, and `git diff --check`: PASS.
- Three independent read-only audits covered proof completeness, diagnostic
  algebra, and cross-source consistency; all actionable findings were
  corrected and rechecked.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md`: full exact theorem, compact reduction,
  branch/transition/facet classification, optimizer, uniqueness, and strict
  comparison.
- `research/ALL_N_LOWER_BOUND.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md`: synchronized authoritative result and
  roadmap.
- `CURRENT_STATUS.md`: final task state.
- `ops/TASK-20260717__global_four_prefix_optimization/`: STRICT dossier and
  independent exact diagnostic.

## Proposed Next Task

In a fresh STRICT task, audit one explicit nonlocal middle-path reassignment
of the current \(8/25\) product-distance upper construction, with no expanded
enumeration and a full cyclic-distance proof.
