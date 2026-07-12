# TASK_STATUS - TASK-20260712__all_n_lower_bound / All-n lower bound

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Prove and integrate an all-\(n\) mathematical lower bound for Power-Ringmin using an adjacent product-sum lemma, add direct finite enumeration tests for the lemma, and update durable project memory.
- **Expected output:** Self-contained research note, non-tautological canonical-order tests for `n=3..9`, updated project memory and roadmap, existing suite verified green, task dossier set to `READY_FOR_REVIEW`.

## Scope

- **In scope:** all-\(n\) lower-bound proof, adjacent product-sum lemma, geometry-to-adjacent-gap argument, test coverage for canonical cyclic orders, durable memory updates.
- **Out of scope:** new finite certificate generation, new artifact contracts, `n=7` exhaustive certificate work, matching upper-bound construction.

## Verified Facts

- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read on 2026-07-12.
- Initial `git status --short` was clean.
- `src/power_ringmin/search_small_n.py` provides canonical cyclic index-order enumeration modulo rotation and reflection.
- `research/ALL_N_LOWER_BOUND.md` records the all-\(n\) lower-bound proof and classifies the result as `EXACT THEOREM`.
- `tests/test_search_small_n.py` enumerates all canonical cyclic orders for `n=3..9` and directly checks the adjacent product-sum lower bound.

## Assumptions / Inferences

- The mathematical note can live under `research/` because it is project-wide research documentation rather than an artifact schema or checked finite certificate.
- The requested result is classified as `EXACT THEOREM` after checking the proof domain, the geometry-to-gap step, the angular inequality, and the fact that non-adjacent constraints are not needed for this lower-bound relaxation.

## Decisions And Rationale

- Add tests to the existing small-`n` search test module so the lemma is checked against the repository's canonical order convention.
- Do not generate or modify checked finite certificate artifacts.

## Plan And Expected Delta

- Add `research/ALL_N_LOWER_BOUND.md`.
- Add direct canonical-order product-sum tests for `n=3..9`.
- Update `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `research/NEXT_RESEARCH_STEPS.md`.
- Run focused and full verification, inspect `git status`, `git diff`, and `git diff --check`.

## Verification

- **Checks:** `python -m pytest tests\test_search_small_n.py`; `python -m pytest`; `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`; `git status --short`; `git diff`; `git diff --check`.
- **Observed result:** focused tests passed; full suite first had one transient provenance mismatch, the isolated failing test then passed, full suite rerun passed; checked-artifact verifier passed; final diff was inspected; `git diff --check` passed.
- **Limitations:** finite enumeration tests support the combinatorial lemma implementation but are not the proof of the all-\(n\) theorem. Hosted CI was not queried.

## Blockers / Risks

- Matching upper-bound work remains open and requires all-pairs non-adjacent control.
- The first full-suite run had a transient failure in `tests/test_finite_results.py::test_deterministic_generation`; the test passed in isolation and the full suite passed on rerun.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused tests, full test suite rerun, checked-artifact verification, and `git diff --check` passed.
- **Files changed:** `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/ALL_N_LOWER_BOUND.md`, `research/NEXT_RESEARCH_STEPS.md`, `tests/test_search_small_n.py`, and this task dossier.
- **Files to read first:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_search_small_n.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`.
