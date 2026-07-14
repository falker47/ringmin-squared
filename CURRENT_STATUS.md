# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** exact residue-class values of the product-distance
  surrogate.
- **Current task:** construct and prove the exact threshold in the class
  \(n\equiv1\pmod5\), without canonical enumeration beyond \(n=11\).
- **Task dossier:**
  ops/TASK-20260714__residue_one_exact_construction/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Residue-One Construction

Write

\[
n=5k+1,\qquad k\ge2,\qquad
d=4k+3,\qquad D=d-1=4k+2,\qquad
h={D^2\over2}=H_n.
\]

EXACT THEOREM: `residue_one_product_distance_order(n)` generates an explicit
cyclic permutation \(\sigma_n^{(1)}\) of \(\{2,\dots,n\}\), without search,
such that

\[
W(\sigma_n^{(1)})=h.
\]

The proof in `research/PRODUCT_DISTANCE_SURROGATE.md` separately checks:

- every adjacent product;
- every pair at positional distance two;
- every pair at positional distance three;
- all pairs crossing the displayed cut;
- every distance at least four through
  \(n(n-1)<4h\).

The closing edge \((2k+1,D)\) has product exactly \(h\). The exact lower
obstruction therefore gives

\[
h=H_n\le B_n\le W_n\le W(\sigma_n^{(1)})=h,
\]

and hence

\[
\boxed{
B_n=W_n=H_n={(d-1)^2\over2}
}
\qquad(n\equiv1\pmod5,\ n\ge11).
\]

## Updated Residue Classification

For \(n\ge9\), with
\(d_n=\lceil(4n+8)/5\rceil\), exact surrogate values are now known in four
classes:

\[
B_n=W_n=H_n
=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5.
\end{cases}
\]

Only residue two remains unresolved beyond the bounded table. Its current
proved interval has width

\[
T_n-H_n=
\begin{cases}
(4n+7)/5,&n\equiv2\pmod5,\ n\ge17,\\
10,&n=12.
\end{cases}
\]

These are bound widths, not asserted optimality gaps.

## Exact Support And Verification

- CURRENT LOCAL VERIFIED FACT: source and tests compile; Ruff passes.
- CURRENT LOCAL VERIFIED FACT: focused product-distance tests pass `31/31`.
- CURRENT LOCAL VERIFIED FACT: integrated product-distance, zigzag,
  induced-subset, and insertion tests pass `46/46`.
- CURRENT LOCAL VERIFIED FACT: the full suite passes `159/159` outside the
  filesystem sandbox.
- RETAINED FAILED CHECK: the sandboxed full suite produced 31 temporary-path
  setup errors because the sandbox denied pytest access to its system
  temporary directory. The identical suite passed outside the sandbox; no
  changed product-distance test failed.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: the repository regression checks the exact
  residue-one formula for every `2<=k<=1000` and independent full all-pairs
  scores on selected values through `k=100`.
- CURRENT LOCAL VERIFIED FACT: separate exact oracles checked the formula
  through `k=5000`, reconstructed the implemented order through `k=2000`,
  and checked additional large values `k=9999,10000,10001`.
- CURRENT LOCAL VERIFIED FACT: independent mathematical and implementation
  audits pass after correcting the documented `k=2` boundary wording.
- CURRENT LOCAL VERIFIED FACT: the documentation audit's missing `n>=9`
  roadmap domain was corrected; all 10 changed paths pass strict UTF-8 and
  trailing-whitespace checks; the proof has 118 unique equation tags and 215
  balanced display pairs; complete diff inspection and `git diff --check`
  pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current worktree has not been
  independently verified.

## Residual Limitations

- Exact values of \(B_n\) and \(W_n\) beyond the bounded table remain open
  only in residue class two.
- Structural classifications of optimal orders remain open in every class.
- The first index, if any, where distances at least three change \(W_n\)
  remains open.
- Finite canonical core-order enumeration remains bounded to `n=3..11`.
- The geometric lower and upper coefficients remain different; this exact
  combinatorial result does not prove a geometric optimum.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.
