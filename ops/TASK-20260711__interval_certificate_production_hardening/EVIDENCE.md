# EVIDENCE - TASK-20260711__interval_certificate_production_hardening / Interval Certificate Production Hardening

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and source audit | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, prior task dossiers, interval certificate source/tests | PASS |
| EV-002 | file | Production hardening implementation | `src/`, `tests/`, `schemas/`, `examples/`, `pyproject.toml` | PASS |
| EV-003 | test | Focused interval certificate hardening tests | `tests/test_interval_verifier.py`, `tests/test_small_n_interval_certificate.py` | PASS after initial failure |
| EV-004 | command | Full verification and final diff checks | `python -m pytest`; Git/diff/whitespace checks | PASS |

## EV-001 - Startup And Source Audit

- **Date:** 2026-07-11
- **Method or command:** Read project startup files, prior interval-certificate task memory, `src/power_ringmin/interval_verifier.py`, `src/power_ringmin/interval_bracket_exporter.py`, `src/power_ringmin/small_n_interval_certificate.py`, and related tests.
- **Relevant output:** Initial `git status --short` produced no entries. `CURRENT_STATUS.md` named interval-certificate production hardening as the proposed next task.
- **Interpretation:** The repository is ready for a bounded hardening task. Current `n=3` and `n=4` artifacts are checked examples only; no `n=5` artifact should be generated in this task.
- **Limitations:** Source audit identifies hardening opportunities but does not itself change or verify behavior.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---startup-and-audit`

## EV-002 - Implementation

- **Date:** 2026-07-11
- **Method or command:** File edits using `apply_patch`; regenerated existing checked `n=3`/`n=4` examples through the package exporters.
- **Relevant output:** Added `schemas/small_n_interval_certificate.schema.json`; registered `power-ringmin-export-small-n-interval-certificate`; added a bounded general exporter/dry-run path; hardened aggregate validation; changed local interval verification to parse decimals at oracle precision; regenerated `examples/small_n_interval_certificate_n3.json` and `examples/small_n_interval_certificate_n4.json`.
- **Interpretation:** The production path now has a structural schema, stricter semantic validation, precision-aware decimal handling, and an explicit order-count gate before larger finite certificate generation.
- **Limitations:** The implementation still relies on the documented guarded `mpmath.iv` interval backend contract and does not generate an `n=5` artifact.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---implementation`

## EV-003 - Focused Tests

- **Date:** 2026-07-11
- **Method or command:** Initial `python -m pytest tests\test_interval_verifier.py tests\test_small_n_interval_certificate.py`.
- **Relevant output:** Initial run failed with 10 small-n certificate failures and 14 passes. The failures were summary decimal mismatches after stricter recomputation.
- **Interpretation:** The failing run exposed a real hardening issue: summary decimals were formatted through ambient low precision. The formatter was changed to honor the requested precision, and the existing checked examples were regenerated.
- **Limitations:** This was an intermediate failure, not the final verification result.
- **Method or command:** Mistaken `node --check src\power_ringmin\small_n_interval_certificate.py`.
- **Relevant output:** Failed because Node cannot syntax-check a Python file with extension `.py`.
- **Interpretation:** This was an operator/tool-selection mistake and not evidence about Python source validity.
- **Limitations:** Superseded by Python test execution.
- **Method or command:** Final `python -m pytest tests\test_interval_verifier.py tests\test_small_n_interval_certificate.py`.
- **Relevant output:** `24 passed in 3.45s`.
- **Interpretation:** Focused tests verify oracle-precision decimal parsing, schema contract checks, stricter summary/aggregation validation, checked example loading, and the bounded generic dry-run/export CLI behavior.
- **Limitations:** Focused tests cover finite fixtures and CLI behavior only; they do not prove a theorem for all `n`.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification-and-handoff`

## EV-004 - Full Verification And Diff Checks

- **Date:** 2026-07-11
- **Method or command:** `python -m pytest`.
- **Relevant output:** `66 passed in 12.66s`.
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, existing `examples/`, `pyproject.toml`, `schemas/README.md`, source files, and tests. New untracked paths: this task dossier and `schemas/small_n_interval_certificate.schema.json`.
- **Method or command:** `git diff --stat`.
- **Relevant output:** Tracked diff showed 11 tracked files changed with 512 insertions and 62 deletions; new untracked schema/task files are visible in `git status --short`.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" PROJECT_KNOWLEDGE.md CURRENT_STATUS.md pyproject.toml schemas src tests ops\TASK-20260711__interval_certificate_production_hardening examples\small_n_interval_certificate_n3.json examples\small_n_interval_certificate_n4.json`.
- **Relevant output:** No matches.
- **Interpretation:** Full tests and final diff hygiene checks passed after the production-path hardening.
- **Limitations:** `git diff --check` does not inspect untracked files until staged, so the separate trailing-whitespace scan included the new schema and dossier files.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification-and-handoff`
