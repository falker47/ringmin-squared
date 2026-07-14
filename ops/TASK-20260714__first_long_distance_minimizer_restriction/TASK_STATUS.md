# TASK_STATUS - TASK-20260714__first_long_distance_minimizer_restriction / First Long-Distance Minimizer Restriction

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine the first index at which positional distances at
  least three strictly restrict the minimizers of the product-distance
  surrogate.
- **Expected output:** an exact theorem proving minimizer-set equality through
  \(n=92\), an exact moved-label witness proving strict inclusion at \(n=93\),
  independent exact scorer tests, synchronized authoritative memory and
  roadmap, and unchanged canonical-enumeration boundary \(n\le11\).

## Scope

- **In scope:** the domination criterion \(n(n-1)/3\le B_n\), exact
  residue-class arithmetic, the requested edit of
  \(\operatorname{eight\_twenty\_fifths\_order}(93)\), exact all-pairs
  scoring, tests, proof note, authoritative memory, roadmap, and task evidence.
- **Out of scope:** canonical enumeration beyond \(n=11\); geometric
  feasibility, optimality, or asymptotic claims; new artifacts, schemas, or
  CLIs; Git writes; upstream Ringmin changes.

## Verified Facts

- The startup files, relevant predecessor dossiers, proof/source/tests,
  roadmap, and initially clean Git worktree were inspected.
- Every pair omitted from the distance-two score is at most
  \(n(n-1)/3\). Exact residue arithmetic proves the sufficient criterion
  throughout \(3\le n\le92\).
- At \(n=93\), the requested relocation of label \(54\) gives exact scores
  \(W^{(\le2)}=2850\) and \(W=2852\), with the latter uniquely attained by
  \((92,93)\) at distance three.
- The proof, authoritative memory, roadmap, tests, current status, and this
  dossier now state the same bounded result and limitations.
- Production source is unchanged, and the canonical enumerator remains
  hard-bounded to \(n\le11\).

## Assumptions / Inferences

- None. The result uses accepted exact formulas, symbolic inequalities, and
  finite exact rational scoring only.

## Decisions And Rationale

- Keep production generators and enumerators unchanged; construct the single
  witness explicitly in the proof and independent test.
- Separate the uniform domination theorem from the exact witness proving
  strict inclusion at the first failed index.
- State no persistence after \(n=93\); the sufficient equality criterion
  already holds again at \(n=94\).
- Keep every geometric claim out of this combinatorial task.

## Plan And Expected Delta

- Add independent exact arithmetic and all-pairs witness regressions.
  COMPLETE.
- Integrate the theorem into the primary proof, authoritative memory, and
  roadmap. COMPLETE.
- Run focused/full tests, checked-artifact verification, and independent
  mathematical/implementation audits. COMPLETE.
- Finish cross-document review and final Git/diff hygiene. COMPLETE.

## Verification

- **Checks:** two targeted tests; focused and full pytest; checked-artifact
  semantic verification; Ruff; Python compilation; three independent audits;
  final text, proof-tag, changed-path, complete-diff, and Git hygiene.
- **Observed result:** targeted tests pass 2/2; focused tests pass 43/43; the
  complete suite passes 171/171 outside the filesystem sandbox; checked
  artifacts accept 4 certificates, 76 local brackets, and the \(n=3,\dots,6\)
  summary; Ruff and compilation pass; mathematical and implementation audits
  pass; the final cross-document, strict text, proof-tag, changed-path,
  complete-diff, stale-claim, and Git hygiene audits pass.
- **Retained failed check:** the first sandboxed full suite produced 31 setup
  errors because pytest could not create its temporary directory. No test body
  failed; the required outside-sandbox rerun passed.
- **Limitations:** hosted CI will not be inferred from local checks.

## Blockers / Risks

- No current blocker.
- The subsequent strict-inclusion indices \(n\ge94\) are unclassified.
- Equality or strictness of these combinatorial minimizer sets has no new
  geometric implication.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact theorem, moved-label witness, all executable
  checks, three independent audits, and final diff/hygiene checks pass.
- **Files changed:** current status, project brief, durable knowledge, primary
  proof, roadmap, one test module, and this three-file task dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md,
  tests/test_product_distance.py, CURRENT_STATUS.md, and this dossier.
