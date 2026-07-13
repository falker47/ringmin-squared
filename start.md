# Power-Ringmin: Quadratic Radii

Working repository name: `power-ringmin`

Author: Maurizio Falconi

Status: independent mathematical research project

This file is the authoritative project brief.

## Summary

Power-Ringmin studies the quadratic-radii extension of Ringmin. Given peripheral circles with radii

\[
1^2,2^2,\dots,n^2,
\]

place all of them externally tangent to one central circle while requiring pairwise-disjoint peripheral interiors.

Definition: \(R_2^*(n)\) is the infimum feasible central radius. No general
attainment assumption is needed for the current theorems.

The quadratic-radii computational foundation has been implemented. Checked finite interval certificate artifacts currently exist for `n=3,4,5,6`; they provide finite global radius brackets under the documented guarded `mpmath.iv` interval-backend contract.

A strengthened all-`n` mathematical lower bound has been proved from induced
subsets of cyclic gaps. For every `n>=4` and `1<=m<=n-2`,

\[
R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
\qquad
P_{m,n}
=
\sum_{k=m}^n k(m+n-k)
=
\frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
\]

Choosing \(m=\lceil(\sqrt2-1)n\rceil\) gives

\[
R_2^*(n)
\ge
\frac{2(\sqrt2-1)}{3\pi}n^3-O(n^2),
\]

and therefore

\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
\ge
4(\sqrt2-1)>1.
\]

The method has now been characterized exactly: for a fixed subset cardinality,
the duplicated-multiset pairing bound is uniquely maximized by the largest
indices \(\{n-q+1,\dots,n\}\), and the remaining discrete maximum over tails is
governed by
\[
\rho_n=\frac{\sqrt{8n^2+8n+1}-(2n+1)}2.
\]
Thus \(2(\sqrt2-1)/(3\pi)\) is optimal only within this specific lower-bound
relaxation, not necessarily for Power-Ringmin itself.

There is also an exact eventual radius-one insertion theorem. Let
\(R^*_{2:n}\) be the infimum feasible central radius for only the core radii
\(2^2,\dots,n^2\). A core configuration at radius \(R\) admits insertion of
the radius-\(1\) circle whenever
\[
\sum_{j=2}^n\theta_R(1,j^2)<\pi.
\]
Rigorous angular majorants combined with the configuration-level
induced-subset lower bound prove
\[
R_2^*(n)=R^*_{2:n}\qquad(n\ge12).
\]
In fact, the full and core feasible-radius sets coincide in that range. The
threshold \(12\) is sufficient and is not claimed minimal; the proof is
independent of the checked cases \(n=5,6\).

For every \(n\ge12\), assigning the core centers to the equally spaced polar
directions of a regular \((n-1)\)-gon gives the order-independent all-pairs
feasible baseline
\[
U_n
=
\sqrt{
n^2(n-1)^2\csc^2\!\left(\frac{\pi}{n-1}\right)
+\frac{(2n-1)^2}{4}}
-\frac{n^2+(n-1)^2}{2}.
\]
The zigzag assignment \((n,2,n-1,3,\dots)\) sharpens this baseline. Defining
\[
M_n=n\left(\left\lfloor\frac n2\right\rfloor+1\right),
\qquad
V_n=\frac{(n-1)M_n}{\pi},
\]
an exact product-distance lemma proves that every core pair is feasible at
\(V_n\). The insertion theorem therefore gives
\[
R_2^*(n)\le V_n\qquad(n\ge12),
\]
and \(V_n/n^3\to1/(2\pi)\). Combined with the induced-subset lower bound,
this settles the order of growth:
\[
R_2^*(n)=\Theta(n^3).
\]
The proof, including the general angular majorant, zigzag closing arc, every
non-adjacent constraint, and the earlier baseline, is recorded in
`research/ALL_N_LOWER_BOUND.md`.

The regular-direction construction now has an exact combinatorial surrogate.
For a cyclic core order \(\sigma\), let \(d_\sigma(i,j)\) be smaller circular
positional distance and define
\[
W(\sigma)=\max_{2\le i<j\le n}{ij\over d_\sigma(i,j)},
\qquad W_n=\min_\sigma W(\sigma).
\]
The core is strictly all-pairs feasible at \((n-1)W(\sigma)/\pi\), and the
accepted insertion theorem transfers this radius to the full problem for
\(n\ge12\). For every \(2\le m\le n-2\), oriented positional gaps on the
induced tail prove the exact obstruction
\[
W(\sigma)\ge {P_{m,n}\over n-1}.
\]
An exact, no-floating-point canonical enumeration bounded to `n=3..11` gives
\[
(W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50),
\]
with canonical minimizer counts \((1,1,1,2,2,4,12,72,24)\). The proof,
complete table, representatives, and finite/all-`n` classification are in
`research/PRODUCT_DISTANCE_SURROGATE.md`.

Consequently the former target
\(R_2^*(n)=n^3/(6\pi)(1+o(1))\) is a disproved claim. The stronger target
\(R_2^*(n)=n^3/(6\pi)+O(n^2)\) is also a disproved claim.

The checked-artifact verification path is now a project foundation: the
repository has a GitHub Actions matrix for tests, checked-artifact semantic
verification, schema checks, and whitespace hygiene. Successful local checks
are recorded in the trust-layer and cross-platform hash task dossiers. The
later green hosted-run statement was user-reported without a commit SHA, run
identifier, URL, or independent inspection, so it establishes no hosted
status for a specific commit. GitHub Actions status for the current `HEAD` has
not been independently verified.

## Asymptotic Status

DISPROVED CLAIM:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}\bigl(1+o(1)\bigr).
\]

DISPROVED CLAIM:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}+O(n^2).
\]

The cubic order is exact, but existence of a limiting coefficient, a
leading-term asymptotic formula, and an upper bound matching the induced-subset
lower coefficient remain unresolved. Current exact bounds give
\[
\frac{2(\sqrt2-1)}{3\pi}
\le
\liminf_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le
\limsup_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le\frac1{2\pi}.
\]

## Scope And Guardrails

In scope:

- the two-dimensional quadratic-radii problem;
- exact geometric formulation;
- cyclic orders and all-pairs non-overlap constraints;
- numerical optimization and independent verification;
- certified finite cases where feasible;
- asymptotic lower and upper bound research.

Out of scope:

- treating finite computation as a proof for all `n`;
- treating checked brackets as exact optimum values;
- silently generalizing Ringmin results to quadratic radii;
- modifying the original Ringmin repository.

## Angular Constraint

For peripheral radii \(r_i,r_j\) and central radius \(R\), the minimum angular separation is

\[
\theta_R(r_i,r_j)
=
2\arcsin
\sqrt{
\frac{r_i r_j}
{(R+r_i)(R+r_j)}
}.
\]

For quadratic radii:

\[
\theta_R(i^2,j^2)
=
2\arcsin
\left(
\frac{ij}
{\sqrt{(R+i^2)(R+j^2)}}
\right).
\]

All-pairs non-overlap constraints are part of the problem, not merely adjacent-pair constraints.

## Current Knowledge Status

- COMPUTER-CERTIFIED RESULT: checked finite global interval brackets exist for `n=3,4,5,6` under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` backend contract.
- EXACT THEOREM: for every `n>=3`,
  \[
  R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2,
  \]
- EXACT THEOREM: for every `n>=4` and `1<=m<=n-2`,
  \[
  R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
  \qquad
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  \frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
  \]
- EXACT THEOREM:
  \[
  \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
  \ge
  4(\sqrt2-1)>1.
  \]
- EXACT THEOREM: if \(R^*_{2:n}\) denotes the core infimum, then
  \(R_2^*(n)=R^*_{2:n}\) for every \(n\ge12\), with equality already at the
  level of feasible-radius sets.
- EXACT THEOREM: the core with polar directions from a regular
  \((n-1)\)-gon is all-pairs feasible at the displayed radius \(U_n\),
  including all non-adjacent direction pairs, and the radius-one theorem gives
  \(R_2^*(n)\le U_n\) for every \(n\ge12\).
- EXACT THEOREM: for \(R>0\) and positive indices \(i,j\),
  \(\theta_R(i^2,j^2)<2ij/R\). In the zigzag core order
  \((n,2,n-1,3,\dots)\), indices at circular distance \(q\) satisfy
  \(ij\le qM_n\), where
  \(M_n=n(\lfloor n/2\rfloor+1)\). Hence the regular-direction core is
  all-pairs feasible at \(V_n=(n-1)M_n/\pi\), and
  \(R_2^*(n)\le V_n\) for every \(n\ge12\).
- EXACT THEOREM:
  \[
  \limsup_{n\to\infty}\frac{R_2^*(n)}{n^3}\le\frac1{2\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
- EXACT THEOREM: for every cyclic order \(\sigma\) of the core, the
  product-distance score
  \(W(\sigma)=\max_{i<j}ij/d_\sigma(i,j)\) gives strict all-pairs core
  feasibility at \((n-1)W(\sigma)/\pi\). For `n>=12`, insertion gives
  \(R_2^*(n)\le(n-1)W_n/\pi\), where \(W_n=\min_\sigma W(\sigma)\).
- EXACT THEOREM: for every `2<=m<=n-2`, oriented positional gaps induced by
  the tail \(\{m,\dots,n\}\) give
  \(W(\sigma)\ge P_{m,n}/(n-1)\).
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): bounded canonical
  enumeration with integer/Fraction scoring gives
  \((W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50)\) and canonical
  minimizer counts \((1,1,1,2,2,4,12,72,24)\). This is not an all-`n`
  formula, a geometric certificate, or an exact geometric-optimum claim.
- EXACT THEOREM: within the induced-subset plus duplicated-pairing plus
  \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\) relaxation, no nonconsecutive subset
  improves the tail bounds \(P_{m,n}\); the best discrete tail is characterized
  by \(\rho_n=(\sqrt{8n^2+8n+1}-(2n+1))/2\), with adjacent ties exactly when
  \(\rho_n\) is an integer.
- VERIFIED FACT (WORKFLOW CONFIGURATION): checked-artifact verification is
  wired into local review and `.github/workflows/verification.yml`.
- LOCAL VERIFIED FACT: successful local tests, checked-artifact verification,
  workflow inspection, and hygiene checks are recorded in
  `ops/TASK-20260712__verification_trust_layer_ci/` and
  `ops/TASK-20260712__cross_platform_finite_hash_ci/`; these are not hosted-run
  results.
- HISTORICAL USER-REPORTED STATUS: the 2026-07-12 roadmap task recorded a green
  hosted run after the cross-platform fix, but no commit SHA, run identifier,
  URL, or independently inspected result was recorded; it establishes no
  hosted status for a specific commit.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.
- INTERPRETATION: these are finite certificates only; they are not exact optimum proofs, all-`n` theorems, or asymptotic results.
- INTERPRETATION: the all-`n` theorems and regular-direction constructions are
  independent of the finite certificates; the upper and lower leading
  coefficients do not currently match.
- INTERPRETATION: the coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal for the
  documented relaxation only; it is not a proved exact asymptotic coefficient
  for Power-Ringmin.
- LIMITATION: the interval-backend trust/provenance limitation remains explicit and unresolved for public production claims.
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))\).
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)\).
