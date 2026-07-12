# EVIDENCE - TASK-20260712__verification_trust_layer_ci / Verification Trust Layer And CI

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source/command | Startup and source audit | startup files, prior dossiers, verifier/schema/tests, `git status --short` | PASS |
| EV-002 | file/test | Local verifier hardening | `src/power_ringmin/interval_verifier.py`, interval and small-n certificate tests | PASS |
| EV-003 | file/test/command | Schema and checked-artifact verification | `verify_checked_artifacts.py`, schema tests, checked-artifact tests and command | PASS |
| EV-004 | file/command/test | Documentation, CI, and final verification | trust note, workflow, project memory, pytest, hygiene checks | PASS |

## EV-001 - Startup And Source Audit

- **Date:** 2026-07-12
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, prior task status/evidence, verifier and artifact validator sources, schema files, and tests.
- **Method or command:** `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries.
- **Relevant output:** `src/power_ringmin/interval_verifier.py` checked fixed-order interval schema version but did not yet check local `artifact_type`; backend matching checked `backend`, `precision_digits`, and `guard_decimal` exactly, but accepted any non-empty `rounding_policy`.
- **Interpretation:** The bounded task starts cleanly and the requested hardening has identifiable implementation points.
- **Limitations:** This startup audit did not yet verify modified behavior.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup-and-source-audit`

## EV-002 - Local Verifier Hardening

- **Date:** 2026-07-12
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** `src/power_ringmin/interval_verifier.py` now defines and checks `FIXED_ORDER_INTERVAL_BRACKET_ARTIFACT_TYPE`, requires local fixed-order interval bracket `artifact_type` to equal `fixed_order_interval_bracket`, and requires the `theta_interval_backend` key set and every key value to exactly match `oracle.backend_info.to_record()`.
- **Relevant output:** Added tests for local artifact-type tampering, backend metadata tampering across `backend`, `precision_digits`, `rounding_policy`, `outward_enclosure`, `certification_capable`, `tolerance_based`, and `guard_decimal`, and missing/extra backend metadata keys.
- **Relevant output:** Added aggregate small-n certificate tests proving embedded local artifact-type and backend policy tampering are rejected through the semantic validator.
- **Method or command:** `python -m py_compile src\power_ringmin\interval_verifier.py src\power_ringmin\verify_checked_artifacts.py src\power_ringmin\__init__.py tests\test_interval_verifier.py tests\test_small_n_interval_certificate.py tests\test_checked_artifact_schema_validation.py tests\test_verify_checked_artifacts.py`.
- **Relevant output:** Passed with no output.
- **Method or command:** `python -m pytest tests\test_interval_verifier.py`.
- **Relevant output:** `16 passed in 2.55s`.
- **Method or command:** `python -m pytest tests\test_small_n_interval_certificate.py`.
- **Relevant output:** `21 passed in 5.42s`.
- **Interpretation:** Local interval verifier hardening is covered by focused tests, and aggregate checked certificates re-run the hardened local verifier semantics.
- **Limitations:** These tests do not prove `mpmath.iv` itself correct.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verifier-hardening-and-tests`

## EV-003 - Schema And Checked-Artifact Verification

- **Date:** 2026-07-12
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `src/power_ringmin/verify_checked_artifacts.py` and registered `power-ringmin-verify-checked-artifacts` in `pyproject.toml`.
- **Relevant output:** Added `jsonschema>=4.22` to the `test` optional dependency, not to runtime dependencies.
- **Relevant output:** Added `tests/test_checked_artifact_schema_validation.py` to validate checked small-n certificate examples and finite-results summary examples against JSON Schema, and to demonstrate that schema validation is structural while semantic validators reject stale/tampered content.
- **Relevant output:** Added `tests/test_verify_checked_artifacts.py` covering discovery, checked-artifact verification, CLI success output, nonzero CLI failure on summary-source mismatch, and console script registration.
- **Method or command:** Initial `python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** Failed with `ModuleNotFoundError: No module named 'power_ringmin'` because the local checkout was not installed in that shell environment.
- **Interpretation:** This was an environment invocation issue, not a verifier failure. Pytest adds `src/` via `tests/conftest.py`, and CI installs the package before invoking the console script.
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Method or command:** `python -m pytest tests\test_checked_artifact_schema_validation.py tests\test_verify_checked_artifacts.py`.
- **Relevant output:** `9 passed in 5.66s`.
- **Method or command:** Final `python -m pytest tests\test_checked_artifact_schema_validation.py`; final `python -m pytest tests\test_verify_checked_artifacts.py`.
- **Relevant output:** Schema tests: `4 passed in 1.20s`; checked-artifact verifier tests: `5 passed in 4.44s`.
- **Interpretation:** The deterministic checked-artifact verification path validates structure, semantic reloads, embedded local interval brackets, and summary/source consistency without generating certificates.
- **Limitations:** Local command execution with `PYTHONPATH=src` is not the same as a hosted CI console-script run.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---checked-artifact-verification-and-ci`

## EV-004 - Documentation, CI, And Final Verification

- **Date:** 2026-07-12
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `docs/INTERVAL_BACKEND_TRUST.md` documenting the guarded `mpmath.iv` trust contract, guards, assumed outward-enclosure properties, tested coverage, unproved/audited gaps, classification implications, publication-grade trust requirements, possible future backends, and current work-count bounded generation meaning.
- **Relevant output:** Added `.github/workflows/verification.yml` for Python `3.11`, `3.12`, and `3.13`; the workflow installs `.[test]`, runs full pytest, runs `power-ringmin-verify-checked-artifacts`, runs schema validation tests, and checks diff/tracked-text whitespace.
- **Relevant output:** Updated `schemas/README.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Method or command:** `python -m pytest`.
- **Relevant output:** Final run: `107 passed in 33.53s`.
- **Method or command:** `python -c "from pathlib import Path; import yaml; payload=yaml.safe_load(Path('.github/workflows/verification.yml').read_text()); assert payload['jobs']['test']['strategy']['matrix']['python-version'] == ['3.11','3.12','3.13']; print('workflow yaml parsed')"`.
- **Relevant output:** `workflow yaml parsed`.
- **Method or command:** `rg -n "[ \t]+$" .github docs schemas src tests PROJECT_KNOWLEDGE.md CURRENT_STATUS.md pyproject.toml ops\TASK-20260712__verification_trust_layer_ci; if ($LASTEXITCODE -eq 1) { exit 0 }; exit $LASTEXITCODE`.
- **Relevant output:** No trailing-whitespace matches were found.
- **Method or command:** `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Relevant output:** Final status and diff were inspected; final `git diff --check` produced no output.
- **Interpretation:** Implementation, tests, documentation, and local CI workflow syntax sanity checks passed. The task is ready for manual review.
- **Limitations:** Hosted GitHub Actions did not run locally and is not claimed as successful. YAML parsing is not a complete GitHub Actions validation.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---backend-trust-documentation-and-handoff`
