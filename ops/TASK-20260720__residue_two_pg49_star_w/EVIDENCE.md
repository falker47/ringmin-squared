# EVIDENCE - TASK-20260720 / Residue-Two PG49-Star W

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / definition | Startup and candidate fixed before score | repository sources and task dossier | VERIFIED |
| EV-002 | exact theorem | Ferrers relation, Hall support, images, boundaries, closure | (PGE2-1)--(PGE2-25) | PROVED |
| EV-003 | exact theorem | all cyclic distance classes and exact \(W\) | (PGE2-26)--(PGE2-29) | PROVED |
| EV-004 | bounded exact computation | sole standalone diagnostic | `exact_diagnostic.py` | PASS |
| EV-005 | independent review | compatibility and score audits | two read-only audits | PASS |
| EV-006 | verification suite | tests, artifact verifier, Ruff, source audit | repository commands | PASS |
| EV-007 | final review / Git | complete diff and scope inspection | tracked and untracked changes | PASS |

## EV-001 - Startup And Candidate Fixed Before Score

- **Date:** 2026-07-20
- **Method or command:** read the mandatory startup files, relevant residue-two
  and PG49-star task memory, the literal proof/source scaffold, and read-only
  Git status.
- **Relevant output:** the worktree was clean at startup. The sole candidate
  is recorded verbatim in `TASK_STATUS.md`; no global score had been computed
  when it was fixed.
- **Interpretation:** this is a definition and provenance checkpoint, not a
  compatibility theorem or score computation.
- **Limitations at this provenance checkpoint:** every Ferrers, Hall,
  boundary, closure, and score claim was intentionally pending; EV-002 and
  EV-003 record their later resolution.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---startup-and-candidate-fixing-before-score`.

## EV-002 - Exact All-Domain Compatibility

- **Date:** 2026-07-20
- **Method:** direct symbolic classification of every one- and two-step form
  in the literal gap word, followed by exact Ferrers and residual-suffix Hall
  arguments.
- **Relevant result:** triples are admitted exactly for
  \(k\ge\kappa_j\); doubleton and singleton paths are strictly universal;
  the Hall support equals the local relation; and all four image blocks of
  the fixed map are supported and partition the path indices.
- **Boundary evidence:** empty ranges, \(m=1\), the closing equality
  \(\alpha(2m-1)=q=\kappa_{2m-1}\), the complete minimum-row order, and the
  literal cyclic word \((n,2,A_q,c_q,B_q,4m+1,D)\) are explicit.
- **Interpretation:** **exact combinatorial theorem** for every \(m\ge1\).
  No symbolic obstacle exists.
- **Limitations:** construction compatibility only; it is not a \(K\),
  geometric, minimizing-order, or global-optimality theorem.

## EV-003 - Exact Product-Distance Score

- **Date:** 2026-07-20
- **Method:** only after EV-002, cover cyclic distances one and two by the
  local relation; use \(A_0c_0=J\) for equality; prove the strict
  distance-three margin
  \(3J-n(D-1)=16m^2+36m+8\); and prove the strict all-\(s\ge4\) margin
  \(4J-n(n-1)=28m^2+66m+14\).
- **Relevant result:**
  \[
  W=J={(8m+4)(8m+2)\over2}=32m^2+24m+4.
  \]
- **Interpretation:** **exact fixed-order theorem** for all \(m\ge1\).
- **Limitations:** no \(K\) was calculated and no alternative candidate was
  inspected after scoring.

## EV-004 - Sole Bounded Standalone Diagnostic

- **Date:** 2026-07-20
- **Command:**
  `python ops/TASK-20260720__residue_two_pg49_star_w/exact_diagnostic.py`
- **Declared limits:** formula/Ferrers rows \(m=1,\ldots,1000\); literal
  relation and residual Hall rows \(m=1,\ldots,40\); exact all-pairs scoring
  rows \(m=1,\ldots,80\).
- **Relevant output:** PASS; 1,001,000 candidate-image entries, 88,560 local
  relation checks, 5,290,640 Hall inequalities, and 8,710,200 unordered
  cyclic pairs.
- **Interpretation:** **bounded exact computation** corroborating EV-002 and
  EV-003, not replacing their all-domain proofs.
- **Limitations:** the script imports only the standard library, constructs
  one candidate, performs no candidate/matching/path-permutation/order-family
  or subset search, and computes no \(K\).

## EV-005 - Independent Mathematical Audits

- **Date:** 2026-07-20
- **Method:** two read-only independent derivations, one focused on
  compatibility and one on every positional distance.
- **Relevant output:** both audits reproduce compatibility for every
  \(m\ge1\) and \(W=J\). The score audit independently checked every pair
  with exact rational arithmetic through \(m=100\).
- **Interpretation:** independent corroboration and editorial hardening.
- **Limitations:** these audits are supporting evidence; the durable symbolic
  proof and standalone diagnostic remain the primary evidence.

## EV-006 - Final Verification Suite

- **Date:** 2026-07-20
- **Commands:** standalone diagnostic; scoped Ruff check/format; full
  `python -m pytest -p no:cacheprovider`; focused checked-artifact schema
  tests; `python -m power_ringmin.verify_checked_artifacts` with
  `PYTHONPATH=src`; and a scoped PGE2 source audit.
- **Relevant output:** diagnostic PASS with the EV-004 counts; Ruff PASS;
  283 pytest tests passed; 4 focused schema tests passed; checked artifacts
  verified for four certificates, 76 local brackets, and \(n=3,4,5,6\);
  source audit PASS with 29 sequential unique PGE2 tags, 34 balanced
  displays, balanced math environments, no control characters, and no
  missing `\left` token.
- **Failed-check evidence:** the initial Ruff format check found one
  mechanical formatting delta and the formatter corrected it. The first
  source-audit command had a PowerShell interpolation parse error before
  source inspection; the corrected command passed.
- **Interpretation:** repository and task-scoped verification pass after the
  recorded mechanical/tooling corrections.
- **Limitations:** bounded diagnostics remain bounded; all-domain validity
  comes from EV-002 and EV-003.

## EV-007 - Final Diff, Scope, And Handoff

- **Date:** 2026-07-20
- **Method or commands:** `git status --short --branch`, `git diff --stat`,
  complete per-file tracked diff inspection, complete untracked dossier
  inspection, `git diff --check`, and a separate read-only final diff audit.
- **Relevant output:** only `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`,
  `research/NEXT_RESEARCH_STEPS.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, `start.md`, and the new
  `ops/TASK-20260720__residue_two_pg49_star_w/` dossier are in scope. The
  whitespace check and independent audit pass.
- **Interpretation:** the bounded task is implemented and verified, with
  production code untouched; status is `READY_FOR_REVIEW`.
- **Limitations:** the user must review and decide whether to commit. Codex
  ran no Git write operation.
