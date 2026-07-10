# EVIDENCE - TASK-20260710__batch_standalone_verifier_check / Batch Standalone-Verifier Check

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and existing verifier/artifact inspection | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `verify.py`, `src/power_ringmin/`, `tests/`, `schemas/` | PASS |
| EV-002 | file | Batch standalone-verifier CLI, verifier option, docs, and tests added | `src/power_ringmin/verify_fixed_order_artifacts_cli.py`, `verify.py`, `pyproject.toml`, `schemas/README.md`, `tests/test_verify_fixed_order_artifacts_cli.py` | PASS |
| EV-003 | test | Focused verifier tests and full repository tests | `python -m pytest tests/test_verify_fixed_order_artifacts_cli.py tests/test_crosscheck_and_verifier.py`; `python -m pytest` | PASS |
| EV-004 | command | Final diff and whitespace check | `git status --short`; `git diff --stat`; `git diff`; `git diff --check` | PASS |

## EV-001 - Startup Inspection

- **Date:** 2026-07-10
- **Method or command:** Read startup files, previous batch fixed-order artifact export task dossier, root standalone verifier, artifact helpers, exporter CLIs, tests, schema docs, and package metadata.
- **Relevant output:** Initial `git status --short` produced no entries. Existing `FixedOrderArtifact.to_verifier_payload()` derives the minimal payload accepted by root `verify.py`.
- **Interpretation:** A batch verifier can preserve the standalone verifier boundary by validating v1 artifacts in package code, writing minimal payloads, and invoking root `verify.py` as a subprocess.
- **Limitations:** Source inspection does not validate the new batch implementation; tests will be recorded separately.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---startup-and-scope`

## EV-002 - Batch Verifier Implementation

- **Date:** 2026-07-10
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `src/power_ringmin/verify_fixed_order_artifacts_cli.py`; registered `power-ringmin-verify-fixed-order-artifacts` in `pyproject.toml`; documented batch verification in `schemas/README.md`; added focused tests in `tests/test_verify_fixed_order_artifacts_cli.py`; added optional `verify.py --stn-tol`.
- **Interpretation:** The package now has a directory-level standalone-verifier check for v1 fixed-order artifacts.
- **Limitations:** File edits alone do not validate behavior; tests are recorded separately.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---batch-verifier-added`

## EV-003 - Focused And Full Tests

- **Date:** 2026-07-10
- **Method or command:** `python -m pytest tests/test_verify_fixed_order_artifacts_cli.py tests/test_crosscheck_and_verifier.py`; `python -m pytest`.
- **Relevant output:** An initial focused run reported one expectation failure because float64 artifacts include witness positions and the standalone verifier reported `witness=PASS` rather than `witness=SKIP`. A subsequent focused run exposed Windows subprocess handle errors under pytest capture; the runner was fixed to use `stdin=subprocess.DEVNULL`, explicit `stdout=subprocess.PIPE`, explicit `stderr=subprocess.PIPE`, and string `cwd`. Final focused tests reported `8 passed in 1.66s`. Full repository suite reported `28 passed in 2.90s`.
- **Interpretation:** The batch verifier passed tests for mpmath artifact directories with recorded local eta, float64 artifacts with explicit STN tolerance, deliberately weakened artifact failure, empty directory rejection, console-script metadata, and existing standalone verifier behavior.
- **Limitations:** Tests cover finite small explicit orders only. Passing tests do not establish a global optimum, certified quadratic-radii result, or theorem. Console script registration is checked from `pyproject.toml`; the package was not installed into a separate environment.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---tests-passed`

## EV-004 - Final Diff And Whitespace Check

- **Date:** 2026-07-10
- **Method or command:** `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Relevant output:** `git status --short` showed modified `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `pyproject.toml`, `schemas/README.md`, and `verify.py`, plus untracked `ops/TASK-20260710__batch_standalone_verifier_check/`, `src/power_ringmin/verify_fixed_order_artifacts_cli.py`, and `tests/test_verify_fixed_order_artifacts_cli.py`. `git diff --check` produced no output.
- **Interpretation:** The worktree contains the expected batch verifier task changes, and the tracked diff has no whitespace errors.
- **Limitations:** Because Codex must not stage files, `git diff --check` does not include untracked files until the user stages them for manual review; the new Python files were exercised by the test suite.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---ready-for-review`
