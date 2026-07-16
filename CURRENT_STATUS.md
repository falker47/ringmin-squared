# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** exact obstruction for one parametric perturbation of the
  \(8/25\) upper construction.
- **Current task:** reverse one triple path in the symbolic residue-three
  branch and determine the full-distance score.
- **Task dossier:**
  ops/TASK-20260716__one_triple_reversal_obstruction/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact One-Triple Reversal Obstruction

For

\[
n=10m+3,
\qquad m\ge3,
\qquad d=8m+4,
\qquad T={d(d-1)\over2},
\]

the symbolic eight-twenty-fifths order has triple paths

\[
P_s=(d-1-2s,\ 4m+2+s,\ d-2-2s),
\qquad 0\le s\le m.
\]

Let \(\tau_{m,s}\) reverse only the two outer entries of \(P_s\). Then

\[
\boxed{
W(\tau_{m,s})=
\begin{cases}
(d^2-1)/2=T+(d-1)/2,&s=0,\\
T,&1\le s\le m.
\end{cases}}
\]

The distance-class maxima are

\[
M_1=T,
\qquad
M_2=W(\tau_{m,s}),
\qquad
M_3={(5m+2)(9m+5)\over3}<T,
\]

\[
M_{\ge4}={n(n-1)\over4}<T.
\]

For the canonical cut, the exact closing maxima are

\[
C_1=(4m+1)d,
\qquad
C_2={(6m+1)d\over2},
\qquad
C_3={(4m+1)(d-1-\mathbf1_{\{s=0\}})\over3},
\]

all strictly below \(T\).

## Exact Obstruction And Counterexample

The edge \(\{4m+2,d-1\}\) remains adjacent after every allowed reversal
and always has product \(T\). Thus no member improves even the finite
threshold. For \(s\ge1\), the distance-two pair \((d,d-1)\) also remains
saturated. For \(s=0\), the new distance-two pair
\((d-1,d+1)\) raises the score by \((d-1)/2\).

Consequently, for every parameter choice \(s=s(m)\),

\[
{W(\tau_{m,s(m)})\over(10m+3)^2}\longrightarrow{8\over25}.
\]

The smallest admitted non-neutral row is the reproducible exact
counterexample

\[
(m,s,n,d)=(3,0,33,28),
\qquad
T=378,
\qquad
W={783\over2},
\]

attained at distance two by \((27,29)\).

## Surrogate / Geometry Separation

The theorem is exact for the product-distance surrogate. Applying the
established regular-direction construction and radius-one insertion gives
only

\[
R_2^*(10m+3)
\le{(10m+2)W(\tau_{m,s})\over\pi}.
\]

For \(s\ge1\), this reproduces the existing upper bound on the subsequence;
for \(s=0\), it is weaker. It is not a geometric lower bound, an exact
fixed-order geometric threshold, a convergence theorem, or an obstruction to
other directions or order families.

## Verification

- The standalone standard-library diagnostic reconstructs the block family
  without project/test imports and passes six selected exact rows.
- The six new parametrized tests pass through two independent all-pairs
  traversals and the production scorer.
- The complete product-distance module passes 49 tests.
- The complete 283-test local suite passes outside the filesystem sandbox;
  the first sandboxed run retained 31 temporary-directory setup errors and no
  failed test body.
- Checked-artifact semantic verification accepts 4 certificates and 76 local
  brackets; the schema-selection suite passes 4 tests.
- Ruff passes on the changed Python paths.
- Three independent read-only mathematical audits found no counterexample or
  scope defect.
- The primary proof has 179 unique equation tags, 309 balanced display-math
  pairs, and balanced aligned environments.
- Strict UTF-8, changed-path scope, protected-source scope, complete diff
  review, `git diff --check`, and final worktree inspection pass.

## Files Changed

- `research/PRODUCT_DISTANCE_SURROGATE.md`: exact family definition, all
  distance classes, closure, obstruction, and geometry separation.
- `tests/test_product_distance.py`: six small exact generated-order controls.
- `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and
  `research/NEXT_RESEARCH_STEPS.md`: synchronized authoritative memory and
  roadmap.
- `ops/TASK-20260716__one_triple_reversal_obstruction/`: STRICT dossier and
  independent standard-library diagnostic.

## Protected Limitations

- Only the one-triple reversal family on \(n\equiv3\pmod{10}\),
  \(n\ge33\), is classified.
- No production generator, public API, enumerator, enumeration limit,
  artifact, schema, interval backend, or certificate changed.
- No new best surrogate value, global upper coefficient, geometric lower
  bound, exact geometric leading coefficient, or convergence result follows.

## Proposed Next Task

In a fresh STRICT task, audit one explicit nonlocal reassignment of the
symbolic middle paths among terminal gaps, again with a full cyclic-distance
proof and no expanded enumeration.
