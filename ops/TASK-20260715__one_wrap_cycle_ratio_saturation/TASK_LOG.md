# TASK_LOG - TASK-20260715__one_wrap_cycle_ratio_saturation / One-Wrap Cycle-Ratio Saturation

Append-only. Add a new entry to correct previous information.

## 2026-07-15 - Startup And Exact Reduction

- **Action:** Completed the STRICT startup protocol, inspected the accepted
  cyclic-ratio proof/scorer/tests and roadmap, confirmed a clean worktree, and
  began independent mathematical and exact-computation audits.
- **Result:** A `q=1` simple cycle is forced by its selected positions, giving
  the cyclic adjacent-product sum of their induced order, with the
  two-element product counted twice.
- **Interpretation:** The one-wrap equivalence is exact; the remaining
  saturation question requires either an all-order domination argument or a
  smallest exact counterexample.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-exact-reduction`
- **Next step:** complete saturation proof/counterexample search and add the
  independent bounded oracle.

## 2026-07-15 - Exact All-Order Saturation Proof

- **Action:** Proved the induced-subset equivalence, reused the exact
  duplicated-pairing lower bound for the complete order, and bounded every
  vertex-simple multi-wrap cycle by half the total square sum.
- **Result:** No counterexample exists: \(\Lambda(\sigma)=
  \Lambda^{(1)}(\sigma)\) for every complete order and `n>=3`. The proof also
  gives a strict gap for vertex-simple cycles with `q>=2` and establishes
  integrality of the fixed-order and global scores.
- **Interpretation:** This is an exact all-order theorem. It does not depend on
  finite enumeration and does not transfer one-wrap sufficiency to nonlinear
  exact angular-STN cycle weights.
- **Evidence:** `EVIDENCE.md#ev-002---exact-all-order-proof-and-audit`
- **Next step:** implement an independent bounded oracle and verify every
  canonical order for `n=3..8`.

## 2026-07-15 - Independent Oracle And Exhaustive Bounded Check

- **Action:** Added a literal nonempty-subset cyclic-sum oracle and a separate
  exact subset/path dynamic program for the full simple-cycle ratio; compared
  both with production on every canonical order for `n=3..8`.
- **Result:** All 2,956 orders agree exactly. The global values and minimizer
  counts remain `(12,26,47,77,118,172)` and `(1,3,4,15,24,84)`. The focused
  module passes all 23 tests.
- **Interpretation:** The oracle is independent of production descending
  closure, macro compression, and Karp recurrence. It verifies the bounded
  implementation, not the all-order theorem.
- **Evidence:** `EVIDENCE.md#ev-003---independent-oracle-and-bounded-regression`
- **Next step:** synchronize durable sources and run complete verification.

## 2026-07-15 - Audit Corrections, Complete Verification, And Handoff

- **Action:** Synchronized the proof, source note, project brief, durable
  knowledge, roadmap, current status, and dossier; ran complete tests,
  artifact verification, compilation, lint, and hygiene; commissioned
  independent proof, oracle, and classification audits.
- **Result:** Audits accepted the final theorem and implementation after
  correcting collisions with the established product-distance symbols
  \(B_n,Q_n\), making singleton semantics explicit, and narrowing one
  closed-walk equality sentence. The final suite passes all 196 tests;
  checked artifacts remain valid; task-scoped lint and diff hygiene pass.
- **Interpretation:** The task is complete and ready for manual review, with
  the finite/all-order and product-weight/exact-angular boundaries explicit.
- **Evidence:** `EVIDENCE.md#ev-004---complete-verification-and-final-hygiene`
- **Next step:** user review and manual commit decision.
