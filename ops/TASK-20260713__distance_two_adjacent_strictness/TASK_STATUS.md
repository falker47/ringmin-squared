# TASK_STATUS - TASK-20260713__distance_two_adjacent_strictness / Distance-Two Adjacent Strictness

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** decide exactly whether positional-distance-two constraints make the adjacent product-distance relaxation strict for every `n>=9`.
- **Expected output:** parity-specific equality characterization for `A_n`, an all-`n` theorem for `B_n=W_n^(<=2)`, only the exact support/tests used by the proof, and aligned durable memory.

## Scope

- **In scope:** high/low equality cases, forced high-high edges, products between the two high neighbors of each low, exact `n=12` exceptional lemma, bounded `n=3..11` regression, source/tests/research memory.
- **Out of scope:** cyclic-order enumeration beyond `n=11`; a formula for `B_n`; distances at least three; new certificates, artifacts, schemas, or CLIs; geometric-optimum claims; Git writes or upstream changes.

## Verified Facts

- Startup files, relevant prior dossiers, source, tests, patterns, and the research note were inspected; the initial Git tree was clean.
- The parity-specific equality structure reduces every `A_n`-optimal cycle to one alternating high/low path after removing the forced high-high edge or two-edge segment.
- A terminal-high incidence obstruction proves distance-two strictness except for `n=12`; a separate exact degree argument covers `n=12`.
- Direct witnesses give `B_n=A_n` for `3<=n<=8`; the all-`n` proof gives `B_n>A_n` for every `n>=9` and therefore `W_n>A_n` in the same range.

## Assumptions / Inferences

- The all-`n` theorem is mathematical and does not follow from the bounded regression table.
- Strictness of `B_n>A_n` does not determine the value of the full surrogate `W_n` or whether distances at least three are essential.

## Decisions And Rationale

- Add one structural classifier for adjacent equality cases; retain the existing bounded truncated enumerator unchanged.
- Use no cyclic-order enumeration beyond `n=11`; test the all-`n` proof through exact lemma arithmetic and bounded regression only.

## Plan And Expected Delta

- Complete startup and derivation. COMPLETE.
- Add minimal structural support and exact focused tests. COMPLETE.
- Update the proof note and durable memory. COMPLETE.
- Run focused/full verification and final diff review. COMPLETE.

## Verification

- **Checks:** Python compilation; bounded structural regression; focused and integrated pytest; exact formula diagnostics; full pytest; checked-artifact semantic verification; exact path scope, strict UTF-8, trailing whitespace, equation-tag uniqueness, complete diff, and `git diff --check` review.
- **Observed result:** compilation passed; focused tests passed `16/16` and `31/31`; direct structure/incidence probes passed; full pytest passed `144/144`; artifact verification accepted 4 certificates and 76 local brackets; all 10 intended paths passed final hygiene and diff review.
- **Limitations:** local Python is 3.14.3; parameter sweeps are diagnostic only; no formula for `B_n` or `W_n` and no beyond-`n=11` equality with the full surrogate is claimed.

## Blockers / Risks

- No blocker.
- Main risk is confusing the all-`n` proof with finite enumeration or inferring a full-surrogate formula.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** full verification and final scope/UTF-8/whitespace/equation-tag/diff review pass.
- **Files changed:** product-distance source/tests, research note/roadmap, project memory/status, and this dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`, `src/power_ringmin/product_distance.py`, `tests/test_product_distance.py`.
