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

Definition: \(R_2^*(n)\) is the minimum feasible central radius.

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

Consequently the former target
\(R_2^*(n)=n^3/(6\pi)(1+o(1))\) is a disproved claim. The stronger target
\(R_2^*(n)=n^3/(6\pi)+O(n^2)\) is also a disproved claim.

The checked-artifact verification path is now a project foundation: the repository has a GitHub Actions matrix for tests, checked-artifact semantic verification, schema checks, and whitespace hygiene. Current task context reports the hosted workflow is green after the cross-platform finite-summary hash fix; this hosted status was not independently queried in the roadmap task.

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

The exact leading constant, any matching upper bound, and any asymptotic
equality theorem remain unresolved. The induced-subset lower bound proves only
a strict lower obstruction above the former \(1/(6\pi)\) coefficient; it does
not identify the exact asymptotic constant.

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
- EXACT THEOREM: within the induced-subset plus duplicated-pairing plus
  \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\) relaxation, no nonconsecutive subset
  improves the tail bounds \(P_{m,n}\); the best discrete tail is characterized
  by \(\rho_n=(\sqrt{8n^2+8n+1}-(2n+1))/2\), with adjacent ties exactly when
  \(\rho_n\) is an integer.
- VERIFIED FACT: checked-artifact verification is wired into local review and GitHub Actions.
- USER-REPORTED STATUS: current task context reports the hosted run is green after the CI fix.
- INTERPRETATION: these are finite certificates only; they are not exact optimum proofs, all-`n` theorems, or asymptotic results.
- INTERPRETATION: the all-`n` induced-subset lower-bound theorem is independent of the finite certificates and does not provide a matching upper bound.
- INTERPRETATION: the coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal for the
  documented relaxation only; it is not a proved exact asymptotic coefficient
  for Power-Ringmin.
- LIMITATION: the interval-backend trust/provenance limitation remains explicit and unresolved for public production claims.
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))\).
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)\).
