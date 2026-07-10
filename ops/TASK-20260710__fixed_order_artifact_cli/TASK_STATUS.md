# TASK_STATUS - TASK-20260710__fixed_order_artifact_cli / Fixed-Order Artifact CLI

Last update: 2026-07-10

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Add a small command-line entry point for exporting v1 fixed-order artifacts from explicit order inputs.
- **Expected output:** Console script entry point, package CLI module, focused tests, verification evidence, and updated durable project memory.

## Scope

- **In scope:** CLI argument parsing for explicit radius or quadratic-index cyclic orders; artifact export through existing package APIs; focused tests; schema README note.
- **Out of scope:** global cyclic-order searches; batch export; certified-search frontier artifacts; new mathematical claims.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- `CURRENT_STATUS.md` proposed this exact task as the next atomic action.
- Existing package APIs include `export_full_result_artifact`, `export_highprec_artifact`, `dump_fixed_order_artifact`, `load_fixed_order_artifact`, float64 `full_radius`, and high-precision `full_radius_mp` / `recover_positions_mp`.

## Assumptions / Inferences

- A small first CLI should write one artifact for one explicit fixed order.
- Radius-order input should match existing verifier convention, while index-order input is useful because artifacts also record quadratic indices.
- The CLI should not claim global optimality; generated artifacts remain fixed-order numerical observations.

## Decisions And Rationale

- Add a dedicated module for the export command instead of introducing a broad subcommand framework.
- Register a `power-ringmin-export-fixed-order` console script in `pyproject.toml`.
- Support both `--order` radius values and `--index-order` quadratic indices as mutually exclusive explicit inputs.
- Provide a fast `float64` default backend and an optional `mpmath` backend with precision and local-bracket controls.
- Refuse to write an artifact if the exported radius is infeasible at the requested precision; this avoids recording a false feasible result when decimal serialization lands just below the STN tolerance.

## Plan And Expected Delta

- Add task dossier. COMPLETE.
- Add CLI module and console script entry point. COMPLETE.
- Add focused tests for radius-order and index-order export. COMPLETE.
- Document the CLI briefly in `schemas/README.md`. COMPLETE.
- Run focused and full test suites. COMPLETE.
- Update project memory and current status. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests/test_fixed_order_artifact_cli.py`; `python -m pytest tests/test_fixed_order_artifact_exporter_loader.py`; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Observed result:** Focused CLI tests passed: 4 passed. Exporter/loader tests passed: 3 passed. Full test suite passed: 18 passed. `git diff --check` produced no output.
- **Limitations:** Tests exercise finite explicit orders only and do not establish a global optimum, certified quadratic-radii result, or theorem. Console script registration is checked from `pyproject.toml`; the package was not installed into a separate environment.

## Blockers / Risks

- No current blocker. Residual risk is limited to untested larger orders or installed-environment packaging behavior.

## Next Atomic Action

- User reviews the fixed-order artifact CLI diff and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed 18 tests and `git diff --check` produced no output.
- **Files changed:** `pyproject.toml`, `schemas/README.md`, `src/power_ringmin/export_fixed_order_cli.py`, `tests/test_fixed_order_artifact_cli.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `src/power_ringmin/export_fixed_order_cli.py`, `tests/test_fixed_order_artifact_cli.py`.
