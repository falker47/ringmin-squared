# TASK_STATUS - TASK-20260715__lambda10_equality_cycle_classification / Lambda_10 Equality-Cycle Classification

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove structurally that equality in the `n=10` seven-label
  lemma occurs in exactly the dihedral classes represented by
  `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`.
- **Expected output:** an exact branch proof separating tail scores 322 and
  323, complete label-four correction data, independent test-only regression
  over all 360 seven-label classes, synchronized authoritative memory, and no
  production change.

## Scope

- **In scope:** cyclic orders on labels `4..10`; duplicated-pairing
  signatures already classified at 320--322; exact insertion corrections for
  label `4`; fixed-edge residual pairing bounds; proof, tests, roadmap, status,
  and task evidence.
- **Out of scope:** placing labels `2` or `3`; classifying or counting all
  `n=10` core minimizers; production scorer, API, canonicalizer, or public
  enumeration changes; exact geometry or `R_2^*(10)`; interval artifacts,
  schemas, all-`n` formulas, asymptotics, or Git writes.

## Verified Facts

- Startup completed on a clean worktree at `5d94228ced7b`.
- Equality forces the tail score to be 322 or 323.
- In the 322 branch, the unique simple signature forces insertion on
  `{7,9}`, giving `(10,5,9,4,7,8,6)` with score pair `(323,322)`.
- In the 323 branch, the exact correction table leaves four candidate edges.
  Their fixed-edge pairing floors are `(323,323,326,330)`; the `{8,9}`
  equality signature is not simple, so only `{7,10}` survives. It gives
  `(10,4,7,8,6,9,5)` with score pair `(321,323)`.
- The separate test-only sweep checks all 360 dihedral classes and recovers
  exactly the two proved classes.

## Assumptions / Inferences

- This is a finite exact combinatorial theorem, not a geometric optimum or an
  all-`n` statement.
- The 360-class sweep is an oracle audit only and is not used in the proof.

## Decisions And Rationale

- Reuse the accepted 320--322 pairing classification for the 322 branch.
- Treat the 323 branch by first constraining the insertion edge through the
  sign of the correction, then applying pairing bounds to the residual
  multiset. This avoids cyclic-order enumeration in the proof.
- Keep the structural branch test and 360-class oracle in separate tests.

## Plan And Expected Delta

- Add the structural equality theorem to the proof note. COMPLETED.
- Extend independent test-only arithmetic for both branches. COMPLETED.
- Synchronize project memory and roadmap. COMPLETED.
- Complete final diff and hygiene inspection. COMPLETED.

## Verification

- **Checks:** focused/module/full pytest; checked-artifact semantic and schema
  regressions; Ruff and compilation; independent mathematical, test, and
  documentation audits; final Git/diff/whitespace and scope inspection.
- **Observed result:** focused tests pass 3/3, the cyclic-ratio module passes
  31/31, and the complete suite passes 207/207. Schema validation passes 4/4;
  the semantic verifier accepts 4 certificates and 76 local brackets; Ruff,
  compilation, and the three independent audits pass after applying their
  editorial precision findings.
- **Limitations:** local execution used Python 3.14.3. Python 3.11 syntax and
  used APIs were audited, but a local Python 3.11 runtime was unavailable.
  Hosted CI was not run or independently inspected.

## Blockers / Risks

- No blocker.
- The seven-label equality classes must not be described as the complete set
  of `n=10` core minimizers.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact branch proof, all focused/full regressions,
  three independent audits, and final diff/worktree hygiene pass.
- **Files changed:** proof note, cyclic-ratio tests, project brief, durable
  knowledge, roadmap, current status, and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
