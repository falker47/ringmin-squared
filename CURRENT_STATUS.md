# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** cubic order proved; the zigzag regular-direction construction now gives the best proved limsup upper coefficient, while coefficient matching and the minimal insertion threshold remain open.
- **Current task:** Prove and integrate the improved zigzag cubic upper bound.
- **Task dossier:** `ops/TASK-20260713__zigzag_core_improved_upper_bound/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Stable Result

EXACT THEOREM: for every \(R>0\) and positive indices \(i,j\),
\[
\theta_R(i^2,j^2)<\frac{2ij}{R}.
\]
For
\[
M_n=n\left(\left\lfloor\frac n2\right\rfloor+1\right),
\]
the core zigzag order
\[
z_n=(n,2,n-1,3,\dots)
\]
has the exact all-pairs property \(ij\le qM_n\) whenever \(i,j\) are at
smaller circular positional distance \(q\). The closing arc has the maximum
adjacent product, exactly \(M_n\); every other adjacent product is smaller for
\(n\ge4\), and every \(q\ge2\) pair follows from
\[
ij\le n(n-1)<2M_n\le qM_n.
\]

Assigning this order to the polar directions of a regular \((n-1)\)-gon is
strictly all-pairs feasible at
\[
V_n=\frac{(n-1)M_n}{\pi}.
\]
The accepted radius-one insertion theorem therefore gives
\[
R_2^*(n)\le V_n\qquad(n\ge12),
\]
without assuming attainment. Consequently,
\[
\limsup_{n\to\infty}\frac{R_2^*(n)}{n^3}\le\frac1{2\pi}.
\]
This is a limsup upper coefficient, not an exact leading constant.

## Other Stable Context

The prior order-independent regular-direction radius \(U_n\) remains a valid
baseline with coefficient \(1/\pi\). The induced-subset lower theorem still
gives
\[
\frac{2(\sqrt2-1)}{3\pi}
\le
\liminf_{n\to\infty}\frac{R_2^*(n)}{n^3}.
\]
Thus the exact leading coefficient, existence of a limit, and a
coefficient-matching construction remain open.

The full and core feasible-radius sets remain equal for every \(n\ge12\) by
the accepted insertion theorem. The threshold `12` is sufficient, not claimed
minimal. The former \(n^3/(6\pi)\) asymptotic targets remain disproved.

## Verification

- Focused zigzag, prior-upper-bound, and insertion diagnostics passed: 11 tests.
- `python -m pytest` passed: 128 tests.
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  passed: 4 checked certificates, 76 embedded local brackets, and the
  `n=3..6` derived summary.
- Independent final mathematical and diagnostic review passed.
- Final Git status, diff, whitespace, and trailing-whitespace checks passed.

## Proposed Next Task

Document the fixed-order STN/geometric equivalence and endpoint semantics used
by the verifier, independently of any particular asymptotic constant.

Acceptance criteria:

- state the fixed-order angular/STN feasibility equivalence;
- state lower-endpoint negative-cycle and upper-endpoint witness semantics;
- separate exact mathematical implications from interval-backend trust
  assumptions;
- do not generate certificates, begin exhaustive enumeration, optimize the
  zigzag upper bound, or claim that the insertion threshold is minimal.
