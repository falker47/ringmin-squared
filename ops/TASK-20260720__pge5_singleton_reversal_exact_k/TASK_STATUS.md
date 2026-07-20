# TASK_STATUS - TASK-20260720 / PGE5 Singleton-Reversal Exact K

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** correct the KRPGE5 theorem closure by applying the already
  proved exact label-one elimination and strict fixed-order/global
  sandwiches to the singleton-reversal core.
- **Expected output:** explicit KRPGE5 consequences for \(\Lambda\),
  \(\rho\), \(R_2^*\), and the one requested subsequence; exact task-local
  symbolic checks; synchronized durable memory; and no production or test
  change.

## Scope

- **In scope:** the fixed core (KRPGE5-1)--(KRPGE5-32), exact elimination
  (CR12p), the strict fixed-order sandwich (CR22), the strict global sandwich
  (CR27), the reduced global objective (CR28a), and task-local exact checks
  for the resulting closure (KRPGE5-33)--(KRPGE5-36).
- **Out of scope:** every other new bijection, Ferrers permanent, production
  or test changes, a minimizing-order or geometric-optimality theorem, a
  matching global lower bound, an all-\(n\) limsup bound, and an exact leading
  constant for the global optimum \(R_2^*\).

## Verified Facts

- Startup found a clean `main` worktree at the reviewed KRPGE5 baseline
  `bce6e4d8a935bd9d8509e59b760cf78c345779b6`.
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

## Assumptions / Inferences

- No unproved assumption is used. The all-\(m\) closure statements are exact
  deductions from proved theorems; bounded computation is classified only as
  corroboration.

## Decisions And Rationale

- Apply CR12p, CR22, CR27, and CR28a literally; do not introduce a new
  bijection or re-prove their real-arithmetic content inside KRPGE5.
- Keep the diagnostic task-local and standard-library-only. Check exact
  integer identities and elimination hypotheses, but do not approximate
  \(\pi\) or recast the angular sandwich as a numerical experiment.

## Implemented Delta

- Added the exact closure (KRPGE5-33)--(KRPGE5-36) to Section 21 and replaced
  overbroad angular/geometric negations with the precise limitations.
- Extended the existing standalone diagnostic with exact \(n\)-form,
  all-insertion-gap, and label-one elimination checks.
- Synchronized stable memory, current status, roadmap, and this STRICT
  dossier.
- Changed no production file or test.

## Verification

- **Local working-tree checks:** the updated standalone diagnostic passes on
  \(m=2,\ldots,30\), including 4,727 insertion gaps and 484,387 exact
  neighbor-pair inequalities; (KRPGE5-31) passes coefficientwise and formulas
  pass through \(m=1000\). The approved full pytest rerun reports `283
  passed`; focused schema and Arb suites report `4 passed` and `3 passed`;
  four certificates and 76 local brackets verify. The two preceding sandbox
  attempts are retained as environmental `tmp_path` permission failures in
  `EVIDENCE.md`.
- **Hosted CI baseline:** GitHub Actions run `29771633257` succeeded for
  commit `bce6e4d8a935bd9d8509e59b760cf78c345779b6` on Python 3.11--3.13.
  It verifies the reviewed KRPGE5-1--KRPGE5-32 baseline, not the present
  uncommitted closure correction.
- **Limitations:** bounded exact computation corroborates rather than proves
  the all-\(m\) theorem; the real-arithmetic sandwich is invoked from its
  proof, not numerically certified here; no hosted run can cover an
  uncommitted working tree.

## Blockers / Risks

- No blocker.
- Residual risk is external-review or transcription error in the four-step
  theorem application. Independent mathematical and document audits found
  none.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the exact closure, task-local symbolic checks,
  synchronized durable memory, and local/hosted provenance separation are
  complete.
- **Files changed:** proof note, stable memory, current status, roadmap, and
  the existing four-file KRPGE5 dossier; no production or test file.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` Section 21,
  `exact_diagnostic.py`, and `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Correct the KRPGE5 geometric closure`.
- **Proposed next fresh task:** after review and commit, audit
  KRPGE5-1--KRPGE5-36 and verify hosted CI for the corrected commit.
