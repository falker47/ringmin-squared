# TASK_STATUS - TASK-20260712__critical_constraints_order_structure / Critical Constraints And Order Structure

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Extract structural information from the checked `n=3..6` finite interval certificates, focusing on certified candidate orders, normalized lower critical cycles, upper-witness slack patterns, and common candidate subsystems without generating `n=7`.
- **Expected output:** Terminology/design note, deterministic analysis module or script, machine-readable structural output, focused tests, concise research note, durable memory updates, and verification evidence.

## Scope

- **In scope:** Checked `examples/small_n_interval_certificate_n3.json` through `examples/small_n_interval_certificate_n6.json`; derived `examples/finite_results_summary_n3_n6.json`; certified candidate orders; lower-endpoint negative-cycle signatures; upper-witness all-pairs slacks; weakly constrained empirical observations; structural conjectures clearly labeled.
- **Out of scope:** `n=7` generation or preflight; new certificate production; exact optimum claims; exact tie claims; all-`n` or asymptotic proofs; modifying upstream Ringmin.

## Verified Facts

- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- Checked source certificates exist for `n=3`, `n=4`, `n=5`, and `n=6` under `examples/`.
- The prior finite-results summary contract task ended `READY_FOR_REVIEW` and identified this structural analysis as the next task.
- `src/power_ringmin/critical_structure.py` builds deterministic `power-ringmin.critical_structure_analysis.v1` output for certified candidate orders only.
- `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json` was regenerated with fixed timestamp `2026-07-12T00:00:00Z` and matched a fresh deterministic rebuild byte-for-byte.
- `research/FINITE_RESULTS.md` records classified finite facts, verified structural data, numerical observations, empirical patterns, heuristic weak-constraint labels, conjectures, open questions, and warnings.

## Assumptions / Inferences

- This task uses `STRICT` mode because it interprets certified finite artifacts and proposes falsifiable structural conjectures.
- Candidate-order membership is inherited from the checked finite-results summary contract and remains finite-certificate evidence only.
- Upper-witness slack rankings are diagnostics at certified upper endpoints, not exact active-contact certificates.

## Decisions And Rationale

- Created a local terminology note before analysis to avoid using "floating" as an undefined or over-strong term.
- Analyzed only certified candidate orders because the requested objective is structural extraction from the current candidate sets rather than another exhaustive certificate task.
- Separated exact directed lower-cycle signatures, pair-kind signatures, and undirected pair-set signatures so common reduced subsystems are not confused with identical directed cycles.
- Required zero lower-cycle incidence before listing a possible weakly constrained index, keeping the heuristic label restricted to the stronger finite proxy pattern observed at `n=5` and `n=6`.

## Plan And Expected Delta

- Read checked certificate and summary artifacts, then identify certified candidate orders. COMPLETE.
- Add terminology/design note for floating and weaker constraint labels. COMPLETE.
- Implement deterministic structural analysis module or script and machine-readable output. COMPLETE.
- Add tests for normalization invariance and deterministic output. COMPLETE.
- Create `research/FINITE_RESULTS.md` with classified finite facts, observations, patterns, heuristics, conjectures, and warnings. COMPLETE.
- Update project durable memory and this task dossier. COMPLETE.
- Run focused tests, full tests, deterministic output checks, Markdown reference checks, final status/diff inspection, and `git diff --check`. COMPLETE.

## Verification

- **Checks:** Python compile check; focused structural tests; full pytest suite; deterministic structural output comparison; JSON parse checks; Markdown reference check; trailing-whitespace scan; Git status/diff inspection; `git diff --check`.
- **Observed result:** `python -m py_compile ...` passed; `python -m pytest tests/test_critical_structure.py` passed with `5 passed`; `python -m pytest` passed with `87 passed`; deterministic structural output comparison printed `True`; JSON parse checks passed; Markdown reference check reported `41`; trailing-whitespace scan found no matches; final `git diff --check` produced no output.
- **Limitations:** Checks do not prove exact optima, exact ties, true active contact sets, all-`n` behavior, or asymptotics. The source finite certificates retain the documented guarded `mpmath.iv` backend limitation.

## Blockers / Risks

- No current blocker.
- Residual risk: structural observations are derived from finite `n=3..6` artifacts and must not be promoted to exact or all-`n` statements.

## Next Atomic Action

- User reviews the structural analysis implementation and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed with `87 passed in 24.34s`; deterministic rebuild matched `critical_structure_n3_n6.json`; `git diff --check` produced no output.
- **Files changed:** `src/power_ringmin/critical_structure.py`, `src/power_ringmin/__init__.py`, `pyproject.toml`, `tests/test_critical_structure.py`, `research/FINITE_RESULTS.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `research/FINITE_RESULTS.md`, `src/power_ringmin/critical_structure.py`, `tests/test_critical_structure.py`, and `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json`.
- **Suggested manual commit message:** `Analyze finite candidate critical structure`
