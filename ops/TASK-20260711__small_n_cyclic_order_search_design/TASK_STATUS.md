# TASK_STATUS - TASK-20260711__small_n_cyclic_order_search_design / Small-n Cyclic-Order Search Design

Last update: 2026-07-11

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Design a radius-sequence-aware small-n cyclic-order search for quadratic radii.
- **Expected output:** Durable search design, task memory, verification evidence, and updated global status.

## Scope

- **In scope:** Search design; radius/index representation; canonical cyclic-order enumeration; exhaustive small-n baseline; future artifact/verifier/test boundaries.
- **Out of scope:** Implementing `search.py`; running new numerical searches; creating global optimum artifacts; proving lower-bound theorems; importing the upstream certified-search pipeline.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- Existing fixed-order evaluation is radius-sequence-aware: `full_radius(order)` accepts explicit radius orders and checks all-pairs STN feasibility.
- Existing fixed-order artifact and batch export code records explicit quadratic radius sequence and explicit cyclic order metadata.
- Upstream Ringmin search code has generic value-based entry points but also original-radii defaults and lower-bound choices that must not be mechanically ported.

## Assumptions / Inferences

- The requested "Design" task should produce a durable design document, not a production search implementation.
- For the first implementation, exhaustive float64 search over canonical index orders is the safest baseline because it avoids unproven pruning.
- Global `computer_certified_result` claims require more than evaluating every order once in float64; they require independent regeneration and interval evidence or equivalent certified lower bounds.

## Decisions And Rationale

- Keep index labels and radius values separate so the order-space claim is tied to the explicit quadratic sequence.
- Canonicalize cyclic orders by fixing index `n` first and requiring the second index to be smaller than the last, removing rotation and reflection duplicates.
- Use existing fixed-order STN machinery as the evaluator, and create a separate future search artifact schema for global-order claims.
- Treat pruned lower-bound search as a later design/proof task, not part of the first baseline implementation.

## Plan And Expected Delta

- Inspect startup files, relevant task memory, source modules, schema docs, and upstream search scaffold. COMPLETE.
- Write a durable design document for a radius-sequence-aware small-n search. COMPLETE.
- Update global durable status and knowledge pointer. COMPLETE.
- Run documentation-relevant verification and final diff checks. COMPLETE.

## Verification

- **Checks:** Source/document inspection; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`; trailing-whitespace scan on changed docs and new dossier.
- **Observed result:** Full test suite passed with `30 passed in 5.02s`. Final diff is scoped to `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this new task dossier. `git diff --check` produced no output, and the trailing-whitespace scan found no matches.
- **Limitations:** This task verifies the design document and unchanged existing tests only. It does not implement the search, run a new search, certify a global optimum, or prove a lower-bound theorem.

## Blockers / Risks

- No current blocker.
- Residual risk: the future certified-search design still needs a high-precision interval verifier and a reviewed proof for any pruning lower bounds.

## Next Atomic Action

- Implement canonical index-order enumeration and exhaustive float64 small-n search with tests, keeping output classified as numerical observation.

## Handoff

- **Last verified result:** `python -m pytest` passed 30 tests; `git diff --check` produced no output; trailing-whitespace scan found no matches.
- **Files changed:** `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `ops/TASK-20260711__small_n_cyclic_order_search_design/DESIGN.md`, `src/power_ringmin/evaluator.py`, `src/power_ringmin/geometry.py`, `schemas/README.md`.
