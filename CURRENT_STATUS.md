# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** cubic order proved by induced-subset lower and regular-core upper bounds; exact leading constant, coefficient matching, and the minimal insertion threshold remain open.
- **Current task:** Prove a constructive cubic upper bound using a regular core configuration.
- **Task dossier:** `ops/TASK-20260713__regular_core_cubic_upper_bound/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Stable Result

EXACT THEOREM: for every \(n\ge12\) and fixed \(R>0\), the largest required
angular separation among distinct core radii \(2^2,\dots,n^2\) is attained by
\(((n-1)^2,n^2)\). Assigning the core centers to the equally spaced polar
directions of a regular \((n-1)\)-gon is all-pairs feasible at
\[
U_n
=
\sqrt{
n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
+{(2n-1)^2\over4}}
-{n^2+(n-1)^2\over2}.
\]
Every non-adjacent vertex pair is included: its smaller angular separation is
at least one polygon edge, while every required separation is at most the
tight worst-pair edge angle.

The accepted radius-one theorem gives
\[
R_2^*(n)\le U_n\qquad(n\ge12).
\]
Moreover,
\[
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{1\over\pi}.
\]
Combining this with the existing induced-subset lower bound proves
\[
R_2^*(n)=\Theta(n^3).
\]
The self-contained proof is in `research/ALL_N_LOWER_BOUND.md`. It does not
claim an exact leading constant or assume that an infimum is attained.

## Other Stable Context

`research/ALL_N_LOWER_BOUND.md` also retains the exact induced-subset lower
bound and its extremal characterization. In particular,
\[
R_2^*(n)\ge\frac{P_{m,n}}\pi-n^2
\]
for the documented range, and the best leading coefficient within that
specific relaxation is \(2(\sqrt2-1)/(3\pi)\). This does not match the regular
core's \(1/\pi\) upper coefficient, so existence and value of any limiting
coefficient remain open.

The full and core feasible-radius sets remain exactly equal for every
\(n\ge12\), by the accepted forbidden-arc insertion theorem. The threshold
`12` is sufficient, not claimed minimal, and the theorem assumes no minimizer.

The former targets
\[
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))
\quad\text{and}\quad
R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)
\]
remain DISPROVED CLAIMS.

`research/FINITE_RESULTS.md` keeps the checked `n=3..6` results and finite
critical-structure diagnostics separate from the exact eventual insertion
theorem. `research/NEXT_RESEARCH_STEPS.md` is the aligned research roadmap.

## Verification

- Focused regular-core diagnostics passed: 3 tests.
- `python -m pytest` passed: 125 tests.
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  passed: 4 checked certificates, 76 embedded local brackets, and summary
  `examples/finite_results_summary_n3_n6.json` for `n=3,4,5,6`.
- Independent final proof review found no mathematical or test defect after
  clarifying that the construction uses regular-polygon polar directions.
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
  regular-core bound, or claim that the insertion threshold is minimal.
