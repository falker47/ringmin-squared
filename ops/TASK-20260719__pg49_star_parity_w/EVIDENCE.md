# EVIDENCE - TASK-20260719 / PG49-Star Parity W

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git | Startup and source reconstruction | repository root and retained research notes | VERIFIED |
| EV-002 | exact theorem | Candidate, odd Ferrers/PG49 compatibility, and `W` | `research/PRODUCT_DISTANCE_SURROGATE.md` | PROVED |
| EV-003 | bounded exact computation | Direct integer relation/Hall/all-pairs diagnostic | `exact_diagnostic.py` | VERIFIED |
| EV-004 | regression / hygiene | Repository checks and final diff audit | repository root | VERIFIED |

## EV-001 - Startup And Source Reconstruction

- **Date:** 2026-07-19
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the general scaffold
  (UC1)--(UC20), the even-`v` PG1--PG49 and PG110--PG114 proofs, pertinent
  task dossiers, and read-only Git state.
- **Relevant output:** clean worktree at
  `c45a5dc7133670874bc76246684cc7d8ed323f89`; no unrelated modifications.
- **Interpretation:** the task could proceed independently and the doubleton
  parity case required a new proof rather than reuse of PG49 by analogy.
- **Limitations:** source reconstruction does not itself prove the new map.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---startup-candidate-fixing-and-symbolic-proof`.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-19
- **Method or command:** direct integer local-score calculation, exact
  Ferrers threshold and Hall analysis, image-interval partition, literal
  boundary and cyclic-word audit, and cyclic distance-class bounds.
- **Relevant output:** with `q=floor((4m+5)/5)=kappa_(2m)`, (PGODD-6) is a
  compatible bijection for every `m>=1`; the doubleton and all singleton rows
  are strictly universal; the minimum map is `(0,2,1)`; and
  `W=(8m+8)(8m+7)/2`.
- **Interpretation:** the requested construction, compatibility, and score
  are exact all-domain combinatorial theorems. No obstruction occurs.
- **Limitations:** `K`, geometry, angular thresholds, and every global
  optimality conclusion are excluded.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---startup-candidate-fixing-and-symbolic-proof`.

## EV-003 - Direct Integer Diagnostic

- **Date:** 2026-07-19
- **Method or command:**
  `python ops/TASK-20260719__pg49_star_parity_w/exact_diagnostic.py`.
- **Relevant output:** the first run failed because the checker applied the
  residual Hall criterion to nonlocal pairs. After changing the diagnostic
  definition to `direct_local and hall_extendible(...)`, the final run
  reported `PASS`: 1,000 formula/Ferrers rows and 1,002,000 image entries;
  40 literal relation rows, 91,880 local checks, and 5,557,960 residual Hall
  inequalities; and 80 full-score rows containing 8,906,280 unordered cyclic
  pairs. The minimum boundary, doubleton, singleton reversal, and closure
  checks also passed.
- **Interpretation:** the initial failure is retained as a corrected
  diagnostic implementation defect. The final bounded exact computation
  corroborates the threshold, support, image, closure, and score formulas.
- **Limitations:** bounded corroboration only; it cannot prove EV-002.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---bounded-diagnostic`.

## EV-004 - Regression And Diff Hygiene

- **Date:** 2026-07-19
- **Method or command:** standalone compile; scoped
  `python -m ruff check --no-cache` and
  `python -m ruff format --check --no-cache`; sole bounded diagnostic;
  `python -m pytest -p no:cacheprovider`; focused schema pytest;
  `python -m power_ringmin.verify_checked_artifacts` with
  `PYTHONPATH=src`; PowerShell tag/delimiter/control-text audit;
  read-only `git status`, complete `git diff`, and
  `git diff --check`.
- **Relevant output:** syntax PASS; Ruff lint and format PASS; diagnostic
  PASS; full pytest 283 passed; schema suite 4 passed; checked artifacts
  verified for four certificates, 76 local brackets, and `n=3,4,5,6`;
  source audit PASS with 27 sequential unique tags and 34 balanced displays;
  final diff and whitespace checks PASS.
- **Interpretation:** repository-proportional regression and hygiene checks
  find no remaining implementation, source-structure, or whitespace defect.
  Independent read-only proof review reports no mathematical defect after
  the preclosing doubleton boundary and explicit `k<=2m` support domain
  were made literal.
- **Limitations:** repository regressions do not independently prove EV-002.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---verification-integration-and-handoff`.
