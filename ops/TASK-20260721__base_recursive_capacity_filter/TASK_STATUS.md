# TASK_STATUS - TASK-20260721 / Base-Recursive Capacity Filter

Last update: 2026-07-21

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** formalize the smallest nonconstant base/recursive capacity
  filter inside the one-prefix CR28dw proof, derive its exact normalized
  cubic objective, optimize the full compact closure, and decide whether the
  class improves \(C_{\mathrm{AF}}\).
- **Expected output:** exact all-order finite inequality, complete compact
  optimization including boundaries and the filter collision, exact
  improvement or no-go, one independent bounded exact diagnostic, and
  synchronized authoritative sources without production or artifact changes.

## Scope

- **In scope:** CR28ax--CR28dw49; one selected prefix; the existing
  base/recursive split dichotomy; original-edge capacity; exact asymptotic
  normalization; all compact faces; one task-local standard-library oracle;
  proof, memory, roadmap, status, and dossier synchronization.
- **Out of scope:** the distinct PG49/KPGZERO continued-fraction cardinality
  problem; broader structural filters; production source; test modules;
  schemas; enumerators; geometric artifacts; certificate backends; and any
  exact global leading-constant claim.

## Verified Facts

- A base cycle on \(S_r\) has \(q=n-r+1\) original edges.  Among the
  \(\ell=r-s\) selected splits, at least
  \([\ell-q]_+=[2r-s-n-1]_+\) are recursive.
- Retaining the stronger recursive floor proves (CR28dw41), strictly
  strengthening the \(k=1\) CR28dw right-hand side whenever the capacity
  term is positive and \(\lambda>0\).
- The normalized objective is the continuous positive-part expression
  (CR28dw43) on
  \(0\le\beta\le\alpha\le1\), \(0\le\lambda\le1\).
- The active-side compact closure has unique maximum \(13/48\) at its
  filter-off hinge \((1/2,0,0)\).  The whole class has the unique old
  inactive one-prefix maximum
  \[
  {4+2\sqrt3\over27}
  <{434+4\sqrt2\over1587}=C_{\mathrm{AF}}.
  \]
- The task-local exact diagnostic passes 3,300 selected-prefix histories and
  8,125 rational compact-domain points without importing project or test
  helpers.

## Assumptions / Inferences

- "Smallest" is defined only inside the declared class: one prefix, the two
  cells already exposed by the CR28 proof, and the sole original-edge
  capacity.  No uniqueness or minimality among arbitrary order filters is
  claimed.
- The roadmap's older phrase "filtered cubic-convergent obstruction" refers
  literally to the unrelated KPGZERO algebraic-cubic problem.  The present
  task follows the user's explicit CR28dw and \(C_{\mathrm{AF}}\) anchors and
  records the distinction in the roadmap.

## Decisions And Rationale

- Keep one prefix so that the only new statistic is base versus recursive
  split type; this makes the claimed filter class exact and auditable.
- Optimize the positive-part objective on both closed sides rather than
  assuming the active formula extends through the hinge.
- Use exact inequalities and rational radical separators; bounded grids are
  diagnostic evidence only.
- Keep the diagnostic task-local and independent of production code,
  public tests, enumerators, and artifacts.

## Plan And Expected Delta

- [x] Complete STRICT startup and resolve the roadmap/CR28 terminology.
- [x] Prove the capacity count and exact finite inequality.
- [x] Derive and optimize the normalized compact objective.
- [x] Add and run the independent exact diagnostic.
- [x] Synchronize the detailed proof, all-\(n\) synopsis, stable knowledge,
  and roadmap.
- [x] Complete repository regressions, source audits, and final diff review.
- [x] Set all task and global status files to `READY_FOR_REVIEW`.

## Verification

- **Checks:** standalone exact diagnostic; Ruff lint and format check; full
  pytest suite; checked-artifact schema test and independent verifier;
  equation-tag, display-math, control-character, protected-scope, Git-status,
  final-diff, and whitespace audits.
- **Observed result:** diagnostic PASS on 3,300 exhaustive selected-prefix
  histories and 8,125 exact grid points; Ruff PASS; 283 pytest tests PASS;
  4 schema tests PASS; 4 certificates and 76 local brackets PASS; all source
  and Git-hygiene audits PASS.
- **Limitations:** finite histories and a rational grid corroborate but do
  not replace the all-history and all-real proofs; hosted CI cannot inspect
  an uncommitted diff.

## Blockers / Risks

- No blocker.
- Residual risk is human review of the new proof; hosted CI cannot inspect an
  uncommitted diff.

## Next Atomic Action

- User review and manual commit decision; do not begin another roadmap item in
  this task.

## Handoff

- **Last verified result:** exact finite theorem, compact no-go, bounded
  independent diagnostic, and repository-wide verification all pass.
- **Files changed:** authoritative proof/synopses, stable memory/roadmap, and
  this task-local dossier with one exact diagnostic.
- **Files to read first:** the one-prefix base-capacity section in
  `research/FIXED_ORDER_CYCLE_RATIO.md`, then `EVIDENCE.md`.
