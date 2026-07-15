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
- **EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION):** equality in the
  six-label lemma forces the induced cycle `(9,5,8,6,7,4)` up to dihedral
  symmetry. Label `3` may be inserted in exactly the four gaps not incident
  to label `4`, after which label `2` may be inserted in any of the seven
  gaps. These are exactly 28 dihedral core minimizers. Exact label-one
  insertion gives exactly \(28\cdot8=224\) complete minimizer classes.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** an independent
  test-only oracle checks all \(7!/2=2{,}520\) dihedral core classes and all
  255 nonempty subsets of each, recording every maximizing subset. It finds
  exactly the 28 proved classes. A separate oracle checks the six-label lemma
  on all 60 dihedral classes. Neither check calls a repository canonicalizer,
  the public enumerator, or the production Karp scorer.
- **EXACT THEOREM (FINITE SEVEN-LABEL LEMMA):** for every cyclic order
  \(\omega\) on \(\{4,\ldots,10\}\),
  \[
  \max\{P_\omega(\{4,\ldots,10\}),P_\omega(\{5,\ldots,10\})\}\ge323.
  \]
  The proof applies the duplicated-multiset pairing relaxation to
  \(\{5,\ldots,10\}\), classifies exactly the eight pairing signatures at
  the only relevant integer levels 320--322, and then applies the exact
  correction for inserting label \(4\).
- **EXACT THEOREM (FINITE SEVEN-LABEL EQUALITY CLASSIFICATION):** equality in
  the preceding lemma holds in exactly two dihedral classes, represented by
  `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`. The proof treats separately
  tail scores 323 and 322. In the 323 branch, the insertion correction leaves
  four possible tail edges; fixed-edge pairing bounds eliminate two, and the
  exact residual equality signatures eliminate a third. Exactly one insertion
  gap survives in each score branch.
- **EXACT THEOREM (FINITE LABEL-THREE INSERTION-GAP CLASSIFICATION):** write
  \(K_{\ge3}\) for the maximum induced-subset score of a partial cycle on
  labels \(3,\ldots,10\). Inserting label \(3\) into
  `(10,4,7,8,6,9,5)` gives \(K_{\ge3}=323\) in every gap except
  \(\{4,7\}\), where it gives 326. Inserting label \(3\) into
  `(10,5,9,4,7,8,6)` gives \(K_{\ge3}=323\) except on
  \(\{4,9\}\) and \(\{4,7\}\), where it gives 326 and 328. The proof uses
  the exact insertion correction and a complete shortcut-gain certificate,
  not subset enumeration.
- **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT):** the seven-label
  lemma and the exact shortcut-gain witness
  \(\tau=(10,2,3,4,7,8,6,9,5)\) give
  \(\Lambda_{10}=323\). Exactly two witness subsets maximize: the six-label
  tail \(\{5,\ldots,10\}\) and the eight-label tail
  \(\{3,\ldots,10\}\).
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** independent
  test-only code checks the lemma on all \(6!/2=360\) seven-label dihedral
  classes, literally scores all \(2^9-1=511\) nonempty witness subsets, and
  separately checks all 14 label-three insertions and all 255 nonempty
  subsets of each. None of these paths calls a repository canonicalizer, the
  public enumerator, or the production scorer.
- **VERIFIED FACT:** `src/power_ringmin/fixed_order_cycle_ratio.py` implements
  a float-free exact scorer using descending-path compression and Karp's
  maximum-cycle-mean dynamic program. Direct simple-cycle enumeration is not
  used in production and exists only as an independent small-test oracle.
- **LIMITATION:** the exact `n=9` classification and exact `n=10` value are
  not a closed-form all-\(n\) evaluation or evidence for convergence to a
  new asymptotic constant. Label `3` is now classified only relative to the
  two `n=10` seven-label equality cycles; label `2` remains unplaced, and the
  `n=10` core minimizers remain unclassified. No interval backend, verifier,
  interval-certificate artifact, checked artifact, schema, or example is
  changed by this work.

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
By itself this is a reduction from complete to core orders, not a closed-form
evaluation or a general classification of the minimizing core orders. The
separate finite `n=9` classification below uses additional equality and
shortcut-gain arguments.

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

The equality case is equally rigid. In the nonexceptional branch,
simultaneously having both displayed scores at most 239 would force equality
in (L9-3) and correction \(4\) in (L9-2). Equality in the duplicated-multiset
pairing bound would require the five edge pairs

\[
(5,9),(5,9),(6,8),(6,8),(7,7).
\tag{L9-4a}
\]

The loop \((7,7)\) cannot be an edge of a cyclic order on five distinct
labels, so in that branch \(P_\omega(S_5)\ge236\) and
\(P_\omega(S_6)\ge240\). The exceptional pair \(\{8,9\}\) is excluded by
the lower value 242 already displayed in the table. For \(\{7,9\}\), the
correction is \(1\), so both scores are at most 239 only when
\(P_\omega(S_5)\le238\). The table has exactly one such row: `586`, with
value 238. Reinserting label \(4\) between \(7\) and \(9\) gives, up to
rotation and reflection, the unique equality cycle

\[
\Omega=(9,5,8,6,7,4),
\qquad
P_\Omega(S_6)=239,
\qquad
P_\Omega(S_5)=238.
\tag{L9-4b}
\]

Consequently,

\[
\max\{P_\omega(S_6),P_\omega(S_5)\}=239
\quad\Longleftrightarrow\quad
\omega\sim_{\rm dihedral}\Omega.
\tag{L9-4c}
\]

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
claim, or any conclusion about exact angular minimizers.

#### Complete core classification at \(n=9\)

It remains to insert labels \(3\) and \(2\) into the forced six-label cycle
\(\Omega\). Fix the displayed orientation in (L9-4b) and name its gaps

\[
\begin{array}{lll}
h_0:9\to5,&h_1:5\to8,&h_2:8\to6,\\
h_3:6\to7,&h_4:7\to4,&h_5:4\to9.
\end{array}
\tag{L9-13}
\]

Insert label \(3\) into one gap and call the resulting seven-cycle \(C_h\).
The six complete sums are direct one-edge replacement calculations:

| Gap containing `3` | \(C_h\) | \(P(C_h)\) | Status if \(K\le239\) |
|---|---|---:|---|
| \(h_0\) | `(9,3,5,8,6,7,4)` | 236 | possible |
| \(h_1\) | `(9,5,3,8,6,7,4)` | 238 | possible |
| \(h_2\) | `(9,5,8,3,6,7,4)` | 233 | possible |
| \(h_3\) | `(9,5,8,6,3,7,4)` | 236 | possible |
| \(h_4\) | `(9,5,8,6,7,3,4)` | 244 | impossible |
| \(h_5\) | `(9,5,8,6,7,4,3)` | 242 | impossible |

Thus label \(3\) cannot lie in either gap incident to label \(4\). For the
other four rows, apply the shortcut definition (L9-7) to \(C_h\). The exact
certificate compresses to

| \(h\) | Full sum | Sole positive nontrivial shortcut | Gain | Largest other nontrivial gain |
|---:|---:|---|---:|---:|
| 0 | 236 | \(9\to5\), deleting `3` | \(+3\) | \(-1\) |
| 1 | 238 | \(5\to8\), deleting `3` | \(+1\) | \(-1\) |
| 2 | 233 | \(8\to6\), deleting `3` | \(+6\) | \(-1\) |
| 3 | 236 | \(6\to7\), deleting `3` | \(+3\) | \(-1\) |

In every row the unique \(-1\) entry is \(7\to9\), deleting label \(4\);
direct evaluation of the remaining oriented arcs gives still smaller integer
gains. Singletons have score at most \(9^2=81\). For subsets of at least two
labels, selected gaps partition the full cycle as in (L9-8). The sole positive
gap cannot occur in a subset that retains label \(3\), because that shortcut
skips \(3\). Therefore every subset retaining \(3\) has score at most the
displayed full sum. Deleting \(3\) through the sole positive shortcut gives
exactly \(\Omega\) and score 239, and equality forces every other selected gap
to be adjacent. Hence each of the four \(C_h\) has \(K=239\), with \(S_6\)
as its unique maximizing subset before label \(2\) is inserted.

Now insert label \(2\) into an arbitrary gap of one of these four cycles.
For a selected subset \(U\) containing \(2\), put \(V=U\setminus\{2\}\).
When \(|V|\ge2\), let \(a,b\) be the two distinct neighbors of label \(2\)
in the order induced on \(U\). Deleting \(2\) gives the exact change

\[
P(U)-P(V)
=2(a+b)-ab
=4-(a-2)(b-2).
\tag{L9-14}
\]

If \(3\notin V\), then \(a,b\ge4\) and the change is at most \(-2\). If
\(3\in V\), its maximum is \(2\), attained only for
\(\{a,b\}=\{3,4\}\); the only other positive case is
\(\{a,b\}=\{3,5\}\), with change \(1\). The rows \(h=0,2,3\) have full
sum at most 236, so even the change \(2\) stays below 239. In the remaining
row \(h=1\), the pair \(\{3,5\}\) gives at most \(238+1=239\). If the
neighbors are \(\{3,4\}\), those labels are not adjacent in \(C_1\), so
making them adjacent in \(V\) forces a nontrivial shortcut. It cannot be the
positive shortcut that deletes the selected label \(3\), or the unique
\(-1\) shortcut that deletes the selected label \(4\). Every remaining gain
is an integer below \(-1\), so \(P(V)\le236\) and \(P(U)\le238\). In the
\(\{3,5\}\) branch, equality \(P(U)=239\) forces \(P(V)=238\). Because
\(V\) retains \(3\), this in turn forces \(V=C_1\) with no nontrivial
shortcut, and label \(2\) must occupy the gap \(5\to3\). The cases
\(|V|\le1\) have score at most \(4\cdot9=36\). Thus label \(2\) may occupy
every gap, and the only new equality is the one just identified.

This gives the promised human-checkable parametrization:

1. orient the forced six-cycle as \(\Omega=(9,5,8,6,7,4)\);
2. insert `3` in one of \(h_0,h_1,h_2,h_3\), the four gaps not incident to
   label `4`;
3. insert `2` immediately after any one of the seven displayed labels of the
   resulting \(C_h\).

Equivalently, after choosing the gap of `3`, label `2` may occupy any of the
other five original gaps, or the same original gap in either internal order.
The count is therefore

\[
4\cdot7=4(5+2)=28.
\tag{L9-15}
\]

These are 28 distinct dihedral classes: after fixing the displayed orientation
of the induced labelled cycle \(\Omega\), a rotation is fixed by label \(9\),
while a reflection reverses that orientation, so no two different placements
in the parametrization are identified. Conversely, (L9-4c) forces every
minimizer into this list, and the preceding bounds admit every listed order.
This proves the **EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION)**

\[
K(\tau)=239
\quad\Longleftrightarrow\quad
\tau\text{ is one of the 28 classes in (L9-15).}
\tag{L9-16}
\]

All 28 classes maximize on \(S_6\). In 27 classes this is the unique
maximizing subset. The sole exception is represented in the chosen orientation
by

\[
(9,5,2,3,8,6,7,4),
\tag{L9-17}
\]

whose canonical reflected representative is
`(9,4,7,6,8,3,2,5)`: both \(S_6\) and the full core
\(\{2,3,4,5,6,7,8,9\}\) have score 239. Indeed, this is the unique equality
case \(238+1\) in the \(h=1\), \(\{3,5\}\)-neighbor branch above.

Finally, (CR12p)--(CR12q) show that inserting label \(1\) into a core gap
preserves the score and introduces no maximizing subset containing \(1\).
For \(n=9\), the eight labelled gaps of each core class give eight distinct
complete dihedral classes. Indeed, a dihedral equivalence between two
insertions would restrict, after deleting label \(1\), to a label-preserving
dihedral automorphism of the same eight-cycle. Its distinct labels force that
automorphism to be the identity, so the two gaps coincide. Deletion of label
\(1\) also prevents insertions from different core classes from merging.
Hence

\[
\#\{\text{complete dihedral minimizers at }n=9\}
=28\cdot8
=224.
\tag{L9-18}
\]

Of these, 216 have \(S_6\) as their sole maximizing subset, while the eight
insertions into (L9-17) retain the two core maximizing subsets. This count is
a consequence of the exact elimination/insertion theorem, not an enlargement
of the public complete-order enumerator.

#### Independent finite oracles

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

A third, classification-level oracle directly generates

\[
(9,\pi_2,\ldots,\pi_8),
\qquad
(\pi_2,\ldots,\pi_8)\in\operatorname{Perm}(2,\ldots,8),
\qquad
\pi_2<\pi_8.
\tag{L9-19}
\]

It therefore covers exactly \(7!/2=2{,}520\) core dihedral classes, without
calling `canonical_core_orders`, any repository canonicalizer, the public
enumerator, or the production Karp scorer. For every row it literally scores
all 255 nonempty subsets and records every maximizing subset: 642,600 exact
integer subset evaluations in total. The deterministic 84,395-byte
serialization of `(order, score, all maximizing subsets)` has SHA-256
`557226668a82f6489274571148572076e373d49baefaa61e6d1f5a458bb857a2`.
It finds minimum 239, exactly the 28 canonical representatives hard-coded in
the test, 27 unique \(S_6\) argmax records, and the single two-argmax record
(L9-17).

These sweeps are **VERIFIED FACTS (FINITE EXHAUSTIVE EXACT COMPUTATION)** and
independently audit the finite proofs; they are not their source. The number
2,520 here is the `n=9` **core** space and only happens to equal the production
ceiling at `n=8`. Production still hard-rejects `n=9`, and no public
enumeration limit changed.

### Reduced exact evaluation at \(n=10\), without public enumeration or core classification

Put
\[
T_7=\{4,5,6,7,8,9,10\},
\qquad
T_6=\{5,6,7,8,9,10\}.
\tag{L10-1}
\]
Let \(\omega\) be a cyclic order on \(T_7\), and let \(a,b\) be the two
neighbors of label \(4\). Deleting \(4\) replaces the two contributions
\(4a+4b\) by \(ab\), so
\[
P_\omega(T_7)
=P_\omega(T_6)+4(a+b)-ab
=P_\omega(T_6)+16-(a-4)(b-4).
\tag{L10-2}
\]

The six edges of the cycle induced on \(T_6\) pair the duplicated multiset
\[
M=(5,5,6,6,7,7,8,8,9,9,10,10).
\tag{L10-3}
\]
The duplicated-multiset rearrangement bound gives
\[
P_\omega(T_6)
\ge2(5\mathbin\cdot10+6\mathbin\cdot9+7\mathbin\cdot8)
=320.
\tag{L10-4}
\]
Because every cyclic sum is an integer, only the pairing levels 320, 321,
and 322 can require work before the target 323 is automatic. The following
small recurrence classifies them without enumerating cyclic orders.

For an even sorted multiset
\(N=(x_1\le\cdots\le x_{2r})\), define
\[
A(N)=\sum_{i=1}^r x_i x_{2r+1-i},
\qquad A(\varnothing)=0.
\tag{L10-5}
\]
The same rearrangement lemma says that \(A(N)\) is a lower bound for every
pairing of \(N\). A state consists of the remaining multiset \(N\), a
partial cost \(s\), and the multiset \(E\) of pairs already chosen. Take
\(x=\min N\), try each distinct possible mate \(y\), and form
\[
N'=N\setminus\{x,y\},
\qquad
s'=s+xy,
\qquad
E'=E\mathbin\uplus\{(x,y)\}.
\tag{L10-6}
\]
Retain the branch exactly when
\[
s'+A(N')\le322,
\tag{L10-7}
\]
identifying states that differ only by exchanging equal copies. Every
pairing of cost at most 322 survives by following the actual mate of the
least remaining entry; conversely, every leaf is a pairing. Thus the
recurrence is exhaustive.

At the first step, the lower totals for pairing the first copy of \(5\) with
\(y=5,6,7,8,9,10\) are respectively
\[
335, 330, 326, 323, 321, 320,
\tag{L10-8}
\]
so only \(y=9,10\) survive. Continuing the same test leaves, after
\(0,1,\ldots,6\) chosen pairs,
\[
1, 2, 3, 6, 6, 10, 8
\tag{L10-9}
\]
distinct states. The eight leaves are listed below; \((i,j)^2\) denotes a
pair with multiplicity two.

| Value | Multiset of six unordered pairs | Simple six-cycle? |
|---:|---|---|
| 320 | \((5,10)^2,(6,9)^2,(7,8)^2\) | no: repeated pairs |
| 321 | \((5,9),(5,10),(6,9),(6,10),(7,8)^2\) | no: \((7,8)\) repeats |
| 321 | \((5,10)^2,(6,8),(6,9),(7,8),(7,9)\) | no: \((5,10)\) repeats |
| 321 | \((5,10)^2,(6,9)^2,(7,7),(8,8)\) | no: loops |
| 322 | \((5,9)^2,(6,10)^2,(7,8)^2\) | no: repeated pairs |
| 322 | \((5,9),(5,10),(6,8),(6,10),(7,8),(7,9)\) | yes |
| 322 | \((5,9),(5,10),(6,9),(6,10),(7,7),(8,8)\) | no: loops |
| 322 | \((5,10)^2,(6,8)^2,(7,9)^2\) | no: repeated pairs |

A simple cycle on six distinct labels has neither a loop nor a repeated
unordered edge. Hence 320 and 321 are impossible, while 322 forces, up to
rotation and reflection,
\[
C_*=(10,5,9,7,8,6),
\tag{L10-10}
\]
with
\[
P_{C_*}(T_6)
=10\mathbin\cdot5+5\mathbin\cdot9+9\mathbin\cdot7
 +7\mathbin\cdot8+8\mathbin\cdot6+6\mathbin\cdot10
=322.
\tag{L10-11}
\]

It remains to insert label \(4\). On the six edges of \(C_*\), the exact
correction \(\delta(a,b)=4(a+b)-ab\) in (L10-2) is

| Edge \(\{a,b\}\) | \(\delta(a,b)\) |
|---|---:|
| \(\{5,10\}\) | 10 |
| \(\{5,9\}\) | 11 |
| \(\{7,9\}\) | 1 |
| \(\{7,8\}\) | 4 |
| \(\{6,8\}\) | 8 |
| \(\{6,10\}\) | 4 |

Every correction is at least one. If \(P_\omega(T_6)\ge323\), the desired
maximum is already at least 323. Otherwise (L10-4) and the complete
classification force \(P_\omega(T_6)=322\) and the induced cycle to be
\(C_*\), so (L10-2) gives \(P_\omega(T_7)\ge323\). This proves the exact
finite lemma
\[
\boxed{
\max\{P_\omega(\{4,\ldots,10\}),
      P_\omega(\{5,\ldots,10\})\}\ge323
}
\tag{L10-12}
\]
for every cyclic order \(\omega\) on \(\{4,\ldots,10\}\). The pairing
recurrence and insertion table are the proof; the finite oracle below is an
independent check, not its source.

For any core order \(\tau\) of \(\{2,\ldots,10\}\), the order induced on
\(T_7\) satisfies (L10-12), and both displayed subsets occur in the
definition of \(K\). Therefore
\[
K(\tau)
\ge\max\{P_\tau(T_7),P_\tau(T_6)\}
\ge323.
\tag{L10-13}
\]

For the reverse inequality, take the supplied core order
\[
\tau_*=(10,2,3,4,7,8,6,9,5).
\tag{L10-14}
\]
Its nine cyclic edge products are
\[
20,6,12,28,56,48,54,45,50,
\]
and hence its complete-core sum is
\[
B=P_{\tau_*}(\{2,\ldots,10\})=319.
\tag{L10-15}
\]
For an oriented arc from \(i\) to \(j\) in \(\tau_*\), define the exact
shortcut gain
\[
g(i,j)
=ij-
\sum_{xy\text{ an edge on the oriented arc from }i\text{ to }j}xy.
\tag{L10-16}
\]
Adjacent endpoints have gain zero. The following table records every
nontrivial gain; \(r\) is the number of skipped internal labels, and each
entry has the form `endpoint:gain`.

| Start | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) | \(r=5\) | \(r=6\) | \(r=7\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | `3:+4` | `4:+2` | `7:+4` | `8:-42` | `6:-110` | `9:-134` | `5:-219` |
| 2 | `4:-10` | `7:-32` | `8:-86` | `6:-138` | `9:-186` | `5:-239` | `10:-279` |
| 3 | `7:-19` | `8:-72` | `6:-126` | `9:-171` | `5:-228` | `10:-263` | `2:-307` |
| 4 | `8:-52` | `6:-108` | `9:-150` | `5:-211` | `10:-241` | `2:-293` | `3:-295` |
| 7 | `6:-62` | `9:-95` | `5:-168` | `10:-183` | `2:-259` | `3:-258` | `4:-263` |
| 8 | `9:-30` | `5:-107` | `10:-117` | `2:-201` | `3:-199` | `4:-203` | `7:-207` |
| 6 | `5:-69` | `10:-89` | `2:-157` | `3:-157` | `4:-163` | `7:-173` | `8:-223` |
| 9 | `10:-5` | `2:-97` | `3:-94` | `4:-97` | `7:-98` | `8:-145` | `6:-211` |
| 5 | `2:-60` | `3:-61` | `4:-68` | `7:-81` | `8:-132` | `6:-190` | `9:-229` |

Every entry is an integer subtraction from the displayed edge products.
Complementary arcs give the additional audit identity
\[
g(i,j)+g(j,i)=2ij-B=2ij-319.
\tag{L10-17}
\]

Let \(U\) be an induced subset with \(|U|\ge2\). The oriented arcs from
each selected label to the next selected label partition the nine edges of
the complete core cycle. Consequently,
\[
P_{\tau_*}(U)-319
=\sum_{(i,j)\text{ a selected gap}}g(i,j).
\tag{L10-18}
\]
For \(|U|=2\), the two complementary arcs supply both occurrences of the
same unordered product, as required by the two-element convention.

The only positive nontrivial gains are
\[
g(10,3)=4,
\qquad
g(10,4)=2,
\qquad
g(10,7)=4.
\tag{L10-19}
\]
All three leave label \(10\), and exactly one selected gap can leave a given
selected label. Thus the sum in (L10-18) is at most four. There is no
nontrivial zero gain, so equality requires either the shortcut \(10\to3\)
or \(10\to7\), with every other selected gap adjacent. These two cases give
exactly
\[
U_8=\{3,4,5,6,7,8,9,10\},
\qquad
U_6=\{5,6,7,8,9,10\}.
\tag{L10-20}
\]
Their sums are, respectively,
\[
10\mathbin\cdot3+3\mathbin\cdot4+4\mathbin\cdot7
+7\mathbin\cdot8+8\mathbin\cdot6+6\mathbin\cdot9
+9\mathbin\cdot5+5\mathbin\cdot10
=323
\tag{L10-21}
\]
and
\[
10\mathbin\cdot7+7\mathbin\cdot8+8\mathbin\cdot6
+6\mathbin\cdot9+9\mathbin\cdot5+5\mathbin\cdot10
=323.
\tag{L10-22}
\]
Singleton scores are at most \(10^2=100\). Therefore the shortcut table is
an exact certificate that
\[
K(10,2,3,4,7,8,6,9,5)=323,
\tag{L10-23}
\]
with precisely \(U_6\) and \(U_8\) as its maximizing subsets.

Combining (L10-13), (L10-23), and the accepted reduction (CR28a) proves
\[
\boxed{\Lambda_{10}=323.}
\tag{L10-24}
\]
This is a **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT)**. It does not
give an exact value of \(R_2^*(10)\), change the production scorer, enlarge
the public enumeration domain, classify the `n=10` core minimizers, or imply
a geometric, all-\(n\), or asymptotic statement.

#### Structural equality classification for the seven-label lemma

The equality cases of (L10-12) can be classified without enumerating cyclic
orders. Write
\[
s=P_\omega(T_6),
\qquad
q=P_\omega(T_7),
\qquad
q=s+\delta(a,b),
\tag{L10-25}
\]
where \(\{a,b\}\) is the edge of the induced tail cycle split by label \(4\)
and
\[
\delta(a,b)=4(a+b)-ab=16-(a-4)(b-4).
\tag{L10-26}
\]
Suppose \(\max\{q,s\}=323\). Then \(s\le323\). The pairing lower bound
(L10-4) and the complete 320--322 signature table show that a simple tail
cycle cannot have score 320 or 321. Hence only the two branches
\[
s=322
\qquad\hbox{or}\qquad
s=323
\tag{L10-27}
\]
remain.

In the branch \(s=322\), the same table forces the unique dihedral tail class
\[
C_*=(10,5,9,7,8,6).
\tag{L10-28}
\]
All six corrections were computed in the insertion table above. Since
\[
\max\{322,322+\delta(a,b)\}=323
\quad\Longleftrightarrow\quad
\delta(a,b)=1,
\tag{L10-29}
\]
only the edge \(\{7,9\}\) survives. Inserting label \(4\) there gives
\[
\omega_{322}=(10,5,9,4,7,8,6),
\qquad
(q,s)=(323,322).
\tag{L10-30}
\]

It remains to treat the genuinely different branch \(s=323\). Here equality
requires \(q\le323\), or equivalently \(\delta(a,b)\le0\). For completeness,
the correction on every one of the 15 possible unordered pairs of distinct
tail labels is

| \(a\backslash b\) | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|
| 5 | 14 | 13 | 12 | 11 | 10 |
| 6 | -- | 10 | 8 | 6 | 4 |
| 7 | -- | -- | 4 | 1 | -2 |
| 8 | -- | -- | -- | -4 | -8 |
| 9 | -- | -- | -- | -- | -14 |

Thus exactly four candidate edges have nonpositive correction:
\[
\{7,10\},\quad \{8,9\},\quad \{8,10\},\quad \{9,10\}.
\tag{L10-31}
\]
Fix one such edge \(e=\{a,b\}\). The other five edges pair the residual
multiset \(N_e=M\setminus\{a,b\}\), with one copy of each endpoint removed.
The rearrangement bound therefore sharpens to
\[
s\ge ab+A(N_e).
\tag{L10-32}
\]
The four exact residual calculations are:

| Fixed edge \(e\) | \(A(N_e)\) | \(ab+A(N_e)\) | Anti-sorted residual signature |
|---|---:|---:|---|
| \(\{7,10\}\) | 253 | 323 | \((5,9),(5,10),(6,8),(6,9),(7,8)\) |
| \(\{8,9\}\) | 251 | 323 | \((5,10)^2,(6,8),(6,9),(7,7)\) |
| \(\{8,10\}\) | 246 | 326 | \((5,9),(5,10),(6,8),(6,9),(7,7)\) |
| \(\{9,10\}\) | 240 | 330 | \((5,9),(5,10),(6,8)^2,(7,7)\) |

The last two edges are impossible because their fixed-edge lower bounds
already exceed 323. For each of the first two, apply the exact least-entry
recurrence (L10-6)--(L10-7) to \(N_e\), with residual cutoff \(A(N_e)\).
At depths zero through five its surviving-state counts are, respectively,
\[
(1,2,1,2,1,1)
\qquad\hbox{and}\qquad
(1,1,1,2,1,1),
\tag{L10-33}
\]
and in each case the displayed anti-sorted residual signature is the unique
leaf. This is the same exhaustive pairing recurrence used for the 320--322
classification, now restricted by the candidate insertion edge; no cyclic-
order enumeration enters the argument.

Adding back \(\{8,9\}\) to its unique residual signature produces both the
loop \((7,7)\) and the repeated edge \((5,10)^2\), so it cannot be a simple
tail cycle. Adding back \(\{7,10\}\), on the other hand, gives the simple
cycle
\[
D_*=(10,5,9,6,8,7).
\tag{L10-34}
\]
Its six exact corrections are

| Edge \(\{a,b\}\) | \(\delta(a,b)\) |
|---|---:|
| \(\{5,10\}\) | 10 |
| \(\{5,9\}\) | 11 |
| \(\{6,9\}\) | 6 |
| \(\{6,8\}\) | 8 |
| \(\{7,8\}\) | 4 |
| \(\{7,10\}\) | -2 |

Thus its only admissible insertion gap is the already fixed edge
\(\{7,10\}\). Inserting label \(4\) there gives
\((10,5,9,6,8,7,4)\); reflecting while fixing label \(10\) gives the chosen
representative
\[
\omega_{323}=(10,4,7,8,6,9,5),
\qquad
(q,s)=(321,323).
\tag{L10-35}
\]

Conversely, the literal scores in (L10-30) and (L10-35) show that both
classes attain equality. Their tail scores differ, so the classes are
distinct. We have therefore proved the exact finite structural theorem
\[
\boxed{
\max\{P_\omega(T_7),P_\omega(T_6)\}=323
\quad\Longleftrightarrow\quad
\omega\sim_{\rm dihedral}(10,4,7,8,6,9,5)
\qquad\hbox{or}\qquad
\omega\sim_{\rm dihedral}(10,5,9,4,7,8,6).
}
\tag{L10-36}
\]
The theorem (L10-36) by itself classifies equality in the seven-label lemma
only. It places neither label \(2\) nor label \(3\), and it does not classify
the minimizing `n=10` core orders.

#### Exact label-three insertion gaps over the equality cycles

The next partial step can be classified without placing label \(2\). Set
\[
T_8=\{3,\ldots,10\},
\qquad
K_{\ge3}(\nu)
=\max_{\varnothing\ne U\subseteq T_8}P_\nu(U)
\tag{L10-37}
\]
for a cyclic order \(\nu\) on \(T_8\). This is deliberately distinct from
the full-core score \(K\), whose domain also contains label \(2\). If a later
full-core order \(\tau\) induces \(\nu\) after deleting label \(2\), then
\[
K(\tau)\ge K_{\ge3}(\nu).
\tag{L10-38}
\]
Thus a value above 323 is a definitive obstruction, whereas a value equal to
323 only leaves the gap available for a later label-two analysis.

Write
\[
\omega_A=(10,4,7,8,6,9,5),
\qquad
\omega_B=(10,5,9,4,7,8,6).
\tag{L10-39}
\]
Their complete seven-label sums are 321 and 323, respectively. For an edge
\(h=\{a,b\}\) of one of these displayed cycles, let \(\iota_h(\omega)\)
insert label \(3\) between its endpoints in the displayed orientation. The
full eight-label sum changes by the exact one-edge replacement
\[
\begin{aligned}
B_h
&=P_{\iota_h(\omega)}(T_8)
=P_\omega(T_7)+\Delta_3(a,b),\\
\Delta_3(a,b)
&=3(a+b)-ab
=9-(a-3)(b-3).
\end{aligned}
\tag{L10-40}
\]

It remains to control all proper induced subsets. Use the shortcut gain from
(L10-16), now computed in the inserted eight-cycle. For \(|U|\ge2\), the
same partition of the full cycle into selected gaps gives
\[
P_{\iota_h(\omega)}(U)-B_h
=\sum_{(i,j)\text{ a selected gap}}g_{\iota_h(\omega)}(i,j).
\tag{L10-41}
\]
There is a compact exact audit of every gain that can be nonnegative. For old
endpoints \(i,j\), splitting \(h\) changes the forward-arc sum only when that
arc contains \(h\), so
\[
g_{\iota_h(\omega)}(i,j)
=
\begin{cases}
g_\omega(i,j)-\Delta_3(a,b),&
   \text{if the forward arc from \(i\) to \(j\) contains \(h\)},\\
g_\omega(i,j),&\text{otherwise}.
\end{cases}
\tag{L10-42}
\]
The new shortcut that deletes only label \(3\) has gain
\(-\Delta_3(a,b)\). Every nontrivial shortcut having label \(3\) as an
endpoint is strictly negative: its arc contains a product \(3x\ge12\) and
an old--old product \(yz\ge20\), while its endpoint product is at most 30.

For \(\omega_A\), the edge products are
\[
40,28,56,48,54,45,50,
\tag{L10-43}
\]
and its one-internal-label shortcut gains, in the displayed starting-label
order, are
\[
2,-52,-62,-30,-69,-5,-70.
\tag{L10-44}
\]
The only two requiring separate attention are
\(g_A(10,7)=2\) on \(10\to4\to7\) and
\(g_A(9,10)=-5\) on \(9\to5\to10\). Every longer base arc uses at least
three edges and hence has gain at most
\[
90-(28+40+45)=-23.
\tag{L10-45}
\]
Since \(-\Delta_3(a,b)\le12\) in all 14 rows, (L10-42) keeps these longer
gains and every other one-internal gain strictly negative. The gain
\(g_A(10,7)\) becomes zero for \(h=\{4,10\}\), becomes \(-3\) for
\(h=\{4,7\}\), and otherwise remains 2. The gain \(g_A(9,10)\) becomes
\(-2\) for \(h=\{5,9\}\), becomes zero for \(h=\{5,10\}\), and
otherwise remains \(-5\).

For \(\omega_B\), the edge products and one-internal-label gains are
\[
50,45,36,28,56,48,60
\tag{L10-46}
\]
and
\[
-5,-61,-1,-52,-62,-28,-80.
\tag{L10-47}
\]
Here the only relevant gains are \(g_B(10,9)=-5\) on
\(10\to5\to9\) and \(g_B(9,7)=-1\) on \(9\to4\to7\). Every longer
base arc has gain at most
\[
90-(28+36+45)=-19,
\tag{L10-48}
\]
so it remains negative after (L10-42), as do the other one-internal gains.
The gain \(g_B(10,9)\) becomes zero only for \(h=\{5,10\}\); the gain
\(g_B(9,7)\) remains negative in every row.

The following tables are therefore complete shortcut-gain certificates.
In a bracket after a gain, the listed labels are exactly those skipped by
that shortcut. A dash means that there is no nontrivial gain of the indicated
sign. The argmax column records every maximizing label subset.

| Cycle | Gap \(h\) | \(\Delta_3\) | \(B_h\) | Positive nontrivial gains | Zero nontrivial gains | \(K_{\ge3}\) | Argmax subsets |
|---|---|---:|---:|---|---|---:|---|
| \(\omega_A\) | \(\{4,10\}\) | 2 | 323 | -- | \(10\to7:0\ [3,4]\) | 323 | \(T_6,T_8\) |
| \(\omega_A\) | \(\{4,7\}\) | 5 | 326 | -- | -- | 326 | \(T_8\) |
| \(\omega_A\) | \(\{7,8\}\) | -11 | 310 | \(10\to7:+2\ [4]\); \(7\to8:+11\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{6,8\}\) | -6 | 315 | \(10\to7:+2\ [4]\); \(8\to6:+6\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{6,9\}\) | -9 | 312 | \(10\to7:+2\ [4]\); \(6\to9:+9\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{5,9\}\) | -3 | 318 | \(10\to7:+2\ [4]\); \(9\to5:+3\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{5,10\}\) | -5 | 316 | \(10\to7:+2\ [4]\); \(5\to10:+5\ [3]\) | \(9\to10:0\ [5,3]\) | 323 | \(T_6\) |
| \(\omega_B\) | \(\{5,10\}\) | -5 | 318 | \(10\to5:+5\ [3]\) | \(10\to9:0\ [3,5]\) | 323 | \(T_7\) |
| \(\omega_B\) | \(\{5,9\}\) | -3 | 320 | \(5\to9:+3\ [3]\) | -- | 323 | \(T_7\) |
| \(\omega_B\) | \(\{4,9\}\) | 3 | 326 | -- | -- | 326 | \(T_8\) |
| \(\omega_B\) | \(\{4,7\}\) | 5 | 328 | -- | -- | 328 | \(T_8\) |
| \(\omega_B\) | \(\{7,8\}\) | -11 | 312 | \(7\to8:+11\ [3]\) | -- | 323 | \(T_7\) |
| \(\omega_B\) | \(\{6,8\}\) | -6 | 317 | \(8\to6:+6\ [3]\) | -- | 323 | \(T_7\) |
| \(\omega_B\) | \(\{6,10\}\) | -12 | 311 | \(6\to10:+12\ [3]\) | -- | 323 | \(T_7\) |

Indeed, (L10-41) bounds every score with at least two labels by \(B_h\) plus
the sum of all positive gains in its row. The displayed lower witnesses attain
that bound, and singletons score at most \(10^2=100\). The argmax list is
also exact. In the first row, either every selected gap is adjacent, giving
\(T_8\), or the sole zero shortcut is used, giving \(T_6\). In each of the
other admissible \(\omega_A\) rows, equality requires both positive shortcuts
and gives \(T_6\); in the \(\{5,10\}\) row its zero shortcut cannot coexist
with the positive \(5\to10\) shortcut because both enter label 10. In every
admissible \(\omega_B\) row, equality requires the shortcut deleting label
3 and gives \(T_7\); in its \(\{5,10\}\) row the zero and positive
shortcuts cannot coexist because both leave label 10. With no nontrivial
nonnegative gain, each excluded row is uniquely maximized by \(T_8\).

Consequently the exact partial classification is
\[
\boxed{
K_{\ge3}(\iota_h(\omega_A))
=
\begin{cases}
326,&h=\{4,7\},\\
323,&\text{for every other edge of \(\omega_A\)},
\end{cases}
}
\tag{L10-49}
\]
and
\[
\boxed{
K_{\ge3}(\iota_h(\omega_B))
=
\begin{cases}
326,&h=\{4,9\},\\
328,&h=\{4,7\},\\
323,&\text{for every other edge of \(\omega_B\)}.
\end{cases}
}
\tag{L10-50}
\]
Thus exactly \(\{4,7\}\) is excluded in the first equality cycle, while
exactly \(\{4,9\}\) and \(\{4,7\}\) are excluded in the second. This is
an **EXACT THEOREM (FINITE LABEL-THREE INSERTION-GAP CLASSIFICATION)**. It
makes no placement claim for label \(2\) and is not a classification or count
of the full `n=10` core minimizers.

#### Independent finite oracles for \(n=10\)

The independent test-only lemma oracle fixes label \(10\) to remove
rotations, directly permutes labels \(4,\ldots,9\), and retains the
orientation whose second label is smaller than its last. It therefore checks
exactly \(6!/2=360\) dihedral classes. Literal cyclic sums give minimum 323
and exactly two equality rows:

| Canonical test-local order | \(P(T_7)\) | \(P(T_6)\) |
|---|---:|---:|
| `(10,4,7,8,6,9,5)` | 321 | 323 |
| `(10,5,9,4,7,8,6)` | 323 | 322 |

This exhaustive **computational** equality list agrees with the structural
theorem (L10-36). It remains an independent test-only oracle and is not the
source of that theorem.

The same test independently enumerates duplicated-label pairing signatures
through 322, recovers exactly the eight rows above, recognizes only the
displayed 322 signature as a simple spanning cycle, and checks the exact
correction and fixed-edge pairing data used in both equality branches.

A separate structural regression constructs all seven label-three insertions
in each equality cycle and directly audits all 48 nontrivial oriented
shortcuts of each inserted order. It reproduces the complete nonnegative-gain
columns in the table above and the exact bound obtained from (L10-41). This
checks the certificate data but is not the source of (L10-49)--(L10-50).

An independent literal subset oracle then treats the two equality cycles as
fixed test-local tuples, splices label \(3\) into each of their seven labelled
gaps, and scores all \(2^8-1=255\) nonempty induced subsets of every resulting
order. It performs exactly
\[
14\cdot255=3{,}570
\tag{L10-51}
\]
integer subset evaluations, without using the insertion formula, shortcut
gains, a repository canonicalizer, the public enumerator, or the production
scorer. It independently returns the score rows
\[
\begin{aligned}
\omega_A:&\quad(323,326,323,323,323,323,323),\\
\omega_B:&\quad(323,323,326,328,323,323,323),
\end{aligned}
\tag{L10-52}
\]
in the gap order of the certificate table. It also recovers every displayed
argmax: \(T_6,T_8\) in the first \(\omega_A\) row; only \(T_8\) in each
excluded row; only \(T_6\) in the other five admissible \(\omega_A\) rows;
and only \(T_7\) in all five admissible \(\omega_B\) rows.

A separate literal computation scores all \(2^9-1=511\) nonempty subsets
of \(\tau_*\). It records every maximizing subset and supplies the following
per-cardinality audit; each row has a unique maximizer.

| \(|U|\) | Maximum | Unique maximizing subset |
|---:|---:|---|
| 1 | 100 | \(\{10\}\) |
| 2 | 180 | \(\{9,10\}\) |
| 3 | 242 | \(\{8,9,10\}\) |
| 4 | 288 | \(\{7,8,9,10\}\) |
| 5 | 318 | \(\{6,7,8,9,10\}\) |
| 6 | 323 | \(\{5,6,7,8,9,10\}\) |
| 7 | 321 | \(\{4,5,6,7,8,9,10\}\) |
| 8 | 323 | \(\{3,4,5,6,7,8,9,10\}\) |
| 9 | 319 | \(\{2,3,4,5,6,7,8,9,10\}\) |

These are **VERIFIED FACTS (FINITE EXHAUSTIVE EXACT COMPUTATION)** and audit
the proof without supplying it. The helpers call no repository canonicalizer,
public enumerator, or production Karp scorer. Production source is unchanged,
and the public complete-order enumeration domain remains `n<=8`.

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
