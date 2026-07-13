# Product-Distance Surrogate For Regular Directions

## Classification And Scope

- **DEFINITION:** the objective \(W(\sigma)\) below is a purely combinatorial
  surrogate for assigning the core indices \(2,\dots,n\) to equally spaced
  polar directions.
- **EXACT THEOREM (all \(n\ge3\)):** every core order \(\sigma\) gives a
  strictly all-pairs feasible core at \(R=(n-1)W(\sigma)/\pi\).
- **EXACT THEOREM (\(n\ge12\)):** the accepted radius-one insertion theorem
  transfers this construction to the full Power-Ringmin problem.
- **EXACT THEOREM (all admissible tails):**
  \(W(\sigma)\ge P_{m,n}/(n-1)\) for \(2\le m\le n-2\).
- **VERIFIED FACT (finite exhaustive exact computation):** the table below
  gives \(W_n\), canonical minimizer counts, and representatives for
  \(3\le n\le11\). It is not an all-\(n\) theorem, a geometric certificate,
  or a claim of exact geometric optimality.
- **CONJECTURE:** none is proposed from nine finite cases.

Fractions are oriented exactly as displayed below. The accepted angular
majorant, radius-one insertion theorem, duplicated-multiset pairing lemma, and
zigzag product lemma are proved in `research/ALL_N_LOWER_BOUND.md`; this note
applies them to the new surrogate without changing their hypotheses.

## Definition

Fix \(n\ge3\) and put \(N=n-1\). Let \(\sigma\) be a cyclic order of the core

\[
C_n=\{2,3,\dots,n\}.
\]

If \(p_\sigma(i)\in\{0,\dots,N-1\}\) is the position of \(i\), define the
smaller circular positional distance

\[
d_\sigma(i,j)
=
\min\bigl\{
|p_\sigma(i)-p_\sigma(j)|,
N-|p_\sigma(i)-p_\sigma(j)|
\bigr\}.
\]

Then

\[
W(\sigma)
=
\max_{2\le i<j\le n}{ij\over d_\sigma(i,j)},
\qquad
W_n=\min_\sigma W(\sigma).
\tag{1}
\]

Both extrema exist because the order space and the pair set are finite. The
objective is invariant under rotation and reflection of \(\sigma\).

For \(n=3\), the core has two elements. We use two antipodal directions,
\(d_\sigma(2,3)=1\), and the unique cyclic class has \(W_3=6\). This case is
kept separate from the ordinary regular-polygon terminology below.

## Exact Core Feasibility

For \(n\ge4\), assign the entry in position \(k\) of \(\sigma\) to polar
direction \(2\pi k/N\), a direction of a regular \(N\)-gon. For \(n=3\), use
the two antipodal directions just specified. Put

\[
R_\sigma={N W(\sigma)\over\pi}
\tag{2}
\]

and place the center of the circle of radius \(i^2\) at radial distance
\(R_\sigma+i^2\) on its assigned direction.

Take any distinct core indices \(i,j\), write \(d=d_\sigma(i,j)\), and let

\[
\delta={2\pi d\over N}\in(0,\pi]
\]

be their smaller angular separation. From (1),

\[
ij\le W(\sigma)d.
\tag{3}
\]

The accepted exact angular majorant, valid for every positive central radius,
is

\[
\theta_R(i^2,j^2)<{2ij\over R}.
\tag{4}
\]

Equations (2)--(4) give

\[
\theta_{R_\sigma}(i^2,j^2)
< {2ij\over R_\sigma}
\le {2W(\sigma)d\over NW(\sigma)/\pi}
= {2\pi d\over N}
=\delta.
\tag{5}
\]

Because \(\delta\le\pi\), the usual angle-distance equivalence is strictly
monotone here. Explicitly, if \(D_{ij}\) is the center distance, then

\[
D_{ij}^2-(i^2+j^2)^2
=
4(R_\sigma+i^2)(R_\sigma+j^2)
\left(
\sin^2{\delta\over2}
-{i^2j^2\over(R_\sigma+i^2)(R_\sigma+j^2)}
\right)>0.
\]

Thus \(D_{ij}>i^2+j^2\). Since the pair was arbitrary, all
\(\binom{N}{2}\) core pairs have strict clearance simultaneously. Every core
circle remains externally tangent to the central circle by construction.

This proves core feasibility at \(R_\sigma\). It is a sufficient radius, not a
proof that (2) is the least feasible radius for \(\sigma\), even within the
regular-direction class: the majorant (4) is one-sided.

For \(n\ge12\), the accepted insertion theorem gives equality of full and core
feasible-radius sets. Hence the same constructed radius is feasible for the
full problem and

\[
R_2^*(n)
\le {N W(\sigma)\over\pi},
\qquad
R_2^*(n)
\le {N W_n\over\pi}
\quad(n\ge12).
\tag{6}
\]

No attainment assumption for \(R_2^*(n)\) or the core infimum is used: (2) is
an explicitly feasible core radius, and insertion acts at that same radius.

## Tail Obstruction From Oriented Positional Gaps

Fix \(2\le m\le n-2\) and let

\[
T=\{m,m+1,\dots,n\},
\qquad |T|=n-m+1\ge3.
\]

Filter the oriented cycle \(\sigma\) to \(T\), obtaining the induced cyclic
order

\[
\tau_1,\tau_2,\dots,\tau_q,
\qquad \tau_{q+1}=\tau_1.
\]

Let \(g_\ell\) be the positive number of forward positional steps in the full
\(N\)-cycle from \(\tau_\ell\) to \(\tau_{\ell+1}\). Because these are the gaps
between consecutive elements of the induced oriented order, they partition
the positional cycle exactly once:

\[
g_\ell\in\{1,\dots,N-1\},
\qquad
\sum_{\ell=1}^q g_\ell=N.
\tag{7}
\]

The smaller circular distance uses either this forward gap or its complement,
so, explicitly,

\[
d_\sigma(\tau_\ell,\tau_{\ell+1})
=\min\{g_\ell,N-g_\ell\}
\le g_\ell.
\tag{8}
\]

By the definition of \(W(\sigma)\), equations (7)--(8) imply

\[
\tau_\ell\tau_{\ell+1}
\le
W(\sigma)d_\sigma(\tau_\ell,\tau_{\ell+1})
\le W(\sigma)g_\ell,
\]

and therefore

\[
\sum_{\ell=1}^q\tau_\ell\tau_{\ell+1}
\le N W(\sigma).
\tag{9}
\]

The duplicated-multiset pairing lemma gives the opposite bound for every
cyclic order of this tail:

\[
\sum_{\ell=1}^q\tau_\ell\tau_{\ell+1}
\ge P_{m,n},
\]

where

\[
P_{m,n}
=
\sum_{k=m}^n k(m+n-k)
=
{(n-m+1)(m^2+4mn+m+n^2-n)\over6}.
\tag{10}
\]

Combining (9)--(10) proves the exact obstruction

\[
\boxed{
W(\sigma)\ge {P_{m,n}\over N}
}
\qquad(2\le m\le n-2).
\tag{11}
\]

Consequently, with

\[
L_n=\max_{2\le m\le n-2}{P_{m,n}\over N},
\]

one has \(W_n\ge L_n\). The range is empty for \(n=3\).

## Zigzag Benchmark

For the core zigzag

\[
z_n=(n,2,n-1,3,\dots),
\qquad
M_n=n\left(\left\lfloor{n\over2}\right\rfloor+1\right),
\]

the accepted product-distance lemma says that a pair at positional distance
\(d\) satisfies \(ij\le dM_n\). Thus \(W(z_n)\le M_n\). The closing pair has
distance one and product exactly \(M_n\), so in fact

\[
\boxed{W(z_n)=M_n}.
\tag{12}
\]

Equation (2) therefore recovers the earlier zigzag radius
\(V_n=NM_n/\pi\). The new optimization can improve that sufficient radius
when \(W_n<M_n\).

## Exact Bounded Enumeration For \(3\le n\le11\)

The implementation is `src/power_ringmin/product_distance.py`.

- Every pair score is represented by `fractions.Fraction`; enumeration uses
  integer cross-products and no floating point.
- Every unordered pair is scored, including the closing pair, non-adjacent
  pairs, and the unique antipodal distance when \(N\) is even.
- For \(n=3\), the sole canonical order is `(3, 2)`.
- For \(n\ge4\), rotation is removed by fixing \(n\) first and reflection is
  removed by retaining the orientation whose second entry is smaller than its
  last. The canonical count is
  \[
  {(N-1)!\over2}={(n-2)!\over2}.
  \]
- The enumerator rejects \(n>11\) and checks an explicit positive
  `max_canonical_orders` ceiling before generating permutations. The maximum
  admitted row has \(181{,}440\) canonical orders.
- A strict integer cutoff discards an order only when a pair already exceeds
  the incumbent. Equality is retained, so minimizer counts are exact.

The representative below is the lexicographically least canonical minimizer.
The minimizer count is a count of rotation/reflection classes.

| \(n\) | canonical orders | \(W_n\) | minimizers | representative | \(W(z_n)\) | \(L_n\) (maximizing \(m\)) | \(W_n-L_n\) | \(W(z_n)-W_n\) |
|---:|---:|---:|---:|---|---:|---:|---:|---:|
| 3 | 1 | \(6\) | 1 | `(3, 2)` | \(6\) | -- | -- | \(0\) |
| 4 | 1 | \(12\) | 1 | `(4, 2, 3)` | \(12\) | \(25/3\) (`m=2`) | \(11/3\) | \(0\) |
| 5 | 3 | \(15\) | 1 | `(5, 2, 4, 3)` | \(15\) | \(23/2\) (`m=3`) | \(7/2\) | \(0\) |
| 6 | 12 | \(20\) | 2 | `(6, 2, 4, 5, 3)` | \(24\) | \(76/5\) (`m=3`) | \(24/5\) | \(4\) |
| 7 | 60 | \(24\) | 2 | `(7, 2, 5, 4, 6, 3)` | \(28\) | \(58/3\) (`m=4`) | \(14/3\) | \(4\) |
| 8 | 360 | \(30\) | 4 | `(8, 2, 5, 6, 4, 7, 3)` | \(40\) | \(170/7\) (`m=4`) | \(40/7\) | \(10\) |
| 9 | 2,520 | \(36\) | 12 | `(9, 2, 6, 5, 7, 3, 8, 4)` | \(45\) | \(59/2\) (`m=4`) | \(13/2\) | \(9\) |
| 10 | 20,160 | \(45\) | 72 | `(10, 2, 6, 7, 3, 8, 5, 9, 4)` | \(60\) | \(320/9\) (`m=5`) | \(85/9\) | \(15\) |
| 11 | 181,440 | \(50\) | 24 | `(11, 2, 7, 6, 8, 3, 10, 5, 9, 4)` | \(66\) | \(42\) (`m=5`) | \(8\) | \(16\) |

The bounded run covers \(204{,}557\) canonical classes in total. It shows
that zigzag is surrogate-optimal for \(n=3,4,5\) and strictly suboptimal for
every enumerated \(n=6,\dots,11\). The tail obstruction is strict for every
enumerated case where it is defined. These are finite exact facts only.

## Verification Boundary And Open Questions

`tests/test_product_distance.py` checks exact rational comparisons, canonical
counts, every pair rather than only adjacent pairs, an independent full
permutation calculation for the smallest cases, deterministic work bounds,
zigzag and tail comparisons, and exact reproduction of the table.

The following remain unresolved.

- **OPEN QUESTION:** what is the asymptotic behavior of \(W_n/n^2\), and does
  a limit exist?
- **OPEN QUESTION:** can a symbolic order family improve the zigzag
  coefficient while approaching the tail obstruction?
- **OPEN QUESTION:** can stronger combinatorial obstructions narrow the finite
  and asymptotic gap between \(L_n\) and \(W_n\)?

No formula suggested by the nine values of \(W_n\) is promoted to a
conjecture. No geometric certificate, schema, serialized result artifact, or
CLI is created by this work.
