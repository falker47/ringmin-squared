# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** cubic order proved; the next research priority is the product-distance surrogate for regular-direction constructions, while coefficient matching and the minimal insertion threshold remain open.
- **Current task:** Align the operating contract, CI-status provenance, and next-task roadmap.
- **Task dossier:** `ops/TASK-20260713__align_contract_state_provenance/`.
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

## Verification And CI Provenance

- LOCAL VERIFIED FACT: the prior zigzag task's focused tests, full suite,
  checked-artifact verification, and mathematical review are recorded in
  `ops/TASK-20260713__zigzag_core_improved_upper_bound/`. This documentation
  task did not rerun them and does not reinterpret them as hosted results.
- LOCAL VERIFIED FACT: the trust-layer and cross-platform hash CI dossiers
  record successful local tests, checked-artifact verification, workflow
  inspection, and hygiene checks.
- VERIFIED FACT (WORKFLOW CONFIGURATION):
  `.github/workflows/verification.yml` defines the GitHub Actions verification
  matrix.
- HISTORICAL USER-REPORTED STATUS: the 2026-07-12 roadmap task recorded a green
  hosted run after the cross-platform fix, but no commit SHA, run identifier,
  URL, or independently inspected result was recorded; it establishes no
  hosted status for a specific commit.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.
- Current documentation checks passed: required wording, obsolete-wording
  absence, referenced paths, UTF-8 reads, trailing whitespace,
  `git diff --check`, independent review, and final scope/diff inspection.

## Proposed Next Task

Formalize and analyze the product-distance combinatorial surrogate induced by
assigning the core indices to regular directions.

Acceptance criteria:

- define the cyclic product-distance objective and its domain precisely;
- determine its precise implications and limitations for all-pairs feasibility
  within the regular-direction construction class, and prove every claimed
  implication;
- analyze the zigzag assignment and structured alternatives while separating
  exact results, finite diagnostics, conjectures, and open questions;
- do not generate certificates or begin unrestricted exhaustive permutation
  enumeration;
- keep fixed-order STN/geometric equivalence and endpoint documentation as a
  separate subsequent certification-debt task.
