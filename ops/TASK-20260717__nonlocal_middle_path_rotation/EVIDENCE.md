# EVIDENCE - TASK-20260717__nonlocal_middle_path_rotation / Nonlocal Middle-Path Rotation

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / decision / Git inspection | Startup and a-priori family selection | project memory, predecessor proof/dossiers, Git worktree | PASS |
| EV-002 | exact proof / computation / review | Exact score and independent all-pairs corroboration | proof note, standalone diagnostic, three read-only audits | PASS after one proof-range correction and formatting |
| EV-003 | regression / static / scope / diff | Final repository verification and synchronized handoff | test suite, artifact verifier, schema regression, structure and Git checks | PASS; one retained sandbox-only setup failure documented |

## EV-001 - Startup And A-Priori Family Selection

- **Date:** 2026-07-17
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the accepted construction and
  one-triple-reversal dossiers, and the relevant sections of
  `research/PRODUCT_DISTANCE_SURROGATE.md`; ran read-only Git status. Before
  any new direct scorer was run, fixed the literal assignment
  `G_j <- P_(j+1 mod 2*m)`.
- **Relevant output:** Initial tree clean. The fixed transformation preserves
  the terminal/low scaffold and each oriented path, moves every whole middle
  path exactly once, and sends `P_0` to `G_(2*m-1)`. No alternative family
  was explored.
- **Interpretation:** The experimental corroboration, when added, cannot have
  selected the family after seeing scores.
- **Limitations:** This entry records scope and chronology; it is not yet the
  permutation or score proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---startup-and-a-priori-family-selection`.

## EV-002 - Exact Proof And Independent All-Pairs Corroboration

- **Date:** 2026-07-17
- **Method or command:** Derived every positional-distance class and the
  canonical cut symbolically in
  `research/PRODUCT_DISTANCE_SURROGATE.md`; ran
  `python ops/TASK-20260717__nonlocal_middle_path_rotation/exact_diagnostic.py`;
  ran Ruff lint and format on the sole diagnostic; obtained independent
  read-only audits of the near-distance, far-distance, cut, and diagnostic
  arguments.
- **Relevant output:** The exact theorem is
  \[
  W(\widehat\sigma_m)
  ={(10m+3)(8m+3)\over2},
  \qquad
  \operatorname{Sat}(\widehat\sigma_m)
  =\bigl\{\{10m+3,8m+3\}\bigr\}.
  \]
  The diagnostic passes \(m=3,4,9,25\). At the boundary row \(m=3\), it
  gives
  \[
  (M_1,M_2,M_3,M_{\ge4})
  =(378,891/2,527/3,264),
  \]
  \[
  (C_1,C_2,C_3,C_{\ge4})
  =(364,364,392/3,189),
  \]
  with sole full saturator \((27,33,2)\). The three audits found no
  mathematical or scope defect after adding the required
  \(0\le j\le2m-2\) range to the terminal-low difference. Ruff lint and
  format then pass.
- **Interpretation:** EXACT FAMILY-SPECIFIC OBSTRUCTION: the forced closing
  word \(n,2,d-1\) raises the coefficient from \(8/25\) to \(2/5\);
  bounded exact scoring corroborates but does not prove the all-parameter
  result.
- **Limitations:** Only the a-priori fixed rotation is classified. No second
  family, cyclic-order enumeration, production scorer, API, limit, or
  geometric conclusion is introduced.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---exact-proof-and-independent-corroboration`.

## EV-003 - Final Repository Verification And Synchronized Handoff

- **Date:** 2026-07-17
- **Method or command:** Ran the task-local diagnostic, Python compilation,
  Ruff lint and format checks, the focused product-distance tests, the complete
  test suite, the checked-artifact semantic verifier, and the schema-selection
  regression. Repeated strict UTF-8, trailing-whitespace, display-math,
  proof-tag, sole-diagnostic, protected-scope, cross-source, complete-diff,
  and `git diff --check` inspections after synchronizing the proof note,
  project memory, status, roadmap, and dossier.
- **Relevant output:**
  - `python ops/TASK-20260717__nonlocal_middle_path_rotation/exact_diagnostic.py`:
    PASS for the fixed rows \(m=3,4,9,25\).
  - `python -m py_compile .../exact_diagnostic.py`, Ruff lint, and Ruff format:
    PASS.
  - Focused `tests/test_product_distance.py`: 49 tests passed.
  - Complete suite outside the restricted sandbox: 283 tests passed.
  - The first complete-suite attempt inside the restricted sandbox produced
    31 setup errors, all from denied access to pytest's temporary directory;
    no test body failed. The unrestricted rerun then passed all 283 tests.
  - Checked-artifact verifier: 4 certificates and 76 local brackets verified.
  - Schema-selection regression: 4 tests passed.
  - Final structure report:
    `UTF8_OK=9 TRAILING_OK DISPLAY_OK NR_UNIQUE=42
    ONE_DIAGNOSTIC_OK PROTECTED_SCOPE_OK`.
  - Final `git diff --check`: PASS.
- **Interpretation:** The exact theorem, bounded diagnostic, durable project
  state, and protected scope are synchronized and ready for manual review.
  The retained sandbox failure is environmental and is resolved by the
  successful complete-suite rerun.
- **Limitations:** Verification does not enlarge the theorem beyond the one
  fixed reassignment. Git staging and committing remain manual.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---final-verification-and-handoff`.
