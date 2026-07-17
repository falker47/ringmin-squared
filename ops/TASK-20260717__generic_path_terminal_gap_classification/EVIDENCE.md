# EVIDENCE - TASK-20260717__generic_path_terminal_gap_classification / Generic Path Terminal-Gap Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / confirmation | Startup, scope, and independent derivation | retained PG material and repository state | PASS |
| EV-002 | computation | Bounded exact local diagnostic | exact_diagnostic.py | PASS |
| EV-003 | test / command | Static checks, regressions, suite, artifacts | repository commands | PASS |
| EV-004 | inspection | Proof correction, scope, hygiene, and final diff | proof/dossier/Git inspection | PASS |

## EV-001 - Startup, Scope, And Independent Derivation

- **Date:** 2026-07-17
- **Method or command:** Read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, the predecessor dossier, relevant sections of
  research/PRODUCT_DISTANCE_SURROGATE.md, and
  research/NEXT_RESEARCH_STEPS.md; inspect
  git status --short --branch; compare three independent symbolic
  derivations.
- **Relevant output:** clean main...origin/main worktree at \(d8107ef\);
  agreement on the exact triple cutoff, universal singleton relation, cyclic
  and endpoint formulas, \(m=3\) table, and the separation between local
  non-exclusion and matching/full-score existence.
- **Interpretation:** Scope and retained definitions were stable before
  editing, and the mathematical delta was independently reproducible.
- **Limitations:** This evidence does not replace the written all-\(m\) proof.
- **Linked log entry:** TASK_LOG.md, STRICT startup and exact derivation.

## EV-002 - Bounded Exact Local Diagnostic

- **Date:** 2026-07-17
- **Method or command:**
  python ops\TASK-20260717__generic_path_terminal_gap_classification\exact_diagnostic.py
- **Relevant output:**
  \[
  \begin{array}{c|r|r|r|r}
  m&\text{scanned }(k,j)&\text{locally allowed}&
  \kappa_{2m-2}&\kappa_{2m-1}\\ \hline
  3&36&27&2&3\\
  4&64&49&3&3\\
  9&324&251&7&7\\
  34&4624&3614&27&27.
  \end{array}
  \]
- **Interpretation:** The standalone standard-library script directly
  reconstructs every constant-size local word for the fixed rows, compares
  every distance-one and distance-two pair with the symbolic formulas, and
  confirms both cutoff forms. It covers cyclic closure, the last nonclosing
  gap, path-type transition, complete \(m=3\) relation, and the equality
  \((34,11,24)\).
- **Limitations:** It scans only \((m,k,j)\) for four fixed values of \(m\);
  it constructs no complete order or bijection, enumerates no path
  permutation, and corroborates rather than proves the all-\(m\) theorem.
- **Linked log entry:** TASK_LOG.md, exact diagnostic and static checks.

## EV-003 - Static Checks, Regressions, Suite, And Artifacts

- **Date:** 2026-07-17
- **Method or commands:**
  - python -m py_compile
    ops\TASK-20260717__generic_path_terminal_gap_classification\exact_diagnostic.py
  - python -m ruff check
    ops\TASK-20260717__generic_path_terminal_gap_classification\exact_diagnostic.py
  - python -m ruff format --check
    ops\TASK-20260717__generic_path_terminal_gap_classification\exact_diagnostic.py
  - python -m pytest -p no:cacheprovider tests\test_product_distance.py
    --basetemp C:\tmp\power-ringmin-pytest-generic-path-focused
  - python -m pytest -p no:cacheprovider
    tests\test_checked_artifact_schema_validation.py
    --basetemp C:\tmp\power-ringmin-pytest-generic-path-schema
  - python -m pytest -p no:cacheprovider
    --basetemp C:\tmp\power-ringmin-pytest-generic-path-full
  - set PYTHONPATH=src and run
    python -m power_ringmin.verify_checked_artifacts
- **Relevant output:** compilation PASS; Ruff lint and format PASS; focused
  regression 49 passed; schema regression 4 passed; full suite 283 passed in
  79.23 seconds; checked artifacts verified with 4 certificates and 76 local
  brackets.
- **Interpretation:** The new diagnostic is statically valid and the
  repository behavior, schema selection, and checked artifacts remain
  unchanged.
- **Retained failed checks:** the initial Ruff format check reported that the
  new script would be reformatted; formatting was applied and the repeated
  checks passed. A later attempt to redirect py_compile cache output to
  C:\tmp\power-ringmin-generic-path-pycache failed with WinError 5; ordinary
  compilation then passed, and the generated dossier cache was removed.
- **Limitations:** Existing tests do not prove the symbolic all-\(m\) theorem.
- **Linked log entry:** TASK_LOG.md, regression suite and artifact
  verification.

## EV-004 - Proof Correction, Scope, Hygiene, And Final Diff

- **Date:** 2026-07-17
- **Method or command:** independent read-only proof and code audits;
  expected-path and sole-diagnostic inspection; UTF-8/delimiter delta checks;
  PG-tag uniqueness; git status, git diff, and git diff --check.
- **Relevant output:** independent audit found one false ordering in the
  prose before (PG19), corrected from \(A_k>c_k>B_k\) to
  \(A_k>B_k>c_k\). Subsequent proof/code audit passed. Expected scope is
  exactly nine files, with one standalone diagnostic and no generated cache.
  PG16--PG36 are unique; UTF-8/delimiter delta, complete diff inspection, and
  final git diff --check pass.
- **Interpretation:** Mathematical formulas and code agree after the recorded
  correction, and the synchronized diff is ready for user review.
- **Retained harness corrections:** a whole-file inline-delimiter check
  surfaced inherited imbalances without changing their delta; a subsequent
  PowerShell Split-based check treated delimiter characters separately; a
  line-aware literal delta check corrected both harness issues and passed.
- **Limitations:** Inspection cannot replace the user's mathematical and
  repository review before a manual commit.
- **Linked log entry:** TASK_LOG.md, independent audits and correction.
