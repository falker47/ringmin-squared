# TASK_STATUS - TASK-20260712__subset_pairing_extremal_bound / Subset Pairing Extremal Bound

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** characterize exactly the best lower bound obtainable from the induced-subset, duplicated-multiset pairing, and \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\) relaxation.
- **Expected output:** self-contained extremal theorem, integer-arithmetic tests, durable memory updates, and no finite table, upper-bound construction, LP work, new certificates, or `n=7` work.

## Scope

- **In scope:** explicit formula for \(A(S)\), fixed-cardinality tail optimality, exact discrete maximizer characterization for \(P_{m,n}\), documentation updates, and focused tests.
- **Out of scope:** diagnostic `n=3..6` table, upper-bound construction, leading-order LP, new certificates, and `n=7`.

## Verified Facts

- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` was clean.
- `research/ALL_N_LOWER_BOUND.md` now records the explicit \(A(S)\) formula,
  tail optimality at fixed cardinality, exact \(\rho_n\)-based discrete
  maximizer characterization, and method-specific optimality of
  \(2(\sqrt2-1)/(3\pi)\).
- `tests/test_induced_subset_lower_bound.py` now uses integer arithmetic to
  enumerate small-`n` subsets and characterize discrete maximizers.

## Assumptions / Inferences

- The task affects mathematical documentation, tests, and durable memory only.

## Decisions And Rationale

- Use integer arithmetic in tests for subset enumeration and discrete maximizer decisions to avoid floating-point maximizer selection.
- Treat \(2(\sqrt2-1)/(3\pi)\) as optimal only inside the named relaxation.

## Plan And Expected Delta

- Update `research/ALL_N_LOWER_BOUND.md` with the extremal theorem.
- Strengthen `tests/test_induced_subset_lower_bound.py`.
- Align `research/FINITE_RESULTS.md`, `docs/INTERVAL_BACKEND_TRUST.md`, `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md`.

## Verification

- **Checks:** `python -m pytest tests\test_induced_subset_lower_bound.py`; `python -m pytest`; `python -m power_ringmin.verify_checked_artifacts`; `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Observed result:** focused tests passed 7/7; full suite passed 117/117; first checked-artifact command failed because `power_ringmin` was not importable without `PYTHONPATH`; rerun with `PYTHONPATH=src` passed for 4 checked certificates, 76 local brackets, and the `n=3..6` summary.
- **Limitations:** tests are finite diagnostics and do not replace the all-`n` proof; checked-artifact verification remains under the documented guarded `mpmath.iv` backend contract.

## Blockers / Risks

- None currently known.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** full pytest and checked-artifact semantic verification passed.
- **Files changed:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_induced_subset_lower_bound.py`, `research/FINITE_RESULTS.md`, `docs/INTERVAL_BACKEND_TRUST.md`, `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_induced_subset_lower_bound.py`, `EVIDENCE.md`.
