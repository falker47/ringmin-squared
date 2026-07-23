# EVIDENCE - TASK-20260723 / KR1G Equality Full Residual

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources / Git | PASS |
| EV-002 | exact theorem | Complete residual on every positive-branch equality family | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Independent complete-residual checker | `exact_checker.py` | PASS |
| EV-004 | regression / audit | Repository and final diff verification | commands / Git | PASS |

## EV-001 - Startup And Source Isolation

- **Date:** 2026-07-23
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, KR1G-1--KR1G-68,
  and the three preceding KR1G dossiers; inspect the exact oracles; run
  `git status --short --branch` and `git log -3 --oneline`.
- **Relevant output:** clean `main...origin/main` at `1370303`
  (`docs: classify KR1G relaxed equality families`).
- **Interpretation:** STRICT startup and bounded-task isolation pass.
- **Limitations:** source inspection alone does not prove the new theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---strict-startup-and-scope-isolation`.

## EV-002 - Exact Full-Equality-Residual Theorem

- **Date:** 2026-07-23
- **Method or command:** exact specialization of KR1G-6; cycle
  deviation-sum identity; weighted Cauchy; fixed-parameter floor/ceiling
  limit; subsequent all-middle mesh limit; exact SymPy verification of the
  two integrals, logarithm ratio, closed coefficient, radical certificate,
  and square margin; two independent read-only mathematical reviews.
- **Relevant output:** KR1G-69--KR1G-73 prove
  \[
  P(C_0)+M_h-B_{h,n}
  \ge{[T_{k,n}-(c-\ell)]_+^2\over Q_{k,n}}
  \]
  for every equality pair, assignment, and completion. KR1G-74--KR1G-80
  prove
  \[
  \liminf_{k\to\infty}\liminf_{n\to\infty}
  {\min_h(P(C_0)+M_h-B_{h,n})\over n^3}
  \ge C_{\rm eq}
  =0.000859667403694594600649737486716\ldots
  >{786-473\sqrt2\over170338}>0.
  \]
  SymPy returns zero for every symbolic difference and the exact square
  margin is \(170338\). Both independent reviews report `PASS`.
- **Interpretation:** exact theorem. The complete residual is uniformly cubic
  on all positive-branch equality families at the unchanged all-middle
  cutoffs, in the required fixed-\(k\), \(n\), then \(k\) order.
- **Limitations:** the theorem does not give the exact infimum coefficient,
  prove ordinary-limit existence, or include a nonequality history.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---uniform-complete-residual-theorem`.

## EV-003 - Bounded Independent Exact Checker

- **Date:** 2026-07-23
- **Method or command:**
  `python -B
  ops\TASK-20260723__kr1g_equality_full_residual\exact_checker.py`;
  `python -m ruff check
  ops\TASK-20260723__kr1g_equality_full_residual\exact_checker.py`;
  `python -m ruff format --check
  ops\TASK-20260723__kr1g_equality_full_residual\exact_checker.py`;
  independent read-only checker review.
- **Relevant output:** 204,556 canonical cycles and 96,887 literal
  deletion checks discover 1,066 equality pairs without the old
  classification predicate. The one-segment sweep passes 17,188 assignments
  and 230,252 complete histories. The two-segment fixture passes 192
  assignments and 21,120 histories. Every direct complete residual,
  base-slack identity, full KR1G decomposition, finite square-center bound,
  literal completion minimum, independent DP minimum, and four \(q=10\)
  golden minima agree exactly. Final Ruff lint and format checks pass.
- **Failed-check record:** the first Ruff format check requested one
  mechanical reformat. `python -m ruff format` was applied; the checker
  returned identical counts and minima afterward, and the final format check
  passed.
- **Interpretation:** exact bounded computation with standard-library
  `Fraction` arithmetic and no project or earlier dossier import. It checks
  the full residual, not only the equality classification.
- **Limitations:** the rational fixtures are synthetic and finite. They do
  not realize the eventual irrational all-middle rows or replace the
  all-\(q\) and asymptotic proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---independent-exact-full-residual-checker`.

## EV-004 - Repository And Final Diff Verification

- **Date:** 2026-07-23
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  checker and Ruff commands from EV-003; equation-tag, Markdown-display,
  aligned-environment, UTF-8/LF, local-link, Git status, complete tracked and
  untracked diff, trailing-whitespace, and `git diff --check` audits.
- **Relevant output:** 283 tests pass in 74.58 seconds; all four checked
  artifacts pass with 76 local brackets and summary rows \(3,4,5,6\); all
  four focused schema tests pass. The final hardened checker passes all
  251,372 histories and Ruff passes. All 1,045 equation tags are unique;
  standalone displays balance 1,668/1,668 and aligned environments
  201/201; all 43 local links resolve; all eight changed text/code files are
  strict UTF-8 without BOM or CR and end in LF; no changed line has trailing
  whitespace; the complete tracked diff and untracked dossier were
  inspected; `git diff --check` passes.
- **Interpretation:** the proof, stable memory, checker, dossier, and
  unchanged production verification layer are consistent. The task is
  `READY_FOR_REVIEW`.
- **Limitations:** regression, bounded enumeration, and source review do not
  replace the symbolic all-\(q\) theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---repository-verification-and-final-handoff`.
