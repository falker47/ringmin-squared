# TASK_STATUS - TASK-20260715__one_wrap_cycle_ratio_saturation / One-Wrap Cycle-Ratio Saturation

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** define the one-wrap score \(\Lambda^{(1)}(\sigma)\), prove
  its exact induced-subset formulation, decide whether it equals the full
  cyclic ratio for every complete order, and independently verify the result
  on all canonical orders for `n=3..8` without enlarging production
  enumeration.
- **Expected output:** an all-order proof or the smallest exact
  counterexample; a Karp-independent exact test oracle over the existing
  bounded domain; synchronized proof, roadmap, tests, durable memory, and
  task evidence.

## Scope

- **In scope:** complete orders of `{1,...,n}`, `n>=3`; nonempty directed
  closed walks and vertex-simple cycles; one-wrap cycles; cyclic orders induced
  on nonempty subsets; exact integer/`Fraction` arithmetic; canonical orders
  for `n=3..8`; proof, tests, roadmap, and durable memory.
- **Out of scope:** increasing the production bound `n<=8`; interval
  backends, certificates, checked artifacts, schemas, or examples; new
  geometric optimum or asymptotic claims; product-distance changes; Git
  writes; unrelated lint cleanup.

## Verified Facts

- A one-wrap closed walk is forced to be the reverse orientation of the cyclic
  order induced on one subset of at least two positions. With the singleton
  square convention, singleton scores are dominated for `n>=3`, so
  \[
  \Lambda^{(1)}(\sigma)
  =\max_{|T|\ge2}P_\sigma(T)
  =\max_{T\ne\varnothing}P_\sigma(T).
  \]
- The all-order saturation theorem holds: for every complete order,
  \[
  \Lambda(\sigma)=\Lambda^{(1)}(\sigma).
  \]
  The proof strictly dominates every vertex-simple multi-wrap ratio by
  comparing half the total square sum with the duplicated-pairing lower bound
  on the complete induced cycle.
- Consequently \(\Lambda(\sigma)\) and \(\Lambda_n\) are integers. This is a
  product-weight theorem and does not reduce the nonlinear exact angular STN
  to one-wrap checks.
- Exact test-only subset/path and literal subset oracles agree with each other
  and production on all 2,956 canonical orders for `n=3..8`. The bounded
  values and minimizer counts remain `(12,26,47,77,118,172)` and
  `(1,3,4,15,24,84)`.
- Production remains hard-bounded to `3<=n<=8` and 2,520 canonical orders in
  one row.

## Assumptions / Inferences

- The saturation proof reuses the exact duplicated-multiset pairing bound
  already proved in `research/ALL_N_LOWER_BOUND.md` and restates its complete-
  set value for independent audit.
- Existing checked artifacts retain their separate guarded `mpmath.iv` trust
  premise; this task neither strengthens nor weakens it.

## Decisions And Rationale

- Keep both new oracles test-only so the production algorithm, public API,
  hard domain, and enumeration ceiling remain unchanged.
- Use a literal nonempty-subset cyclic-sum oracle and an exact subset/path
  full-cycle dynamic program independent of descending closure, macro
  compression, and Karp maximum-cycle-mean scoring.
- Preserve singleton, two-element multiplicity, repeated-closed-walk, and
  exact-angular non-consequence semantics explicitly.
- Retain the production `Fraction` type and Karp algorithm as an independent
  full-ratio implementation even though the theorem forces denominator one.

## Plan And Expected Delta

- Complete the exact proof and independent mathematical audit. COMPLETED.
- Add the bounded independent oracle and focused regressions. COMPLETED.
- Synchronize authoritative proof, roadmap, global memory, status, and task
  evidence. COMPLETED.
- Run complete verification and final diff hygiene. COMPLETED.

## Verification

- **Checks:** exhaustive independent-oracle regression; focused and full
  pytest; checked-artifact semantic verification; Python compilation;
  task-scoped Ruff; independent mathematical, oracle, and classification
  reviews; final status, diff, whitespace, and temporary-path hygiene.
- **Observed result:** 23 focused and 196 full tests pass; all 2,956 canonical
  orders agree; checked-artifact verification accepts 4 certificates, 76
  local brackets, and the finite summary; compilation, task-scoped Ruff,
  independent reviews, and diff hygiene pass.
- **Limitations:** local execution used Python 3.14.3; hosted Python 3.11-3.13
  CI was not run. Four known repository-wide Ruff findings remain outside the
  changed paths.

## Blockers / Risks

- No current blocker.
- Finite oracle agreement is implementation evidence, not the all-order proof.
- Saturation gives no all-`n` formula for \(\Lambda_n\), new exact geometric
  value, improved geometric sandwich, or asymptotic coefficient.
- A repeated maximizing one-wrap cycle is a multi-wrap closed walk with the
  same ratio; strict multi-wrap separation is only for vertex-simple cycles.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact all-order theorem, independent bounded
  oracle, synchronized durable memory, complete tests, artifact verification,
  independent audits, and final hygiene pass.
- **Files changed:** authoritative proof note; test module; production
  docstrings; project brief; durable knowledge; fixed-order STN source note;
  roadmap; current status; and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, `CURRENT_STATUS.md`, and this
  dossier.

