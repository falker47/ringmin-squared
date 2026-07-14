# Fixed-Order Maximum Cyclic Ratio

Date: 2026-07-14

## Scope And Classification

This note formalizes the exact combinatorial cycle ratio associated with the
complete fixed-order angular STN. It uses the real-arithmetic semantics proved
in `research/FIXED_ORDER_ANGULAR_STN.md` and the two angular comparisons proved
in `research/ALL_N_LOWER_BOUND.md`.

- **DEFINITION:** for a complete cyclic order \(\sigma\) of
  \(\{1,\ldots,n\}\), \(q(C)\) counts `wrap_upper` edge occurrences and
  \(S(C)\) sums endpoint-index products over all directed edge occurrences,
  with multiplicity.
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
- **VERIFIED FACT:** `src/power_ringmin/fixed_order_cycle_ratio.py` implements
  a float-free exact scorer using descending-path compression and Karp's
  maximum-cycle-mean dynamic program. Direct simple-cycle enumeration is not
  used in production and exists only as an independent small-test oracle.
- **LIMITATION:** the finite table is not an all-\(n\) formula or evidence for
  convergence to a new asymptotic constant. No interval backend, verifier,
  certificate, checked artifact, schema, or example is changed by this work.

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
The value is a positive rational number.

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

## 6. Bounded Exact Experiment, \(n=3,\ldots,8\)

The production scorer was minimized over every canonical complete order using
the repository convention: put \(n\) first and retain the reflection with
second label smaller than the last. The direct simple-cycle oracle independently
checked every canonical order through \(n=6\); it was not used to produce the
larger rows.

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
data, not an all-\(n\) theorem or conjecture.

## 7. Comparison With \(W\)

The two symbols describe different combinatorial relaxations.

- \(\Lambda(\sigma)\) uses a **complete** order of
  \(\{1,\ldots,n\}\), sums products around directed STN cycles, and divides
  by the number of `wrap_upper` occurrences. It represents variable angular
  spacings through the difference-constraint cycle criterion.
- The repository's \(W(\tau)\) uses a **core** order of
  \(\{2,\ldots,n\}\), maximizes one pair ratio
  \(ij/d_\tau(i,j)\), and controls a construction on equally spaced regular
  directions.

Thus neither their order domains nor their objectives agree. In particular,
the last two columns of the bounded table are a comparison of separate exact
finite computations, not evidence that
\(\Lambda_n=(n-1)W_n\) or that their minimizers coincide.

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

Deleting label \(1\) still does not make the full \(\Lambda\) score a
function of the induced-core \(W\) score. Exact finite examples at \(n=6\)
are:

- `(6,1,2,4,5,3)` and `(6,3,5,2,1,4)` both have \(\Lambda=77\), while
  their induced-core \(W\) scores are respectively \(20\) and \(24\);
- `(6,1,2,4,5,3)` and `(6,2,5,4,1,3)` both induce \(W=20\), while their
  full scores are respectively \(77\) and \(80\).

These examples disprove identification of the two order scores; they do not
establish a general ordering between the global minima.

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
(CR34) do not imply an all-\(n\) formula; \(8/25\) remains an upper
coefficient, not an exact constant.

Further non-consequences are important.

- The theorem does not assert \(\rho_\sigma=\Lambda(\sigma)/\pi\), equality
  of minimizing order sets, or \(\Lambda_n=(n-1)W_n\).
- A cycle attaining \(\Lambda(\sigma)\) is a witness for the product-angle
  comparison, not necessarily a critical or negative exact-STN cycle at
  \(\rho_\sigma\). For \(n=3\), the two-cycle on labels \(2,3\) attains
  \(\Lambda=12\), but its exact weight
  \(2\pi-2\theta_R(4,9)\) is positive for every \(R>0\).
- The exact real-arithmetic theorem supplies no new interval-backend audit,
  certificate, exact geometric finite optimum value, or checked-artifact
  conclusion.
