# EVIDENCE - TASK-20260712__all_n_lower_bound / All-n lower bound

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and scope inspection | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `git status --short` | pass |
| EV-002 | file / test | Lower-bound proof and finite combinatorial test | `research/ALL_N_LOWER_BOUND.md`, `tests/test_search_small_n.py` | pass |
| EV-003 | command / test | Automated verification | pytest, checked-artifact verifier, and diff-check commands | pass after rerun |

## EV-001 - Startup And Scope

- **Date:** 2026-07-12
- **Method or command:** Read required startup files and ran `git status --short`.
- **Relevant output:** `git status --short` produced no paths.
- **Interpretation:** The repository started clean and the requested all-\(n\) lower-bound task is independent of prior ready-for-review work.
- **Limitations:** Hosted CI status was not queried.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup`

## EV-002 - Proof And Finite Combinatorial Test

- **Date:** 2026-07-12
- **Method or command:** Wrote `research/ALL_N_LOWER_BOUND.md`; computed direct canonical-order product minima for `n=3..9`; added `test_adjacent_product_lower_bound_on_all_canonical_orders_n3_to_n9`.
- **Relevant output:** Corrected exploratory computation reported `(n, count, min, relaxed_bound)` as `3 1 11 10`, `4 3 21 20`, `5 12 37 35`, `6 60 58 56`, `7 360 87 84`, `8 2520 123 120`, `9 20160 169 165`.
- **Interpretation:** The test enumerates all canonical orders for `n=3..9` and directly checks the lemma inequality; the strict gap between observed minima and the relaxed bound confirms the test is not asserting exact Hamiltonian-cycle optimality.
- **Limitations:** The finite enumeration test is not the all-\(n\) proof. Two initial exploratory one-liners failed before the corrected computation: one due newline escaping, one due missing direct `src` import path.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---proof-and-tests`

## EV-003 - Verification

- **Date:** 2026-07-12
- **Method or command:** `python -m pytest tests\test_search_small_n.py`
- **Relevant output:** `8 passed in 0.93s`.
- **Interpretation:** The focused canonical-order and small-`n` search tests passed.
- **Limitations:** Focused test coverage does not cover the full repository.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification`

- **Date:** 2026-07-12
- **Method or command:** `python -m pytest`
- **Relevant output:** First run: `1 failed, 109 passed`; failing test was `tests/test_finite_results.py::test_deterministic_generation`, with a transient Git provenance mismatch where regenerated `git_commit` was `null`. Isolated rerun of that test passed. Full-suite rerun: `110 passed in 32.22s`.
- **Interpretation:** The full suite is green after rerun; the first failure was investigated and did not reproduce in isolation or on full rerun.
- **Limitations:** Hosted CI was not queried.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification`

- **Date:** 2026-07-12
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Interpretation:** Existing checked finite artifacts still pass semantic verification; no new finite certificates were generated.
- **Limitations:** This uses the repository's documented local interval-verifier semantics and guarded `mpmath.iv` backend contract.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification`

- **Date:** 2026-07-12
- **Method or command:** `git status --short`; `git diff`; `git diff --check`.
- **Relevant output:** `git status --short` listed the intended modified files plus the new task dossier and `research/ALL_N_LOWER_BOUND.md`; `git diff` was inspected; `git diff --check` produced no output and exited successfully.
- **Interpretation:** The final diff is scoped to the requested proof, tests, roadmap/status, and dossier updates; whitespace checks passed.
- **Limitations:** Untracked file contents were inspected directly because plain `git diff` does not include untracked files.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification`
