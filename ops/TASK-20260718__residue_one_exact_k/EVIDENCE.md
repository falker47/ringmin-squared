# EVIDENCE - TASK-20260718 / Residue-One Exact K

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
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, both relevant predecessor
  dossiers, and the residue-one/canonical proof, source, and test sections;
  ran `git status --short --branch` and `git rev-parse HEAD`.
- **Relevant output:** clean `main...origin/main`; HEAD
  `aca4a7b3544fa015b21774be2413296321f47ed3`.
- **Interpretation:** safe STRICT startup. The exact public target is
  (n=5k+1), (k\ge2), and residue two is excluded.
- **Limitations:** source and scope audit only; no theorem follows from this
  check alone.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---strict-startup-and-independent-derivation`.

## EV-002 - Exact Theorem And Proof

- **Date:** 2026-07-18
- **Method or command:** symbolic derivation from the residue-one block word;
  shortcut-budget proof using (K825-6)--(K825-9); direct even/odd block
  summation; three independent read-only mathematical audits.
- **Relevant output:** every hole in \(\{2,\ldots,2k\}\) has positive
  deletion gain, every non-atomic compressed path has strict positive margin,
  and equality forces the unique subset
  \(S_k=\{2k+1,\ldots,5k+1\}\). With \(\varepsilon=k\bmod2\),
  \[
  K(\tau_n^{(1)})=
  {857k^3+891k^2+214k
   +\varepsilon(27k^2-51k-18)\over24}.
  \]
  The direct boundary values are \(K=452\) at \(k=2\) and \(K=1328\) at
  \(k=3\).
- **Interpretation:** this is an **exact theorem** for every \(k\ge2\), not
  an extrapolation from finite data. Parity changes only lower-order terms;
  there are no tied or exceptional maximizing subsets.
- **Limitations:** the theorem is for the stated fixed residue-one order only;
  it does not classify globally minimizing orders and says nothing about
  residue two.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---exact-theorem-and-shortcut-budget-proof`.

## EV-003 - Sole Bounded Exact Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python ops/TASK-20260718__residue_one_exact_k/exact_diagnostic.py`.
  A separate read-only audit also compared both local generators with their
  production definitions for \(2\le k\le30\).
- **Relevant output:** `PASS`; 29 full-certificate rows; 4,504,280 max-plus
  transitions in each DP family; 234,030 oriented shortcut arcs; 970
  formula/comparison tail rows; minimum bounded hole gain 14; minimum bounded
  path margin 15; one maximizer per residue-one row; zero K825 crossovers.
- **Interpretation:** the diagnostic reconstructs both orders independently,
  enumerates increasing paths by aggregated dynamic programming rather than
  subsets, and checks every oriented shortcut arc. It imports only
  `__future__` and `dataclasses`; there are no project or test helpers.
- **Limitations:** this is a **bounded exact computation** on
  \(2\le k\le30\), plus direct formula checks through \(k=1000\). It
  corroborates but does not replace EV-002's all-\(k\) proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---sole-bounded-diagnostic`.

## EV-004 - Authoritative Synchronization And Scope

- **Date:** 2026-07-18
- **Method or command:** line-by-line source inspection plus an independent
  read-only audit of formulas, pointwise rows, asymptotics, consequences, and
  modified-path scope.
- **Relevant output:** the exact theorem and proof are primary in
  `research/FIXED_ORDER_CYCLE_RATIO.md`; `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `start.md`, and
  `PROJECT_KNOWLEDGE.md` carry only pertinent cross-references and stable
  consequences. The canonical gap is positive for every \(k\ge2\), has no
  crossover, and is \(n^3/3000+O(n^2)\).
- **Interpretation:** the only geometric/global statements are those licensed
  by exact label-one elimination and the fixed-order sandwich, including the
  residue-one subsequence upper bound \(857/3000\). Explicit non-consequences
  prevent globalization or an exact angular comparison.
- **Limitations:** no production/test file, artifact, schema, certificate, or
  residue-two analysis is in scope.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---exact-comparison-and-authoritative-synchronization`.

## EV-005 - Final Repository Verification

- **Date:** 2026-07-18
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `python -m power_ringmin.verify_checked_artifacts`;
  `python -m pytest -p no:cacheprovider
  tests/test_checked_artifact_schema_validation.py`; the EV-003 diagnostic;
  `python -m ruff check`, `python -m ruff format --check`, and
  `python -m py_compile` on that diagnostic; strict source-structure and
  equation-tag checks; `git status --short --branch`, complete tracked and
  untracked diff inspection, and `git diff --check`.
- **Relevant output:** pytest `283 passed in 69.29s`; artifact verification
  `certificates=4 local_brackets=76 summary_n_values=3,4,5,6`; schema
  `4 passed`; diagnostic PASS with 29 full rows, 4,504,280 transitions per DP,
  and 234,030 arcs; Ruff and `py_compile` PASS; source structure PASS for nine
  Markdown paths, 453 unique primary equation tags, and all 32 KR1 tags;
  final diff check has no output.
- **Interpretation:** all relevant regression, independent bounded,
  structural, and repository-hygiene checks pass. Final Git scope is six
  pertinent tracked Markdown files and the four-file dossier, with no
  production or test modification.
- **Failed-check record:** the first Ruff format check correctly reported the
  new diagnostic needed formatting; `python -m ruff format` was applied and
  both final Ruff checks pass. Two initial source-check invocations had checker
  defects (a case-row spacing token was counted as a display opener, then the
  two-character literal `\\r` was searched instead of a carriage-return
  byte); the corrected line-exact and byte-exact checker passes. An initial
  artifact-verifier invocation used the nonexistent path
  `scripts/verify_checked_artifacts.py`; the authoritative module command
  above passes. None was a theorem, source-content, or repository-test defect.
- **Limitations:** the bounded diagnostic remains finite; the all-\(k\) result
  depends on the independently audited symbolic proof. Historical dossiers
  are not rewritten.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---regressions-audits-and-ready-for-review`.
