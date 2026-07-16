# TASK_STATUS - TASK-20260716__one_triple_reversal_obstruction / One-Triple Reversal Obstruction

Last update: 2026-07-16

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** analyze one explicit parametric perturbation of the
  `eight_twenty_fifths_order` symbolic construction and prove either a lower
  asymptotic product-distance coefficient or an exact family obstruction.
- **Expected output:** a precise perturbation family, symbolic full-distance
  score split by distance and cyclic closure, an exact theorem, small
  reproducible checks, synchronized authoritative memory, and unchanged
  enumeration limits.

## Scope

- **In scope:** the residue-three subsequence `n=10*m+3`, reversal of one
  triple path, exact adjacency/distance-two/distance-three/long-distance and
  closing analysis, the surrogate conclusion, and a separately labelled
  geometric upper-bound consequence.
- **Out of scope:** a second perturbation family; cyclic-order enumeration;
  production generator changes; geometric optimality; checked artifacts,
  schemas, interval backends, certificates, or Git writes.

## Verified Facts

- The required startup files, prior construction dossier, proof, source, and
  tests were read; the initial worktree was clean.
- The selected family is defined for `m>=3`, `0<=s<=m` by reversing only the
  endpoints of the triple `P_s` in the symbolic `n=10*m+3` branch.
- The symbolic derivation gives `M_1=T`, the exact piecewise `M_2`,
  `M_3=(5*m+2)*(9*m+5)/3`, the exact long-distance maximum, exact closing
  maxima, and the full formula recorded in (PT13).
- The persistent adjacent pair prevents every member from improving below
  `T`; `s=0` is strictly worse by `(d-1)/2`.

## Assumptions / Inferences

- None. The theorem uses the already proved symbolic construction and exact
  integer inequalities only.

## Decisions And Rationale

- Restrict to one infinite residue/parity subsequence so the parameter family
  and closing cut have a single literal formula with no exceptional rows.
- Keep the perturbation test-local and dossier-local; no public production API
  is required for this negative family result.
- Treat exact `W` first. State the regular-direction geometric consequence
  only afterward and only as a redundant upper bound.

## Plan And Expected Delta

- Record the exact proof and independent diagnostic. COMPLETE.
- Add small exact test-local controls without enumerating orders. COMPLETE.
- Run focused, full, artifact, static, and document verification. COMPLETE.
- Synchronize authoritative memory only after verification. COMPLETE.

## Verification

- **Checks:** standalone diagnostic; targeted and complete product-distance
  pytest; complete repository pytest; checked-artifact semantic verifier;
  schema-selection pytest; Ruff; equation-tag, display-math, UTF-8,
  changed-path, protected-source, complete-diff, and Git hygiene; three
  independent final read-only audits.
- **Observed result:** six diagnostic rows pass; targeted tests pass 6/6;
  product-distance tests pass 49/49; all 283 repository tests pass outside
  the sandbox; checked artifacts accept 4 certificates and 76 local brackets;
  schema selection passes 4/4; Ruff and all final document/diff checks pass.
  The first sandboxed full suite retained 31 temporary-directory setup errors
  and no failed test body; the required outside-sandbox rerun passed.
- **Limitations:** bounded computation will corroborate but not prove the
  all-parameter theorem.

## Blockers / Risks

- No current blocker.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact theorem, six-row independent diagnostic,
  focused/full tests, checked artifacts, static checks, three final audits,
  and complete diff/hygiene review pass.
- **Files changed:** primary product-distance proof, one focused test module,
  project brief, durable knowledge, current status, roadmap, and this
  four-file task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `tests/test_product_distance.py`, `CURRENT_STATUS.md`, and this dossier.
