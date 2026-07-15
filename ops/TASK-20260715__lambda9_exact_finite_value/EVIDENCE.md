# EVIDENCE - TASK-20260715__lambda9_exact_finite_value / Exact Finite Value of Lambda_9

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection / exact probe | Clean startup and reduction | authoritative files and read-only arithmetic | PASS |
| EV-002 | proof | Six-label lower-bound lemma and witness certificate | proof note | PASS |
| EV-003 | exact computation / test | 60-class oracle and 255-subset witness check | focused test module | PASS |
| EV-004 | verification / hygiene | Full suite and final review | repository checks | PASS |

## EV-001 - Startup And Reduction

- **Date:** 2026-07-15
- **Method or command:** Read the mandatory startup files, accepted
  cyclic-ratio proof and scorer, focused tests, roadmap, prior task dossiers,
  and task templates; inspected `git status`; used exact integer-only
  read-only probes to derive the six-label and witness data.
- **Relevant output:** Git reported `main...origin/main` with no changed
  paths. The reduced six-label space has 60 dihedral classes. Literal scoring
  found lower threshold 239 and witness score 239.
- **Interpretation:** The requested result can be handled as a bounded exact
  proof and test-only regression without changing production enumeration.
- **Limitations:** Exploratory arithmetic is not the final recorded proof or
  regression.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-exact-reduction`

## EV-002 - Finite Lower Lemma And Witness Proof

- **Date:** 2026-07-15
- **Method:** Applied the exact duplicated-multiset rearrangement bound to
  \(S_5\), computed the change caused by inserting label `4`, and evaluated
  the six complementary paths for each of the only two exceptional neighbor
  pairs. For the witness, decomposed every induced-subset score relative to
  the full core cycle into exact shortcut gains.
- **Relevant result:** Every cyclic order on \(S_6\) satisfies
  \(\max\{P_\omega(S_6),P_\omega(S_5)\}\ge239\), so every core order has
  \(K\ge239\).
  For \(\tau_*=(9,2,3,5,8,6,7,4)\), only the shortcuts `9->3` and `9->5`
  have positive gain, of `3` and `6`; at most one can occur. Equality forces
  the latter and every other gap adjacent, so \(K(\tau_*)=239\) with unique
  maximizer \(S_6\).
- **Classification:** the lower statement is an EXACT THEOREM (FINITE
  SIX-LABEL LEMMA); \(\Lambda_9=239\) is a VERIFIED FACT (FINITE EXACT
  COMBINATORIAL RESULT).
- **Limitations:** no geometric, exact-radius, all-`n`, asymptotic, or complete
  minimizer-classification claim follows.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---finite-lemma-and-exact-witness`

## EV-003 - Independent Oracles And Focused Tests

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3.
- **Oracle design:** fixing label `9` removes rotations from direct
  permutations of labels `4..8`; retaining second label smaller than the last
  removes reflection, giving 60 classes. A separate literal scorer uses
  position combinations to evaluate all 255 nonempty subsets of the witness.
  Neither path calls a repository canonicalizer, the public enumerator, or
  the production Karp scorer.
- **Exact result:** the 60-class minimum is 239. The unique canonical equality
  row is `(9,4,7,6,8,5)` with `(P(S6),P(S5))=(239,238)`; the only row with
  `P(S6)<239` is `(9,4,8,6,7,5)` with `(238,242)`. Literal witness scoring
  gives 239 only for `S6`.
- **Command:**
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp .tmp_pytest_lambda9_focused`
- **Relevant output:** `27 passed in 12.72s`.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** the sweeps are independent finite implementation evidence,
  not geometric certificates or all-`n` proofs.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---independent-test-only-oracles`

## EV-004 - Complete Verification And Handoff

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3.
- **Commands:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp .tmp_pytest_lambda9_focused`
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider --basetemp .tmp_pytest_lambda9_full`
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  - `$env:PYTHONPATH='src'; python -m ruff check tests/test_fixed_order_cycle_ratio.py`
  - `python -m compileall -q tests/test_fixed_order_cycle_ratio.py`
  - `python --version`
  - `git status --short`, `git diff`, and `git diff --check`
- **Relevant output:** focused pytest reports `27 passed in 12.72s`; full
  pytest reports `200 passed in 59.18s`; semantic verification accepts
  `certificates=4`, `local_brackets=76`, and the `n=3..6` finite summary;
  targeted Ruff reports `All checks passed!`; compilation and final diff
  whitespace checks pass.
- **Independent review:** mathematical audit independently recomputed all 120
  rooted orientations underlying the 60 classes, all 48 shortcut gains, and
  all 255 witness subsets. Test audit found no coverage, independence, or
  Python 3.11 grammar issue. Documentation audit found no mathematical or
  classification defect; its orientation and status clarity suggestions were
  applied.
- **Temporary-path hygiene:** task-created pytest base directories were
  resolved inside the workspace and removed after execution.
- **Interpretation:** the proof, independent finite oracles, documentation,
  and durable handoff are locally verified and ready for manual review.
- **Limitations:** hosted Python 3.11-3.13 CI was not run. Local execution used
  Python 3.14.3; Python 3.11 compatibility was independently grammar-checked
  but not locally executed. Checked-artifact verification is a non-regression
  check and does not strengthen the guarded interval-backend trust contract.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---complete-verification-and-handoff`
