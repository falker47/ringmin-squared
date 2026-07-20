# TASK_STATUS - TASK-20260720 / Residue-Two PG49-Star W

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** fix one deterministic PG49-star analogue on the existing
  residue-two `e=2` scaffold at `n=10m+2`, `m>=1`; prove or refute its
  Ferrers/PG49 compatibility on every row; and, only if compatible, determine
  its exact product-distance score `W` from all cyclic positional distances.

## Fixed Candidate Before Scoring

Write the existing path indices as `0,...,2m-1`, and let
`q=kappa_(2m-1)` be the literal threshold of the genuine closing gap. The
only candidate admitted in this task is

\[
\alpha(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le m-1,\\
3m-1-j,&m\le j\le2m-2,\\
q,&j=2m-1.
\end{cases}
\]

Thus the closing gap receives `P_q`; every non-singleton path keeps its
existing orientation; and the complete singleton block
`P_(m+1),...,P_(2m-1)` is assigned in reverse order. The boundary row
`m=1` is literal: the singleton range is empty and `alpha=(1,0)`.

This map was fixed before any global score calculation and will not be
modified after score inspection. No alternative candidate belongs to this
task.

## Scope

- **In scope:** explicit map, image partition, exact Ferrers thresholds,
  residual Hall support, all empty ranges, `m=1`, genuine cyclic closure,
  and--only after compatibility--all positional distances needed for `W`.
- **Out of scope:** `K`, induced-subset scoring, candidate search or repair,
  production-code changes, angular or geometric consequences, and global
  minimizing-order or optimality claims.

## Exact Compatibility Result

Put

\[
d=8m+4,\qquad D=8m+3,\qquad
J={d(d-2)\over2}.
\]

For the literal residue-two paths, the exact local relation is

\[
N(G_j)=\{P_{\kappa_j},\ldots,P_{2m-1}\},\qquad
\kappa_j=
\left\lceil{(j-1)(D-1)\over2(D+j)}\right\rceil.
\]

The thresholds are nondecreasing,
\(\kappa_0=\kappa_1=0\), and
\(1\le\kappa_j\le j-1\) on the nonempty range
\(2\le j\le2m-1\). The genuine closing threshold is

\[
q=\kappa_{2m-1}
=\left\lceil{(m-1)(4m+1)\over5m+1}\right\rceil
=\begin{cases}
0,&m=1,\\
\lfloor(4m+1)/5\rfloor,&m\ge2.
\end{cases}
\]

The candidate images are the four disjoint blocks

\[
[0,q-1],\quad[q+1,m],\quad[m+1,2m-1],\quad\{q\},
\]

with every reversed or shifted interval interpreted literally when empty.
They partition all path indices and satisfy their Ferrers thresholds. Because
the first two thresholds are zero, the residual suffix Hall inequalities show
that every local edge is extendible: the Hall support is the entire local
board. Thus the fixed map is compatible for every \(m\ge1\); there is no
symbolic obstacle.

At \(m=1\), \(q=0\), both the initial and singleton ranges are empty,
\(\alpha=(1,0)\), and the expanded cyclic order is

\[
(11,4,7,8,3,12,2,10,6,9,5).
\]

For every row, the literal closing word is

\[
(n,2,A_q,c_q,B_q,4m+1,D).
\]

## Exact Score After Compatibility

All cyclic pairs at positional distances one and two satisfy the threshold
by the compatibility proof. The retained orientation of \(P_0\) supplies
\(A_0c_0=J\). Every distance-three pair has at most one terminal endpoint,
and every distance at least four has the uniform all-label bound:

\[
3J-n(D-1)=16m^2+36m+8>0,
\]

\[
4J-n(n-1)=28m^2+66m+14>0.
\]

Consequently

\[
\boxed{
W(\sigma_{\alpha^{(2)}_*})
=J
={(8m+4)(8m+2)\over2}
=32m^2+24m+4}
\qquad(m\ge1).
\]

## Verification State

- The symbolic proof and two independent mathematical audits agree.
- The sole bounded standalone standard-library diagnostic passes after
  formatting on its declared formula, Ferrers, Hall, closure, and all-pairs
  score limits.
- Scoped Ruff lint and format checks, full pytest (283 passed), the focused
  schema suite (4 passed), the checked-artifact verifier, and the scoped PGE2
  source audit all pass.
- A separate final read-only diff audit reports no defect.
- Final Git status, complete tracked/untracked inspection, and
  `git diff --check` pass.
- The task is ready for user review and a manual commit decision.

## Current Blocker

- None.
