# EVIDENCE - TASK-20260718 / Canonical 8/25 Core-Order K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup, domain, and clean-tree audit | repository sources and Git | PASS |
| EV-002 | exact theorem | Shortcut-budget proof and exact block sum | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Independent max-plus and shortcut audit | `exact_diagnostic.py` | PASS |
| EV-004 | source inspection | Authoritative synchronization | seven Markdown sources | PASS |
| EV-005 | tests / checks | Final repository verification | commands below | PASS |
| EV-006 | review | Final diff and independent audits | Git diff / read-only agents | PASS |

## EV-001 - Startup And Scope

- **Date:** 2026-07-18
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the prior construction dossier,
  construction/scorer sources and tests; ran `git status --short --branch`
  and `git rev-parse HEAD`.
- **Relevant output:** clean `main...origin/main`; HEAD
  `1ec6e0b7fca85b9ed1bb81636c87934564994e97`.
- **Interpretation:** safe STRICT startup; public construction domain is every
  n>=9 and includes fourteen explicit rows outside the symbolic inequality.
- **Limitations:** read-only scope audit; no mathematical conclusion by itself.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---strict-startup-and-domain-audit`.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-18
- **Method or command:** exact algebra using the block parameters d,v,e,t,
  epsilon,r; isolated-hole deletion gains; compressed-path shortcut margins;
  direct summation of induced block edges.
- **Relevant output:** (K825-2) uniquely classifies the symbolic maximizer;
  (K825-4) gives exact K; the fourteen-row table covers the remaining public
  domain; (K825-20) gives K=143 n^3/500+O(n^2).
- **Interpretation:** exact all-domain, construction-specific theorem. It
  sharpens the global upper coefficients but does not identify global
  minimizers or an exact geometric leading constant.
- **Limitations:** the ten r=0 rows, n=47 inequality exception, and fourteen
  fixed public orders use displayed finite local margin certificates; no
  subset or permutation enumeration is used.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---exact-backbone-theorem-derived`.

## EV-003 - Bounded Exact Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python ops/TASK-20260718__canonical_eight_twenty_fifths_k/exact_diagnostic.py`
- **Relevant output:**

  ```text
  canonical 8/25 K diagnostic: PASS
  rows: 112 (n=9..120)
  symbolic rows: 98; explicit rows: 14
  max-plus transitions: 8495284
  oriented shortcut arcs: 561568
  shortcut-certificate rows: 112
  hard-coded shortcut anchor rows: 25
  formula-only tail rows: 880
  leading coefficient: 143/500
  ```

- **Interpretation:** independently corroborates exact values, uniqueness,
  formula, and shortcut conditions on a bounded interval.
- **Corrected failures:** the first run used `zip(strict=True)` on adjacent
  unequal-length path slices; after removing that diagnostic-only misuse it
  passed. The first Ruff format check requested one mechanical reformat; the
  final lint and format checks pass.
- **Limitations:** bounded computation is not the source of the infinite
  symbolic proof. The DP optimizes increasing paths and does not enumerate
  subsets; no permutation search occurs.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---bounded-independent-diagnostic-passed`.

## EV-004 - Authoritative Synchronization

- **Date:** 2026-07-18
- **Method or command:** source inspection and cross-reference audit across
  `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/ALL_N_LOWER_BOUND.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md`.
- **Relevant output:** all seven sources distinguish the exact
  regular-direction limit `W_n/n^2 -> 8/25` from the sharper current upper
  coefficients `143/500` and `143/(500*pi)`; symbolic and fourteen-row domains
  are stated separately.
- **Interpretation:** historical product-distance coefficient 8/25 remains
  exact for W, while 143/500 is the new current upper coefficient for Lambda
  and the variable-spacing geometric sandwich.
- **Limitations:** historical append-only dossiers are not rewritten.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---authoritative-synchronization-in-progress`.

## EV-005 - Final Repository Verification

- **Date:** 2026-07-18
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `python -m power_ringmin.verify_checked_artifacts`;
  `python -m pytest -p no:cacheprovider
  tests/test_checked_artifact_schema_validation.py`; the EV-003 diagnostic;
  `python -m ruff check` and `python -m ruff format --check` on the diagnostic;
  strict source-structure one-liners; `git diff --check`.
- **Relevant output:** pytest `283 passed in 70.62s`; artifact verification
  `certificates=4 local_brackets=76 summary_n_values=3,4,5,6`; schema
  `4 passed`; diagnostic PASS; Ruff PASS; source structure PASS for 10 paths,
  421 unique primary tags, and all 26 K825 tags; LaTeX environments PASS;
  final diff check has no output.
- **Corrected failures:** an initial bare `python verify.py` invocation failed
  because that standalone fixed-order CLI requires `--input` or `--order`;
  the appropriate aggregate checked-artifact command above passes. An initial
  structural one-liner was defeated by PowerShell backtick/regex escaping;
  the corrected strict command passes. A post-handoff EOF check initially
  assumed CRLF endings although the repository uses LF; the corrected
  newline-agnostic check passes. None of these checker/invocation failures
  exposed a source, theorem, artifact, or production defect.
- **Interpretation:** the requested theorem, local corroboration, and existing
  repository behavior verify together.
- **Limitations:** hosted CI was not inspected; bounded computation remains
  corroborative rather than the source of the all-parameter proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---regressions-audits-and-ready-for-review`.

## EV-006 - Final Review

- **Date:** 2026-07-18
- **Method or command:** three independent read-only audits of proof algebra,
  shortcut-role completeness, diagnostic independence, domain/sandwich
  consistency, and authoritative wording; complete tracked and untracked diff
  inspection; final status and `git diff --check`.
- **Relevant output:** reviewers found two material transcription/scope issues:
  the all-endpoint `n=47` four-edge minimum is 1446, and (K825-2)--(K825-4)
  apply only to symbolic rows. Both were corrected and re-audited. No further
  issue remains; the final intended scope is seven authoritative Markdown
  files plus one four-file dossier.
- **Interpretation:** exact theorem, evidence, limitations, and protected-path
  scope are READY_FOR_REVIEW.
- **Limitations:** user review and commit are manual; no Git staging or commit
  was performed.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-18---regressions-audits-and-ready-for-review`.
