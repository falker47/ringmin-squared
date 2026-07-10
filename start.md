# Power-Ringmin: Quadratic Radii

Working repository name: `power-ringmin`

Author: Maurizio Falconi

Status: independent mathematical research project

This file is the authoritative project brief.

## Summary

Power-Ringmin studies the following extension of the original Ringmin problem.

Given peripheral circles with radii

\[
1^2,2^2,\dots,n^2,
\]

place all of them externally tangent to one central circle, while requiring that the interiors of all peripheral circles are pairwise disjoint.

Definition: \(R_2^*(n)\) is the minimum feasible radius of the central circle.

## Main Research Target

Conjecture:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}\bigl(1+o(1)\bigr).
\]

This is a conjecture and heuristic target, not an established theorem.

Possible stronger research direction:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}+O(n^2).
\]

This stronger statement is currently an unresolved possible direction, not a theorem.

## Motivation

The project was selected because it combines:

- a geometrically explicit optimization problem;
- reusable ideas from Ringmin;
- finite computational experiments;
- possible certified finite results;
- opportunities for counterexample search;
- a plausible route from numerical evidence to rigorous proof;
- suitability for AI-assisted work through Codex.

## Relevant Prior Work

Verified fact from the project prompt and read-only upstream inspection: Maurizio Falconi previously created the Ringmin repository and developed the original problem for peripheral radii

\[
1,2,\dots,n.
\]

Read-only upstream inspection found mathematical results, code, tests, optimization methods, STN-based angular feasibility methods, computational certificates, figures, and paper material in Ringmin.

Ringmin must be treated as prior work and as a read-only upstream reference.

No Ringmin theorem, implementation assumption, or observed structural pattern may be silently generalized to quadratic radii.

## Initial Scope

In scope:

- the two-dimensional quadratic-radii problem;
- exact geometric formulation;
- cyclic orders;
- contact structures;
- floating circles;
- all-pairs non-overlap constraints;
- numerical optimization;
- STN or equivalent angular feasibility methods;
- exhaustive small-case searches;
- certified finite cases where feasible;
- asymptotic lower and upper bounds;
- reproducible experiments;
- rigorous proof development.

Initially out of scope:

- arbitrary exponents \(k^\alpha\);
- three-dimensional sphere problems;
- immediate creation of a shared Ringmin core library;
- publication claims;
- modifying the original Ringmin repository;
- treating finite computation as a general proof.

## Angular Constraint

Definition: for peripheral radii \(r_i\) and \(r_j\), and central radius \(R\), the minimum angular separation is

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

## Current Heuristic

Heuristic: in the expected regime \(R\asymp n^3\),

\[
\theta_R(i^2,j^2)
\approx
\frac{2ij}{R}.
\]

Heuristic: a Supnick-type or alternating chain is expected to generate a leading adjacent weight of order

\[
\sum ij \sim \frac{n^3}{6},
\]

suggesting

\[
R_2^*(n)\sim \frac{n^3}{6\pi}.
\]

This reasoning is heuristic until the following are controlled rigorously:

- the correct optimal or asymptotically optimal cyclic order;
- all non-adjacent constraints;
- floating circles;
- uniform approximation errors;
- a matching globally feasible construction.

## Desired Outcomes

Minimum viable outcome:

- an independent reproducible repository;
- a radius-sequence-aware computational pipeline;
- reliable quadratic-radii experiments;
- all-pairs validation;
- exact or certified small cases;
- explicit separation between observations and proofs.

Target outcome:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}\bigl(1+o(1)\bigr)
\]

with a rigorous proof.

Long-term outcomes may include:

- a quantitative error bound;
- characterization of floating circles or contact regimes;
- later extension to \(r_k=k^\alpha\).

## Knowledge Classification

Current established content in this repository is limited to definitions, project scope, upstream provenance, and operating rules. No quadratic-radii theorem, numerical result, certified result, or implementation result has yet been established here.

Material claims must be labeled where relevant as definition, verified fact, exact theorem, computer-certified result, numerical observation, empirical pattern, heuristic, conjecture, unresolved claim, or disproved claim.

