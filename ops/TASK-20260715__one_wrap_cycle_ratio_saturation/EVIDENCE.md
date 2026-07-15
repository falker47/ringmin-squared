# EVIDENCE - TASK-20260715__one_wrap_cycle_ratio_saturation / One-Wrap Cycle-Ratio Saturation

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / computation | Clean startup and exact problem reduction | authoritative sources and read-only probes | PASS |
| EV-002 | proof / independent review | Induced-subset equivalence and all-order saturation | authoritative proof note and three independent audits | PASS after recorded corrections |
| EV-003 | code / exact computation / test | Independent full-cycle and induced-subset oracles on `n=3..8` | test module and exhaustive pytest regression | PASS |
| EV-004 | test / lint / verification / hygiene | Complete repository verification and final review | pytest, artifact verifier, Ruff, compilation, Git diff | PASS with known unrelated global lint findings |

## EV-001 - Startup And Exact Reduction

- **Date:** 2026-07-15
- **Method or command:** Read the mandatory startup files, prior cyclic-ratio
  dossier, complete proof note, source scorer, tests, roadmap, and task
  templates; inspected read-only Git status; ran exact exploratory comparisons
  between production and literal induced-subset scoring.
- **Relevant output:** Git reported `main...origin/main` with no changed paths.
  A bounded rerun compared all 2,956 canonical orders for `n=3..8` in 1.67
  seconds and found no discrepancy. A separate sampled probe checked random
  orders through `n=14` without finding a counterexample.
- **Failed exploratory probe preserved:** an initial combined bounded/random
  script exceeded its 120-second command timeout after entering an
  unnecessarily large random subset sweep; its buffered output was unusable.
  The separated bounded rerun completed and supplied the stated result.
- **Interpretation:** The data motivated the proof search but did not prove an
  all-order claim.
- **Limitations:** These exploratory comparisons called production and were
  not the final independent oracle.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-exact-reduction`

## EV-002 - Exact All-Order Proof And Audit

- **Date:** 2026-07-15
- **Method:** Classified `q=1` closed walks by their unique ascent and strict
  descending remainder; applied the duplicated-multiset pairing lower bound to
  the complete induced order; applied \(2ij\le i^2+j^2\) and degree two to
  every vertex-simple multi-wrap cycle; used the accepted closed-walk
  decomposition.
- **Relevant result:** For every complete order and `n>=3`,
  \[
  \Lambda(\sigma)=\Lambda^{(1)}(\sigma)
  =\max_{|T|\ge2}P_\sigma(T)
  =\max_{T\ne\varnothing}P_\sigma(T).
  \]
  Every vertex-simple `q>=2` cycle lies at least \(n(n+1)/4\) below the
  complete induced-order lower bound. Thus the scores are integers.
- **Independent review:** three independent mathematical/documentation audits
  recovered the theorem. They identified and prompted correction of reused
  product-distance notation \(B_n,Q_n\), conditional singleton wording, and
  an overbroad statement about concatenating closed walks. The final re-audit
  reports no remaining mathematical or classification defect.
- **Classification:** induced-subset equivalence and saturation are EXACT
  THEOREMS. The integer consequence is an EXACT THEOREM. No finite computation
  is used in their proof.
- **Limitations:** this is a theorem for the separable product ratio. It does
  not reduce nonlinear exact angular-STN feasibility to one-wrap cycle checks,
  identify exact geometric optima, or add asymptotic claims.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---exact-all-order-saturation-proof`

## EV-003 - Independent Oracle And Bounded Regression

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3.
- **Oracle design:** the literal oracle enumerates every nonempty position
  subset and evaluates its induced cyclic sum, including singleton squares and
  twice-counted two-element products. The full-ratio oracle rotates every
  simple cycle to its least position and uses exact states
  `(visited subset, last position, wrap count)`; retaining only maximum path
  score per state is exact because every future extension and closure depends
  only on that state.
- **Independence:** neither test oracle calls or reproduces production
  descending-path closure, one-wrap macro compression, or Karp's maximum-
  cycle-mean recurrence.
- **Exhaustive result:** all canonical-order counts
  `(1,3,12,60,360,2520)` for `n=3..8`, totaling 2,956, agree between the two
  oracles and production. Values are `(12,26,47,77,118,172)` and minimizer
  counts are `(1,3,4,15,24,84)`.
- **Additional independent audit:** a direct anchored simple-cycle enumerator
  evaluated 41,358,293 cycles, while the subset/path audit visited 4,719,901
  states and 10,718,765 transitions; both agreed with induced subsets on every
  bounded order.
- **Command:**
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp .tmp_pytest_focused_final`
- **Relevant output:** `23 passed in 10.97s`.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** the local runtime is finite implementation evidence, not
  the all-order proof. Python 3.11 compatibility is source-inspected, not
  locally executed. Production constants remain `MAX_ENUMERATION_N=8` and
  `MAX_CANONICAL_ORDERS=2520`.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---independent-oracle-and-exhaustive-bounded-check`

## EV-004 - Complete Verification And Final Hygiene

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3.
- **Commands:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider --basetemp .tmp_pytest_final_one_wrap`
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  - `$env:PYTHONPATH='src'; python -m ruff check src/power_ringmin/fixed_order_cycle_ratio.py tests/test_fixed_order_cycle_ratio.py`
  - `$env:PYTHONPATH='src'; python -m ruff check .`
  - `python -m compileall -q src/power_ringmin/fixed_order_cycle_ratio.py tests/test_fixed_order_cycle_ratio.py`
  - `git status --short`, `git diff`, and `git diff --check`
- **Relevant output:** `196 passed in 50.81s`; semantic verification accepts
  `certificates=4`, `local_brackets=76`, and the `n=3..6` finite summary;
  targeted Ruff reports `All checks passed!`; compilation and diff whitespace
  checks pass. Repository-wide Ruff reports exactly the four previously
  recorded F401/F841 findings in three untouched files.
- **Independent review:** mathematical, oracle, implementation, and
  classification audits accept the final work after the corrections recorded
  in EV-002. Test-oracle runtime and Python 3.11 API compatibility were also
  reviewed.
- **Temporary-path hygiene:** task-created pytest base directories were
  resolved inside the workspace and removed after their runs.
- **Interpretation:** the proof, bounded oracle, documentation, and complete
  local repository state are verified and ready for manual review.
- **Limitations:** hosted CI was not run. Repository-wide Ruff retains four
  pre-existing F401/F841 findings in three untouched files; task-scoped Ruff
  is clean. Checked-artifact verification confirms no regression but does not
  strengthen its guarded interval-backend trust contract.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---audit-corrections-complete-verification-and-handoff`
