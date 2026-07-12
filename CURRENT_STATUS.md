# CURRENT_STATUS - power-ringmin

Last update: 2026-07-12

- **Current phase:** induced-subset lower-bound relaxation exactly characterized; exact Power-Ringmin asymptotic leading constant and matching upper bound remain open.
- **Current task:** Characterize the extremal subset-pairing lower bound and its exact discrete maximizer.
- **Task dossier:** `ops/TASK-20260712__subset_pairing_extremal_bound/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Stable Artifacts

`research/ALL_N_LOWER_BOUND.md` records the self-contained induced-subset lower
bound and the exact extremal characterization of the specific relaxation.

For \(S=\{s_1<\cdots<s_q\}\), the duplicated-multiset pairing value is
\[
A(S)=2\sum_{a=1}^t s_a s_{2t+1-a}\quad(q=2t),
\]
and
\[
A(S)=2\sum_{a=1}^t s_a s_{2t+2-a}+s_{t+1}^2\quad(q=2t+1).
\]

At fixed cardinality \(q\), \(A(S)\) is uniquely maximized by the tail
\[
\{n-q+1,\dots,n\}.
\]
Therefore no nonconsecutive subset improves the corresponding \(P_{m,n}\)
bound within the induced-subset plus duplicated-pairing plus
\(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\) relaxation.

For every `n>=4` and `1<=m<=n-2`,
\[
R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
\qquad
P_{m,n}
=
\sum_{k=m}^n k(m+n-k)
=
\frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
\]

The exact discrete maximizers of \(P_{m,n}\) over \(1\le m\le n-2\) are
characterized by
\[
\rho_n=\frac{\sqrt{8n^2+8n+1}-(2n+1)}2.
\]
For \(n\ge4\), the unique maximizer is \(\lfloor\rho_n\rfloor+1\) unless
\(\rho_n\in\mathbb Z\), in which case the two maximizers are
\(\rho_n,\rho_n+1\). For \(n=3\), the admissible set is the singleton \(m=1\).

Consequently the relaxation's best leading coefficient is exactly
\[
\frac{2(\sqrt2-1)}{3\pi}.
\]
This is optimal only within the named relaxation. It is not a matching upper
bound and not a proved exact asymptotic coefficient for Power-Ringmin.

The all-\(n\) lower bound still implies
\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
\ge
4(\sqrt2-1)>1.
\]
Thus the former conjectural target
\[
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))
\]
is a DISPROVED CLAIM, and the former stronger target
\[
R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)
\]
is also a DISPROVED CLAIM.

`tests/test_induced_subset_lower_bound.py` now contains finite diagnostic tests
using integer arithmetic for the explicit \(A(S)\) formula, exhaustive small-`n`
fixed-cardinality tail optimality, exact \(\rho_n\)-based discrete maximizers,
and pairing bounds on sample nonconsecutive subsets and induced orders. These
tests are finite verifications only; they are not the all-\(n\) proof.

`research/FINITE_RESULTS.md` summarizes the checked finite results and now
labels the ratio to `n^3/(6*pi)` as a legacy diagnostic baseline only.

`docs/INTERVAL_BACKEND_TRUST.md` records that the checked finite interval
backend does not prove exact optima, matching upper bounds, asymptotic equality,
or exact leading constants. The all-\(n\) induced-subset theorem is independent
of that backend.

`research/NEXT_RESEARCH_STEPS.md` is the current research roadmap. It no longer
proposes a diagnostic `n=3..6` comparison table as the next task; the
recommended next atomic task is to document fixed-order STN/geometric
equivalence and endpoint semantics.

`examples/finite_results_summary_n3_n6.json` remains the checked derived
finite-results summary under `power-ringmin.finite_results_summary.v1`.

## Verification

- `python -m pytest tests\test_induced_subset_lower_bound.py` passed: 7 tests.
- `python -m pytest` passed: 117 tests.
- `python -m power_ringmin.verify_checked_artifacts` failed before setting
  `PYTHONPATH` because the local package was not importable from site-packages.
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  passed: 4 checked certificates, 76 embedded local brackets, summary
  `examples/finite_results_summary_n3_n6.json` for `n=3,4,5,6`.

## Current Research Finding

The best lower bound obtainable from the named relaxation has now been
characterized exactly. The result eliminates nonconsecutive subsets as a source
of improvement inside that relaxation and gives an exact integer-discrete
maximizer rule. It does not solve the exact Power-Ringmin asymptotic constant.

## Proposed Next Task

Document the fixed-order STN/geometric equivalence and endpoint semantics used
by the verifier, independently of any particular asymptotic constant.

Acceptance criteria:

- state the fixed-order angular/STN feasibility equivalence;
- state lower-endpoint negative-cycle and upper-endpoint witness semantics;
- separate exact mathematical implications from interval-backend trust
  assumptions;
- do not generate certificates, create `n=3..6` diagnostic tables, start
  upper-bound construction, run leading-order LP, or begin `n=7`.
