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

An all-`n` mathematical lower bound has been proved from adjacent cyclic gaps:
for every `n>=3`,

\[
R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2,
\]

and therefore

\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}\ge 1.
\]

The checked-artifact verification path is now a project foundation: the repository has a GitHub Actions matrix for tests, checked-artifact semantic verification, schema checks, and whitespace hygiene. Current task context reports the hosted workflow is green after the cross-platform finite-summary hash fix; this hosted status was not independently queried in the roadmap task.

## Main Research Target

Conjecture:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}\bigl(1+o(1)\bigr).
\]

This remains open. No exact optimum value, matching upper bound, or asymptotic
equality theorem has been proved in this repository.

The matching upper-bound direction remains open. The all-`n` lower-bound theorem
proves only the lower asymptotic inequality
\(\liminf 6\pi R_2^*(n)/n^3\ge 1\), not the conjectured asymptotic equality.

Possible stronger research direction:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}+O(n^2).
\]

This stronger statement is also unresolved.

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
  hence \(\liminf_{n\to\infty}6\pi R_2^*(n)/n^3\ge 1\).
- VERIFIED FACT: checked-artifact verification is wired into local review and GitHub Actions.
- USER-REPORTED STATUS: current task context reports the hosted run is green after the CI fix.
- INTERPRETATION: these are finite certificates only; they are not exact optimum proofs, all-`n` theorems, or asymptotic results.
- INTERPRETATION: the all-`n` lower-bound theorem is independent of the finite certificates and does not provide a matching upper bound.
- LIMITATION: the interval-backend trust/provenance limitation remains explicit and unresolved for public production claims.
- CONJECTURE: \(R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))\) remains open.
