# EVIDENCE - TASK-20260723 / KR1G Equality Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources / Git | PASS |
| EV-002 | exact theorem | Equality classification and universal selected-prefix barrier | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Independent \(q\le10\) classification oracle | `equality_oracle.py` | PASS |
| EV-004 | regression / audit | Repository and final diff verification | commands / Git | PASS |

## EV-001 - Startup And Source Isolation

- **Date:** 2026-07-23
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, CR28ax,
  CR28dr--CR28dw, CR28dw1--CR28dw12, KR1G-1--KR1G-43, and both preceding
  KR1G dossiers; run `git status --short --branch` and inspect relevant
  source paths.
- **Relevant output:** clean `main...origin/main` at `0c70dec`.
- **Interpretation:** STRICT startup and bounded-task isolation pass.
- **Limitations:** source inspection alone does not prove the new theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---strict-startup-and-task-isolation`.

## EV-002 - Exact Equality And Selected-Prefix Theorem

- **Date:** 2026-07-23
- **Method or command:** simultaneous equality audit of KR1G-25; contraction
  of the forced complementary matching; exact chronological convex
  weighting; centered connector-slot identity; endpoint-sum cancellation;
  weighted square rearrangement; fixed-parameter Riemann limit; exact
  quadratic-surd sign margins; exact SymPy checks of the finite identity,
  antiderivative, endpoint integral, logarithmic closed form, and square
  margins; two independent read-only mathematical reviews.
- **Relevant output:** KR1G-44--KR1G-50 give the iff and signed-block
  classification. KR1G-51--KR1G-58 give the exact assignment-uniform finite
  prefix bound. KR1G-59--KR1G-68 prove, with fixed \(k\), then
  \(n\to\infty\), then \(k\to\infty\),
  \[
  \liminf_{k\to\infty}\liminf_{n\to\infty}
  {\min M_h\over n^3}
  \ge I(E)
  \ge {787-551\sqrt2\over73002}>0.
  \]
  The exact algebra command returns zero for the finite summand identity,
  the derivative and initial value of the closed form for \(I(D)\), the
  endpoint integral, its logarithm argument, and both closed-form
  coefficients. The three square margins are respectively
  \(4761\), \(170338\), and \(12167\). Both independent reviews report
  `PASS`.
- **Interpretation:** exact theorem. At each fixed all-middle KR1G cutoff,
  every relaxed-minimum equality family and every selected-edge assignment
  already forces a cubically positive correction prefix. An arbitrary later
  completion cannot erase an attained prefix maximum.
- **Limitations:** the theorem concerns relaxed-minimum equality families and
  their selected correction prefixes. It does not classify non-equality
  histories or evaluate the complete KR1G residual.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---symbolic-equality-and-prefix-classification`.

## EV-003 - Bounded Exact Classification Oracle

- **Date:** 2026-07-23
- **Method or command:**
  `python -B
  ops\TASK-20260723__kr1g_equality_classification\equality_oracle.py`;
  `python -m ruff check
  ops\TASK-20260723__kr1g_equality_classification\equality_oracle.py`;
  `python -m ruff format --check
  ops\TASK-20260723__kr1g_equality_classification\equality_oracle.py`;
  independent read-only oracle review.
- **Relevant output:** all 204,556 canonical cycles, 20 positive-branch rows,
  815,188 cycle minima, 720 equality-cycle rows, 1,066 equality pairs, and
  173,819 literal deletion subsets pass. The cycle-by-cycle binomial formula,
  signed interval components, complementary-matching cycle count, and
  bad-edge histograms agree exactly. Ruff lint and format pass; the
  independent review reports `PASS`.
- **Failed-check record:** the first Ruff format check requested one
  mechanical reformat. `python -m ruff format` was applied, after which the
  oracle returned the same mathematical counts and the final format check
  passed.
- **Interpretation:** exact bounded computation using only standard-library
  integers, with no project or test import, independently corroborates the
  symbolic classification.
- **Limitations:** finite enumeration can corroborate only the classification
  for \(q\le10\); it cannot prove either all-\(q\) structure or the
  asymptotic prefix theorem.

## EV-004 - Repository And Final Diff Verification

- **Date:** 2026-07-23
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  the oracle and Ruff commands from EV-003; equation-tag, Markdown-display,
  aligned-environment, UTF-8/LF, local-link, Git status, complete-diff, and
  whitespace audits.
- **Relevant output:** 283 tests pass in 70.47 seconds; all four checked
  artifacts pass with 76 local brackets and summary rows \(3,4,5,6\); all
  four focused schema tests pass; all 1,033 equation tags are unique;
  standalone displays balance \(1578/1578\), aligned environments balance
  \(194/194\), all eight changed text/code files are strict UTF-8 without BOM
  or CR and end in LF, all new local links resolve, the complete tracked diff
  and untracked dossier were inspected, no changed line has trailing
  whitespace, and `git diff --check` passes.
- **Failed-check record:** the read-only Git status/diff audit emits the known
  sandbox warning for the inaccessible user-level global ignore file, but
  returns the complete repository-local status and diff successfully.
- **Interpretation:** the proof, memory, oracle, dossier, and unchanged
  production verification layer are consistent. The task is
  `READY_FOR_REVIEW`.
- **Limitations:** regression, bounded enumeration, and source review do not
  replace the symbolic all-\(q\) theorem.
