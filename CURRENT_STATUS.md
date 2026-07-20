# CURRENT_STATUS - power-ringmin

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** classify the one pre-fixed even-\(v\), residue-two
  PG49-star analogue on \(n=10m+2\), \(m\ge1\), and determine only its exact
  product-distance score \(W\) if compatible.
- **Repository state at startup:** clean main worktree at commit
  513f294d6c7e79e899d953f8b197ae3e23cded73.
- **Implementation state:** exact compatibility and \(W\) theorems are proved
  and synchronized; the sole bounded diagnostic passes.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

On the existing residue-two \(e=2\) scaffold, fix exactly one deterministic
analogue before scoring: place the path at the genuine final threshold in the
closing gap, preserve every non-singleton path orientation, and reverse the
maximum parity-compatible singleton block. Prove or refute compatibility on
every row, including image partition, Ferrers thresholds, Hall support, empty
ranges, \(m=1\), and cyclic closure. Only after compatibility, determine
\(W\) from all cyclic positional distances.

The task excludes \(K\), alternative-candidate search or repair, production
code, angular or geometric consequences, global minimizing-order claims, and
global optimality.

## Fixed Map Before Score

Put

\[
q=\kappa_{2m-1}
=\left\lceil{(m-1)(4m+1)\over5m+1}\right\rceil
=\begin{cases}
0,&m=1,\\
\lfloor(4m+1)/5\rfloor,&m\ge2.
\end{cases}
\]

The only admitted map is

\[
\alpha^{(2)}_*(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le m-1,\\
3m-1-j,&m\le j\le2m-2,\\
q,&j=2m-1.
\end{cases}
\]

It was fixed before any full-order score was calculated and was never
altered after score inspection.

## Exact Compatibility Theorem

With \(d=8m+4\), \(D=d-1=8m+3\), and
\(J=d(d-2)/2\), the literal local relation is

\[
N(G_j)=\{P_{\kappa_j},\ldots,P_{2m-1}\},\qquad
\kappa_j=
\left\lceil{(j-1)(D-1)\over2(D+j)}\right\rceil.
\]

The thresholds are nondecreasing,
\(\kappa_0=\kappa_1=0\), and
\(1\le\kappa_j\le j-1\) on \(2\le j\le2m-1\). The four map images are

\[
[0,q-1],\qquad[q+1,m],\qquad[m+1,2m-1],\qquad\{q\}.
\]

Every empty range is literal. These blocks are disjoint, exhaustive, and
Ferrers-supported. The residual suffix Hall inequalities prove that every
local edge is extendible, including both threshold-zero columns. Therefore
the fixed map is compatible for every \(m\ge1\); there is no symbolic
obstacle.

At \(m=1\), \(q=0\), the singleton and first image ranges are empty,
\(\alpha^{(2)}_*=(1,0)\), and the expanded cyclic order is

\[
(11,4,7,8,3,12,2,10,6,9,5).
\]

The genuine closing word on every row is

\[
(n,2,A_q,c_q,B_q,4m+1,D).
\]

## Exact Product-Distance Score

Compatibility covers every cyclic positional distance one and two. The
retained \(P_0\) orientation supplies \(A_0c_0=J\). Terminal separation and
the all-label bound give the strict remaining margins

\[
3J-n(D-1)=16m^2+36m+8>0,
\]

\[
4J-n(n-1)=28m^2+66m+14>0.
\]

Thus

\[
\boxed{
W(\sigma_{\alpha^{(2)}_*})
=J
={(8m+4)(8m+2)\over2}
=32m^2+24m+4}
\qquad(m\ge1).
\]

This is an exact theorem for one fixed combinatorial construction only.

## Verification

- The sole standalone standard-library diagnostic constructs only (PGE2-6)
  with explicit limits \(m\le1000\) for formula/Ferrers checks, \(m\le40\)
  for literal relation/Hall checks, and \(m\le80\) for exact all-pairs
  scoring. It passes on 1,001,000 image entries, 88,560 local relations,
  5,290,640 Hall inequalities, and 8,710,200 unordered cyclic pairs.
- Scoped Ruff lint and final format checks pass. The first format check found
  one mechanical delta; Ruff formatted the standalone script and its
  post-format diagnostic rerun passes.
- Full pytest passes: 283 passed.
- The focused checked-artifact schema suite passes: 4 passed.
- The standalone checked-artifact verifier passes for four certificates,
  76 local brackets, and \(n=3,4,5,6\).
- The corrected scoped source audit passes with 29 sequential unique PGE2
  tags, 34 balanced displays, balanced math environments, no control
  characters, and no missing `\left` token. Its first invocation failed
  before inspecting the source because of a PowerShell interpolation error;
  that command was corrected and rerun successfully.
- Two independent mathematical audits reproduce the compatibility and score
  results. Their two editorial findings were corrected.
- A separate final read-only diff audit reports no mathematical, scope, or
  synchronization defect.
- Final Git status, complete tracked and untracked diff inspection, and
  `git diff --check` pass. Only the five intended documentation/memory files
  and the one task dossier are modified or untracked.

## Evidence Classification And Limitations

- (PGE2-1)--(PGE2-25) are an **exact all-domain combinatorial compatibility
  theorem**.
- (PGE2-26)--(PGE2-29) are an **exact fixed-order product-distance theorem**.
- The standalone diagnostic is **bounded exact computation** corroborating,
  not replacing, the symbolic proof.
- No \(K\), alternative candidate, production change, angular, geometric,
  global-minimizer, global-optimality, or upstream Ringmin conclusion is
  asserted or inferred.

## Files In Scope

- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260720__residue_two_pg49_star_w/`

## Proposed Next Task

In a fresh STRICT task, evaluate the induced-subset objective \(K\) for this
same unchanged even-\(v\) core, with all empty ranges and cyclic shortcuts
proved exactly and without inferring geometry or global optimality.
