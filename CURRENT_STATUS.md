# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** exact eventual radius-one insertion proved; exact asymptotic leading constant, matching upper bound, and minimal insertion threshold remain open.
- **Current task:** Prove or disprove an exact radius-one insertion lemma and derive an explicit equality threshold for the full and core infima.
- **Task dossier:** `ops/TASK-20260713__radius_one_insertion/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Stable Result

Let
\[
\mathcal F_n
=\{R>0:1^2,\dots,n^2\text{ are feasible at }R\}
\]
and
\[
\mathcal C_n
=\{R>0:2^2,\dots,n^2\text{ are feasible at }R\}.
\]
Define
\[
R_2^*(n)=\inf\mathcal F_n,
\qquad
R^*_{2:n}=\inf\mathcal C_n.
\]

EXACT THEOREM: a feasible core configuration at radius \(R>0\) admits a
circle of radius \(1\) at the same central radius whenever
\[
\sum_{j=2}^n\theta_R(1,j^2)<\pi.
\]
The proof assigns to every core circle an open forbidden angular arc of measure
\(2\theta_R(1,j^2)\), uses subadditivity of arc measure, and explicitly checks
all new pairs \((1,j^2)\), the new central tangency, and the unchanged core
pairs.

EXACT THEOREM: for every \(n\ge12\),
\[
\mathcal F_n=\mathcal C_n
\quad\text{and hence}\quad
R_2^*(n)=R^*_{2:n}.
\]
The proof combines
\[
\theta_R(1,j^2)
<\frac{2j}{\sqrt{R(R+j^2+1)}}
<\frac{2j}{R}
\]
with the already-proved configuration-level induced-subset lower bound.
Exact rational estimates cover `n=12,13`; a symbolic parity inequality covers
all `n>=14`.

The threshold `12` is sufficient, not claimed minimal. Failure of the current
bound chain to close `n<=11` is not a counterexample. The theorem does not use
the checked `n=5,6` structures as evidence and assumes no minimizer: it proves
equality of feasible-radius sets before taking infima.

## Other Stable Context

`research/ALL_N_LOWER_BOUND.md` also retains the exact induced-subset lower
bound and its extremal characterization. In particular,
\[
R_2^*(n)\ge\frac{P_{m,n}}\pi-n^2
\]
for the documented range, and the best leading coefficient within that
specific relaxation is \(2(\sqrt2-1)/(3\pi)\). This is not a matching upper
bound or an exact asymptotic coefficient.

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

- `python -m pytest tests\test_radius_one_insertion.py tests\test_induced_subset_lower_bound.py` passed: 12 tests.
- `python -m pytest` passed: 122 tests.
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  passed: 4 checked certificates, 76 embedded local brackets, and summary
  `examples/finite_results_summary_n3_n6.json` for `n=3,4,5,6`.
- Independent proof review found no actionable defect in the geometry,
  inequalities, threshold algebra, or infimum handling.
- `git diff --check` passed; final status and diff were inspected.

## Proposed Next Task

Document the fixed-order STN/geometric equivalence and endpoint semantics used
by the verifier, independently of any particular asymptotic constant.

Acceptance criteria:

- state the fixed-order angular/STN feasibility equivalence;
- state lower-endpoint negative-cycle and upper-endpoint witness semantics;
- separate exact mathematical implications from interval-backend trust
  assumptions;
- do not generate certificates, begin exhaustive enumeration, start an
  upper-bound construction, or claim that the insertion threshold is minimal.
