# TASK_STATUS - TASK-20260711__small_n_float64_search / Small-n Float64 Search

Last update: 2026-07-11

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Implement canonical index-order enumeration and exhaustive float64 small-n search with tests.
- **Expected output:** Search implementation, CLI, tests, numerical-observation output contract, verification evidence, and updated durable status.

## Scope

- **In scope:** Canonical quadratic index-order enumeration modulo rotation/reflection; exhaustive float64 search over canonical orders; JSON summary output classified as finite numerical observation; focused tests; direct tiny CLI smoke run.
- **Out of scope:** Certified global optimum artifacts; high-precision interval verification for every order; pruned/frontier search; Ringmin upstream code changes; Git staging or commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- The prior design dossier `ops/TASK-20260711__small_n_cyclic_order_search_design/` specified canonical index orders and an exhaustive float64 baseline as the next implementation task.

## Assumptions / Inferences

- The requested implementation should produce deterministic finite numerical observations, not a new certified global optimum claim.
- Direct CLI output should be a small review artifact under this task dossier rather than a production result directory.

## Decisions And Rationale

- Keep the search layer separate from fixed-order artifacts because it owns the finite order-space enumeration statement.
- Require search artifacts to use evidence classification `numerical_observation` and to disclaim certified global optimality.
- Keep only the float64 backend in the first CLI; high-precision certification remains a later task.

## Plan And Expected Delta

- Add `src/power_ringmin/search_small_n.py` with canonical enumeration, canonicalization, index/radius conversion, exhaustive float64 search, JSON artifact helpers, and CLI. COMPLETE.
- Register the `power-ringmin-search-small-n` console script. COMPLETE.
- Add tests for enumeration, canonicalization, search behavior, artifact validation, and CLI output. COMPLETE.
- Run focused and full verification, plus a direct source-tree CLI smoke run. COMPLETE.
- Update durable project knowledge and current status. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests\test_search_small_n.py`; `python -m pytest`; source-tree CLI smoke run for n=3 with `PYTHONPATH=src`; artifact inspection; `git status --short`; `git diff --stat`; `git diff --check`; trailing-whitespace scan.
- **Observed result:** Focused tests passed with `7 passed in 0.37s`; final full suite passed with `37 passed in 6.71s`; CLI smoke wrote `small_n_search_n3_smoke.json` with `evidence.classification = numerical_observation`; `git diff --check` produced no output; trailing-whitespace scan found no matches.
- **Limitations:** Verification covers finite tests and one n=3 smoke artifact. It does not certify a global optimum or provide high-precision intervals for every order.

## Blockers / Risks

- No current blocker.
- Residual risk: float64 exhaustive search is not a certified optimum proof and may need high-precision interval checks in a later task.

## Next Atomic Action

- User reviews the implementation diff and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed 37 tests in 6.71s; source-tree CLI smoke for n=3 passed after setting `PYTHONPATH=src`; final `git diff --check` and trailing-whitespace scan passed.
- **Files changed:** `src/power_ringmin/search_small_n.py`, `tests/test_search_small_n.py`, `pyproject.toml`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier including `small_n_search_n3_smoke.json`.
- **Files to read first:** `src/power_ringmin/search_small_n.py`, `tests/test_search_small_n.py`, this task dossier.
