# EVIDENCE - TASK-20260712__critical_constraints_order_structure / Critical Constraints And Order Structure

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source/file/command | Startup and terminology guardrail | startup files, prior dossier, `git status --short`, `TERMINOLOGY.md` | PASS |
| EV-002 | file/artifact/test | Implementation and machine-readable output | `src/power_ringmin/critical_structure.py`, tests, `critical_structure_n3_n6.json` | PASS |
| EV-003 | file/source | Research note and durable memory | `research/FINITE_RESULTS.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md` | PASS |
| EV-004 | command/test | Verification and diff hygiene | pytest, deterministic checks, JSON/Markdown checks, Git diff checks | PASS |

## EV-001 - Startup And Terminology

- **Date:** 2026-07-12
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the prior finite-results summary task status/evidence.
- **Method or command:** `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries.
- **Relevant output:** `TERMINOLOGY.md` defines a strict criterion for any future certified non-incidence/floating statement and weaker labels for this task.
- **Interpretation:** The task starts cleanly and avoids undefined or over-strong "floating" terminology before structural analysis begins.
- **Limitations:** This startup evidence does not verify the analysis implementation or research findings.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup-and-terminology-guardrail`

## EV-002 - Implementation And Machine Output

- **Date:** 2026-07-12
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `src/power_ringmin/critical_structure.py` with `power-ringmin.critical_structure_analysis.v1` output, CLI support, lower-cycle normalization, stable index/radius-pair labels, all-pairs upper-witness slack rankings, common-core intersections, candidate differences, weak-constraint proxy labels, and identical-bracket diagnostics.
- **Relevant output:** Registered `power-ringmin-analyze-critical-structure` in `pyproject.toml` and exported public helpers from `src/power_ringmin/__init__.py`.
- **Relevant output:** Added `tests/test_critical_structure.py` covering cyclic normalization invariance, current core patterns, identical-bracket diagnostics, deterministic generation/load round trip, and console script registration.
- **Method or command:** `python -c "from power_ringmin.critical_structure import main; raise SystemExit(main([...]))"` with fixed `--created-at-utc`.
- **Relevant output:** Generated `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json`.
- **Interpretation:** The requested machine-readable structural data exists and is generated from checked source artifacts without generating `n=7`.
- **Limitations:** The output is structural finite analysis only; it is not a new certificate and does not identify exact active contacts.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---structural-analyzer-and-output`

## EV-003 - Research Note And Durable Memory

- **Date:** 2026-07-12
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** `research/FINITE_RESULTS.md` includes the `n=3..6` certified-result table, candidate orders, exclusion gaps, ratios to `n^3/(6*pi)`, normalized critical-cycle comparison, recurring upper-witness slack patterns, weak-constraint observations, four falsifiable conjectures, open questions, and warnings.
- **Relevant output:** `PROJECT_KNOWLEDGE.md` now records stable structural findings: shared lower-cycle pair cores for `n=5` and `n=6`, the heuristic status of index `1`, and open questions about reduced subsystems and repeated brackets.
- **Relevant output:** `CURRENT_STATUS.md` points the next task at reduced-subsystem analysis and explicitly excludes `n=7` generation/preflight.
- **Interpretation:** Durable memory preserves reusable findings while keeping detailed evidence in the task dossier and machine-readable output.
- **Limitations:** The research note contains conjectures and empirical patterns, not proofs.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---research-note-and-memory`

## EV-004 - Verification And Diff Hygiene

- **Date:** 2026-07-12
- **Method or command:** `python -m py_compile src/power_ringmin/critical_structure.py src/power_ringmin/__init__.py tests/test_critical_structure.py`.
- **Relevant output:** Passed with no output.
- **Method or command:** `python -m pytest tests/test_critical_structure.py`.
- **Relevant output:** `5 passed in 4.83s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `87 passed in 24.34s`.
- **Method or command:** Deterministic structural output comparison against `critical_structure_n3_n6.json`.
- **Relevant output:** `deterministic structural output: True`.
- **Method or command:** JSON parse check for `critical_structure_n3_n6.json` and `examples/finite_results_summary_n3_n6.json`.
- **Relevant output:** JSON parse check passed.
- **Method or command:** Markdown reference check over `research/FINITE_RESULTS.md`, `CURRENT_STATUS.md`, and `PROJECT_KNOWLEDGE.md`.
- **Relevant output:** `markdown references checked: 41`.
- **Method or command:** `rg -n "[ \t]+$" ...` over changed/new text files.
- **Relevant output:** No trailing-whitespace matches were found.
- **Method or command:** `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Relevant output:** Final status and diff were inspected; `git diff --check` produced no output.
- **Relevant output:** A mistaken `node --check` on a Python file failed with `ERR_UNKNOWN_FILE_EXTENSION`; the correct `py_compile` check passed. An initial inline Markdown-reference command had a quoting `SyntaxError`; the same check rerun from stdin passed.
- **Interpretation:** Verification passed, and failed command attempts were command-selection/quoting issues rather than implementation failures.
- **Limitations:** `git diff --check` does not inspect untracked files, so explicit whitespace and JSON/Markdown checks covered new files.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification-and-handoff`
