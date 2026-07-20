# TASK_STATUS - TASK-20260720 / PGE5 Post-Review Consolidation

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** eliminate the documentation and verifiability debt found in
  review of PGE5 at baseline
  `6ec74a834920732b1be1b16409b2207e21e2ae13`, without developing new
  mathematics.
- **Expected output:** one unambiguous document hierarchy, a deprecated
  `start.md` stub, one compact stable PGE5 synopsis linked to the sole complete
  proof, formula-independent internal matching evidence, correctly qualified
  CI provenance, and one next mathematical priority.

## Scope

- **In scope:** `AGENTS.md`; the global routing documents; PGE5 references and
  open/closed qualifications; the existing direct `m=2..40` diagnostic; one
  new standalone standard-library oracle; workflow inspection; local
  verification and durable evidence.
- **Out of scope:** new mathematical claims, evaluation of the PGE5 core's
  `K`, production/test code, hosted CI execution, commits, pushes, and changes
  to the protected upstream repository.

## Verified Facts

- Startup found a clean `main` worktree exactly at the requested baseline.
- The authoritative PGE5 proof is PGE5-1--PGE5-26 in
  `research/PRODUCT_DISTANCE_SURROGATE.md`.
- The existing task-local scan is direct on `m=2..40`, but its extendibility
  check uses suffix Hall and therefore is not the independent matching oracle
  requested by review.
- The already closed Ferrers count and identically named threshold-closing
  `K` theorem concern the earlier `n=10m+3`, `e=4` scaffold, not PGE5 on
  `n=10m+4`, `e=5`.

## Decisions And Rationale

- Keep the original diagnostic unchanged for provenance and add the new
  oracle in this dossier, so formula-based and formula-independent evidence
  remain distinct.
- Remove the duplicated global roadmap from `PROJECT_KNOWLEDGE.md` and reduce
  `research/NEXT_RESEARCH_STEPS.md` to routing and priorities with links.
- Treat the former task-local Ferrers-permanent suggestion as historical and
  superseded; it is not a current global priority.
- Remove the hosted workflow's no-op `git diff --check` step while retaining
  its effective repository-wide tracked-text whitespace scan.

## Plan And Expected Delta

- Consolidate document roles and references without changing PGE5 equations.
- Compare a literal-word augmenting-path oracle with theoretical support on
  `m=2..20`.
- Exhaust all scaffold bijections for `m=2,3,4` with independent full and
  distance-at-most-two cyclic scorers.
- Run local diagnostic, syntax, Ruff, full pytest, artifact, reference, diff,
  and whitespace checks; then record the exact outputs.

## Verification

- **Checks:** original and independent PGE5 diagnostics; in-memory syntax over
  all Python files; Ruff lint/format; full pytest; focused schema pytest;
  checked-artifact verifier; Markdown target/anchor and source-role audit.
- **Observed result:** both diagnostics pass; 81 Python files compile; the new
  oracle passes scoped Ruff lint and format; 283 full tests and four schema
  tests pass; four certificates and 76 local brackets verify; all four local
  Markdown links and all 26 sequential PGE5 tags pass the document audit;
  final diff, tracked-plus-untracked whitespace, scope, and cache checks pass.
- **Retained repository debt:** repository-wide Ruff lint reports four
  pre-existing errors in four untouched source/test files, and repository-wide
  Ruff format reports 39 untouched files. The task does not reformat or repair
  unrelated baseline code.
- **Limitations:** both diagnostics are internal bounded computations. Neither
  is an external audit, a symbolic proof, or a hosted CI run. Local Python
  3.14.3 is not the hosted Python 3.11--3.13 matrix.

## Blockers / Risks

- No blocker.
- Hosted GitHub Actions for the uncommitted result cannot exist and must remain
  `UNVERIFIED` until a commit is pushed and a run is associated with its SHA.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Files changed:** eight tracked documents/workflow files and four new
  task-dossier files; no production or test file changed.
- **Files to read first:** `AGENTS.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, and this dossier's `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Consolidate PGE5 post-review verification`.
- **Proposed next fresh task:** evaluate exactly `K` for the PGE5 `e=5`,
  `n=10m+4` interval shift `alpha_(q,2m-1)`, with
  `q=floor((4m+3)/5)`.
