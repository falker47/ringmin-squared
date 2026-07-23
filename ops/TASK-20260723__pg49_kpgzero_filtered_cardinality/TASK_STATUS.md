# TASK_STATUS - TASK-20260723 / PG49 KPGZERO Filtered Cardinality

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** formalize the exact KPGZERO filtered cubic-convergent
  cardinality on the PG49 support, determine what PG49-supported families can
  or cannot prove about it, and preserve the separation among support \(W\),
  induced value \(K\), and geometry.
- **Expected output:** exact cardinality fibres and equivalences; a proved
  support-only and fixed-direction no-go; a small independent discriminating
  diagnostic; synchronized proof, stable memory, roadmap, status, and dossier.

## Scope

- **In scope:** the \(n=10m+3\), \(m\ge3\), PG49 board; descending-min
  bijections; KPGZERO-1--KPGZERO-41; filtered convergent/scale pairs; exact
  per-row and global cardinality; comparison with another supported
  bijection on the same board.
- **Out of scope:** changing production, public tests, schemas, or artifacts;
  factorial enumeration; a claim that PG49 support determines \(K\);
  angular thresholds, geometric feasibility, or a global geometric optimum.

## Verified Facts

- The filtered fibre \(\mathcal C_m\) is bijective with
  \(\mathcal Z_m\), and the descending-min argmax count is
  \(2^{|\mathcal C_m|}\).
- The canonical marked supported family is infinite exactly when the
  filtered convergent/scale set and the numerical zero-label union are
  infinite.
- Each primitive convergent direction admits only finitely many scales; no
  finite set of directions can generate an infinite filtered family.
- On one exact PG49 board, descending-min has multiple induced-\(K\)
  maximizers while PG49-star has one, although both have \(W=T=W_n\).
- The affine right conic/support ray is infinite but fails both literal
  plateau residuals at every index.
- These results use no geometry and do not decide KPGZERO-24.

## Assumptions / Inferences

- No finite convergent sweep is used to infer global finiteness or
  infinitude.
- The exact PG49, KPGMIN, KPGZERO, and KPGSTAR theorems are retained inputs.

## Decisions And Rationale

- Treat the literal KPGZERO plateau, congruence, side, domain, and scale
  conditions as indivisible parts of the filter.
- State a no-go only for what is proved: PG49 supportedness does not
  determine induced-\(K\) maximizer cardinality, and a fixed finite set of
  primitive directions cannot generate an infinite filtered family. Do not
  relabel the residual arithmetic dichotomy as solved.
- Use same-board and conic/support false positives so the diagnostic tests
  genuine distinctions rather than another bounded sweep.

## Plan And Expected Delta

- Complete STRICT startup and inspect the exact predecessor sources. COMPLETE.
- Formalize filtered fibres and supported-family cardinality. COMPLETE.
- Prove the support-only and fixed-direction no-go. COMPLETE.
- Add and run the independent exact diagnostic. COMPLETE.
- Synchronize durable sources and run final verification. COMPLETE.

## Verification

- **Checks:** exact diagnostic; Ruff; full pytest; checked-artifact schema
  test; checked-artifact verifier; independent mathematical and
  synchronization audits; Git status/diff/diff-check.
- **Observed result:** exact diagnostic PASS; Ruff PASS; sequential full
  suite 283 passed; schema test 4 passed; four checked certificates and 76
  local brackets verified; final diff hygiene PASS.
- **Limitations:** finite diagnostic instances corroborate the symbolic
  theorem but cannot decide the remaining infinite convergent subsequence.

## Blockers / Risks

- No workflow blocker.
- Residual scientific uncertainty: the absolute finite/infinite dichotomy in
  KPGZERO-24 is not decided by PG49 and requires additional number theory.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** KPGZERO-31--KPGZERO-41 give the exact filtered
  cardinality and the support-only/fixed-direction no-go; KPGZERO-24 remains
  unresolved.
- **Files changed:** `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`,
  `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, and this four-file task dossier.
- **Files to read first:** the KPGZERO subsection of
  `research/FIXED_ORDER_CYCLE_RATIO.md`, then `EVIDENCE.md`.
