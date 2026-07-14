# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** exact residue-class classification of the product-distance
  surrogates.
- **Current task:** construct and prove a search-free matching order in the
  class \(n\equiv2\pmod5\).
- **Task dossier:**
  ops/TASK-20260714__residue_two_exact_construction/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Residue-Two Construction

Write

\[
n=5k+2,\qquad k\ge2,\qquad d=4k+4,\qquad
J_n={d(d-2)\over2}.
\]

EXACT THEOREM: there is an explicit parity-aware cyclic core order
\(\sigma_n^{(2)}\), generated with integer arithmetic and no search, such that

\[
W(\sigma_n^{(2)})=J_n.
\]

With \(D=d-1=4k+3\) and \(t=\lceil k/2\rceil\), its terminal and low labels
are

\[
E_j=D+j,\qquad
\lambda_j=2k-2j,\qquad
\rho_j=2k+1-2j.
\]

The first \(t\) middle paths are

\[
P_j=(D-1-2j,\ 2k+2+j,\ D-2-2j),
\]

and the residual interval is partitioned into singleton paths when \(k\) is
odd, or one doubleton followed by singleton paths when \(k\) is even. The
cycle is

\[
\sigma_n^{(2)}
=
\bigoplus_{j=0}^{k-1}(E_j,\lambda_j,P_j,\rho_{j+1}),
\]

with the \(\rho\)-subscript read modulo \(k\).

## Exact Consequence

The accepted saturation obstruction gives

\[
B_{12}\ge60=J_{12},
\qquad
B_n\ge J_n
\quad(n\equiv2\pmod5,\ n\ge17).
\]

The matching order supplies the reverse upper bound. Therefore

\[
\boxed{B_n=W_n=J_n}
\]

at \(n=12\) and for every \(n\equiv2\pmod5\), \(n\ge17\). Together with the
previous residue-class constructions,

\[
B_n=W_n=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
d_n(d_n-2)/2,&n\equiv2\pmod5
\end{cases}
\qquad(n\ge9).
\]

The \(n=7\) value remains covered by the bounded exact table.

## Proof Separation

- Permutation coverage is proved from five disjoint integer intervals and the
  separate even/odd residual-path cardinalities.
- The maximum adjacent product is exactly \(J_n\), attained by
  \((D-1,2k+2)\).
- The exact maximum product at positional distance two is \(D(D-1)<2J_n\).
- No terminal-terminal pair occurs at positional distance three, and
  \(3J_n-n(D-1)=4k^2+18k+8>0\).
- Every pair crossing the displayed cut is listed separately at distances one,
  two, and three.
- For every distance \(q\ge4\),
  \[
  ij\le n(n-1)<4J_n\le qJ_n
  \]
  because
  \[
  4J_n-n(n-1)=7k^2+33k+14>0.
  \]

## Verification

- CURRENT LOCAL VERIFIED FACT: two independent derivations and a third
  mathematical audit agree on the formula and every symbolic inequality.
- CURRENT LOCAL VERIFIED FACT: an independent implementation audit
  reconstructed the generated tuple for every \(2\le k\le5000\).
- CURRENT LOCAL VERIFIED FACT: two separate all-pairs scorers, one
  position-first and one label-first, both return \(J_n\) on selected cases
  from both parity branches.
- CURRENT LOCAL VERIFIED FACT: the six new test items, all 41 focused
  product-distance tests, 56 integrated tests, and the full 169-test suite
  pass. The full suite ran outside the filesystem sandbox because pytest
  requires its system temporary directory.
- CURRENT LOCAL VERIFIED FACT: source/test compilation and Ruff pass.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the \(n=3,\dots,6\) summary.
- CURRENT LOCAL VERIFIED FACT: strict text hygiene, complete diff inspection,
  and `git diff --check` pass for the intended ten-path delta.
- CURRENT HOSTED STATUS: GitHub Actions for the current worktree has not been
  independently verified.

## Residual Limitations

- This is an exact combinatorial surrogate result, not an exact value of the
  geometric optimum \(R_2^*(n)\).
- No new geometric claim, principal coefficient, or asymptotic coefficient is
  asserted.
- Structural classifications of minimizing cyclic orders remain open.
- The first index, if any, where positional distances at least three change
  the optimum remains open.
- Canonical cyclic-order enumeration remains bounded to \(n=3,\dots,11\).

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.
