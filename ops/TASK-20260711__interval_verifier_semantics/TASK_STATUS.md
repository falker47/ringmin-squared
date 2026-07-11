# TASK_STATUS - TASK-20260711__interval_verifier_semantics / Interval Verifier Semantics

Last update: 2026-07-11

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Design the high-precision interval verifier semantics needed to upgrade finite small-n output from numerical observation to possible `computer_certified_result`.
- **Expected output:** Durable verifier semantics design, task memory, verification evidence, and updated global status.

## Scope

- **In scope:** Fixed-order interval endpoint semantics; STN edge/cycle semantics; feasible witness semantics; global finite small-n aggregation semantics; artifact/verifier boundaries; future implementation acceptance criteria.
- **Out of scope:** Implementing interval arithmetic; creating a JSON schema; generating or certifying a small-n result; proving all mathematical obligations; importing upstream certified-search code; Git staging or commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- Current small-n search artifacts are classified as `numerical_observation`.
- Current high-precision rechecks cover the float64 incumbent/tie set only and do not compute certified interval lower bounds for every order.
- Existing fixed-order feasibility code uses all-pairs STN constraints.

## Assumptions / Inferences

- The requested task is a design task, not an implementation task.
- Certification semantics should be stricter than current `mpmath` tolerance-based verification.
- A future global small-n certificate should require one verified interval bracket per canonical order.

## Decisions And Rationale

- Use `STRICT` mode because the task defines semantics for future certification claims.
- Require outward interval enclosures and strict sign checks for `computer_certified_result` evidence.
- Require feasible upper endpoints to be verified by explicit all-pairs witness slacks using upper theta bounds.
- Require infeasible lower endpoints to be verified by explicit negative cycles in a relaxed STN using lower theta bounds.
- Keep global finite certification separate from fixed-order numerical artifacts and small-n float64 search artifacts.

## Plan And Expected Delta

- Inspect startup files, prior small-n dossiers, current high-precision verifier code, current small-n search code, and schema docs. COMPLETE.
- Write a durable interval verifier semantics design. COMPLETE.
- Update global durable status and knowledge pointer. COMPLETE.
- Run documentation-relevant verification and final diff checks. COMPLETE.

## Verification

- **Checks:** Source/document inspection; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`; trailing-whitespace scan on changed docs and new dossier.
- **Observed result:** Full test suite passed with `37 passed in 8.07s`. The tracked diff is scoped to `PROJECT_KNOWLEDGE.md` and `CURRENT_STATUS.md`; `git status --short` also shows the new task dossier. `git diff --check` produced no output, and the trailing-whitespace scan found no matches.
- **Limitations:** This task verifies the design document and unchanged existing tests only. It does not implement interval arithmetic, prove the listed proof obligations, create a schema, generate a certificate, or certify a quadratic-radii optimum.

## Blockers / Risks

- No current blocker.
- Residual risk: the design depends on proof obligations and an interval backend that have not yet been implemented or certified.

## Next Atomic Action

- Implement the local fixed-order interval bracket verifier semantics before attempting a full global small-n certificate.

## Handoff

- **Last verified result:** `python -m pytest` passed 37 tests; final diff checks passed.
- **Files changed:** `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `ops/TASK-20260711__interval_verifier_semantics/DESIGN.md`, `src/power_ringmin/highprec.py`, `verify.py`, `src/power_ringmin/search_small_n.py`.
