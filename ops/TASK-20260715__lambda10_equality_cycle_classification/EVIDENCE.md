# EVIDENCE - TASK-20260715__lambda10_equality_cycle_classification / Lambda_10 Equality-Cycle Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection | Clean startup and equality reduction | authoritative files | PASS |
| EV-002 | exact proof | Tail-322 and tail-323 structural classification | proof note | PASS |
| EV-003 | exact computation / test | Independent branch and 360-class checks | focused test module | PASS |
| EV-004 | verification / audit | Full suite, artifact regressions, lint, audits | repository checks | PASS |
| EV-005 | hygiene | Final diff, whitespace, scope, and temp-path inspection | Git/worktree | PASS |

## EV-001 - Startup And Reduction

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the prior `n=10` dossier,
  proof note, tests, roadmap, and templates; ran `git status --short` and
  `git rev-parse --short=12 HEAD`.
- **Relevant output:** Clean startup at `5d94228ced7b`. Existing durable state
  identifies structural classification of the two oracle equality rows as the
  next bounded task.
- **Interpretation:** No unrelated change or missing dependency blocked work.
- **Limitations:** Startup inspection establishes scope, not the theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-equality-reduction`.

## EV-002 - Structural Equality Proof

- **Date:** 2026-07-15
- **Method:** Let `s=P(T6)` and `q=P(T7)=s+delta(a,b)`. Use the accepted
  pairing classification through 322, then constrain every possible insertion
  edge exactly in the 323 branch and apply the rearrangement lower bound to
  the residual multiset.
- **Relevant output:** Tail 322 forces the unique simple cycle
  `(10,5,9,7,8,6)` and correction `+1` on `{7,9}`. For tail 323, the 15 exact
  corrections leave four nonpositive edges; their fixed-edge pairing floors
  are 323, 323, 326, 330. The two equality residual signatures are unique;
  `{8,9}` yields a loop and repeated edge, while `{7,10}` yields
  `(10,5,9,6,8,7)` and correction `-2`. The resulting seven-label classes
  are exactly `(10,5,9,4,7,8,6)` and `(10,4,7,8,6,9,5)`.
- **Independent review:** A separate mathematical audit reconstructed every
  correction, floor, residual signature, recurrence state count, dihedral
  equivalence, and converse; its notation finding was applied.
- **Classification:** EXACT THEOREM (FINITE SEVEN-LABEL EQUALITY
  CLASSIFICATION).
- **Limitations:** No placement of labels `2` or `3`, core-minimizer
  classification, geometric conclusion, or all-`n` claim follows.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---structural-branch-proof`.

## EV-003 - Independent Test-Only Checks

- **Date:** 2026-07-15
- **Environment:** Windows, Python 3.14.3; exact integer arithmetic only in the
  new paths.
- **Oracle design:** Exhaustively pair explicit test-local multisets; compute
  cyclic scores literally; fix label `10`, directly permute labels `4..9`,
  and retain one orientation to obtain 360 dihedral classes. No new path calls
  a repository canonicalizer, public enumerator, or production scorer.
- **Relevant output:** The structural test reproduces all low signatures, 15
  possible corrections, four fixed-edge floors and unique residual minima,
  both branch insertions, and both score pairs. The separate 360-class sweep
  has minimum 323 and exactly the two proved rows.
- **Command:** `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py -k lambda10 --basetemp .tmp_pytest_lambda10_equality_focused`
  -> `3 passed, 28 deselected in 0.29s`.
- **Independent review:** A separate test audit reran the two classification
  tests (`2 passed, 29 deselected`) and found no independence, coverage, or
  Python 3.11 API defect.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** The 360-class sweep audits but does not prove the theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---independent-test-only-checks`.

## EV-004 - Complete Verification

- **Date:** 2026-07-15
- **Environment:** Windows, Python 3.14.3. Python 3.11 compatibility was
  audited statically; hosted GitHub Actions was not run or inspected.
- **Commands and relevant output:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp .tmp_pytest_lambda10_equality_module`
    -> `31 passed in 14.08s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider --basetemp .tmp_pytest_lambda10_equality_full`
    -> `207 passed in 66.86s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py --basetemp .tmp_pytest_lambda10_equality_schema`
    -> `4 passed in 0.88s`.
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
    -> accepted 4 certificates, 76 local brackets, and the checked summary.
  - `$env:PYTHONPATH='src'; python -m ruff check tests/test_fixed_order_cycle_ratio.py`
    -> `All checks passed!`.
  - `python -m compileall -q tests/test_fixed_order_cycle_ratio.py`
    -> exit code 0 with no output.
- **Independent audits:** mathematical, test, and documentation audits found
  no proof, coverage, independence, or scope defect after their precise
  notation/wording findings were applied.
- **Interpretation:** The implementation and documentation are locally
  verified; final diff hygiene is recorded separately.
- **Limitations:** Local success does not establish hosted CI status.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---complete-verification-in-progress`.

## EV-005 - Final Diff And Hygiene

- **Date:** 2026-07-15
- **Method or command:** Inspected `git status --short`, `git diff --stat`,
  `git diff --numstat`, the complete per-file diff, and every new dossier
  file; ran `git diff --check`, a trailing-whitespace scan over all changed
  paths, `git diff --name-only -- src`, a production-boundary search, and a
  task-temp directory search.
- **Relevant output:** Whitespace and `git diff --check` pass; the `src/` diff
  and task-temp search are empty; production remains bounded to `n<=8` and
  `MAX_CANONICAL_ORDERS=2520`; status shows only the seven in-scope tracked or
  untracked paths and no staged entry.
- **Interpretation:** The final worktree is internally consistent and ready
  for user review and a manual commit decision.
- **Limitations:** Read-only local diff inspection does not establish hosted
  CI status or perform a Git commit.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---final-hygiene-and-handoff`.
