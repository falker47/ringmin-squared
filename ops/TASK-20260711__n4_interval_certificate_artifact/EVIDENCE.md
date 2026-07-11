# EVIDENCE - TASK-20260711__n4_interval_certificate_artifact / N=4 Interval Certificate Artifact

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and task setup | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `ops/TASK-20260711__n4_finite_certificate_next_step_design/`, certificate source/tests | PASS |
| EV-002 | source / test | Bounded n=4 export path | `src/power_ringmin/small_n_interval_certificate.py`, `tests/test_small_n_interval_certificate.py`, `pyproject.toml` | PASS |
| EV-003 | command | Checked n=4 artifact generation and reload validation | `examples/small_n_interval_certificate_n4.json` | PASS |
| EV-004 | test | Focused and full automated tests | `tests/test_small_n_interval_certificate.py`, full test suite | PASS |
| EV-005 | command | Final diff and whitespace checks | Git status/diff plus tracked/untracked whitespace scan | PASS |

## EV-001 - Startup And Task Setup

- **Date:** 2026-07-11
- **Method or command:** Read project startup files, the prior `n=4` finite-certificate design dossier, and current certificate source/tests. Inspected the initial working tree with `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries. The prior design task recorded a passing in-memory `n=4` aggregate certificate probe over exactly three canonical orders.
- **Interpretation:** The bounded `n=4` artifact/export implementation can proceed.
- **Limitations:** Startup inspection does not itself create or validate the checked artifact.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---startup-and-task-setup`

## EV-002 - Bounded N=4 Export Path

- **Date:** 2026-07-11
- **Method or command:** Source edits using `apply_patch`; `python -m pytest tests\test_small_n_interval_certificate.py::test_n4_interval_certificate_fixture_covers_every_canonical_order -q`.
- **Relevant output:**
  ```text
  .                                                                        [100%]
  ```
- **Interpretation:** The bounded n=4 fixture builder generated and validated exactly the three canonical n=4 local brackets in memory.
- **Limitations:** This focused test alone did not write the checked artifact.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---bounded-export-path-and-tests`

## EV-003 - Checked N=4 Artifact Generation

- **Date:** 2026-07-11
- **Method or command:** `python -c "import sys; sys.path.insert(0, 'src'); from power_ringmin.small_n_interval_certificate import main_n4; raise SystemExit(main_n4(['--output', 'examples/small_n_interval_certificate_n4.json', '--digits', '80', '--guard-decimal', '1e-70', '--radius-eta', '1e-4', '--max-canonical-orders', '3', '--local-max-attempts', '8', '--created-at-utc', '2026-07-11T00:00:00Z']))"`.
- **Relevant output:**
  ```text
  wrote examples\small_n_interval_certificate_n4.json n=4 bracket=(1.4955284118749971877804227915476076304912567138671875, 1.4957284118749971657535979829845018684864044189453125] classification=computer_certified_result covered=3
  ```
- **Method or command:** Reloaded `examples/small_n_interval_certificate_n4.json` with `load_small_n_interval_certificate_artifact` and printed the summary fields.
- **Relevant output:**
  ```text
  n 4
  covered 3
  lower 1.4955284118749971877804227915476076304912567138671875
  upper 1.4957284118749971657535979829845018684864044189453125
  lower_source [4, 1, 3, 2]
  upper_source [4, 1, 3, 2]
  classification computer_certified_result
  ```
- **Interpretation:** The checked artifact was written only through the validating bounded exporter and reload validation accepted it.
- **Limitations:** The artifact is finite n=4 evidence under the local interval-verifier semantics; it is not an exact optimum value and not a theorem for all `n`.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---checked-n4-artifact-generation`

## EV-004 - Focused And Full Tests

- **Date:** 2026-07-11
- **Method or command:** `python -m pytest tests\test_small_n_interval_certificate.py -q`.
- **Relevant output:** `12 passed`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `60 passed in 11.89s`.
- **Interpretation:** The focused small-n certificate tests and full repository test suite passed after adding the bounded n=4 export path and checked artifact.
- **Limitations:** Automated tests validate the implemented finite cases and schema semantics only; they do not remove the documented interval-backend provenance limitation.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification-and-memory-update`

## EV-005 - Final Diff And Whitespace Checks

- **Date:** 2026-07-11
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `pyproject.toml`, `src/power_ringmin/small_n_interval_certificate.py`, `tests/test_small_n_interval_certificate.py`. New untracked paths: `examples/small_n_interval_certificate_n4.json`, `ops/TASK-20260711__n4_interval_certificate_artifact/`.
- **Method or command:** `git diff --stat`.
- **Relevant output:** Tracked diff showed five modified tracked files with `344 insertions(+)` and `16 deletions(-)`. New untracked files are visible in `git status --short`, not tracked diff stats.
- **Method or command:** Tracked `git diff` inspection.
- **Relevant output:** The tracked diff was limited to current-status/project-knowledge handoff updates, n=4 console registration, bounded n=4 exporter code, and focused n=4 tests.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" PROJECT_KNOWLEDGE.md CURRENT_STATUS.md pyproject.toml src\power_ringmin\small_n_interval_certificate.py tests\test_small_n_interval_certificate.py examples\small_n_interval_certificate_n4.json ops\TASK-20260711__n4_interval_certificate_artifact`.
- **Relevant output:** No matches.
- **Interpretation:** The final review checks found no whitespace errors and no out-of-scope tracked diff.
- **Limitations:** Untracked new files require user review and manual Git staging/commit.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification-and-memory-update`
