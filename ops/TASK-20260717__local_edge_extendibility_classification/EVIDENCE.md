# EVIDENCE - TASK-20260717__local_edge_extendibility_classification / Local Edge Extendibility Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / confirmation | Startup, scope, and three independent symbolic audits | retained PG material and repository state | PASS |
| EV-002 | computation | Bounded exact Hall/shift diagnostic | exact_diagnostic.py | PASS |
| EV-003 | test / command | Static checks, regressions, suite, and artifacts | repository commands | PASS |
| EV-004 | inspection | Proof corrections, scope, hygiene, and final diff | proof/dossier/Git inspection | PASS |

## EV-001 - Startup, Scope, And Independent Derivation

- **Date:** 2026-07-17
- **Method or command:** Read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, the predecessor dossier,
  research/PRODUCT_DISTANCE_SURROGATE.md, and
  research/NEXT_RESEARCH_STEPS.md; inspect
  `git status --short --branch`, `git rev-parse HEAD`, and the retained local
  relation; compare three independent read-only derivations.
- **Relevant output:** clean `main...origin/main` worktree at
  `d772b289c6d93cd1e0d10d26d7070d8b2ba5366e`; unanimous agreement on the
  exact Ferrers thresholds, residual Hall formula, three interval shifts,
  boundary treatment, and candidate classification.
- **Interpretation:** The starting relation and scope were stable, and the
  theorem was independently reproducible before editing.
- **Limitations:** This evidence does not replace the written all-\(m\) proof.
- **Linked log entry:** TASK_LOG.md, STRICT startup and independent derivation.

## EV-002 - Bounded Exact Hall And Shift Diagnostic

- **Date:** 2026-07-17
- **Method or command:**
  `python ops\TASK-20260717__local_edge_extendibility_classification\exact_diagnostic.py`
- **Relevant output:**
  \[
  \begin{array}{c|r|r|r|r}
  m&|\mathcal R_{\rm loc}|&|\mathcal R_{\rm ext}|&
  \text{Hall obstructions}&\kappa_{2m-1}\\ \hline
  3&27&22&5&3\\
  4&49&42&7&3\\
  9&251&234&17&7\\
  34&3614&3547&67&27.
  \end{array}
  \]
- **Interpretation:** For every local edge in the four bounded rows, the
  script evaluates residual Hall. For every extendible edge it constructs
  exactly the proof's interval shift and checks permutation, target, forced
  zero edge, and every resulting Ferrers edge. For each zero-column
  obstruction it directly obtains \(2m-1\) residual gaps and \(2m-2\)
  neighbors. Transition, terminal-singleton, closing-column, \(m=3\), and
  the retained equality \((34,11,24)\) checks pass.
- **Limitations:** The script scans four fixed values of \(m\). It performs no
  matching search, enumerates no path permutation, builds no cyclic order,
  and scores no distance; it corroborates rather than proves the theorem.
- **Linked log entry:** TASK_LOG.md, proof and sole bounded diagnostic.

## EV-003 - Static Checks, Regressions, Suite, And Artifacts

- **Date:** 2026-07-17
- **Method or commands:**
  - `python ops\TASK-20260717__local_edge_extendibility_classification\exact_diagnostic.py`
  - in-memory `compile(...)` of the diagnostic source;
  - `python -m ruff check` and `python -m ruff format --check` on the
    diagnostic;
  - `python -m pytest -p no:cacheprovider tests\test_product_distance.py
    --basetemp C:\tmp\power-ringmin-pytest-edge-extendibility-focused`;
  - isolated rerun of
    `tests\test_finite_results.py::test_deterministic_generation`;
  - serial complete-suite rerun with `-p no:cacheprovider` and a task-specific
    `C:\tmp` basetemp;
  - schema regression with `-p no:cacheprovider` and a task-specific basetemp;
  - set `PYTHONPATH=src` and run
    `python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** diagnostic PASS at \(m=3,4,9,34\); syntax PASS; Ruff
  lint/format PASS; 49 focused tests PASS; isolated provenance test PASS;
  serial complete suite 283 PASS; schema regression 4 PASS; checked artifacts
  verified with 4 certificates and 76 local brackets.
- **Retained failed check:** the first complete-suite run was launched in
  parallel with other provenance-aware commands and returned 282 PASS / 1
  FAIL. `test_deterministic_generation` compared the checked
  `git_commit=d772b28...` with a transient regenerated `git_commit=null`.
  The exact test passed immediately in isolation, and the complete suite then
  passed serially.
- **Interpretation:** No persistent production, schema, artifact, or
  repository regression was detected. The transient failure was confined to
  concurrent Git-provenance observation and is retained rather than hidden.
- **Limitations:** Existing tests do not prove the symbolic all-\(m\) theorem.
- **Linked log entry:** TASK_LOG.md, static checks and focused regression;
  complete regression and retained transient failure.

## EV-004 - Proof, Scope, Hygiene, And Final Diff

- **Date:** 2026-07-17
- **Method or command:** three independent read-only proof/code/repository
  audits; diagnostic reruns; expected-path and sole-diagnostic inspection;
  UTF-8/BOM and generated-cache checks; PG37--PG49 uniqueness; stale-claim
  search; `git status`, complete `git diff`, and `git diff --check`.
- **Relevant output:** Hall equivalence, every shift direction, minimum row,
  triple/singleton crossings, terminal singleton, last nonclosing gap, cyclic
  closure, and logical separation pass. Four precision edits were applied:
  terminal-row exclusion from rightward slack, PG39--PG40 citation at
  \(r=1\), the extra universal singleton closing-column edge in one PG44
  shift, and explicit expected shift-case assertions. The final scope is five
  synchronized project Markdown files plus one four-file STRICT dossier, with
  one diagnostic, no cache, valid UTF-8/no BOM, unique PG37--PG49 tags, and a
  clean whitespace diff.
- **Retained harness correction:** The first expected-path comparison failed
  because `git status --porcelain` collapses the wholly untracked dossier to
  one directory entry. The corrected comparison combines tracked changed
  paths with a direct enumeration of the four dossier files.
- **Interpretation:** The theorem, code, and durable state agree after the
  recorded prose/assertion corrections and are ready for user review.
- **Limitations:** Inspection cannot replace user review.
- **Linked log entry:** TASK_LOG.md, independent audits and corrections;
  final synchronization and handoff.
