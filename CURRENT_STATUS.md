# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** exact terminal-high compatible-low incidence obstruction.
- **Current task:** generalize the incidence obstruction to every exact
  threshold, combine it with the existing exact tail-cycle condition, and
  determine the resulting half-integer threshold and asymptotic coefficient.
- **Task dossier:**
  `ops/TASK-20260714__terminal_high_incidence/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Exact Incidence Result

Fix `n>=3` and an exact threshold `T>=0`. With

\[
a_T=\min\{k\ge2:k(k+1)>T\},
\qquad
b_T=\min\{k\ge2:k(k+1)>2T\},
\]

put

\[
U_T=\{a_T,\ldots,n\},
\quad
V_T=\{b_T,\ldots,n\},
\quad
u=|U_T|,
\quad
v=|V_T|.
\]

Define the compatible-low capacity

\[
C_n(T)
=
\#\{\ell\in\{2,\ldots,a_T-1\}:\ell b_T\le T\}
=
\max\!\left(0,\left\lfloor{T\over b_T}\right\rfloor-1\right).
\]

EXACT THEOREM: every cyclic order of `2,...,n` whose score at distance at most
two is at most `T` satisfies

\[
\boxed{2v\le C_n(T)}.
\]

For `n>=4`, each vertex of `V_T` has two distinct cyclic neighbors. A neighbor
in `U_T` would form a distinct pair with product at least
`a_T(a_T+1)>T`; hence both neighbors lie outside `U_T`. A low adjacent to two
distinct vertices of `V_T` would put those vertices at distance at most two,
with product at least `b_T(b_T+1)>2T`. Thus the `2v` incidence endpoints are
distinct compatible lows and inject into the set counted by `C_n(T)`.

The exceptional cycle `n=3` has score six. Feasibility therefore requires
`T>=6`, which implies `b_T>=4` and `v=0`. The theorem is then vacuous. The
same is true for every `v=0` case; when `v=1`, the single high still requires
two distinct compatible lows. Empty tails, singleton tails, floor endpoints,
and strict/non-strict equalities are included literally: tail starts use
strict `>`, while compatibility and the capacity use `<=`.

## Joint Half-Integer Obstruction

Keep the existing tail-cycle function and threshold unchanged:

\[
\Psi_n(T)=\max(2u,u+2v+\delta_n(T)),
\qquad
Q_n=\min\{q/2:\Psi_n(q/2)\le n-1\}.
\]

Define the distinct joint threshold

\[
\boxed{
H_n
=
\min\left\{
{q\over2}:q\in\mathbb Z_{\ge0},\
\Psi_n(q/2)\le n-1,\
2v(q/2)\le C_n(q/2)
\right\}.
}
\]

Then

\[
B_n\ge H_n\ge Q_n,
\qquad
B_n\ge\max(A_n,H_n).
\]

An exact finite event set for `H_n` is

\[
\widehat{\mathcal F}_n
=
\widehat{\mathcal E}_n
\cup
\left\{{k^2\over2}:4\le k\le n,\ k\ {\rm even}\right\},
\]

where the unchanged event set for `Q_n` is

\[
\widehat{\mathcal E}_n
=
\{0\}
\cup
\left\{
{k(k+1)\over2},\ k(k+1),\ {k^2-1\over2}:2\le k\le n
\right\}.
\]

The new events are exactly the internal capacity jumps for even `b_T=k`.
For odd `k` the floor is constant between consecutive `b_T` events; `k=2`
has `0<=T<3` and zero positive-part capacity.

## All-`n` Asymptotic Decision

Every `H_n`-admissible threshold satisfies

\[
T>{8\over25}n^2+{2\over5}n.
\]

Conversely, for every `n>=11`, setting

\[
d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T_n^*={d_n(d_n-1)\over2}
\]

satisfies both `2v<=C_n(T_n^*)` and `Psi_n(T_n^*)<=n-1`, and

\[
T_n^*
<
{8\over25}n^2+{42\over25}n+{52\over25}.
\]

Therefore

\[
\boxed{H_n={8\over25}n^2+O(n)},
\qquad
\lim_{n\to\infty}{H_n\over n^2}={8\over25},
\qquad
\liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}.
\]

The coefficient `8/25` is derived from matching lower and upper estimates; it
was not assumed. This proves the coefficient of the obstruction `H_n`, not a
limit or exact asymptotic coefficient for `B_n`.

## Finite Exact Regression

VERIFIED FACT (FINITE EXACT FORMULA EVALUATION):

\[
(H_3,\ldots,H_{11})=(6,12,15,20,21,30,36,45,50).
\]

Combined with the existing bounded exact table:

| `n` | `A_n` | `Q_n` | `H_n` | `max(A_n,H_n)` | `B_n` |
|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 6 | 6 | 6 | 6 |
| 4 | 12 | 12 | 12 | 12 | 12 |
| 5 | 15 | 12 | 15 | 15 | 15 |
| 6 | 20 | 20 | 20 | 20 | 20 |
| 7 | 24 | 21 | 21 | 24 | 24 |
| 8 | 30 | 30 | 30 | 30 | 30 |
| 9 | 35 | 63/2 | 36 | 36 | 36 |
| 10 | 42 | 42 | 45 | 45 | 45 |
| 11 | 48 | 45 | 50 | 50 | 50 |

The `A_n,Q_n,H_n` columns are exact formula evaluations. The `B_n` column is
the pre-existing finite exhaustive exact computation, still bounded to
`n=3..11`. No cyclic-order enumeration was extended beyond `n=11`.

## Verification And CI Provenance

- CURRENT LOCAL VERIFIED FACT: changed source and tests compile.
- CURRENT LOCAL VERIFIED FACT: focused product-distance tests pass `24/24`.
- CURRENT LOCAL VERIFIED FACT: the independent verifier exhausts all 872
  orders for `n=3..7` and checks 34,160 qualifying half-integer states,
  including every incidence endpoint and an explicit `n=11,T=50` witness.
- CURRENT LOCAL VERIFIED FACT: integrated
  product-distance/zigzag/tail/insertion tests pass `39/39`.
- CURRENT LOCAL VERIFIED FACT: exact formula diagnostics pass for
  `n=3..1000`, including 990 upper witnesses for `n=11..1000`; these checks
  do not enumerate cyclic orders.
- CURRENT LOCAL VERIFIED FACT: full pytest passes `152/152`.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: independent mathematical, implementation, and
  documentation reviews pass with no residual finding.
- CURRENT LOCAL VERIFIED FACT: the exact 10-path scope, strict UTF-8,
  trailing whitespace, 64 unique equation tags, 143 balanced display pairs,
  complete diff inspection, and final `git diff --check` all pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.

## Residual Limitations

- No exact formula, matching upper construction, or limit for `B_n` is
  proved.
- No equality `B_n=W_n` beyond the bounded `n=3..11` table is claimed.
- The result is a combinatorial distance-two obstruction only. It is not
  transferred to `L_n`, `R_2^*(n)`, or the geometric optimum.
- Finite exhaustive core-order computation remains bounded to `n=3..11`.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.
