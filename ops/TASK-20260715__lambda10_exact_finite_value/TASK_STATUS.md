# TASK_STATUS - TASK-20260715__lambda10_exact_finite_value / Exact Finite Value of Lambda_10

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove the finite exact value \(\Lambda_{10}=323\) through
  the accepted core reduction, without changing the production scorer or its
  public `n<=8` enumeration boundary.
- **Expected output:** a human-checkable seven-label lower lemma based on the
  pairing relaxation and its `320`--`322` low-signature audit; an exact
  shortcut-gain witness certificate; independent test-only checks over 360
  lemma classes and all 511 witness subsets; synchronized authoritative
  sources and task evidence.

## Scope

- **In scope:** cyclic orders induced on `S7={4,...,10}` and
  `S6={5,...,10}`; the witness core order
  `(10,2,3,4,7,8,6,9,5)`; exact integer subset scoring; proof, focused
  tests, authoritative project memory, and this dossier.
- **Out of scope:** production scorer or API changes; increasing the public
  complete-order enumeration domain beyond `n<=8`; enumerating or
  classifying all `n=10` core minimizers; exact geometry, `R_2^*(10)`,
  interval-certificate artifacts, schemas, checked artifacts, all-`n`
  formulas, asymptotic claims, or Git writes.

## Verified Facts

- Startup completed on a clean worktree at `f5d056113d54`.
- The accepted index-one theorem gives
  \(\Lambda_{10}=\min_\tau K(\tau)\).
- The exact pairing classification has baseline `320`, no
  six-cycle at levels `320` or `321`, one dihedral six-cycle at level `322`,
  and exact witness score `323`.
- The exact least-entry pairing recurrence proves that its surviving state
  counts are `(1,2,3,6,6,10,8)` and its leaves are exactly the eight recorded
  low signatures.
- The finite lemma gives `K(tau)>=323` for every core order, while the exact
  shortcut-gain certificate gives
  `K(10,2,3,4,7,8,6,9,5)=323`; hence `Lambda_10=323`.
- Independent test-only arithmetic covers all 360 lemma classes and all 511
  nonempty witness subsets. The witness has exactly two argmax subsets.

## Assumptions / Inferences

- The requested result is a finite exact combinatorial fact, not an exact
  geometric optimum or an all-`n` theorem.
- Test-only finite enumeration will audit the proof but will not serve as the
  source of the mathematical lower bound.

## Decisions And Rationale

- Keep every new enumeration and literal subset computation test-local and
  independent of repository canonicalizers, public enumeration, and the
  production Karp scorer.
- Record the complete low-pairing signature table so the exclusion of levels
  `320` and `321` and the unique cyclic signature at `322` can be checked by
  hand.
- Do not pursue the complete `n=10` core minimizer set in this task.

## Plan And Expected Delta

- Prove the pairing-level lower lemma. COMPLETED.
- Add the exact witness certificate and independent bounded tests. COMPLETED.
- Synchronize authoritative sources and this dossier. COMPLETED.
- Run proportional verification and final diff hygiene. COMPLETED.

## Verification

- **Checks:** focused and full pytest; checked-artifact semantic verification;
  explicit schema-validation regression; targeted Ruff and Python
  compilation; independent mathematical, test, and documentation audits;
  final Git status, diff, whitespace, and production-boundary inspection.
- **Observed result:** the focused `n=10` tests pass 2/2, the cyclic-ratio
  module passes 30/30, and the complete repository suite passes 206/206.
  Schema validation passes 4/4; semantic verification accepts 4 certificates
  and 76 local brackets; lint, compilation, all three audits, and final diff
  hygiene pass. No `src/` diff exists.
- **Limitations:** local execution used Python 3.14.3; Python 3.11 syntax and
  APIs were independently audited but not run locally. Hosted CI was not run
  or independently inspected for this worktree.

## Blockers / Risks

- No current blocker.
- The exact value must not be conflated with \(R_2^*(10)\), and the bounded
  lemma oracle must not be described as an enlarged public enumeration.
- The oracle computationally lists two lemma equality cycles, but this task
  does not supply their separate structural classification or classify all
  minimizing core orders.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact finite proof, independent 360-class and
  511-subset checks, complete local suite, three independent audits, and final
  diff hygiene all pass.
- **Files changed:** proof note, focused test module, project brief, durable
  knowledge, roadmap, current status, and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
