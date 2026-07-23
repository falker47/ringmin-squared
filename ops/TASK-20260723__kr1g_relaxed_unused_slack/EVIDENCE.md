# EVIDENCE - TASK-20260723 / KR1G Relaxed Unused Slack

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources / Git | PASS |
| EV-002 | exact theorem | Relaxed unused-original-edge minimum | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Independent exhaustive oracle | `exact_oracle.py` | PASS |
| EV-004 | regression / audit | Repository and final diff verification | commands / Git | PASS |

## EV-001 - Startup And Source Isolation

- **Date:** 2026-07-23
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, CR28ax, the KR1G
  proof and prior dossier; run `git status --short --branch` and
  `git log -1 --oneline`.
- **Relevant output:** clean `main...origin/main` at
  `cb9c8ff29db9a42da558c776a3b728ca6f2a6f6e`.
- **Interpretation:** STRICT startup and bounded-task isolation pass.
- **Limitations:** source inspection alone does not prove the new theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---strict-startup-and-task-isolation`.

## EV-002 - Exact Relaxed Slack Theorem

- **Date:** 2026-07-23
- **Method or command:** exact matching count, parity-explicit zigzag
  construction, floor/ceiling inequalities, and compatible-history
  projection/lift in KR1G-23--KR1G-33.
- **Relevant output:** for \(q\ge3\), \(\ell\ge1\),
  \[
  \mathfrak U(q,\ell)
  ={1\over2}\left[\left\lceil{q\over2}\right\rceil-\ell\right]_+.
  \]
  With the requested \(a,b,r,s\), for every \(n\ge25\),
  \[
  \mathfrak U_n
  ={2+5\sqrt2\over92}n+O(1),
  \qquad
  {\mathfrak U_n\over n^3}\longrightarrow0.
  \]
- **Interpretation:** exact theorem. The same value is the sharp uniform
  history minimum of the unused-edge term alone. The full history residual
  retains separate uncontrolled nonnegative terms.
- **Limitations:** no full-residual tightness, global coefficient
  improvement, minimizing-order claim, growing-prefix theorem, or geometric
  consequence follows.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---compatible-history-scope`.

## EV-003 - Bounded Exact Oracle

- **Date:** 2026-07-23
- **Method or command:**
  `python -B ops\TASK-20260723__kr1g_relaxed_unused_slack\exact_oracle.py`;
  `python -m ruff check
  ops\TASK-20260723__kr1g_relaxed_unused_slack\exact_oracle.py`;
  `python -m ruff format --check
  ops\TASK-20260723__kr1g_relaxed_unused_slack\exact_oracle.py`.
- **Relevant output:** for every \(3\le q\le10\), all Hamiltonian cycles were
  enumerated once modulo rotation and reversal and every
  \(1\le\ell\le q\) was optimized. All 204,556 canonical cycles, 52 exact
  \((q,\ell)\) minima, and every zigzag deletion profile pass. Ruff lint and
  format checks pass.
- **Interpretation:** exact bounded computation using only standard-library
  integers and `Fraction`, with no production or test import, independently
  corroborates the matching proof and explicit construction.
- **Failed-check record:** the standalone `ruff` executable was not on
  `PATH`; the repository-supported `python -m ruff` commands passed.
- **Limitations:** finite enumeration does not replace the symbolic all-\(q\)
  theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---independent-exact-oracle`.

## EV-004 - Repository And Final Diff Verification

- **Date:** 2026-07-23
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  the oracle and Ruff commands from EV-003; exact equation-tag,
  Markdown-display, aligned-environment, UTF-8/LF, local-link, Git status,
  complete-diff, and whitespace audits.
- **Relevant output:** 283 tests pass in 75.57 seconds; all four checked
  artifacts pass with 76 local brackets and summary rows \(3,4,5,6\); all
  four focused schema tests pass; Ruff lint and format pass; all 998 equation
  tags in the proof note are unique; standalone displays balance
  \(1911/1911\), aligned environments balance \(190/190\), all eight changed
  text/code files are strict UTF-8 without BOM or CR and end in LF, all new
  local links resolve, the complete diff and untracked files were inspected,
  and `git diff --check` passes.
- **Failed-check record:** the read-only Git status/stat audit emitted a
  sandbox permission warning for the user-level global ignore file, but
  returned the complete repository status successfully with exit code zero.
- **Interpretation:** the proof, memory, task-local oracle, and repository
  regressions are consistent. The bounded task is `READY_FOR_REVIEW`.
- **Limitations:** regression and bounded enumeration do not replace the
  symbolic theorem or control the complete compatible-history residual.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---final-verification-and-handoff`.
