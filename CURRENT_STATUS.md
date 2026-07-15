# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact finite structural classification beyond the public
  cyclic-ratio enumeration boundary.
- **Current task:** classify every label-three insertion gap in the two proved
  `n=10` seven-label equality cycles while leaving label `2` unplaced.
- **Task dossier:**
  `ops/TASK-20260715__lambda10_label3_insertion_gap_classification/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md` now defines the partial score
  \[
  K_{\ge3}(\nu)=
  \max_{\varnothing\ne U\subseteq\{3,\ldots,10\}}P_\nu(U)
  \]
  and proves the exact label-three insertion classification over
  `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`.
- The proof uses the insertion correction
  \(\Delta_3(a,b)=3(a+b)-ab=9-(a-3)(b-3)\), the exact transformation of old
  shortcut gains, bounds for every other shortcut family, and complete
  nonnegative-gain tables for all 14 insertions.
- `tests/test_fixed_order_cycle_ratio.py` adds a structural certificate test
  that enumerates no label subsets and a separate literal oracle over all 14
  inserted orders and all 255 nonempty subsets of each.
- No production source, scorer, API, or canonicalizer changed. No interval or
  checked artifact changed, and the public complete-order domain remains
  `n<=8`.

## Exact Finite Result

- EXACT THEOREM (FINITE LABEL-THREE INSERTION-GAP CLASSIFICATION): for
  \(\omega_A=(10,4,7,8,6,9,5)\),
  \[
  K_{\ge3}(\iota_h(\omega_A))=
  \begin{cases}
  326,&h=\{4,7\},\\
  323,&\text{otherwise},
  \end{cases}
  \]
  while for \(\omega_B=(10,5,9,4,7,8,6)\),
  \[
  K_{\ge3}(\iota_h(\omega_B))=
  \begin{cases}
  326,&h=\{4,9\},\\
  328,&h=\{4,7\},\\
  323,&\text{otherwise}.
  \end{cases}
  \]
- Thus the first cycle excludes only `{4,7}`, the second excludes `{4,9}` and
  `{4,7}`, and every other partial insertion has exact score 323.
- The first cycle's `{4,10}` insertion has argmaxes
  `{5,...,10}` and `{3,...,10}`; its other five admissible gaps have sole
  argmax `{5,...,10}`. All five admissible gaps of the second cycle have sole
  argmax `{4,...,10}`.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the independent
  test-only oracle performs 3,570 literal subset evaluations and recovers
  every proved score and argmax. It is not the source of the theorem.

## Verification

- Focused label-three tests passed: 2 tests in 0.17 seconds.
- The complete cyclic-ratio test module passed all 33 tests in 16.63 seconds.
- The first complete-suite attempt had 31 setup errors because the sandbox
  denied the requested `C:\tmp` base directory; 178 tests passed and no
  functional assertion failed. The identical rerun with that permission
  restriction removed passed all 209 tests in 76.87 seconds.
- Explicit checked-artifact schema validation passed all 4 tests in 0.97
  seconds.
- The unchanged checked-artifact semantic verifier accepted 4 certificates,
  76 embedded local brackets, and the checked `n=3..6` summary.
- Targeted Ruff and Python compilation passed.
- Independent mathematical, test, and documentation audits reconstructed the
  proof, independently recomputed all rows and argmaxes, checked exact oracle
  coverage and separation, audited Python 3.11 APIs, and confirmed the scope
  boundary.
- The complete diff, every new dossier file, changed-file whitespace,
  `git diff --check`, absence of a `src/` diff, production boundary, staged
  state, and task-created temporary paths were inspected; nothing is staged
  and no temporary path remains.
- CURRENT HOSTED STATUS: GitHub Actions on Ubuntu/Python 3.11--3.13 has not
  been run or independently verified for this worktree.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` adds the exact label-three insertion
  formula, shortcut certificates, 14-row classification, argmax data, and
  independent-oracle record.
- `tests/test_fixed_order_cycle_ratio.py` adds separate structural and literal
  subset checks for the 14 insertions.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize the theorem, evidence roles,
  limitations, and next research boundary.
- `CURRENT_STATUS.md` and the STRICT task dossier record the durable handoff.

## Residual Limitations

- Label `2` remains unplaced. A partial cycle with \(K_{\ge3}=323\) is only a
  surviving necessary case, not yet a proved minimizing full-core order.
- The task does not classify or count the minimizing `n=10` core orders.
- It is finite and combinatorial. It gives no exact value of \(R_2^*(10)\),
  geometric minimizer statement, all-`n` formula, or asymptotic claim.
- Local execution used Python 3.14.3. Python 3.11 compatibility was audited
  syntactically and at the API level but not run locally.
- Hosted GitHub Actions for this worktree has not been inspected.

## Proposed Next Task

In a fresh chat, classify insertion of label `2` into the eleven surviving
partial cycles, using the recorded argmax and shortcut data and an independent
bounded oracle. Do not state a full-core count until that proof is complete.
