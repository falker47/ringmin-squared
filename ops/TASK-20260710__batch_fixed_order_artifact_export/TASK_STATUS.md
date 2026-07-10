# TASK_STATUS - TASK-20260710__batch_fixed_order_artifact_export / Batch Fixed-Order Artifact Export

Last update: 2026-07-10

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Add batch fixed-order artifact export from a JSON list of explicit orders.
- **Expected output:** Batch CLI entry point, package implementation, focused tests, schema docs, verification evidence, and updated durable project memory.

## Scope

- **In scope:** JSON list/object input for explicit radius or index orders; one v1 fixed-order artifact per order; shared backend options with the single-order exporter; focused tests; documentation.
- **Out of scope:** global cyclic-order search; generated pattern batches; new artifact schema; global optimum certificates; mathematical claims beyond fixed-order numerical observations.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- `CURRENT_STATUS.md` proposed this exact task as the next atomic action.
- Existing `src/power_ringmin/export_fixed_order_cli.py` exposes `export_artifact_for_order` for one explicit fixed-order artifact.
- Existing `src/power_ringmin/patterns.py` includes `load_json_orders`, accepting either a top-level JSON list or an object with an `orders` list.

## Assumptions / Inferences

- The batch exporter should preserve the existing v1 one-order artifact schema and write multiple files instead of creating a new aggregate result schema.
- A top-level JSON list or `{ "orders": [...] }` should be treated as radius orders by default.
- An explicit CLI mode should support index-order JSON lists where entries are permutations of `1..n`.

## Decisions And Rationale

- Add a dedicated `power-ringmin-export-fixed-order-batch` entry point rather than adding batch mode to the single-order CLI; this keeps single-order argument validation simple.
- Preserve the existing v1 fixed-order artifact schema and write one artifact file per input order.
- Accept either a top-level JSON list or an object with an `orders` list; additionally accept `index_orders` when `--order-kind index` is selected.
- Generate deterministic names of the form `fixed_order_####_n#.json`, with an optional `--filename-prefix`.
- Refuse to overwrite generated artifact files unless `--overwrite` is passed.
- Reuse the single-order `export_artifact_for_order` implementation so backend behavior and feasibility guards stay aligned.

## Plan And Expected Delta

- Create task dossier and active status. COMPLETE.
- Implement batch JSON-order export CLI and console script metadata. COMPLETE.
- Add focused tests and schema docs. COMPLETE.
- Run focused and full verification. COMPLETE.
- Update project memory and final task status. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests/test_fixed_order_artifact_batch_cli.py tests/test_fixed_order_artifact_cli.py`; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Observed result:** Focused batch/single CLI tests passed: 9 passed. Full repository test suite passed twice, with final run reporting 23 passed. `git diff --check` produced no output.
- **Limitations:** Tests cover finite small explicit orders only. Passing tests do not establish a global optimum, certified quadratic-radii result, or theorem. Console script registration is checked from `pyproject.toml`; the package was not installed into a separate environment.

## Blockers / Risks

- No current blocker. Residual risk is limited to untested larger batches, installed-environment packaging behavior, and possible future need for a manifest format.

## Next Atomic Action

- User reviews the batch fixed-order artifact export diff and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed 23 tests and `git diff --check` produced no output.
- **Files changed:** `pyproject.toml`, `schemas/README.md`, `src/power_ringmin/export_fixed_order_cli.py`, `src/power_ringmin/export_fixed_order_batch_cli.py`, `tests/test_fixed_order_artifact_batch_cli.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `src/power_ringmin/export_fixed_order_batch_cli.py`, `tests/test_fixed_order_artifact_batch_cli.py`.
