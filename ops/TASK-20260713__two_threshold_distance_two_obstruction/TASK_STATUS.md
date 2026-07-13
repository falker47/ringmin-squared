# TASK_STATUS - TASK-20260713__two_threshold_distance_two_obstruction / Two-Threshold Distance-Two Obstruction

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** develop a quantitative all-`n` lower obstruction for
  `B_n=W_n^(<=2)` from cyclic packing at exact product thresholds `T` and
  `2T`.
- **Expected output:** a self-contained theorem with integer thresholds,
  degenerate tails, exact finite obstruction, explicit quadratic bound,
  asymptotic consequence, comparison table, minimal exact support, and tests.

## Scope

- **In scope:** induced cyclic gaps on threshold tails; exact marked-word
  adjacency count; empty/singleton cases; finite half-integer inversion;
  comparison with `A_n`, `L_n`, and the existing `n=3..11` table; exact source
  support and focused tests; proof and durable-memory updates.
- **Out of scope:** cyclic-order enumeration beyond `n=11`; formulas for exact
  `B_n` or `W_n`; new artifacts, schemas, certificates, CLIs, or
  infrastructure; geometric optimum claims; Git writes or upstream changes.

## Verified Facts

- The initial Git tree was clean and all required startup and relevant
  product-distance/lower-bound sources were inspected.
- The candidate lemma is correct for `u>=2`; the same numerical inequality
  extends separately to the empty and singleton tails.
- Exact `Fraction` support computes the finite obstruction from the finite set
  of threshold events; focused product-distance tests pass.

## Assumptions / Inferences

- The full-distance tail obstruction `L_n<=W_n` is not assumed to lower-bound
  `B_n`; the new proof uses only distances one and two.
- Bounded exact enumeration is regression evidence only and is not used for
  the all-`n` theorem.

## Decisions And Rationale

- Define threshold starts before intersecting with `{2,...,n}` so singleton
  and empty tails remain distinct.
- Package the obstruction as the least admissible nonnegative half-integer
  `Q_n`, using only the finite equality events where a tail changes.
- Add two functions and one data class to the existing product-distance module;
  add no new module or command surface.

## Plan And Expected Delta

- Formalize and prove the cyclic gap lemma. COMPLETE.
- Implement exact tail data and finite obstruction with focused tests. COMPLETE.
- Update primary proof, essential memory, and exact bounded comparison. COMPLETE.
- Run integrated/full verification and final diff review. COMPLETE.

## Verification

- **Checks:** Python compilation; focused and integrated pytest; exact
  `n=9..1000` formula diagnostics; full pytest; checked-artifact semantic
  verification; exact scope, strict UTF-8, corrected trailing-whitespace,
  equation-tag, complete diff, and `git diff --check` review.
- **Observed result:** compilation passed; focused tests passed `18/18`;
  integrated tests passed `33/33`; 992 formula checks passed; full pytest
  passed `146/146`; artifact verification accepted 4 certificates and 76
  local brackets; all 10 intended paths and 51 equation tags pass final
  hygiene.
- **Limitations:** tests support but do not replace the symbolic all-`n` proof;
  no enumeration beyond `n=11` is permitted.

## Blockers / Risks

- No blocker.
- Main risks are off-by-one errors at strict product equalities, treating
  vacuous tails as nondegenerate gap cycles, or transferring `L_n` to `B_n`.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused/integrated/full tests, formula diagnostics,
  artifact verification, and final scope/encoding/whitespace/diff review pass.
- **Files changed:** product-distance source/tests, primary research proof,
  project memory/roadmap, and this dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`, `tests/test_product_distance.py`,
  and `EVIDENCE.md`.
