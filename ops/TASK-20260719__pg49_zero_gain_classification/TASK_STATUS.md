# TASK_STATUS - TASK-20260719 / PG49 Zero-Gain Classification

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** BLOCKED
- **Objective:** classify the left and right zero-gain equations for the
  descending-min PG49 order, including every plateau inequality and boundary;
  decide finite versus infinite if current mathematics permits, otherwise
  isolate the exact obstruction without extrapolating from finite data.
- **Expected output:** exact necessary-and-sufficient parametrizations,
  preserved left witness, explicit right-hole search, one bounded
  standard-library diagnostic, synchronized authoritative notes, and a
  rigorous statement of every residual claim.

## Scope

- **In scope:** `n=10m+3`, `m>=3`; the fixed descending-min order; equations
  `L_{m,j}=0` and `R_{m,j}=0`; `1<=j<m`; exact ceiling/plateau semantics;
  primitive Diophantine parameters; boundary columns; global cardinality of
  the zero triples; exact left and right witnesses.
- **Out of scope:** geometry, angular thresholds, global `K`-minimality,
  classification of minimizing orders, other PG49 assignments, or an
  all-`m` inference from a bounded computation.

## Verified Facts

- Each branch has a unique primitive square-factor parametrization by
  `(g,u,w)` with `g>0`, `gcd(u,w)=1`, and `u>w>0`.
- Integrality, domain, and the two half-open plateau ceilings reduce to
  explicit congruences and polynomial inequalities, separately for left and
  right holes.
- Every accepted primitive ratio `u/w` is a regular convergent of the same
  irreducible cubic root; each convergent supports only finitely many `g`.
- The known giant left witness is reconstructed exactly, including both
  ceiling residuals and the negative right gain.
- Right holes exist.  An exact primitive right witness with `g=19` is
  recorded with its full `(m,j,r)`, both ceiling residuals, and literal gains.

## Assumptions / Inferences

- Legendre's continued-fraction criterion is used after a direct uniform
  `<1/(2w^2)` proof; no numerical approximation is used in the theorem.
- The exact parametrization proves that global infinitude is equivalent to
  infinitely many congruence-filtered one-sided convergents entering the
  displayed finite `g` windows.
- No theorem available in the repository or identified primary literature
  decides that filtered subsequence for this cubic.  Finite versus infinite
  is therefore retained as an unresolved Diophantine claim.

## Decisions And Rationale

- Keep `L=0` and `R=0` separate after the shared square-factor lemma, because
  their residual constants and allowed ceiling boundaries differ.
- Retain the allowed left upper-ceiling equality and prove both right
  ceiling equalities impossible.
- Use the sole diagnostic only for falsification and initial checks.  Its
  discovery of right holes corrects the prior absence of a right witness but
  does not prove an infinite family.
- Mark the global cardinality claim unresolved rather than infer a theorem
  from 200 decimal digits of bounded convergent data.

## Plan And Expected Delta

- Complete STRICT startup and inspect KPGMIN/PG49 sources. COMPLETE.
- Derive both primitive parametrizations and exact plateaux. COMPLETE.
- Run the sole bounded diagnostic and audit discovered witnesses. COMPLETE.
- Write the fixed-order theorem and synchronize pertinent sources. COMPLETE.
- Run repository verification and independent mathematical review. COMPLETE.
- Inspect the complete final diff and whitespace hygiene. COMPLETE.

## Verification

- **Checks:** sole diagnostic, exact substitution of both witnesses, source
  and tag audit, scoped static checks, complete tests, checked artifacts, and
  final Git diff checks.
- **Observed result:** the diagnostic currently passes; it reports no literal
  zero through `m=500`, then exactly validates 56 left and eight right
  parameter triples among its bounded proposed convergents.
- **Limitations:** decimal arithmetic proposes bounded convergents but proves
  no absence claim.  Every reported positive witness is rechecked with exact
  integers.  Full pytest passes 283 tests; the focused schema suite passes 4
  tests; checked-artifact verification confirms 4 certificates and 76 local
  brackets; scoped Ruff, the KPGZERO source audit, complete diff inspection,
  and whitespace hygiene pass.

## Blockers / Risks

- The requested global finite/infinite dichotomy is blocked by the exact
  congruence-filtered, one-sided continued-fraction condition for a cubic
  irrational.  Neither branch currently has a proved infinite family or a
  proved finiteness obstruction.
- Residual risk is human review of large exact formulas and integers.

## Next Atomic Action

- Inspect the complete diff and hand the mathematically blocked cardinality
  claim to the user for review.

## Handoff

- **Last verified result:** exact branch parametrizations and two-sided
  plateau residuals, plus exact nonempty left and right branches.
- **Files changed:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`, subsection
  `Exact Diophantine classification of the zero-gain set`, then
  `EVIDENCE.md`.
