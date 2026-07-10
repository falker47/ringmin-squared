# EVIDENCE - TASK-20260710__fixed_order_artifact_schema / Fixed-Order Artifact Schema

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and existing fixed-order code inspection | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `src/power_ringmin/*.py`, `verify.py`, `tests/` | PASS |
| EV-002 | file | Schema, README, example fixture, and tests added | `schemas/`, `examples/`, `tests/test_fixed_order_artifact_schema.py` | PASS |
| EV-003 | test | Focused schema/example verification | `python -m pytest tests/test_fixed_order_artifact_schema.py` | PASS |
| EV-004 | test | Full repository test suite | `python -m pytest` | PASS |
| EV-005 | command | Final diff whitespace check | `git diff --check` | PASS |

## EV-001 - Startup Inspection

- **Date:** 2026-07-10
- **Method or command:** Read startup files and inspected fixed-order evaluator/verifier sources and tests.
- **Relevant output:** Initial `git status --short` produced no entries. Existing evaluator/verifier code works from explicit radius tuples and all-pairs STN feasibility. `verify.py` accepts minimal JSON payloads containing order/radius/positions.
- **Interpretation:** A canonical fixed-order artifact should require explicit radius sequence, explicit cyclic order, all-pairs evidence, numeric precision/tolerances, and reproducibility provenance.
- **Limitations:** Source inspection does not validate the new schema; tests are recorded separately.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---startup-and-design`

## EV-002 - Schema Files

- **Date:** 2026-07-10
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `schemas/fixed_order_result.schema.json`, `schemas/README.md`, `examples/fixed_order_result_n3.json`, and `tests/test_fixed_order_artifact_schema.py`.
- **Interpretation:** The design artifact exists and passed focused and full test verification.
- **Limitations:** Final diff inspection is recorded separately.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---schema-draft-added`

## EV-003 - Focused Schema Example Verification

- **Date:** 2026-07-10
- **Method or command:** `python -m pytest tests/test_fixed_order_artifact_schema.py`
- **Relevant output:** `3 passed in 0.07s`.
- **Interpretation:** The schema contract and n=3 fixture semantics passed focused checks, including standalone verifier feasibility, local bracket, and witness-position checks.
- **Limitations:** The tests do not exercise a third-party JSON Schema validator; they verify the project-level schema contract and fixture semantics.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---tests-passed`

## EV-004 - Full Test Suite

- **Date:** 2026-07-10
- **Method or command:** `python -m pytest`
- **Relevant output:** `11 passed in 1.40s`.
- **Interpretation:** Existing repository tests and new schema tests all pass.
- **Limitations:** Passing finite tests is not a theorem about all quadratic-radii instances.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---tests-passed`

## EV-005 - Final Diff Whitespace Check

- **Date:** 2026-07-10
- **Method or command:** `git status --short`; `git diff --stat`; `git diff --check`.
- **Relevant output:** `git status --short` showed modified `CURRENT_STATUS.md` and `PROJECT_KNOWLEDGE.md`, plus untracked `examples/`, `ops/TASK-20260710__fixed_order_artifact_schema/`, `schemas/`, and `tests/test_fixed_order_artifact_schema.py`. `git diff --check` produced no output.
- **Interpretation:** The worktree contains only the expected schema-task changes, and the tracked diff has no whitespace errors.
- **Limitations:** Because Codex must not stage files, `git diff --check` does not include untracked files until the user stages them for manual review.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---ready-for-review`
