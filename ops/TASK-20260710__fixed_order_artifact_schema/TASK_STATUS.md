# TASK_STATUS - TASK-20260710__fixed_order_artifact_schema / Fixed-Order Artifact Schema

Last update: 2026-07-10

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Design the Power-Ringmin artifact schema for fixed-order numerical results, including radius sequence, precision/tolerance metadata, provenance, and evidence classification.
- **Expected output:** Versioned schema, documented design rules, checked example artifact, focused tests, and updated durable project memory.

## Scope

- **In scope:** Fixed-order numerical result artifact schema; explicit quadratic radius sequence and cyclic order fields; numerical precision and tolerance metadata; provenance; evidence classification; schema fixture tests.
- **Out of scope:** Global cyclic-order optimum schema; certified-search frontier schema; package CLI export implementation; importing additional upstream Ringmin result artifacts.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` was clean.
- Existing fixed-order code records orders as explicit radius tuples and verifies all-pairs STN feasibility.
- Existing standalone `verify.py` accepts a minimal fixed-order payload with an order, radius, and optional witness positions.

## Assumptions / Inferences

- The schema should be JSON because existing verifier payloads and future numerical artifacts naturally serialize to JSON.
- High-precision numerical values should be decimal strings rather than JSON floats.
- A fixed-order result artifact should not be interpreted as a global optimum claim unless evidence explicitly supports that stronger scope.

## Decisions And Rationale

- Add `schemas/fixed_order_result.schema.json` as Draft 2020-12 JSON Schema.
- Require both natural `instance.radius_sequence` and supplied `fixed_order.radius_order` to avoid implicit radius-sequence assumptions.
- Normalize evidence classifications to snake case while preserving the project classification set from `AGENTS.md`.
- Require provenance fields for repository state, software, source files, commands, and randomness.
- Add `examples/fixed_order_result_n3.json` as a schema fixture, classified as `numerical_observation`, not as a global optimum certificate.

## Plan And Expected Delta

- Add versioned fixed-order artifact schema.
- Add schema README explaining design rules and verifier compatibility.
- Add one checked n=3 example fixture.
- Add tests that inspect schema contract, enforce semantic consistency of the fixture, and verify the fixture with standalone verifier functions.
- Update project memory and final status after verification.

## Verification

- **Checks:** `python -m pytest tests/test_fixed_order_artifact_schema.py`; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Observed result:** Focused schema/example tests passed: 3 passed. Full test suite passed: 11 passed. `git diff --check` produced no output.
- **Limitations:** Tests validate the schema contract and example semantics, but they do not provide a full JSON Schema implementation or a global optimum certificate.

## Blockers / Risks

- No current blocker.
- The schema is a v1 design contract; future certified-search artifacts may need a separate frontier/global-result schema.

## Next Atomic Action

- User reviews the fixed-order artifact schema diff and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed 11 tests and `git diff --check` produced no output.
- **Files changed:** `schemas/fixed_order_result.schema.json`, `schemas/README.md`, `examples/fixed_order_result_n3.json`, `tests/test_fixed_order_artifact_schema.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `schemas/README.md`, `schemas/fixed_order_result.schema.json`, `tests/test_fixed_order_artifact_schema.py`.
