# EVIDENCE - TASK-20260712__finite_results_summary_contract / Finite Results Summary Contract

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source/command/file | Startup and required pre-implementation design note | startup files, previous task dossier, `git status --short`, `DESIGN.md` | PASS |
| EV-002 | file/source | Implementation of derived v1 summary contract | `src/power_ringmin/finite_results.py`, schema, tests, docs | PASS |
| EV-003 | test/artifact | Focused tests, checked artifact generation, full suite | `tests/test_finite_results.py`, `examples/finite_results_summary_n3_n6.json`, `python -m pytest` | PASS |
| EV-004 | command | Final status, diff, JSON, and whitespace hygiene | `git status --short`, `git diff`, `git diff --check`, JSON parsing, trailing-whitespace scan | PASS |

## EV-001 - Startup And Design Note

- **Date:** 2026-07-12
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `ops/TASK-20260712__certified_finite_results_extraction/`.
- **Method or command:** `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries.
- **Relevant output:** `DESIGN.md` records the primary-certificate versus derived-analysis split and keeps `power-ringmin.small_n_interval_certificate.v1` unchanged.
- **Interpretation:** The task starts from a clean tree and has the required design basis for a separate finite-results summary artifact.
- **Limitations:** This evidence does not verify the implementation, generated artifact, or tests.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup-and-design-contract`

## EV-002 - Implementation

- **Date:** 2026-07-12
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `power-ringmin.finite_results_summary.v1` artifact semantics in `src/power_ringmin/finite_results.py`.
- **Relevant output:** Added `schemas/finite_results_summary.schema.json` and documented it in `schemas/README.md`.
- **Relevant output:** Exported summary helpers and validation APIs from `src/power_ringmin/__init__.py`.
- **Relevant output:** Reworked `tests/test_finite_results.py` to cover schema structure, semantic validation, stale-source detection, candidate/gap regressions, deterministic generation, and checked artifact loading.
- **Interpretation:** The derived summary now has a separate contract with source hashes and semantic stale-summary rejection while leaving the primary small-n certificate v1 contract unchanged.
- **Limitations:** Implementation evidence is not a substitute for test execution.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---contract-implementation`

## EV-003 - Tests And Checked Artifact

- **Date:** 2026-07-12
- **Method or command:** `python -m pytest tests/test_finite_results.py -k "not checked_artifact_loader"`.
- **Relevant output:** `13 passed, 1 deselected in 5.78s`.
- **Method or command:** `python -c "import sys; sys.path.insert(0, r'src'); from power_ringmin.finite_results import main; raise SystemExit(main(['--created-at-utc', '2026-07-12T00:00:00Z', '--output', 'examples/finite_results_summary_n3_n6.json']))"`.
- **Relevant output:** Generated `examples/finite_results_summary_n3_n6.json`.
- **Method or command:** `python -m pytest tests/test_finite_results.py`.
- **Relevant output:** `14 passed in 6.08s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `82 passed in 19.70s`, then after documentation and memory updates `82 passed in 19.31s`.
- **Interpretation:** The checked example was generated only after semantic tests passed, and the generated example loads and validates against checked source certificates.
- **Limitations:** Passing tests do not establish exact optima, exact ties, or behavior beyond the listed finite inputs.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---checked-artifact-generation-and-tests`

## EV-004 - Final Hygiene

- **Date:** 2026-07-12
- **Method or command:** `git status --short`; `git diff --stat`; targeted `git diff`; `git diff --check`.
- **Relevant output:** Final status and diffs were inspected; `git diff --check` produced no output.
- **Method or command:** `python -m json.tool schemas/finite_results_summary.schema.json`; `python -m json.tool examples/finite_results_summary_n3_n6.json`.
- **Relevant output:** Both JSON files parsed successfully.
- **Method or command:** `rg -n "[ \t]+$" ...` over changed and new paths.
- **Relevant output:** No trailing-whitespace matches were found.
- **Interpretation:** Diff, JSON, and whitespace hygiene checks passed.
- **Limitations:** `git diff --check` does not include untracked files until staged, so JSON parsing and trailing-whitespace scans covered the new files explicitly.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---durable-memory-and-handoff`
