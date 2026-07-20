# EVIDENCE - TASK-20260720 / Residue-Two PG49-Star K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / definition | Startup, clean scope, unchanged PGE2 object | repository sources and dossier | VERIFIED |
| EV-002 | exact theorem | Argmax, gains, shortcuts, formula, comparisons | proof note | PROVED |
| EV-003 | bounded exact computation | Sole independent max-plus/all-arcs diagnostic | `exact_diagnostic.py` | PASS |
| EV-004 | verification / review | Tests, source audit, diff hygiene, independent audits | repository commands | PASS |

## EV-001 - Startup Scope And Fixed Object

- **Date:** 2026-07-20
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the relevant task dossiers,
  (PGE2-1)--(PGE2-29), (K825-1)--(K825-9), (KR2-1)--(KR2-36), and
  (KPGODD-1)--(KPGODD-36); inspect read-only Git status.
- **Relevant output:** the worktree was clean. The only evaluated object is
  the unchanged map (PGE2-6) on the already proved compatible scaffold.
- **Interpretation:** verified provenance and task boundary, not a K theorem.
- **Limitations:** all symbolic score and uniqueness claims remain pending in
  EV-002 at this checkpoint.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---strict-startup-and-literal-reconstruction`.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-20
- **Method:** direct reconstruction of (PGE2-6); isolated-hole identity
  (K825-6)--(K825-9); nine exhaustive gain classes; endpoint-hole, every
  two-edge middle role, three-edge, and all longer compressed shortcuts;
  literal block summation; exact comparator specialization.
- **Relevant output:** (KPGE2-1)--(KPGE2-45) prove the unique maximizer
  \(B_m=\{4m+1,\ldots,10m+2\}\), score (KPGE2-4), five regular residue
  branches plus the literal \(m=1\) residual, and strict all-row improvement
  over both the known residue-two order and K825.
- **Boundary evidence:** all empty ranges, the doubleton, singleton block,
  retained and deleted closing roles, \(m=1,2\), and every equality case are
  explicit. The unique shortcut minimum changes at \(m=1,2,3\) without
  changing the argmax or all-row score formula.
- **Interpretation:** **exact fixed-core combinatorial theorem** for every
  \(m\ge1\).
- **Limitations:** no production, angular, geometric, global-minimizer, or
  global-optimality conclusion follows.
- **Linked log entry:**
  TASK_LOG.md#2026-07-20---exact-all-domain-k-theorem.

## EV-003 - Sole Bounded Independent Diagnostic

- **Date:** 2026-07-20
- **Command:**
  python ops/TASK-20260720__residue_two_pg49_star_k/exact_diagnostic.py
- **Declared limits:** exact formula, residual, boundary, and comparator
  checks for \(m=1,\ldots,1000\); max-plus and every proper oriented arc for
  \(m=1,\ldots,30\).
- **Relevant output:** PASS on 5,006,000 literal core entries, 36,511,800
  max-plus transitions, 1,830 deletion gains, 950,150 proper oriented arcs,
  and 943,640 nontrivial compressed shortcuts.
- **Independent mechanism:** the script imports only the standard library,
  constructs only (PGE2-6), aggregates subset choices by max-plus rather than
  enumerating them, and checks the exact raw-sum plus internal-hole-budget
  identity on every arc.
- **Interpretation:** **bounded exact computation** corroborating EV-002.
- **Limitations:** finite rows do not prove the all-\(m\) theorem.
- **Linked log entry:**
  TASK_LOG.md#2026-07-20---sole-independent-diagnostic.

## EV-004 - Final Verification, Review, And Handoff

- **Date:** 2026-07-20
- **Commands:** the standalone diagnostic; scoped
  `python -m ruff check` and `python -m ruff format --check`; full
  `python -m pytest -p no:cacheprovider`; focused
  `tests/test_checked_artifact_schema_validation.py`;
  `python -m power_ringmin.verify_checked_artifacts` with `PYTHONPATH=src`;
  a scoped Section 18 source audit; and read-only Git status, stat, complete
  tracked/untracked inspection, and `git diff --check`.
- **Relevant output:** diagnostic PASS with the EV-003 counts; Ruff PASS;
  283 full-suite tests passed; 4 focused schema tests passed; checked
  artifacts verified for four certificates, 76 local brackets, and
  \(n=3,4,5,6\); source audit PASS with 45 sequential unique KPGE2 tags,
  52 balanced displays, balanced aligned/array/cases/gathered environments,
  and no control characters; final diff whitespace check PASS.
- **Independent review:** three focused read-only audits checked the symbolic
  proof, exact comparator algebra, and diagnostic mechanism. A fourth
  read-only audit checked the final proof, all authoritative summaries, and
  the dossier. All actionable quantifier, notation, formula-copy, reference,
  and editorial findings were corrected.
- **Failed-check evidence:** the initial Ruff format check found one
  mechanical delta and the formatter corrected it. One final source-audit
  wrapper invocation had a PowerShell interpolation parse error before
  source inspection; the corrected command passed.
- **Scope result:** only `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`,
  `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/NEXT_RESEARCH_STEPS.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, `start.md`, and the new
  `ops/TASK-20260720__residue_two_pg49_star_k/` dossier are in scope.
  Production and test files are untouched; Codex ran no Git write operation.
- **Interpretation:** repository and task-scoped verification pass. The task
  is `READY_FOR_REVIEW`.
- **Limitations:** the bounded diagnostic remains finite; all-domain validity
  comes from EV-002. The user must review and decide whether to commit.
- **Linked log entry:**
  TASK_LOG.md#2026-07-20---final-verification-and-handoff.
