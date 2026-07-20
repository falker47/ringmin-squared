# EVIDENCE - TASK-20260720 / PGE5 Interval-Shift Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | Git / source | Startup and source boundary | repository root / authoritative notes | VERIFIED |
| EV-002 | exact proof | Symbolic fixed-core theorem | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Candidate-free K oracle and all-arcs audit | `exact_diagnostic.py` | PASS |
| EV-004 | documentation | Source roles, links, and scope | global research/memory/roadmap files | IMPLEMENTED |
| EV-005 | local verification | Dynamic, static, artifact, and document checks | repository root | PASS IN TASK SCOPE; BASELINE RUFF DEBT RETAINED |
| EV-006 | final inspection | Diff, status, whitespace, and cache hygiene | repository root | PASS |

## EV-001 - Startup And Source Boundary

- **Date:** 2026-07-20
- **Method or command:** `git status --short`; `git rev-parse HEAD`;
  `git branch --show-current`; direct inspection of `AGENTS.md`, global
  memory/status/roadmap, PGE5-1--PGE5-26, K825-1--K825-26, and
  KPG46Q-1--KPG46Q-29.
- **Relevant output:** clean `main` at
  `8dc7b4247017f5845f9ae1f3df2433221c423ec3`; PGE5 proves the exact
  supported W-minimizing scaffold bijections but leaves this e=5 K value
  open; the e=4 theorem is a different core.
- **Interpretation:** the bounded task is well posed and begins from a clean
  reviewed baseline.
- **Limitations:** source inspection proves neither the new maximizer nor its
  score.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---strict-startup-and-scope-isolation`.

## EV-002 - Symbolic Fixed-Core Theorem

- **Date:** 2026-07-20
- **Method:** literal expansion of PGE5-1--PGE5-4 under only
  `alpha_(q,2m-1)`; the exact isolated-hole identity K825-6--K825-9; direct
  integer algebra for nine deletion classes, every two-edge middle role,
  all three-edge and longer compressed paths, the cyclic cut, standard sums
  of `j,j^2`, and exact residue/K825 substitutions. A separate line-by-line
  algebra audit found no mathematical defect.
- **Relevant result:** KPGE5-1--KPGE5-30 prove the unique maximizer
  \[
  B_m=\{4m+1,\ldots,10m+4\}
  \]
  and
  \[
  K={572m^3+809m^2+8mq+329m+4q^2+20q+36\over2}.
  \]
  The unique deletion minimum is `36m+20`; the unique shortcut minimum is
  `9` at `m=2` and `4m+2` for `m>=3`. All five residue branches are regular.
  Exact subtraction gives strict same-row improvement over K825 and
  `K825-K=13n^2/2500+O(n)`.
- **Interpretation:** exact theorem for one prescribed cyclic core order.
- **Limitations:** it proves no claim for another supported bijection, the
  permanent, an angular threshold, geometry, global K-minimization, or global
  optimality.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---symbolic-maximizer-and-score-theorem`.

## EV-003 - Independent Bounded Exact Oracle

- **Date:** 2026-07-20
- **Command:**
  `python -B ops/TASK-20260720__pge5_interval_shift_exact_k/exact_diagnostic.py`.
- **Relevant output:** PASS. On `m=2..30`, 29 rows use 37,475,656 max-plus
  transitions and traverse all 968,774 proper oriented arcs. Every row has
  optimizer count one and witness `B_m`; all deletion and compressed-
  shortcut margins are positive, with the exact unique minimizers asserted.
  Formula/support/residue/K825 checks cover 999 rows through `m=1000`.
- **Method:** the optimizer fixes the unique least selected position and
  solves an increasing-position DAG, without receiving the claimed backbone
  as input. The second traversal reconstructs raw arc sums, removes only
  internal holes, checks the exact budget identity, and includes both
  directions and every cyclic-cut arc.
- **Interpretation:** independent bounded exact corroboration of the symbolic
  theorem and complete bounded argmax classification.
- **Limitations:** internal finite computation, not an all-`m` proof, external
  audit, artifact certificate, production path, or hosted CI run. It
  enumerates no alternative assignment, matching, permutation, subset, or
  permanent.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---independent-bounded-oracle`.

## EV-004 - Document And Scope Consolidation

- **Date:** 2026-07-20
- **Method:** source-role inspection and targeted link/tag/scope audit over
  the four modified authoritative Markdown files.
- **Relevant result:** KPGE5-1--KPGE5-30 occur sequentially and exactly once;
  all modified relative links and target anchors resolve; the obsolete open
  PGE5 question is absent; the roadmap contains one next atomic task; and
  all theorem synopses retain the fixed-bijection and non-consequence scope.
- **Interpretation:** detailed proof, stable memory, roadmap, and task
  evidence retain their assigned roles without importing the e=4 theorem.
- **Limitations:** document consistency alone proves no formula.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---authoritative-proof-and-durable-memory`.

## EV-005 - Local Repository Verification

- **Date:** 2026-07-20
- **Methods or commands:** standalone diagnostic; scoped `ruff check` and
  `ruff format --check`; `python -m pytest -p no:cacheprovider`; focused
  checked-artifact schema pytest; `PYTHONPATH=src` checked-artifact verifier;
  in-memory modified-document link/tag/scope audit; repository-wide Ruff.
- **Relevant output:** diagnostic PASS; scoped Ruff PASS; full pytest
  `283 passed in 73.63s`; focused schema pytest `4 passed in 0.97s`;
  artifact verifier PASS for four certificates, 76 local brackets, and
  summary rows `n=3,4,5,6`; document audit PASS for KPGE5 tags 1--30 and all
  modified local targets.
- **Retained failed checks:** repository-wide Ruff lint reports the same four
  existing findings in untouched `critical_structure.py`,
  `fixed_order_artifact.py`, and `test_finite_results.py`; repository-wide
  Ruff format reports the same 39 untouched files. The new diagnostic is in
  neither failure set and passes both scoped checks.
- **Interpretation:** task-scoped code and all dynamic checks pass; no tested
  or artifact regression is present. Baseline Ruff debt is unchanged and out
  of scope.
- **Limitations:** local Python 3.14.3 is not the hosted Python 3.11--3.13
  matrix; no commit-associated hosted run exists.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---local-verification`.

## EV-006 - Final Inspection

- **Date:** 2026-07-20
- **Methods or commands:** `git status --short --branch`; `git diff
  --name-only`; `git diff --numstat`; `git diff --check`; direct tracked and
  untracked content inspection; task-directory listing; and an inline UTF-8
  trailing-whitespace scan over `git ls-files -co --exclude-standard`.
- **Relevant output:** five tracked project/status documents and four new
  task-dossier files are exactly in scope; `git diff --check` emits no
  finding; the 468-file tracked-plus-untracked text scan passes; the task
  directory contains only its four intended files and no cache artifact.
- **Interpretation:** final diff, scope, durable memory, and hygiene satisfy
  `READY_FOR_REVIEW`; the user retains manual commit authority.
- **Limitations:** no staging, commit, push, or hosted CI run was performed.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---final-inspection-and-handoff`.
