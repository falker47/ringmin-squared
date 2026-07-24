# EVIDENCE - TASK-20260723 / KR1G Distinct Original-Edge Residual

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and scope isolation | repository sources; Git | PASS |
| EV-002 | proof / computation | General finite theorem and exact ordered-limit coefficient | `research/FIXED_ORDER_CYCLE_RATIO.md` | PASS |
| EV-003 | code / computation | Independent exact checker with nonequality histories | `exact_checker.py` | PASS |
| EV-004 | test / audit | Repository and final diff verification | repository commands | PASS |

## EV-001 - Startup and source isolation

- **Date:** 2026-07-23
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, the relevant
  authoritative KR1G proof, and prior dossiers; run
  `git status --short --branch` and `git rev-parse --short HEAD`.
- **Relevant output:** startup worktree was clean on
  `main...origin/main` at `9160631`.
- **Interpretation:** no unrelated uncommitted work was mixed into the task.
  The equality theorem and all-middle tuple were the accepted starting
  points.
- **Limitations:** this establishes local source state, not hosted CI state.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---strict-startup-and-scope-isolation`.

## EV-002 - Distinct original-edge residual theorem

- **Date:** 2026-07-23
- **Method or command:** exact algebra from the cycle-sum identity and
  KR1G-6; piecewise completion of the square in
  \(x=\sqrt{2mU}\); independent read-only review by three agents; exact
  SymPy simplification of \(\mu_\infty\), the denominator, and
  \(C_{\rm dist}\).
- **Relevant output:** all reviews report `PASS` and no counterexample.
  The exact finite bounds are KR1G-83--KR1G-85. The fixed-\(k\) coefficient
  is \(\tau_k^2/(\chi_k+2\mu_k)\), and the subsequent exact limit is
  \[
  C_{\rm dist}
  =
  \frac{2833-1968\sqrt2}
  {12167[
  2(18-\sqrt2)\log(2-\sqrt2/2)+4+10\sqrt2]}
  =0.000153593551798992409046805037317\ldots.
  \]
  Exact positivity uses
  \(2833^2-2\cdot1968^2=279841>0\) and a positive denominator.
- **Interpretation:** this is an exact theorem for every history in the
  declared distinct-original-edge class at each eventual fixed-\(k\)
  all-middle row. \(C_{\rm dist}\) is the exact limit of the optimized
  lower-bound coefficients, not the exact history infimum.
- **Limitations:** selected recursive splits and geometric consequences are
  excluded. No inner or outer ordinary-limit existence is proved.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---general-finite-theorem-and-ordered-asymptotics`.

## EV-003 - Bounded independent exact checker

- **Date:** 2026-07-23
- **Method or command:**
  `python ops\TASK-20260723__kr1g_distinct_original_edge_residual\exact_checker.py`
- **Relevant output:** `PASS: 2956 canonical cycles, 255975 broad target
  pairs, 1103715 broad histories (1103135 nonequality), plus 13440
  two-segment completion histories (12768 nonequality); full residual, exact
  radical chain, optimized bound, combined Cauchy, and completion DP all
  pass`. The named inactive golden has residual \(8/3\) and optimized bound
  \(4/15\). The named active-radical golden has residual \(717/140\) and
  optimized bound \(13778/7035\).
- **Interpretation:** the standard-library checker enumerates every cycle,
  target subset, and assignment for \(3\le q\le8\) and
  \(1\le\ell<\lceil q/2\rceil\), with no equality filter. The separate
  fixture exhausts every two-label completion and agrees with an independent
  memoized DP.
- **Limitations:** bounded exact enumeration corroborates but does not prove
  the all-\(q\) or asymptotic theorem. Its rational weights are synthetic,
  not rounded irrational all-middle weights.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---independent-exact-nonequality-checker`.

## EV-004 - Repository and final diff verification

- **Date:** 2026-07-24
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  final checker and Ruff commands from EV-003; exact SymPy identities;
  equation-tag, Markdown-display, aligned-environment, local-link, UTF-8/LF,
  trailing-whitespace, complete tracked/untracked source, Git status, and
  `git diff --check` audits.
- **Relevant output:** 283 tests pass in 70.28 seconds; all four checked
  artifacts pass with 76 local brackets and summary rows \(3,4,5,6\); all
  four focused schema tests pass. The final checker passes all 1,117,155
  histories, including 1,115,903 nonequality histories, and Ruff lint and
  format pass. All 1,053 equation tags are unique; authoritative-proof
  displays balance 1,689/1,689 and aligned environments 204/204; all 45
  local file links resolve and the new roadmap anchor matches its heading;
  all eight changed text/code files are strict UTF-8 without BOM or CR and
  end in LF. Exact symbolic coefficient and scalar-square identities reduce
  to zero, the positive margin is \(279841\), no changed line has trailing
  whitespace, and final Git diff checks pass.
- **Interpretation:** the proof, stable memory, roadmap, status, checker, and
  unchanged production verification layer are consistent. The bounded task
  is `READY_FOR_REVIEW`.
- **Limitations:** regression and bounded exact enumeration do not replace
  the symbolic all-\(q\) theorem or prove the exact history infimum.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-24---repository-verification-and-final-handoff`.
