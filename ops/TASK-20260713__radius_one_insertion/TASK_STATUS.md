# TASK_STATUS - TASK-20260713__radius_one_insertion / Radius-One Insertion

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove or disprove an exact radius-one insertion lemma and derive an explicit eventual equality threshold for the full and reduced-core infima.
- **Expected output:** self-contained exact theorem or formalized gap, focused diagnostic tests, aligned research notes and durable memory, and no new certificates or exhaustive order enumeration.

## Scope

- **In scope:** forbidden-arc geometry; all new pairwise constraints; rigorous angular majorants; application of the existing configuration-level induced-subset lower bound; infimum semantics; focused tests; documentation and memory updates.
- **Out of scope:** new finite certificates, new exhaustive order enumeration, exact-optimum claims for checked small cases, `n=7` generation, commits, pushes, and upstream changes.

## Verified Facts

- Startup files were read and the initial Git working tree was clean.
- The relevant prior theorem is the arbitrary-subset, configuration-level result in `research/ALL_N_LOWER_BOUND.md`; its scalar full-optimum corollary alone cannot be transferred to the core.
- Independent mathematical audits and a final proof-diff review support an exact insertion lemma and the sufficient threshold `N=12`.

## Assumptions / Inferences

- No existence of a minimizing core or full configuration is assumed.
- Finite floating-point tests are diagnostics only; the proof uses exact inequalities.

## Decisions And Rationale

- Update the existing all-`n` note instead of creating a second theory note.
- Prove equality of feasible-radius sets before taking infima.
- Treat `N=12` as a sufficient explicit threshold, not a minimal threshold.

## Plan And Expected Delta

- Record the forbidden-arc lemma and exact threshold proof in `research/ALL_N_LOWER_BOUND.md`.
- Add focused diagnostic tests for the angular majorant, exact `n=12,13` bounds, and the uniform parity inequality.
- Align finite-results context, roadmap, project knowledge, current status, and project brief.
- Run focused tests, full pytest, checked-artifact semantic verification, and final diff checks.

## Verification

- **Checks:** focused insertion and induced-lower-bound tests; full pytest; checked-artifact semantic verifier; independent proof-diff review; `git diff --check`; final Git status and diff inspection.
- **Observed result:** focused tests passed 12/12; full suite passed 122/122; checked-artifact verifier passed with 4 certificates, 76 local brackets, and the `n=3..6` summary; proof review found no actionable issue; diff hygiene passed.
- **Limitations:** tests are diagnostics and do not replace the exact proof; the proof is not a minimal-threshold result and makes no claim for `n<=11`; checked finite artifacts retain the documented guarded `mpmath.iv` limitation.

## Blockers / Risks

- None currently known.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused and full tests, checked-artifact verification, proof review, and diff checks passed.
- **Files changed:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_radius_one_insertion.py`, `research/FINITE_RESULTS.md`, `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_radius_one_insertion.py`, `EVIDENCE.md`.
