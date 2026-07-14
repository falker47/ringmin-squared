# TASK_STATUS - TASK-20260714__residue_two_saturation_obstruction / Residue-Two Saturation Obstruction

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove the sharper distance-two lower obstruction
  \(B_{12}\ge60\) and, for \(n=5k+2\), \(k\ge3\),
  \(B_n\ge J_n=d_n(d_n-2)/2\), then transfer it to \(W_n\) and update the
  proved bound widths to the existing uniform threshold \(T_n\).
- **Expected output:** a symbolic saturation proof with every strict boundary,
  floor, cardinality, half-integer, and distinct-terminal point explicit;
  independent exact tests at `n=12,17,22` and over a broader falsification
  range; minimal proof, state, roadmap, and task-memory updates.

## Scope

- **In scope:** the residue class `n == 2 (mod 5)`, the interval
  `H_n <= T < J_n`, saturation of terminal-high incidences, the separate
  `n=12` arithmetic, the consequence `W_n >= B_n`, and widths to the already
  proved upper threshold `T_n`.
- **Out of scope:** a matching upper construction, exact values of `B_n` or
  `W_n`, cyclic-order enumeration beyond `n=11`, geometry, artifacts, schemas,
  CLIs, Git writes, or upstream changes.

## Verified Facts

- Required startup files, relevant predecessor memory, the primary proof
  note, exact source/tests, roadmap, and a clean initial Git tree were
  inspected.
- Three independent audits agree on the symbolic proof, strict endpoints,
  exact low and terminal sets, saturated incidence injection, residual
  component, distinct terminal positions, separate `n=12` argument, and
  consequences for `W_n` and the widths.
- The proof establishes
  \[
  B_{12}\ge60,
  \qquad
  B_n\ge J_n={d_n(d_n-2)\over2}
  \quad(n\equiv2\pmod5,\ n\ge17).
  \]
- Independent tests cover all 40 half-integer states in `[H_n,J_n)` at
  `n=12,17,22`, the exact boundary `J_n`, and all 999 values `2<=k<=1000`
  in the broad symbolic endpoint sweep.
- Targeted, focused, integrated, full, artifact, compile, changed-line style,
  documentation, path-scope, and diff-hygiene checks pass as recorded below.

## Assumptions / Inferences

- Finite exact tests are falsification and regression support only; the
  all-`n` conclusion comes from the symbolic proof.
- Widths refer to intervals between proved lower and upper bounds, not to
  optimum gaps or claims of attained equality.

## Decisions And Rationale

- Keep the exact definition and closed form of `H_n` unchanged. The new
  argument is a structural strengthening that rules out every threshold in
  `[H_n,J_n)` specifically in residue two.
- Reuse the independent threshold constructor already present in the test
  module; add no production API.
- Preserve the canonical order-enumeration boundary `n<=11`; all larger
  checks evaluate exact formulas and threshold sets only.

## Plan And Expected Delta

- Complete independent symbolic audits. COMPLETE.
- Add the saturation proof to the product-distance proof note. COMPLETE.
- Add minimal independent arithmetic/structure tests. COMPLETE.
- Update stable project state, current status, and roadmap. COMPLETE.
- Run focused, integrated, full, artifact, and final diff verification.
  COMPLETE.

## Verification

- **Checks:** targeted/focused/integrated/full pytest; compile; checked-artifact
  semantic verification; Ruff pre-existing-finding audit; three independent final
  reviews; strict UTF-8, trailing whitespace, equation-tag, display-delimiter,
  path-scope, complete diff, and `git diff --check` inspection.
- **Observed result:** targeted `4/4`; focused `35/35`; integrated `50/50`;
  full unsandboxed `163/163`; 4 certificates, 76 local brackets, and summary
  values `3,4,5,6` accepted; compile PASS; Ruff with the sole pre-existing
  `F841` ignored PASS; 9 intended paths; strict UTF-8 and trailing whitespace
  PASS; 130 unique proof tags; 243 balanced display pairs; final diff check
  PASS.
- **Retained failed checks:** the first focused run had 3 test-body harness
  failures when entering the threshold scan because `range` received integral
  `Fraction` endpoints; preliminary formula assertions ran, but no
  per-threshold assertion ran in those rows. The corrected harness then passed
  `35/35`. Sandboxed full pytest reported `132 passed, 31 errors`, all from
  denied temporary-directory creation; the identical unsandboxed suite passed
  `163/163`. Unmodified Ruff reports only pre-existing `F841` at unchanged
  line 566.
- **Limitations:** hosted GitHub Actions for the current worktree was not
  inspected; no canonical cyclic-order enumeration was extended beyond
  `n=11`.

## Blockers / Risks

- No current blocker.
- Exact `B_n` and `W_n` values remain unresolved in residue two; the new
  lower endpoint need not be attained or sharp.
- No matching construction or geometric implication was investigated.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the symbolic proof, independent threshold tests,
  all local suites, artifact verifier, independent audits, and final hygiene
  pass; the bounded task is ready for manual review.
- **Files changed:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `tests/test_product_distance.py`, `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, and this three-file
  task dossier. No production source file changed.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `tests/test_product_distance.py`, and this dossier.
