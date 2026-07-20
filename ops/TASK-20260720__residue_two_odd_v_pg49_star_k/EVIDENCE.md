# EVIDENCE - TASK-20260720 / Residue-Two Odd-v PG49-Star K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / definition | Startup, clean scope, unchanged PGE2ODD object | repository sources and dossier | VERIFIED |
| EV-002 | exact theorem | Argmax, gains, shortcuts, formula, comparisons | fixed-order proof | PROVED |
| EV-003 | bounded exact computation | Sole independent max-plus/all-arcs diagnostic | `exact_diagnostic.py` | PASS |
| EV-004 | verification / review | Tests, source audit, diff hygiene, independent audits | repository commands | PASS |

## EV-001 - Startup Scope And Fixed Object

- **Date:** 2026-07-20
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the relevant task dossiers,
  (PGE2ODD-1)--(PGE2ODD-29), (K825-1)--(K825-9), (KR2-1)--(KR2-36), and
  (KPGE2-1)--(KPGE2-45); inspect read-only Git status.
- **Relevant output:** the worktree was clean. The only evaluated object is
  the unchanged map (PGE2ODD-6) on the already proved compatible scaffold.
- **Interpretation:** verified provenance and task boundary, not a \(K\)
  theorem.
- **Limitations:** every symbolic score and uniqueness claim was pending at
  this checkpoint.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---strict-startup-and-literal-reconstruction`.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-20
- **Method:** direct reconstruction of (PGE2ODD-6); isolated-hole identity
  (K825-6)--(K825-9); seven exhaustive gain classes; endpoint-hole, every
  two-edge middle role, three-edge, and all longer compressed shortcuts;
  literal block summation; exact comparator specialization.
- **Relevant output:** (KPGE2ODD-1)--(KPGE2ODD-43) prove the unique maximizer
  \(B_m=\{4m+3,\ldots,10m+7\}\), score (KPGE2ODD-4), five regular residue
  branches without a correction, and strict all-row improvement over both the
  known residue-two order and K825.
- **Boundary evidence:** all empty ranges, singleton block, absent doubleton,
  singleton subsets, the two-element convention, cyclic closure,
  \(m=1,2,3\), and every equality case are explicit. The unique shortcut
  minimum changes after \(m=2\) without changing the argmax or score formula.
- **Interpretation:** **exact fixed-core combinatorial theorem** for every
  \(m\ge1\).
- **Limitations:** no construction, production, angular, geometric, global-
  minimizer, or global-optimality conclusion follows.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---exact-all-domain-k-theorem`.

## EV-003 - Sole Bounded Independent Diagnostic

- **Date:** 2026-07-20
- **Command:**
  `python ops/TASK-20260720__residue_two_odd_v_pg49_star_k/exact_diagnostic.py`
- **Declared limits:** exact formula, residue, boundary, and comparator checks
  for \(m=1,\ldots,1000\); max-plus and every proper oriented arc for
  \(m=1,\ldots,30\).
- **Relevant output:** PASS on 5,011,000 literal core entries, 38,957,975
  max-plus transitions, 1,890 cancellation gains, 997,550 proper oriented
  arcs, and 990,830 nontrivial compressed shortcuts.
- **Independent mechanism:** the script imports only the standard library,
  constructs only (PGE2ODD-6), aggregates subset choices by max-plus rather
  than enumerating them, and checks the exact raw-sum plus internal-hole-
  budget identity on every arc.
- **Interpretation:** **bounded exact computation** corroborating EV-002.
- **Limitations:** finite rows do not prove the all-\(m\) theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---sole-independent-diagnostic`.

## EV-004 - Final Verification, Review, And Handoff

- **Date:** 2026-07-20
- **Commands:** the standalone diagnostic; scoped `python -m ruff check` and
  `python -m ruff format --check`; full
  `python -m pytest -p no:cacheprovider`; focused
  `tests/test_checked_artifact_schema_validation.py`;
  `python -m power_ringmin.verify_checked_artifacts` with `PYTHONPATH=src`;
  a scoped Section 19 tag/display/environment/control-character audit; and
  read-only Git status, stat, complete tracked/untracked inspection, and
  `git diff --check`.
- **Relevant output:** diagnostic PASS with the EV-003 counts; Ruff PASS;
  283 full-suite tests passed; 4 focused schema tests passed; checked
  artifacts verified for four certificates, 76 local brackets, and
  \(n=3,4,5,6\); source audit PASS with 43 sequential unique KPGE2ODD tags,
  48 balanced display pairs, balanced environments, and no control
  characters; final diff whitespace check PASS.
- **Independent review:** four read-only audits checked the symbolic proof,
  exact comparator algebra, diagnostic mechanism, synchronization, and scope.
  All formula, bound, notation, and editorial findings were corrected and
  reaudited to PASS.
- **Failed-check evidence:** two `rg` wrappers used malformed regular
  expressions and exited before completing their searches. Corrected fixed-
  string searches and the independent source audit pass. No mathematical,
  diagnostic, test, artifact, or diff-hygiene check failed.
- **Scope result:** only `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`,
  `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/NEXT_RESEARCH_STEPS.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, `start.md`, and the new
  `ops/TASK-20260720__residue_two_odd_v_pg49_star_k/` dossier are in scope.
  Production and test files are untouched; Codex ran no Git write operation.
- **Interpretation:** repository and task-scoped verification pass. The task
  is `READY_FOR_REVIEW`.
- **Limitations:** the bounded diagnostic remains finite; all-domain validity
  comes from EV-002. The user must review and decide whether to commit.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---final-verification-and-handoff`.
