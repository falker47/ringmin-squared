# TASK_STATUS - TASK-20260713__exact_tail_incompatibility / Exact Tail Incompatibility

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** characterize exactly the minimum number of product-
  incompatible adjacencies in the induced threshold tail and invert the
  resulting distance-two packing condition.
- **Delivered output:** an exact all-`n` theorem for `eta_n(T)`, explicit
  cardinality and equality boundaries, exact finite inversion, asymptotic
  coefficient decision, bounded independent tail verification, and aligned
  durable memory.

## Scope

- **In scope:** the nested-neighborhood graph on `U_T`; cardinalities zero,
  one, and two; strict threshold equalities; the finite half-integer
  inversion; the existing `n=3..11` core regression; clarification of the
  formerly omitted `k=n` event; source, tests, proof, and durable memory.
- **Out of scope:** core-order enumeration beyond `n=11`; new artifacts,
  certificates, schemas, CLIs, modules, or infrastructure; a formula for
  exact `B_n` or `W_n`; geometric-optimum claims; Git writes or upstream
  changes.

## Verified Facts

- The compatible graph on the consecutive tail is a split threshold graph:
  the lower block is a clique, the upper block is independent, and the cross
  neighborhoods are nested prefixes.
- Its exact cyclic incompatibility is
  `eta_n(T)=max(0,2*v-u+delta_n(T))`, where the correction is zero or one and
  all zero-, one-, and two-vertex cases are included.
- The exact packing condition is `n-1>=2*u+eta_n(T)`. Its finite inversion
  changes only `Q_9` in the `n=3..11` row, from the clique value `30` to
  `63/2`.
- The refined inversion still satisfies
  `Q_n=((36-16*sqrt(2))/49)*n^2+O(n)`, so this subproblem does not improve the
  earlier leading coefficient.
- Independent mathematical, implementation, and documentation reviews report
  no remaining blocker.

## Assumptions / Inferences

- Bounded tail-cycle enumeration is verification evidence only; the all-`n`
  result is established symbolically.
- The asymptotic coefficient obtained from this necessary condition is not
  the actual asymptotic coefficient of `B_n` unless a separate matching
  theorem is proved.

## Decisions And Rationale

- Refined the existing two-threshold support in place; added no new command,
  artifact, schema, module, or file format.
- Included `k=n` in the finite event set so its exhaustivity is literal, and
  documented why its former omission did not change the clique-only minimum.
- Limited the independent permutation enumerator to tail cardinality seven
  and preserved the existing core-order enumeration boundary `n<=11`.

## Plan And Expected Delta

- Complete exact graph derivation and boundary audit. COMPLETE.
- Implement exact `eta_n(T)` support and bounded independent tests. COMPLETE.
- Update the proof and stable project memory. COMPLETE.
- Run focused, integrated, full, artifact, review, and diff verification.
  COMPLETE.

## Verification

- **Checks:** Python compilation; focused and integrated pytest; independent
  tail enumeration; exact finite and asymptotic formula diagnostics; full
  pytest; checked-artifact semantic verification; three independent reviews;
  exact path scope; strict UTF-8; trailing whitespace; equation-tag
  uniqueness; complete diff inspection; `git diff --check`; final Git status.
- **Observed result:** compilation passed; focused tests passed `20/20`;
  integrated tests passed `35/35`; all 299 independent tail states matched;
  992 inversion and 956 asymptotic-witness diagnostics passed; full pytest
  passed `148/148`; the artifact verifier accepted 4 certificates, 76 local
  brackets, and the `n=3..6` summary; all independent reviews passed; the 10
  intended paths passed final hygiene and diff review.
- **Limitations:** no core enumeration beyond `n=11`; finite diagnostics do
  not replace the all-`n` proof; hosted CI for the current `HEAD` was not
  independently inspected.

## Blockers / Risks

- No blocker.
- Residual risk is interpretive: the result is exact for one tail-cycle
  subproblem but neither computes `B_n` nor proves its asymptotic limit.

## Next Atomic Action

- User review and manual commit decision. Do not begin the proposed STN
  documentation task in this chat.

## Handoff

- **Last verified result:** full tests, artifact verification, three
  independent reviews, and final diff hygiene pass.
- **Files changed:** `src/power_ringmin/product_distance.py`,
  `tests/test_product_distance.py`, `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, and this three-file task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`,
  `tests/test_product_distance.py`, and this dossier.

