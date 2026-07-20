# CURRENT_STATUS - power-ringmin

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** exact path-to-gap relation and complete support at the
  sharp product-distance threshold on the canonical `e=5`, even-`v=2m`
  branch, `n=10m+4`, `m>=2`.
- **Repository state at startup:** clean `main` worktree at commit
  `d69178766f61a22875ea9f29fc99121db6e2fddf`.
- **Implementation state:** exact symbolic theorem, direct standalone
  diagnostic, authoritative synchronization, independent audits, full
  repository tests, artifact verification, and final diff/scope/hygiene
  inspection are complete.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Canonical E5 Scaffold

For

\[
v=2m,\qquad m\ge2,\qquad d=8m+5,
\qquad n=10m+4,
\qquad T={d(d-1)\over2}=W_n,
\]

the unchanged scaffold has `m+1` oriented triples, one doubleton, and `m-2`
singletons. The singleton range is empty exactly at `m=2`; the symbolic
scaffold does not exist at `m=1`.

## Exact Local Relation

Put

\[
\kappa_j=\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
\]

PGE5-1--PGE5-18 prove

\[
\boxed{\mathcal R_{\rm loc}=\{(k,j):k\ge\kappa_j\}.}
\]

For a triple `P_k`, this is the exact closed condition

\[
j(d-1-2k)\le2kd.
\]

The doubleton and every singleton are strictly universal. The true terminal
thresholds are

\[
\kappa_{2m-2}=\left\lfloor{4m+1\over5}\right\rfloor,
\qquad
\kappa_{2m-1}=\left\lfloor{4m+3\over5}\right\rfloor.
\]

Every triple, doubleton, singleton, nonclosing, and closing local maximum is
classified separately. The literal last words are

\[
(n-1,4,P_k,3,n),
\qquad
(n,2,P_k,4m+1,d).
\]

## Exact Hall And Full Support

After fixing a local edge `(k,j)`, residual Hall is necessary and sufficient
exactly when

\[
\kappa_r+\mathbf1_{\{k\ge\kappa_r\}}
\le r+\mathbf1_{\{j>r\}}
\qquad(r\ne j).
\]

PGE5-19--PGE5-26 give

\[
\boxed{
\mathcal R_{\rm full}=\mathcal R_{\rm ext}
=\{(0,0)\}\cup
\{(k,j):1\le j\le2m-1,\ k\ge\kappa_j\}.}
\]

The only local nonextendible edges are `(k,0)`, `k>0`, which fail on the
suffix `G_1,...,G_(2m-1)` with `2m-1` gaps but only `2m-2` residual
neighbors. Every positive-column local edge passes Hall and has an explicit
interval-shift witness used only for existence, not as a selected
construction.

Every whole-path bijection satisfies

\[
W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha).
\]

Distances three and at least four are universally strict below `T`, while
the left terminal pair of `P_0` has truncated score at least `T`. Thus local
compatibility is equivalent to the global surrogate value `W_n`. This does
not classify `W`-minimizers outside the scaffold.

## Ferrers Classification And PG49

- `R_loc` is Ferrers because its column neighborhoods are nested suffixes.
- The complete support `R_full=R_ext` is not Ferrers: `(0,0)` and `(1,1)`
  form an induced `2K2`, with both cross-edges absent.
- After deleting the forced vertices `P_0,G_0`, the reduced support is
  Ferrers and every edge is matching-covered.

Therefore PG49 has a complete support theorem on this branch. The precise
obstruction is only to the stronger, false assertion that the unreduced
global support itself is Ferrers.

## Literal Boundary Rows

\[
\begin{array}{c|c|c|c|c}
m&(d,n,T)&(\kappa_j)&\text{path types}&
(|\mathcal R_{\rm loc}|,|\mathcal R_{\rm ext}|)\\ \hline
2&(21,24,210)&(0,1,1,2)&3\text{ triples}+1\text{ doubleton}&(12,9)\\
3&(29,34,406)&(0,1,1,2,2,3)&
4\text{ triples}+1\text{ doubleton}+1\text{ singleton}&(27,22)
\end{array}
\]

At `m=2` the doubleton is the closing canonical path and the singleton range
is empty. At `m=3` the only singleton is the closing canonical path. Neither
row is exceptional to the formulas.

## Bounded Diagnostic

The task's sole standalone standard-library diagnostic reconstructs the
literal scaffold directly and passes on `m=2..40`:

- 88,556 path/gap incidences;
- 69,124 local Ferrers edges;
- 4,132,070 residual suffix Hall inequalities;
- 67,525 Hall-extendible support edges;
- 1,599 exact zero-column obstructions.

It also checks the minimum row, empty singleton range, cyclic closure,
inclusive cutoff equality, global induced `2K2`, reduced Ferrers nesting, and
the symbolic full-distance margins. It imports no project/test helper,
constructs no complete assignment, searches no matching or permutation, and
computes no `K`.

## Verification

- The final standalone diagnostic passes with the exact counts above.
- In-memory syntax, scoped Ruff lint, and Ruff format checks pass.
- Three independent mathematical/Hall/diagnostic audits pass after one
  missing `\left` and one overbroad scope disclaimer were corrected.
- The PGE5 source audit passes with 26 sequential tags, 42 balanced displays,
  139/139 braces, balanced environments, and no control characters.
- Full pytest passes: 283 tests.
- The focused checked-artifact schema suite passes: 4 tests.
- The standalone checked-artifact verifier passes for four certificates,
  76 local brackets, and `n=3,4,5,6`.
- Final Git status, complete tracked and untracked scope inspection, diff
  review, cache audit, and whitespace hygiene pass. The first final
  `git diff --check` caught one trailing blank line in this file; it was
  removed, and the repeated check passes.

## Evidence Classification And Scope

- PGE5-1--PGE5-26 are an **exact all-domain combinatorial theorem**.
- The standalone diagnostic is **bounded exact computation** corroborating,
  not replacing, the symbolic proof.
- Exact global `W`-minimality is asserted for the supported scaffold
  bijections because their score is `W_n`; minimizers outside the scaffold
  are not classified.
- No preferred assignment, `K`, angular, geometric, global `K`-minimality,
  or global geometric-optimality conclusion is included.

## Files In Scope

- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260720__canonical_e5_even_path_gap_support/

## Proposed Next Task

In a fresh STRICT task, derive the exact labelled permanent/count of the
reduced canonical `e=5` Ferrers support without enumerating path permutations
or selecting a preferred assignment.
