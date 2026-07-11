# TASK_STATUS - TASK-20260711__small_n_highprec_rechecks / Small-n High-Precision Rechecks

Last update: 2026-07-11

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Add high-precision incumbent/tie rechecks to small-n search outputs while preserving numerical-observation classification.
- **Expected output:** Updated search implementation, tests, smoke artifact with recheck payload, verification evidence, and durable status updates.

## Scope

- **In scope:** mpmath rechecks for the float64 incumbent and float64 tie set; JSON artifact fields and semantic validation for the recheck block; CLI flags for recheck digits and optional skip; tests proving classification remains `numerical_observation`; n=3 smoke artifact.
- **Out of scope:** High-precision interval bounds for every order; certified global optimum artifacts; pruned/frontier search; Ringmin upstream changes; Git staging or commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- The prior design dossier explicitly called for high-precision rechecks of the incumbent and tie candidates while reserving certified global claims for future interval evidence.
- `src/power_ringmin/highprec.py` already provides `full_radius_mp`, `feasibility_margin_mp`, and `is_feasible_mp`.

## Assumptions / Inferences

- "Incumbent/tie rechecks" means rechecking the float64 winner and any records grouped into the float64 tie set, not recomputing every canonical order in high precision.
- Recheck output should be serialized inside the small-n search artifact rather than creating separate fixed-order artifacts in this task.
- Because no interval lower bounds are computed for every nonwinner order, the artifact must remain a finite numerical observation.

## Decisions And Rationale

- Default small-n search now runs an `mpmath` recheck for the float64 incumbent/tie set at 80 digits.
- CLI users may set `--highprec-recheck-digits` or use `--no-highprec-recheck` for speed-sensitive exploratory runs.
- The artifact includes both search-method recheck metadata and a top-level `high_precision_recheck` payload, and validation requires those sections to agree.
- When a recheck payload is present, validation requires its records to cover exactly the float64 tie set.
- The evidence claim scope remains `finite_exhaustive_float64_order_search`, and the artifact continues rejecting `computer_certified_result`.

## Plan And Expected Delta

- Add high-precision recheck dataclass, result fields, JSON serialization, and validation. COMPLETE.
- Add CLI flags and provenance/evidence text for the recheck path. COMPLETE.
- Extend focused tests to assert the recheck payload, classification boundary, and validator consistency. COMPLETE.
- Run focused/full tests and a source-tree CLI smoke run. COMPLETE.
- Update durable memory and inspect the final diff. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests\test_search_small_n.py`; `python -m pytest`; source-tree CLI smoke run with `PYTHONPATH=src`; generated artifact inspection; `git status --short`; `git diff --stat`; `git diff --check`; trailing-whitespace scan.
- **Observed result:** Focused tests passed with `7 passed in 0.54s`; full suite passed with `37 passed in 5.83s`; CLI smoke wrote `small_n_search_n3_highprec_recheck_smoke.json` with `highprec_rechecks=1` and `evidence.classification = numerical_observation`.
- **Limitations:** Verification covers finite tests and one n=3 smoke artifact. It does not provide high-precision interval lower bounds for all canonical orders and does not certify global optimality.

## Blockers / Risks

- No current blocker.
- Residual risk: high-precision rechecks can expose tighter numerical values for selected orders, but they still cannot prove a global optimum without interval verification across the order space.

## Next Atomic Action

- Design the high-precision interval verifier semantics needed to upgrade a finite small-n result from numerical observation to a possible `computer_certified_result`.

## Handoff

- **Last verified result:** `python -m pytest` passed 37 tests in 5.83s; source-tree CLI smoke for n=3 wrote a high-precision recheck artifact; final diff checks passed.
- **Files changed:** `src/power_ringmin/search_small_n.py`, `tests/test_search_small_n.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier including `small_n_search_n3_highprec_recheck_smoke.json`.
- **Files to read first:** `src/power_ringmin/search_small_n.py`, `tests/test_search_small_n.py`, this task dossier.
