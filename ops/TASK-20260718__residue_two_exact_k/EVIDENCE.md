# EVIDENCE - TASK-20260718 / Residue-Two Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup, clean-tree, and scope audit | repository sources and Git | PASS |
| EV-002 | exact theorem | Shortcut-budget proof, argmax classification, and block sum | `research/FIXED_ORDER_CYCLE_RATIO.md` | PASS |
| EV-003 | bounded exact computation | Independent max-plus and shortcut diagnostic | `exact_diagnostic.py` | PASS |
| EV-004 | source inspection | Pertinent authoritative synchronization and scope audit | Markdown sources | PASS |
| EV-005 | tests / checks / review | Final verification and diff audit | commands and Git diff | PASS |

## EV-001 - Startup And Scope

- **Date:** 2026-07-18
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the relevant predecessor
  dossiers, and the residue-two/canonical/residue-one proof, source, and test
  sections; ran `git status --short --branch` and `git rev-parse HEAD`.
- **Relevant output:** clean `main...origin/main`; HEAD
  `6edc37325200dec1826173b2506dd0893219b28b`.
- **Interpretation:** safe STRICT startup. The target is \(n=5k+2\),
  \(k\ge2\); production, tests, artifacts, and global optimum claims are out
  of scope unless an actual defect is found.
- **Limitations:** source and scope audit only; no theorem follows from this
  check alone.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---strict-startup-and-independent-derivation`.

## EV-002 - Exact Theorem And Proof

- **Date:** 2026-07-18
- **Method or command:** symbolic derivation from (R2C1)--(R2C8), the
  shortcut-budget lemma (K825-6)--(K825-9), direct even/odd block summation,
  and three independent read-only audits.
- **Relevant output:** every hole in \(\{2,\ldots,2k\}\) has positive gain,
  with minimum \(10k+6\); every compressed path with at least two edges has
  strict positive margin; equality forces the sole subset
  \(S_k=\{2k+1,\ldots,5k+2\}\). With \(\varepsilon=k\bmod2\),
  \[
  K(\tau_n^{(2)})
  ={286k^3+459k^2+198k+16
   +\varepsilon(-10k^2+40k+27)\over8}.
  \]
- **Interpretation:** this is an **exact theorem** for every \(k\ge2\), not
  an extrapolation from finite data. Parity changes internal paths and
  lower-order terms only; every argmax is classified.
- **Limitations:** the theorem is for the stated fixed residue-two order. It
  does not identify globally minimizing orders, exact angular thresholds, or
  geometric optima.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---exact-theorem-and-shortcut-budget-proof`.

## EV-003 - Sole Bounded Exact Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python ops/TASK-20260718__residue_two_exact_k/exact_diagnostic.py`;
  `python -m ruff check` and `python -m ruff format --check` on the same
  script; `python -m py_compile` on the same script.
- **Relevant output:** diagnostic `PASS`; 29 full-certificate rows; 4,623,615
  transitions in each max-plus DP; 238,670 oriented shortcut arcs; 970
  formula/comparison tail rows; minimum bounded hole and path margins
  respectively \(26\) and \(7\); one maximizer per residue row; zero K825
  crossovers. Final Ruff and compile checks pass.
- **Interpretation:** the script reconstructs both orders independently,
  aggregates increasing paths by dynamic programming, and imports only the
  standard library. It enumerates neither subsets nor cyclic orders.
- **Failed-check record:** the first Ruff format check requested mechanical
  formatting; `python -m ruff format` was applied, after which lint, format,
  compilation, and the diagnostic all pass.
- **Limitations:** this is a **bounded exact computation** on
  \(2\le k\le30\), with direct formula checks through \(k=1000\). It
  corroborates but does not replace EV-002.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---sole-bounded-diagnostic`.

## EV-004 - Authoritative Synchronization And Scope

- **Date:** 2026-07-18
- **Method or command:** line-by-line source inspection and independent
  read-only audits of formulas, pointwise rows, asymptotics, consequences,
  and intended file scope.
- **Relevant output:** the primary exact theorem and proof are in
  `research/FIXED_ORDER_CYCLE_RATIO.md`; pertinent cross-references and stable
  consequences are synchronized to the surrogate note, roadmap, project
  brief, stable knowledge, and current status. No production, test, artifact,
  schema, backend, certificate, or enumeration-limit change is included.
- **Interpretation:** exact label-one elimination and the fixed-order sandwich
  authorize the fixed-order score and subset-argmax transfer, its angular
  inequalities, and one-sided global or subsequential upper bounds. The
  \(O(n^2)\) K825 improvement does not order angular thresholds or improve
  the cubic coefficient.
- **Limitations:** the synchronization records a construction-specific exact
  theorem and its authorized consequences only; it adds no global optimum or
  geometric activity classification.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---exact-comparison-and-authoritative-synchronization`.

## EV-005 - Final Repository Verification

- **Date:** 2026-07-18
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `python -m power_ringmin.verify_checked_artifacts`;
  `python -m pytest -p no:cacheprovider
  tests/test_checked_artifact_schema_validation.py`; the EV-003 diagnostic in
  normal and `python -I` modes; `python -m ruff check`,
  `python -m ruff format --check`, and `python -m py_compile` on the
  diagnostic; strict source-structure and equation-tag checks;
  `git status --short --branch`, complete tracked and untracked diff
  inspection, and `git diff --check`.
- **Relevant output:** pytest `283 passed in 65.64s`; artifact verification
  `certificates=4 local_brackets=76 summary_n_values=3,4,5,6`; schema
  `4 passed`; diagnostic PASS in both modes with 29 full rows, 4,623,615
  transitions per DP, and 238,670 arcs; Ruff and `py_compile` PASS; source
  structure PASS for ten intended paths, 489 unique primary equation tags,
  and KR2-1 through KR2-36; final diff check has no output.
- **Interpretation:** all relevant regressions, independent bounded checks,
  structural checks, and repository-hygiene checks pass. Final Git scope is
  six pertinent tracked Markdown files and the four-file dossier, with no
  production, test, artifact, schema, certificate, or cache modification.
- **Failed-check record:** the first Ruff format check requested mechanical
  formatting; the final Ruff checks pass. The first two source-check
  invocations had checker-scope defects: one counted LaTeX row spacing
  `\\[6pt]` as a display opener, and the next tested tag uniqueness across
  unrelated research notes rather than the primary note. Corrected line-exact
  display and primary-note tag checks pass. Neither was a theorem, source-
  content, or repository-test defect.
- **Limitations:** the bounded diagnostic remains finite; the all-\(k\)
  result rests on the independently audited symbolic proof. Historical
  dossiers are not rewritten.
