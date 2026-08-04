# EVIDENCE - TASK-20260804 / KR1G Variable Recursive Count

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources; Git | PASS |
| EV-002 | proof / audit | Variable-count theorem and order-statistic asymptotic | authoritative proof | PASS |
| EV-003 | code / computation | Focused exact order-statistic checker | `exact_checker.py` | PASS |
| EV-004 | test / regression | Repository and prior KR1G regressions | repository commands | PASS |
| EV-005 | source / diff audit | Final documentation and diff verification | changed files; Git | PASS |

## EV-001 - Startup and source isolation

- **Date:** 2026-08-04
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, KR1G-69--KR1G-101,
  and the fixed-count dossier; run `git status --short --branch`,
  `git rev-parse HEAD`, and targeted `rg` source searches.
- **Relevant output:** baseline
  `6e5ea239ae06277a836b64253a07f36379bf7a7d`; startup worktree clean; the
  only asymptotic use of fixed \(p\) is after KR1G-99.
- **Interpretation:** the bounded STRICT task starts without unrelated local
  changes and can extend KR1G-98 in place.
- **Limitations:** this is source isolation, not proof or test evidence.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---strict-startup-and-variable-count-isolation`.

## EV-002 - Variable-count proof and order-statistic asymptotic

- **Date:** 2026-08-04
- **Method or command:** exact derivation from KR1G-98; finite denominator
  identity; threshold representation of lower order statistics; literal
  floor/ceiling Riemann convergence at each fixed \(k\); exact cellwise
  comparison with the refining linear profile; two independent read-only
  mathematical audits.
- **Relevant output:** KR1G-102--KR1G-113 prove that, whenever one common
  \(\sigma\in(0,1]\) satisfies
  \(\liminf_n b^{\rm base}_{k,n}/\ell_{k,n}\ge\sigma\) for every fixed
  \(k\), every declared history obeys
  \[
  \mathscr R_{k,n}(h)\ge
  {\mathsf L_{k,n}(b^{\rm base}_{k,n})^2\over Q_{k,n}+2m},
  \]
  where \(\mathsf L\) is exactly the sum of the indicated number of smallest
  \(d_t\)'s. The fixed-\(k\) limit is the lower rearranged integral
  \(\Phi_k(\sigma)\), and
  \(\Phi_k(\sigma)\to2\sigma^2E^2\). Thus the nested lower bound is
  \(\sigma^4C_{\rm dist}\).
- **Interpretation:** the target coefficient is correct for the requested
  order-statistic numerator and uniform \(Q+2m\) denominator relaxation.
  Fixed \(p\) and \(p=o(n)\) recover \(C_{\rm dist}\) at \(\sigma=1\).
- **Limitations:** this does not optimize correlations retained by the exact
  KR1G-98 denominator or discarded recursive terms, and proves no exact
  residual infimum, discrete attainment, geometry, \(k=k(n)\), or diagonal
  limit. The only count regime not covered is
  \(\liminf b^{\rm base}/\ell=0\).
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---variable-count-theorem-and-coefficient-audit`.

## EV-003 - Focused exact order-statistic checker

- **Date:** 2026-08-04
- **Method or command:**
  `python ops\TASK-20260804__kr1g_variable_recursive_count\exact_checker.py`;
  `python -m ruff check
  ops\TASK-20260804__kr1g_variable_recursive_count\exact_checker.py`;
  `python -m ruff format --check
  ops\TASK-20260804__kr1g_variable_recursive_count\exact_checker.py`.
- **Relevant output:** the checker reports two rational fixtures, 16 total
  coordinate subsets, crossover sums
  \((12/7,228/35,438/35)\), a genuine two-minimizer tie, and uniform first
  bound \(90/511\). The exact rounded all-middle row \((k,n)=(3,200)\)
  has \(r=88\), cutoffs \((86,83,80)\), \(\ell=8\), increasing order
  \((82,81,80,85,84,83,87,86)\), and all 256 subsets pass. The limiting
  midpoint profile passes at \(\sigma=1/4,1/2,3/4,1\), with numerator
  factor \(\sigma^2\) and squared factor \(\sigma^4\). The checker prints
  PASS; Ruff reports `All checks passed!` and `1 file already formatted`.
- **Interpretation:** exact independent arithmetic corroborates the finite
  order-statistic identity, denominator relaxation, rounding, and density
  exponent.
- **Limitations:** the checker is bounded and audits the enlarged coordinate
  relaxation. It does not enumerate compatible histories, prove the
  asymptotic theorem, or assert discrete residual attainment.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---focused-exact-order-statistic-checker`.

## EV-004 - Repository and prior KR1G regressions

- **Date:** 2026-08-04
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `python -m pytest tests\test_n3_arb_interval_crosscheck.py -p
  no:cacheprovider`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; fixed-\(p=2\) and historical
  one-recursive exact checker commands.
- **Relevant output:** 283 tests pass in 69.14 seconds; 3 focused Arb tests
  and 4 focused schema tests pass; 4 checked artifacts and 76 local brackets
  verify with summary rows \(3,4,5,6\). The fixed-count checker passes
  15,120 selected prefixes, 151,200 completions, its 42-prefix/4,620-
  completion Bellman fixture, and 1,296 position-sweep histories. The
  one-recursive checker passes 96,600 broad histories and 6,720 arbitrary
  completions.
- **Interpretation:** the documentation/checker extension is compatible with
  the unchanged production and certification layer and the earlier recursive
  finite theorems.
- **Limitations:** finite regressions corroborate but do not replace the new
  symbolic asymptotic proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---repository-and-recursive-history-regressions`.

## EV-005 - Final documentation and diff verification

- **Date:** 2026-08-04
- **Method or command:** exact equation-tag uniqueness audit; strict UTF-8,
  BOM, CR/LF, final-LF, trailing-whitespace, and display-environment audit;
  targeted local-link/anchor resolution; `git status --short --branch`;
  complete `git diff --color=never`; `git diff --stat`; and
  `git diff --check`.
- **Relevant output:** all 1,080 equation tags are unique, including 115
  KR1G tags. All eight changed text/code files are strict UTF-8 without BOM
  or CR, end in LF, contain no trailing whitespace, and have balanced display,
  `aligned`, `array`, and `cases` delimiters. All ten new local targets and
  anchor sources resolve. The complete proof/memory/roadmap/status diff and
  every new dossier file were inspected; `git diff --check` passes.
- **Interpretation:** authoritative proof, stable memory, roadmap, current
  status, task evidence, and checker are internally aligned, and the task is
  ready for manual review.
- **Limitations:** Git does not include untracked files in ordinary diff
  output, so the four new dossier files were inspected directly as well.
  Hosted CI cannot cover this uncommitted working tree.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---final-documentation-and-review-handoff`.
