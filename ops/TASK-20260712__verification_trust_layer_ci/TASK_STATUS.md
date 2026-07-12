# TASK_STATUS - TASK-20260712__verification_trust_layer_ci / Verification Trust Layer And CI

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Harden checked-artifact verifier trust semantics, add structural JSON Schema validation tests, add deterministic checked-artifact verification, add CI, and document the interval-backend trust contract without generating `n=7`.
- **Expected output:** Local verifier hardening, focused tampering and precision tests, schema validation tests, checked-artifact verification command/test path, GitHub Actions workflow, interval backend trust note, durable memory updates, and verification evidence.

## Scope

- **In scope:** Local fixed-order interval bracket verifier semantics; checked `examples/small_n_interval_certificate_n3.json` through `examples/small_n_interval_certificate_n6.json`; `examples/finite_results_summary_n3_n6.json`; JSON Schema validation as structural tests; CI workflow aligned with `pyproject.toml`; interval-backend trust documentation.
- **Out of scope:** Generating `n=7`; changing finite result classifications; proving the guarded `mpmath.iv` backend contract; publishing hosted CI results before GitHub runs them; Git staging, commits, pushes, rebases, merges, resets, or remote changes.

## Verified Facts

- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- The prior structural analysis task was recorded as `READY_FOR_REVIEW`, and the current tree is clean.
- Checked source certificates currently exist for `n=3`, `n=4`, `n=5`, and `n=6`.
- The current local interval verifier checks local schema version and selected backend metadata but did not yet check local `artifact_type` or exact `rounding_policy`.

## Assumptions / Inferences

- This task may add test/dev dependencies and CI metadata, but should avoid new runtime dependencies unless semantic runtime validation requires them.
- JSON Schema validation should remain a structural guard; Python semantic validators remain authoritative for interval verification and stale-artifact rejection.
- "Bounded" generation currently means work-count bounded by canonical-order and local-attempt ceilings, not wall-clock bounded.

## Decisions And Rationale

- Use `STRICT` mode because changes affect certification trust and reproducible checked-artifact validation.
- Add a separate checked-artifact verification command so CI and local review can exercise the full checked artifact surface deterministically without generating new certificates.
- Record the interval backend trust contract in a focused document without upgrading evidence classifications.

## Plan And Expected Delta

- Read verifier, artifact, schema, and test code. COMPLETE.
- Create this task dossier. COMPLETE.
- Harden local verifier metadata checks and tests. COMPLETE.
- Add structural JSON Schema validation tests using a test dependency. COMPLETE.
- Add deterministic checked-artifact verifier command/test path. COMPLETE.
- Add GitHub Actions workflow. COMPLETE.
- Add interval backend trust note and boundedness documentation if justified. COMPLETE.
- Run focused tests, full tests, checked-artifact verification, schema validation, workflow validation where possible, status/diff inspection, whitespace checks, and `git diff --check`. COMPLETE.
- Update project durable memory and set `READY_FOR_REVIEW`. COMPLETE.

## Verification

- **Checks:** Python compile checks; focused local verifier tests; focused aggregate certificate tests; checked-artifact schema tests; checked-artifact verifier tests; direct checked-artifact verification command; full pytest; workflow YAML parse; trailing-whitespace scan; Git status/diff inspection; `git diff --check`.
- **Observed result:** `python -m pytest` passed with `107 passed`; `python -m power_ringmin.verify_checked_artifacts` with `PYTHONPATH=src` verified 4 checked certificates, 76 embedded local brackets, and summary `n=3,4,5,6`; schema tests passed with `4 passed`; workflow YAML parsed; trailing-whitespace scan found no matches; final `git diff --check` produced no output.
- **Limitations:** Hosted GitHub Actions results cannot be claimed from local checks. Local workflow validation was YAML parsing/source inspection only, not an `actionlint` or hosted-run result.

## Blockers / Risks

- No current blocker.
- Residual risk: the guarded `mpmath.iv` backend remains trusted under a documented contract rather than formally proved or independently audited.

## Next Atomic Action

- Harden local verifier checks and add focused tests.

## Handoff

- **Last verified result:** `python -m pytest` passed with `107 passed in 33.53s`; checked-artifact verification passed; schema tests passed; workflow YAML parsed; trailing-whitespace scan and `git diff --check` passed.
- **Files changed:** `src/power_ringmin/interval_verifier.py`, `src/power_ringmin/verify_checked_artifacts.py`, `tests/test_interval_verifier.py`, `tests/test_small_n_interval_certificate.py`, `tests/test_checked_artifact_schema_validation.py`, `tests/test_verify_checked_artifacts.py`, `pyproject.toml`, `.github/workflows/verification.yml`, `docs/INTERVAL_BACKEND_TRUST.md`, `schemas/README.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `docs/INTERVAL_BACKEND_TRUST.md`, `src/power_ringmin/interval_verifier.py`, `src/power_ringmin/verify_checked_artifacts.py`, `.github/workflows/verification.yml`, and `tests/test_checked_artifact_schema_validation.py`.
