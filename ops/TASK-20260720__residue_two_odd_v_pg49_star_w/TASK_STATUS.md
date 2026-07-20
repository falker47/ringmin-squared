# TASK_STATUS - TASK-20260720 / Residue-Two Odd-v PG49-Star W

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** on the odd branch `v=2m+1` of the existing residue-two
  scaffold, hence `n=10m+7` for every `m>=1`, fix one deterministic
  PG49-star analogue before any score; prove or refute its exact
  Ferrers/PG49 compatibility; and only if compatible audit every cyclic
  positional distance and determine its exact product-distance score `W`.

## Fixed Candidate Before Scoring

Put

\[
d=8m+8,\qquad D=8m+7,\qquad
J={d(d-2)\over2},
\]

and index the `2m+1` gaps and paths by `0,...,2m`.  The retained residue-two
paths are the oriented triples

\[
P_k=(D-1-2k,\ 4m+4+k,\ D-2-2k)
\qquad(0\le k\le m)
\]

and the singleton paths

\[
P_k=(4m+4+k)\qquad(m+1\le k\le2m).
\]

There is no doubleton on this parity branch; its type and index range are
identically empty.  Define

\[
\kappa_j=
\left\lceil{(j-1)(D-1)\over2(D+j)}\right\rceil,
\qquad
q=\kappa_{2m}.
\]

Before any full-order score calculation, the sole candidate admitted in this
task is fixed as

\[
\alpha^{(2,\mathrm{odd})}_*(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le m-1,\\
3m-j,&m\le j\le2m-1,\\
q,&j=2m.
\end{cases}
\]

Thus the actual closing gap receives `P_q`, the residual triples shift by one,
and the entire singleton block is assigned in reverse path-index order.  The
triple orientations are unchanged, a singleton has no internal orientation,
and no doubleton is introduced.  This map will not be repaired, replaced, or
changed after its score is inspected.  No alternative candidate belongs to
this task.

## Scope

- **In scope:** literal scaffold and path orientations; exact threshold and
  image formulas; bijectivity; residual Hall support; all empty ranges; the
  minimum row `m=1`; the genuine cyclic closure; and, only after exact
  compatibility, every positional distance needed for `W`.
- **Out of scope:** `K`; induced-subset scoring; candidate, matching,
  permutation, path-assignment, or order search; production-code changes;
  angular or geometric consequences; and global minimizing-order or
  optimality claims.

## Provenance Note

The authoritative construction/`W` odd-parity precedent in
`research/PRODUCT_DISTANCE_SURROGATE.md` is tagged (PGODD-1)--(PGODD-27).
The separate 36-tag sequence is (KPGODD-1)--(KPGODD-36) and concerns `K`, so
it is excluded from this task except as a read-only literal-word convention.
The other controlling precedent is (PGE2-1)--(PGE2-29).

## Verification

- **Exact compatibility result:** the local relation is
  \(k\ge\kappa_j\), every local edge is Hall-extendible, and the fixed map is
  a supported bijection for every \(m\ge1\).  The exact closing threshold is
  \[
  q=\kappa_{2m}
  =\left\lfloor{4m+3\over5}\right\rfloor,
  \qquad 1\le q\le m.
  \]
  Its four image blocks are
  \([0,q-1]\), \([q+1,m]\), \([m+1,2m]\), and \(\{q\}\).
  The shifted-triple range is empty exactly at \(m=1,2,3\); the singleton
  block is always nonempty and the doubleton class is always empty.
- **Minimum row:** \(q=1\), \(\kappa=(0,0,1)\),
  \(\alpha=(0,2,1)\), and the expanded order is
  \[
  (15,6,14,8,13,5,16,4,10,3,17,2,12,9,11,7).
  \]
- **Literal closure:** \((n,2,A_q,c_q,B_q,4m+3,D)\).
- **Verification completed:** exact all-distance score, sole bounded
  diagnostic, scoped Ruff checks, source-structure audit, full pytest,
  focused schema suite, and checked-artifact verifier all pass.
- **Independent audits:** three read-only reviews of compatibility,
  all-distance scoring/diagnostic code, and authoritative synchronization
  report PASS after the recorded status cleanup.

## Exact Score After Compatibility

Distances one and two are covered cyclically by the compatibility proof, and
the retained edge \(A_0c_0\) attains \(J\).  Every distance-three pair has at
most one terminal endpoint, while every distance at least four has the
uniform distinct-label bound.  The strict margins are

\[
3J-n(D-1)=16m^2+52m+30>0,
\]

\[
4J-n(n-1)=28m^2+94m+54>0.
\]

Consequently

\[
\boxed{
W(\sigma_{\alpha^{(2,\mathrm{odd})}_*})
=J
={(8m+8)(8m+6)\over2}
=32m^2+56m+24}
\qquad(m\ge1).
\]

This is an exact fixed-construction score, not an evaluation of \(K\) or a
geometric or global statement.

## Bounded Diagnostic

The task's sole standalone standard-library diagnostic constructs only
(PGE2ODD-6).  It passes on:

- formula, image, orientation, empty-range, and Ferrers rows
  \(m=1,\ldots,1000\), totaling 1,002,000 candidate-image entries;
- literal local-relation and residual-Hall rows \(m=1,\ldots,40\), totaling
  91,880 local checks and 5,557,960 suffix inequalities;
- exact all-pairs cyclic score rows \(m=1,\ldots,80\), totaling 8,873,400
  unordered pairs.

It checks the no-doubleton classification, minimum row, and true closure,
imports no project or test helper, searches no alternative object, and
computes no \(K\).

## Blockers / Risks

- **Current blocker:** none.
- The missing doubleton is a genuine parity feature of (R2C5), not a path to
  be synthesized.  Any argument that silently imports the PGODD doubleton
  would analyze the wrong core.
- The bounded diagnostic corroborates but cannot replace the exact symbolic
  all-\(m\) proof.
- The repository contains PGODD tags only through 27; the 36-tag theorem is
  KPGODD and remains out of scope.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** (PGE2ODD-1)--(PGE2ODD-29) are an exact
  all-domain construction/compatibility/\(W\) theorem; the sole diagnostic
  and repository verification suite pass.
- **Files changed:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** this file, `EVIDENCE.md`, and the PGE2ODD
  section of `research/PRODUCT_DISTANCE_SURROGATE.md`.
