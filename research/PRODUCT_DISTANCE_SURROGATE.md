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
- **EXACT THEOREM (adjacent relaxation):** if
  \(A_n=\min_\sigma\max_k\sigma_k\sigma_{k+1}\), then \(A_3=6\) and
  \[
  A_n=
  \left(\left\lfloor{n\over2}\right\rfloor+1\right)
  \left(\left\lceil{n\over2}\right\rceil+2\right)
  \qquad(n\ge4).
  \]
  The generic `patterns.interleave` order realizes this bound for every
  \(n\).
- **VERIFIED FACT (finite exhaustive exact computation):** the table below
  gives the objectives truncated at positional distances at most one and two,
  as well as \(W_n\), for \(3\le n\le11\). Non-adjacent constraints first
  change the optimum at \(n=9\), while distance-two constraints already
  recover \(W_n\) throughout this bounded range. This is not an all-\(n\)
  theorem, a geometric certificate, or a claim of exact geometric optimality.
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

For an integer \(q\ge1\), define the truncated objectives

\[
W^{(\le q)}(\sigma)
=
\max_{\substack{2\le i<j\le n\\d_\sigma(i,j)\le q}}
{ij\over d_\sigma(i,j)},
\qquad
W_n^{(\le q)}=\min_\sigma W^{(\le q)}(\sigma).
\tag{2}
\]

In particular,

\[
A(\sigma)=\max_k\sigma_k\sigma_{k+1}
=W^{(\le1)}(\sigma),
\qquad
A_n=W_n^{(\le1)}.
\tag{3}
\]

Both extrema exist because the order space and the pair set are finite. The
objective is invariant under rotation and reflection of \(\sigma\).

For \(n=3\), the core has two elements. We use two antipodal directions,
\(d_\sigma(2,3)=1\), and the unique cyclic class has
\(A_3=W_3^{(\le2)}=W_3=6\). This case is kept separate from the ordinary
regular-polygon terminology below.

## Exact Adjacent Relaxation

We prove the claimed formula for \(A_n\) before using computation.

### Lower bound by internal-edge counting

Partition the vertices of any simple cycle into a high block \(H\) and a low
block \(L\). Write \(e_H\) for the number of cycle edges with both endpoints
in \(H\), and \(e_{HL}\) for the number of crossing edges. Degree counting on
\(H\) gives

\[
2|H|=2e_H+e_{HL}.
\]

Every vertex of \(L\) is incident to at most two crossing edges, so
\(e_{HL}\le2|L|\), and hence

\[
e_H\ge |H|-|L|.
\tag{4}
\]

Let first \(n=2t\ge4\), and choose

\[
H=\{t+1,\dots,2t\},
\qquad
L=\{2,\dots,t\}.
\]

Here \(|H|-|L|=1\), so (4) forces a high-high edge. Its distinct
endpoints have product at least \((t+1)(t+2)\). Therefore

\[
A_{2t}\ge(t+1)(t+2).
\tag{5}
\]

Now let \(n=2t+1\ge5\), and choose

\[
H=\{t+1,\dots,2t+1\},
\qquad
L=\{2,\dots,t\}.
\]

This time (4) forces at least two high-high edges. Among unordered pairs of
distinct elements of \(H\), the only edge with product strictly below
\((t+1)(t+3)\) is \(\{t+1,t+2\}\). A simple cycle cannot use that same edge
twice, so at least one of the two forced high-high edges has product at least
\((t+1)(t+3)\). Thus

\[
A_{2t+1}\ge(t+1)(t+3).
\tag{6}
\]

The exceptional two-vertex core gives \(A_3=2\cdot3=6\).

### Explicit all-\(n\) construction

For \(n\ge4\), put \(C_n=\{2,\dots,n\}\) and consider the two partial
involutions

\[
f(x)=n+1-x,
\qquad
g(x)=n+3-x.
\]

Join distinct vertices whenever their sum is \(n+1\) or \(n+3\). If \(n\)
is even, these edges form one Hamilton path with endpoints \(2,n\); close it
with \(\{2,n\}\). If \(n=2t+1\) is odd, they form two parity paths whose four
endpoints are \(2,n,t+1,t+2\); join the paths at both ends with
\(\{2,n\}\) and \(\{t+1,t+2\}\).

For completeness, the path assertion is not an appeal to a picture. Every
non-endpoint has degree two and the displayed endpoints have degree one.
Along alternating \(f\)- and \(g\)-edges,

\[
(g\mathbin\circ f)(x)=x+2,
\]

whenever both steps are defined. Hence there is no additional cycle
component. For even \(n\), only \(2,n\) have degree one, so there is one path
through all vertices. For odd \(n\), both edge sums are even and preserve
parity, giving exactly the two stated paths; the two added cross-parity edges
make one Hamilton cycle.

Every edge of the resulting cycle has endpoint sum \(n+1\), \(n+2\), or
\(n+3\). Among distinct positive integers with sum at most \(n+3\), the
largest possible product is

\[
\begin{cases}
(t+1)(t+2),&n=2t,\\
(t+1)(t+3),&n=2t+1.
\end{cases}
\tag{7}
\]

Indeed, for odd sum \(2t+3\) the closest two integers are \(t+1,t+2\); for
even sum \(2t+4\), equality of the endpoints is forbidden and the closest
distinct integers are \(t+1,t+3\). This proves the matching upper bounds.

Unfolding the one-based indices in `patterns.interleave` shows that its
unordered cycle-edge set is exactly the construction above: the sum-\(n+1\)
and sum-\(n+3\) edges, the closing edge \(\{2,n\}\), and, for odd \(n\), the
middle edge \(\{t+1,t+2\}\). Therefore that existing constructor realizes the
optimum for every \(n\), and (5)--(7) prove

\[
\boxed{
A_3=6,
\qquad
A_n=
\left(\left\lfloor{n\over2}\right\rfloor+1\right)
\left(\left\lceil{n\over2}\right\rceil+2\right)
\quad(n\ge4).
}
\tag{8}
\]

## Exact Core Feasibility

For \(n\ge4\), assign the entry in position \(k\) of \(\sigma\) to polar
direction \(2\pi k/N\), a direction of a regular \(N\)-gon. For \(n=3\), use
the two antipodal directions just specified. Put

\[
R_\sigma={N W(\sigma)\over\pi}
\tag{9}
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
\tag{10}
\]

The accepted exact angular majorant, valid for every positive central radius,
is

\[
\theta_R(i^2,j^2)<{2ij\over R}.
\tag{11}
\]

Equations (9)--(11) give

\[
\theta_{R_\sigma}(i^2,j^2)
< {2ij\over R_\sigma}
\le {2W(\sigma)d\over NW(\sigma)/\pi}
= {2\pi d\over N}
=\delta.
\tag{12}
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
proof that (9) is the least feasible radius for \(\sigma\), even within the
regular-direction class: the majorant (11) is one-sided.

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
\tag{13}
\]

No attainment assumption for \(R_2^*(n)\) or the core infimum is used: (9) is
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
\tag{14}
\]

The smaller circular distance uses either this forward gap or its complement,
so, explicitly,

\[
d_\sigma(\tau_\ell,\tau_{\ell+1})
=\min\{g_\ell,N-g_\ell\}
\le g_\ell.
\tag{15}
\]

By the definition of \(W(\sigma)\), equations (14)--(15) imply

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
\tag{16}
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
\tag{17}
\]

Combining (16)--(17) proves the exact obstruction

\[
\boxed{
W(\sigma)\ge {P_{m,n}\over N}
}
\qquad(2\le m\le n-2).
\tag{18}
\]

Consequently, with

\[
L_n=\max_{2\le m\le n-2}{P_{m,n}\over N},
\]

one has \(W_n\ge L_n\). The range is empty for \(n=3\).

## Comparison Of \(A_n\) And The Tail Obstruction

The adjacent formula has the parity expansions

\[
A_n=
\begin{cases}
n^2/4+3n/2+2,&n\ \text{even},\\
n^2/4+3n/2+5/4,&n\ \text{odd},
\end{cases}
\]

and therefore

\[
\lim_{n\to\infty}{A_n\over n^2}={1\over4}.
\]

The accepted exact characterization of the maximizing tail start gives
\(m/n\to\alpha=\sqrt2-1\). Dividing the closed form for \(P_{m,n}\) by
\((n-1)n^2\) yields

\[
\lim_{n\to\infty}{L_n\over n^2}
=
{(1-\alpha)(\alpha^2+4\alpha+1)\over6}
=
{2(\sqrt2-1)\over3}.
\]

Since \(\sqrt2>11/8\),

\[
\boxed{
{1\over4}
<
{2(\sqrt2-1)\over3}.
}
\]

This comparison can be made effective without enumerating any cyclic orders.
For every \(n\ge33\), take the admissible tail start
\(m=\lceil2n/5\rceil\), and set

\[
D(n)=P_{m,n}-(n-1)A_n.
\]

Write \(n=10q+r\), \(0\le r\le9\). In the first three residue classes put
\(q_0=4\), and in the remaining classes put \(q_0=3\); these are exactly the
least possible \(q\) values once \(n\ge33\). With \(x=q-q_0\ge0\), direct
substitution gives:

| \(r\) | \(m-4q\) | \(q_0\) | \(D(10q+r)\) as a polynomial in \(x=q-q_0\) |
|---:|---:|---:|---|
| 0 | 0 | 4 | \(26x^3+227x^2+562x+282\) |
| 1 | 1 | 4 | \(26x^3+236x^2+629x+405\) |
| 2 | 1 | 4 | \(26x^3+243x^2+661x+418\) |
| 3 | 2 | 3 | \(26x^3+174x^2+304x+44\) |
| 4 | 2 | 3 | \(26x^3+181x^2+326x+40\) |
| 5 | 2 | 3 | \(26x^3+188x^2+362x+80\) |
| 6 | 3 | 3 | \(26x^3+197x^2+405x+120\) |
| 7 | 3 | 3 | \(26x^3+204x^2+445x+172\) |
| 8 | 4 | 3 | \(26x^3+213x^2+490x+215\) |
| 9 | 4 | 3 | \(26x^3+220x^2+534x+280\) |

Every coefficient is positive. Thus \(D(n)>0\), so

\[
L_n\ge {P_{\lceil2n/5\rceil,n}\over n-1}>A_n
\qquad(n\ge33).
\]

This is an exact all-\(n\) theorem from \(33\) onward. Separately, exact
rational evaluation of the already proved tail formula and its exact
maximizer gives \(L_n\le A_n\) for every \(4\le n\le32\). Hence \(33\) is the
first \(n\) at which this particular tail obstruction alone proves that the
adjacent relaxation is strict. Because \(W_n\ge L_n\), non-adjacent
constraints are necessarily essential to the full surrogate for every
\(n\ge33\). This does not decide the full values \(W_n\) for \(12\le n\le32\).

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
\tag{19}
\]

Equation (9) therefore recovers the earlier zigzag radius
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

The exact truncated objectives are:

| \(n\) | \(W_n^{(\le1)}=A_n\) | \(W_n^{(\le2)}\) | \(W_n\) | \(W_n-A_n\) | \(W_n-W_n^{(\le2)}\) | minimizers \((\le1,\le2)\) |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | \(6\) | \(6\) | \(6\) | \(0\) | \(0\) | \(1,1\) |
| 4 | \(12\) | \(12\) | \(12\) | \(0\) | \(0\) | \(1,1\) |
| 5 | \(15\) | \(15\) | \(15\) | \(0\) | \(0\) | \(1,1\) |
| 6 | \(20\) | \(20\) | \(20\) | \(0\) | \(0\) | \(2,2\) |
| 7 | \(24\) | \(24\) | \(24\) | \(0\) | \(0\) | \(2,2\) |
| 8 | \(30\) | \(30\) | \(30\) | \(0\) | \(0\) | \(4,4\) |
| 9 | \(35\) | \(36\) | \(36\) | \(1\) | \(0\) | \(4,12\) |
| 10 | \(42\) | \(45\) | \(45\) | \(3\) | \(0\) | \(24,72\) |
| 11 | \(48\) | \(50\) | \(50\) | \(2\) | \(0\) | \(24,24\) |

Thus the first exact gap between the adjacent relaxation and the full
surrogate occurs at \(n=9\):

\[
W_9^{(\le1)}=A_9=35<36=W_9^{(\le2)}=W_9.
\]

In fact \(W_n^{(\le2)}=W_n\) for every enumerated \(3\le n\le11\).
The distance-two and full minimizer counts and lexicographically least
representatives also agree in every row. Since every full minimizer is then a
distance-two minimizer and the finite counts agree, their canonical minimizer
sets coincide. Therefore non-adjacent pairs are first essential at distance
two for \(n=9\), while distances three and larger do not change either the
optimum or the minimizer set anywhere in this bounded range.

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
the all-\(n\) adjacent formula against the explicit interleave construction,
the effective tail comparison, zigzag and tail values, and exact reproduction
of both the truncated and full tables.

The following remain unresolved.

- **OPEN QUESTION:** what is the asymptotic behavior of \(W_n/n^2\), and does
  a limit exist?
- **OPEN QUESTION:** can a symbolic order family improve the zigzag
  coefficient while approaching the tail obstruction?
- **OPEN QUESTION:** can stronger combinatorial obstructions narrow the finite
  and asymptotic gap between \(L_n\) and \(W_n\)?
- **OPEN QUESTION:** are non-adjacent constraints strict for every
  \(12\le n\le32\)? The bounded enumeration stops at \(11\), while the tail
  theorem proves strictness for every \(n\ge33\).
- **OPEN QUESTION:** at what \(n\), if any, do positional distances at least
  three first change the optimum? They do not do so for \(3\le n\le11\).

No formula suggested by the nine values of \(W_n\) is promoted to a
conjecture. No geometric certificate, schema, serialized result artifact, or
CLI is created by this work.
