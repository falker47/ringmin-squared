# TASK_STATUS - TASK-20260712__induced_subset_lower_bound / Induced-subset lower bound

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Strengthen the all-\(n\) lower bound by applying the cyclic pairing lemma to induced subsets of peripheral circles, determine whether this disproves the \(n^3/(6\pi)\) asymptotic conjecture and \(n^3/(6\pi)+O(n^2)\) target, add finite diagnostic tests, and update durable project memory.
- **Expected output:** Self-contained proof or explicit gap, finite tests for the induced-subset arithmetic and pairing checks, coherent documentation reclassification, full verification, checked-artifact verification, diff checks, and dossier status `READY_FOR_REVIEW`.

## Scope

- **In scope:** induced cyclic order proof for subsets with at least three indices, specialization to consecutive subsets \(\{m,\dots,n\}\), formula and asymptotic optimization for \(P_{m,n}\), active search for proof gaps, finite diagnostic tests, durable memory updates.
- **Out of scope:** upper-bound constructions, leading-order LP work, new checked certificate generation, new exact asymptotic constant proposal.

## Verified Facts

- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read on 2026-07-12.
- Initial `git status --short` was clean.
- `research/ALL_N_LOWER_BOUND.md` previously recorded only the full-index adjacent-product lower bound and \(\liminf 6\pi R_2^*(n)/n^3\ge 1\).
- `tests/test_search_small_n.py` already contains finite canonical-order checks for the older full-cycle product lower bound.
- `research/ALL_N_LOWER_BOUND.md` now records the induced-subset theorem, the consecutive-subset formula \(P_{m,n}\), and the rounded asymptotic optimization.
- The former \(R_2^*(n)=n^3/(6\pi)(1+o(1))\) conjectural target and \(R_2^*(n)=n^3/(6\pi)+O(n^2)\) target are now classified as `DISPROVED CLAIM`.

## Assumptions / Inferences

- The finite tests are diagnostics and regression checks only; the all-\(n\) statement rests on the written proof.

## Decisions And Rationale

- Use a new STRICT dossier because the task changes the classification of the main conjectural target.
- Keep proof documentation in the existing all-\(n\) lower-bound note rather than creating a duplicate research note.
- Add a focused test module for the induced-subset arithmetic and finite pairing checks.
- Do not propose a new exact asymptotic constant; record only the proved lower obstruction and the disproof of the former targets.

## Plan And Expected Delta

- Extended `research/ALL_N_LOWER_BOUND.md`.
- Added finite direct tests for \(P_{m,n}\), the discrete maximum over \(m\), and nonconsecutive subset pairing bounds.
- Updated `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `research/NEXT_RESEARCH_STEPS.md`.
- Ran focused tests, full suite, checked-artifact verifier, `git status --short`, `git diff --stat`, full tracked diff inspection, untracked new-file inspection, and `git diff --check`.

## Verification

- **Checks:** `python -m pytest tests\test_induced_subset_lower_bound.py`; `python -m pytest`; `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`; `git status --short`; `git diff`; `git diff --check`; direct inspection of untracked new files.
- **Observed result:** focused tests passed (`4 passed`); full suite passed (`114 passed`); checked-artifact verifier passed (`certificates=4 local_brackets=76 summary_n_values=3,4,5,6`); tracked diff was inspected; untracked new files were inspected; `git diff --check` passed.
- **Limitations:** finite tests are not the proof; hosted CI was not queried; plain `git diff` does not show untracked files until the user stages them.

## Blockers / Risks

- No blocker remains.
- Residual risk is mathematical review risk in the induced cyclic order/gap argument, pairing relaxation, and rounded asymptotic optimization; these are explicitly audited in `research/ALL_N_LOWER_BOUND.md`.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused tests, full suite, checked-artifact verifier, tracked diff inspection, untracked new-file inspection, and `git diff --check` passed.
- **Files changed:** `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/ALL_N_LOWER_BOUND.md`, `research/NEXT_RESEARCH_STEPS.md`, `tests/test_induced_subset_lower_bound.py`, and this task dossier.
- **Files to read first:** `research/ALL_N_LOWER_BOUND.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`.
