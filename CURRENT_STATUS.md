# CURRENT_STATUS - power-ringmin

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** classify the fixed odd-\(v\) PG49-star parity analogue on
  \(n=10m+8\) through construction, Ferrers/PG49 compatibility, and exact
  product-distance score \(W\) only.
- **Repository state at startup:** clean main worktree at commit
  c45a5dc7133670874bc76246684cc7d8ed323f89.
- **Implementation state:** the candidate was fixed before scoring; its
  search-free formula, odd Ferrers thresholds, exact extendible support,
  image partition, boundary rows, literal cyclic closure, and all
  distance classes for \(W\) are proved and synchronized. The sole bounded
  independent diagnostic and repository-proportional checks pass.
- **Current blocker:** none.
- **Current next atomic action:** user review; a fresh STRICT task may
  evaluate \(K\) for this already fixed order without changing it.
- **Awaiting user review:** yes.

## Objective And Scope

On the canonical eight-twenty-fifths scaffold with

\[
n=10m+8,\qquad v=2m+1,\qquad d=8m+8,\qquad m\ge1,
\]

determine whether the odd-\(v\) analogue that moves the threshold path into
the genuine closing gap and reverses the singleton block is a
Ferrers/PG49-compatible bijection on its whole symbolic domain. Evaluate
only its exact fixed-order score \(W\).

The task excludes \(K\), induced-subset maximizers, angular or geometric
claims, global minimizing-order or optimality conclusions, and production
changes.

## Exact Construction

Let

\[
\kappa_j=
\left\lceil{j(d-1)\over2(d+j)}\right\rceil,
\qquad
q=\kappa_{2m}=\left\lfloor{4m+5\over5}\right\rfloor.
\]

The fixed map is

\[
\alpha^\circ(j)=
\begin{cases}
0,&j=0,\\
j,&1\le j<q,\\
j+1,&q\le j\le m,\\
3m+1-j,&m+1\le j\le2m-1,\\
q,&j=2m.
\end{cases}
\]

It shifts the residual triples and the doubleton one gap left, preserves the
doubleton orientation, reverses only the actual singleton block, and places
\(P_q\) in \(G_{2m}\). Its five images are

\[
\{0\},\quad[1,q-1],\quad[q+1,m+1],\quad
[m+2,2m],\quad\{q\},
\]

which are pairwise disjoint and complete.

## Exact Compatibility And Boundaries

The newly derived odd local relation is

\[
(k,j)\in\mathcal R^{\rm odd}_{\rm loc}
\quad\Longleftrightarrow\quad
k\ge\kappa_j.
\]

The doubleton and singleton rows are strictly universal. Nested-neighborhood
Hall inequalities give the exact extendible support

\[
\mathcal R^{\rm odd}_{\rm ext}
=\{(0,0)\}\mathbin\cup
\{(k,j):1\le j\le2m,\ \kappa_j\le k\le2m\}.
\]

Every image of \(\alpha^\circ\) lies in this support. The closing image is
the exact threshold equality
\(\alpha^\circ(2m)=q=\kappa_{2m}\), checked in the literal word

\[
(n,2,A_q,c_q,B_q,4m+3,d).
\]

At \(m=1\), the singleton range is empty and
\(\alpha^\circ=(0,2,1)\); at \(m=2\), singleton reversal is order-neutral.
The equality \(q=m\) holds exactly for \(1\le m\le5\), when the shifted
third image block reduces to the doubleton at its endpoint.

## Exact Score

Compatibility controls every pair at positional distance one or two.
The fixed path \(P_0\subset G_0\) supplies

\[
A_0c_0=T={d(d-1)\over2}.
\]

No distance-three pair contains two terminals, so its score is strictly
below \(T\) by \(3d-2n=4m+8>0\). Every distance at least four is strictly
below \(T\) because

\[
4T-n(n-1)=28m^2+90m+56>0.
\]

Therefore

\[
W(\sigma_{\alpha^\circ})
=T
={(8m+8)(8m+7)\over2}
\qquad(m\ge1).
\]

No obstruction occurs.

## Verification

- The sole bounded integer diagnostic passes. Formula, image, and Ferrers
  checks cover \(m=1,\ldots,1000\); local-relation and residual-Hall checks
  cover \(m=1,\ldots,40\); exact all-pairs scoring covers
  \(m=1,\ldots,80\), including 8,906,280 unordered cyclic pairs.
- Full pytest passes: 283 passed.
- The focused checked-artifact schema suite passes: 4 passed.
- The standalone checked-artifact verifier passes:
  certificates=4, local_brackets=76, n=3,4,5,6.
- Standalone syntax, scoped Ruff lint, and Ruff format checks pass for the
  sole new Python file.
- The source audit passes with 27 sequential unique PGODD tags, balanced
  displays and environments, no unescaped TeX control word, and no control
  character.
- The initial diagnostic-domain defect, initial Ruff formatting failure,
  one unescaped TeX token, and one overly strict doubleton-bound sentence
  were corrected and retained in task evidence.
- Complete diff inspection and final whitespace hygiene pass.

## Evidence Classification And Limitations

- (PGODD-1)--(PGODD-27) are an **exact combinatorial theorem** about one
  fixed cyclic order.
- The diagnostic is **bounded exact computation** used only for independent
  corroboration.
- No \(K\), angular, geometric, global-optimality, or upstream Ringmin result
  is asserted or inferred.

## Files In Scope

- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260719__pg49_star_parity_w/

## Proposed Next Task

In a fresh STRICT task, evaluate the induced-subset score \(K\) of the
already fixed map (PGODD-6), including its boundary rows and cyclic closure,
without changing the candidate or inferring geometry or global optimality.
