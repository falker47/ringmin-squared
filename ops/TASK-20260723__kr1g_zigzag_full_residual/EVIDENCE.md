# EVIDENCE - TASK-20260723 / KR1G Zigzag Full Residual

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources / Git | PASS |
| EV-002 | exact theorem | Cubic lower bound on the complete zigzag-class residual | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Independent exhaustive history checker | `exact_checker.py` | PASS |
| EV-004 | regression / audit | Repository and final diff verification | commands / Git | PASS |

## EV-001 - Startup And Source Isolation

- **Date:** 2026-07-23
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, CR28dr--CR28dw,
  CR28dw1--CR28dw12, KR1G-1--KR1G-33, and both preceding KR1G dossiers;
  run `git status --short --branch` and `git log -1 --oneline`.
- **Relevant output:** clean `main...origin/main` at
  `b76b91077bbc6637fb7d2ebb7a3058fafa77615a`
  (`docs: correct KR1G dossier provenance`).
- **Interpretation:** STRICT startup and bounded-task isolation pass.
- **Limitations:** source inspection alone does not prove the new theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---strict-startup-and-scope-isolation`.

## EV-002 - Zigzag-Class Cubic Lower Bound

- **Date:** 2026-07-23
- **Method or command:** exact completion DP, zigzag endpoint-sum
  classification, split-invariant induction, AM--GM correction bound, exact
  finite prefix sum, fixed-\(k\) floor/ceiling limit, and subsequent use of
  \(M_k\uparrow1/3\) in KR1G-34--KR1G-43.
- **Relevant output:** for every fixed \(k\),
  \[
  \liminf_{n\to\infty}
  {\min_h(P(C_0)+M_h-B_{h,n})\over n^3}
  \ge
  \delta_k
  ={(3a-1)^2\over32}
  \bigl(1+a-4(3a-1)M_k\bigr),
  \]
  and
  \[
  \liminf_{k\to\infty}\liminf_{n\to\infty}
  {\min_h(P(C_0)+M_h-B_{h,n})\over n^3}
  \ge {470-159\sqrt2\over73002}>0.
  \]
- **Interpretation:** exact theorem. A cubic lower bound holds for every
  connector choice, label assignment, and completion in the declared
  zigzag-base witness class. The zero alternative is excluded.
- **Limitations:** the theorem does not give the exact residual coefficient,
  prove existence of the outer limit, extend to arbitrary histories or base
  cycles, classify minimizing orders, improve \(C_{\rm AF}\), or imply a
  geometric result.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---separated-fixed-k-and-subsequent-k-limits`.

## EV-003 - Bounded Independent Exact Checker

- **Date:** 2026-07-23
- **Method or command:**
  `python -B
  ops\TASK-20260723__kr1g_zigzag_full_residual\exact_checker.py`;
  `python -m ruff check
  ops\TASK-20260723__kr1g_zigzag_full_residual\exact_checker.py`;
  `python -m ruff format --check
  ops\TASK-20260723__kr1g_zigzag_full_residual\exact_checker.py`.
- **Relevant output:** four rational fixtures exhaust 18,468 literal
  histories, including every target subset, every selected assignment, and
  every completion. All exact DP, KR1G decomposition, endpoint-sum,
  correction, finite-barrier, history-count, and golden-minimum checks pass.
  Exact \(\mathbb Q(\sqrt2)\) arithmetic checks \(k=1,\ldots,12\) and
  \(\delta_\infty=0.003357990789056161\ldots>0\).
- **Interpretation:** independent bounded exact computation corroborates the
  finite structure and scalar algebra without importing project code.
- **Failed-check record:** the initial Ruff format check requested one
  mechanical reformat; `python -m ruff format` was applied, after which the
  checker remained unchanged mathematically. The final format recheck is
  part of EV-004.
- **Limitations:** synthetic finite fixtures do not realize the eventual
  irrational cutoff rows and do not replace the proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---independent-exact-checker`.

## EV-004 - Repository And Final Diff Verification

- **Date:** 2026-07-23
- **Method or command:** rerun the checker and Ruff commands from EV-003;
  `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  independent proof and checker reviews; exact equation-tag,
  Markdown-display, aligned-environment, UTF-8/LF, local-link, Git status,
  complete-diff, and whitespace audits.
- **Relevant output:** the hardened checker passes all 18,468 histories and
  twelve exact scalar rows; Ruff lint and format pass; 283 tests pass in
  63.58 seconds; all four checked artifacts pass with 76 local brackets and
  summary rows \(3,4,5,6\); all four focused schema tests pass; both
  independent reviews report `PASS`; all 1,008 equation tags are unique;
  standalone displays balance \(1544/1544\), aligned environments balance
  \(190/190\), all changed text/code files are strict UTF-8 without BOM or
  CR and end in LF, both new local links resolve, the complete diff and
  untracked files were inspected, and `git diff --check` passes.
- **Interpretation:** the proof, memory, checker, and repository regressions
  are consistent. The bounded task is `READY_FOR_REVIEW`.
- **Limitations:** regression, finite enumeration, and peer review do not
  replace the symbolic theorem or promote its class-specific lower bound to
  an exact coefficient, an outer-limit existence theorem, arbitrary
  histories, minimizing orders, or geometry.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---final-verification-and-handoff`.
