# TASK_STATUS - TASK-20260719 / PG49-Star Parity W

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine whether the fixed odd-\(v\) parity analogue of
  PG49-star on `n=10m+8` is a Ferrers/PG49-compatible bijection throughout
  its symbolic domain, and evaluate only its exact product-distance score
  `W`.
- **Result:** no obstruction. The search-free map (PGODD-6) is a compatible
  bijection for every `m>=1`, and
  `W=(8m+8)(8m+7)/2`.

## Scope

- **In scope:** the canonical `e=4`, odd-`v`
  eight-twenty-fifths scaffold; triple, doubleton, and singleton paths; the
  candidate fixed before scoring; exact odd Ferrers relation and PG49
  support; bijectivity; all positional distances needed for `W`; empty
  ranges, threshold boundaries, and literal cyclic closure.
- **Out of scope:** `K`, induced-subset maximizers, shortcut/backbone
  analysis, exact angular thresholds, geometry, global minimizing-order or
  optimality conclusions, production generators, and searches over orders,
  matchings, path permutations, or subsets.

## Verified Facts

- Startup found a clean worktree at
  `c45a5dc7133670874bc76246684cc7d8ed323f89`.
- The retained general scaffold is (UC1)--(UC20); the former PG49-star
  theorem (PG110)--(PG114) applies only to even `v=2m`. The odd branch
  required a new proof because it contains a doubleton.
- The candidate (PGODD-6) was fixed before any score calculation.
- The exact local board is `k>=kappa_j`; the exact extendible support is
  (PGODD-18). The image intervals in (PGODD-20) are disjoint and complete.
- The genuine closing image is
  `alpha(2m)=q=kappa_(2m)=floor((4m+5)/5)`.
- The minimum row is `alpha=(0,2,1)`; `q=m` exactly for
  `1<=m<=5`; singleton reversal is empty at `m=1` and order-neutral
  at `m=2`.
- The full fixed-order score is
  `W=(8m+8)(8m+7)/2` for every `m>=1`.

## Decisions And Rationale

- The doubleton is shifted into `G_m` and retains its orientation; only
  the actual singleton path block is reversed.
- The closing threshold is derived from `kappa_(2m)`, not copied from
  the last nonclosing column.
- The sole standalone integer diagnostic constructs only the prescribed map
  and checks no alternative matching or order.

## Verification

- `python ops/TASK-20260719__pg49_star_parity_w/exact_diagnostic.py`:
  PASS; 1,000 formula rows, 40 local/Hall rows, 80 full-score rows, and
  8,906,280 unordered cyclic pairs.
- Standalone compile check: PASS.
- Scoped Ruff lint and format checks: PASS.
- `python -m pytest -p no:cacheprovider`: 283 passed.
- Focused checked-artifact schema suite: 4 passed.
- Standalone checked-artifact verifier: PASS for four certificates,
  76 local brackets, and `n=3,4,5,6`.
- Source audit: PASS with 27 sequential unique PGODD tags, 34 balanced
  displays, balanced aligned/cases/array environments, and no malformed
  control text.
- Final Git diff inspection and whitespace hygiene: PASS.
- Corrected failures are preserved in `TASK_LOG.md` and
  `EVIDENCE.md`: an initially overbroad diagnostic Hall call, Ruff
  formatting, an unescaped `qquad`, and the preclosing doubleton equality
  omitted by the first wording.

## Blockers / Risks

- No blocker.
- Residual risk is confined to manual review of a long symbolic proof. The
  all-domain result rests on exact algebra, not the bounded diagnostic.

## Handoff

- **Status:** READY_FOR_REVIEW; the user decides whether to commit manually.
- **Files changed:** the product-distance research note, project roadmap,
  startup brief, stable knowledge, current status, and this task dossier.
- **Files to read first:**
  `research/PRODUCT_DISTANCE_SURROGATE.md` and `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Prove odd-v PG49-star parity compatibility and W`.
- **Proposed next atomic task:** in a fresh STRICT task, evaluate `K` for
  the already fixed map without changing it or inferring geometry.
