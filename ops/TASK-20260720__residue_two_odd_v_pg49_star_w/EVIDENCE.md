# EVIDENCE - TASK-20260720 / Residue-Two Odd-v PG49-Star W

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / definition | Startup and candidate fixed before score | repository sources and task dossier | VERIFIED |
| EV-002 | exact theorem | Ferrers relation, Hall support, images, orientations, boundaries, closure | (PGE2ODD-1)--(PGE2ODD-25) | PROVED |
| EV-003 | exact theorem | all cyclic positional distances and exact \(W\) | (PGE2ODD-26)--(PGE2ODD-29) | PROVED |
| EV-004 | bounded exact computation | sole standalone standard-library diagnostic | `exact_diagnostic.py` | PASS |
| EV-005 | independent review | compatibility, score/diagnostic, synchronization | three read-only audits | PASS |
| EV-006 | verification suite | Ruff, diagnostic, source audit, tests, artifact verifier | repository commands | PASS |
| EV-007 | final review / Git | complete diff, untracked dossier, scope, whitespace, status | repository tree | PASS |

## EV-001 - Startup Provenance And Pre-Score Definition

- **Date:** 2026-07-20
- **Method or command:** read the mandatory startup files, relevant task
  memory, (R2C1)--(R2C8), (PGE2-1)--(PGE2-29), the actual construction/`W`
  sequence (PGODD-1)--(PGODD-27), and read-only Git status.
- **Relevant output:** the worktree was clean at startup.  The sole candidate
  is recorded verbatim in `TASK_STATUS.md` before any full-order score
  conclusion.  Direct specialization of (R2C5) proves that the doubleton
  class is empty on this branch.
- **Interpretation:** verified provenance and a **definition**, not a
  compatibility theorem or score computation.
- **Limitations:** every Ferrers, Hall, image, boundary, closure, and score
  claim remains pending at this checkpoint.  The repository contains no tags
  PGODD-28--PGODD-36; those numerals belong to the out-of-scope KPGODD
  theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---startup-and-candidate-fixing-before-score`.

## EV-002 - Exact All-Domain Compatibility

- **Date:** 2026-07-20
- **Method:** direct symbolic classification of every one- and two-step form
  in the literal gap word, followed by exact Ferrers-threshold and
  residual-suffix Hall arguments.
- **Relevant result:** triples are admitted exactly when
  \(k\ge\kappa_j\); every singleton is strictly universal; no doubleton
  exists; the Hall support equals the local relation; and all four image
  blocks of the pre-fixed map are disjoint, exhaustive, and supported.
- **Boundary evidence:** the exact closing value
  \(q=\lfloor(4m+3)/5\rfloor\), all empty ranges, the complete \(m=1\)
  order, unchanged triple orientations, trivial singleton orientations, the
  absent doubleton type, and the genuine closing word are explicit in
  (PGE2ODD-1)--(PGE2ODD-25).
- **Interpretation:** **exact combinatorial theorem** for every \(m\ge1\).
  No symbolic obstruction exists.
- **Limitations:** construction compatibility only.  This evidence neither
  computes \(K\) nor asserts a geometric, minimizing-order, or global
  optimality consequence.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---exact-compatibility-proof`.

## EV-003 - Exact Product-Distance Score

- **Date:** 2026-07-20
- **Method:** only after EV-002, cover circular distances one and two by the
  exact local relation; use \(A_0c_0=J\) for equality; prove the strict
  distance-three margin
  \(3J-n(D-1)=16m^2+52m+30\); and prove the strict all-\(s\ge4\) margin
  \(4J-n(n-1)=28m^2+94m+54\).
- **Relevant result:**
  \[
  W=J={(8m+8)(8m+6)\over2}=32m^2+56m+24.
  \]
- **Interpretation:** **exact fixed-order theorem** for every \(m\ge1\).
- **Limitations:** no \(K\) was calculated, no alternative candidate was
  inspected, and no angular, geometric, minimizing-order, or global
  optimality conclusion follows.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---exact-score-after-compatibility`.

## EV-004 - Sole Bounded Standalone Diagnostic

- **Date:** 2026-07-20
- **Command:**
  `python ops/TASK-20260720__residue_two_odd_v_pg49_star_w/exact_diagnostic.py`
- **Declared limits:** formula/Ferrers rows \(m=1,\ldots,1000\); literal
  relation and residual Hall rows \(m=1,\ldots,40\); exact all-pairs scoring
  rows \(m=1,\ldots,80\).
- **Relevant output:** PASS; 1,002,000 candidate-image entries, 91,880
  literal local-relation checks, 5,557,960 residual Hall inequalities, and
  8,873,400 unordered cyclic pairs.
- **Interpretation:** **bounded exact computation** corroborating EV-002 and
  EV-003, not replacing their all-domain proofs.
- **Limitations:** the script imports only the standard library, constructs
  one candidate, performs no candidate, matching, path-assignment,
  order-family, subset, or \(K\) search, and changes no production path.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---sole-bounded-diagnostic-and-source-synchronization`.

## EV-005 - Independent Mathematical And Synchronization Audits

- **Date:** 2026-07-20
- **Method:** three independent read-only audits, focused respectively on
  (PGE2ODD-1)--(PGE2ODD-25), (PGE2ODD-26)--(PGE2ODD-29) plus the diagnostic,
  and synchronization/scope across every authoritative file and the dossier.
- **Relevant output:** PASS after correcting stale in-progress lines in
  TASK_STATUS.  The audits independently reproduce the exact thresholds,
  Hall support, images, empty ranges, minimum row, closure, equality witness,
  longer-distance margins, exact \(W\), and all bounded counts.
- **Interpretation:** independent mathematical, code, editorial, and scope
  corroboration.
- **Limitations:** read-only audits support but do not replace the durable
  symbolic proof or the declared bounded diagnostic.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---independent-audits-and-strict-verification`.

## EV-007 - Final Diff, Scope, And Handoff

- **Date:** 2026-07-20
- **Method or commands:** `git status --short --branch`,
  `git diff --stat`, `git diff --numstat`, complete per-file tracked
  diff inspection, complete untracked dossier inspection, and
  `git diff --check`.
- **Relevant output:** only `CURRENT_STATUS.md`,
  `PROJECT_KNOWLEDGE.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, `start.md`, and
  `ops/TASK-20260720__residue_two_odd_v_pg49_star_w/` are in scope.
  The dossier has exactly three memory files and one diagnostic.  Whitespace
  hygiene passes.
- **Interpretation:** the exact bounded task is implemented, verified,
  synchronized, and READY_FOR_REVIEW; production code is untouched.
- **Limitations:** the user must review and decide whether to commit.  Codex
  ran no Git write operation.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---final-diff-status-and-handoff`.

## EV-006 - STRICT Verification Suite

- **Date:** 2026-07-20
- **Commands:** scoped Ruff check/format; the standalone diagnostic; a scoped
  PGE2ODD tag/display/environment/control-character audit; full
  `python -m pytest -p no:cacheprovider`; focused checked-artifact schema
  tests; and the checked-artifact verifier with `PYTHONPATH=src`.
- **Relevant output:** Ruff PASS; diagnostic PASS with EV-004 counts; source
  audit PASS with 29 sequential unique tags, 34 balanced displays, balanced
  environments, and no control characters; 283 pytest tests passed; 4
  focused tests passed; checked artifacts verified for four certificates,
  76 local brackets, and \(n=3,4,5,6\).
- **Failed-check evidence:** the initial Ruff format check reported one
  mechanical delta and the formatter corrected it.  A post-format diagnostic
  invocation with a 10-second timeout was terminated before completion; the
  unchanged 120-second invocation passed in 38 seconds.
- **Interpretation:** task-scoped and repository-wide checks pass after the
  recorded mechanical/tooling corrections.
- **Limitations:** bounded checks remain bounded; all-domain validity comes
  from EV-002 and EV-003.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---independent-audits-and-strict-verification`.
