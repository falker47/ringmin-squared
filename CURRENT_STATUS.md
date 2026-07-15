# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact finite structural classification beyond the public
  cyclic-ratio enumeration boundary.
- **Current task:** classify equality in the `n=10` seven-label lemma without
  placing labels `2` or `3` or classifying complete core minimizers.
- **Task dossier:**
  `ops/TASK-20260715__lambda10_equality_cycle_classification/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md` now proves structurally that
  \[
  \max\{P_\omega(\{4,\ldots,10\}),P_\omega(\{5,\ldots,10\})\}=323
  \]
  holds in exactly the two dihedral classes represented by
  `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`.
- The proof starts from the accepted pairing classification at levels
  320--322 and rigorously separates tail score 322 from tail score 323.
- In the 322 branch, the unique simple signature has six exact insertion
  corrections and only `{7,9}: +1` is compatible with equality.
- In the 323 branch, all 15 possible corrections are evaluated. The four
  nonpositive candidates have fixed-edge pairing floors 323, 323, 326, and
  330; the unique `{8,9}` equality signature is not simple, leaving only
  `{7,10}: -2`.
- `tests/test_fixed_order_cycle_ratio.py` audits the pairing branches with
  exact test-local multiset arithmetic and keeps the direct sweep over all 360
  seven-label dihedral classes in a separate oracle test.
- No production source, scorer, API, or canonicalizer changed. No interval or
  checked artifact changed, and the public complete-order domain remains
  `n<=8`.

## Exact Finite Result

- EXACT THEOREM (FINITE SEVEN-LABEL EQUALITY CLASSIFICATION):
  \[
  \max\{P_\omega(T_7),P_\omega(T_6)\}=323
  \]
  if and only if \(\omega\) is dihedrally equivalent to one of the two
  displayed representatives.
- Their exact score pairs are
  \[
  (P(T_7),P(T_6))=(321,323)
  \quad\hbox{and}\quad
  (323,322),
  \]
  respectively.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the independent
  test-only 360-class oracle has minimum 323 and recovers exactly the two
  proved equality rows. It is not the source of the theorem.

## Verification

- Focused `lambda10` tests passed: 3 tests in 0.29 seconds.
- The complete cyclic-ratio test module passed all 31 tests in 14.08 seconds.
- The complete repository suite passed all 207 tests in 66.86 seconds.
- Explicit checked-artifact schema validation passed all 4 tests in 0.88
  seconds.
- The unchanged checked-artifact semantic verifier accepted 4 certificates,
  76 embedded local brackets, and the checked `n=3..6` summary.
- Targeted Ruff and Python compilation passed.
- Independent mathematical, test, and documentation audits reconstructed the
  proof, checked test independence and Python 3.11 APIs, and confirmed the
  scope boundaries after their precision findings were applied.
- The complete diff, changed-file whitespace, `git diff --check`, absence of
  a `src/` diff, production boundary, and task-created temporary paths were
  inspected; nothing is staged.
- CURRENT HOSTED STATUS: GitHub Actions on Ubuntu/Python 3.11--3.13 has not
  been run or independently verified for this worktree.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` adds the exact equality theorem and
  its two structural branches.
- `tests/test_fixed_order_cycle_ratio.py` adds independent branch arithmetic
  and separates the 360-class oracle.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize the theorem, evidence roles,
  limitations, and next research boundary.
- `CURRENT_STATUS.md` and the STRICT task dossier record the durable handoff.

## Residual Limitations

- The equality theorem places neither label `2` nor label `3` and does not
  classify or count the minimizing `n=10` core orders.
- It is finite and combinatorial. It gives no exact value of \(R_2^*(10)\),
  geometric minimizer statement, all-`n` formula, or asymptotic claim.
- Local execution used Python 3.14.3. Python 3.11 compatibility was audited
  syntactically and at the API level but not run locally.
- Hosted GitHub Actions for this worktree has not been inspected.

## Proposed Next Task

In a fresh chat, classify the admissible insertion gaps for label `3` in the
two proved seven-label equality cycles, leaving label `2` unplaced and making
no complete core-minimizer classification or production change.
