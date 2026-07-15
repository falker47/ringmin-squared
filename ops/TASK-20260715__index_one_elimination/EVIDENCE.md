# EVIDENCE - TASK-20260715__index_one_elimination / Exact Index-One Elimination

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection | Clean startup and bounded scope | authoritative sources and read-only probes | PASS |
| EV-002 | proof / review | Exact index-one elimination and consequences | proof note and independent audit | PASS |
| EV-003 | exact computation / test | All core orders and insertions for `n=3..8` | focused test module | PASS |
| EV-004 | verification / hygiene | Full suite, artifact guard, lint, diff review | repository checks | PASS |

## EV-001 - Startup And Scope

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the previous task dossier,
  proof note, roadmap, source scorer, product-distance canonical enumerator,
  tests, and dossier templates; inspected `git status`, `git log`, and the
  current diff read-only.
- **Relevant output:** `main...origin/main` with no changed paths; current
  `HEAD` is `9f1239e Prove one-wrap saturation of cyclic ratio`.
- **Interpretation:** The previous task is durably committed and this bounded
  task can proceed without mixing unrelated work.
- **Limitations:** No mathematical theorem or finite regression is established
  by startup inspection alone.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-scope`

## EV-002 - Exact Elimination And Consequences

- **Date:** 2026-07-15
- **Method:** Combined the accepted induced-subset characterization of
  \(\Lambda\) with a complete classification of subsets containing label
  `1`; then applied the already-proved same-order product-distance comparison.
- **Relevant result:** Subsets avoiding `1` preserve their score;
  \(\{1\}\) gives `1<4`; \(\{1,j\}\) gives \(2j\le j^2\); and deleting
  `1` between distinct selected core neighbors \(a,b\) raises the score by
  \(ab-a-b=(a-1)(b-1)-1\ge1\). Therefore
  \[
  \Lambda(\sigma)=K(\tau),
  \quad
  \Lambda_n=\min_\tau K(\tau),
  \quad
  \Lambda_n\le(n-1)W_n,
  \quad
  R_2^*(n)<{\Lambda_n\over\pi}\le{(n-1)W_n\over\pi}.
  \]
- **Independent review:** mathematical and test-design audits independently
  recovered the proof, the non-strict `W` comparison, the strict geometric
  chain, and the `n=3` degeneracy; no proof gap was reported.
- **Classification:** EXACT THEOREM for every `n>=3`.
- **Limitations:** No statement is made that \(\rho_\sigma\) is independent of
  insertion, that \(K=W\), or that the geometric upper bound is attained.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---exact-elimination-and-consequences`

## EV-003 - All-Core All-Insertion Regression

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3; exact
  integer/`Fraction` arithmetic.
- **Method:** For every canonical core order on `n=3..8`, evaluated literal
  nonempty-subset score \(K\), inserted label `1` into every cyclic gap,
  compared literal full-subset scoring and the production Karp scorer with
  \(K\), and checked that canonicalized insertions equal the full canonical
  order space. Also checked \(K(\tau)\le(n-1)W(\tau)\) exactly.
- **Relevant output:** 437 core classes, 2,957 insertion trials, and 2,956
  distinct complete classes all pass. Minima are
  `(12,26,47,77,118,172)`; core minimizer counts are
  `(1,1,1,3,4,12)` and complete counts are `(1,3,4,15,24,84)`. For `n=3`,
  `(3,1,2)` and `(3,2,1)` both score `12` and canonicalize to `(3,1,2)`.
- **Command:**
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py`
- **Relevant test output:** `25 passed in 12.91s`; targeted Ruff reports
  `All checks passed!`.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** This is finite implementation evidence, not the proof of
  the all-order theorem. The production domain remains `n<=8`.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---all-core-all-insertion-regression`

## EV-004 - Complete Verification And Handoff

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3.
- **Commands:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider`
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  - `$env:PYTHONPATH='src'; python -m ruff check tests/test_fixed_order_cycle_ratio.py`
  - `python -m compileall -q tests/test_fixed_order_cycle_ratio.py`
  - `python --version`
  - `git status --short --branch`, `git diff`, and `git diff --check`
- **Relevant output:** full pytest reports `198 passed in 66.36s`; checked
  artifact verification reports `certificates=4`, `local_brackets=76`, and
  accepts `examples/finite_results_summary_n3_n6.json`; targeted Ruff reports
  `All checks passed!`; compilation and diff whitespace checks pass.
- **Independent review:** proof, test, and documentation audits accept the
  final theorem, all edge cases, strictness, bounded coverage, exact counts,
  evidence classifications, and unchanged certification boundary. The
  documentation audit prompted five clarity/status refinements; reinspection
  found no mathematical defect.
- **Final diff scope:** only proof/research documentation, the test module,
  project memory/status, and this dossier changed. No production source,
  backend, verifier, certificate, checked artifact, schema, example, CLI, or
  enumeration limit changed.
- **Interpretation:** implementation, documentation, and durable handoff are
  locally verified and ready for manual review.
- **Limitations:** hosted Python 3.11-3.13 CI was not run. Python 3.11
  compatibility of the new test-only syntax was source-inspected, not locally
  executed. Artifact verification is a non-regression check and does not
  strengthen the guarded interval-backend trust contract.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---complete-verification-and-handoff`
