# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** exact characterization of the distance-two threshold-tail
  incompatibility.
- **Current task:** characterize `eta_n(T)`, invert the resulting packing
  condition, and decide whether its asymptotic coefficient improves.
- **Task dossier:**
  `ops/TASK-20260713__exact_tail_incompatibility/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Exact Result

Fix `n>=3` and an exact threshold `T>=0`. Let `a=a_T` and `b=b_T` be the
least integers at least two satisfying

\[
a(a+1)>T,
\qquad
b(b+1)>2T,
\]

and put

\[
u=\max(0,n-a+1),
\qquad
v=\max(0,n-b+1).
\]

On `U_T={a,...,n}`, join distinct labels when `xy<=2T` and define

\[
\delta_n(T)
=
\mathbf1_{\{a<b\le n-1,\ 2T<b^2-1\}}.
\]

EXACT THEOREM: the compatible graph is a split threshold graph whose cross
neighborhoods are nested prefixes, and

\[
\boxed{
\eta_n(T)=\max(0,2v-u+\delta_n(T))
}.
\]

For `u=0,1`, `eta_n(T)=0`. For `u=2`, the two oriented arcs are counted
separately, so an incompatible pair contributes two and a compatible pair
contributes zero. The equality `2T=b^2-1` is compatible and turns the
correction off.

The earlier clique term is exact up to one:

\[
0\le
\eta_n(T)-\max(0,2v-u)
\le1.
\]

The improvement is real: `n=5,T=6` gives `eta=2` and clique bound one. It is
also uniformly bounded and vanishes on infinite families, including
`2T=b^2-1`.

## Exact Gap Inversion

If a cyclic core order has distance-at-most-two score at most `T`, the induced
tail gaps give

\[
\boxed{n-1\ge2u+\eta_n(T)}.
\]

Define

\[
\Psi_n(T)
=2u+\eta_n(T)
=\max(2u,u+2v+\delta_n(T))
\]

and

\[
Q_n
=
\min\left\{
{q\over2}:q\in\mathbb Z_{\ge0},\quad
\Psi_n(q/2)\le n-1
\right\}.
\]

The exact finite event set is

\[
\{0\}\cup
\left\{
{k(k+1)\over2},\ k(k+1),\ {k^2-1\over2}:2\le k\le n
\right\}.
\]

The range now includes `k=n`, so exhaustivity is literal. In the earlier
clique-only event set, the omitted `b` event at `T=n(n+1)/2` either coincided
with an already included `a` event or left the clique function unchanged. The
omitted `a` event occurred only after the condition was already admissible.
Thus the earlier values were not wrong; the new statement removes the
expositional gap.

Because every distance-two objective is a half-integer,

\[
B_n\ge Q_n,
\qquad
B_n\ge\max(A_n,Q_n).
\]

## Asymptotic Decision

For every `n>=9`,

\[
B_n\ge Q_n\ge
{36-16\sqrt2\over49}\left(n+{1\over2}\right)^2.
\]

The exact inversion has a matching upper estimate:

\[
\boxed{
Q_n={36-16\sqrt2\over49}n^2+O(n)
}.
\]

Therefore

\[
\lim_{n\to\infty}{Q_n\over n^2}
={36-16\sqrt2\over49},
\qquad
\liminf_{n\to\infty}{B_n\over n^2}
\ge {36-16\sqrt2\over49}>{1\over4}.
\]

INTERPRETATION: the exact nested-neighborhood refinement improves some finite
thresholds but does not improve the asymptotic coefficient obtainable from
this tail-cycle subproblem. This does not prove that `B_n/n^2` converges or
that its actual coefficient equals the displayed constant.

## Finite Exact Regression

VERIFIED FACT (FINITE EXACT FORMULA EVALUATION):

\[
(Q_3,\dots,Q_{11})=(6,12,12,20,21,30,63/2,42,45).
\]

Combined with the existing bounded exact table:

| `n` | `A_n` | `Q_n` | `max(A_n,Q_n)` | `B_n` | `L_n` | `W_n` |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 6 | 6 | 6 | -- | 6 |
| 4 | 12 | 12 | 12 | 12 | 25/3 | 12 |
| 5 | 15 | 12 | 15 | 15 | 23/2 | 15 |
| 6 | 20 | 20 | 20 | 20 | 76/5 | 20 |
| 7 | 24 | 21 | 24 | 24 | 58/3 | 24 |
| 8 | 30 | 30 | 30 | 30 | 170/7 | 30 |
| 9 | 35 | 63/2 | 35 | 36 | 59/2 | 36 |
| 10 | 42 | 42 | 42 | 45 | 320/9 | 45 |
| 11 | 48 | 45 | 48 | 50 | 42 | 50 |

The `A_n,Q_n,L_n` columns are exact formula evaluations. The `B_n,W_n`
columns are the existing finite exhaustive exact computation, still bounded
to `n=3..11`. No cyclic-order enumeration was extended beyond `n=11`.

## Verification And CI Provenance

- CURRENT LOCAL VERIFIED FACT: changed source and tests compile.
- CURRENT LOCAL VERIFIED FACT: focused product-distance tests pass `20/20`.
- CURRENT LOCAL VERIFIED FACT: integrated
  product-distance/zigzag/tail/insertion tests pass `35/35`.
- CURRENT LOCAL VERIFIED FACT: the independent verifier matches 299 graph
  states with tail cardinality at most seven; it does not enumerate core
  orders.
- CURRENT LOCAL VERIFIED FACT: exact obstruction minimality passes for all 992
  values `n=9..1000`; 956 explicit asymptotic witnesses pass for
  `n=45..1000`. These are formula diagnostics, not order enumeration.
- CURRENT LOCAL VERIFIED FACT: full pytest passes `148/148`.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: independent mathematical, implementation, and
  documentation reviews pass with no remaining blocker; the exact 10-path
  scope, UTF-8, whitespace, 51 equation tags, and final diff checks pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.

## Residual Limitations

- No exact formula or matching upper construction for `B_n` is proved.
- No equality `B_n=W_n` beyond the bounded `n=3..11` table is claimed.
- The exact result settles only the single-tail cyclic incompatibility
  subproblem; a stronger coefficient would require a genuinely different or
  combined obstruction.
- The coefficient `(36-16*sqrt(2))/49` remains a proved lower coefficient for
  `B_n`, not an exact asymptotic constant or a claim that a limit exists.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.
