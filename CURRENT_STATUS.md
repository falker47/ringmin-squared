# CURRENT_STATUS - power-ringmin

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** fix and classify one deterministic PG49-star analogue on
  the odd-\(v\) branch of the residue-two scaffold,
  \(n=5v+2=10m+7\), \(v=2m+1\), \(m\ge1\).
- **Repository state at startup:** clean main worktree at commit
  f4e48e43aee9e9348e68e6c36486ae61c9898b88.
- **Implementation state:** exact construction, Ferrers/Hall compatibility,
  all-distance \(W\), sole bounded diagnostic, authoritative synchronization,
  independent audits, repository regression, and diff hygiene are complete.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Fixed Candidate Before Scoring

Put

\[
d=8m+8,\qquad D=8m+7,\qquad
J={d(d-2)\over2},
\]

and retain the residue-two paths

\[
P_k=(D-1-2k,\ 4m+4+k,\ D-2-2k)
\qquad(0\le k\le m),
\]

\[
P_k=(4m+4+k)\qquad(m+1\le k\le2m).
\]

Thus this parity branch has \(m+1\) oriented triples, \(m\) singletons, and
no doubleton.  With

\[
\kappa_j=
\left\lceil{(j-1)(D-1)\over2(D+j)}\right\rceil,
\qquad
q=\kappa_{2m}=\left\lfloor{4m+3\over5}\right\rfloor,
\]

the sole pre-score map is

\[
\alpha^{(2,\mathrm{odd})}_*(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le m-1,\\
3m-j,&m\le j\le2m-1,\\
q,&j=2m.
\end{cases}
\]

It closes with the threshold triple \(P_q\), shifts the residual triples,
and reverses the complete singleton block.  No path orientation is changed,
and no candidate was repaired or replaced after scoring.

## Exact Compatibility Theorem

For every \(m\ge1\),

\[
N(G_j)=\{P_{\kappa_j},\ldots,P_{2m}\},
\qquad
(k,j)\in\mathcal R_{\rm loc}
\Longleftrightarrow k\ge\kappa_j.
\]

The thresholds are nondecreasing,
\(\kappa_0=\kappa_1=0\), \(\kappa_2=1\), and
\(1\le\kappa_j\le j-1\) for \(2\le j\le2m\).  Residual suffix Hall proves

\[
\mathcal R_{\rm ext}=\mathcal R_{\rm loc};
\]

every local edge is extendible.  The fixed map has the four images

\[
[0,q-1],\qquad[q+1,m],\qquad[m+1,2m],\qquad\{q\},
\]

which are disjoint, exhaustive, and supported.  The shifted-triple range is
empty exactly for \(m=1,2,3\); the singleton block is always nonempty and
its reversal is order-neutral only at \(m=1\); the doubleton class is empty
on every row.

At the minimum row,

\[
(m,d,D,n,J,q)=(1,16,15,17,112,1),\qquad
\kappa=(0,0,1),\qquad
\alpha=(0,2,1),
\]

and the complete expanded order is

\[
(15,6,14,8,13,5,16,4,10,3,17,2,12,9,11,7).
\]

The genuine closing word is

\[
(n,2,A_q,c_q,B_q,4m+3,D).
\]

These statements are the exact all-domain theorem
(PGE2ODD-1)--(PGE2ODD-25).

## Exact Product-Distance Score

Compatibility covers all cyclic distances one and two.  The retained edge
\(A_0c_0=J\) supplies equality.  The strict remaining margins are

\[
3J-n(D-1)=16m^2+52m+30>0,
\]

\[
4J-n(n-1)=28m^2+94m+54>0.
\]

Therefore every unordered cyclic pair is covered and

\[
\boxed{
W(\sigma_{\alpha^{(2,\mathrm{odd})}_*})
=J
={(8m+8)(8m+6)\over2}
=32m^2+56m+24}
\qquad(m\ge1).
\]

This is the exact fixed-construction theorem
(PGE2ODD-26)--(PGE2ODD-29).  It does not evaluate \(K\), inspect an
alternative, alter production, or imply an angular, geometric,
global-minimizer, or global-optimality conclusion.

## Verification

- The sole standalone standard-library diagnostic constructs only
  (PGE2ODD-6).  It passes through \(m=1000\) for formulas/images,
  \(m=40\) for the literal local relation and Hall support, and \(m=80\)
  for every unordered cyclic pair: 1,002,000 image entries, 91,880 local
  checks, 5,557,960 Hall inequalities, and 8,873,400 cyclic pairs.
- Three independent read-only audits of compatibility, scoring/diagnostic
  code, and synchronization/scope pass.
- Scoped Ruff lint and post-format checks pass.  The first format check
  found one mechanical delta, which was applied before the passing reruns.
- The first post-format diagnostic rerun used an insufficient 10-second
  timeout and was terminated; the unchanged 120-second rerun passes in
  38 seconds.
- The PGE2ODD source audit passes with 29 sequential unique tags,
  34 balanced displays, balanced environments, and no control characters.
- Full pytest passes: 283 passed.
- The focused checked-artifact schema suite passes: 4 passed.
- The standalone checked-artifact verifier passes for four certificates,
  76 local brackets, and \(n=3,4,5,6\).
- Final Git status, complete tracked/untracked diff inspection, and
  whitespace hygiene pass.

## Evidence Classification And Provenance

- (PGE2ODD-1)--(PGE2ODD-25) are an **exact all-domain combinatorial
  compatibility theorem**.
- (PGE2ODD-26)--(PGE2ODD-29) are an **exact all-domain fixed-construction
  product-distance theorem**.
- The standalone diagnostic is **bounded exact computation** corroborating,
  not replacing, those proofs.
- The authoritative construction/\(W\) odd-parity precedent is
  (PGODD-1)--(PGODD-27).  The repository's 36-tag sequence is KPGODD,
  concerns \(K\), and was not evaluated in this task.

## Files In Scope

- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260720__residue_two_odd_v_pg49_star_w/

## Proposed Next Task

In a fresh STRICT task, and only if explicitly selected, evaluate the
induced-subset objective \(K\) of the unchanged core fixed by (PGE2ODD-6),
without changing the construction or inferring geometry or global
optimality.
