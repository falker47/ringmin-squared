# EVIDENCE - TASK-20260713__regular_core_cubic_upper_bound / Regular-Core Cubic Upper Bound

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / review | Startup and independent mathematical audit | startup files, prior theorem, geometry source, test sources | PASS |
| EV-002 | test | Focused and full pytest verification | theorem diagnostics and full suite | PASS |
| EV-003 | command | Checked-artifact semantic verification | `power_ringmin.verify_checked_artifacts` | PASS |
| EV-004 | review / command | Final proof, diff, and hygiene review | theorem/test diff and Git checks | PASS |

## EV-001 - Startup And Mathematical Audit

- **Date:** 2026-07-13
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/ALL_N_LOWER_BOUND.md`, `research/NEXT_RESEARCH_STEPS.md`, `src/power_ringmin/geometry.py`, prior radius-one task memory, and relevant tests; confirmed the working tree with `git status --short --branch`; obtained independent read-only audits of the proof, diagnostics, and documentation impact.
- **Relevant output:** Initial status was `## main...origin/main` with no changed paths. The proof audit confirmed strict fixed-`R` monotonicity, the displayed quadratic root, explicit regular-polygon all-pairs feasibility, valid insertion without attainment, and the asymptotic coefficient gap.
- **Interpretation:** The requested exact construction is sound and ready for repository verification.
- **Limitations:** Independent review supports but does not replace the recorded symbolic proof; finite diagnostics remain non-proof evidence.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---startup-proof-audit-and-implementation`

## EV-002 - Focused And Full Pytest

- **Date:** 2026-07-13
- **Method or command:** `python -m pytest tests\test_regular_core_upper_bound.py`; `python -m pytest`.
- **Relevant output:** Focused run: `3 passed in 0.16s`. Full run: `125 passed in 30.03s`.
- **Interpretation:** The closed-form identity, finite worst-pair reduction, explicit adjacent and non-adjacent all-pairs feasibility, and complete repository suite pass.
- **Limitations:** The new tests are finite floating-point diagnostics. The all-`n` result rests on the exact proof in `research/ALL_N_LOWER_BOUND.md`.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---verification-and-handoff`

## EV-003 - Checked-Artifact Semantic Verification

- **Date:** 2026-07-13
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Interpretation:** Existing checked artifacts remain semantically valid; none was generated or modified.
- **Limitations:** This verification retains the documented guarded `mpmath.iv` backend trust limitation and is independent of the exact upper-bound proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---verification-and-handoff`

## EV-004 - Independent Review And Final Diff Hygiene

- **Date:** 2026-07-13
- **Method or command:** Independent read-only proof, test, and documentation reviews; `git diff --check`; changed-file trailing-whitespace scan; `git diff --stat`; `git diff`; `git status --short`.
- **Relevant output:** Review confirmed the algebra, worst-pair monotonicity, all-pairs logic, asymptotics, coefficient classification, and insertion/infimum semantics. The one wording issue about regular-polygon vertices versus polar directions was corrected. Final Git and whitespace checks passed.
- **Interpretation:** The exact proof, focused diagnostics, higher-level references, durable memory, and diff are ready for manual review.
- **Limitations:** User review and manual commit remain required; Codex did not stage or commit any file.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---verification-and-handoff`
