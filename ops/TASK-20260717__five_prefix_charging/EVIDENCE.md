# EVIDENCE - Five-Prefix One-Use Charging

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | STRICT startup and task isolation | authoritative memory and Git | pass |
| EV-002 | exact theorem | Five-prefix one-use charging | `research/FIXED_ORDER_CYCLE_RATIO.md` | proved |
| EV-003 | exact computation | Five-split local-history oracle | `literal_oracle.py` | 15,120 pass |
| EV-004 | static check | Oracle lint and format | Ruff | pass |
| EV-005 | regression | Focused/full tests and artifact verification | pytest / verifier | pass |
| EV-006 | structure / failed check | Tags, delimiters, line endings, timeouts | source / commands | pass after correction |
| EV-007 | audit / scope | Independent proof, oracle, synchronization, and final diff audits | source / Git | pass |

## EV-001 - Startup And Isolation

- **Date:** 2026-07-17
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the relevant proof sections,
  prior dossier, and oracle; run `git status --short --branch`,
  `git rev-parse HEAD`, and `git log -1 --oneline`.
- **Relevant output:** clean `main` tracking `origin/main` at
  `1116b1274949475da8462994f296ebd22d0a7bf3`.
- **Interpretation:** verified task isolation; the four-prefix theorem and
  fixed-`k` simplex are the exact prior inputs.
- **Limitations:** this does not establish or refute the five-prefix theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---strict-startup-and-expected-delta`.

## EV-002 - Exact Five-Prefix Theorem

- **Date:** 2026-07-17
- **Method or command:** direct symbolic derivation from CR28ax--CR28bd and
  the literal-history invariant, recorded as CR28dr--CR28dw.
- **Relevant output:** six convex coefficients telescope to five disjoint
  segments; the base-split map is injective; the original edges have one
  canonical charged/unused partition; every recursive edge has an endpoint in
  the already-inserted frontier through all four boundaries. Therefore
  \[
  \begin{aligned}
  \gamma^{(r)}_{1,n}\ge{}&P_{r,n}
  +(r-s_1)F_{1,n}+(s_1-s_2)F_{2,n}+(s_2-s_3)F_{3,n}\\
  &+(s_3-s_4)F_{4,n}+(s_4-s_5)F_{5,n}.
  \end{aligned}
  \]
- **Interpretation:** exact finite method-specific theorem; no literal
  counterexample exists.
- **Limitations:** no coefficient optimization, finite rounding, result for
  six or more prefixes, \(k\to\infty\) passage, or geometric claim.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---exact-five-prefix-derivation`.

## EV-003 - Bounded Exact Five-Split Oracle

- **Date:** 2026-07-17
- **Method or command:**
  `python -B ops\TASK-20260717__five_prefix_charging\literal_oracle.py`.
- **Relevant output:** 15,120 histories and 15,120 distinct final cycles;
  base splits \((5,20,100,600,4200)\), recursive splits
  \((0,10,110,1080,10920)\), and inserted-pair splits
  \((0,0,10,180,2520)\). The used-base histogram is
  \(\{1:600,2:4800,3:7200,4:2400,5:120\}\). The five local floors sum to
  \(253523/1155\), and the checked lower bound is \(1541348/1155\).
- **Interpretation:** verified bounded exact computation. It exercises
  five simultaneous original-edge charges and deeply nested fifth splits.
- **Limitations:** finite corroboration, not the all-history proof; no project,
  production, or test helper is imported.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---standalone-exact-oracle`.

## EV-004 - Oracle Static Checks

- **Date:** 2026-07-17
- **Method or command:**
  `python -m ruff check ops\TASK-20260717__five_prefix_charging\literal_oracle.py`;
  `python -m ruff format --check ops\TASK-20260717__five_prefix_charging\literal_oracle.py`.
- **Relevant output:** `All checks passed!`; `1 file already formatted`.
- **Interpretation:** verified lint and format compliance.
- **Limitations:** static checks do not prove the mathematics.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---standalone-exact-oracle`.

## EV-005 - Repository Regression

- **Date:** 2026-07-17
- **Method or command:**
  `python -m pytest tests\test_fixed_order_cycle_ratio.py -q -p no:cacheprovider`;
  `python -m pytest -q -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  `python -m pytest tests\test_checked_artifact_schema_validation.py -q -p no:cacheprovider`.
- **Relevant output:** focused module pass with 101 collected tests; all 283
  local tests pass; verifier reports 4 certificates and 76 local brackets;
  schema regression reports 4 passes.
- **Interpretation:** verified regression and artifact semantic stability.
- **Limitations:** hosted GitHub Actions were not inspected.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---synchronization-and-regression`.

## EV-006 - Structural And Failed-Check Audit

- **Date:** 2026-07-17
- **Method or command:** exact equation-tag and Markdown-environment counts,
  UTF-8/BOM/newline inspection, `git diff --check`, and full-suite execution.
- **Relevant output:** 321 unique equation tags; standalone display lines,
  `aligned`, and `array` environments balance; all changed files are UTF-8
  without BOM, end in LF, and use LF consistently after normalizing one mixed
  `PROJECT_KNOWLEDGE.md` edit; `git diff --check` passes.
- **Failed checks retained:** the first full-suite command had an intentionally
  too-small five-second timeout and returned exit 124 before producing a test
  result; the immediate 66.7-second rerun passed all 283 tests. The first
  display check counted every `\\[` substring, including bracket escapes
  inside formulas, and failed with 576 versus 571; the corrected check counts
  only standalone delimiter lines and passes with 571 versus 571.
- **Interpretation:** both failures were diagnostic-command defects, not
  mathematical, test, or document failures.
- **Limitations:** source-structure checks do not replace proof review.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---synchronization-and-regression`.

## EV-007 - Independent Audits And Final Scope

- **Date:** 2026-07-17
- **Method or command:** three independent read-only audits of the proof,
  adversarial split histories/oracle arithmetic, and cross-source
  synchronization/scope; `git status --short`, complete `git diff`,
  `git diff --check`, UTF-8/newline inspection, and changed-path review.
- **Relevant output:** all audits pass after clarifying that the normalized
  simplex does not supply the independent five-prefix theorem and normalizing
  one mixed-line-ending edit. Proof identities, all 15,120 oracle histories,
  counts, formulas, summaries, and exclusions agree. Exactly one new `.py`
  file exists, the standalone dossier oracle.
- **Interpretation:** verified mathematical, computational, synchronization,
  formatting, and scope consistency; task is `READY_FOR_REVIEW`.
- **Limitations:** manual user review and commit decision remain; no hosted CI
  status was inspected.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---independent-audits-and-handoff`.
