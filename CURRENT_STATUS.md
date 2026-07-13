# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** quantitative all-`n` lower obstruction for the
  distance-two product-distance relaxation.
- **Current task:** prove and invert the two-threshold cyclic packing lemma for
  `B_n=W_n^(<=2)`.
- **Task dossier:**
  `ops/TASK-20260713__two_threshold_distance_two_obstruction/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Exact Result

Fix `n>=3` and an exact threshold `T>=0`. Let `a_T` and `b_T` be the least
integers at least two satisfying

\[
a_T(a_T+1)>T,
\qquad
b_T(b_T+1)>2T,
\]

and set

\[
u=\max(0,n-a_T+1),
\qquad
v=\max(0,n-b_T+1).
\]

EXACT THEOREM: if a cyclic core order has distance-at-most-two score at most
`T` and `u>=2`, then induced `U_T` gaps and the exact cyclic marked-word count
give

\[
\boxed{n-1\ge2u+\max(0,2v-u)}.
\]

Every induced `U_T` gap costs at least two positions. A `V_T-V_T` gap costs
at least three, and a cyclic word with `u` positions and `v` marked has
minimum exactly `max(0,2v-u)` marked-marked adjacencies. The two oriented gaps
when `u=2` are counted separately. Degenerate tails are explicit: `u=0`
forces `v=0`, while `u=1` forces `v=0` for every `n>=3`, so the same necessary
numerical inequality remains valid.

Define the exact finite obstruction

\[
Q_n=
\min\left\{
{q\over2}:q\in\mathbb Z_{\ge0},\quad
2u_{q/2}+\max(0,2v_{q/2}-u_{q/2})\le n-1
\right\}.
\]

It is enough to inspect the finite event set

\[
\{0\}\cup
\{k(k+1)/2,k(k+1):2\le k\le n-1\}.
\]

Because every distance-two objective is a half-integer,

\[
B_n\ge Q_n,
\qquad
B_n\ge\max(A_n,Q_n).
\]

For every `n>=9`, the explicit all-`n` consequence is

\[
\boxed{
B_n\ge Q_n\ge
{36-16\sqrt2\over49}\left(n+{1\over2}\right)^2
}.
\]

Therefore

\[
\boxed{
\liminf_{n\to\infty}{B_n\over n^2}
\ge {36-16\sqrt2\over49}>{1\over4}
}.
\]

This is stronger than `B_n>=c*n^2-O(n)`: it gives
`B_n>=c*n^2+c*n+c/4` for the displayed `c` and `n>=9`.

## Comparison With Existing Obstructions

The rigorous domains are

\[
A_n\le B_n\le W_n,
\qquad
Q_n\le B_n,
\qquad
L_n\le W_n.
\]

The full-distance tail argument for `L_n` uses induced gaps of arbitrary
length and does not prove `L_n<=B_n`. The constants satisfy

\[
{1\over4}
<
{36-16\sqrt2\over49}
<
{2(\sqrt2-1)\over3}.
\]

Thus the two-threshold obstruction strictly improves the adjacent coefficient
for `B_n`, while the slightly larger tail coefficient remains a statement
about `W_n`.

## Finite Exact Regression

VERIFIED FACT (FINITE EXACT FORMULA EVALUATION):

\[
(Q_3,\dots,Q_{11})=(6,12,12,20,21,30,30,42,45).
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
| 9 | 35 | 30 | 35 | 36 | 59/2 | 36 |
| 10 | 42 | 42 | 42 | 45 | 320/9 | 45 |
| 11 | 48 | 45 | 48 | 50 | 42 | 50 |

The `A_n,Q_n,L_n` columns are exact formula evaluations. The `B_n,W_n`
columns are the existing finite exhaustive exact computation, still bounded
to `n=3..11`. No cyclic-order enumeration was extended beyond `n=11`.

## Verification And CI Provenance

- CURRENT LOCAL VERIFIED FACT: changed source and tests compile.
- CURRENT LOCAL VERIFIED FACT: focused product-distance tests pass `18/18`.
- CURRENT LOCAL VERIFIED FACT: integrated
  product-distance/zigzag/tail/insertion tests pass `33/33`.
- CURRENT LOCAL VERIFIED FACT: exact formula diagnostics pass for all 992
  values `n=9..1000`; this is parameter evaluation, not order enumeration or
  a substitute for the symbolic proof.
- CURRENT LOCAL VERIFIED FACT: full pytest passes `146/146`.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: exact ten-path scope, strict UTF-8, corrected
  trailing-whitespace scan, 51 unique equation tags, complete diff review, and
  `git diff --check` pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.

## Residual Limitations

- No exact formula or matching upper construction for `B_n` is proved.
- No equality `B_n=W_n` beyond the bounded `n=3..11` table is claimed.
- The coefficient `(36-16*sqrt(2))/49` is a proved lower coefficient, not an
  exact asymptotic constant or a claim that a limit exists.
- The full-distance tail coefficient is not silently transferred to `B_n`.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.
