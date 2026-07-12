# TASK_STATUS - TASK-20260712__cross_platform_finite_hash_ci / Cross-Platform Finite Summary Hashes

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Fix hosted CI stale-summary failures caused by platform-dependent source certificate line endings in finite-results `content_sha256` values, without changing certificate mathematics or evidence classifications.
- **Expected output:** Normalized source-content digest in `finite_results.py`, tests for LF/CRLF/content-change behavior and summary validation across line-ending-only source differences, schema documentation, regenerated checked finite-results summary, GitHub Actions extras installation update, verification evidence, and durable memory updates.

## Scope

- **In scope:** Finite-results source certificate digest semantics; summary generation/validation; finite-results schema documentation; focused tests; checked summary regeneration; CI dependency installation for the claimed full suite.
- **Out of scope:** Certificate mathematics, interval-verifier semantics, candidate-set results, source certificate artifacts, critical-structure artifacts, and evidence classifications.

## Verified Facts

- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- `src/power_ringmin/finite_results.py` previously computed `content_sha256` with a raw-byte `_sha256_file`.
- `.github/workflows/verification.yml` previously installed only `.[test]` before running the full suite.

## Assumptions / Inferences

- This task uses `STRICT` mode because it affects checked-artifact reproducibility and hosted CI verification.
- The `content_sha256` field should remain a SHA-256 hex digest but its input bytes should be the source certificate bytes after newline normalization only.

## Plan And Expected Delta

- Create task dossier and record scope. COMPLETE.
- Implement normalized source-content digest in `finite_results.py`. COMPLETE.
- Add digest and line-ending validation tests. COMPLETE.
- Update schema documentation and CI extras. COMPLETE.
- Regenerate checked finite-results summary. COMPLETE.
- Run full verification and checked-artifact verification. COMPLETE.
- Inspect final status/diff and set task to READY_FOR_REVIEW. COMPLETE.

## Verification

- **Focused finite-results tests before regeneration:** `python -m pytest tests\test_finite_results.py` failed with `1 failed, 15 passed`; failure was expected because the checked summary still contained old raw-byte source hashes.
- **Initial regeneration attempt:** `python -m power_ringmin.finite_results --created-at-utc 2026-07-12T00:00:00Z --output examples\finite_results_summary_n3_n6.json` failed because the package was not installed on `sys.path` for direct module execution.
- **Regeneration:** `$env:PYTHONPATH='src'; python -m power_ringmin.finite_results --created-at-utc 2026-07-12T00:00:00Z --output examples/finite_results_summary_n3_n6.json` passed and regenerated the checked summary with normalized digests. Python emitted a `runpy` warning caused by package `__init__` importing `power_ringmin.finite_results` before module execution; the command exited successfully.
- **Focused finite-results tests after regeneration:** `python -m pytest tests\test_finite_results.py` passed with `16 passed`.
- **Full suite:** final `python -m pytest` passed with `109 passed`.
- **Checked-artifact verification:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts` passed with `certificates=4`, `local_brackets=76`, and `summary_n_values=3,4,5,6`.
- **Final hygiene:** `git diff --check` produced no output.

## Blockers / Risks

- No current blocker.
- Residual risk: hosted GitHub Actions itself is not observed locally; local verification covered the repository command paths.

## Next Atomic Action

- User reviews the digest, documentation, regenerated summary, tests, and workflow update, then decides whether to commit manually.
