# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact finite evaluation of the reduced cyclic-ratio
  objective beyond the public enumeration boundary.
- **Current task:** prove \(\Lambda_{10}=323\) from a human-checkable
  seven-label pairing lemma and an exact shortcut-gain witness certificate.
- **Task dossier:**
  `ops/TASK-20260715__lambda10_exact_finite_value/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md` proves
  \[
  \max\{P_\omega(\{4,\ldots,10\}),
        P_\omega(\{5,\ldots,10\})\}\ge323
  \]
  for every cycle on \(\{4,\ldots,10\}\).
- The proof applies the duplicated-pairing relaxation to labels `5..10`,
  obtains baseline 320, and exhaustively classifies the only relevant integer
  levels: one pairing signature at 320, three at 321, and four at 322. Only
  one 322 signature is a simple six-cycle, and every insertion of label `4`
  into that cycle adds at least one.
- The same note records every nontrivial shortcut gain for
  `(10,2,3,4,7,8,6,9,5)`. The complete sum is 319; the only positive gains
  are `g(10,3)=4`, `g(10,4)=2`, and `g(10,7)=4`; none is nontrivially zero.
- `tests/test_fixed_order_cycle_ratio.py` adds a direct test-local oracle for
  the 360 lemma classes, the eight low pairing signatures and six insertion
  corrections, plus literal scoring of all 511 nonempty witness subsets.
- No production source, scorer, API, or canonicalizer changed; neither did any
  interval/checked artifact or schema. The complete-order enumerator remains
  hard-bounded to `n<=8`.

## Exact Finite Results

- EXACT THEOREM (FINITE SEVEN-LABEL LEMMA): the displayed maximum is at least
  323 for every cyclic order on labels `4..10`.
- VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT):
  \[
  K(10,2,3,4,7,8,6,9,5)=323,
  \qquad
  \Lambda_{10}=323.
  \]
- The witness has exactly two maximizing subsets:
  \(\{5,6,7,8,9,10\}\) and
  \(\{3,4,5,6,7,8,9,10\}\).
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the 360-class oracle
  has minimum 323 and exactly two computational equality rows. Literal
  evaluation of all 511 witness subsets reproduces the two argmax sets and
  the recorded unique maximum in every cardinality.

## Verification

- Focused `n=10` tests passed: 2 tests in 0.16 seconds.
- The complete cyclic-ratio test module passed all 30 tests in 15.17 seconds.
- The complete repository suite passed all 206 tests in 66.94 seconds.
- Explicit checked-artifact schema validation passed all 4 tests in 0.79
  seconds.
- The unchanged checked-artifact semantic verifier accepted 4 certificates,
  76 embedded local brackets, and the checked `n=3..6` summary.
- Targeted Ruff and Python compilation passed.
- Independent mathematical, test, and documentation audits reconstructed the
  proof and finite data, verified Python 3.11 syntax/API compatibility, and
  confirmed that the new paths call no production scorer or canonicalizer.
- The complete diff, changed-file whitespace, `git diff --check`, absence of
  a `src/` diff, and production boundary were inspected; no task-created
  temporary directory remains and nothing is staged.
- CURRENT HOSTED STATUS: GitHub Actions on Ubuntu/Python 3.11--3.13 has not
  been run or independently verified for this worktree.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` adds the exact lemma, pairing
  classification, insertion correction, witness certificate, and finite
  oracle report.
- `tests/test_fixed_order_cycle_ratio.py` adds the independent 360-class and
  511-subset checks.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize the finite result, limits,
  and follow-up boundary.
- `CURRENT_STATUS.md` and the STRICT task dossier record the durable handoff.

## Residual Limitations

- This task does not classify all `n=10` core minimizers. The oracle lists two
  lemma equality cycles, but their separate structural equality proof is a
  possible follow-up.
- The result is combinatorial and finite. It gives no exact value of
  \(R_2^*(10)\), geometric minimizer statement, all-`n` formula, or
  asymptotic claim.
- Local execution used Python 3.14.3. Python 3.11 compatibility was audited
  syntactically and at the API level but not run locally.
- Hosted GitHub Actions for this worktree has not been inspected.

## Proposed Next Task

In a fresh chat, give a human-checkable structural proof that the two equality
cycles already listed by the independent `n=10` lemma oracle are exhaustive,
without yet placing labels `2` and `3`, classifying all core minimizers, or
changing production.
