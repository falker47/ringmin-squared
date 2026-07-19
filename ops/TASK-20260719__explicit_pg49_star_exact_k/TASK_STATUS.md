# TASK_STATUS - TASK-20260719 / Explicit PG49-Star Exact K

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove Ferrers compatibility of the prescribed explicit
  PG49 bijection on `n=10m+3`, evaluate its exact induced-subset objective
  `K`, classify every maximizing subset, derive all five `m mod 5` formulas
  and the cubic coefficient, and compare it with K825 and both PG46 orders.
- **Expected output:** exact symbolic proofs, one bounded independent
  standard-library max-plus diagnostic, and synchronization of only the
  pertinent research and durable-memory sources.

## Scope

- **In scope:** the single displayed bijection `alpha_*`, the retained
  symbolic scaffold, exact Ferrers thresholds, fixed-order combinatorial
  `K`, deletion gains, every compressed shortcut including the cyclic
  closure, formulas, maximizers, and the three requested comparators.
- **Out of scope:** other PG49 matchings, production generators, matching or
  permutation enumeration, subset enumeration, exact angular thresholds,
  geometric feasibility, and any global minimizing-order or optimality
  conclusion.

## Verified Facts

- The startup worktree was clean at
  `fded0cc29029b5d2e725f1609f71ea17b4468e38`.
- The retained scaffold and exact Ferrers support are (PG1)--(PG49); the
  induced-subset definition is (CR12j)--(CR12k); the reusable shortcut
  identity is (K825-6)--(K825-9).
- The proposed map is a bijection and is Ferrers-compatible for every
  `m>=3`; its closing edge is exactly on the threshold.
- Symbolic deletion-gain and compressed-shortcut audits prove that the sole
  maximizing subset is `B_m={4m+1,...,10m+3}`.
- The exact score, five residue formulas, coefficient `857/3000`, and strict
  improvement over all three requested comparators have been derived.

## Assumptions / Inferences

- The three claims supplied by the user were treated as conjectures until
  the shortcut proof was complete. All three are now exact theorems for this
  fixed core-order family; no counterexample exists.
- Previously proved Ferrers, scaffold, and shortcut lemmas are retained
  exact inputs. No Ringmin or geometric statement is generalized.

## Decisions And Rationale

- Use the isolated-hole shortcut identity so every equality case is visible;
  finite max-plus rows corroborate but do not prove the all-`m` theorem.
- Keep one dossier-local diagnostic only. It constructs the prescribed order
  directly, uses an increasing-path max-plus recurrence, and enumerates no
  subset, matching, or permutation.

## Completed Delta

- Added the explicit Ferrers theorem after (PG109).
- Added one exact fixed-order `K` section with gain, shortcut, closure,
  formula, coefficient, and comparator audits.
- Added the standalone bounded diagnostic and synchronized only pertinent
  research/status sources; production, test, schema, and artifact code are
  unchanged.

## Verification

- **Checks:** direct diagnostic; scoped lint, format, and compile; complete
  pytest suite; focused schema tests; checked-artifact verification; scoped
  source-tag/delimiter audit; three independent audits; Git status/diff and
  whitespace audit.
- **Observed result:** all checks pass. The diagnostic finds the unique
  `B_m` argmax on 28 rows, checks 36,989,498 max-plus transitions, all
  958,916 proper oriented arcs, and 998 formula/Ferrers rows. The full test
  suite passes 283 tests; the artifact verifier confirms 4 certificates and
  76 local brackets.
- **Limitations:** bounded computation is corroboration only; all claims are
  about one explicit combinatorial core order.

## Blockers / Risks

- None. A whole-file delimiter-count warning in the long product-distance
  note is inherited unchanged from `HEAD`; the new section is balanced.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** proof, diagnostic, regressions, and independent
  audits all pass; no counterexample exists.
- **Files changed:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/FIXED_ORDER_CYCLE_RATIO.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/FIXED_ORDER_CYCLE_RATIO.md`, and this dossier's `EVIDENCE.md`.
