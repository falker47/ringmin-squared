# EVIDENCE - TASK-20260711__small_n_float64_search / Small-n Float64 Search

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Implementation and test scope | `src/power_ringmin/search_small_n.py`, `tests/test_search_small_n.py`, `pyproject.toml` | PASS |
| EV-002 | test/command | Focused small-n search tests | `python -m pytest tests\test_search_small_n.py` | PASS |
| EV-003 | test/command | Full test suite | `python -m pytest` | PASS |
| EV-004 | command/file | Source-tree CLI smoke | `power_ringmin.search_small_n`, `small_n_search_n3_smoke.json` | PASS after two setup/path failures |
| EV-005 | file | Durable memory and handoff | `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, task dossier | PASS |
| EV-006 | command | Final diff and whitespace checks | `git status --short`; `git diff --stat`; `git diff --check`; `rg` trailing whitespace scan | PASS |

## EV-001 - Implementation And Test Scope

- **Date:** 2026-07-11
- **Method or command:** Source inspection and file edits using `apply_patch`.
- **Relevant output:** Added `src/power_ringmin/search_small_n.py`; registered `power-ringmin-search-small-n`; added `tests/test_search_small_n.py`.
- **Interpretation:** The new search layer exhaustively enumerates canonical quadratic index orders modulo rotation/reflection and evaluates them with the existing float64 all-pairs fixed-order STN evaluator. Its artifact helper requires `evidence.classification == "numerical_observation"` and rejects `computer_certified_result`.
- **Limitations:** Source inspection and tests do not certify a global optimum. The implementation is a float64 baseline for finite small-n exploration.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---startup-and-implementation`

## EV-002 - Focused Tests

- **Date:** 2026-07-11
- **Method or command:** `python -m pytest tests\test_search_small_n.py`.
- **Relevant output:** `7 passed in 0.37s`.
- **Interpretation:** Focused tests cover canonical counts for n=3 through n=8, rotation/reflection canonicalization, quadratic index-to-radius conversion, n=3 exhaustive search behavior, artifact validation rejection for mismatched/certified outputs, CLI JSON output, and console script registration.
- **Limitations:** The tests use small finite examples and do not certify global optima.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification`

## EV-003 - Full Test Suite

- **Date:** 2026-07-11
- **Method or command:** `python -m pytest`.
- **Relevant output:** `37 passed in 6.71s`.
- **Interpretation:** The full repository test suite passed after adding the small-n float64 search implementation.
- **Limitations:** Passing tests verify tested behavior only. They do not prove a theorem about all n and do not establish certified global optimality.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification`

## EV-004 - Source-Tree CLI Smoke

- **Date:** 2026-07-11
- **Method or command:** `python -m power_ringmin.search_small_n --n 3 --top-k 5 --output C:\tmp\power_ringmin_small_n_search_smoke.json --created-at-utc 2026-07-11T00:00:00Z`.
- **Relevant output:** Failed with `ModuleNotFoundError: No module named 'power_ringmin'`.
- **Interpretation:** Direct `python -m` source-tree invocation requires the package to be installed or `PYTHONPATH=src`.
- **Limitations:** This was an invocation setup failure, not a search failure.
- **Method or command:** Source-tree rerun with `PYTHONPATH=src` and output path `C:\tmp\power_ringmin_small_n_search_smoke.json`.
- **Relevant output:** Failed with `[Errno 13] Permission denied`; it also exposed a `runpy` warning caused by importing `search_small_n` from package `__init__`, which was removed.
- **Interpretation:** The output path was unsuitable in this environment, and the package `__init__` should not import a module intended for `python -m` execution.
- **Limitations:** This was a path/package-surface issue, not a numerical result.
- **Method or command:** Source-tree rerun with `PYTHONPATH=src` and output path `ops\TASK-20260711__small_n_float64_search\small_n_search_n3_smoke.json`.
- **Relevant output:** `wrote ops\TASK-20260711__small_n_float64_search\small_n_search_n3_smoke.json n=3 backend=float64 enumerated=1 best_R=0.38338703613939273`.
- **Interpretation:** The CLI successfully wrote an n=3 small-n search artifact. The artifact records canonical index order `[3, 1, 2]`, radius order `[9, 1, 4]`, all-pairs checked metadata, and `evidence.classification = numerical_observation`.
- **Limitations:** This is a finite float64 numerical observation for n=3 only, not a certified global optimum.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification`

## EV-005 - Durable Memory And Handoff

- **Date:** 2026-07-11
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Updated `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Interpretation:** Durable memory now records the small-n search implementation, CLI registration, test results, and the n=3 smoke artifact as a numerical observation.
- **Limitations:** Durable memory records the current implementation state; the user still needs to review and commit manually.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---ready-for-review`

## EV-006 - Final Diff And Whitespace Checks

- **Date:** 2026-07-11
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `pyproject.toml`; untracked paths: `ops/TASK-20260711__small_n_float64_search/`, `src/power_ringmin/search_small_n.py`, `tests/test_search_small_n.py`.
- **Method or command:** `git diff --stat`.
- **Relevant output:** Tracked diff summary: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, and `pyproject.toml` with 15 insertions and 5 deletions. New untracked files are not included in `git diff --stat`.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" CURRENT_STATUS.md PROJECT_KNOWLEDGE.md pyproject.toml src\power_ringmin\search_small_n.py tests\test_search_small_n.py ops\TASK-20260711__small_n_float64_search`.
- **Relevant output:** No matches.
- **Interpretation:** The final tracked diff has no whitespace errors, and the changed/untracked task files have no trailing whitespace.
- **Limitations:** `git diff --check` does not inspect untracked files until they are staged; the separate `rg` scan included the untracked files.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---ready-for-review`
