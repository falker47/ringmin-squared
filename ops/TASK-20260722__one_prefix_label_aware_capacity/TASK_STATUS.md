# TASK_STATUS - TASK-20260722 / One-Prefix Label-Aware Capacity

Last update: 2026-07-22

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** refine CR28dw40--CR28dw49 without replacing individual
  selected-label contributions by uniform floors at \(s\); prove the
  strongest history-uniform finite bound supported by the retained data,
  derive and optimize its exact continuous closure including collisions, and
  decide rigorously whether its coefficient exceeds \(C_{\mathrm{AF}}\).
- **Expected output:** exact cardinality and literal-history finite bounds,
  exact compact optimization, one independent exact-arithmetic diagnostic,
  and synchronization of only the authoritative proof, stable synopsis,
  roadmap, current status, and this dossier.

## Scope

- **In scope:** CR28ax--CR28dw49; one selected prefix; label-dependent
  \(G_{n,\lambda}(t)\) and \(J_{n,\lambda}(t)\); base/recursive type
  capacity; exact finite sums; cubic normalization; every compact face and
  formula collision; one task-local standard-library diagnostic.
- **Out of scope:** production source, tests, schemas, checked artifacts,
  enumerators, geometric claims, broader endpoint filters, global upper
  bounds on \(\Lambda_n\), and claims about an exact geometric leading
  constant.

## Verified Facts

- The exact advantage \(\Delta(t)=J(t)-G(t)\) is nonnegative and strictly
  decreasing in \(t\) for \(\lambda>0\).
- The strongest consequence of \(|\mathcal R|\ge\nu\) alone adds the
  \(\nu\) smallest advantages to \(\sum G(t)\).  Literal histories improve
  this by a one-label shift because the first selected split is necessarily
  base; every otherwise admissible binary type word is realizable.
- The two finite bounds differ by \(O(n^2)\), strictly when
  \(\nu>0\) and \(\lambda>0\), and have the same exact cubic objective.
- The active compact side has unique maximum \(13/48\) at
  \((\alpha,\beta,\lambda)=(1/2,0,0)\).
- The unique global maximizer is capacity-inactive and satisfies
  \[
  (\alpha_*,\beta_*,\lambda_*)
  \in(0.4365889,0.4365890)\times(0.3850802,0.3850803)
     \times(0.5024738,0.5024739),
  \]
  with
  \[
  {4+2\sqrt3\over27}<0.2768854<C_{\rm LA,*}<0.2768855
  <{434+4\sqrt2\over1587}=C_{\rm AF}.
  \]

## Assumptions / Inferences

- "Strongest" is split into two precise statements: strongest from the
  capacity cardinality alone, and strongest from the complete realizable
  binary type histories.  No simultaneous equality of all local geometric
  floors is asserted.
- Equality of the two cubic limits follows from their exact \(O(n^2)\)
  finite difference; it does not identify their lower-order terms.

## Decisions And Rationale

- Preserve each label's local floor before minimizing over recursive-label
  sets; this is the refinement requested by the task.
- State the forced-first-base refinement separately so the requested order-
  statistic statement is not overstated.
- Optimize both sides of the positive-part hinge on the full compact closure
  and use exact Bernstein, resultant, Sturm, interval, and rational/radical
  certificates.
- Keep the diagnostic standalone and independent of repository production,
  test, artifact, and certificate helpers.

## Plan And Expected Delta

- [x] Complete STRICT startup and inspect CR28dw40--CR28dw49 and its dossier.
- [x] Derive the exact labelwise finite inequalities and closed sums.
- [x] Derive and optimize the complete continuous closure.
- [x] Add the independent exact-arithmetic diagnostic.
- [x] Synchronize proof, synopsis, stable knowledge, roadmap, and dossier.
- [x] Complete repository regressions, source audits, and final diff review.
- [x] Set task and global status to `READY_FOR_REVIEW`.

## Verification

- **Checks:** standalone diagnostic; Ruff lint and format; full
  pytest suite; focused checked-artifact schema tests and verifier; equation-
  tag, display-math, control-character, protected-scope, Git-status, final-
  diff, and whitespace audits.
- **Observed result:** diagnostic PASS on 3,300 histories and 729 active
  points, with both degree-ten Sturm chains, coordinate and value enclosures,
  and exact comparisons passing; Ruff PASS; 283 pytest tests PASS; 4 schema
  tests PASS; 4 certificates and 76 local brackets PASS; 933 equation tags
  are unique; all source, scope, generated-file, diff, and whitespace audits
  PASS.  Two independent final read-only reviews found no remaining issue.
- **Limitations:** bounded exact computation corroborates but does not
  replace the all-history or all-real proofs; hosted CI cannot inspect an
  uncommitted diff.

## Blockers / Risks

- No blocker.
- Residual risk is human review of the long exact compact certificate; hosted
  CI cannot inspect the uncommitted diff.

## Next Atomic Action

- User review and manual commit decision; do not begin another roadmap item
  in this task.

## Handoff

- **Last verified result:** the finite derivation, exact compact
  classification, independent diagnostic, repository regressions, and final
  source/diff audits all pass.
- **Files changed:** proof and synopsis, stable memory and roadmap, current
  status, and this task-local dossier with one diagnostic.
- **Files to read first:** the one-prefix label-aware capacity section in
  `research/FIXED_ORDER_CYCLE_RATIO.md`, then `EVIDENCE.md`.
