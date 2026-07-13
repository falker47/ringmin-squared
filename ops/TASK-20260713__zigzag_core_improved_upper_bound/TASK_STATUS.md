# TASK_STATUS - TASK-20260713__zigzag_core_improved_upper_bound / Zigzag Core Improved Upper Bound

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove and integrate the improved cubic upper bound obtained by assigning the core indices in zigzag order to regular-polygon directions.
- **Expected output:** one exact all-pairs proof, focused finite diagnostics, concise durable-memory updates, and no certificate generation or permutation search.

## Scope

- **In scope:** the general angular upper bound; the exact zigzag product-distance lemma; adjacent maximum, closing arc, and every `q>=2` pair; core feasibility at \(V_n\); reuse of the accepted insertion theorem; the improved limsup; focused diagnostics and documentation.
- **Out of scope:** an exact-leading-coefficient claim, optimal-order search, exhaustive permutation enumeration, certificate generation, new artifact infrastructure, commits, pushes, and upstream changes.

## Verified Facts

- Required startup files and relevant prior dossiers were read, and the initial Git working tree was clean.
- `patterns.zigzag(range(2, n + 1))` returns exactly the requested order \((n,2,n-1,3,\dots)\).
- The accepted radius-one theorem proves equality of full and core feasible-radius sets for every `n>=12`.
- Independent mathematical audits found no gap in the angular bound, combinatorial lemma, all-pairs construction, insertion step, or asymptotic conclusion.

## Assumptions / Inferences

- The angular formula and its strict upper bound are used only for \(R>0\).
- Finite integer and floating-point tests are diagnostics; the all-\(n\) result rests on the symbolic proof.

## Decisions And Rationale

- Preserve the prior \(U_n\) construction as a valid order-independent baseline and add \(V_n\) as a separate zigzag refinement.
- Reuse the existing `patterns.zigzag` helper and do not search over other permutations.
- Prove feasibility at the level of every unordered core pair before invoking feasible-radius-set equality; do not assume attainment.

## Plan And Expected Delta

- Extend `research/ALL_N_LOWER_BOUND.md` with the angular majorant, exact zigzag lemma, all-pairs construction, and improved limsup.
- Add exact finite combinatorial diagnostics and sampled numerical all-pairs geometry.
- Align `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `research/NEXT_RESEARCH_STEPS.md`.
- Run focused tests, the full suite, checked-artifact verification, and final diff/hygiene checks.

## Verification

- **Checks:** focused zigzag diagnostics; full pytest; checked-artifact semantic verifier; independent proof review; `git diff --check`; trailing-whitespace and final diff inspection.
- **Observed result:** focused tests passed 11/11; full suite passed 128/128; checked-artifact verification passed for 4 certificates, 76 local brackets, and the `n=3..6` summary; independent final proof review and diff hygiene passed.
- **Limitations:** diagnostics do not replace the exact proof; \(1/(2\pi)\) is only a limsup upper coefficient and is not claimed exact.

## Blockers / Risks

- None currently known.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused and full tests, checked-artifact verification, independent final proof review, and final diff hygiene pass.
- **Files changed:** theorem note, zigzag diagnostics, project brief, project knowledge, current status, research roadmap, and this task dossier.
- **Files to read first:** `research/ALL_N_LOWER_BOUND.md`, `tests/test_zigzag_core_upper_bound.py`, `EVIDENCE.md`.
