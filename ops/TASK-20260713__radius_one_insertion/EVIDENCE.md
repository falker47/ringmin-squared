# EVIDENCE - TASK-20260713__radius_one_insertion / Radius-One Insertion

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / computation | Startup and independent mathematical audit | startup files, prior theorem, test sources, exact rational calculations | PASS |
| EV-002 | test | Focused and full pytest verification | insertion/lower-bound tests and full suite | PASS |
| EV-003 | command | Checked-artifact semantic verification | `power_ringmin.verify_checked_artifacts` | PASS |
| EV-004 | review / command | Independent proof review and final diff hygiene | theorem/test diff, Git status and diff | PASS |

## EV-001 - Startup And Mathematical Audit

- **Date:** 2026-07-13
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/ALL_N_LOWER_BOUND.md`, `research/FINITE_RESULTS.md`, `research/NEXT_RESEARCH_STEPS.md`, relevant prior dossiers, `tests/test_induced_subset_lower_bound.py`, and `src/power_ringmin/geometry.py`; ran exact-arithmetic diagnostic probes for candidate angular and threshold bounds.
- **Relevant output:** Initial `git status --short --branch` was `## main...origin/main` with no changed paths. Independent audits agreed on the forbidden-arc proof, the configuration-level reuse of the induced-subset lower bound, the exact `n=12,13` rational bounds, the uniform `n>=14` parity inequality, and feasible-radius-set equality.
- **Interpretation:** The proposed conclusion follows with sufficient explicit threshold `N=12`; no minimizer is required and no checked `n=5,6` observation is used as proof.
- **Limitations:** The audit does not prove `N=12` minimal and does not decide `n<=11`.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---startup-audit-and-proof-draft`

## EV-002 - Focused And Full Pytest

- **Date:** 2026-07-13
- **Method or command:** `python -m pytest tests\test_radius_one_insertion.py tests\test_induced_subset_lower_bound.py`; `python -m pytest`.
- **Relevant output:** focused run: `12 passed in 0.16s`; full run: `122 passed in 31.61s`.
- **Interpretation:** Exact-arithmetic threshold diagnostics, floating angular-majorant diagnostics, prior induced-subset diagnostics, and the complete repository suite pass.
- **Limitations:** The tests are finite diagnostics. The all-`n` conclusion rests on the symbolic proof in `research/ALL_N_LOWER_BOUND.md`.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---verification-and-handoff`

## EV-003 - Checked-Artifact Semantic Verification

- **Date:** 2026-07-13
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Interpretation:** Existing checked artifacts remain semantically valid; none was regenerated or modified.
- **Limitations:** This verification retains the documented guarded `mpmath.iv` backend trust limitation and is independent of the exact insertion theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---verification-and-handoff`

## EV-004 - Proof And Final Diff Review

- **Date:** 2026-07-13
- **Method or command:** Independent read-only review of `research/ALL_N_LOWER_BOUND.md` and `tests/test_radius_one_insertion.py`; `git diff --check`; `git diff --stat`; `git diff`; `git status --short`.
- **Relevant output:** Independent review found no actionable mathematical or test defect. `git diff --check` produced no output; final modified and untracked paths were inspected.
- **Interpretation:** Geometry, strict inequalities, rational boundary calculations, uniform parity algebra, infimum semantics, scope, and diff hygiene are ready for manual review.
- **Limitations:** User review and manual commit remain required; Codex did not stage or commit any file.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---verification-and-handoff`
