# TASK STATUS - Global Four-Prefix Optimization

- Task ID: `TASK-20260717__global_four_prefix_optimization`
- Mode: STRICT
- Status: READY_FOR_REVIEW
- Last updated: 2026-07-17
- Blocker: none

## Objective

Optimize globally the asymptotic coefficient \(C_4\) in the proved direct
four-prefix theorem. Reduce the ordered density/weight problem to its exact
compact closure, classify every clipping branch, transition, collision, and
boundary face, prove the exact global value and maximizing set, compare it
rigorously with \(C_{3,*}\), and add an independent exact algebraic
diagnostic.

## Scope Guard

- In scope: the asymptotic four-prefix parameter optimization; exact compact
  reduction and boundary audit; one standalone dossier-local exact
  diagnostic; synchronization of the authoritative proof notes, project
  memory, and roadmap.
- Out of scope: finite rounding in \(n\); five-prefix extensions; production,
  API, artifact, schema, backend, certificate, or enumerator changes; any
  change to enumeration limits.

## Expected Delta

- Extend the exact ordered-weight reduction from three to four prefixes.
- Prove a complete compact-closure classification and exact global maximum.
- Record the exact optimizer, coefficient, uniqueness statement, and strict
  comparison with \(C_{3,*}\).
- Corroborate the algebra independently with exact standard-library
  arithmetic.
- Finish with proportional verification, final diff inspection, and status
  `READY_FOR_REVIEW` if complete.

## Current Truth

- Repository root: `C:/Users/Falker/Desktop/Code/circle/ringmin-squared`.
- Startup branch: clean `main` tracking `origin/main`.
- Startup commit: `24bea121d96906bfb884c57e3e97f189351d8791`.
- The compact closure is
  \(0\le\beta_4\le\beta_3\le\beta_2\le\beta_1\le\alpha\le1\) and
  \(0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1\).
- Independent clipping leaves exactly fifteen ordered regimes
  \(H^hM^m0^{4-h-m}\). The fixed-\(\alpha\) winner follows
  `0000`, `MMMM`, `HMMM`, `HHMM`, `HHHM`; the `HHHH` transition lies beyond
  \(\alpha=1\).
- Exact Bellman predecessor calculations classify every branch and
  transition. Density collisions and both outer weight facets reduce to the
  optimized three-prefix problem; all remaining compact faces are exhausted.
- The unique global nine-parameter point lies strictly in `MMMM`, with
  \[
  \alpha_*={18170840871749-3666143\sqrt{2903456040383}
   \over27631313622349}
  \]
  and normalized simplex coordinate
  \((3190338,2672508,2091528,1394352)/3666143\).
- Its exact value is
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403},
  \]
  and \(C_{3,*}<2767/10000<C_{4,*}\).
- The strengthened standalone exact diagnostic passes. Regression,
  historical-oracle, checked-artifact, formatting, mathematical-source, and
  diff checks pass.

## Plan

- [x] Complete STRICT startup and confirm a clean baseline.
- [x] Derive the exact ordered-weight and compact-density reduction.
- [x] Classify branches, transitions, collisions, and boundary faces.
- [x] Prove the exact maximum, maximizing set, and comparison with
  \(C_{3,*}\).
- [x] Add and run an independent exact algebraic diagnostic.
- [x] Synchronize authoritative sources and roadmap.
- [x] Run proportional verification and complete final diff review.

## Next Atomic Action

User review and manual commit decision.
