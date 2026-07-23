# TASK STATUS - TASK-20260723 / KR1G Relaxed Unused Slack

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine exactly the asymptotic minimum of the unused
  original-edge slack under the cycle/edge-cardinality relaxation at the
  fixed KR1G densities, and state precisely what transfers to compatible
  histories.
- **Expected output:** an exact finite formula, explicit sharp family,
  \(n^3\)-normalized classification, history-scope audit, and one independent
  bounded oracle.

## Scope

- **In scope:** simple cycles on \(S_r\); at most \(r-s\) charged original
  edges; exact floor/ceiling algebra; the projection of compatible histories
  to their base cycle and charged-edge set; task-local exhaustive checking.
- **Out of scope:** a new order family, optimization of the complete history
  residual, a growing-prefix theorem, production code, public tests, schemas,
  artifacts, enumeration limits, and new geometric claims.

## Verified Facts

- For \(q\ge3\) and \(\ell\ge1\), the relaxed minimum is exactly
  \[
  {1\over2}\left[\left\lceil{q\over2}\right\rceil-\ell\right]_+.
  \]
- At \(r=\lfloor an\rfloor\), \(s=\lceil bn\rceil\), this gives, for
  \(n\ge25\),
  \[
  {2+5\sqrt2\over92}n+O(1),
  \]
  and its \(n^3\)-normalized limit is zero.
- The zigzag equality witness can be lifted to a compatible history for the
  unused-edge term alone. It does not control the other KR1G remainders.

## Assumptions / Inferences

- The direct all-row inequalities use the clean sufficient threshold
  \(n\ge25\); no claim of threshold sharpness is needed for the asymptotic
  theorem.
- A compatible-history lift of the deleted-edge set is not an assertion that
  the lifted history is KR1 or minimizes the full history objective.

## Decisions And Rationale

- Translate \(S_r\) to consecutive coordinates so zero slack becomes the
  fixed complementary matching.
- Prove the lower bound by matching cardinality and attain it with one
  parity-explicit zigzag family.
- Record the relaxation, its history projection, and the complete KR1G
  residual as three distinct objects.
- Keep the oracle task-local and independent of production and test helpers.

## Plan And Expected Delta

- [x] Complete STRICT startup on a clean worktree.
- [x] Derive the exact finite formula and asymptotic coefficient.
- [x] Prove and scope the compatible-history lift.
- [x] Add and run the bounded independent oracle.
- [x] Update proof note, stable memory, and roadmap.
- [x] Complete repository verification and final diff review.

## Verification

- **Checks:** independent exhaustive oracle; Ruff lint and format; focused
  source audits; repository regressions; checked-artifact verifier; schema
  tests; Git diff and whitespace checks.
- **Observed result:** the oracle has passed 204,556 canonical cycles and 52
  exact \((q,\ell)\) cases for \(3\le q\le10\); 283 repository tests, all
  four checked artifacts, four focused schema tests, Ruff, source-structure,
  encoding, link, final-diff, and whitespace checks pass.
- **Limitations:** bounded enumeration corroborates but does not replace the
  all-\(q\) matching proof.

## Blockers / Risks

- No blocker.
- Residual risk is final human review of the distinction between the sharp
  unused-edge projection and the uncontrolled full history residual.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact finite theorem, explicit zigzag witness,
  compatible-history projection, bounded exhaustive oracle, complete
  regression, and final source/diff audits.
- **Files changed:** authoritative proof, stable memory, roadmap, current
  status, and this task dossier; no production or public test file.
- **Files to read first:** the relaxed-unused-edge subsection of
  `research/FIXED_ORDER_CYCLE_RATIO.md` and `EVIDENCE.md`.
