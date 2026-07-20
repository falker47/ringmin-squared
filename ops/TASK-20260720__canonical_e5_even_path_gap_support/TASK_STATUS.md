# TASK_STATUS - TASK-20260720 / Canonical Even-v E5 Path-Gap Support

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** on the canonical `e=5`, even-`v=2m` scaffold at
  `n=10m+4`, derive the exact whole-path local relation at the sharp
  threshold `W_n`, classify Hall-extendible edges and Ferrers structure, and
  determine whether PG49 has a complete support theorem or an exact
  obstruction.
- **Expected output:** exact all-domain theorem with path/gap types, cyclic
  closure, local iff condition, Hall support, minimum-domain and empty-range
  treatment, one direct standalone standard-library diagnostic, synchronized
  durable memory, and repository-proportional verification.

## Scope

- **In scope:** the unchanged canonical scaffold and path orientations;
  arbitrary whole-path bijections; distance-one and distance-two local
  conditions; all triple, doubleton, singleton, nonclosing, and closing
  forms; residual Hall; global versus reduced Ferrers structure; and the
  assignment-independent distance-three/long-distance bounds needed to
  identify the full-threshold support.
- **Out of scope:** searching for a path permutation or matching, selecting a
  preferred construction, evaluating `K`, changing production or test code,
  angular or geometric conclusions, classifying `W`-minimizers outside this
  scaffold, and global `K`- or geometric-optimality claims.

## Exact Result

Put

\[
v=2m,\quad m\ge2,\quad d=8m+5,\quad n=10m+4,
\quad T={d(d-1)\over2}=W_n.
\]

There are `m+1` triples, one doubleton, and `m-2` singletons. The singleton
range is empty exactly at `m=2`. With

\[
\kappa_j=\left\lceil{j(d-1)\over2(d+j)}\right\rceil,
\]

the exact local relation is

\[
\mathcal R_{\rm loc}=\{(k,j):k\ge\kappa_j\}.
\]

For a triple this is equivalent to

\[
j(d-1-2k)\le2kd;
\]

the doubleton and every singleton are universal. The terminal thresholds are

\[
\kappa_{2m-2}=\left\lfloor{4m+1\over5}\right\rfloor,
\qquad
\kappa_{2m-1}=\left\lfloor{4m+3\over5}\right\rfloor.
\]

Residual Hall is exactly

\[
\kappa_r+\mathbf1_{\{k\ge\kappa_r\}}
\le r+\mathbf1_{\{j>r\}}
\qquad(r\ne j),
\]

and therefore

\[
\mathcal R_{\rm full}=\mathcal R_{\rm ext}
=\{(0,0)\}\cup
\{(k,j):1\le j\le2m-1,\ k\ge\kappa_j\}.
\]

The only local nonextendible edges are `(k,0)` with `k>0`. The local board is
Ferrers. The complete support is not Ferrers because `(0,0)` and `(1,1)`
induce a `2K2`; after deleting the forced vertices `P_0,G_0`, the reduced
support is Ferrers and every edge is matching-covered. Thus PG49 survives
exactly as a forced edge plus a reduced Ferrers board.

Every whole-path bijection satisfies `W=W^(<=2)`: distances three and at
least four are uniformly below `T`, while the left terminal pair of `P_0`
has truncated score at least `T`. Hence local compatibility is equivalent to
global surrogate score `W_n`. This global conclusion is confined to the
supported scaffold bijections; no minimizer outside the scaffold is
classified.

## Boundary Rows

- `m=2`: `d=21`, `n=24`, `T=210`,
  `kappa=(0,1,1,2)`; three triples, one closing doubleton, no singleton;
  12 local edges and 9 extendible edges.
- `m=3`: `d=29`, `n=34`, `T=406`,
  `kappa=(0,1,1,2,2,3)`; four triples, one doubleton, one closing singleton;
  27 local edges and 22 extendible edges.
- The literal last nonclosing and closing words are
  `(n-1,4,P_k,3,n)` and `(n,2,P_k,4m+1,d)`, respectively.

## Verification

- The standalone diagnostic passes on `m=2..40`: 88,556 path/gap
  incidences, 69,124 local edges, 4,132,070 residual Hall inequalities,
  67,525 extendible edges, and 1,599 exact zero-column obstructions.
- Syntax, scoped Ruff lint, and Ruff format checks pass.
- Three independent mathematical/Hall/diagnostic audits agree after two
  documentation corrections: one missing `\left` and one overbroad scope
  disclaimer.
- The PGE5 source audit passes with 26 sequential tags, 42 balanced displays,
  balanced environments and braces, and no control characters.
- Full pytest passes: 283 tests.
- The focused checked-artifact schema suite passes: 4 tests.
- The standalone checked-artifact verifier passes for four certificates,
  76 local brackets, and `n=3,4,5,6`.
- Final Git status, complete tracked and untracked scope inspection, diff
  review, cache audit, and whitespace hygiene pass.

## Retained Failed Checks

- The first diagnostic implementation used direct Python sets through
  `m=60` and timed out at 60.4 seconds. It was replaced by exact bit-mask
  suffix unions and the declared bounded interval was set to `m=2..40`; the
  final direct checks pass in about 14--16 seconds.
- The first Ruff format check found one mechanical formatting delta; the
  formatter changed only the diagnostic, after which lint and format pass.
- The first source-audit wrapper counted the `\\[5pt]` row-spacing tokens in
  `cases` environments as display starts and reported a false mismatch. The
  corrected line-anchored audit passes; no source delimiter was missing.
- The first final `git diff --check` reported one new blank line at EOF in
  `CURRENT_STATUS.md`. The blank line was removed, and the repeated check
  passes.

## Blockers / Risks

- No blocker.
- Residual risk is ordinary manual review of a long symbolic proof. Bounded
  computation corroborates but does not replace the all-domain theorem.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Files changed:** the product-distance proof, roadmap, startup brief,
  stable knowledge, current status, and this four-file STRICT dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`, then
  `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Prove canonical e5 path-gap support theorem`.
- **Historical proposal, superseded:** at baseline `6ec74a8`, this dossier
  proposed deriving the labelled permanent of the reduced `e=5` support. The
  post-review consolidation in
  `ops/TASK-20260720__pge5_post_review_consolidation/` supersedes that
  task-local proposal; the sole current priority is authoritative only in
  `research/NEXT_RESEARCH_STEPS.md`.
