# TASK_STATUS - TASK-20260720 / PGE5 Interval-Shift Exact K

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** evaluate exactly the induced-subset objective \(K\) for the
  single PGE5 interval shift \(\alpha_{q,2m-1}\) on
  \(n=10m+4\), \(m\ge2\), with
  \(q=\lfloor(4m+3)/5\rfloor\), classify every maximizing subset, and
  compare it exactly and asymptotically with the canonical K825 order on the
  same subsequence.
- **Expected output:** one symbolic proof, all five residue branches and the
  minimum row, one bounded independent exact oracle, durable evidence, and
  no conclusion outside the fixed core-order scope.

## Scope

- **In scope:** only the unchanged PGE5 scaffold (PGE5-1)--(PGE5-26), the
  one interval shift (PGE5-22) specialized to \((q,2m-1)\), exact deletion
  gains, all compressed shortcuts including cyclic closure, the exact block
  sum, residue classes, and same-row K825 comparison.
- **Out of scope:** every other supported bijection, the Ferrers permanent,
  production-order changes, angular or geometric evaluation, global
  \(K\)-minimization, and global optimality.

## Verified Facts

- Startup found a clean `main` worktree at
  `8dc7b4247017f5845f9ae1f3df2433221c423ec3`.
- PGE5-1--PGE5-26 are the authoritative construction/support theorem and
  stop at \(W\); the requested \(K\) question is explicitly the sole next
  task.
- The specialized map fixes indices below \(q\), shifts each
  \(q\le j\le2m-2\) to path \(j+1\), and places \(P_q\) in the genuine
  closing gap.
- KPGE5-1--KPGE5-30 prove that the sole maximizing subset is
  \(B_m=\{4m+1,\ldots,10m+4\}\) and
  \[
  K={572m^3+809m^2+8mq+329m+4q^2+20q+36\over2}.
  \]
- The unique deletion minimum is \(36m+20\). The unique shortcut minimum is
  the closing margin \(9\) at \(m=2\), and \(4m+2\) at \(c_0\) thereafter.
  All five residue branches are regular.
- Canonical K825 is strictly larger on every same-subsequence row; both
  families have cubic coefficient \(143/500\), and
  \(K_{825}-K=13n^2/2500+O(n)\).

## Assumptions / Inferences

- None. The symbolic proof and independent bounded oracle agree; no
  heuristic or conjectural statement is promoted.

## Decisions And Rationale

- Reuse only the general isolated-hole identity (K825-6)--(K825-9); derive
  every PGE5-specific gain and shortcut bound afresh.
- Keep the diagnostic standalone and standard-library-only so it is
  independent of project scorers and proof formulas at its optimization
  layer.

## Implemented Delta

- Added one exact fixed-core theorem to
  `research/FIXED_ORDER_CYCLE_RATIO.md`, closed and routed it from the
  surrogate proof, stable memory, status, and roadmap.
- Added one standalone task-local exact diagnostic and this STRICT dossier.
- Changed no production or test file and evaluated no alternative bijection.

## Verification

- **Checks:** symbolic line audit; standalone candidate-free max-plus and
  all-arcs diagnostic; scoped syntax/Ruff; full and focused pytest;
  checked-artifact verifier; modified-document link/tag/scope audit;
  repository-wide Ruff; final Git, diff, whitespace, and cache inspection.
- **Observed result:** symbolic audit found no defect; diagnostic PASS on
  `m=2..30` and formulas through `m=1000`; scoped Ruff PASS; full pytest
  `283 passed`; focused schema pytest `4 passed`; four certificates and 76
  local brackets verify; document audit PASS. Repository-wide Ruff retains
  four lint and 39 format findings in untouched baseline files. Final
  `git diff --check`, 468-file text scan, scope, and cache checks pass.
- **Limitations:** bounded computation corroborates rather than proves the
  all-\(m\) theorem; local Python 3.14.3 is not hosted CI.

## Blockers / Risks

- No blocker.
- Residual risk is transcription or review error in a long symbolic proof;
  two independent algebra audits and the bounded oracle found none. The
  distinct \(e=4\), \(n=10m+3\) theorem remains explicitly separated.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** implementation, proof, bounded oracle, local
  verification, durable memory, and final hygiene are complete.
- **Files changed:** five project/status documents and four new task-dossier
  files; no production or test file.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` Section 20,
  `exact_diagnostic.py`, and `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Prove exact K for the fixed PGE5 interval shift`.
- **Proposed next fresh task:** post-review audit of KPGE5-1--KPGE5-30 and
  the standalone diagnostic at the reviewed commit.
