# EVIDENCE - TASK-20260713__product_distance_surrogate / Product-Distance Surrogate

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / computation / review | Startup and independent audits | project memory, theorem/code/test sources, independent exact enumeration | PASS |
| EV-002 | file / test / computation | Exact implementation, table, and focused tests | source, tests, research note, exact probe | PASS |
| EV-003 | command | Full repository and checked-artifact verification | pytest, semantic verifier | PASS |
| EV-004 | review | Independent mathematical, code, table, and documentation review | changed source/test/research/memory files | PASS |
| EV-005 | command / review | Final path, UTF-8, whitespace, status, and diff inspection | ten intended paths and Git diff | PASS |

## EV-001 - Startup And Independent Audits

- **Date:** 2026-07-13
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant `ops/` dossiers, `research/ALL_N_LOWER_BOUND.md`, roadmap, canonical-order and pattern sources, and related tests; ran `git status --short --branch`; obtained three independent read-only audits.
- **Relevant output:** The initial tree was clean. The audits independently derived the all-pairs feasibility and oriented-tail-gap proofs, identified the `n=3` exception and bounded dihedral convention, and obtained matching exact values, minimizer counts, representatives, zigzag scores, and tail obstructions for `n=3..11`.
- **Interpretation:** The mathematical statement and finite target table have independent pre-implementation checks, including explicit detection of the rendered fraction orientation.
- **Limitations:** The independent finite enumeration is not an all-`n` proof or a geometric certificate; its results must be reproduced by repository code and tests.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---startup-disambiguation-and-independent-audit`

## EV-002 - Exact Implementation, Table, And Focused Tests

- **Date:** 2026-07-13
- **Method or command:** Added `src/power_ringmin/product_distance.py`,
  `tests/test_product_distance.py`, and
  `research/PRODUCT_DISTANCE_SURROGATE.md`; ran an exact `n=3..11` table probe
  with `PYTHONPATH=src`; ran `python -m pytest tests\\test_product_distance.py tests\\test_zigzag_core_upper_bound.py tests\\test_induced_subset_lower_bound.py tests\\test_radius_one_insertion.py`.
- **Relevant output:** The exact probe reproduced all nine rows in about `0.24`
  local seconds. Focused tests reported `24 passed in 1.56s`. The local
  environment was Python `3.14.3` at `HEAD d93f224`; the computation used no
  precision setting, seed, or floating-point value.
- **Interpretation:** Exact rational comparisons, all-pairs scoring,
  canonization/counts, independent smallest cases, bounded work, table values,
  representatives, zigzag, and tail comparisons pass.
- **Limitations:** Timing is a local diagnostic, not a guaranteed bound. The
  deterministic bounds are the hard `n<=11` domain and preflight order cap.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---exact-implementation-table-and-research-note`

## EV-003 - Full Suite And Checked-Artifact Verification

- **Date:** 2026-07-13
- **Method or command:** `python -m pytest`.
- **Relevant output:** `137 passed in 29.63s`.
- **Interpretation:** The complete repository suite passes with the new exact
  surrogate implementation and tests.
- **Limitations:** Tests do not replace the symbolic all-`n` proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---full-verification-and-independent-review`

- **Date:** 2026-07-13
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Interpretation:** Existing checked artifacts remain semantically valid; no
  artifact was created or changed by this task.
- **Limitations:** Existing artifacts retain the documented guarded
  `mpmath.iv` backend trust limitation.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---full-verification-and-independent-review`

## EV-004 - Independent Mathematical, Code, And Documentation Review

- **Date:** 2026-07-13
- **Method or command:** Three read-only reviews of the actual changed proof,
  implementation/tests, exact table, classifications, memory, and scope. The
  code reviewer also ran a second enumeration that did not import the new
  module or use its cutoff, a pre-permutation cap check, and a Python 3.11 AST
  grammar check.
- **Relevant output:** Proof and table review found no mathematical defect.
  Independent enumeration matched every `n=3..11` score, minimizer count,
  representative, zigzag score, and tail obstruction. Code review found no
  float literal or algorithmic defect. Documentation review confirmed the
  ten-file scope and no CLI/schema/artifact/certificate additions; its inline
  math and wording findings were corrected.
- **Interpretation:** Generator, independent computation, proofs, tests, and
  classifications agree.
- **Limitations:** Runtime verification used Python 3.14.3; Python 3.11 syntax
  compatibility was checked statically rather than on a local 3.11 runtime.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---full-verification-and-independent-review`

## EV-005 - Final Scope, UTF-8, Whitespace, And Diff Inspection

- **Date:** 2026-07-13
- **Method or command:** Strict UTF-8/path/trailing-whitespace PowerShell check
  over the intended changed files; `git status --short --untracked-files=all`;
  complete tracked diff and direct untracked-file inspection;
  `git diff --check`.
- **Relevant output:** The first scope-check attempt failed because ordinary
  `git status --short` collapsed the untracked dossier to one directory entry;
  this was a checker-input mismatch, not a repository defect. The corrected
  command used `--untracked-files=all` and reported
  `scope_paths=10 utf8_ok=10 trailing_whitespace=0`. `git diff --check`
  produced no output.
- **Interpretation:** The final scope is exactly the intended source, test,
  research/memory, and dossier paths; all are readable and whitespace-clean.
- **Limitations:** Git warnings about the inaccessible user-global ignore file
  are environmental and do not affect repository status or diff content.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---final-hygiene-and-handoff`
