# TASK_STATUS - TASK-20260721 / Canonical Odd-v E5 Path-Gap Support

Last update: 2026-07-21

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** on the canonical odd-`v=2m+1`, `e=5` scaffold at
  `n=10m+9`, classify the exact path/gap support, including the minimum
  domain, literal cyclic closure, Hall-extendible support, full-threshold
  support, and the complete relationship with `W=W_n`.
- **Expected output:** one exact all-domain theorem, one standalone
  standard-library small-row diagnostic, synchronized proof, stable
  knowledge, roadmap, current status, and task dossier.

## Scope

- **In scope:** the unchanged canonical path orientations; arbitrary
  whole-path bijections; exact distance classes `1`, `2`, `3`, and `>=4`;
  triple and singleton forms; the identically empty doubleton type; true
  closing column; residual Hall; Ferrers structure; and the exact
  full-threshold edge support.
- **Out of scope:** evaluating `K`; selecting or optimizing a preferred path
  assignment; changing production code or tests; classifying minimizers
  outside this scaffold; and angular, geometric, or global geometric
  conclusions.

## Exact Result

Put

\[
v=2m+1,\quad m\ge1,\quad d=8m+9,\quad n=10m+9,
\quad T={d(d-1)\over2}=W_n.
\]

The exact path decomposition has `m+2` triples, no doubleton, and `m-1`
singletons. The singleton range is empty exactly at `m=1`; `m=0` is not a
row of this scaffold. With

\[
\kappa_j=\left\lceil{j(d-1)\over2(d+j)}\right\rceil,
\]

the literal local relation is

\[
\mathcal R^{\rm odd}_{\rm loc}=\{(k,j):k\ge\kappa_j\}.
\]

Its genuine terminal thresholds are

\[
\kappa_{2m-1}=\left\lfloor{4m+3\over5}\right\rfloor,
\qquad
\kappa_{2m}=\left\lfloor{4m+5\over5}\right\rfloor.
\]

Residual Hall is exactly

\[
\kappa_r+\mathbf1_{\{k\ge\kappa_r\}}
\le r+\mathbf1_{\{j>r\}}
\qquad(r\ne j),
\]

and therefore

\[
\mathcal R^{\rm odd}_{\rm full}
=\mathcal R^{\rm odd}_{\rm ext}
=\{(0,0)\}\cup
\{(k,j):1\le j\le2m,\ k\ge\kappa_j\}.
\]

The local board is Ferrers. The full support is not Ferrers because
`(0,0)` and `(1,1)` induce a `2K2`; deleting the forced pair
`(P_0,G_0)` leaves a matching-covered Ferrers board.

Every scaffold bijection satisfies `W=W^(<=2)`. Distance one is strictly
below `T`; distance two is classified exactly by the local relation and
`P_0` always supplies a score at least `T`; distances three and at least
four are uniformly strict. Hence

\[
W(\sigma_\alpha)=W_n=T
\iff
\alpha(j)\ge\kappa_j\quad(0\le j\le2m).
\]

There is no odd-parity obstruction to the even-`v` completion theorem. The
only obstruction is to calling the unreduced full support itself Ferrers.

## Boundary Rows

- `m=1`: `(d,n,T)=(17,19,136)`, three triples, no singleton,
  `kappa=(0,1,1)`, `ell=(0,2,2)`, and true closure
  `(19,2,P_k,7,17)`.
- `m=2`: four triples, the sole singleton `(16)`, and
  `kappa=(0,1,1,2,2)`.
- `m=4` is the first genuine closure split: `P_3=(34,23,33)` has score
  `816<820` in `G_7`, but `833>820` in the actual closing gap `G_8`.

## Verification

- The sole diagnostic passes on direct rows `m=1..30`: 39,710 local
  incidences, 30,948 local Ferrers edges, 1,408,738 residual Hall
  inequalities, 30,018 extendible edges, and 930 exact zero-column
  obstructions.
- The same script exhausts all 5,166 scaffold bijections for `m=1..3`,
  scores every unordered core pair by true smaller cyclic distance, and
  finds exactly 158 compatible/full-threshold bijections with the predicted
  support.
- Three independent audits agree with the theorem and diagnostic after the
  retained notation/context corrections. Source structure, syntax, Ruff,
  full pytest, focused schema/Arb suites, checked artifacts, final scope,
  caches, diff, and whitespace all pass.

## Blockers / Risks

- No blocker.
- Residual risk is ordinary manual review of a long symbolic proof. The
  bounded computation corroborates but does not replace the all-domain
  theorem.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** all mathematical, bounded diagnostic, repository,
  source-structure, scope, cache, diff, and whitespace checks pass.
- **Files changed:** authoritative product-distance proof, stable knowledge,
  roadmap, current status, and this four-file STRICT dossier.
- **Files to read first:**
  `research/PRODUCT_DISTANCE_SURROGATE.md`, then `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Prove canonical odd-v e5 path-gap support theorem`.
