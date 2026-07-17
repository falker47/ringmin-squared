# EVIDENCE - TASK-20260717__p0_terminal_gap_classification / P0 Terminal-Gap Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / decision | Startup and scope lock | project state, predecessor proof, Git worktree | PASS |
| EV-002 | exact proof / independent review | Exact local placement theorem | proof note and three read-only derivations | PASS |
| EV-003 | exact computation / regression | Independent diagnostic and regressions | task script, pytest, Ruff, artifact verifier | PASS after one format correction |
| EV-004 | hygiene / consistency / diff | Final synchronized handoff | project memory, structure checks, Git diff | PASS |

## EV-001 - Startup And Scope Lock

- **Date:** 2026-07-17
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the full roadmap, the relevant
  proof-note sections, and the predecessor STRICT dossier; ran read-only Git
  root and status checks.
- **Relevant output:** Repository root confirmed; initial worktree clean. The
  retained data are \(n=10m+3\), \(m\ge3\), \(d=8m+4\),
  \(T=d(d-1)/2\), the scaffold (NR4), and paths (NR2)--(NR3).
- **Interpretation:** Scope was fixed before the new diagnostic: characterize
  the location of \(P_0\) only, under a generic bijection, without choosing or
  enumerating a full reassignment.
- **Limitations:** Startup evidence is not the mathematical proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---strict-startup-and-scope-lock`.

## EV-002 - Exact Local Placement Theorem

- **Date:** 2026-07-17
- **Method or command:** Derived every distance-one and distance-two pair in
  the seven-label local word and checked the algebra through three independent
  read-only derivations. Treated \(j=0\), \(1\le j\le2m-2\),
  \(j=2m-1\), the transition indices, and the smallest \(m=3\).
- **Relevant output:**
  \[
  M^{\rm loc}_1(j)=T,
  \qquad
  M^{\rm loc}_2(j)=T+{j(d-1)\over2}.
  \]
  The right terminal condition alone permits \(j\in\{0,2m-1\}\), but the
  left permits only \(j=0\). The closing word is
  \((n,2,d-1,4m+2,d-2,4m+1,d)\).
- **Interpretation:** EXACT NECESSARY PLACEMENT THEOREM: every reassignment
  with \(W^{(\le2)}\le T\) must fix \(P_0\) in \(G_0\). All other gaps are
  excluded; \(G_0\) is locally non-excluded but not globally sufficient.
- **Limitations:** The identity assignment is a separate prior witness. This
  proof gives no nonidentity existence claim and does not classify the other
  paths.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---exact-placement-theorem-and-independent-audits`.

## EV-003 - Independent Diagnostic And Regressions

- **Date:** 2026-07-17
- **Method or command:** Ran
  `python ops/TASK-20260717__p0_terminal_gap_classification/exact_diagnostic.py`,
  Python compilation, Ruff lint and format checks,
  `python -m pytest tests/test_product_distance.py`, the schema-selection
  regression, the complete test suite with a task-specific `--basetemp`, and
  the checked-artifact semantic verifier.
- **Relevant output:**
  - Diagnostic: `locally_allowed=(0,)` for \(m=3,4,9,25\); symbolically, the
    one-sided sets are \(\{0\}\) and \(\{0,2m-1\}\), with the closing index
    printed numerically in each row.
  - First Ruff format check: one file would be reformatted. After applying
    Ruff format, compilation, lint, and format checks pass.
  - A final direct `ruff` command was unavailable on the shell `PATH`; reruns
    through `python -m ruff` passed lint and confirmed the file was already
    formatted.
  - Focused surrogate regression: 49 passed.
  - Schema-selection regression: 4 passed.
  - Complete suite: 283 passed.
  - Checked artifacts: 4 certificates and 76 local brackets verified.
- **Interpretation:** FINITE EXACT CORROBORATION plus regression safety. The
  diagnostic scans only the \(2m\) gap indices and constant-size local words;
  it constructs no complete order and enumerates no reassignment.
- **Limitations:** Four exact rows are not the all-\(m\) proof and say nothing
  about completion of the remaining paths.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---gap-index-diagnostic-and-regression-verification`.

## EV-004 - Final Synchronized Handoff

- **Date:** 2026-07-17
- **Method or command:** Inspected every changed and new file; checked the
  exact expected path set, absence of unexpected dossier children, UTF-8
  readability, trailing whitespace, display-math delimiters, unique proof
  tags, the sole-diagnostic claim, cross-source agreement, Git status, the
  complete diff, and `git diff --check`. Obtained independent read-only audits
  of the final proof text and diagnostic implementation.
- **Relevant output:** The final structure summary was
  `TRACKED_SCOPE_OK=5 NEW_DOSSIER_OK=4`
  `CHANGED_FILES_UTF8_TRAILING_OK=9 CHANGED_MARKDOWN_DISPLAY_OK=8`
  `PROOF_TAGS_UNIQUE=156 PG_TAGS=15 SOLE_DIAGNOSTIC_OK`. Both independent
  audits returned PASS, and the final diff check returned no output. The first
  hygiene harness had a PowerShell variable-interpolation parse error; a
  second heuristic incorrectly counted the LaTeX row break `\\[6pt]` as a
  display opener. The final trimmed-line delimiter check corrected that test
  defect and passed for all eight changed Markdown files. A direct final
  `ruff` call was unavailable on `PATH`; the module invocation passed.
- **Interpretation:** The proof note, stable memory, current state, roadmap,
  and dossier agree on the exact necessary classification and its existence
  boundary. The work is READY_FOR_REVIEW.
- **Limitations:** Git review and committing remain manual.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---final-synchronization-and-handoff`.
