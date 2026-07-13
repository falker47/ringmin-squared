# EVIDENCE - TASK-20260713__zigzag_core_improved_upper_bound / Zigzag Core Improved Upper Bound

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / exact audit | Startup and independent mathematical audit | startup files, theorem note, patterns and geometry sources | PASS |
| EV-002 | test | Focused exact and numerical diagnostics | focused upper-bound/insertion tests | PASS |
| EV-003 | test | Full repository suite | `python -m pytest` | PASS |
| EV-004 | command | Checked-artifact semantic verification | `power_ringmin.verify_checked_artifacts` | PASS |
| EV-005 | review / command | Final proof, diff, and hygiene review | theorem/test diff and Git checks | PASS |

## EV-001 - Startup And Independent Mathematical Audit

- **Date:** 2026-07-13
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/ALL_N_LOWER_BOUND.md`, `research/NEXT_RESEARCH_STEPS.md`, the prior insertion and regular-core dossiers, `src/power_ringmin/patterns.py`, `src/power_ringmin/geometry.py`, and relevant tests; confirmed the tree with `git status --short --branch`; obtained three independent read-only audits.
- **Relevant output:** Initial status was `## main...origin/main` with no changed paths. The audits independently derived \(\theta_R(i^2,j^2)<2ij/R\), the exact adjacent/closing/`q>=2` zigzag lemma, all-pairs feasibility at \(V_n\), and \(V_n/n^3\to1/(2\pi)\), with no counterexample for `n>=12`.
- **Interpretation:** The exact proof strategy is sound and scoped for implementation.
- **Limitations:** Independent review supports but does not replace the recorded symbolic proof; finite probes are diagnostic only.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---startup-audit-and-implementation`

## EV-002 - Focused Exact And Numerical Diagnostics

- **Date:** 2026-07-13
- **Method or command:** `python -m pytest tests\test_zigzag_core_upper_bound.py tests\test_regular_core_upper_bound.py tests\test_radius_one_insertion.py`.
- **Relevant output:** `11 passed in 1.51s`.
- **Interpretation:** The exact-integer zigzag lemma over `n=3..256`, sampled angular majorant, sampled direct all-pairs geometry at \(V_n\), prior \(U_n\) baseline, and accepted insertion diagnostics all pass.
- **Limitations:** The finite diagnostics do not prove the all-\(n\) theorem; the proof is symbolic.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---focused-full-and-artifact-verification`

## EV-003 - Full Repository Suite

- **Date:** 2026-07-13
- **Method or command:** `python -m pytest`.
- **Relevant output:** `128 passed in 35.67s`.
- **Interpretation:** The complete repository test suite passes with the new diagnostics included.
- **Limitations:** Passing tests do not replace mathematical proof or remove the documented artifact-backend trust limitation.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---focused-full-and-artifact-verification`

## EV-004 - Checked-Artifact Semantic Verification

- **Date:** 2026-07-13
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Interpretation:** Every existing checked artifact remains semantically valid; none was generated or modified.
- **Limitations:** The verifier retains the documented guarded `mpmath.iv` backend trust limitation and is independent of the exact all-\(n\) proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---focused-full-and-artifact-verification`

## EV-005 - Final Proof, Diff, And Hygiene Review

- **Date:** 2026-07-13
- **Method or command:** Independent read-only review of the theorem and test implementation; final `git diff`, `git diff --check`, changed-file trailing-whitespace scan, and `git status --short`.
- **Relevant output:** Independent mathematical review passed. `git diff --check`, explicit changed-file trailing-whitespace scan, and dossier tab scan produced no findings; final status contained only the intended modified and untracked task files.
- **Interpretation:** The proof, diagnostics, documentation, and repository hygiene are ready for manual review.
- **Limitations:** User review and manual commit remain required; Codex will not stage or commit any file.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---independent-review-and-handoff`
