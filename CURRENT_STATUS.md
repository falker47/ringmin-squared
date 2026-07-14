# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** global exact classification of the product-distance
  surrogates.
- **Current task:** consolidate the exact bounded table and residue-class
  theorem into the all-\(n\) distance-two saturation result.
- **Task dossier:**
  ops/TASK-20260714__global_surrogate_classification/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Global Exact Consequence

By definition,

\[
B_n=W_n^{(\le2)}\le W_n.
\]

VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the bounded table gives

\[
(B_3,\dots,B_{11})
=
(W_3,\dots,W_{11})
=
(6,12,15,20,24,30,36,45,50).
\]

EXACT THEOREM: the residue-class constructions give

\[
B_n=W_n=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
d_n(d_n-2)/2,&n\equiv2\pmod5
\end{cases}
\qquad(n\ge9),
\]

where \(d_n=\lceil(4n+8)/5\rceil\). On the overlap \(n=9,10,11\), this
formula returns \(36,45,50\), matching the exact table.

EXACT THEOREM (FINITE-EXHAUSTIVE PLUS SYMBOLIC): because
\([3,11]\cup[9,\infty)=[3,\infty)\),

\[
\boxed{W_n^{(\le2)}=B_n=W_n\qquad(n\ge3)}.
\]

Consequently, for every integer \(q\ge2\),

\[
B_n\le W_n^{(\le q)}\le W_n=B_n,
\]

so positional distances at least three never change the optimum value.

## Minimizer-Set Boundary

Let \(\mathcal M_n\) and \(\mathcal M_n^{(\le2)}\) be the full and
distance-two minimizer sets. For any \(\sigma\in\mathcal M_n\),

\[
B_n
\le W^{(\le2)}(\sigma)
\le W(\sigma)
=W_n
=B_n.
\]

Therefore

\[
\mathcal M_n\subseteq\mathcal M_n^{(\le2)}
\qquad(n\ge3).
\]

The exact bounded enumeration proves equality of the canonical minimizer sets
for \(3\le n\le11\). The correctly bounded open question is whether this
inclusion is strict for some \(n\ge12\), equivalently whether distances at
least three remove some distance-two minimizers without changing the optimum.

## Ruff Provenance Correction

The unused `t = n // 2` assignment in the terminal-high boundary test helper
was removed. The identically named assignment in production source and the
other assignment in the adjacent-equality test remain because both are used.

- CURRENT LOCAL VERIFIED FACT: `python -m ruff --version` returned exactly
  `ruff 0.11.12`.
- CURRENT LOCAL VERIFIED FACT: default Ruff rules, no ignores, explicit
  two-file provenance scope:
  `python -m ruff check src\power_ringmin\product_distance.py
  tests\test_product_distance.py` returned exactly
  `All checks passed!` with exit code `0`.
- LIMITATION: this is not a repository-wide Ruff claim.

## Verification

- CURRENT LOCAL VERIFIED FACT: three independent read-only audits pass the
  domain cover, residue squeezes, overlap values, all-\(q\ge2\) corollary,
  minimizer inclusion, cross-document consistency, and Ruff provenance.
- CURRENT LOCAL VERIFIED FACT:
  `python -m pytest tests\test_product_distance.py` reports
  `41 passed in 20.47s`.
- CURRENT LOCAL VERIFIED FACT:
  `python -m pytest --basetemp
  C:\tmp\power-ringmin-pytest-global-surrogate-20260714-a` reports
  `169 passed in 47.24s`.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the \(n=3,\dots,6\) summary.
- CURRENT LOCAL VERIFIED FACT: no generator, residue formula, enumeration,
  artifact, schema, CLI, certificate, or STN documentation was added or
  changed.
- CURRENT LOCAL VERIFIED FACT: final text, proof-tag, complete-diff, and Git
  hygiene checks pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current worktree has not been
  independently verified.

## Residual Limitations

- This is an exact combinatorial surrogate theorem, not an exact value of the
  geometric optimum \(R_2^*(n)\).
- Equality of optimum values does not prove equality of minimizer sets for
  \(n\ge12\), nor that every constraint at distance at least three is slack or
  inactive.
- Canonical cyclic-order enumeration remains bounded to \(n=3,\dots,11\).

## Proposed Next Task

In a fresh chat, document the fixed-order angular/STN equivalence and endpoint
semantics, as already prioritized in `research/NEXT_RESEARCH_STEPS.md`. This
task did not begin or add that documentation.
