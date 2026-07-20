# TASK_STATUS - TASK-20260720 / PGE5 Singleton-Reversal Exact K

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** perform one post-review closure of state and provenance for
  the accepted KRPGE5 commit
  `a15a4d34cc034b669f02382e2e4f27b4822ed382`.
- **Accepted baseline:** `main` and `origin/main` both resolved to the exact
  accepted SHA, with a clean worktree before and after all requested baseline
  checks.
- **Expected output:** accepted-baseline identification, fresh local
  verification, one exact-SHA hosted `Verification` record, synchronized
  status/provenance sources, and no new mathematics.

## Scope

- **In scope:** exact accepted-SHA and clean-tree checks; rerunning the sole
  KRPGE5 diagnostic, full pytest, checked-artifact verifier, focused schema
  suite, and repository hygiene; inspecting one hosted `Verification` run
  associated exactly with the accepted SHA; updating current status, roadmap
  routing, stable hosted provenance, and this dossier.
- **Out of scope:** changing KRPGE5-1--KRPGE5-36, adding or evaluating any
  construction, rederiving a mathematical result, changing the diagnostic,
  production, tests, schemas, artifacts, or workflow, rewriting append-only
  chronology, or performing any Git write operation.

## Verified Facts

- The accepted KRPGE5-1--KRPGE5-36 baseline is commit
  `a15a4d34cc034b669f02382e2e4f27b4822ed382`, titled
  `Correct the KRPGE5 geometric closure`.
- At startup, `HEAD`, `main`, and `origin/main` resolved to that SHA and
  `git status --porcelain=v1 --untracked-files=all` was empty.
- The accepted KPGE5 map shifts every path after \(q\) monotonically; the new
  map instead keeps that shift only through the doubleton and reverses the
  complete singleton block.
- KRPGE5-1--KRPGE5-32 prove that the map is supported, has \(W=W_n\),
  has sole argmax \(B_m=\{4m+1,\ldots,10m+4\}\), and has exact score
  \[
  K_*={1714m^3+2439m^2+24mq+965m+12q^2+60q+120\over6}.
  \]
- The target is true:
  \(K_\uparrow-K_*=(m-1)(m-2)(m-3)/3\). Hence the fixed-family cubic
  coefficient is \(857/3000\), and K825 is strictly larger on every row.
- The unique deletion minimum is \(36m+20\). The unique shortcut minimum is
  \(9\) at the genuine closing arc for \(m=2\), and \(4m+2\) at \(c_0\)
  for \(m\ge3\).
- For every insertion gap \(g\), (CR12p) and (CR22) prove
  \[
  \Lambda\bigl(\sigma_{m,g}^{(5,*)}\bigr)=K_*,
  \qquad
  {K_*\over\pi}-(10m+4)^2
  <\rho_{\sigma_{m,g}^{(5,*)}}
  <{K_*\over\pi}.
  \]
- Globally, only
  \[
  R_2^*(10m+4)<{\Lambda_{10m+4}\over\pi}\le {K_*\over\pi}
  \]
  follows. Therefore the requested subsequential coefficient is at most
  \(857/(3000\pi)\).
- The fresh standalone diagnostic passed on the clean accepted commit for
  29 bounded rows, 37,475,656 max-plus transitions, 968,774 proper arcs,
  4,727 insertion gaps, 484,387 neighbor-pair inequalities, and 999
  formula/support rows.
- Fresh local repository verification on the clean accepted commit reported
  `283 passed`, verified four checked certificates and 76 local brackets,
  and reported `4 passed` for the focused schema suite.
- GitHub Actions `Verification` run
  [`29777676234`](https://github.com/falker47/ringmin-squared/actions/runs/29777676234)
  has exact `head_sha`
  `a15a4d34cc034b669f02382e2e4f27b4822ed382`, event `push`, attempt 1,
  and conclusion `success`; all Python 3.11, 3.12, and 3.13 jobs succeeded.
- Historical run `29771633257` remains associated only with
  `bce6e4d8a935bd9d8509e59b760cf78c345779b6` and was not reused as
  evidence for the accepted commit.

## Assumptions / Inferences

- No new mathematical inference is made. The existing all-\(m\) statements
  retain their exact-theorem classification, while the rerun diagnostic is
  bounded exact corroboration.
- Hosted provenance is a direct exact-`head_sha` association, not an
  inference from branch position or from the earlier baseline run.

## Decisions And Rationale

- Preserve the historical evidence for commits
  `15ba9f9c58e8c7783ec2ad39d8eaa44b1be50318` and
  `bce6e4d8a935bd9d8509e59b760cf78c345779b6`; supersede their former
  current-status role with a new accepted-baseline evidence item.
- Associate hosted status only by exact SHA. Do not reuse a successful run
  from an ancestor as coverage of the accepted commit.
- Keep this closure documentary and provenance-only; do not alter proof or
  computational content.

## Implemented Delta

- Recorded the accepted KRPGE5 SHA and its fresh clean-commit local results.
- Recorded `Verification` run `29777676234` and its exact-SHA Python
  3.11--3.13 success, while retaining the earlier run as historical only.
- Removed directly connected pre-commit routing and handoff language from
  current status, stable hosted provenance, roadmap, and this dossier's
  current truth.
- Changed no proof, diagnostic, workflow, production file, test, schema, or
  artifact.

## Verification

- **Clean accepted-commit diagnostic:**
  `python -B ops/TASK-20260720__pge5_singleton_reversal_exact_k/exact_diagnostic.py`
  exited 0 and reported PASS with the counts above.
- **Clean accepted-commit repository checks:** `python -m pytest` reported
  `283 passed in 73.82s`; the checked-artifact verifier reported four
  certificates, 76 local brackets, and summary rows \(n=3,4,5,6\); focused
  schema pytest reported `4 passed in 0.80s`.
- **Clean accepted-commit hygiene:** empty porcelain status before and after;
  `git diff --check` and the accepted commit-delta whitespace check passed;
  the tracked trailing-whitespace search found no match; the tracked cache
  scan was empty; `origin/main` equaled the accepted SHA.
- **Hosted accepted-commit verification:** run `29777676234`, created
  `2026-07-20T20:48:56Z` and completed with `success`, has exactly the
  accepted SHA. Full pytest, checked-artifact verification, focused schema
  validation, and tracked-text whitespace steps succeeded in every matrix
  job.
- **Limitations:** bounded computation remains corroboration rather than an
  all-\(m\) proof. The local and hosted baseline results cover the accepted
  commit, while this later documentation-only record receives its own final
  diff and hygiene inspection.

## Blockers / Risks

- No blocker.
- Residual risk is limited to transcription of commit/run metadata; exact
  SHA-filtered run and job queries, plus local Git checks, agree.

## Next Atomic Action

- User review of this documentation-only post-review record. No further
  KRPGE5 mathematical action is queued.

## Handoff

- **Last verified result:** accepted commit
  `a15a4d34cc034b669f02382e2e4f27b4822ed382` has fresh local PASS results
  and a successful exact-SHA hosted Python 3.11--3.13 matrix.
- **Files changed:** current status, stable hosted provenance, roadmap
  routing, and the three documentary KRPGE5 dossier files; no proof, script,
  workflow, production, test, schema, or artifact file.
- **Files to read first:** this `TASK_STATUS.md`, EV-012 in `EVIDENCE.md`,
  and the final entry of `TASK_LOG.md`.
- **Suggested manual commit message:**
  `Close accepted KRPGE5 review provenance`.
- **Proposed next fresh task:** select one bounded item from the deferred
  roadmap; this closure does not choose or begin it.
