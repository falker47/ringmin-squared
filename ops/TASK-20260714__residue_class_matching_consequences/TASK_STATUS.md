# TASK_STATUS - TASK-20260714__residue_class_matching_consequences / Residue-Class Matching Consequences

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** derive the exact residue-class formula for the terminal-high
  obstruction `H_n`, including the separate value at `n=12`, and combine it
  with the eight-twenty-fifths upper construction without extending canonical
  enumeration beyond `n=11`.
- **Expected output:** a symbolic five-residue theorem, exact equalities for
  `B_n` and `W_n` in residues `0,3,4`, exact theorem-threshold gaps in residues
  `1,2`, exact source support, independent formula tests, and minimal durable
  memory updates.

## Scope

- **In scope:** exact half-integer inversion consequences for `H_n`, the
  exceptional packing event at `n=12`, the existing uniform threshold `T_n`,
  one proof-note witness rename, exact formula support, and formula tests.
- **Out of scope:** a new cyclic-order construction; new all-`n` exact `B_n`
  or `W_n` formulas in residues `1,2`; canonical enumeration beyond `n=11`;
  geometric improvements; artifacts, schemas, CLIs, Git writes, or upstream
  changes.

## Verified Facts

- Startup files, the two relevant predecessor dossiers, the proof note, exact
  source/tests, and a clean initial Git worktree were inspected.
- Independent read-only audits agree on the five residue formulas, the exact
  exception `H_12=56`, and the two linear gaps to the uniform threshold.
- The existing event-set inversion remains available as an exact independent
  oracle for the new constant-time formula helper.
- The symbolic proof establishes the residue formula, the exact exception,
  the equality chain in residues `0,3,4`, and the exact interval widths in
  residues `1,2` without finite-order extrapolation.
- Exact source/test support, all local suites, checked-artifact verification,
  three independent audits, and final repository hygiene pass.

## Assumptions / Inferences

- The gap statements concern the uniform theorem threshold
  `T_n=d_n(d_n-1)/2`; they are not asserted optimality gaps or necessarily the
  score gaps of every displayed exceptional witness.

## Decisions And Rationale

- Keep `terminal_high_incidence_lower_obstruction` unchanged and add a public
  closed-form helper on the theorem domain `n>=9`, so definition-level event
  inversion and formula evaluation remain independent.
- Rename only the older asymptotic witness for `Q_n`; retain `T_n` for the
  matching construction already used throughout project memory.

## Plan And Expected Delta

- Derive and independently audit the residue formulas and boundary cases.
  COMPLETE.
- Add exact formula support and independent tests. COMPLETE.
- Update the proof note and derive exact residue-class consequences. COMPLETE.
- Update only necessary task/global memory. COMPLETE.
- Run focused, full, artifact, independent, and diff verification. COMPLETE.

## Verification

- **Checks:** compile, Ruff, focused/integrated/full pytest, checked-artifact
  verifier, independent formula diagnostics, mathematical/implementation/
  documentation audits, strict UTF-8, trailing whitespace, equation tags,
  display delimiters, path scope, complete diff, and `git diff --check`.
- **Observed result:** compile and Ruff PASS; focused `28/28`; integrated
  `43/43`; full suite `156/156` outside the sandbox; 4 certificates, 76 local
  brackets, and the `n=3..6` summary accepted; formula/event agreement through
  `n=200`; gap checks through `n=5000`; all audits and hygiene PASS.
- **Limitations:** a sandboxed full-suite run retained 31 setup errors and one
  Git-provenance mismatch caused by denied temporary-directory/metadata
  access; the identical suite passed outside the sandbox. No canonical
  enumeration above `n=11` was performed.

## Blockers / Risks

- No current blocker.
- The `n=12` exception is explicitly handled before the generic residue-two
  branch.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact proof/source/tests, full local verification,
  independent audits, necessary memory, and final diff hygiene all pass.
- **Files changed:** `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `start.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`, `tests/test_product_distance.py`,
  and this three-file task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`, and
  `tests/test_product_distance.py`.
