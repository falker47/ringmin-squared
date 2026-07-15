# Fixed-Order Maximum Cyclic Ratio

Date: 2026-07-14

Last updated: 2026-07-15

## Scope And Classification

This note formalizes the exact combinatorial cycle ratio associated with the
complete fixed-order angular STN. It uses the real-arithmetic semantics proved
in `research/FIXED_ORDER_ANGULAR_STN.md` and the two angular comparisons proved
in `research/ALL_N_LOWER_BOUND.md`.

- **DEFINITION:** for a complete cyclic order \(\sigma\) of
  \(\{1,\ldots,n\}\), \(q(C)\) counts `wrap_upper` edge occurrences and
  \(S(C)\) sums endpoint-index products over all directed edge occurrences,
  with multiplicity.
- **EXACT THEOREM:** the one-wrap score
  \(\Lambda^{(1)}(\sigma)=\max_{q(C)=1}S(C)\) is exactly the maximum cyclic
  adjacent-product sum over orders induced on subsets of at least two
  positions. For two positions, the same unordered product occurs twice.
- **EXACT THEOREM:** every complete order is one-wrap saturated:
  \(\Lambda(\sigma)=\Lambda^{(1)}(\sigma)\). In fact, every vertex-simple
  cycle with at least two wraps has strictly smaller ratio. Thus the fixed-
  order and global scores are integers, although the implementation retains
  its exact `Fraction` return type.
- **EXACT THEOREM:** if \(\tau\) is obtained from \(\sigma\) by deleting
  label \(1\), and \(K(\tau)\) is the maximum induced cyclic product sum over
  nonempty core subsets, then
  \(\Lambda(\sigma)=K(\tau)\), independently of the insertion gap of label
  \(1\). Consequently \(\Lambda_n=\min_\tau K(\tau)\).
- **EXACT THEOREM:** the accepted same-order comparison gives
  \(\Lambda_n\le(n-1)W_n\). Combined with the strict cyclic-ratio sandwich,
  this yields
  \[
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{(n-1)W_n\over\pi}
  \qquad(n\ge3).
  \]
- **EXACT THEOREM:** the maximum ratio \(\Lambda(\sigma)\) gives the requested
  fixed-order sandwich
  \[
  {\Lambda(\sigma)\over\pi}-n^2
  \le \rho_\sigma
  \le {\Lambda(\sigma)\over\pi}.
  \]
  On the stated domain, both inequalities are in fact strict.
- **EXACT THEOREM:** minimizing over the finite complete-order space gives the
  analogous global sandwich for \(\Lambda_n\) and \(R_2^*(n)\).
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** bounded canonical
  enumeration for \(n=3,\ldots,8\) gives
  \((12,26,47,77,118,172)\), with no counterexample to the supplied
  prediction.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** a test-only exact
  subset/path oracle, independent of the production macro graph and Karp
  recurrence, agrees with literal induced-subset maximization on all 2,956
  canonical orders for \(n=3,\ldots,8\). This regression is not the proof of
  the all-\(n\) theorem.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** a separate
  all-core/all-insertion regression checks 437 canonical core orders and all
  2,957 insertion gaps for \(n=3,\ldots,8\). It covers the same 2,956
  complete rotation/reflection classes; the extra trial is the explicit
  two-arc degeneracy at \(n=3\).
- **EXACT THEOREM (FINITE SIX-LABEL LEMMA):** for every cyclic order
  \(\omega\) on \(S_6=\{4,\ldots,9\}\), with
  \(S_5=\{5,\ldots,9\}\),
  \[
  \max\{P_\omega(S_6),P_\omega(S_5)\}\ge239.
  \]
  The proof uses a general rearrangement lower bound and only twelve explicit
  exceptional cyclic sums, rather than enumerating the 60 classes.
- **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT):** the accepted core
  reduction, the six-label lemma, and the exact witness
  \(\tau=(9,2,3,5,8,6,7,4)\) give
  \(\Lambda_9=239\). The witness has the unique maximizing subset
  \(\{4,5,6,7,8,9\}\). This is a finite combinatorial value, not an exact
  geometric value or an all-\(n\) formula.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** an independent
  test-only oracle checks the six-label lemma on all 60 dihedral classes, and
  a separate literal audit checks all 255 nonempty witness subsets. Neither
  check calls the public enumerator or production Karp scorer.
- **VERIFIED FACT:** `src/power_ringmin/fixed_order_cycle_ratio.py` implements
  a float-free exact scorer using descending-path compression and Karp's
  maximum-cycle-mean dynamic program. Direct simple-cycle enumeration is not
  used in production and exists only as an independent small-test oracle.
- **LIMITATION:** the exact core reduction is not a closed-form evaluation of
  its minimum or evidence for convergence to a new asymptotic constant. No
  interval backend, verifier, certificate, checked artifact, schema, or
  example is changed by this work.

## 1. Complete Fixed-Order STN

Fix an integer \(n\ge3\) and a complete order
\[
\sigma=(\sigma_0,\ldots,\sigma_{n-1}),
\qquad
\{\sigma_0,\ldots,\sigma_{n-1}\}=\{1,\ldots,n\}.
\tag{CR1}
\]
The vertices of the STN are the positions \(0,\ldots,n-1\). For distinct
positions \(u,v\), define
\[
\varepsilon(u,v)=\mathbf 1_{\{u<v\}},
\qquad
s_\sigma(u,v)=\sigma_u\sigma_v.
\tag{CR2}
\]
The exact directed-edge weight at central radius \(R>0\) is
\[
w_R(u,v)
=
2\pi\varepsilon(u,v)
-\theta_R(\sigma_u^2,\sigma_v^2).
\tag{CR3}
\]
Indeed, when \(u<v\), this is the `wrap_upper` edge
\(u\to v\) of weight \(2\pi-\theta\). When \(u>v\), it is the
`forward_lower` edge \(u\to v\) of weight \(-\theta\). Thus (CR3) is just
the edge convention already proved in the fixed-order STN note, written
without splitting into two cases.

The domain is deliberately the complete Power-Ringmin instance and
\(n\ge3\). The cases \(n=1,2\) are outside the fixed-order threshold semantics
used here. Peripheral tangency is allowed, so exact STN feasibility permits
zero cycle weight.

## 2. Edge Multiplicity, \(q(C)\), And \(S(C)\)

Let \(C\) be a nonempty directed closed walk
\[
C=(v_0,v_1,\ldots,v_{\ell-1},v_\ell=v_0),
\qquad \ell\ge2,
\tag{CR4}
\]
with no self-loop step. Vertices and directed edges may repeat. Write
\(m_C(u,v)\) for the number of traversals of the directed edge \(u\to v\).
Define
\[
q(C)
=
\sum_{u\ne v}m_C(u,v)\varepsilon(u,v),
\tag{CR5}
\]
and
\[
S(C)
=
\sum_{u\ne v}m_C(u,v)\sigma_u\sigma_v.
\tag{CR6}
\]
Every occurrence is counted. In particular, a directed two-cycle
\(u\to v\to u\) traverses the same unordered pair in both directions and
satisfies
\[
q(C)=1,
\qquad
S(C)=2\sigma_u\sigma_v.
\tag{CR7}
\]
This convention is essential: the two-cycle on labels \(2,3\) supplies the
value \(12\) in the \(n=3\) computation.

Every nonempty closed walk satisfies
\[
q(C)\ge1.
\tag{CR8}
\]
If \(q(C)=0\), every traversed edge would have \(u>v\), so the position would
strictly decrease at every step and could not return to its start.

The exact cycle weight obtained by summing (CR3) is
\[
\omega_R(C)
=
2\pi q(C)
-
\sum_{u\ne v}
m_C(u,v)\theta_R(\sigma_u^2,\sigma_v^2).
\tag{CR9}
\]
Angles have the same traversal multiplicity as products. The fixed-order STN
is feasible exactly when every simple directed cycle has nonnegative weight.

Any directed closed walk decomposes into simple directed cycles. Both \(S\)
and \(q\) are additive under this decomposition, and every component has
positive \(q\) by (CR8). Hence
\[
{S(C)\over q(C)}
=
{\sum_r q(C_r)\,S(C_r)/q(C_r)\over\sum_r q(C_r)}
\le
\max_r {S(C_r)\over q(C_r)}.
\tag{CR10}
\]
It follows that repeated walks do not enlarge the optimum and that the finite
simple-cycle maximum exists. Define
\[
\boxed{
\Lambda(\sigma)
=
\max_C {S(C)\over q(C)},
}
\tag{CR11}
\]
where the maximum may equivalently be taken over all nonempty directed closed
walks or only over vertex-simple directed cycles of lengths \(2,\ldots,n\).
The value is a positive rational number at this stage; the one-wrap theorem
below strengthens this to an integer for complete Power-Ringmin orders.

### Cyclic-order symmetry

Changing the linear cut of \(\sigma\) preserves \(\Lambda\). Moving one
position through the cut changes the edge indicator by a vertex coboundary,
\[
\varepsilon'(u,v)
=
\varepsilon(u,v)+h(v)-h(u),
\tag{CR12}
\]
for the indicator \(h\) of the moved vertex. The extra terms telescope on
every closed walk, so \(q(C)\) is unchanged. Reflection also preserves the
maximum: reflect the positions and reverse each directed cycle; this preserves
both \(S\) and \(q\). Therefore minimization over the repository's canonical
rotation/reflection representatives covers the complete cyclic-order space.

### One-wrap cycles and induced subset orders

Define the one-wrap score by
\[
\Lambda^{(1)}(\sigma)
=
\max\{S(C): C\text{ is a nonempty directed closed walk and }q(C)=1\}.
\tag{CR12a}
\]
The denominator is absent because it equals one on this class.

Let \(T=\{i_0<\cdots<i_{m-1}\}\) be a nonempty subset of positions, and
let \(\sigma|_T\) denote the cyclic order induced by
\(\sigma\). Put
\[
P_\sigma(T)
=
\sum_{r=0}^{m-1}
\sigma_{i_r}\sigma_{i_{r+1\bmod m}}.
\tag{CR12b}
\]
When \(m=1\), this convention gives
\(P_\sigma(\{i_0\})=\sigma_{i_0}^2\). When \(m=2\), it gives
\(\sigma_{i_0}\sigma_{i_1}+\sigma_{i_1}\sigma_{i_0}\): the same unordered
pair contributes twice, exactly as in (CR7).

A closed walk with \(q=1\) cannot repeat a vertex. Rotate it so that its
unique ascending edge occurs first. Every later edge strictly decreases its
position until the walk closes, so repetition is impossible. If its selected
positions are \(i_0<\cdots<i_{m-1}\), the unique ascent must leave the least
position and enter the greatest one; all later positions are then forced into
strictly decreasing order. The cycle is therefore
\[
i_0\longrightarrow i_{m-1}\longrightarrow i_{m-2}
\longrightarrow\cdots\longrightarrow i_1\longrightarrow i_0.
\tag{CR12c}
\]
Its product sum is \(P_\sigma(T)\), since reversing a cyclic order does not
change its undirected adjacent-product sum. Conversely, (CR12c) gives a
one-wrap cycle for every \(T\) of cardinality at least two. Hence
\[
\boxed{
\Lambda^{(1)}(\sigma)
=
\max_{\substack{T\subseteq\{0,\ldots,n-1\}\\|T|\ge2}}
P_\sigma(T)
=
\max_{\varnothing\ne T\subseteq\{0,\ldots,n-1\}}
P_\sigma(T).
}
\tag{CR12d}
\]
The second equality holds because, for \(n\ge3\), every singleton score is at
most \(n^2\), while the subset carrying labels \(n-1,n\) has score
\(2n(n-1)>n^2\). Cardinality at least two is the cycle-faithful convention.

### Exact one-wrap saturation

The duplicated-multiset pairing lemma from
`research/ALL_N_LOWER_BOUND.md`, applied to the complete induced order, gives
\[
P_\sigma(\{0,\ldots,n-1\})
\ge
{n(n+1)(n+2)\over6}.
\tag{CR12e}
\]
For completeness, the cycle edges pair the multiset containing two copies of
each label. Oppositely pairing its sorted entries is the rearrangement lower
bound, and its value is
\(\sum_{k=1}^n k(n+1-k)=n(n+1)(n+2)/6\). Thus
\(\Lambda^{(1)}(\sigma)\ge n(n+1)(n+2)/6\).

Now let \(C\) be a vertex-simple directed cycle with selected label set
\(U\). The inequality \(2ij\le i^2+j^2\), summed over its edge occurrences,
and degree two at every selected vertex give
\[
S(C)
\le
\sum_{i\in U}i^2
\le
\sum_{i=1}^n i^2
={n(n+1)(2n+1)\over6}.
\tag{CR12f}
\]
If \(q(C)\ge2\), then
\[
{S(C)\over q(C)}
\le {1\over2}\sum_{i=1}^n i^2
={n(n+1)(n+2)\over6}-{n(n+1)\over4}
<{n(n+1)(n+2)\over6}
\le\Lambda^{(1)}(\sigma).
\tag{CR12g}
\]
By (CR10), only vertex-simple cycles are needed for the full maximum. The
cycles with \(q=1\) give (CR12d), while (CR12g) strictly excludes every
vertex-simple cycle with more wraps. Therefore
\[
\boxed{
\Lambda(\sigma)=\Lambda^{(1)}(\sigma)
=
\max_{\substack{T\subseteq\{0,\ldots,n-1\}\\|T|\ge2}}
P_\sigma(T)
=
\max_{\varnothing\ne T\subseteq\{0,\ldots,n-1\}}
P_\sigma(T)
\qquad(n\ge3).
}
\tag{CR12h}
\]
This is an **EXACT THEOREM for every complete order**, not an inference from
the bounded experiment. It also proves that \(\Lambda(\sigma)\), and hence
\(\Lambda_n\), is an integer. A general closed walk with \(q>1\) can still
attain the same ratio, for example by repeating a maximizing one-wrap simple
cycle. Equality in the weighted average (CR10) requires every simple
component to be one-wrap and maximizing. The strict separation in (CR12g) is
specifically a statement about vertex-simple multi-wrap cycles.

### Exact elimination of label \(1\)

Let
\[
\tau=(a_0,\ldots,a_{n-2})
\tag{CR12i}
\]
be the cyclic core order obtained from \(\sigma\) by deleting label \(1\).
For a nonempty subset \(U\subseteq\{2,\ldots,n\}\), write
\(P_\tau(U)\) for the cyclic adjacent-product sum in the order induced by
\(\tau\), with the same conventions
\[
P_\tau(\{j\})=j^2,
\qquad
P_\tau(\{i,j\})=2ij.
\tag{CR12j}
\]
Define
\[
\boxed{
K(\tau)
=
\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U).
}
\tag{CR12k}
\]
Because every label occurs once, label subsets and their position subsets
will be identified below.

Every subset avoiding label \(1\) has exactly the same induced cyclic order
before and after deletion, so
\[
P_\sigma(U)=P_\tau(U)
\qquad
(\varnothing\ne U\subseteq\{2,\ldots,n\}).
\tag{CR12l}
\]
In particular, a core subset attaining \(K(\tau)\) supplies the same score
inside \(\sigma\).

It remains to classify the subsets containing label \(1\).

1. The singleton has
   \[
   P_\sigma(\{1\})=1<4=P_\tau(\{2\})\le K(\tau).
   \tag{CR12m}
   \]
2. For \(j\ge2\), the two-element convention gives
   \[
   P_\sigma(\{1,j\})=2j\le j^2=P_\tau(\{j\})\le K(\tau).
   \tag{CR12n}
   \]
   The first inequality is an equality only at \(j=2\).
3. Suppose \(T\) contains label \(1\) and at least two core labels, and put
   \(U=T\setminus\{1\}\). Let \(a,b\) be the two distinct core neighbors
   of \(1\) in the cyclic order induced by \(T\). Deleting \(1\) replaces
   the two contributions \(a\cdot1+1\cdot b\) by one contribution \(ab\).
   Hence
   \[
   P_\tau(U)-P_\sigma(T)
   =ab-a-b
   =(a-1)(b-1)-1
   \ge1,
   \tag{CR12o}
   \]
   because \(a,b\) are distinct integers at least two. This calculation also
   covers \(|U|=2\): in that case \(P_\tau(U)=2ab\), and only the occurrence
   on the arc through label \(1\) is replaced.

Thus every subset containing label \(1\) is bounded by a core subset, while
(CR12l) realizes the core maximum unchanged. Combining this classification
with (CR12h) proves
\[
\boxed{
\Lambda(\sigma)=K(\tau).
}
\tag{CR12p}
\]
The right side contains no insertion-gap data: the cyclic-ratio score is
therefore independent of where label \(1\) is inserted into a fixed core
order. Equation (CR12o) makes the third case strictly smaller than its core
deletion. The first two cases have score at most \(n^2\), while
\[
K(\tau)\ge P_\tau(\{n-1,n\})=2n(n-1)>n^2.
\tag{CR12q}
\]
Hence no maximizing subset contains label \(1\).
This independence concerns the separable product score \(\Lambda\), not the
exact angular threshold \(\rho_\sigma\) or fixed-order feasibility.

The smallest case is explicit. For \(n=3\), the unique core class is
\(\tau=(3,2)\), and its nonempty-subset scores are \(9,4,12\), so
\[
K(3,2)=12.
\tag{CR12r}
\]
Insertion into its two cyclic arcs gives \((3,1,2)\) and \((3,2,1)\).
They are reflections, represent one complete canonical class, and both have
\(\Lambda=12\).

## 3. Exact Fixed-Order Sandwich

For distinct \(1\le i,j\le n\) and \(R>0\), the two angular estimates needed
here are
\[
\boxed{
{2ij\over R+n^2}
<
\theta_R(i^2,j^2)
<
{2ij\over R}.
}
\tag{CR13}
\]
The right inequality is the strict general angular majorant proved in
`research/ALL_N_LOWER_BOUND.md`. For the left inequality, that note records
the valid weak estimate. Its one-line strict refinement follows because its
argument has \(0<x<1\), so \(\arcsin x>x\), while
\(\sqrt{(R+i^2)(R+j^2)}\le R+n^2\).

Let \(F_\sigma\) be the feasible positive-radius set and
\(\rho_\sigma=\inf F_\sigma\). The fixed-order STN theorem proves
\[
F_\sigma=[\rho_\sigma,\infty),
\qquad
\rho_\sigma>0.
\tag{CR14}
\]

### Lower side

Let \(C_*\) attain (CR11). If \(R\in F_\sigma\), then (CR9), feasibility,
and the strict left estimate in (CR13) give
\[
0
\le \omega_R(C_*)
<
2\pi q(C_*)-{2S(C_*)\over R+n^2}.
\tag{CR15}
\]
Therefore
\[
R
>
{S(C_*)\over\pi q(C_*)}-n^2
=
{\Lambda(\sigma)\over\pi}-n^2.
\tag{CR16}
\]
Applying (CR16) at the attained threshold \(R=\rho_\sigma\) yields
\[
\rho_\sigma
>
{\Lambda(\sigma)\over\pi}-n^2.
\tag{CR17}
\]
Without using threshold attainment, taking the infimum would give only the
requested non-strict inequality. If the expression on the right is
nonpositive, it remains a valid algebraic lower bound but is not a claim about
negative central radii.

### Upper side

Put
\[
R_0={\Lambda(\sigma)\over\pi}>0.
\tag{CR18}
\]
For every simple directed cycle \(C\), the strict right estimate in (CR13)
gives
\[
\omega_{R_0}(C)
>
2\pi q(C)-{2S(C)\over R_0}
\ge0.
\tag{CR19}
\]
All simple cycle weights are strictly positive, so the negative-cycle theorem
makes the STN feasible at \(R_0\). Since there are only finitely many simple
cycles and their weights are continuous, their strict positivity persists on
some left neighborhood of \(R_0\). Hence
\[
\rho_\sigma<R_0={\Lambda(\sigma)\over\pi}.
\tag{CR20}
\]

Combining the two sides proves the requested exact sandwich
\[
\boxed{
{\Lambda(\sigma)\over\pi}-n^2
\le \rho_\sigma
\le {\Lambda(\sigma)\over\pi}
}
\tag{CR21}
\]
and the sharper endpoint statement valid on the present domain,
\[
\boxed{
{\Lambda(\sigma)\over\pi}-n^2
< \rho_\sigma
< {\Lambda(\sigma)\over\pi}
\qquad(n\ge3).
}
\tag{CR22}
\]
Equivalently,
\[
0<\Lambda(\sigma)-\pi\rho_\sigma<\pi n^2.
\tag{CR23}
\]

## 4. Global Version

Let \(\Omega_n\) be the finite space of complete cyclic orders, with or
without quotienting by rotation and reflection, and define
\[
\Lambda_n
=
\min_{\sigma\in\Omega_n}\Lambda(\sigma).
\tag{CR24}
\]
Every feasible full configuration has one complete cyclic order, and the
fixed-order feasible sets are closed upper intervals. Finiteness therefore
gives
\[
R_2^*(n)=\min_{\sigma\in\Omega_n}\rho_\sigma.
\tag{CR25}
\]

For the lower side, apply (CR17) to an order minimizing \(\rho_\sigma\). For
the upper side, apply (CR20) to an order minimizing \(\Lambda(\sigma)\). This
proves
\[
\boxed{
{\Lambda_n\over\pi}-n^2
\le R_2^*(n)
\le {\Lambda_n\over\pi}
}
\tag{CR26}
\]
and, more sharply,
\[
\boxed{
{\Lambda_n\over\pi}-n^2
< R_2^*(n)
< {\Lambda_n\over\pi}
\qquad(n\ge3).
}
\tag{CR27}
\]
Thus the exact global additive relation is
\[
\boxed{
0<\Lambda_n-\pi R_2^*(n)<\pi n^2.
}
\tag{CR28}
\]

Let \(\mathcal T_n\) be the finite cyclic-order space of the core labels
\(\{2,\ldots,n\}\). Deleting label \(1\) maps every complete cyclic order
to one member of \(\mathcal T_n\), and inserting label \(1\) into any core
gap supplies a complete preimage. Equation (CR12p) is constant over all such
preimages. Therefore the global objective has the exact reduced form
\[
\boxed{
\Lambda_n
=
\min_{\tau\in\mathcal T_n}K(\tau).
}
\tag{CR28a}
\]
This is a reduction from complete to core orders, not a closed-form evaluation
or a classification of the minimizing core orders.

## 5. Exact Scorer Without Cycle Enumeration

The proof that simple cycles suffice does not make their enumeration the
production algorithm. The implemented scorer exploits the special resource
structure of the fixed-order graph.

### Descending-path closure

Edges with \(q\)-contribution zero strictly decrease their position, so they
form a directed acyclic graph. For positions \(h\ge v\), let \(D_{h,v}\) be
the maximum product sum along a descending path from \(h\) to \(v\), allowing
the empty path when \(h=v\). Then
\[
D_{v,v}=0,
\qquad
D_{h,v}
=
\max_{v\le z<h}
\bigl(\sigma_h\sigma_z+D_{z,v}\bigr)
\quad(h>v).
\tag{CR29}
\]
Increasing \(h\) gives an exact acyclic dynamic program.

### One-wrap macro graph

Every closed walk can be split at its \(q(C)\) ascending `wrap_upper` edges.
Each block consists of one ascending edge \(u\to h\), followed by a possibly
empty descending path ending at the tail \(v\) of the next ascending edge.
Position \(n-1\) cannot be such a tail, so the macro vertices are
\(0,\ldots,n-2\). Define the complete macro-edge weights
\[
M_{u,v}
=
\max_{h\ge\max(u+1,v)}
\bigl(\sigma_u\sigma_h+D_{h,v}\bigr).
\tag{CR30}
\]
The macro graph retains the cases \(u=v\) as self-loops; these encode
legitimate original closed walks with one `wrap_upper` occurrence. Every macro
edge has resource one. Compressing an original closed walk gives a macro closed
walk of length \(q(C)\) and at least its product sum. Conversely, expanding
the maximizing witness for every macro edge gives an original closed walk
whose \(q\)-value equals the macro-walk length and whose product sum equals the
macro-walk weight. Its ordinary directed-edge length may be larger. Closed-walk
decomposition then proves that \(\Lambda(\sigma)\) is exactly the maximum cycle
mean of \(M\).

### Karp dynamic program

Put \(N=n-1\). The macro graph is complete and hence strongly connected.
Choose macro vertex zero as a source, set
\[
F_0(0)=0,
\qquad
F_0(v)=-\infty\quad(v\ne0),
\tag{CR31}
\]
and compute
\[
F_k(v)=\max_u\bigl(F_{k-1}(u)+M_{u,v}\bigr)
\qquad(1\le k\le N).
\tag{CR32}
\]
Karp's exact maximum-cycle-mean formula is
\[
\Lambda(\sigma)
=
\max_v
\min_{\substack{0\le k<N\\F_k(v)>-\infty}}
{F_N(v)-F_k(v)\over N-k}.
\tag{CR33}
\]
The implementation represents unreachable states by `None`, not a floating
sentinel. All \(D\), \(M\), and \(F\) values are integers; only the ratios in
(CR33) are constructed and compared as `Fraction`. The descending closure,
macro graph, and Karp recurrence each take \(O(n^3)\) exact integer operations,
and the memory bound is \(O(n^2)\).

The public scorer accepts any complete permutation, not only a canonical one.
The separate global enumerator rejects values outside \(3\le n\le8\), checks
the explicit canonical-order ceiling before generating permutations, and has
no CLI or serialized artifact contract.

The one-wrap theorem proves that every public score has denominator one. The
production implementation deliberately retains its full-ratio Karp algorithm
and `Fraction` result: the new induced-subset and subset/path implementations
remain test-only independent oracles, and the hard production enumeration
domain is unchanged.

## 6. Finite Exact Results

### Public bounded enumeration, \(n=3,\ldots,8\)

The production scorer was minimized over every canonical complete order using
the repository convention: put \(n\) first and retain the reflection with
second label smaller than the last. The direct simple-cycle oracle independently
checked every canonical order through \(n=6\). A separate exact subset/path
dynamic program anchors each simple cycle at its least position and retains
states `(visited subset, last position, wrap count)`; it shares neither the
descending closure, macro graph, nor Karp recurrence with production. That
oracle and literal induced-subset maximization agree order by order for every
canonical order through \(n=8\).

For the comparison columns only, recall the separate core definition
\[
W_n
=
\min_\tau
\max_{0\le u<v\le n-2}
{\tau_u\tau_v\over d_\tau(u,v)},
\tag{CR33a}
\]
where \(\tau\) ranges over cyclic orders of \(\{2,\ldots,n\}\) and
\(d_\tau(u,v)=\min(v-u,n-1-(v-u))\) is smaller circular positional distance.

| \(n\) | Canonical complete orders | \(\Lambda_n\) | Canonical minimizers | Lexicographically least representative | \(W_n\) | \((n-1)W_n\) |
|---:|---:|---:|---:|---|---:|---:|
| 3 | 1 | 12 | 1 | `(3,1,2)` | 6 | 12 |
| 4 | 3 | 26 | 3 | `(4,1,2,3)` | 12 | 36 |
| 5 | 12 | 47 | 4 | `(5,1,2,4,3)` | 15 | 60 |
| 6 | 60 | 77 | 15 | `(6,1,2,3,5,4)` | 20 | 100 |
| 7 | 360 | 118 | 24 | `(7,1,2,3,5,6,4)` | 24 | 144 |
| 8 | 2520 | 172 | 84 | `(8,1,2,3,5,6,7,4)` | 30 | 210 |

This is a **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION)** over 2,956
canonical orders. The supplied prediction
\[
(\Lambda_3,\ldots,\Lambda_8)=(12,26,47,77,118,172)
\tag{CR34}
\]
is reproduced exactly, so there is no counterexample to preserve in this
bounded domain. The counts and representative orders are additional finite
data, not a closed-form evaluation or conjecture. The independent oracle also
verifies \(\Lambda=\Lambda^{(1)}\) on every one of these bounded orders, but
the all-order equality is the exact proof (CR12a)--(CR12h), not this finite
regression. The production ceiling remains 2,520 canonical orders at
\(n=8\); no larger production enumeration was enabled.

The elimination theorem has a separate test-only regression over every
canonical core order and every cyclic insertion gap. The exact counts are:

| \(n\) | Canonical core orders | Insertion trials | Distinct complete classes | \(\min K=\Lambda_n\) | Core \(K\)-minimizers | Complete \(\Lambda\)-minimizers |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 2 | 1 | 12 | 1 | 1 |
| 4 | 1 | 3 | 3 | 26 | 1 | 3 |
| 5 | 3 | 12 | 12 | 47 | 1 | 4 |
| 6 | 12 | 60 | 60 | 77 | 3 | 15 |
| 7 | 60 | 360 | 360 | 118 | 4 | 24 |
| 8 | 360 | 2,520 | 2,520 | 172 | 12 | 84 |

In total, 437 core classes and 2,957 insertion trials cover all 2,956
complete classes. The sole duplicate is the explicit \(n=3\) reflection in
(CR12r). For \(n\ge4\), every core class has \(n-1\) distinct labeled cyclic
gaps, so the complete minimizer count is \((n-1)\) times the core minimizer
count. Each insertion is checked both by literal exact subset maximization and
by the production scorer. This is a **VERIFIED FACT (FINITE EXHAUSTIVE EXACT
COMPUTATION)**, not the proof of (CR12p), and it does not extend the production
domain beyond \(n=8\).

### Reduced exact evaluation at \(n=9\), without public enumeration

Put
\[
S_6=\{4,5,6,7,8,9\},
\qquad
S_5=\{5,6,7,8,9\}.
\tag{L9-1}
\]
For a cyclic order \(\omega\) on \(S_6\), write \(P_\omega(S)\) for the
cyclic adjacent-product sum in the order induced on \(S\). Let \(a,b\) be
the two neighbors of label \(4\) in \(\omega\). Deleting \(4\) replaces
the contributions \(4a+4b\) by \(ab\), so
\[
P_\omega(S_6)
=P_\omega(S_5)+4(a+b)-ab
=P_\omega(S_5)+16-(a-4)(b-4).
\tag{L9-2}
\]

The duplicated-multiset rearrangement bound, applied to any cyclic order on
\(S_5\), gives the human-checkable baseline
\[
P_\omega(S_5)
\ge5\cdot9+6\cdot8+7^2+8\cdot6+9\cdot5
=235.
\tag{L9-3}
\]
If \(\{a,b\}\) is neither \(\{7,9\}\) nor \(\{8,9\}\), then the distinct
integers \(a-4,b-4\in\{1,\ldots,5\}\) have product at most \(12\).
Equations (L9-2)--(L9-3) therefore give
\(P_\omega(S_6)\ge235+4=239\).

Only two neighbor pairs remain. Name them so that \(a<b\), and reflect the
cycle if necessary so that the new edge created by deleting label \(4\) is
oriented \(a\to b\). The induced five-cycle can then be written
\((a,b,x,y,z)\). The following table lists all six possibilities for the
three remaining labels, in lexicographic order. Every entry is a direct sum
of five integer products.

| \(\{a,b\}\) | Permutations \((x,y,z)\) | Corresponding values of \(P_\omega(S_5)\) | Minimum |
|---|---|---|---:|
| \(\{7,9\}\) | `568, 586, 658, 685, 856, 865` | `242, 238, 243, 240, 247, 248` | 238 |
| \(\{8,9\}\) | `567, 576, 657, 675, 756, 765` | `245, 242, 247, 243, 248, 247` | 242 |

For \(\{a,b\}=\{7,9\}\), the correction in (L9-2) is \(1\), so
\(P_\omega(S_6)\ge239\). For \(\{a,b\}=\{8,9\}\), the table already gives
\(P_\omega(S_5)\ge242\). This proves the finite exact lemma
\[
\boxed{
\max\{P_\omega(S_6),P_\omega(S_5)\}\ge239
\quad\text{for every cyclic order \(\omega\) on \(S_6\)}.
}
\tag{L9-4}
\]
The argument is a proof, not a conclusion drawn from the 60-class test.

For any core order \(\tau\) of \(\{2,\ldots,9\}\), both \(S_6\) and
\(S_5\) are admitted in the definition of \(K(\tau)\). Applying (L9-4) to
the order induced by \(\tau\) gives
\[
K(\tau)
\ge\max\{P_\tau(S_6),P_\tau(S_5)\}
\ge239.
\tag{L9-5}
\]

For the reverse inequality, consider the supplied core order
\[
\tau_*=(9,2,3,5,8,6,7,4).
\tag{L9-6}
\]
Its complete-core cyclic sum is \(233\). For an oriented arc from \(i\) to
\(j\) in this order, define its shortcut gain by
\[
g(i,j)
=ij-
\sum_{xy\text{ an edge on the oriented arc from }i\text{ to }j}xy.
\tag{L9-7}
\]
Adjacent endpoints have gain zero. The following table gives every
nontrivial gain; \(r\) is the number of skipped internal vertices, and each
cell has the form `endpoint:gain`.

| Start | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) | \(r=5\) | \(r=6\) |
|---:|---:|---:|---:|---:|---:|---:|
| 9 | `3:+3` | `5:+6` | `8:-7` | `6:-73` | `7:-106` | `4:-161` |
| 2 | `5:-11` | `8:-45` | `6:-97` | `7:-137` | `4:-171` | `9:-197` |
| 3 | `8:-31` | `6:-85` | `7:-124` | `4:-161` | `9:-182` | `2:-221` |
| 5 | `6:-58` | `7:-95` | `4:-138` | `9:-149` | `2:-202` | `3:-203` |
| 8 | `7:-34` | `4:-86` | `9:-82` | `2:-156` | `3:-154` | `5:-153` |
| 6 | `4:-46` | `9:-52` | `2:-112` | `3:-112` | `5:-115` | `8:-137` |
| 7 | `9:-1` | `2:-68` | `3:-67` | `5:-68` | `8:-87` | `6:-149` |
| 4 | `2:-46` | `3:-48` | `5:-55` | `8:-83` | `6:-139` | `7:-177` |

Let \(U\) be an induced subset with \(|U|\ge2\). The oriented arcs from
each selected label to the next selected label partition the eight edges of
the complete core cycle. Consequently
\[
P_{\tau_*}(U)-233
=\sum_{(i,j)\text{ a selected gap}}g(i,j).
\tag{L9-8}
\]
For \(|U|=2\), the two complementary arcs contribute the two shortcuts
\(ij+ji=2ij\), exactly matching the adopted two-element convention.

The only positive nontrivial gains in the table are \(g(9,3)=3\) and
\(g(9,5)=6\). Exactly one selected gap can leave label \(9\), so (L9-8) is
at most \(6\). Equality forces the gap \(9\to5\), skipping labels \(2,3\),
and every other gap to be adjacent because there is no nontrivial zero gain.
Thus equality forces
\[
U=S_6,
\qquad
\tau_*|_{S_6}=(9,5,8,6,7,4),
\tag{L9-9}
\]
whose score is
\[
9\cdot5+5\cdot8+8\cdot6+6\cdot7+7\cdot4+4\cdot9=239.
\tag{L9-10}
\]
Singleton scores are at most \(9^2=81\). Therefore
\[
K(\tau_*)=239,
\qquad
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,9\}}
P_{\tau_*}(U)=\{S_6\}.
\tag{L9-11}
\]

Combining (L9-5), (L9-11), and the accepted reduction (CR28a) proves the
requested value
\[
\boxed{\Lambda_9=239.}
\tag{L9-12}
\]
This is a **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT)**. It neither
extends the production enumeration past \(n=8\) nor gives an exact value of
\(R_2^*(9)\), a geometric statement, an all-\(n\) formula, an asymptotic
claim, or a classification of all minimizing core orders.

The independent test-only lower-bound oracle fixes label \(9\) to remove
rotations, generates the \(5!\) remaining permutations directly, and keeps
the orientation whose second label is smaller than its last. It therefore
checks exactly \(5!/2=60\) dihedral classes without calling repository
canonicalizers, the public enumerator, or the production scorer. Its minimum
of \(\max\{P(S_6),P(S_5)\}\) is 239. A separate literal enumeration of all
\(2^8-1=255\) nonempty subsets of \(\tau_*\) verifies (L9-11), records
\(S_6\) as the sole global maximizer, and gives the following independently
reproducible per-cardinality audit:

| \(|U|\) | Maximum score | Unique maximizing subset |
|---:|---:|---|
| 1 | 81 | \(\{9\}\) |
| 2 | 144 | \(\{8,9\}\) |
| 3 | 191 | \(\{7,8,9\}\) |
| 4 | 225 | \(\{6,7,8,9\}\) |
| 5 | 238 | \(S_5\) |
| 6 | 239 | \(S_6\) |
| 7 | 236 | \(\{3,4,5,6,7,8,9\}\) |
| 8 | 233 | \(\{2,3,4,5,6,7,8,9\}\) |

These two sweeps are **VERIFIED FACTS (FINITE EXHAUSTIVE EXACT
COMPUTATION)** and independently audit the finite proof; they are not its
source and do not alter a public enumeration limit.

## 7. Comparison With \(W\)

The native definitions of the two symbols describe different combinatorial
relaxations.

- \(\Lambda(\sigma)\) uses a **complete** order of
  \(\{1,\ldots,n\}\), sums products around directed STN cycles, and divides
  by the number of `wrap_upper` occurrences. It represents variable angular
  spacings through the difference-constraint cycle criterion.
- The repository's \(W(\tau)\) uses a **core** order of
  \(\{2,\ldots,n\}\), maximizes one pair ratio
  \(ij/d_\tau(i,j)\), and controls a construction on equally spaced regular
  directions.

Exact label-one elimination bridges the order domains through the core
objective \(K\), but it does not identify \(K\) with the scalar pair objective
\(W\). In particular, the last two columns of the bounded table compare
separate exact objectives; they do not establish
\(\Lambda_n=(n-1)W_n\) or equality of minimizing order sets.

There is one useful exact comparison after first putting both quantities on
the **same** order. Let
\(\tau=(a_0,\ldots,a_{m-1})\) be a cyclic order of \(m\ge2\) distinct
positive labels. Extend the purely combinatorial definitions (CR5)--(CR11) to
these labels by using \(s(u,v)=a_u a_v\), and call the resulting maximum
\(\Lambda_{\rm same}(\tau)\). For positions \(u\ne v\), put
\[
d_\tau(u,v)=\min(|u-v|,m-|u-v|)
\tag{CR34a}
\]
and define
\[
W_{\rm same}(\tau)=\max_{0\le u<v<m}{a_u a_v\over d_\tau(u,v)}.
\tag{CR35}
\]
For an edge \(u\to v\), its smaller circular distance satisfies
\[
d_\tau(u,v)
\le
\begin{cases}
m-(v-u),&u<v,\\
u-v,&u>v.
\end{cases}
\tag{CR36}
\]
On a closed walk, the total positive position increase equals the total
absolute negative decrease. Summing (CR36) therefore gives
\[
\sum_{e\in C}d_\tau(e)\le m q(C).
\tag{CR37}
\]
Since each edge product is at most
\(W_{\rm same}(\tau)d_\tau(e)\),
\[
\boxed{
\Lambda_{\rm same}(\tau)\le mW_{\rm same}(\tau).
}
\tag{CR38}
\]
This need not be equality: on the core order \(\tau=(4,2,3)\),
\(\Lambda_{\rm same}(\tau)=26\), while \(3W(\tau)=36\).

For a Power-Ringmin core order, singleton scores do not attain \(K\), because
the pair \(\{n-1,n\}\) has score \(2n(n-1)>n^2\). Every relevant subset in
the definition of \(K(\tau)\) is therefore a one-wrap cycle admitted by
\(\Lambda_{\rm same}(\tau)\). Applying (CR38) with \(m=n-1\) gives the
pointwise comparison
\[
\boxed{
K(\tau)
\le\Lambda_{\rm same}(\tau)
\le(n-1)W(\tau).
}
\tag{CR38a}
\]
Using the exact reduction (CR28a) and choosing an order minimizing \(W\),
\[
\boxed{
\Lambda_n\le(n-1)W_n.
}
\tag{CR38b}
\]
The inequality is intentionally non-strict; equality holds at \(n=3\).
Combining it with (CR27) yields the geometric upper bound
\[
\boxed{
R_2^*(n)
< {\Lambda_n\over\pi}
\le {(n-1)W_n\over\pi}
\qquad(n\ge3).
}
\tag{CR38c}
\]
Unlike the regular-direction construction followed by radius-one insertion,
this deduction is valid for every \(n\ge3\) and uses neither construction.
It is an upper bound, not an exact geometric optimum or a certificate claim.
Since the separately proved product-distance theorem gives
\(W_n/n^2\to8/25\), it also recovers
\[
\limsup_{n\to\infty}{\Lambda_n\over n^3}\le{8\over25},
\qquad
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{8\over25\pi}.
\tag{CR38d}
\]

Deleting label \(1\) makes the full \(\Lambda\) score a function of the
entire induced core order through \(K\), but not a function of the single
number \(W(\tau)\). Exact finite examples at \(n=6\) are:

- `(6,1,2,4,5,3)` and `(6,3,5,2,1,4)` both have \(\Lambda=77\), while
  their induced-core \(W\) scores are respectively \(20\) and \(24\);
- `(6,1,2,4,5,3)` and `(6,2,5,4,1,3)` both induce \(W=20\), while their
  full scores are respectively \(77\) and \(80\).

These examples disprove identification of \(K\) with \(W\); they are
consistent with the global one-sided comparison (CR38b).

## 8. Asymptotic Consequences And Non-Consequences

Dividing (CR28) by \(\pi n^3\) gives the exact vanishing-error comparison
\[
0
<
{\Lambda_n\over\pi n^3}
-{R_2^*(n)\over n^3}
<
{1\over n}.
\tag{CR39}
\]
Consequently, normalized liminf, limsup, and all subsequential limits agree
after the factor \(\pi\). Combining this relation with the already-proved
geometric bounds gives
\[
\Lambda_n=\pi R_2^*(n)+O(n^2),
\qquad
\Lambda_n=\Theta(n^3),
\tag{CR40}
\]
\[
{\Lambda_n\over\pi R_2^*(n)}\longrightarrow1,
\tag{CR41}
\]
and
\[
{2(\sqrt2-1)\over3}
\le
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\le
\limsup_{n\to\infty}{\Lambda_n\over n^3}
\le
{8\over25}.
\tag{CR42}
\]

None of these statements proves that either normalized sequence converges, or
identifies an exact leading constant. In particular, the bounded values in
(CR34) do not give a closed-form evaluation of (CR28a); \(8/25\) remains an
upper coefficient, not an exact constant.

Further non-consequences are important.

- The theorem does not assert \(\rho_\sigma=\Lambda(\sigma)/\pi\), equality
  of minimizing order sets, or \(\Lambda_n=(n-1)W_n\). The exact global
  relation proved here is the one-sided inequality (CR38b).
- Insertion-gap independence applies to \(\Lambda(\sigma)\), not to the exact
  angular threshold \(\rho_\sigma\) or to fixed-order feasible-radius sets.
- One-wrap saturation concerns the separable product weights
  \(\sigma_u\sigma_v\). It does not show that checking only one-wrap cycles
  suffices for the exact angular STN weights
  \(2\pi\varepsilon(u,v)-\theta_R(\sigma_u^2,\sigma_v^2)\), or that an exact
  angular critical/negative cycle must have one wrap.
- A cycle attaining \(\Lambda(\sigma)\) is a witness for the product-angle
  comparison, not necessarily a critical or negative exact-STN cycle at
  \(\rho_\sigma\). For \(n=3\), the two-cycle on labels \(2,3\) attains
  \(\Lambda=12\), but its exact weight
  \(2\pi-2\theta_R(4,9)\) is positive for every \(R>0\).
- The exact real-arithmetic theorem supplies no new interval-backend audit,
  certificate, exact geometric finite optimum value, or checked-artifact
  conclusion.
