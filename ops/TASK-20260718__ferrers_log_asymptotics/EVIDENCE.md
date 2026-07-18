# EVIDENCE - TASK-20260718__ferrers_log_asymptotics / Ferrers Log Asymptotics

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / confirmation | Startup, scope, and independent symbolic derivation | PG64--PG85 and three read-only derivations | PASS |
| EV-002 | computation | Growing-row residual diagnostic | `residual_diagnostic.py` | PASS |
| EV-003 | test / command | Static checks and repository regressions | repository commands | PASS |
| EV-004 | inspection | Synchronization, scope, and final diff | intended nine-file scope | PASS |

## EV-001 - Startup, Scope, And Symbolic Derivation

- **Date:** 2026-07-18
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, PG64--PG73 in
  `research/PRODUCT_DISTANCE_SURROGATE.md`, the predecessor dossier, roadmap,
  templates, `git status`, and `git log`; compare three independent
  read-only derivations focused respectively on the asymptotic algebra,
  adversarial boundary audit, and diagnostic design.
- **Relevant output:** clean `main...origin/main` state at
  `3472b47e2f10e721b44c504ce3db9355e89ceac6`; unanimous coefficient
  \(14\log2+6\log3-10\log5-2\); exact factorization
  \[
  Z_m={(2m-1)!(6m-1)!(8m)!\over(4m)!(10m-1)!};
  \]
  and the all-\(m\) residual envelope in PG84.
- **Interpretation:** The proposed asymptotic is correct. Exact rounding
  handles cutoff equality, the factorial component isolates the
  \(j/m\to0\) singularity, and the remaining errors are at most logarithmic.
- **Limitations:** Independent agreement does not replace the written proof;
  no finer \(\log m\) coefficient is claimed.
- **Linked log entry:** `TASK_LOG.md`, STRICT startup and independent
  derivation; proof written.

## EV-002 - Growing-Row Residual Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python -B ops\TASK-20260718__ferrers_log_asymptotics\residual_diagnostic.py`.
- **Relevant output:** the script checked thirteen rows
  \(m=3,4,5,6,7,16,64,256,1024,4096,16384,65536,262144\). Selected columns
  from the final run are:

  | \(m\) | coefficient estimate | residual | residual / \(\log m\) | count minus smooth / \(\log m\) |
  |---:|---:|---:|---:|---:|
  | 3 | -1.00271826452 | 2.38777979993 | 2.17345083844 | -1.04681156519 |
  | 7 | -1.36984062040 | 3.00162970868 | 1.54253253170 | -0.85336277347 |
  | 256 | -1.77701083589 | 5.53831132211 | 0.998761784914 | -0.788148608005 |
  | 4096 | -1.79678231996 | 7.62898242660 | 0.917191259490 | -0.773218214118 |
  | 262144 | -1.79860390184 | 10.7381128464 | 0.860656786222 | -0.766231148313 |

  Final line:
  `PASS: listed rows satisfy the stated all-m envelopes; no permutation or matching enumeration`.
  Exact integer assertions also passed for \(\kappa_0\), \(\kappa_1\), both
  PG71 endpoints, the first universal row, \(\ell_m\), the transition factors
  \(m,m-1,1\), and equality of the complete column/row factor multisets.
- **Interpretation:** The direct factors approach the predicted linear
  coefficient while their residuals remain inside PG84. The signed ceiling
  column is negative, as required by literal ceiling removal. The script is
  independent of project helpers and scans only \(O(m)\) formula indices.
- **Limitations:** finite rows corroborate but do not prove PG84--PG85.
- **Linked log entry:** `TASK_LOG.md`, growing-row diagnostic implemented.

## EV-003 - Static Checks And Repository Regressions

- **Date:** 2026-07-18
- **Method or command:** run the final residual diagnostic and predecessor
  Ferrers Ryser diagnostic; `python -m py_compile` once and subsequent
  `python -B` runs; `python -m ruff check` and
  `python -m ruff format --check`; focused product-distance pytest with cache
  disabled; complete pytest with an isolated `C:\tmp` basetemp; the four
  checked-artifact schema tests; and
  `python -m power_ringmin.verify_checked_artifacts` with `PYTHONPATH=src`.
- **Relevant output:** both diagnostics PASS; compile PASS; final Ruff lint
  and format PASS; 49 focused tests PASS; complete suite 283 PASS; four schema
  tests PASS; checked artifacts verify four certificates and 76 local
  brackets.
- **Retained failed checks:** the first Ruff format check and the check after
  audit-driven diagnostic edits each requested one mechanical reformat; the
  final checks pass. The first complete-suite run reported 252 passed and 31
  setup errors, all `PermissionError` failures creating the isolated
  `C:\tmp\ringmin_squared_ferrers_log_full` directory under the sandbox. The
  approved rerun of the identical suite command passed all 283 tests.
- **Interpretation:** No mathematical, production, test, schema, artifact, or
  certificate regression remains. The initial full-suite failure was an
  environment permission boundary, not a failing assertion.
- **Limitations:** repository tests do not replace the all-\(m\) proof.
- **Linked log entry:** `TASK_LOG.md`, verification and audit corrections.

## EV-004 - Synchronization, Scope, And Final Diff

- **Date:** 2026-07-18
- **Method or command:** three independent read-only audits of PG74--PG85,
  the post-format diagnostic, and cross-file synchronization; incorporate
  findings; rerun diagnostic and static checks; inspect equation-tag
  uniqueness, expected paths, generated caches, trailing whitespace, full
  Git diff, `git status`, and `git diff --check`.
- **Relevant output:** the proof audit found no P0--P2 issue and independently
  checked the algebra and endpoint formulas through \(m=10000\); its sole
  clarity suggestion now states that the first universal row is always a
  triple row. The diagnostic audit found no arithmetic bug and prompted four
  finite-scope improvements: unambiguous signed header, listed-row PASS text,
  literal endpoint/transition assertions, and exact factor-multiset equality
  on every configured row. The synchronization audit found no formula or
  claim drift; its premature-status, wording, and generated-cache findings
  were corrected. Final scope and diff checks are recorded at handoff.
- **Interpretation:** The proof, diagnostic, brief, durable knowledge,
  roadmap, current status, and dossier state the same theorem and limitations.
  Exactly five authoritative project files and four dossier files are in
  scope; no production, test, schema, artifact, certificate, alternative
  scaffold, or geometric source changed.
- **Limitations:** inspection cannot replace user review.
- **Linked log entry:** `TASK_LOG.md`, verification and audit corrections;
  final handoff.
