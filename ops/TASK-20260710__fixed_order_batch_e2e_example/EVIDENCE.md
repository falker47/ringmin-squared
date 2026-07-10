# EVIDENCE - TASK-20260710__fixed_order_batch_e2e_example / Fixed-Order Batch End-To-End Example

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and existing CLI inspection | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `src/power_ringmin/`, `tests/`, `schemas/`, `examples/` | PASS |
| EV-002 | file | End-to-end example files, schema-doc pointer, and regression test added | `examples/fixed_order_batch_end_to_end/`, `schemas/README.md`, `tests/test_examples_fixed_order_batch_e2e.py` | PASS |
| EV-003 | test | Focused example, focused exporter/verifier, and full repository tests | `python -m pytest tests/test_examples_fixed_order_batch_e2e.py`; `python -m pytest tests/test_examples_fixed_order_batch_e2e.py tests/test_fixed_order_artifact_batch_cli.py tests/test_verify_fixed_order_artifacts_cli.py`; `python -m pytest` | PASS |
| EV-004 | command | Final diff and whitespace check | `git status --short`; `git diff --stat`; `git diff`; `git diff --check` | PASS |

## EV-001 - Startup Inspection

- **Date:** 2026-07-10
- **Method or command:** Read startup files, previous batch export and batch verifier task dossiers, exporter/verifier source files, tests, schema docs, package metadata, and existing examples.
- **Relevant output:** Initial `git status --short` produced no entries. Existing CLIs support a high-precision batch export from `index_orders` and batch standalone verification of the generated artifact directory.
- **Interpretation:** A small reproducible example can reuse the established CLIs without changing artifact schema or verifier logic.
- **Limitations:** Source inspection does not validate the new example; command and test verification will be recorded separately.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---startup-and-scope`

## EV-002 - Example Files And Test

- **Date:** 2026-07-10
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `examples/fixed_order_batch_end_to_end/README.md`; added `examples/fixed_order_batch_end_to_end/index_orders.json`; added `tests/test_examples_fixed_order_batch_e2e.py`; added a pointer from `schemas/README.md` to the example.
- **Interpretation:** The repository now includes a checked-in input batch and instructions for exporting and verifying generated fixed-order artifacts end to end.
- **Limitations:** File edits alone do not validate the example; tests are recorded separately.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---example-added`

## EV-003 - Focused And Full Tests

- **Date:** 2026-07-10
- **Method or command:** `python -m pytest tests/test_examples_fixed_order_batch_e2e.py`; `python -m pytest tests/test_examples_fixed_order_batch_e2e.py tests/test_fixed_order_artifact_batch_cli.py tests/test_verify_fixed_order_artifacts_cli.py`; `python -m pytest`.
- **Relevant output:** Initial focused run failed with a Windows subprocess handle error under pytest capture; the test was changed to use `stdin=subprocess.DEVNULL`, explicit `stdout=subprocess.PIPE`, and explicit `stderr=subprocess.PIPE`. A subsequent focused run failed because the attempted n=4 high-precision order was rejected by the exporter as infeasible at the requested precision; the example was changed to two n=3 orders. Final focused example test reported `1 passed in 1.04s`. Focused example/exporter/verifier tests reported `11 passed in 2.55s`. Full repository suite reported `29 passed in 4.53s`.
- **Interpretation:** The source-checkout module entry-point variant of the documented example exports two high-precision artifacts into a temporary directory and verifies them through the batch standalone-verifier path.
- **Limitations:** Tests cover finite small explicit orders only. Passing tests do not establish a global optimum, certified quadratic-radii result, or theorem. Installed console-script execution was not run in a separate environment.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---tests-passed`

## EV-004 - Final Diff And Whitespace Check

- **Date:** 2026-07-10
- **Method or command:** `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Relevant output:** Final `git status --short` showed modified `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, and `schemas/README.md`, plus untracked `examples/fixed_order_batch_end_to_end/`, `ops/TASK-20260710__fixed_order_batch_e2e_example/`, and `tests/test_examples_fixed_order_batch_e2e.py`. `git diff --check` produced no output.
- **Interpretation:** The tracked diff is scoped to current status, project knowledge, and schema docs, while the untracked files are the expected new example, task dossier, and regression test.
- **Limitations:** Because Codex must not stage files, `git diff --check` does not include untracked files until the user stages them for manual review; the new Python test file was exercised by the test suite and the new Markdown/JSON files were manually inspected.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---ready-for-review`
