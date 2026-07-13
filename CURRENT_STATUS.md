# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** the adjacent product-distance relaxation is characterized exactly; non-adjacent constraints first change the bounded optimum at `n=9` and are forced asymptotically.
- **Current task:** Characterize the adjacent product-distance relaxation and locate the first non-adjacent gap.
- **Task dossier:** `ops/TASK-20260713__adjacent_product_distance_relaxation/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Exact Result

For
\[
A_n=\min_\sigma\max_k\sigma_k\sigma_{k+1}
\]
on core cycles \(\{2,\dots,n\}\), the target formula is proved:
\[
A_3=6,
\qquad
A_n=
\left(\left\lfloor{n\over2}\right\rfloor+1\right)
\left(\left\lceil{n\over2}\right\rceil+2\right)
\quad(n\ge4).
\]
The lower bound counts internal edges between high and low blocks. The
existing `patterns.interleave` order realizes the upper bound for every
\(n\); its cyclic edge sums lie in \(\{n+1,n+2,n+3\}\).

Writing
\[
L_n=\max_{2\le m\le n-2}{P_{m,n}\over n-1},
\]
one has
\[
\lim_{n\to\infty}{A_n\over n^2}={1\over4}
< {2(\sqrt2-1)\over3}
=\lim_{n\to\infty}{L_n\over n^2}.
\]
The explicit tail \(m=\lceil2n/5\rceil\) proves \(L_n>A_n\) for every
\(n\ge33\). Exact rational formula evaluation gives \(L_n\le A_n\) for
\(4\le n\le32\), so `33` is the first index where this tail obstruction
alone forces a strict adjacent relaxation.

## Retained Full-Surrogate Context

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

For a cyclic core order \(\sigma\), define
\[
W(\sigma)=\max_{2\le i<j\le n}{ij\over d_\sigma(i,j)},
\qquad W_n=\min_\sigma W(\sigma).
\]
Assigning the order to regular directions is strictly all-pairs feasible at
\[
R={(n-1)W(\sigma)\over\pi}.
\]
For `n>=12`, insertion transfers this radius to the full problem. For every
`2<=m<=n-2`, oriented induced-tail positional gaps sum to `n-1` and prove
\[
W(\sigma)\ge {P_{m,n}\over n-1}.
\]

## Finite Exact Enumeration

VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the distance-one and
distance-two objectives for `n=3..11` are
\[
(W_3^{(\le1)},\dots,W_{11}^{(\le1)})
=(6,12,15,20,24,30,35,42,48),
\]
and
\[
W_n^{(\le2)}=W_n
\qquad(3\le n\le11).
\]
The first non-adjacent gap is
\[
A_9=35<36=W_9^{(\le2)}=W_9.
\]
The distance-two and full canonical minimizer sets also coincide in every
enumerated row. This proves that distance two is first essential at `n=9`;
distances at least three do not change the bounded values or minimizers.

VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the bounded, canonical,
no-floating-point enumeration for `n=3..11` gives
\[
(W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50)
\]
with canonical minimizer counts
\[
(1,1,1,2,2,4,12,72,24).
\]
The complete table, representatives, zigzag scores, and tail obstructions are
in `research/PRODUCT_DISTANCE_SURROGATE.md`. No all-`n` formula or geometric
optimality claim is inferred from this table.

The full-surrogate strictness question for `n=12..32` remains unresolved;
cyclic-order enumeration was not extended beyond `n=11`.

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

- HISTORICAL LOCAL VERIFIED FACT: the prior zigzag task's focused tests, full
  suite, checked-artifact verification, and mathematical review are recorded
  in `ops/TASK-20260713__zigzag_core_improved_upper_bound/`; those results are
  not hosted-run evidence. The current task's new local checks are listed
  separately below.
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
- PRIOR LOCAL VERIFIED FACT: the preceding documentation task recorded its own
  wording, path, UTF-8, whitespace, diff, and independent-review checks.
- PRIOR LOCAL VERIFIED FACT: focused product-distance/zigzag/tail/insertion
  tests passed `24/24`; full pytest passed `137/137`; checked-artifact semantic
  verification accepted 4 certificates, 76 local brackets, and the `n=3..6`
  summary.
- PRIOR LOCAL VERIFIED FACT: independent mathematical and code reviews found
  no defect, and a second implementation reproduced every `n=3..11` table
  entry without importing the new module or using its cutoff.
- PRIOR LOCAL VERIFIED FACT: final ten-path scope, strict UTF-8, trailing
  whitespace, complete diff, and `git diff --check` inspections passed.
- CURRENT LOCAL VERIFIED FACT: focused adjacent/product-distance/zigzag/tail
  tests passed `22/22`; the full suite passed `140/140`; checked-artifact
  semantic verification accepted 4 certificates, 76 local brackets, and the
  `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: an independent exact one-pass implementation
  reproduced all distance-one and distance-two objectives, minimizer counts,
  and representatives for `n=3..11`; 80 direct identities independently
  matched the ten residue polynomials used in the `n>=33` proof.
- CURRENT LOCAL VERIFIED FACT: the final 11-path scope, strict UTF-8,
  trailing-whitespace, 19 unique equation-tag, complete diff, and
  `git diff --check` inspections passed.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics.

Acceptance criteria:

- record the exact angular constraints and their monotonicity in `R`;
- prove the fixed-order STN/geometric feasibility equivalence used by current
  evaluators and verifiers;
- state lower negative-cycle and upper-witness endpoint semantics precisely;
- preserve the documented interval-backend trust boundary;
- do not begin another surrogate enumeration or generate new certificates.
