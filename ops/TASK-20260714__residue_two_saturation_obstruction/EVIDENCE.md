# EVIDENCE - TASK-20260714__residue_two_saturation_obstruction / Residue-Two Saturation Obstruction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / repository state | Startup and symbolic route | project memory, proof/source/tests, clean Git tree | PASS |
| EV-002 | proof / test / independent review | Proof and independent falsification tests | proof note, product-distance tests, three audits | PASS after test-harness correction |
| EV-003 | command / test / artifact / style | Integrated, full, artifact, and style verification | repository test and verification commands | PASS with retained environment/pre-existing findings |
| EV-004 | documentation / independent review / hygiene | Final documentation, scope, and diff audit | exact nine-path worktree delta | PASS |

## EV-001 - Startup And Symbolic Route

- **Date:** 2026-07-14
- **Method or command:** Read all required startup files and relevant
  predecessor task memory; inspected `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`, `tests/test_product_distance.py`,
  and `research/NEXT_RESEARCH_STEPS.md`; ran read-only `git status`; assigned
  three independent read-only audits.
- **Relevant output:** Initial tree clean. For `n=5k+2`, the interval
  `H_n<=T<J_n` forces `b_T=d_n-1`, exactly `2k` compatible lows for `2k`
  terminal incidences, and a unique possible terminal label at distance two
  from `x=d_n-2`. The same mechanism starts at the exact exceptional value
  `H_12=56` and targets `J_12=60`.
- **Interpretation:** The task has a symbolic all-`n` proof route; finite tests
  will serve only as independent falsification support.
- **Limitations:** This startup evidence alone did not close the strict
  inequalities, low-set cap, or terminal-position distinction; EV-002 and
  EV-004 record their completed proof and final independent audits.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---startup-and-proof-route`

## EV-002 - Proof And Independent Falsification Tests

- **Date:** 2026-07-14
- **Method or command:** Wrote R2S1--R2S12 in
  `research/PRODUCT_DISTANCE_SURROGATE.md`; added two independent tests in
  `tests/test_product_distance.py`; ran the focused product-distance suite;
  obtained separate mathematical, test, and consequence audits.
- **Relevant output:** For `n=12,17,22`, the tests reconstruct all 40
  half-integer states in `[H_n,J_n)`, directly obtaining `b_T=d-1`, the
  exact terminal and compatible-low sets, saturation cardinalities, the only
  possible distance-two terminal, and distinct positions `p(x)-2,p(x)+2`. At
  `T=J_n`, they verify that `d/2` and terminal `d` become compatible. A
  separate exact sweep checks the symbolic endpoint inequalities and widths
  for all 999 values `2<=k<=1000`.
- **Failed check retained:** the first focused run reported 3 failures and 32
  passes because Python `range` does not accept an integral `Fraction`.
  Converting the already integral doubled endpoints to their integer
  numerators changed no mathematical condition; the rerun passed all 35
  focused items.
- **Interpretation:** The finite checks actively test the strict boundaries
  but do not prove the all-`n` result; R2S1--R2S12 provide the symbolic proof.
- **Limitations:** No cyclic order was enumerated beyond `n=11`, and no
  matching construction, exact-value claim, or geometric statement was made.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---symbolic-proof-and-independent-tests`

## EV-003 - Integrated, Full, Artifact, And Style Verification

- **Date:** 2026-07-14
- **Method or command:** Ran
  `python -m py_compile tests\test_product_distance.py`; focused and
  integrated pytest with
  `PYTHONPATH=src`; full pytest inside the sandbox with an explicit temporary
  path and outside the sandbox; `python -m power_ringmin.verify_checked_artifacts`;
  and Ruff both with and without the pre-existing `F841` finding ignored.
- **Relevant output:** Targeted `4/4`; focused `35/35`; integrated `50/50`;
  full unsandboxed `163/163`; checked artifacts `certificates=4`,
  `local_brackets=76`, summary values `3,4,5,6`; compile PASS; Ruff with
  `--ignore F841` PASS.
- **Failed checks retained:** sandboxed full pytest reported `132 passed, 31
  errors`, all from denied creation of its temporary directory. Unmodified
  Ruff reported only `F841` for `t = n // 2` at line 566; `git show HEAD`
  confirms that line predates this task.
- **Interpretation:** The unsandboxed rerun resolves the environment-only
  full-suite failure, and no new lint finding is present in the changed lines.
- **Limitations:** Hosted GitHub Actions for the current worktree was not
  inspected.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---integrated-full-and-artifact-verification`

## EV-004 - Final Documentation, Scope, And Diff Audit

- **Date:** 2026-07-14
- **Method or command:** Obtained final read-only mathematical, test, and
  cross-document audits; inspected the complete tracked diff and all three
  untracked dossier files; scanned the nine paths with strict UTF-8 decoding
  and trailing-whitespace detection; checked proof display delimiters and tag
  uniqueness; ran `git status`, `git diff --stat`, and `git diff --check`.
- **Relevant output:** All three audits PASS after applying two optional
  strict-mode clarifications. Exactly 6 tracked and 3 dossier paths are in
  scope. Strict UTF-8 and whitespace PASS; proof displays `243/243`; 130 tags
  are unique; final diff check PASS.
- **Interpretation:** Proof, tests, durable memory, current status, roadmap,
  and evidence agree on the theorem, its non-exact scope, and verification
  boundary. The worktree is ready for manual review.
- **Limitations:** The worktree is intentionally unstaged and uncommitted;
  hosted CI remains unchecked.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---final-documentation-and-diff-audit`
