# EVIDENCE - TASK-20260712__induced_subset_lower_bound / Induced-subset lower bound

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and scope inspection | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/ALL_N_LOWER_BOUND.md`, `tests/test_search_small_n.py`, `git status --short` | pass |
| EV-002 | file / proof | Induced-subset lower-bound proof and documentation reclassification | `research/ALL_N_LOWER_BOUND.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md` | pass |
| EV-003 | file / test | Finite diagnostic tests for arithmetic, discrete maximum, and subset pairing | `tests/test_induced_subset_lower_bound.py` | pass |
| EV-004 | command / verification | Automated tests, checked-artifact verifier, and diff checks | pytest, checked-artifact verifier, git diff checks | pass |

## EV-001 - Startup And Scope

- **Date:** 2026-07-12
- **Method or command:** Read required startup files and relevant prior research/test files; ran `git status --short`.
- **Relevant output:** `git status --short` produced no paths at startup.
- **Interpretation:** The repository started clean and the requested induced-subset strengthening can proceed without mixing unrelated changes.
- **Limitations:** Hosted CI was not queried.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup`

## EV-002 - Proof And Documentation

- **Date:** 2026-07-12
- **Method or command:** Extended `research/ALL_N_LOWER_BOUND.md`; updated `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `research/NEXT_RESEARCH_STEPS.md`.
- **Relevant output:** The note proves that induced subset gaps sum to \(2\pi\), derives \(P_{m,n}=\sum_{k=m}^n k(m+n-k)=((n-m+1)(m^2+4mn+m+n^2-n))/6\), and proves \(\liminf 6\pi R_2^*(n)/n^3\ge4(\sqrt2-1)>1\).
- **Interpretation:** The former \(R_2^*(n)=n^3/(6\pi)(1+o(1))\) conjectural target and \(R_2^*(n)=n^3/(6\pi)+O(n^2)\) target are disproved by the all-\(n\) theorem.
- **Limitations:** The proof does not provide a matching upper bound or identify an exact asymptotic leading constant.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---proof-and-documentation`

## EV-003 - Finite Diagnostic Tests

- **Date:** 2026-07-12
- **Method or command:** Added `tests/test_induced_subset_lower_bound.py`; ran `python -m pytest tests\test_induced_subset_lower_bound.py`.
- **Relevant output:** `4 passed in 0.05s`.
- **Interpretation:** The finite tests check the \(P_{m,n}\) formula, the moderate-`n` discrete maximizer over \(m\), and pairing bounds on selected nonconsecutive subsets and induced orders.
- **Limitations:** These finite tests are not the all-\(n\) proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---tests`

## EV-004 - Verification

- **Date:** 2026-07-12
- **Method or command:** `python -m pytest`
- **Relevant output:** `114 passed in 42.07s`.
- **Interpretation:** The full automated test suite passed after adding the induced-subset diagnostics.
- **Limitations:** Hosted CI was not queried.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification`

- **Date:** 2026-07-12
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Interpretation:** Existing checked finite artifacts still pass semantic verification; no new finite certificates were generated.
- **Limitations:** This uses the repository's documented local interval-verifier semantics and guarded `mpmath.iv` backend contract.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification`

- **Date:** 2026-07-12
- **Method or command:** `git status --short`; `git diff --stat`; `git diff`; direct `Get-Content -Raw` inspection of untracked new files; `git diff --check`.
- **Relevant output:** `git status --short` listed the intended modified files plus new untracked task dossier and test file; `git diff --check` produced no output and exited successfully.
- **Interpretation:** The tracked diff is scoped to the requested proof, tests, roadmap/status, and dossier updates; untracked new files were inspected directly; whitespace checks passed for tracked changes.
- **Limitations:** Plain `git diff` does not include untracked file contents until the user stages them.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification`
