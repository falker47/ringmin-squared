# TASK_STATUS - TASK-20260710__batch_standalone_verifier_check / Batch Standalone-Verifier Check

Last update: 2026-07-10

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Add a batch standalone-verifier check for a directory of fixed-order artifacts.
- **Expected output:** Batch verifier CLI entry point, focused tests, schema documentation update, verification evidence, and updated durable project memory.

## Scope

- **In scope:** Directory scan for v1 fixed-order artifacts; per-artifact derivation of standalone `verify.py` payloads; subprocess invocation of root `verify.py`; pass/fail batch summary; focused tests; documentation.
- **Out of scope:** Changing the v1 artifact schema; changing standalone verifier mathematical logic; global cyclic-order search; global optimum certificates.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- `CURRENT_STATUS.md` proposed this exact task as the next atomic action.
- Existing `verify.py` accepts minimal fixed-order payloads containing `ordering`, claimed radius, and optional witness positions.
- Existing `FixedOrderArtifact.to_verifier_payload()` derives the minimal standalone-verifier payload from one v1 artifact.
- Existing batch exporter writes one v1 fixed-order artifact per explicit order into an output directory.

## Assumptions / Inferences

- The batch check should keep `verify.py` standalone by invoking it as a subprocess rather than moving verifier logic into the package.
- The batch check should validate each v1 artifact before deriving the standalone-verifier payload.
- JSON files in the target directory are the natural default artifact candidates.

## Decisions And Rationale

- Add a dedicated `power-ringmin-verify-fixed-order-artifacts` entry point rather than extending the exporter; checking artifacts is a separate evidence step.
- Keep root `verify.py` standalone by invoking it as a subprocess from the batch CLI.
- Validate each v1 artifact with package helpers before deriving the minimal standalone-verifier payload.
- Use JSON files in the target directory as default artifact candidates, with optional `--pattern` and `--recursive` controls.
- Reuse an artifact's recorded `local_radius_bracket.eta_decimal` by default when present, while allowing `--no-artifact-eta` and a global `--eta` override.
- Add optional `verify.py --stn-tol` and pass-through support in the batch CLI so tolerance-labeled float64 numerical artifacts can be checked explicitly without weakening the standalone verifier default.

## Plan And Expected Delta

- Create task dossier and active status. COMPLETE.
- Implement batch artifact verifier CLI and console script metadata. COMPLETE.
- Add focused tests and schema docs. COMPLETE.
- Run focused and full verification. COMPLETE.
- Update project memory and final task status. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests/test_verify_fixed_order_artifacts_cli.py tests/test_crosscheck_and_verifier.py`; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Observed result:** Final focused verifier tests passed with 8 tests. Full repository test suite passed after implementation and memory updates, with final run reporting 28 passed. `git diff --check` produced no output.
- **Limitations:** Tests cover finite small explicit orders only. Passing tests do not establish a global optimum, certified quadratic-radii result, or theorem. Console script registration is checked from `pyproject.toml`; the package was not installed into a separate environment.

## Blockers / Risks

- No current blocker.
- Residual risk is limited to larger artifact directories, installed-environment console-script behavior, and user choice of tolerance for float64 numerical artifacts.

## Next Atomic Action

- User reviews the batch standalone-verifier artifact check diff and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed 28 tests and `git diff --check` produced no output.
- **Files changed:** `pyproject.toml`, `schemas/README.md`, `verify.py`, `src/power_ringmin/verify_fixed_order_artifacts_cli.py`, `tests/test_verify_fixed_order_artifacts_cli.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `src/power_ringmin/verify_fixed_order_artifacts_cli.py`, `tests/test_verify_fixed_order_artifacts_cli.py`, `verify.py`.
