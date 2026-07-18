# EVIDENCE - TASK-20260718 / Closing PG46 Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git | Startup and scope audit | repository sources | PASS |
| EV-002 | exact theorem | Backbone, shortcut budget, and block sum | proof source | PROVED |
| EV-003 | bounded computation | Independent scorer, DP, shortcut audit | exact_diagnostic.py | PASS |
| EV-004 | source inspection | Authoritative synchronization | six memory sources | PASS |
| EV-005 | tests / checks | Final repository verification | commands below | PASS |
| EV-006 | review | Independent and final diff audits | agents / Git diff | PASS |

## EV-001 - Startup And Scope

- **Date:** 2026-07-18
- **Method or command:** read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, pertinent task dossiers, PG46 and K825 research sources,
  code, and tests; ran git status --short --branch and git rev-parse HEAD.
- **Relevant output:** clean main...origin/main; HEAD
  963aa533e254cc94e17c1d5e7cd81284df13d552.
- **Interpretation:** safe STRICT startup with one explicit core-order family
  and no unrelated uncommitted work.
- **Limitations:** a source and scope audit makes no new mathematical claim.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---strict-startup-and-scope-audit.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-18
- **Method or command:** exact expansion of PG46; exhaustive isolated-hole
  deletion gains; all-length compressed-path shortcut bounds; retained block
  summation; exact specialization and subtraction of K825.
- **Relevant output:** equations (KPG46-1)--(KPG46-21) prove the unique
  optimizer \(S_m=\{4m+1,\ldots,10m+3\}\),
  \[
  K={572m^3+631m^2+223m+22\over2},
  \qquad
  K-K_{825}=m^2-6m-4
  \]
  for every \(m\ge3\). The exact minimum hole and nontrivial compressed-path
  margins are \(28m+12\) and \(12m+4\).
- **Interpretation:** exact construction-specific theorem; improvement at
  \(m=3,4,5,6\), worsening for \(m\ge7\), no tie, and unchanged cubic
  coefficient \(143/500\).
- **Limitations:** no geometric realizability, global minimization, or result
  about another PG46 bijection follows.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---exact-symbolic-theorem-derived.

## EV-003 - Bounded Independent Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  python ops/TASK-20260718__pg46_closing_exact_k/exact_diagnostic.py.
- **Relevant output:**

      closing PG46 K diagnostic: PASS
      max-plus/shortcut rows: 28 (m=3..30)
      max-plus transitions: 36989498
      oriented shortcut arcs: 958916
      formula rows: 998 (m=3..1000)
      minimum row: m=3, K=10907, K825=10920
      pointwise crossover: better m=3..6; worse m>=7; no integer tie
      leading coefficient: unchanged at 143/500

- **Interpretation:** the independent order builder, scorer, max-plus
  increasing-path DP, and shortcut audit agree with exact formula,
  uniqueness, minimum margins, boundary row, and K825 comparison.
- **Corrected exploratory failure:** an early attempt to import an older
  dossier diagnostic through importlib omitted registration in sys.modules,
  so its dataclass decorator failed. Registering the temporary module made
  that exploratory cross-check pass. The new standalone diagnostic neither
  imports nor depends on that script.
- **Limitations:** bounded computation corroborates but does not prove the
  all-\(m\) theorem. The DP uses increasing paths rather than subset,
  permutation, or matching enumeration.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---bounded-independent-diagnostic-passed.

## EV-004 - Authoritative Synchronization

- **Date:** 2026-07-18
- **Method or command:** cross-reference and formula audit of
  research/FIXED_ORDER_CYCLE_RATIO.md,
  research/PRODUCT_DISTANCE_SURROGATE.md,
  research/NEXT_RESEARCH_STEPS.md, start.md, PROJECT_KNOWLEDGE.md, and
  CURRENT_STATUS.md.
- **Relevant output:** all six sources state the same unique tail, cubic
  formula, K825 difference, crossover, unchanged coefficient, and
  construction-specific limitation. Only this task dossier was added.
- **Interpretation:** stable reusable knowledge and current task truth are
  synchronized without changing production, tests, artifacts, schemas,
  certificates, or unrelated research sources.
- **Limitations:** historical completed dossiers were not rewritten.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---authoritative-synchronization-and-regressions.

## EV-005 - Final Repository Verification

- **Date:** 2026-07-18
- **Method or commands:**
  - exact diagnostic, before and after final proof review;
  - Ruff check --no-cache and Ruff format --check on the diagnostic;
  - focused product-distance and fixed-cycle-ratio pytest with
    -p no:cacheprovider and a task-specific C:\tmp basetemp;
  - complete pytest suite with separate cache isolation;
  - checked-artifact schema pytest with a separate basetemp;
  - PYTHONPATH=src and python -m power_ringmin.verify_checked_artifacts;
  - primary equation-tag, KPG46 sequence, added Markdown/LaTeX structure,
    whitespace, status, and Git diff checks.
- **Relevant output:** diagnostic PASS; Ruff PASS; 150 focused tests PASS;
  all 283 repository tests PASS; four schema tests PASS; checked artifacts
  verify with four certificates and 76 local brackets; 832 unique
  letter-prefixed research tags; KPG46-1--KPG46-21 complete and unique;
  47 added display opens and closes; final git diff --check has no output.
- **Corrected source-check failures:** the first tag command incorrectly
  required bare numeric tags to be globally unique across separate research
  notes and therefore reported the expected duplicates 1--19. The corrected
  check uses namespaced letter-prefixed tags. A second overbroad delimiter
  check treated the entire historical fixed-cycle source as newly structured
  content; the corrected check audits the added diff plus the untracked
  dossier and passes. Final hygiene then found an agent-generated
  `__pycache__` inside the new dossier; that cache was removed and the
  ten-file BOM/NUL/final-newline/cache audit passed. None of these checks
  exposed a source or theorem defect.
- **Interpretation:** no production, test, schema, artifact, or repository
  regression was detected.
- **Limitations:** hosted CI was not inspected; existing tests do not prove
  the new all-\(m\) theorem.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---authoritative-synchronization-and-regressions.

## EV-006 - Final Review

- **Date:** 2026-07-18
- **Method or command:** three independent read-only audits of proof algebra,
  shortcut-role completeness, diagnostic independence and counting, K825
  specialization, cross-file synchronization, scope, and Markdown; complete
  tracked and untracked diff inspection.
- **Relevant output:** the proof audit initially found that positivity, but
  not the claimed exact \(q=2\) minimum, had been established for generic
  high-middle and \(L\) roles. The final proof adds sharp comparisons for
  high-middle roles, \(L\), endpoint-hole arcs, \(q=3\), and \(q\ge4\);
  all reviewers then returned PASS with no residual finding. A separate DP
  audit also cross-checked small artificial orders and direct arc
  recompression.
- **Interpretation:** the exact theorem, computation, summaries, limitations,
  and intended ten-file scope are READY_FOR_REVIEW.
- **Limitations:** user review and commit are manual; no Git staging or commit
  was performed.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---final-audits-and-ready-for-review.
