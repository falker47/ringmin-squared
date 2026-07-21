# TASK_STATUS - TASK-20260721 / KR1 Monotone All-Index Lift

Last update: 2026-07-21

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** lift the exact KR1 residue-one upper construction to every
  integer \(n\ge7\) by label cancellation, and update all authoritative
  global upper-coefficient statements.
- **Expected output:** an exact monotonicity proof, explicit
  \(N(n)=5\lceil(n-1)/5\rceil+1\) with \(0\le N(n)-n\le4\), the all-index
  limsup bounds \(857/3000\) and \(857/(3000\pi)\), synchronized sources,
  and one small exact-integer diagnostic.

## Scope

- **In scope:** cancellation monotonicity for \(\Lambda\); the original KR1
  domain; all ten lifted residue classes; both KR1 formula branches;
  one-sided geometric and limsup consequences; authoritative documentation.
- **Out of scope:** new order families; new finite-prefix extensions;
  production or public-test changes; optimality, convergence, exact global
  constants, minimizing-order classification, or a transferred global lower
  bound.

## Verified Facts

- The startup worktree was clean on `main`; the prior task was
  `READY_FOR_REVIEW` with no uncommitted files.
- For \(3\le n\le N\), cancellation preserves every induced-subset score on
  the retained labels, so \(\Lambda_n\le\Lambda_N\).
- For the prescribed \(N(n)\), the sharp usable lift domain is \(n\ge7\):
  \(N(6)=6\) is outside the proved KR1 domain, while \(N(7)=11\) is the first
  admitted KR1 row.

## Plan And Expected Delta

- Prove and audit the cancellation lift in the authoritative cyclic-ratio
  note. DONE.
- Correct every authoritative current-best or KR1 non-improvement statement.
  DONE.
- Add and run the bounded exact-integer diagnostic. DONE.
- Run full repository verification and final diff review. DONE.

## Verification

- **Checks:** exact-integer diagnostic; Ruff check and format check; full
  pytest; checked-artifact semantic verification; focused schema tests;
  equation-tag, local-link, stale-claim, Git diff, and whitespace audits.
- **Observed result:** diagnostic PASS; Ruff PASS; 283 tests PASS; four
  certificates, 76 local brackets, and the derived summary verify; four
  focused schema tests PASS; 40 unique in-file KR1 tags and all final source,
  link, diff, and whitespace audits PASS.
- **Limitations:** the bounded diagnostic corroborates residue/formula
  arithmetic only; the written cancellation argument is the all-index proof.

## Blockers / Risks

- No blocker. The main risks are accidentally using the unsupported \(k=1\)
  algebraic row, treating normalized scores as monotone, or overstating the
  one-sided upper bound as optimality, convergence, or an exact constant.

## Next Atomic Action

- User review and manual commit decision.
