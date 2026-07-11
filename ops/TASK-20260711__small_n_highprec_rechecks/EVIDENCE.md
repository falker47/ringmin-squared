# EVIDENCE - TASK-20260711__small_n_highprec_rechecks / Small-n High-Precision Rechecks

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Implementation and artifact contract | `src/power_ringmin/search_small_n.py`, `tests/test_search_small_n.py` | PASS |
| EV-002 | test/command | Focused and full tests | `python -m pytest tests\test_search_small_n.py`; `python -m pytest` | PASS |
| EV-003 | command/file | Source-tree CLI smoke artifact | `small_n_search_n3_highprec_recheck_smoke.json` | PASS |
| EV-004 | file | Durable memory and handoff | `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, task dossier | PASS |
| EV-005 | command | Final diff and whitespace checks | `git status --short`; `git diff --stat`; `git diff --check`; `rg` trailing whitespace scan | PASS |

## EV-001 - Implementation Scope

- **Date:** 2026-07-11
- **Method or command:** Source inspection and edits using `apply_patch`.
- **Relevant output:** Added `HighPrecisionRecheckRecord`, default `mpmath` rechecks for the float64 incumbent/tie set, artifact `high_precision_recheck` serialization, recheck metadata validation, CLI `--highprec-recheck-digits`, and CLI `--no-highprec-recheck`.
- **Interpretation:** Small-n search outputs now include independent high-precision recomputation for selected incumbent/tie orders while keeping the primary search mode float64.
- **Limitations:** The implementation does not compute interval lower bounds for every canonical order and does not certify a global optimum.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---startup-and-implementation`

## EV-002 - Tests

- **Date:** 2026-07-11
- **Method or command:** `python -m pytest tests\test_search_small_n.py`.
- **Relevant output:** `7 passed in 0.54s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `37 passed in 5.83s`.
- **Interpretation:** Focused tests assert the default high-precision recheck, artifact metadata, validator consistency, and preserved `numerical_observation` classification. The full suite passed after the change.
- **Limitations:** Passing tests verify tested behavior only. They are not mathematical proof of optimality.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification`

## EV-003 - CLI Smoke Artifact

- **Date:** 2026-07-11
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.search_small_n --n 3 --top-k 5 --output ops\TASK-20260711__small_n_highprec_rechecks\small_n_search_n3_highprec_recheck_smoke.json --created-at-utc 2026-07-11T00:00:00Z`.
- **Relevant output:** `wrote ops\TASK-20260711__small_n_highprec_rechecks\small_n_search_n3_highprec_recheck_smoke.json n=3 backend=float64 enumerated=1 best_R=0.38338703613939273 highprec_rechecks=1`.
- **Interpretation:** The direct CLI path wrote an n=3 small-n search artifact with one high-precision recheck record for the float64 incumbent/tie order `(3,1,2)` / `(9,1,4)`. The artifact still records `evidence.classification = numerical_observation` and explicitly disclaims interval certification.
- **Limitations:** The smoke artifact covers n=3 only and is not a certified global optimum artifact.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---smoke-artifact-and-handoff`

## EV-004 - Durable Memory And Handoff

- **Date:** 2026-07-11
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Updated `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Interpretation:** Durable memory records the high-precision recheck behavior, tests, smoke artifact, classification boundary, and the next proposed task.
- **Limitations:** Durable memory records the current implementation state; the user still needs to review and commit manually.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---smoke-artifact-and-handoff`

## EV-005 - Final Diff And Whitespace Checks

- **Date:** 2026-07-11
- **Method or command:** `git status --short`.
- **Relevant output:** Tracked modifications and the new task dossier were present.
- **Method or command:** `git diff --stat`.
- **Relevant output:** Diff was scoped to the small-n search implementation, focused tests, durable status files, and task dossier.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" CURRENT_STATUS.md PROJECT_KNOWLEDGE.md src\power_ringmin\search_small_n.py tests\test_search_small_n.py ops\TASK-20260711__small_n_highprec_rechecks`.
- **Relevant output:** No matches.
- **Interpretation:** Final diff and whitespace checks passed.
- **Limitations:** `git diff --check` does not inspect untracked files until staged; the separate trailing-whitespace scan included the new task dossier.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---smoke-artifact-and-handoff`
