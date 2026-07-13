# TASK_STATUS - TASK-20260713__regular_core_cubic_upper_bound / Regular-Core Cubic Upper Bound

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove a constructive cubic upper bound for Power-Ringmin using a regular core configuration.
- **Expected output:** one self-contained exact proof, focused diagnostic tests, concise durable-memory updates, and no certificates or infrastructure.

## Scope

- **In scope:** fixed-radius worst-pair monotonicity; the closed formula for \(U_n\); explicit all-pairs regular-core feasibility; reuse of the accepted radius-one insertion theorem; asymptotic consequences; focused diagnostics; documentation and memory updates.
- **Out of scope:** exact leading-constant claims, optimization of the regular construction, certificates, exhaustive order enumeration, new infrastructure, commits, pushes, and upstream changes.

## Verified Facts

- Startup files and relevant prior task memory were read, and the initial Git working tree was clean.
- The accepted radius-one theorem proves equality of full and core feasible-radius sets for every `n>=12`.
- Independent mathematical review supports the worst-pair reduction, formula derivation, all-pairs argument, and infimum handling.

## Assumptions / Inferences

- The construction and angular monotonicity use `R>0`.
- Finite floating-point tests are diagnostics only; the all-`n` conclusion rests on the symbolic proof.

## Decisions And Rationale

- Extend `research/ALL_N_LOWER_BOUND.md` so the all-`n` lower bound, insertion theorem, and upper construction remain in one authoritative theorem note.
- Check every unordered regular-polygon vertex pair through its smaller circular separation.
- Use equality of feasible-radius sets rather than assuming an optimum is attained.

## Plan And Expected Delta

- Record the regular-core theorem and proof in the existing all-`n` note.
- Add focused diagnostics for the formula, worst pair, and finite all-pairs feasibility.
- Align the project brief, project knowledge, current status, and research roadmap by concise reference.
- Run focused tests, full pytest, checked-artifact verification, and final diff checks.

## Verification

- **Checks:** focused regular-core diagnostics; full pytest; checked-artifact semantic verification; independent final proof and documentation reviews; `git diff --check`; changed-file trailing-whitespace scan; final Git status and diff inspection.
- **Observed result:** focused tests passed 3/3; full suite passed 125/125; checked-artifact verification passed for 4 certificates, 76 local brackets, and the `n=3..6` summary; independent review found no remaining actionable issue; diff hygiene passed.
- **Limitations:** diagnostics do not replace the proof; the construction leaves a coefficient gap and does not prove an exact leading constant.

## Blockers / Risks

- None currently known.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused and full tests, checked-artifact verification, independent proof/documentation reviews, and diff hygiene passed.
- **Files changed:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_regular_core_upper_bound.py`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, and this task dossier.
- **Files to read first:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_regular_core_upper_bound.py`, `EVIDENCE.md`.
