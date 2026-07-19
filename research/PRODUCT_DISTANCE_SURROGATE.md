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
- **EXACT THEOREM (adjacent equality cases):** for even \(n=2t\), every
  minimizing cycle has the unique high-high edge \(\{t+1,t+2\}\); for odd
  \(n=2t+1\), it has exactly the two high-high edges
  \(\{t+1,t+2\}\) and \(\{t+1,t+3\}\). In both cases there is no low-low
  edge, and removing the forced high-high edge or segment leaves the
  alternating path characterized below.
- **EXACT THEOREM (distance-two relaxation):** writing
  \(B_n=W_n^{(\le2)}\),
  \[
  B_n=A_n\quad(3\le n\le8),
  \qquad
  B_n>A_n\quad(n\ge9).
  \]
  Hence the adjacent relaxation is strict for the full surrogate for every
  \(n\ge9\), not only for the formerly covered bounded and asymptotic ranges.
- **EXACT THEOREM (quantitative distance-two obstruction):** exact
  threshold tails \(U_T,V_T\) have a compatible split graph with nested
  neighborhoods. Its exact cycle incompatibility is
  \(\eta_n(T)=\max(0,2v-u+\delta_n(T))\), where the skip-one correction
  \(\delta_n(T)\) is zero or one. Exact cyclic gap packing gives a finite
  obstruction \(Q_n\le B_n\). For every \(n\ge9\),
  \[
  B_n\ge Q_n\ge
  {36-16\sqrt2\over49}\left(n+{1\over2}\right)^2,
  \]
  and therefore
  \[
  \liminf_{n\to\infty}{B_n\over n^2}
  \ge {36-16\sqrt2\over49}>{1\over4}.
  \]
  Moreover,
  \[
  Q_n={36-16\sqrt2\over49}n^2+O(n),
  \]
  so the exact nested-neighborhood correction does not improve this
  subproblem's leading coefficient.
- **EXACT THEOREM (terminal-high incidence obstruction):** every order with
  distance-two score at most \(T\) also satisfies
  \(2v\le C_n(T)\), where \(C_n(T)\) counts the lows below \(a_T\) compatible
  at distance one with \(b_T\). Keeping \(Q_n\) unchanged and combining this
  condition with \(\Psi_n(T)\le n-1\) defines a new half-integer obstruction
  \(H_n\le B_n\). It has the exact asymptotic behavior
  \[
  H_n={8\over25}n^2+O(n),
  \qquad
  \lim_{n\to\infty}{H_n\over n^2}={8\over25},
  \]
  and therefore
  \[
  \liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}.
  \]
  By itself this is a lower coefficient for the distance-two surrogate; the
  matching construction below upgrades it to an exact asymptotic coefficient.
- **EXACT THEOREM (matching upper construction):** for every \(n\ge9\), with
  \(d_n=\lceil(4n+8)/5\rceil\) and \(T_n=d_n(d_n-1)/2\), the explicit order
  \(\sigma_n\) constructed below satisfies \(W(\sigma_n)\le T_n\). Hence
  \[
  {B_n\over n^2}\longrightarrow{8\over25},
  \qquad
  {W_n\over n^2}\longrightarrow{8\over25}.
  \]
  For \(n\ge12\), insertion transfers the same order and proves
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{8\over25\pi}.
  \]
  This last statement is the regular-direction upper coefficient, not an
  exact geometric asymptotic constant.
- **EXACT THEOREM (later shortcut evaluation):** for the same canonical core
  order \(\tau_n=\sigma_n\), the induced-subset objective \(K(\tau_n)\) has
  the unique symbolic maximizing backbones stated in (UC24a), the exact
  symbolic formula (K825-4), fourteen exact explicit initial values, and
  \[
  K(\tau_n)={143\over500}n^3+O(n^2).
  \]
  Exact label-one elimination and the fixed-order angular sandwich sharpen
  the current upper coefficients to \(143/500\) for \(\Lambda_n\) and
  \(143/(500\pi)\) geometrically. This does not change the exact \(8/25\)
  product-distance asymptotic.
- **EXACT THEOREM (later residue-one shortcut evaluation):** for
  \(n=5k+1\), \(k\ge2\), the sharper order
  \(\tau_n^{(1)}=\operatorname{residue\_one\_product\_distance\_order}(n)\)
  has the unique induced-subset maximizer \(\{2k+1,\ldots,n\}\). Its exact
  parity quasipolynomial has leading coefficient \(857/3000\), and its
  \(K\) value is strictly below the canonical K825 value on every admitted
  residue-one row. This sharpens only the residue-one subsequential upper
  coefficient for \(\Lambda_n\) and \(R_2^*(n)\); it does not change the
  all-residue limsup bound.
- **EXACT THEOREM (later residue-two shortcut evaluation):** for
  \(n=5k+2\), \(k\ge2\), the parity-aware order
  \(\tau_n^{(2)}=\operatorname{residue\_two\_product\_distance\_order}(n)\)
  has the unique induced-subset maximizer \(\{2k+1,\ldots,n\}\). Its exact
  parity quasipolynomial is strictly below K825 on every residue-two row,
  without crossover. Both have cubic coefficient \(143/500\); their rowwise
  difference is \(21n^2/100+O(n)\), so it sharpens finite and quadratic
  terms but not the established cubic upper coefficient.
- **EXACT THEOREM (residue-class matching):** for \(n\ge9\),
  \[
  H_n=
  \begin{cases}
  d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
  (d_n-1)^2/2,&n\equiv1\pmod5,\\
  (d_n-1)(d_n-2)/2,&n\equiv2\pmod5,\ n\ge17,
  \end{cases}
  \]
  while \(H_{12}=56\). The uniform construction gives
  \(B_n=W_n=T_n\) in residues \(0,3,4\). Separate search-free orders attain
  \((d_n-1)^2/2=H_n\) in residue one and
  \(J_n=d_n(d_n-2)/2\) in residue two. Consequently
  \[
  B_n=W_n=
  \begin{cases}
  d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
  (d_n-1)^2/2,&n\equiv1\pmod5,\\
  d_n(d_n-2)/2,&n\equiv2\pmod5
  \end{cases}
  \qquad(n\ge9),
  \]
  with the residue-one and residue-two branches beginning at \(n=11\) and
  \(n=12\), respectively.
- **EXACT THEOREM (residue-two matching):** the saturation obstruction gives
  \(J_n\le B_n\le W_n\) at \(n=12\) and throughout residue two from
  \(n=17\). A parity-aware symbolic order \(\sigma_n^{(2)}\), valid for every
  \(n=5k+2\), \(k\ge2\), is a permutation and has
  \(W(\sigma_n^{(2)})=J_n\). Its proof checks adjacency, distances two and
  three, the closing cut, and all distances at least four separately. Hence
  \(B_n=W_n=J_n\) on the stated domain. The finite \(n=7\) row remains
  covered only by the bounded table.
- **VERIFIED FACT (finite exhaustive exact computation):** the table below
  gives the objectives truncated at positional distances at most one and two,
  as well as \(W_n\), for \(3\le n\le11\). Non-adjacent constraints first
  change the optimum at \(n=9\), while distance-two constraints already
  recover \(W_n\) throughout this bounded range. This computation is not by
  itself an all-\(n\) theorem, a geometric certificate, or a claim of exact
  geometric optimality.
- **EXACT THEOREM (global distance-two saturation):** combining that exact
  table with the residue-class theorem for every \(n\ge9\) gives
  \[
  W_n^{(\le2)}=B_n=W_n\qquad(n\ge3).
  \]
  Thus positional distances at least three never change the optimum value.
- **EXACT THEOREM (first minimizer restriction):** the distance-two and full
  minimizer sets coincide for \(3\le n\le92\). At \(n=93\), relocating label
  `54` in `eight_twenty_fifths_order(93)` from between `4` and `3` to
  between `16` and `48` gives a distance-two minimizer with truncated score
  \(2850\) but full score \(2852\), attained by \((92,93)\) at distance
  three. Hence
  \(93\) is the first index at which distances at least three restrict the
  minimizer set. This uses no canonical enumeration beyond \(n=11\) and has no
  geometric consequence.
- **EXACT THEOREM (arbitrary compatible scaffold bijections):** on the
  symbolic \(n=10m+3\), \(m\ge3\), branch, every whole-path bijection
  satisfies
  \[
  W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha).
  \]
  The complete distance-three classification gives the sharp class bound
  \[
  W^{(=3)}(\sigma_\alpha)\le{n(5m+2)\over3}<T,
  \]
  while every distance at least four is also strictly below \(T\), and the
  internal edge of \(P_0\) equals \(T\). Consequently relation-compatibility
  is equivalent to \(W(\sigma_\alpha)=T=W_n\). Thus (PG49) is exactly the
  edge support of full-optimal scaffold bijections, not merely of locally
  feasible matchings.
- **EXACT THEOREM (Ferrers count of full-optimal scaffold bijections):** put
  \(d=8m+4\) and
  \(\kappa_j=\lceil j(d-1)/(2(d+j))\rceil\). The exact labelled count is
  \[
  \#\{\alpha:W(\sigma_\alpha)=T=W_n\}
  =\prod_{j=1}^{2m-1}(j+1-\kappa_j).
  \]
  This is the permanent of the reduced PG49 Ferrers board, obtained by a
  one-step nested-neighborhood recurrence rather than permutation
  enumeration. Distinct assignments give distinct canonical dihedral core
  orders in this fixed oriented scaffold, so the same integer also counts
  its dihedral classes; no symmetry factor is divided out.
- **EXACT THEOREM (descending-min PG49 representative):** fixing
  \(\alpha_{\min}(0)=0\) and assigning the least unused
  \(k\ge\kappa_j\) while \(j=2m-1,\ldots,1\) is always well defined.
  Its used suffix is the exact interval
  \([\kappa_j,\kappa_j+2m-1-j]\), so it is a relation-compatible
  bijection for every \(m\ge3\), with the closed binary-jump formula
  (PG104). Its separate induced-subset evaluation is (KPGMIN-9) in
  `research/FIXED_ORDER_CYCLE_RATIO.md`; no geometric conclusion is inferred
  from either theorem.
- **EXACT THEOREM (explicit PG49-star representative):** on the same
  \(n=10m+3\), \(m\ge3\), scaffold, put
  \(q=\lfloor(4m+3)/5\rfloor\) and use the piecewise bijection (PG110).
  Its image intervals partition all path indices, every positive-column
  value satisfies its exact Ferrers threshold, and the closing value is
  \(q=\kappa_{2m-1}\). Hence it is relation-compatible for every admitted
  row. Its separate exact induced-\(K\) theorem is (KPGSTAR-3)--(KPGSTAR-28)
  in `research/FIXED_ORDER_CYCLE_RATIO.md`; neither result has a geometric
  or global-optimality consequence.
- **EXACT THEOREM (later monotone threshold-closing shortcut evaluation):**
  specialize (PG46) to \((q,2m-1)\), where
  \(q=\lfloor(4m+3)/5\rfloor=\kappa_{2m-1}\). This puts \(P_q\) in the
  closing gap and keeps every other path increasing. The separate theorem
  (KPG46Q-1)--(KPG46Q-29) in `research/FIXED_ORDER_CYCLE_RATIO.md` proves
  that \(\{4m+1,\ldots,10m+3\}\) is the sole induced-subset maximizer and
  gives its exact five-branch score. The order has coefficient \(143/500\),
  and its exact excess over PG49-star is \(m(m-1)(m-2)/3\); hence the
  singleton reversal accounts for the complete cubic PG49-star gain. This
  is a fixed-core-order comparison only.
- **EXACT THEOREM (later closing-PG46 shortcut evaluation):** for the PG46
  bijection placing \(P_m\) in the closing gap \(G_{2m-1}\), the corresponding
  core order has the sole induced-subset maximizer

  \[
  S_m=\{4m+1,\ldots,10m+3\},
  \]

  and

  \[
  K={572m^3+631m^2+223m+22\over2}.
  \]

  Its exact difference from canonical K825 is \(m^2-6m-4\): it is smaller
  exactly for \(m=3,4,5,6\), larger for every \(m\ge7\), and never tied.
  Both families have cubic coefficient \(143/500\). This is a theorem about
  one explicit core-order family only; it has no geometric or global
  optimality consequence.
- **EXACT THEOREM (later preclosing-PG46 shortcut evaluation):** for the
  other sharp PG46 bijection, placing \(P_m\) in \(G_{2m-2}\), the same tail
  is the sole induced-subset maximizer and
  \[
  K={572m^3+631m^2+235m+22\over2}.
  \]
  This value exceeds the closing PG46 value by \(6m\) and canonical K825 by
  \(m^2-4\), so it is strictly larger than both for every \(m\ge3\). It
  retains cubic coefficient \(143/500\). This is again a fixed-core-order
  theorem with no geometric or global-optimality consequence.
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

We abbreviate

\[
B_n=W_n^{(\le2)}.
\tag{DT1}
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

### Necessary and sufficient equality structure

The internal-edge count contains more information than the value alone. Let
\(e_L\) be the number of low-low edges. Degree counting on both blocks gives

\[
e_H-e_L=|H|-|L|.
\tag{E1}
\]

Suppose first that \(n=2t\). At the optimum
\(T=A_{2t}=(t+1)(t+2)\), the only high-high pair whose product is at most
\(T\) is

\[
\{t+1,t+2\}.
\]

Equation (E1) says \(e_H-e_L=1\). Thus an equality cycle must have
\(e_H=1\), \(e_L=0\), and its unique high-high edge is
\(\{t+1,t+2\}\). Deleting this edge leaves an alternating Hamilton path

\[
t+1,\ \ell_1,\ h_1,\ \ell_2,\ldots,
\ell_{t-1},\ t+2,
\tag{E2}
\]

through

\[
K=\{t+1,\dots,2t\},
\qquad
L=\{2,\dots,t\}.
\]

Conversely, every such path closes with \(\{t+1,t+2\}\) to an equality
cycle exactly when every crossing edge satisfies \(\ell h\le T\). This is a
necessary and sufficient characterization, not merely a property of the
displayed interleave construction.

Now suppose that \(n=2t+1\). At
\(T=A_{2t+1}=(t+1)(t+3)\), the only high-high pairs with product at most
\(T\) are

\[
\{t+1,t+2\},
\qquad
\{t+1,t+3\}.
\]

Here (E1) says \(e_H-e_L=2\). Both allowed edges are therefore forced,
there is no low-low edge, and the cycle contains the segment

\[
t+2,\ t+1,\ t+3.
\]

Deleting its middle vertex \(t+1\) leaves the alternating Hamilton path

\[
t+2,\ \ell_1,\ h_1,\ \ell_2,\ldots,
\ell_{t-1},\ t+3,
\tag{E3}
\]

through

\[
K=\{t+2,\dots,2t+1\},
\qquad
L=\{2,\dots,t\}.
\]

Again the converse holds exactly when every crossing edge has product at most
\(T\). The implementation function `adjacent_equality_structure` checks
these parity-specific structural conditions directly and returns the active
high path together with the two high neighbors of every low.

## Exact Strictness Of The Distance-Two Relaxation

We now decide the equality question for \(B_n\) without extending cyclic-order
enumeration.

### Equality through \(n=8\)

Always \(B_n\ge A_n\). For \(3\le n\le8\), direct exact scoring of the
following `patterns.interleave` witnesses gives the reverse inequality:

| \(n\) | witness | \(W^{(\le1)}\) | \(W^{(\le2)}\) |
|---:|---|---:|---:|
| 3 | `(3, 2)` | \(6\) | \(6\) |
| 4 | `(4, 2, 3)` | \(12\) | \(12\) |
| 5 | `(5, 2, 4, 3)` | \(15\) | \(15\) |
| 6 | `(6, 2, 5, 4, 3)` | \(20\) | \(20\) |
| 7 | `(7, 2, 6, 4, 5, 3)` | \(24\) | \(24\) |
| 8 | `(8, 2, 7, 4, 5, 6, 3)` | \(30\) | \(30\) |

Thus \(B_n=A_n\) throughout this range. This uses explicit witnesses, not
optimal-order enumeration.

### Terminal-high incidence obstruction

Assume \(n\ge9\) and, for contradiction, that a cycle has distance-two
score at most \(T=A_n\). Its adjacent score is at least \(A_n\), hence equals
\(T\), so the equality classification applies. Use the active high path
\(K\) from (E2) or (E3). Every low \(\ell\) lies between two consecutive
active highs \(x,y\). They are at smaller circular positional distance two,
and therefore

\[
\ell x\le T,
\qquad
\ell y\le T,
\qquad
xy\le2T.
\tag{DT2}
\]

Let \(r\) be the least positive integer satisfying

\[
r(r+1)>2T,
\tag{DT3}
\]

and let \(V\) be the terminal block of active highs from \(r\) to the largest
high. For even \(n=2t\ge10\), one has \(r\ge t+3\) and \(V\ne\varnothing\);
for odd \(n=2t+1\ge9\), one has \(r\ge t+4\) and
\(V\ne\varnothing\). Indeed, the products at the claimed lower predecessor
are at most \(2T\), while \((2t)(2t+1)>2T\) in the even case and
\((2t+1)(2t+2)>2T\) in the odd case. In particular, every vertex of \(V\) is
internal in the active high path.

Any two distinct vertices of \(V\) have product at least
\(r(r+1)>2T\), so (DT2) permits at most one \(V\)-neighbor at any low.
Every vertex of \(V\) has two low neighbors. Their \(2|V|\) incidences must
therefore occupy \(2|V|\) distinct lows. But a low incident to \(V\) must
satisfy \(\ell r\le T\). The number of compatible lows is exactly

\[
C=\left\lfloor{T\over r}\right\rfloor-1,
\]

because the preceding lower bounds on \(r\) also give
\(\lfloor T/r\rfloor\le t\) in both parities. Thus the displayed count stays
inside the low domain \(\{2,\dots,t\}\).

Therefore equality at distance two would require

\[
2|V|\le C.
\tag{DT4}
\]

Minimality of \(r\) gives

\[
(r-1)r\le2T<r(r+1).
\tag{DT5}
\]

The strict right inequality implies

\[
\left\lfloor{T\over r}\right\rfloor
\le\left\lfloor{r\over2}\right\rfloor,
\qquad
C\le\left\lfloor{r\over2}\right\rfloor-1.
\tag{DT6}
\]

It remains to compare this capacity with the terminal-block size.

For even \(n=2t\), \(|V|=2t-r+1\). If \(t\ge8\), then
\(5r\le8t+5\). Otherwise, using the left inequality in (DT5),

\[
2T\ge(r-1)r
\ge{(8t+1)(8t+6)\over25}
=2T+{14t^2-94t-94\over25}>2T,
\]

a contradiction; the final polynomial is positive at \(t=8\) and strictly
increasing thereafter. Hence

\[
2|V|=4t-2r+2>{r\over2}-1\ge C.
\tag{DT7}
\]

The remaining nonexceptional even parameters are exact boundary checks:

| \(t\) | \(T\) | \(r\) | \(|V|\) | \(C\) | \(2|V|>C\) |
|---:|---:|---:|---:|---:|---:|
| 5 | 42 | 9 | 2 | 3 | \(4>3\) |
| 7 | 72 | 12 | 3 | 5 | \(6>5\) |

For odd \(n=2t+1\), \(|V|=2t-r+2\). If \(t\ge7\), the analogous bound
is \(5r\le8t+9\). Indeed, the contrary inequality and (DT5) would give

\[
2T\ge(r-1)r
\ge{(8t+5)(8t+10)\over25}
=2T+{14t^2-80t-100\over25}>2T.
\]

The last polynomial is positive at \(t=7\) and strictly increasing. It
follows that

\[
2|V|=4t-2r+4>{r\over2}-1\ge C.
\tag{DT8}
\]

The three smaller odd parameters give:

| \(t\) | \(T\) | \(r\) | \(|V|\) | \(C\) | \(2|V|>C\) |
|---:|---:|---:|---:|---:|---:|
| 4 | 35 | 8 | 2 | 3 | \(4>3\) |
| 5 | 48 | 10 | 2 | 3 | \(4>3\) |
| 6 | 63 | 11 | 3 | 4 | \(6>4\) |

Thus (DT4) is impossible in every odd case and every even case except the
single parameter \(t=6\), namely \(n=12\).

### The exceptional parameter \(n=12\)

Here \(T=56\), the active high path has vertex set
\(K=\{7,8,9,10,11,12\}\), and its endpoints are \(7,8\). Under (DT2), both
neighbors of high \(12\) must lie in

\[
S=\{7,8,9\},
\]

because \(12\cdot10>112=2T\). The low vertex \(6\) also has both high
neighbors in \(S\), because \(6\cdot10>56=T\). Thus the active high path
would contain two \(12\)-to-\(S\) edges and one \(S\)-to-\(S\) edge.

The total degree of \(S\) in this path is

\[
\deg(7)+\deg(8)+\deg(9)=1+1+2=4.
\]

The two edges incident to \(12\) consume two of these degree units, and the
edge belonging to low \(6\) consumes the other two. Vertex \(12\) also has
both of its degrees consumed. Hence \(S\cup\{12\}\) has no path edge to
\(\{10,11\}\), contradicting connectedness of the active Hamilton path.

This handles the only parameter not covered by the incidence inequality.
Consequently no cycle can have distance-two score at most \(A_n\) once
\(n\ge9\). Since the finite order space attains its minimum,

\[
\boxed{
B_n=A_n\quad(3\le n\le8),
\qquad
B_n>A_n\quad(n\ge9).
}
\tag{DT9}
\]

Because \(W_n\ge B_n\), this also proves

\[
W_n>A_n\qquad(n\ge9).
\tag{DT10}
\]

This conclusion is purely combinatorial. By itself it gives neither a formula
for \(B_n,W_n\) nor their later global equality; those require the subsequent
residue-class constructions together with the bounded exact table. It also
does not by itself improve a geometric radius bound for Power-Ringmin.

## Quantitative Two-Threshold Obstruction For \(B_n\)

The preceding strictness theorem compares \(B_n\) with \(A_n\), but gives no
size for the gap. We now prove an independent quantitative obstruction using
only positional distances one and two, and then characterize exactly the
tail-cycle incompatibility that enters it.

### Exact integer thresholds and degenerate tails

Fix \(n\ge3\) and an exact real threshold \(T\ge0\). Define

\[
a_T
=
\min\{k\in\mathbb Z:k\ge2,\ k(k+1)>T\}
=
\max\left\{
2,
1+\left\lfloor{\sqrt{1+4T}-1\over2}\right\rfloor
\right\},
\tag{TT1}
\]

and

\[
b_T
=
\min\{k\in\mathbb Z:k\ge2,\ k(k+1)>2T\}
=
\max\left\{
2,
1+\left\lfloor{\sqrt{1+8T}-1\over2}\right\rfloor
\right\}.
\tag{TT2}
\]

The added one after the floor is essential at equality: if
\(k(k+1)=T\), then the strict inequality in (TT1) starts at \(k+1\), and
similarly for (TT2). Put

\[
U_T=\{a_T,a_T+1,\dots,n\},
\qquad
V_T=\{b_T,b_T+1,\dots,n\},
\tag{TT3}
\]

where either displayed set means its intersection with the core
\(C_n=\{2,\dots,n\}\). Thus

\[
u=|U_T|=\max(0,n-a_T+1),
\qquad
v=|V_T|=\max(0,n-b_T+1).
\tag{TT4}
\]

Because \(2T\ge T\), one has \(b_T\ge a_T\), hence \(V_T\subseteq U_T\)
and \(0\le v\le u\). If \(u\ge2\), the least product of two distinct
elements of \(U_T\) is \(a_T(a_T+1)>T\); if \(v\ge2\), the corresponding
least product in \(V_T\) is \(b_T(b_T+1)>2T\).

The definitions also fix all vacuous cases without silently replacing an
empty threshold tail by a singleton:

- \(a_T\le n-1\) gives \(u=n-a_T+1\ge2\);
- \(a_T=n\) gives the singleton \(U_T=\{n\}\);
- \(a_T\ge n+1\) gives \(U_T=\varnothing\);
- the identical alternatives with \(b_T,v,V_T\) hold at the second
  threshold.

If \(u=0\), then \(v=0\). If \(u=1\), then in fact \(v=0\) for every
\(n\ge3\). Indeed, \(u=1\) means \(a_T=n\), so

\[
(n-1)n\le T<n(n+1).
\]

If also \(v=1\), then \(b_T=n\) and
\((n-1)n\le2T<n(n+1)\). The lower bound on \(T\) would force
\(2n(n-1)<n(n+1)\), or \(n<3\), a contradiction. This verifies the
singleton and empty cases separately from the gap argument below.

### Exact nested-neighborhood cycle theorem

Put \(P=2T\). On \(U_T\), call a distinct pair compatible when its product
is at most \(P\), and define

\[
\eta_n(T)
=
\min_\tau
\#\{i:\tau_i\tau_{i+1}>P\},
\]

where \(\tau\) runs over cyclic orders of \(U_T\). For \(u=0,1\), there is
no distinct-vertex cyclic arc and we define \(\eta_n(T)=0\). For \(u=2\),
the two oriented arcs are counted separately, as they are for the two induced
positional gaps.

Define the exact skip-one indicator

\[
\delta_n(T)
=
\mathbf 1_{\{a_T<b_T\le n-1,\ 2T<b_T^2-1\}}.
\tag{TT5}
\]

The strict inequality is intentional: at \(2T=b_T^2-1\), the pair
\((b_T-1,b_T+1)\) is compatible. The exact answer is

\[
\boxed{
\eta_n(T)
=
\max\bigl(0,2v-u+\delta_n(T)\bigr)
}.
\tag{TT6}
\]

We prove this from the full nested-neighborhood graph, not only from its
terminal incompatible clique. Suppress the subscript on \(a_T,b_T\). Whenever
\(b>2\), and in particular in the split case \(a<b\), minimality of \(b\)
gives

\[
b(b-1)\le P<b(b+1).
\tag{TT7}
\]

When \(a<b\le n\), put

\[
K=\{a,\dots,b-1\},
\qquad
V=\{b,\dots,n\},
\qquad
\ell=|K|=u-v=b-a.
\]

Then \(K\) is a compatible clique, \(V\) is an incompatible independent
set, and for \(y\in V\)

\[
N(y)\cap K
=
\left\{a,\dots,
\min\!\left(b-1,\left\lfloor{P\over y}\right\rfloor\right)
\right\}
\tag{TT8}
\]

when the displayed upper endpoint is at least \(a\), and is empty otherwise.
Thus the cross-neighborhoods are prefixes nested in reverse order as \(y\)
increases. In particular, incidence counting on the independent set \(V\)
gives the earlier clique lower bound

\[
\eta_n(T)\ge\max(0,v-\ell)=\max(0,2v-u).
\tag{TT9}
\]

For matching upper constructions, use the following elementary cyclic-order
fact. On the consecutive normalized labels \(0,\dots,u-1\), suppose every
pair with sum at most \(h\) is compatible. If \(h\ge u\), the alternating
extremes cycle

\[
0,u-1,1,u-2,2,u-3,\dots
\]

has every adjacent sum at most \(u\), including its closing edge. If
\(h\le u-1\), the labels \(0,\dots,h\) have the compatible Hamiltonian path

\[
h,0,h-1,1,h-2,2,\dots,
\]

while \(h+1,\dots,u-1\) may be treated as singleton paths. Closing these
\(u-h\) paths cyclically uses at most \(u-h\) incompatible edges. Therefore
the available sum-threshold subgraph always gives a cycle with at most
\(\max(0,u-h)\) incompatible edges in the cases used below.

If \(P\ge b^2-1\), every distinct pair with sum at most \(2b\) is
compatible: its product is at most \((b-1)(b+1)=b^2-1\). After subtracting
\(a\) from every label, the preceding construction has
\(h=2b-2a=2\ell\), so it uses at most

\[
\max(0,u-2\ell)=\max(0,v-\ell)
\]

incompatible edges. This matches (TT9).

Now suppose \(P<b^2-1\) and \(b\le n-1\). Every distinct pair with sum at
most \(2b-1\) is still compatible, because its product is at most
\(b(b-1)\le P\). The construction with \(h=2\ell-1\) uses at most

\[
\max(0,u-(2\ell-1))
=
\max(0,v-\ell+1)
\]

incompatible edges. This extra one is forced whenever its positive part is
nonzero. Indeed, delete
\(S=\{a,\dots,b-2\}\), of size \(\ell-1\). In the compatible graph minus
\(S\), the pair \(\{b-1,b\}\) is one component and
\(b+1,\dots,n\) are isolated, because

\[
(b-1)b\le P<(b-1)(b+1)<b(b+1).
\]

There are therefore \(v\) components. Deleting \(e\) incompatible cycle
edges and then \(|S|\) vertices leaves at most \(e+|S|\) compatible path
pieces; the disconnected case \(e=|S|=0\) gives the same conclusion
directly. Hence

\[
e\ge v-(\ell-1)=v-\ell+1.
\]

If \(b=n\), then \(v=1\). For \(\ell\ge2\), the same sum-threshold
construction already gives an all-compatible cycle; for \(\ell=1\), the
tail has two vertices and \((b-1)b\le P\), so both oriented arcs are
compatible. If \(b>n\), then \(n(n+1)\le P\), so the whole tail is a
compatible clique. Finally, if \(a=b\), then \(U_T=V_T\) and every distinct
pair is incompatible, giving \(\eta_n(T)=u\). These cases complete the proof
of (TT6).

The two-vertex boundary is worth stating once more. If
\(U_T=\{a,a+1\}\) and \(a(a+1)>2T\), then \(b=a\), \(v=u=2\), and (TT6)
counts both oriented arcs: \(\eta_n(T)=2\). At equality
\(a(a+1)=2T\), both arcs are compatible and \(\eta_n(T)=0\). Together with
the already proved facts \(u=0\Rightarrow v=0\) and
\(u=1\Rightarrow v=0\), this handles cardinalities zero, one, and two
without loops or hidden exceptions.

The clique bound is sometimes strict but misses by at most one:

\[
0\le
\eta_n(T)-\max(0,2v-u)
\le1.
\tag{TT10}
\]

For example, \(n=5,T=6\) gives \(U_T=\{3,4,5\}\),
\(\eta_5(6)=2\), and clique bound one. Conversely, equality holds for
infinite threshold families, including \(2T=b^2-1\), where the correction
turns off exactly at compatibility.

### Exact cyclic gap consequence

Let \(S_2(\sigma)=W^{(\le2)}(\sigma)\). Suppose that a cyclic core order
\(\sigma\) satisfies

\[
S_2(\sigma)\le T
\]

and first assume \(u\ge2\). Filter the oriented \(N=n-1\) position cycle to
\(U_T\), write its induced cyclic word as
\(x_1,\dots,x_u\), and let \(g_i\) be the positive forward positional gap
from \(x_i\) to \(x_{i+1}\), with \(x_{u+1}=x_1\). These induced gaps
partition the full position cycle:

\[
g_i\ge1,
\qquad
\sum_{i=1}^u g_i=N.
\]

Every distinct pair in \(U_T\) has product greater than \(T\). Therefore
\(g_i=1\) would give a distance-one score greater than \(T\), contradicting
(the displayed score assumption). Hence every \(g_i\ge2\). If an adjacency
of the induced \(U_T\)-cycle is incompatible in the graph above, then its
endpoint product exceeds \(2T\). Its induced gap cannot be at most two, so it
is at least three. At least \(\eta_n(T)\) such adjacencies occur by definition.
The two oriented gaps when \(u=2\) are exactly the two arcs counted in
\(\eta_n(T)\). Therefore

\[
n-1\ge2u+\eta_n(T).
\]

Define

\[
\Psi_n(T)
=
2u+\eta_n(T)
=
\max\bigl(2u,u+2v+\delta_n(T)\bigr).
\tag{TT11}
\]

The degenerate cases extend the necessary inequality to every \(u\): for
\(u=0\), both sides contributed by the tails are zero; for \(u=1\), the
result above gives \(v=0\), so \(\Psi_n(T)=2\le n-1\). Therefore

\[
S_2(\sigma)\le T
\quad\Longrightarrow\quad
n-1\ge\Psi_n(T)
\tag{TT12}
\]

for every \(n\ge3\) and every exact \(T\ge0\). Equivalently, the exact
finite condition \(\Psi_n(T)>n-1\) certifies \(B_n>T\).

### Finite exact obstruction

Every distance-at-most-two pair score has denominator one or two. Hence
\(B_n\in\tfrac12\mathbb Z_{\ge0}\). Define

\[
Q_n
=
\min\left\{
{q\over2}:q\in\mathbb Z_{\ge0},\quad
\Psi_n(q/2)\le n-1
\right\}.
\tag{TT13}
\]

This set is nonempty: at \(T=n(n+1)\), one has \(u=v=0\). Moreover the
minimum is a genuinely finite calculation. The first tail changes at
\(T=k(k+1)\), the second at \(T=k(k+1)/2\), and the exact correction turns
off at \(T=(k^2-1)/2\). Strictness makes each change occur at the equality
itself. Thus (TT13) is equivalently the minimum over

\[
\widehat E_n
=
\{0\}\cup
\left\{
{k(k+1)\over2},\ k(k+1),\ {k^2-1\over2}:2\le k\le n
\right\}.
\tag{TT14}
\]

Including \(k=n\) makes the event statement literally exhaustive. In the
earlier clique-only function
\(\Phi_n(T)=\max(2u,u+2v)\), the omitted \(b\)-event
\(T=n(n+1)/2\) either coincided with an already included \(a\)-event or
left \(u\) fixed. In the latter case it changed \(v\) from one to zero but
did not change \(\Phi_n\): when \(v=1\), one has \(u\ge2\), so
\(\max(2u,u+2)=2u\). (For example, at \(n=3,T=6\) the simultaneous
\(a\)-event does change \(\Phi_3\), but that threshold was already present as
the \(k=2\) event.) The omitted \(a\)-event \(T=n(n+1)\) changed
\(\Phi_n\) from two to zero, but could not change its minimum admissible
threshold because the included event \(T=n(n-1)\) already had
\(u=1,v=0\) and \(\Phi_n=2\le n-1\). Thus the former values were correct;
the enlarged range removes the expositional gap.

The finite order space attains \(B_n\). Applying (TT12) at \(T=B_n\) shows
that \(B_n\) belongs to the admissible half-integer set in (TT13), so

\[
\boxed{B_n\ge Q_n},
\qquad
\boxed{B_n\ge\max(A_n,Q_n)}.
\tag{TT15}
\]

The implementation functions `two_threshold_tail_packing` and
`tail_cycle_incompatibility_minimum` evaluate (TT1)--(TT6) exactly;
`two_threshold_lower_obstruction` evaluates (TT13)--(TT14) with integers and
`Fraction` only.

### Explicit all-\(n\) lower bound

We next extract a closed bound from the exact obstruction. For \(n\ge9\),
take any adjacent-optimal order. Its adjacent scores are at most \(A_n\),
and every distance-two score is at most \(n(n-1)/2\). Directly from (8),

\[
{n(n-1)\over2}-A_n
=
\begin{cases}
t^2-4t-2,&n=2t,\ t\ge5,\\
t^2-3t-3,&n=2t+1,\ t\ge4,
\end{cases}
\]

which is positive in both domains. Therefore

\[
Q_n\le B_n\le {n(n-1)\over2}
\qquad(n\ge9).
\]

Put \(T=Q_n\), \(a=a_T\), and \(b=b_T\). The displayed upper bound
\(Q_n\le n(n-1)/2\) gives
\(a\le n-1\) and \(b\le n\), so \(u=n-a+1\ge2\) and
\(v=n-b+1\ge1\). Since \(\Psi_n(Q_n)\le n-1\), (TT11) yields both
\(2u\le n-1\) and \(u+2v\le n-1\). In particular,

\[
a\ge{n+3\over2}>2,
\qquad
a+2b\ge2n+4.
\]

Minimality in (TT1)--(TT2), now with valid predecessors at least two, gives

\[
(a-1)a\le Q_n,
\qquad
(b-1)b\le2Q_n.
\]

Hence \(a\le1+\sqrt{Q_n}\) and
\(b\le1+\sqrt{2Q_n}\). Combining these estimates with the preceding
inequality for \(a+2b\),

\[
2n+4
\le a+2b
\le3+(1+2\sqrt2)\sqrt{Q_n}.
\]

It follows that

\[
\boxed{
B_n\ge Q_n
\ge
\left({2n+1\over1+2\sqrt2}\right)^2
=
{36-16\sqrt2\over49}
\left(n+{1\over2}\right)^2
}
\qquad(n\ge9).
\tag{TT16}
\]

This is stronger than the requested form
\(B_n\ge c n^2-O(n)\): with

\[
c={36-16\sqrt2\over49},
\]

(TT16) gives \(B_n\ge c n^2+c n+c/4\). In particular,

\[
\boxed{
\liminf_{n\to\infty}{B_n\over n^2}
\ge {36-16\sqrt2\over49}>{1\over4}
}.
\tag{TT17}
\]

The exact incompatibility does not improve this leading coefficient. Put

\[
\alpha={2\over1+2\sqrt2},
\qquad
\beta=\sqrt2\,\alpha,
\qquad
c=\alpha^2={36-16\sqrt2\over49};
\]

then \(\alpha+2\beta=2\). Define

\[
A=\lceil\alpha n+1\rceil,
\qquad
D=\lceil\beta n+2\rceil,
\qquad
S_n=\max\left(A(A-1),{D(D-1)\over2}\right).
\]

The threshold definitions give \(a_{S_n}\ge A\) and \(b_{S_n}\ge D\).
For \(n\ge45\), \(A\ge(n+4)/2\): the boundary reduces to
\(133>94\sqrt2\), and \(133^2=17689>17672=2\cdot94^2\).
Also \(A+2D\ge(\alpha+2\beta)n+5=2n+5\). Hence

\[
2u\le n-2,
\qquad
u+2v\le n-2.
\]

Since \(\delta_n(S_n)\le1\), (TT11) gives
\(\Psi_n(S_n)\le n-1\), so \(Q_n\le S_n\). Both terms defining \(S_n\)
equal \(cn^2+O(n)\), while (TT16) gives the matching lower estimate.
Consequently

\[
\boxed{
Q_n=cn^2+O(n),
\qquad
\lim_{n\to\infty}{Q_n\over n^2}
=c={36-16\sqrt2\over49}
}.
\]

Equivalently, if \(T\sim t n^2\) near the transition, then
\(a_T/n\to\sqrt t\), \(b_T/n\to\sqrt{2t}\), and

\[
{\Psi_n(T)\over n}
\longrightarrow
\max\left(2-2\sqrt t,
3-(1+2\sqrt2)\sqrt t\right),
\]

whose crossing with one is exactly at \(t=c\). This proves optimality of the
clique coefficient for this tail-cycle subproblem. It does **not** prove that
\(B_n/n^2\) converges or that its actual lower asymptotic coefficient equals
\(c\).

The strict comparison is exact:

\[
{36-16\sqrt2\over49}-{1\over4}
={95-64\sqrt2\over196}>0,
\]

because \(95^2=9025>8192=2\cdot64^2\).

### Relation to the full-distance tail obstruction

The domains of the two lower obstructions must not be conflated:

\[
A_n\le B_n\le W_n,
\qquad
Q_n\le B_n,
\qquad
L_n\le W_n.
\tag{TT18}
\]

The proof of \(L_n\le W_n\) later in this note uses induced gaps of every
possible positional length, so it does not imply \(L_n\le B_n\). Its known
asymptotic constant is slightly larger than the \(Q_n\) tail-cycle constant:

\[
{1\over4}
<
{36-16\sqrt2\over49}
<
{2(\sqrt2-1)\over3}.
\tag{TT19}
\]

For the second strict inequality, the right difference is

\[
{2(\sqrt2-1)\over3}
-{36-16\sqrt2\over49}
={2(73\sqrt2-103)\over147}>0,
\]

because \(2\cdot73^2=10658>10609=103^2\). Thus the two-threshold result
strictly improves the adjacent asymptotic obstruction for \(B_n\), while the
slightly stronger tail coefficient remains a statement about the full
surrogate \(W_n\).

## Terminal-High Compatible-Low Incidence Obstruction

The terminal-high incidence count used in the proof of \(B_n>A_n\) has an
exact threshold form independent of adjacent optimality. Retain the notation
\(a_T,b_T,U_T,V_T,u,v\) from (TT1)--(TT4), and define

\[
C_n(T)
=
\#\{\ell\in\{2,\dots,a_T-1\}:\ell b_T\le T\}.
\tag{TH1}
\]

The subscript records the ambient problem even though the displayed set is
determined by \(T\). If \(v>0\), then \(b_T\le n\) and
\(a_T\le b_T\le n\), so every label counted here belongs to the core. If
\(v=0\), possible labels above the core are irrelevant because the incidence
condition below is vacuous.

### Exact incidence injection and all boundary cases

Suppose first that \(n\ge4\) and a cyclic core order \(\sigma\) satisfies

\[
S_2(\sigma)\le T.
\]

The position cycle has \(N=n-1\ge3\) vertices, so each \(x\in V_T\) has two
distinct cyclic neighbors. Both are outside \(U_T\). Indeed, if a neighbor
\(y\) also belonged to \(U_T\), then \(x,y\) would be distinct integers in
that tail and hence

\[
xy\ge a_T(a_T+1)>T,
\]

contradicting the distance-one requirement \(xy\le T\). Thus every neighbor
is a low label \(\ell\in\{2,\dots,a_T-1\}\). Since \(x\ge b_T\), adjacency
also gives

\[
\ell b_T\le\ell x\le T,
\]

so the low is counted by \(C_n(T)\).

No one low can serve two distinct vertices \(x,y\in V_T\). If it did, the
two-edge walk \(x,\ell,y\) would give \(d_\sigma(x,y)\le2\); for the
three-position cycle the smaller distance is even one. The score bound would
then imply \(xy\le2T\), whereas distinct labels in \(V_T\) satisfy

\[
xy\ge b_T(b_T+1)>2T.
\]

The two incidences of one \(V_T\)-vertex also have different low endpoints
because its two neighbors are distinct. Consequently all \(2v\) incidences
inject into the compatible-low set:

\[
\boxed{2v\le C_n(T)}.
\tag{TH2}
\]

The excluded small and degenerate cases are exact.

- If \(n=3\), the two-position core has the single pair \(2,3\) at distance
  one, so \(S_2(\sigma)=6\). The hypothesis forces \(T\ge6\), whence
  \(3\cdot4\le2T\). Because the definition of \(b_T\) uses a strict
  inequality, \(b_T\ge4>n\), so \(v=0\) and (TH2) is vacuous.
- If \(v=0\), the left side of (TH2) is zero. This includes every empty
  \(V_T\), whether or not \(U_T\) is empty.
- If \(v=1\) and \(n\ge4\), the unique terminal high has two distinct low
  neighbors, so the proof directly gives two different counted lows. No
  sharing argument between different highs is needed.
- If \(U_T=\varnothing\), then \(V_T=\varnothing\) because
  \(V_T\subseteq U_T\). The earlier singleton result \(u=1\Rightarrow v=0\)
  covers the remaining one-element first tail.

The capacity has an exact floor form. Directly from (TH1),

\[
C_n(T)
=
\max\left(
0,
\min\left(a_T-1,\left\lfloor{T\over b_T}\right\rfloor\right)-1
\right).
\]

The \(a_T-1\) cap is never active. If \(b_T>a_T\), then
\(T<a_T(a_T+1)\le a_Tb_T\). If \(b_T=a_T\), then
\(2T<a_T(a_T+1)\), so \(T/b_T<(a_T+1)/2<a_T\). In both cases
\(\lfloor T/b_T\rfloor\le a_T-1\), and therefore

\[
\boxed{
C_n(T)
=
\max\left(0,\left\lfloor{T\over b_T}\right\rfloor-1\right)
}.
\tag{TH3}
\]

All equality directions are essential. The definitions
\(a_T(a_T+1)>T\) and \(b_T(b_T+1)>2T\) are strict, so equality advances the
corresponding tail start. Compatible-low equality is non-strict:
\(\ell b_T=T\) counts \(\ell\), exactly as the floor in (TH3) requires.

### Joint half-integer obstruction and finite event set

Do not redefine the existing \(\Psi_n\) or \(Q_n\). Introduce instead

\[
H_n
=
\min\left\{
{q\over2}:q\in\mathbb Z_{\ge0},\quad
\Psi_n(q/2)\le n-1,\quad
2v(q/2)\le C_n(q/2)
\right\}.
\tag{TH4}
\]

The set is nonempty. At \(T=n(n-1)\), strictness gives \(a_T=n\), hence
\(u=1\), while \(b_T\ge n+1\), hence \(v=0\). Thus
\(\Psi_n(T)=2\le n-1\) and the incidence condition is vacuous.

Every distance-two objective is a half-integer. Applying (TT12) and (TH2) at
an order attaining \(B_n\) gives

\[
\boxed{B_n\ge H_n\ge Q_n},
\qquad
\boxed{B_n\ge\max(A_n,H_n)}.
\tag{TH5}
\]

The second inequality in the first box follows because the admissible set in
(TH4) is a subset of the unchanged admissible set defining \(Q_n\).

Only one new type of finite event is required. With \(\widehat E_n\) from
(TT14), put

\[
\widehat F_n
=
\widehat E_n
\cup
\left\{{k^2\over2}:4\le k\le n,\ k\text{ even}\right\}.
\tag{TH6}
\]

This set is exhaustive for (TH4). While \(b_T=k>2\), predecessor minimality
gives

\[
{k(k-1)\over2}\le T<{k(k+1)\over2}.
\tag{TH7}
\]

For \(k=2\), the exact interval is instead \(0\le T<3\), because tail starts
are constrained to be at least two; the positive-part capacity in (TH3) is
zero throughout. For \(k=2h+1>2\) odd,
\(\lfloor T/k\rfloor=h\) throughout the half-open interval (TH7), with its
next change already at the upper \(b\)-event. If
\(k=2h\ge4\) is even, the floor changes exactly once inside the interval,
from \(h-1\) to \(h\) at \(T=k^2/2\). At equality the low \(h\) becomes
compatible and must be counted. Once \(k>n\), one has \(v=0\), so further
capacity events are irrelevant. The events in \(\widehat E_n\) already cover
all changes of \(a_T,b_T,\Psi_n\), and \(\delta_n\). Thus the predicate in
(TH4) is constant between consecutive members of \(\widehat F_n\), and
\(H_n\) is equivalently the minimum over that finite set.

Exact evaluation gives

\[
\boxed{
(H_3,\dots,H_{11})
=
(6,12,15,20,21,30,36,45,50)
}.
\tag{TH8}
\]

The value \(H_{11}=50\) occurs at the genuinely new event \(10^2/2\): just
below it the capacity is three, while at equality \(5\cdot10=50\) enters and
the capacity becomes four, matching \(2v=4\).

### Exact asymptotic coefficient

We now determine the coefficient of \(H_n\), rather than assume it. Let \(T\)
be any half-integer admissible in (TH4), and write \(b=b_T\). If \(v=0\),
then \(b\ge n+1\), so \(5b>4n+5\). If \(v>0\), (TH2)--(TH3) give

\[
2v+1
\le
\left\lfloor{T\over b}\right\rfloor
\le {T\over b}
<{b+1\over2},
\]

where the last inequality is the strict threshold relation
\(2T<b(b+1)\). Hence \(b>4v+1\). Substituting \(v=n-b+1\) again yields

\[
5b>4n+5.
\tag{TH9}
\]

For \(n\ge3\), this also gives \(b>2\), so predecessor minimality is valid:
\((b-1)b\le2T\). Since (TH9) implies both
\(b>(4n+5)/5\) and \(b-1>4n/5\),

\[
T
\ge {b(b-1)\over2}
>
{8\over25}n^2+{2\over5}n.
\tag{TH10}
\]

This proves the lower coefficient for every admissible threshold, not only
along a subsequence.

For a matching all-\(n\) upper construction, let \(n\ge11\) and put

\[
d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T_n^*={d_n(d_n-1)\over2}.
\tag{TH11}
\]

Here \(d_n\le n\), and the equality \(2T_n^*=d_n(d_n-1)\) gives
\(b_{T_n^*}=d_n\). Write \(d=d_n\) and \(v=n-d+1\). Formula (TH3) becomes

\[
C_n(T_n^*)
=
\left\lfloor{d-1\over2}\right\rfloor-1
=
\begin{cases}
(d-4)/2,&d\text{ even},\\
(d-3)/2,&d\text{ odd}.
\end{cases}
\]

Since \(5d\ge4n+8\), either parity gives \(C_n(T_n^*)\ge2v\).

It remains to check the unchanged \(\Psi_n\) condition rather than assume it.
Put \(r=\lceil(n+3)/2\rceil\). The bounds

\[
r(r-1)\le{(n+4)(n+2)\over4},
\qquad
T_n^*\ge{(4n+8)(4n+3)\over50}
\]

and

\[
{(4n+8)(4n+3)\over50}
-{(n+4)(n+2)\over4}
={7n^2-62n-152\over100}\ge0
\]

hold for \(n\ge11\); the last polynomial is positive at \(11\) and
increasing thereafter. Thus \(r(r-1)\le T_n^*\), so \(a_{T_n^*}\ge r\) and
\(2u\le n-1\). Moreover,

\[
a_{T_n^*}+2d_n
\ge {n+3\over2}+{2(4n+8)\over5}
={21n+47\over10}
\ge2n+5.
\]

Also, since \(d\le n\),
\[
T_n^*\le {n(n-1)\over2}<n(n+1),
\]
so \(a_{T_n^*}\le n\) and \(u=n-a_{T_n^*}+1\); likewise
\(v=n-d+1\). Since \(\delta_n(T_n^*)\le1\), the preceding bound now gives
explicitly
\[
u+2v+\delta_n(T_n^*)
=
3n-a_{T_n^*}-2d+3+\delta_n(T_n^*)
\le n-1.
\]
Both branches of (TT11) therefore fit, so
\(\Psi_n(T_n^*)\le n-1\) and \(H_n\le T_n^*\). Finally,

\[
T_n^*
<
{(4n+13)(4n+8)\over50}
=
{8\over25}n^2+{42\over25}n+{52\over25}.
\tag{TH12}
\]

Combining (TH10) and (TH12) proves the exact asymptotic decision

\[
\boxed{
H_n={8\over25}n^2+O(n),
\qquad
\lim_{n\to\infty}{H_n\over n^2}={8\over25}
},
\qquad
\boxed{
\liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}
}.
\tag{TH13}
\]

The value \(8/25\) is verified by the inequalities, not inferred from finite
data. At the scale \(T\sim(8/25)n^2\), one has
\(a_T/n\to2\sqrt2/5\) and \(b_T/n\to4/5\). The incidence condition is tight:
both \(2v/n\) and \(C_n(T)/n\) tend to \(2/5\). By contrast, the two branches
of \(\Psi_n(T)/n\) tend to

\[
2-{4\sqrt2\over5}<1,
\qquad
{7-2\sqrt2\over5}<1,
\]

so the older packing condition is strictly slack at the new transition. The
new coefficient also strictly exceeds the unchanged \(Q_n\) coefficient:

\[
{8\over25}-{36-16\sqrt2\over49}
={400\sqrt2-508\over1225}>0,
\]

because \(20000=(100\sqrt2)^2>127^2=16129\). This theorem concerns \(H_n\)
and the resulting lower bound for \(B_n\) only. It does not determine a limit
or exact coefficient for \(B_n\), does not lower-bound or redefine \(L_n\),
and does not transfer to \(R_2^*(n)\) or the geometric optimum.

## Matching Eight-Twenty-Fifths Upper Construction

The preceding limitation can now be removed for the combinatorial surrogates.
The threshold used only as an upper witness for \(H_n\) in (TH11) also admits
an explicit cyclic order. Put

\[
d=d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T=T_n={d(d-1)\over2}.
\tag{UC1}
\]

We prove that every \(n\ge9\) has an explicit core order \(\sigma_n\) with

\[
W(\sigma_n)\le T_n.
\tag{UC2}
\]

The construction is symbolic on five residue-class tails and uses fourteen
displayed witnesses before those tails begin. No canonical cyclic-order
enumeration beyond \(n=11\) is used.

### Parameters and symbolic domain

Set

\[
v=n-d+1,
\qquad
e=d-4v.
\tag{UC3}
\]

Exact evaluation by residue class gives

| \(n\bmod5\) | \(e\) | \(d\) and \(n\) in terms of \(v\) |
|---:|---:|---|
| \(0\) | \(6\) | \(d=4v+6,\ n=5v+5\) |
| \(1\) | \(7\) | \(d=4v+7,\ n=5v+6\) |
| \(2\) | \(8\) | \(d=4v+8,\ n=5v+7\) |
| \(3\) | \(4\) | \(d=4v+4,\ n=5v+3\) |
| \(4\) | \(5\) | \(d=4v+5,\ n=5v+4\) |

Thus always

\[
4\le e\le8,
\qquad
d=4v+e,
\qquad
n=5v+e-1.
\tag{UC4}
\]

The \(v\) terminal labels are \(d,\dots,n\). Reserve the \(2v\) labels
\(2,\dots,2v+1\) as their cyclic neighbors. The middle interval has size

\[
\mu=d-2v-2=2v+e-2.
\]

Define

\[
t=\left\lfloor{\mu-v\over2}\right\rfloor
=\left\lfloor{v+e-2\over2}\right\rfloor,
\qquad
\varepsilon=\mu-v-2t\in\{0,1\},
\qquad
r=v-t-\varepsilon.
\tag{UC5}
\]

The block formula below is valid exactly when \(r\ge0\), equivalently
\(v\ge e-2\). Its first index in residue classes \(3,4,0,1,2\) is,
respectively,

\[
13,\ 19,\ 25,\ 31,\ 37.
\tag{UC6}
\]

It therefore covers every \(n\ge33\), as well as

\[
13,18,19,23,24,25,28,29,30,31.
\tag{UC7}
\]

### The symbolic cycle

For \(0\le j<v\), put

\[
E_j=d+j,
\qquad
\lambda_j=2v-2j,
\qquad
\rho_j=2v+1-2j.
\tag{UC8}
\]

For \(0\le j<t\), define the three-element middle path

\[
P_j=(d-1-2j,\ 2v+2+j,\ d-2-2j).
\tag{UC9}
\]

The still unused middle labels form the interval

\[
S=[a,b],
\qquad
a=2v+t+2,
\qquad
b=d-2t-1=3v+1+\varepsilon.
\tag{UC10}
\]

If \(\varepsilon=1\), let \(P_t=(a,a+1)\). Turn every remaining
member of \(S\), in increasing order, into a singleton path. If
\(\varepsilon=0\), every member of \(S\) is a singleton path. Equation
(UC5) gives exactly \(v\) paths \(P_0,\dots,P_{v-1}\). Moreover, the
connector labels in (UC9), the interval (UC10), and the two outer labels in
each triple partition \(\{2v+2,\dots,d-1\}\).

Expand the paths in the cyclic sequence

\[
\boxed{
\sigma_n=
(E_0,\lambda_0,P_0,\rho_1,E_1,\lambda_1,P_1,\rho_2,
\dots,
E_{v-1},\lambda_{v-1},P_{v-1},\rho_0)
}.
\tag{UC11}
\]

Thus each \(E_j\) has the two neighbors \(\rho_j,\lambda_j\), and the
oriented gap from \(E_j\) to \(E_{j+1}\) has the form

\[
E_j,\lambda_j,P_j,\rho_{j+1},E_{j+1},
\]

with subscripts read cyclically. Every \(P_j\) is nonempty, so consecutive
terminal labels are at positional distance at least four.

### Adjacent products

The larger product at the two terminal-low edges incident to \(E_j\) is at
most

\[
f_j=(d+j)(2v+1-2j).
\]

The sequence \(f_j\) is decreasing, and

\[
f_0=d(2v+1)\le {d(d-1)\over2}=T,
\tag{UC12}
\]

because \(4v+2\le d-1=4v+e-1\). Every low-middle edge satisfies

\[
xy\le(2v+1)(d-1)\le {d(d-1)\over2}=T,
\tag{UC13}
\]

because \(4v+2\le d\).

It remains to check internal triple and doubleton edges. With one-based
\(j=1,\dots,t\), the larger internal product of the \(j\)-th triple is

\[
F_j=(2v+1+j)(d-2j+1),
\qquad
F_{j+1}-F_j=e-4j-3.
\]

For \(e\le7\), the maximum is \(F_1\), while for \(e=8\) it is
\(F_2=F_1+1\). Since

\[
T-F_1={(e-4)(d-1)\over2},
\tag{UC14}
\]

all triple edges have product at most \(T\). When \(e=8\), the displayed
slack is \(2(d-1)>1\), so the one-unit increase is harmless.

If \(\varepsilon=1\), then \(a=(n+2)/2\) and \(a+1=(n+4)/2\). The only
middle-middle edge outside a triple obeys

\[
a(a+1)\le T,
\tag{UC15}
\]

because

\[
2d(d-1)-(n+2)(n+4)
\ge {7n^2-62n-152\over25}\ge0
\]

for the symbolic domain, whose smallest index is \(13\). Equations
(UC12)--(UC15) prove every adjacent product bound.

### Pairs at positional distance two

If neither endpoint is terminal, then

\[
xy\le(d-1)^2\le d(d-1)=2T.
\tag{UC16}
\]

For the triple with one-based index \(j\), the terminal labels at its two
ends give the exact differences

\[
d(d-1)-(d+j-1)(d-2j+1)
=(j-1)(d+2j-1)\ge0,
\]

and

\[
d(d-1)-(d+j)(d-2j)
=(j-1)d+2j^2\ge0.
\tag{UC17}
\]

At \(j=1\), the first product is exactly \(d(d-1)=2T\): the pair
\((d,d-1)\) is at positional distance two. For a singleton or doubleton
endpoint, (UC10) and \(E_j\le n\) give

\[
d(d-1)-nb
=v^2+(5e-6-5\varepsilon)v
 +(e-1)(e-1-\varepsilon)>0.
\tag{UC18}
\]

There is one separate closing form when \(t=v\), so the last path is also a
triple. Its endpoint adjacent at distance two to \(E_{v-1}=n\) satisfies

\[
d(d-1)-n(d-2v+1)
=d(v-1)+2v^2-3v+1\ge0,
\]

while the endpoint seen from \(E_0=d\) is \(d-2v<d-1\). This completes
the distance-two proof, including its closing pairs.

### Pairs at positional distance three

Every terminal-terminal pair has distance at least four because every
terminal gap contains a low, a nonempty \(P_j\), and another low. A pair at
distance three therefore has at most one terminal endpoint. Its product is
bounded by

\[
xy\le n(d-1)< {3d(d-1)\over2}=3T,
\tag{UC19}
\]

since

\[
3d-2n=2v+e+2>0.
\]

This applies cyclically and hence includes every distance-three pair crossing
the displayed cut in (UC11).

### Closing arcs and distances at least four

The displayed closing segment is

\[
E_{v-1},\lambda_{v-1},P_{v-1},\rho_0,E_0.
\]

The edge \(\rho_0E_0\) is the \(j=0\) case of (UC12), the preceding
low-middle edge is covered by (UC13), and its distance-two endpoint is covered
by (UC18) or by the explicit all-triple calculation following (UC17).
There is no terminal-terminal closing pair at distance three. Thus no linear
presentation endpoint has escaped the preceding cyclic checks.

Finally, if \(q=d_{\sigma_n}(i,j)\ge4\), then

\[
ij\le n(n-1)<2d(d-1)=4T\le qT.
\tag{UC20}
\]

The strict middle inequality follows directly from (UC4):

\[
2d(d-1)-n(n-1)
=7v^2+(6e+7)v+(e-1)(e+2)>0.
\]

Hence every distance at least four is automatic at the chosen threshold.

### The fourteen initial witnesses

The symbolic condition \(v\ge e-2\) fails, for \(n\ge9\), exactly at

\[
\mathcal X
=\{9,10,11,12,14,15,16,17,20,21,22,26,27,32\}.
\tag{UC21}
\]

The following orders are explicit witnesses. Each is rotated to start with
\(n\); they are not asserted to be minimizers.

```text
9:  (9,2,8,4,6,5,7,3)
10: (10,2,9,4,7,6,5,8,3)
11: (11,2,10,4,8,6,7,5,9,3)
12: (12,2,11,4,9,6,7,8,5,10,3)
14: (14,3,11,2,13,4,12,6,9,8,7,10,5)
15: (15,3,12,2,14,4,13,6,10,8,9,7,11,5)
16: (16,2,13,4,15,6,11,8,9,10,7,14,5,12,3)
17: (17,5,14,3,13,2,16,4,15,6,12,8,10,9,11,7)
20: (20,2,13,10,11,12,9,17,7,16,5,18,3,15,8,19,4,14,6)
21: (21,6,15,4,20,2,16,3,19,5,17,7,18,9,13,11,12,10,14,8)
22: (22,2,16,4,19,6,20,8,15,10,13,12,11,14,9,21,7,18,5,17,3)
26: (26,2,18,4,23,11,21,8,24,10,17,12,15,14,13,16,6,25,9,20,7,22,5,19,3)
27: (27,2,18,4,24,6,22,8,20,10,23,12,16,14,15,13,17,11,25,9,21,7,26,5,19,3)
32: (32,2,22,4,29,6,26,13,25,10,30,12,21,14,19,16,17,18,15,20,8,31,11,24,9,27,7,28,5,23,3)
```

For an order displayed with this cut, let \(M_q\) be the maximum score
\(xy/q\) over all pairs at positional distance \(q\), and let \(C_q\) be
the same maximum restricted to pairs crossing the cut. Direct exact rational
evaluation gives:

| \(n\) | \(T_n\) | \(M_1\) | \(M_2\) | \(M_3\) | \(C_1\) | \(C_2\) | \(C_3\) | \(W(\sigma_n)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 36 | 35 | 36 | 15 | 27 | \(63/2\) | 15 | 36 |
| 10 | 45 | 42 | 45 | \(56/3\) | 30 | 40 | \(50/3\) | 45 |
| 11 | 55 | 48 | 55 | 20 | 33 | \(99/2\) | \(55/3\) | 55 |
| 12 | 66 | 56 | 66 | 24 | 36 | 60 | 20 | 66 |
| 14 | 78 | 72 | 78 | \(98/3\) | 70 | 70 | \(98/3\) | 78 |
| 15 | 91 | 80 | 91 | 35 | 75 | \(165/2\) | 35 | 91 |
| 16 | 105 | 98 | 104 | 42 | 48 | 96 | \(80/3\) | 104 |
| 17 | 120 | 119 | 120 | 51 | 119 | \(187/2\) | 51 | 120 |
| 20 | 153 | 153 | 144 | \(200/3\) | 120 | 140 | \(80/3\) | 153 |
| 21 | 171 | 168 | \(323/2\) | 70 | 168 | 147 | 70 | 168 |
| 22 | 190 | 189 | 190 | 77 | 66 | 187 | \(110/3\) | 190 |
| 26 | 253 | 253 | 252 | \(325/3\) | 78 | 247 | \(130/3\) | 253 |
| 27 | 276 | 276 | 273 | \(325/3\) | 81 | \(513/2\) | 45 | 276 |
| 32 | 378 | 360 | 378 | 155 | 96 | 368 | \(160/3\) | 378 |

Every displayed \(M_q\) is at most \(T_n\), while its underlying product is
at most \(qT_n\). The \(C_q\) columns separately check all local closing
pairs. Equation (UC20), which also holds at these indices, covers every
remaining distance. This proves (UC2) for the fourteen initial cases by exact
finite substitution, not by an extrapolation from them.

An exact positional constraint search was used only to falsify candidates and
identify these witnesses. It used Boolean position-label assignments and
forbidden local pairs for distances one, two, and three; it did not enumerate
canonical cyclic orders. The production generator performs no search. The
repository's canonical factorial enumerator remains hard-bounded to
\(n\le11\).

### Exact residue-class formula for \(H_n\)

The upper threshold in (UC1) also exposes the exact finite obstruction by
residue class. Write \(n=5k+r\), with \(0\le r<5\). For any half-integer
threshold \(X\) admissible in (TH4), put \(b=b_X\). The all-threshold lower
argument (TH9) and integrality give the following minimum possible value of
\(b\):

| \(r\) | \(d_n\) | lower bound on \(b_X\) | candidate \(h_{k,r}\) |
|---:|---:|---:|---:|
| 0 | \(4k+2\) | \(d_n\) | \(d_n(d_n-1)/2\) |
| 1 | \(4k+3\) | \(d_n-1\) | \((d_n-1)^2/2\) |
| 2 | \(4k+4\) | \(d_n-1\) | \((d_n-1)(d_n-2)/2\) |
| 3 | \(4k+4\) | \(d_n\) | \(d_n(d_n-1)/2\) |
| 4 | \(4k+5\) | \(d_n\) | \(d_n(d_n-1)/2\) |

Indeed, substituting \(n=5k+r\) into \(5b>4n+5\) gives exactly the third
column. Predecessor minimality gives

\[
(b-1)b\le2X.
\tag{RC1}
\]

Thus (RC1) proves \(X\ge h_{k,r}\) immediately in residues
\(0,2,3,4\). In residue one, if \(b\ge d_n\), (RC1) is already stronger
than the displayed candidate. If \(b=d_n-1=4k+2\), then
\(v=n-b+1=k\), and (TH2)--(TH3) force

\[
2k\le\left\lfloor{X\over d_n-1}\right\rfloor-1.
\]

Hence \(X\ge(d_n-1)^2/2=h_{k,1}\). This is the even-square capacity event
from (TH6), not an estimate from the asymptotic theorem.

It remains to prove that the lower candidates are admissible. In residues
\(0,3,4\), the candidate is \(T_n\). Equations (TH11)--(TH12) already prove
its admissibility for \(n\ge11\). The two smaller boundary cases give the
exact data

\[
(n,T_n,a,b,u,v,C_n(T_n),\Psi_n(T_n))
=(9,36,6,9,4,1,3,8)
\]

and

\[
(n,T_n,a,b,u,v,C_n(T_n),\Psi_n(T_n))
=(10,45,7,10,4,1,3,8),
\]

so they are admissible as well.

For residues one and two, let \(h=h_{k,r}\) be the smaller candidate and
put

\[
p=\left\lceil{n+3\over2}\right\rceil.
\]

In residue one, \(k\ge2\), while in residue two take \(k\ge3\), equivalently
\(n\ge17\). Direct substitution gives

\[
h-{(n+4)(n+2)\over4}
=
\begin{cases}
(7k^2-8k-7)/4,&r=1,\\
(7k^2-10k-12)/4,&r=2.
\end{cases}
\tag{RC2}
\]

Both expressions are nonnegative on the stated domains. Since
\(p(p-1)\le(n+4)(n+2)/4\), (RC2) gives \(a_h\ge p\) and hence
\(2u\le n-1\). At either candidate, \(b_h=d_n-1\), \(v=k\), and (TH3)
gives \(C_n(h)=2k=2v\). In residue one, \(2h=b_h^2\), so
\(\delta_n(h)=0\), and \(p\ge2k+2\) gives

\[
u+2v+\delta_n(h)\le7k+2-(2k+2)=5k=n-1.
\]

In residue two, \(\delta_n(h)\le1\), and \(p\ge2k+3\) gives

\[
u+2v+\delta_n(h)\le7k+4-(2k+3)=5k+1=n-1.
\]

Both branches of (TT11) therefore fit, so these candidates are admissible.

The excluded residue-two boundary is genuinely exceptional. The lower
argument gives \(H_{12}\ge55\). At both \(X=55\) and \(X=111/2\), one has
\(a=7,b=11,u=6,v=2,C_{12}(X)=4\), but
\(\Psi_{12}(X)=12>11\). At \(X=56\), the exact data become

\[
a=8,\quad b=11,\quad u=5,\quad v=2,\quad C_{12}(56)=4,
\quad\Psi_{12}(56)=10,
\]

so both conditions in (TH4) hold. Consequently

\[
\boxed{
H_n=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
(d_n-1)(d_n-2)/2,&n\equiv2\pmod5,\ n\ge17,\\
56,&n=12.
\end{cases}
}
\tag{RC3}
\]

Equivalently, apart from the displayed exception,

\[
H_n=
\begin{cases}
(4n+10)(4n+5)/50,&n\equiv0\pmod5,\\
(4n+6)^2/50,&n\equiv1\pmod5,\\
(4n+7)(4n+2)/50,&n\equiv2\pmod5,\\
(4n+8)(4n+3)/50,&n\equiv3\pmod5,\\
(4n+9)(4n+4)/50,&n\equiv4\pmod5.
\end{cases}
\tag{RC4}
\]

### Sharper saturation obstruction in residue two

The exact value of \(H_n\) in (RC3) is unchanged. We now use the structure
behind (TH2), rather than only its aggregate inequality, to exclude a further
interval of thresholds in residue two.

First let

\[
n=5k+2,
\qquad
k\ge3,
\qquad
d=d_n=4k+4,
\]

and abbreviate

\[
H=H_n={(d-1)(d-2)\over2},
\qquad
J=J_n={d(d-2)\over2}.
\tag{R2S1}
\]

The interval is nonempty because

\[
J-H={d-2\over2}=2k+1>0.
\]

Suppose for contradiction that a cyclic core order \(\sigma\) has
\(S_2(\sigma)\le X\) at an exact threshold

\[
H\le X<J.
\tag{R2S2}
\]

The strict definition of \(b_X\) is decisive. At the predecessor and
candidate labels,

\[
(d-2)(d-1)=2H\le2X,
\qquad
2X<2J=d(d-2)<d(d-1).
\]

Thus \(d-2\) does not satisfy \(b(b+1)>2X\), while \(d-1\) does. Since
\(b(b+1)\) is strictly increasing for \(b\ge2\),

\[
b_X=d-1,
\qquad
V_X=\{d-1,\dots,n\},
\qquad
v=n-d+2=k.
\tag{R2S3}
\]

Put \(q=d/2-1=2k+1\). The lower and strict upper endpoints in (R2S2) give

\[
q={H\over d-1}
\le {X\over d-1}
<{J\over d-1}
<{d\over2}=q+1.
\]

Therefore

\[
\left\lfloor{X\over b_X}\right\rfloor=2k+1.
\tag{R2S4}
\]

There is no hidden \(a_X\)-cap in this floor. Indeed,

\[
q(q+1)={d(d-2)\over4}<H\le X,
\]

so the strict definition of \(a_X\) gives \(a_X\ge q+1=d/2\).
At the other end, with \(x=d-2\),

\[
x(x+1)=2H>J>X,
\qquad
2H-J={(d-2)^2\over2}>0,
\]

so \(a_X\le x=d-2\). In particular
\(d/2\le a_X\le d-2\), although its exact value need not be constant as
\(X\) varies.

Consequently the compatible lows in (TH1) are exactly

\[
L=\{2,\dots,2k+1\},
\qquad
|L|=2k=2v=C_n(X).
\tag{R2S5}
\]

The injection proved in (TH2) is therefore a bijection: every terminal high
has two distinct neighbors in \(L\), and every label in \(L\) is adjacent to
exactly one terminal high.

The remaining labels form the intermediate block

\[
M=\left\{{d\over2},\dots,d-2\right\},
\qquad
|M|=2k+1,
\]

and the cardinalities check the entire core:

\[
|L|+|M|+|V_X|=2k+(2k+1)+k=5k+1=n-1.
\tag{R2S6}
\]

Delete the vertices of \(V_X\) from the position cycle. Saturation makes
every low in \(L\) have residual degree one, while every intermediate label
has residual degree two because terminal highs have no intermediate
neighbors. Recall that \(x=d-2\in M\).

For every possible distinct intermediate neighbor \(y\in M\),

\[
xy\ge x{d\over2}={(d-2)d\over2}=J>X.
\tag{R2S7}
\]

The adjacent score constraint excludes such an edge. Hence the residual
component containing \(x\) is exactly

\[
\ell_-\;--\;x\;--\;\ell_+,
\qquad
\ell_-,\ell_+\in L,
\]

and in the original cycle it extends to

\[
t_-\;--\;\ell_-\;--\;x\;--\;\ell_+\;--\;t_+,
\qquad
t_-,t_+\in V_X.
\tag{R2S8}
\]

The two terminal positions are distinct. They occur at \(p(x)-2\) and
\(p(x)+2\) in a simple cycle of length
\(N=n-1=5k+1\ge16\); equality of the positions would require \(N\mid4\).
Both positions are at smaller circular distance exactly two from \(x\).
Thus \(S_2(\sigma)\le X\) requires

\[
{x t_\pm\over2}\le X<J={xd\over2}.
\]

It follows that \(t_\pm<d\). But (R2S8) also gives
\(t_\pm\in V_X=\{d-1,\dots,n\}\), so integrality forces

\[
t_-=t_+=d-1.
\tag{R2S9}
\]

This contradicts the distinctness of the two terminal positions, because a
cyclic core order is a permutation.

For completeness, the half-integer endpoint semantics contain no gap.
Every truncated score is in \(\tfrac12\mathbb Z\), the finite order space
attains \(B_n\), and (TH5) gives \(B_n\ge H_n\). Since \(J_n\) is an
integer, an assumption \(B_n<J_n\) would put the exact threshold
\(X=B_n\) among

\[
H_n,H_n+{1\over2},\dots,J_n-{1\over2},
\]

all of which were excluded above. Therefore

\[
\boxed{
B_n\ge J_n={d_n(d_n-2)\over2}
}
\qquad(n\equiv2\pmod5,\ n\ge17).
\tag{R2S10}
\]

The boundary \(X=J_n\) is deliberately not excluded: at equality the edge
from \(x\) to \(d/2\) and the distance-two pair \((x,d)\) both become
compatible. The strict inequality in (R2S2) is therefore essential, and
(R2S10) is a lower bound, not an exact-value claim.

The exceptional value \(n=12\) must start from the exact obstruction
\(H_{12}=56\), not from the generic residue-two expression \(55\). Here

\[
d=12,
\qquad
H_{12}=56,
\qquad
J_{12}=60.
\tag{R2S11}
\]

Suppose for contradiction that \(S_2(\sigma)\le X\) for some
\(56\le X<60\). Strict threshold arithmetic gives

\[
7\cdot8\le X<8\cdot9,
\qquad
10\cdot11<2H_{12}\le2X<120<11\cdot12.
\]

Thus

\[
a_X=8,
\qquad
b_X=11,
\qquad
V_X=\{11,12\},
\qquad
v=2.
\]

Moreover \(\lfloor X/11\rfloor=5\), so the compatible lows are exactly
\(L=\{2,3,4,5\}\), with \(|L|=4=2v\), and the incidence injection again
saturates. The intermediate block is \(M=\{6,7,8,9,10\}\). With \(x=10\),

\[
x\cdot6=60=J_{12}>X,
\]

so the residual component is again low--\(x\)--low. Its two terminal
extensions occupy the distinct positions \(p(x)-2,p(x)+2\) in the
length-\(11\) cycle. Since \(10\cdot12/2=60>X\), each terminal would have
to be \(11\), contradicting those distinct positions. Finally, if
\(B_{12}<60\), then (TH5) gives \(56=H_{12}\le B_{12}\), and the attained
threshold \(X=B_{12}\) is one of those just excluded. Hence

\[
\boxed{B_{12}\ge60=J_{12}}.
\tag{R2S12}
\]

### Exact matching construction in residue two

The boundary deliberately left open by the saturation argument is attained by
a search-free symbolic family. Keep

\[
n=5k+2,
\qquad
k\ge2,
\qquad
d=4k+4,
\]

and put

\[
D=d-1=4k+3,
\qquad
J=J_n={d(d-2)\over2}={D^2-1\over2},
\qquad
t=\left\lceil{k\over2}\right\rceil.
\tag{R2C1}
\]

For \(0\le j<k\), define

\[
E_j=D+j,
\qquad
\lambda_j=2k-2j,
\qquad
\rho_j=2k+1-2j.
\tag{R2C2}
\]

For \(0\le j<t\), let

\[
P_j=(D-1-2j,\ 2k+2+j,\ D-2-2j).
\tag{R2C3}
\]

The residual middle interval has endpoints

\[
a=2k+t+2,
\qquad
b=D-2t-1.
\tag{R2C4}
\]

There are two parity branches. If \(k=2m+1\), then \(t=m+1\) and set

\[
P_{t+r}=(a+r)
\qquad(0\le r<m).
\tag{R2C5}
\]

If \(k=2m\), then \(t=m\) and set

\[
P_t=(a,a+1),
\qquad
P_j=(a+j-t+1)
\quad(t<j<k).
\tag{R2C6}
\]

Expand these paths in the cyclic concatenation

\[
\boxed{
\sigma_n^{(2)}
=
\bigoplus_{j=0}^{k-1}
(E_j,\lambda_j,P_j,\rho_{j+1})
},
\tag{R2C7}
\]

where the subscript on \(\rho\) is read modulo \(k\). Thus \(E_j\) has
neighbors \(\rho_j,\lambda_j\), and the oriented gap to \(E_{j+1}\) is

\[
E_j,\lambda_j,P_j,\rho_{j+1},E_{j+1}.
\tag{R2C8}
\]

#### Permutation and parity branches

The terminal labels \(E_j\) cover \([D,n]\), while the
\(\lambda_j,\rho_j\) cover \([2,2k+1]\). The connectors in (R2C3) cover
\([2k+2,2k+t+1]\), and the two outer labels of those triples cover
\([D-2t,D-1]\). The only interval left between them is exactly
\([a,b]\).

If \(k=2m+1\), then \([a,b]\) has \(m\) labels, and (R2C5) places them in
the \(m=k-t\) residual singleton paths. If \(k=2m\), then \([a,b]\) has
\(m+1\) labels; (R2C6) places its first two labels in one doubleton and its
remaining \(m-1\) labels in singleton paths. Hence the displayed sets are
disjoint, exhaust \(\{2,\dots,n\}\), and give exactly \(k\) nonempty paths
in both parity branches. Therefore (R2C7) is a cyclic core order for every
\(k\ge2\).

#### Adjacent products

The larger of the two terminal-low products incident to \(E_j\) is

\[
f_j=(D+j)(2k+1-2j).
\]

This sequence is strictly decreasing, and

\[
J-f_0=J-D(2k+1)=2k+1>0.
\tag{R2C9}
\]

Every low-middle edge obeys

\[
(2k+1)(D-1)=J-(4k+2)<J.
\tag{R2C10}
\]

For the larger internal product in the triple \(P_j\), put

\[
F_j=(D-1-2j)(2k+2+j).
\]

Then

\[
F_0=J,
\qquad
F_{j+1}-F_j=-4(j+1)<0.
\tag{R2C11}
\]

The other internal edge has the same connector and a smaller outer label. In
the even branch \(k=2m\), the only remaining internal edge is the doubleton
in (R2C6), and

\[
J-a(a+1)=7m^2-m-2>0
\qquad(m\ge1).
\tag{R2C12}
\]

There is no internal edge in a residual singleton. Thus every adjacent
product is at most \(J\), and the edge
\((D-1,2k+2)\) inside \(P_0\) has product exactly \(J\).

#### Pairs at positional distance two

Every \(P_j\) is nonempty, so consecutive terminal labels are at positional
distance at least four. If neither endpoint at distance two is terminal, its
product is at most \((D-1)^2<D(D-1)\). The remaining pairs join a terminal
to the first or last label of a middle path.

For the triple \(P_j\), direct subtraction gives

\[
D(D-1)-(D+j)(D-1-2j)
=j(D+1+2j)\ge0
\tag{R2C13}
\]

and

\[
D(D-1)-(D+j+1)(D-2-2j)
=Dj+2(j+1)^2>0.
\tag{R2C14}
\]

Every residual endpoint is at most \(b\), and every terminal is at most
\(n\). The needed formal endpoint bound is strict. Indeed,

\[
D(D-1)-nb
=
\begin{cases}
4m^2+8m+2,&k=2m,\\
4m^2+22m+14,&k=2m+1,
\end{cases}
>0.
\tag{R2C15}
\]

Consequently the exact maximum product at positional distance two is
\(D(D-1)\), attained by \(E_0=D\) and the first label \(D-1\) of \(P_0\).
Since

\[
D(D-1)<D^2-1=2J,
\tag{R2C16}
\]

every distance-two score is strictly below \(J\).

#### Pairs at positional distance three

The nonempty \(P_j\) also exclude terminal-terminal pairs at positional
distance three. Such a pair therefore has at most one terminal endpoint, and
its other endpoint is at most \(D-1\). Hence

\[
xy\le n(D-1)<3J,
\tag{R2C17}
\]

because

\[
3J-n(D-1)=4k^2+18k+8>0.
\tag{R2C18}
\]

This verifies the distance-three class separately and cyclically.

#### Closing pairs

The part of (R2C7) surrounding its displayed cut is

\[
\cdots,E_{k-1},2,P_{k-1},2k+1
\mid
D,2k,P_0,\cdots,
\tag{R2C19}
\]

and \(\operatorname{last}(P_{k-1})=b\). The products crossing the cut are

\[
q=1:\quad D(2k+1),
\tag{R2C20}
\]

\[
q=2:\quad Db,\quad 2k(2k+1),
\tag{R2C21}
\]

and

\[
q=3:\quad Dz,\quad 2kb,\quad(2k+1)(D-1),
\qquad
z=
\begin{cases}
7,&k=2,\\
2,&k\ge3.
\end{cases}
\tag{R2C22}
\]

Equation (R2C9) covers (R2C20). In (R2C21), \(b<D-1\), so
\(Db<D(D-1)<2J\), while the low-low product is smaller still. Every product
in (R2C22) is at most \(n(D-1)<3J\) by (R2C17). Thus all pairs crossing the
displayed cut satisfy their respective distance bounds; none is hidden by the
linear presentation.

#### Distances at least four and exact consequence

For every pair at smaller circular positional distance \(q\ge4\), distinctness
of its labels and the identity required for this residue class give

\[
ij\le n(n-1)<4J\le qJ,
\qquad
4J-n(n-1)=7k^2+33k+14>0.
\tag{R2C23}
\]

Together, (R2C9)--(R2C23) prove \(W(\sigma_n^{(2)})\le J_n\). The internal
edge identified after (R2C12) proves equality:

\[
\boxed{W(\sigma_n^{(2)})=J_n}
\qquad(n=5k+2,\ k\ge2).
\tag{R2C24}
\]

Combining this upper construction with (R2S10) and (R2S12) yields

\[
\boxed{B_n=W_n=J_n={d_n(d_n-2)\over2}}
\tag{R2C25}
\]

for \(n=12\) and for every \(n\equiv2\pmod5\), \(n\ge17\). The case \(n=7\)
remains covered by the bounded exact table and is outside the stated generator
domain. The supplied finite witnesses were used only to falsify candidate
forms and identify this block structure; the production formula (R2C1)--
(R2C7) performs no search, and canonical cyclic-order enumeration remains
hard-bounded to \(n\le11\).

The induced-subset objective on this same cyclic core is evaluated separately
in Section 10 of `research/FIXED_ORDER_CYCLE_RATIO.md`, where it is denoted by
\(\tau_n^{(2)}=\sigma_n^{(2)}\). Its shortcut-budget theorem proves that the
unique maximizing subset is \(\{2k+1,\ldots,n\}\) and that
\[
K(\tau_n^{(2)})=K(\sigma_n^{(2)})
={143\over500}n^3+O(n^2).
\]
The exact two parity branches are (KR2-3)--(KR2-4). They are strictly below
the canonical K825 score in every residue-two row, with no crossover and
with difference \(21n^2/100+O(n)\). This is a statement about \(K\), not a
change to the exact surrogate identity \(W(\sigma_n^{(2)})=J_n\).

### Exact construction in residue one

The smaller residue-one obstruction is also attained. Write

\[
n=5k+1,\qquad k\ge2,\qquad
D=d_n-1=4k+2,\qquad
h={D^2\over2}=H_n.
\tag{R1C1}
\]

There is a useful structural reason for the form below. At threshold \(h\),
the terminal tail

\[
V=\{D,\dots,n\}
\]

has \(k\) vertices. Every neighbor of a vertex in \(V\) must be at most
\(h/D=D/2=2k+1\). No label can neighbor two vertices of \(V\), because those
two vertices would be at positional distance two while their product is at
least

\[
D(D+1)>D^2=2h.
\]

The \(2k\) terminal incidences therefore saturate exactly the \(2k\) labels
\(2,\dots,2k+1\). Removing \(V\) leaves \(k\) paths whose internal labels
come from

\[
M=\{2k+2,\dots,D-1\}.
\]

The most immediate specialization of the older block family is false:

\[
(D-1)(2k+2)-h=2k>0.
\tag{R1C2}
\]

Thus \(D-1\) cannot have a neighbor in \(M\); it must be a one-vertex path
between two low labels. This exact failed inequality, not an extrapolation
from finite witnesses, motivates the shifted construction.

Put

\[
t=\left\lfloor{k\over2}\right\rfloor,
\qquad
\varepsilon=k-2t\in\{0,1\}.
\tag{R1C3}
\]

For \(0\le j<k\), define

\[
E_j=D+j,\qquad
\lambda_j=2k-2j,\qquad
\rho_j=2k+1-2j.
\tag{R1C4}
\]

Define the middle paths by

\[
P_0=(D-1),
\tag{R1C5}
\]

\[
P_j=(D-2j,\ 2k+1+j,\ D-2j-1)
\qquad(1\le j\le t),
\tag{R1C6}
\]

and, for \(t<j<k-\varepsilon\), let \(P_j\) be the one-vertex path

\[
P_j=(D-t-j-1).
\tag{R1C7}
\]

If \(\varepsilon=1\), so \(k=2t+1\), finish with the two-vertex path

\[
P_{k-1}=(2k+t+3,\ 2k+t+2).
\tag{R1C8}
\]

Expand every \(P_j\) in the cyclic concatenation

\[
\boxed{
\sigma_n^{(1)}
=
\bigoplus_{j=0}^{k-1}
(E_j,\lambda_j,P_j,\rho_{j+1})
},
\tag{R1C9}
\]

where the subscript on \(\rho\) is read modulo \(k\). The terminal labels
cover \([D,n]\), while the \(\lambda_j,\rho_j\) cover
\([2,2k+1]\). The triple connectors cover
\([2k+2,2k+t+1]\), their two outer labels cover
\([D-2t-1,D-2]\), and \(P_0\) supplies \(D-1\).
The remaining, possibly empty, integer interval is

\[
[a,b]=[2k+t+2,\ D-2t-2].
\tag{R1C10}
\]

It is empty exactly at \(k=2\). If \(k=2t\), the singleton paths in (R1C7)
list this interval in decreasing order. If \(k=2t+1\), they list
\(b,\dots,a+2\), and (R1C8) supplies
\((a+1,a)\). Thus the displayed families are disjoint, exhaust
\(\{2,\dots,n\}\), and give exactly \(k\) nonempty middle paths. In
particular, (R1C9) is a cyclic core order produced without search.

#### Adjacent products

The larger of the two terminal-low products incident to \(E_j\) is

\[
f_j=(D+j)\left({D\over2}-2j\right)
=h-{3D\over2}j-2j^2
\le h.
\tag{R1C11}
\]

Every low-middle edge has product at most

\[
{D\over2}(D-1)<h.
\]

There is no internal edge in a singleton path. In the triple \(P_j\), the
larger internal product is

\[
(D-2j)\left({D\over2}+j\right)=h-2j^2<h.
\tag{R1C12}
\]

When \(k=2t+1\), the only remaining internal edge is the doubleton in
(R1C8). Its endpoints are \(5t+5,5t+4\), and

\[
h-(5t+5)(5t+4)=7t^2+3t-2>0
\qquad(t\ge1).
\tag{R1C13}
\]

This proves every adjacent inequality, including both parity branches.

#### Pairs at positional distance two

If neither endpoint is terminal, then

\[
xy\le(D-1)^2<D^2=2h.
\tag{R1C14}
\]

Every \(P_j\) is nonempty, so any two terminal labels are at distance at
least four. It remains to check the first and last label of each \(P_j\)
against the terminal at that end of its gap. For \(P_0\), the two products are
\(D(D-1)\) and

\[
(D+1)(D-1)=D^2-1.
\tag{R1C15}
\]

For a triple \(P_j\), the left endpoint product satisfies

\[
(D+j)(D-2j)=D^2-Dj-2j^2<D^2
\]

and the right endpoint product is at most

\[
(D+j+1)(D-2j-1)
=D^2-Dj-(j+1)(2j+1)<D^2.
\tag{R1C16}
\]

Here \(D+j+1\) is also a valid formal upper bound when the terminal on the
right is cyclically \(E_0\), as happens at the \(k=2\) closing triple.
For a residual singleton \(x_j=D-t-j-1\), its larger formal terminal bound
is

\[
(D+j+1)x_j
=D^2-Dt-(j+1)(t+j+1)<D^2.
\tag{R1C17}
\]

When a last even singleton exists, the actual terminal on the right is
\(E_0=D\), which is smaller than this formal bound. Finally, when
\(k=2t+1\), the first endpoint of the final doubleton is checked against
\(E_{k-1}=n\) by

\[
D^2-n(5t+5)=14t^2+16t+6>0,
\tag{R1C18}
\]

while its last endpoint is less than \(D\) and is checked against \(E_0=D\).
Therefore every distance-two product is at most \(D^2=2h\). In fact (R1C15)
and integrality show that the exact distance-two maximum product is
\(D^2-1\), so its exact score is \(h-1/2\).

#### Pairs at positional distance three

The gap from \(E_j\) to \(E_{j+1}\) has
\(|P_j|+3\ge4\) edges. Hence two terminal labels never occur at positional
distance three. Such a pair has at most one terminal endpoint, and therefore

\[
xy\le n(D-1)<3h,
\tag{R1C19}
\]

because

\[
3D^2-2n(D-1)=8k^2+30k+10>0.
\]

This argument is cyclic and does not depend on the displayed cut.

#### Closing arcs

The part of (R1C9) surrounding the displayed cut is

\[
E_{k-1},\ 2,\ P_{k-1},\ 2k+1,\ E_0,\ 2k,\ P_0.
\tag{R1C20}
\]

The closing edge has product

\[
(2k+1)E_0={D\over2}D=h.
\tag{R1C21}
\]

The two distance-two pairs crossing the cut are
\((2k+1,2k)\) and
\((\operatorname{last}(P_{k-1}),E_0)\). Their products are strictly below
\(D^2=2h\), since every factor is at most \(D\) and each pair has a
nonterminal factor strictly below \(D\). Every
distance-three pair crossing the cut has at most one terminal endpoint and is
covered by (R1C19). Thus the linear presentation has omitted no cyclic local
constraint.

#### Automatic distances at least four

For \(q=d_{\sigma_n^{(1)}}(i,j)\ge4\),

\[
ij\le n(n-1)<4h\le qh,
\tag{R1C22}
\]

because

\[
4h-n(n-1)=2D^2-n(n-1)=7k^2+27k+8>0.
\tag{R1C23}
\]

Equations (R1C11)--(R1C23) prove \(W(\sigma_n^{(1)})\le h\), while the closing
edge (R1C21) proves equality:

\[
\boxed{W(\sigma_n^{(1)})=h}.
\tag{R1C24}
\]

The induced-subset objective on this same cyclic core is evaluated separately
in Section 9 of `research/FIXED_ORDER_CYCLE_RATIO.md`, where it is denoted by
\(\tau_n^{(1)}=\sigma_n^{(1)}\). Its shortcut-budget theorem proves that the
unique maximizing subset is \(\{2k+1,\ldots,n\}\) and that
\[
K(\tau_n^{(1)})=K(\sigma_n^{(1)})
={857\over3000}n^3+O(n^2).
\]
The exact two parity branches are (KR1-3)--(KR1-4). They are strictly below
the canonical K825 score in every residue-one row, with no crossover. This is
a statement about \(K\), not a change to the exact surrogate identity
\(W(\sigma_n^{(1)})=h\).

Exact bounded positional-constraint search was used only to falsify the
naive family and identify this pattern. The production formula (R1C3)--(R1C9)
contains no search, and canonical factorial enumeration remains bounded to
\(n\le11\).

### Exact surrogate limits and geometric consequence

The existing lower obstruction and the new construction give, for every
\(n\ge9\),

\[
H_n\le B_n\le W_n\le W(\sigma_n)\le T_n.
\tag{UC22}
\]

The first inequality is (TH5), the middle inequality follows from the
definitions of the distance-two and full objectives, and the last two are
the explicit construction. In residues \(0,3,4\), (RC3) makes the two
endpoints in (UC22) equal. In residue one, (R1C24) instead gives

\[
H_n\le B_n\le W_n
\le W(\sigma_n^{(1)})=H_n.
\]

Combining all three constructions proves

\[
\boxed{
B_n=W_n
=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
d_n(d_n-2)/2,&n\equiv2\pmod5
\end{cases}
}
\qquad(n\ge9).
\tag{RC5}
\]

The residue-one branch begins at \(n=11\), and the residue-two branch begins
at \(n=12\). Their separate matching squeezes are (R1C24) and (R2C25).
The former uniform construction has positive slack in both classes, but that
slack is no longer an unresolved objective interval. In residue two,

\[
T_n-J_n
=
\begin{cases}
d_n/2=(2n+6)/5,&n\equiv2\pmod5,\ n\ge17,\\
6,&n=12.
\end{cases}
\tag{RC6}
\]

This is the score excess of the older uniform order threshold over the exact
objective, not an optimality gap. At the exceptional index the exact reference
values are

\[
H_{12}=56<B_{12}=W_{12}=J_{12}=60<T_{12}=66;
\]

for \(n=5k+2\), \(k\ge3\), one instead has

\[
H_n={(d_n-1)(d_n-2)\over2}
<B_n=W_n=J_n={d_n(d_n-2)\over2}
<T_n={d_n(d_n-1)\over2}.
\]

Since

\[
{H_n\over n^2}\longrightarrow{8\over25},
\qquad
{T_n\over n^2}
={1\over2}{d_n\over n}\left({d_n\over n}-{1\over n}\right)
\longrightarrow{8\over25},
\]

the squeeze theorem proves the exact combinatorial asymptotics

\[
\boxed{
{B_n\over n^2}\longrightarrow{8\over25},
\qquad
{W_n\over n^2}\longrightarrow{8\over25}
}.
\tag{UC23}
\]

For \(n\ge12\), the exact core-feasibility result and the accepted
radius-one insertion theorem apply to \(\sigma_n\) at the same explicit
radius. Therefore

\[
R_2^*(n)
\le{(n-1)W(\sigma_n)\over\pi}
\le{(n-1)T_n\over\pi},
\]

and hence

\[
\boxed{
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le {8\over25\pi}
}.
\tag{UC24}
\]

This is a geometric upper coefficient, not a proof that
\(R_2^*(n)/n^3\) converges or that \(8/(25\pi)\) is its exact leading
constant. The cases \(n=9,10,11\) establish the all-\(n\) combinatorial
construction but are not used by the insertion theorem.

### Later exact shortcut evaluation of the same core order

The regular-direction conclusion (UC24) does not exhaust the geometric value
of this construction. Let \(\tau_n=\sigma_n\) as a cyclic core order and use
the induced-subset objective \(K\) from
`research/FIXED_ORDER_CYCLE_RATIO.md`. The later shortcut-budget theorem
in Section 8 determines \(K(\tau_n)\) exactly for every \(n\ge9\).
Equations (K825-2)--(K825-4) cover the symbolic domain, where the unique
maximizing subset is
\[
U_n^*=
\begin{cases}
\{2v+1,\ldots,n\},&e=4,5,\\
\{2v+1,\ldots,n\}\setminus\{2v+2\},&e=6,7,8,
\end{cases}
\tag{UC24a}
\]
and the fourteen orders in (UC21) have the unique maximizing tails recorded
in the fourteen-row table of the K825 theorem. In particular,
\[
K(\tau_n)={143\over500}n^3+O(n^2).
\tag{UC24b}
\]

Inserting label \(1\) in any gap gives a complete order
\(\widehat\sigma_{n,g}\) with
\[
\Lambda(\widehat\sigma_{n,g})=K(\tau_n).
\tag{UC24c}
\]
The exact fixed-order angular sandwich therefore sharpens the current global
upper consequence to
\[
\boxed{
\limsup_{n\to\infty}{\Lambda_n\over n^3}\le{143\over500},
\qquad
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{143\over500\pi}.
}
\tag{UC24d}
\]
This does not change the exact product-distance theorem (UC23):
\(W_n/n^2\to8/25\). The improvement is specific to shortcut optimization
and variable angular spacings; it proves neither convergence nor equality of
the displayed global upper bounds.

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
\(n\ge33\). Neither this tail argument nor the independent distance-two
strictness theorem (DT9)--(DT10) alone determines the full values \(W_n\) for
\(12\le n\le32\); the later residue-class theorem (RC5) does determine them.

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

The exact comparison table is below. The \(A_n,Q_n,H_n,L_n\) columns are
exact formula evaluations; the \(B_n,W_n\) columns and minimizer counts are
the bounded exhaustive results.

| \(n\) | \(A_n\) | \(Q_n\) | \(H_n\) | \(\max(A_n,H_n)\) | \(B_n=W_n^{(\le2)}\) | \(L_n\) | \(W_n\) | minimizers \((\le1,\le2)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | \(6\) | \(6\) | \(6\) | \(6\) | \(6\) | -- | \(6\) | \(1,1\) |
| 4 | \(12\) | \(12\) | \(12\) | \(12\) | \(12\) | \(25/3\) | \(12\) | \(1,1\) |
| 5 | \(15\) | \(12\) | \(15\) | \(15\) | \(15\) | \(23/2\) | \(15\) | \(1,1\) |
| 6 | \(20\) | \(20\) | \(20\) | \(20\) | \(20\) | \(76/5\) | \(20\) | \(2,2\) |
| 7 | \(24\) | \(21\) | \(21\) | \(24\) | \(24\) | \(58/3\) | \(24\) | \(2,2\) |
| 8 | \(30\) | \(30\) | \(30\) | \(30\) | \(30\) | \(170/7\) | \(30\) | \(4,4\) |
| 9 | \(35\) | \(63/2\) | \(36\) | \(36\) | \(36\) | \(59/2\) | \(36\) | \(4,12\) |
| 10 | \(42\) | \(42\) | \(45\) | \(45\) | \(45\) | \(320/9\) | \(45\) | \(24,72\) |
| 11 | \(48\) | \(45\) | \(50\) | \(50\) | \(50\) | \(42\) | \(50\) | \(24,24\) |

Thus \(\max(A_n,H_n)=B_n\) throughout this bounded table. The equality is a
finite exact comparison with the already enumerated \(B_n\) values, not an
all-\(n\) formula. The \(L_n\) values happen to be below both \(Q_n\) and
\(H_n\) in every displayed admissible case, but only \(Q_n,H_n\) are proved
to lower-bound \(B_n\); \(L_n\) remains a full-distance obstruction as stated
in (TT18).

Thus the bounded regression agrees with the all-\(n\) theorem: the first exact
gap between the adjacent relaxation and the full surrogate occurs at \(n=9\):

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

## Global Distance-Two Saturation

By definition, \(B_n=W_n^{(\le2)}\), and restriction of the pair set gives
\(B_n\le W_n\). The bounded exhaustive table proves

\[
(B_3,\dots,B_{11})
=
(W_3,\dots,W_{11})
=
(6,12,15,20,24,30,36,45,50).
\]

Independently, the residue-class squeezes summarized in (RC5) prove
\(B_n=W_n\) for every \(n\ge9\): residues zero, three, and four use the
matching endpoints \(H_n=T_n\), residue one uses the order
\(\sigma_n^{(1)}\), and residue two uses the saturation bound \(J_n\) and
the order \(\sigma_n^{(2)}\). On the overlap \(n=9,10,11\), the formula gives
\(36,45,50\), exactly matching the table. Since
\([3,11]\cup[9,\infty)=[3,\infty)\), these two exact inputs prove

\[
\boxed{W_n^{(\le2)}=B_n=W_n\qquad(n\ge3)}.
\tag{GC1}
\]

More generally, for every integer \(q\ge2\), monotonicity in the retained
pair set gives

\[
B_n\le W_n^{(\le q)}\le W_n=B_n,
\]

so every such truncated objective has the same optimum value.

This value theorem must be separated from a minimizer-set theorem. Let
\(\mathcal M_n\) and \(\mathcal M_n^{(\le2)}\) be the cyclic orders minimizing
the full and distance-two objectives. If \(\sigma\in\mathcal M_n\), then

\[
B_n
\le W^{(\le2)}(\sigma)
\le W(\sigma)
=W_n
=B_n,
\]

and hence
\(\mathcal M_n\subseteq\mathcal M_n^{(\le2)}\) for every \(n\ge3\).

Every pair omitted from the distance-two objective has circular positional
distance \(q\ge3\). Since its two labels are distinct elements of
\(\{2,\dots,n\}\),

\[
{ij\over q}\le {n(n-1)\over3}.
\tag{MS1}
\]

Consequently,

\[
{n(n-1)\over3}\le B_n
\quad\Longrightarrow\quad
\mathcal M_n=\mathcal M_n^{(\le2)}.
\tag{MS2}
\]

Indeed, if \(\sigma\in\mathcal M_n^{(\le2)}\), its retained-pair maximum is
\(B_n\), while (MS1)--(MS2) bound every omitted pair by \(B_n\). Thus
\(W(\sigma)=B_n=W_n\), where the last equality is (GC1), and the reverse
inclusion follows. The forward inclusion was proved above.

It remains to evaluate (MS2) exactly. For \(n=5k+r\ge9\), define

\[
\Delta_r(k)=3B_n-n(n-1).
\tag{MS3}
\]

The exact residue-class formula (RC5) gives:

| \(r\) | \(d_n\) | \(B_n\) | \(\Delta_r(k)\) | \(k\)-range for \(9\le n\le92\) | endpoint values |
|---:|---:|---:|---:|---:|---:|
| 0 | \(4k+2\) | \(8k^2+6k+1\) | \(-k^2+23k+3\) | \(2\le k\le18\) | \(45,93\) |
| 1 | \(4k+3\) | \(8k^2+8k+2\) | \(-k^2+19k+6\) | \(2\le k\le18\) | \(40,24\) |
| 2 | \(4k+4\) | \(8k^2+12k+4\) | \(-k^2+21k+10\) | \(2\le k\le18\) | \(48,64\) |
| 3 | \(4k+4\) | \(8k^2+14k+6\) | \(-k^2+17k+12\) | \(2\le k\le17\) | \(42,12\) |
| 4 | \(4k+5\) | \(8k^2+18k+10\) | \(-k^2+19k+18\) | \(1\le k\le17\) | \(36,52\) |

Each quadratic is concave, so its minimum on the displayed integer interval
occurs at an endpoint. Every listed endpoint value is positive. For
\(3\le n\le8\), the exact values
\((B_3,\dots,B_8)=(6,12,15,20,24,30)\) instead give

\[
(3B_n-n(n-1))_{n=3}^8=(12,24,25,30,30,34).
\tag{MS4}
\]

Therefore (MS2) proves the exact initial range

\[
\boxed{
\mathcal M_n=\mathcal M_n^{(\le2)}
\qquad(3\le n\le92)
}.
\tag{MS5}
\]

The next index is \(93=5\cdot18+3\). Here \(d_{93}=76\), and (RC5) gives

\[
B_{93}=W_{93}={76\cdot75\over2}=2850,
\qquad
{93\cdot92\over3}=2852.
\tag{MS6}
\]

The failure of (MS2) does not by itself prove strict inclusion, so an explicit
witness is needed. Start from the already proved search-free order
\(\sigma_{93}=\operatorname{eight\_twenty\_fifths\_order}(93)\). It contains
the oriented fragments

\[
\ldots,86,16,48,15,\ldots,92,4,54,3,93,\ldots .
\]

Delete label \(54\) from the second fragment and insert it between \(16\) and
\(48\), preserving the cyclic order of every other label. Call the result
\(\tau_{93}\); its two changed fragments are

\[
\ldots,86,16,54,48,15,\ldots,92,4,3,93,\ldots .
\]

The base order has full score \(2850\). The only new adjacent scores are

\[
16\cdot54=864,
\qquad54\cdot48=2592,
\qquad4\cdot3=12,
\]

and the only new distance-two scores are

\[
{86\cdot54\over2}=2322,
\quad {16\cdot48\over2}=384,
\quad {54\cdot15\over2}=405,
\quad {92\cdot3\over2}=138,
\quad {4\cdot93\over2}=186.
\]

All are below \(2850\). The unaffected pairs \((38,75)\) at distance one and
\((75,76)\) at distance two still attain \(2850\), so
\(W^{(\le2)}(\tau_{93})=2850=B_{93}\). On the other hand, the second changed
fragment places \((92,93)\) at distance three, and hence

\[
{92\cdot93\over3}=2852.
\]

By (MS1), no pair at distance at least three can exceed \(2852\). Therefore

\[
W^{(\le2)}(\tau_{93})=2850,
\qquad
W(\tau_{93})=2852,
\qquad
\boxed{\mathcal M_{93}\subsetneq\mathcal M_{93}^{(\le2)}}.
\tag{MS7}
\]

Equations (MS5) and (MS7) prove that \(93\) is the first restriction index.
No persistence for every later \(n\) is asserted: the sufficient criterion
(MS2), for example, holds again at \(n=94\).

## One-Triple Reversal Obstruction

We now analyze one explicit parametric perturbation of the symbolic
eight-twenty-fifths construction. Restrict to the infinite subsequence

\[
n=10m+3,
\qquad
m\ge3,
\qquad
d=8m+4,
\qquad
T={d(d-1)\over2}.
\tag{PT1}
\]

This is the residue-three branch of (UC3)--(UC11), with
\(v=2m\), \(e=4\), \(t=m+1\), \(\varepsilon=0\), and
\(r=m-1\). Its triple middle paths are

\[
P_s=(A_s,c_s,B_s)
=
(d-1-2s,\ 4m+2+s,\ d-2-2s),
\qquad 0\le s\le m.
\tag{PT2}
\]

For one selected parameter \(s\in\{0,\ldots,m\}\), define
\(\tau_{m,s}\) by the single local replacement

\[
P_s=(A_s,c_s,B_s)
\longmapsto
P_s^{\rm rev}=(B_s,c_s,A_s),
\tag{PT3}
\]

leaving every other entry of \(\sigma_n\) fixed. This is a search-free
permutation of \(\{2,\ldots,n\}\). We determine its full-distance score
exactly.

### Adjacencies

In the local word

\[
E_s,\lambda_s,A_s,c_s,B_s,\rho_{s+1},E_{s+1},
\]

the two internal products are merely exchanged. The boundary product
\(\lambda_sA_s\) decreases to \(\lambda_sB_s\), while

\[
A_s\rho_{s+1}
\le(d-1)(4m-1)
<T.
\]

All other adjacencies retain the bounds in (UC12)--(UC15). Moreover,
\(c_0=4m+2\) remains adjacent to \(A_0=d-1\), even when \(s=0\), and

\[
c_0A_0=(4m+2)(8m+3)=T.
\]

Thus the adjacent score is exactly

\[
M_1(\tau_{m,s})=T
\qquad(0\le s\le m).
\tag{PT4}
\]

This persistent pair is already an exact obstruction to a strict improvement
below \(T\) anywhere in the selected family.

### Positional distance two

Only two terminal--middle distance-two pairs can change. The pair
\(E_sA_s\) is replaced by the smaller \(E_sB_s\), while
\(B_sE_{s+1}\) is replaced by \(A_sE_{s+1}\). The latter is the sole
potential increase. Exact subtraction gives

\[
\begin{aligned}
d(d-1)-A_sE_{s+1}
&=d(d-1)-(d-1-2s)(d+s+1)\\
&=(s-1)d+(s+1)(2s+1).
\end{aligned}
\tag{PT5}
\]

At \(s=0\), the right side is \(-(d-1)\), and the new pair is
\((A_0,E_1)=(d-1,d+1)\). For every \(s\ge1\), the right side is
positive. When \(s\ge1\), the unchanged pair \((d,d-1)\) in \(P_0\)
still has positional distance two and score \(T\). Therefore

\[
M_2(\tau_{m,s})
=
\begin{cases}
(d^2-1)/2=T+(d-1)/2,&s=0,\\
T,&1\le s\le m.
\end{cases}
\tag{PT6}
\]

### Distances three and at least four

The reversal changes no terminal position and no terminal-gap length.
In a triple block, a distance-three pair with no low endpoint is
\(c_jE_j\) or \(c_jE_{j+1}\). The latter products increase with \(j\) and
are largest at \(j=m\). Every other distance-three pair, including every
one in or across a singleton block, has one endpoint at most
\(\rho_0=4m+1\). The candidate
\((c_m,E_{m+1})=(5m+2,9m+5)\) dominates that whole class because

\[
(5m+2)(9m+5)-n(4m+1)=5m^2+21m+7>0.
\]

The connector positions do not change under any reversal, so the maximum is
exactly

\[
M_3(\tau_{m,s})={(5m+2)(9m+5)\over3}<T,
\tag{PT7}
\]

because
\(3T-(5m+2)(9m+5)=51m^2+41m+8>0\). For every positional distance
\(q\ge4\),

\[
{ij\over q}\le {n(n-1)\over4}<T,
\tag{PT8}
\]

where

\[
4T-n(n-1)=28m^2+62m+18>0.
\]

The first inequality in (PT8) is attained. Since \(m\ge3\), the untouched
singleton gap between \(E_{2m-2}=n-1\) and \(E_{2m-1}=n\) is

\[
n-1,\ 4,\ 6m,\ 3,\ n.
\]

Thus

\[
M_{\ge4}(\tau_{m,s})={n(n-1)\over4}<T.
\tag{PT9}
\]

### Cyclic closure

For the cut immediately before \(E_0=d\), none of the reversed triples
meets the final singleton block. The local closing word is

\[
\ldots,n,2,6m+1,4m+1
\mathbin{|}
d,4m,x_s,\ldots,
\qquad
x_s=d-1-\mathbf1_{\{s=0\}}.
\tag{PT10}
\]

Directly checking the one, two, and three pairs crossing this cut gives the
exact closing maxima

\[
\begin{aligned}
C_1&=(4m+1)d,\\
C_2&={(6m+1)d\over2},\\
C_3&={(4m+1)(d-1-\mathbf1_{\{s=0\}})\over3}.
\end{aligned}
\tag{PT11}
\]

For distance three the three raw candidates are
\(2d\), \(4m(6m+1)\), and
\((4m+1)(d-1-\mathbf1_{\{s=0\}})\). The last is largest; even in the
smaller \(s=0\) case its excess over the second is
\(8m^2+12m+2>0\).

They are all strictly below \(T\). For example,

\[
T-C_1=4m+2,
\qquad
T-C_2=(4m+2)(2m+2),
\]

and replacing the indicator in \(C_3\) by zero still gives

\[
3T-(4m+1)(d-1)=64m^2+64m+15>0.
\tag{PT12}
\]

All longer closing arcs are already covered by (PT8)--(PT9). Hence the
linear presentation loses no cyclic pair.

### Exact score and obstruction

Combining (PT4), (PT6), (PT7), (PT9), and (PT11) proves the full-distance
formula

\[
\boxed{
W(\tau_{m,s})
=
\begin{cases}
(d^2-1)/2=T+(d-1)/2,&s=0,\\
T,&1\le s\le m.
\end{cases}}
\tag{PT13}
\]

The case \(s=0\) is a reproducible counterexample to the tempting stronger
claim that every triple reversal preserves \(T\). At the first admitted row
\((m,n,d)=(3,33,28)\), the pair \((27,29)\) has distance two and gives

\[
W(\tau_{3,0})={783\over2}>378=T.
\tag{PT14}
\]

For every choice of parameters \(s=s(m)\), including choices that vary with
\(m\), (PT13) gives uniformly

\[
{W(\tau_{m,s(m)})\over(10m+3)^2}
\longrightarrow {8\over25}.
\tag{PT15}
\]

This is an **EXACT FAMILY-SPECIFIC OBSTRUCTION**: a one-triple reversal never
lowers the finite threshold \(T\), and it cannot lower the asymptotic
product-distance coefficient below \(8/25\). The conclusion is about the
surrogate \(W\). Applying the established regular-direction construction and
radius-one insertion theorem gives only the subsequent geometric upper bound

\[
R_2^*(10m+3)
\le{(10m+2)W(\tau_{m,s})\over\pi}.
\tag{PT16}
\]

For \(s\ge1\), (PT16) merely reproduces the existing upper bound on this
subsequence; for \(s=0\), it is weaker. It neither identifies a fixed-order
geometric threshold nor obstructs improvement by non-regular geometric
configurations.

## One-Gap Nonlocal Middle-Path Rotation Obstruction

We now fix one nonlocal reassignment of whole middle paths. The
transformation is chosen before direct scoring and has no search parameter.
Retain the residue-three parameters

\[
n=10m+3,
\qquad
m\ge3,
\qquad
d=8m+4,
\qquad
T={d(d-1)\over2},
\qquad
v=2m.
\tag{NR1}
\]

For \(0\le k\le m\), write

\[
P_k=(A_k,c_k,B_k)
=(d-1-2k,\ 4m+2+k,\ d-2-2k),
\tag{NR2}
\]

and, for \(m+1\le k\le2m-1\), write

\[
P_k=(x_k),
\qquad
x_k=4m+2+k.
\tag{NR3}
\]

The terminal and low labels remain

\[
E_j=d+j,
\qquad
\lambda_j=4m-2j,
\qquad
\rho_j=4m+1-2j
\qquad(0\le j<2m).
\tag{NR4}
\]

In the original order, the oriented terminal gap \(G_j\) contains \(P_j\).
Define \(\widehat\sigma_m\) by the single deterministic rule

\[
\boxed{
G_j^{\rm rot}
=
(E_j,\lambda_j,P_{j+1\bmod2m},\rho_{j+1},E_{j+1})
}
\qquad(0\le j<2m),
\tag{NR5}
\]

with all subscripts cyclic. Thus every oriented path moves to the preceding
terminal gap, while \(P_0\) moves to the canonical closing gap
\(G_{2m-1}\). No other reassignment is considered here.

### Permutation property

The low labels in (NR4) are exactly \([2,4m+1]\). The remaining displayed
families give the disjoint consecutive intervals

\[
\begin{array}{c|c}
\text{labels}&\text{source}\\ \hline
[4m+2,5m+2]&c_0,\ldots,c_m\\
[5m+3,6m+1]&x_{m+1},\ldots,x_{2m-1}\\
[6m+2,d-1]&A_0,B_0,\ldots,A_m,B_m\\
[d,n]&E_0,\ldots,E_{2m-1}.
\end{array}
\tag{NR6}
\]

They partition \(\{2,\ldots,n\}\). Since
\(j\mapsto j+1\pmod{2m}\) is a bijection, (NR5) uses every whole middle
path exactly once and changes no other label. Hence
\(\widehat\sigma_m\) is a permutation of \(\{2,\ldots,n\}\) for every
\(m\ge3\).

### Pairs at positional distance one

The terminal--low edges are unchanged. The larger product incident to
\(E_j\) is

\[
f_j=(d+j)(4m+1-2j),
\qquad
f_{j+1}-f_j=-12m-9-4j<0
\qquad(0\le j\le2m-2).
\tag{NR7}
\]

Consequently their maximum is

\[
f_0=d(4m+1)=T-(4m+2)<T.
\tag{NR8}
\]

Every low--middle edge is at most
\((4m+1)(d-1)<T\). Within a triple,

\[
A_kc_k=T-k(2k+1),
\qquad
B_kc_k<A_kc_k.
\tag{NR9}
\]

Therefore the exact adjacent maximum is

\[
\boxed{M_1(\widehat\sigma_m)=T},
\tag{NR10}
\]

and its unique unordered maximizing pair is

\[
\boxed{\{A_0,c_0\}=\{d-1,4m+2\}}.
\tag{NR11}
\]

### Pairs at positional distance two

Every terminal gap contains a low, a nonempty middle path, and another low,
so no two terminals are at distance two. A distance-two pair with no terminal
has product at most \((d-1)(d-2)\). A pair with a terminal has product at
most \(n(d-1)\), and equality can occur only for the unique two largest
eligible labels \(n\) and \(d-1\). The closing gap in (NR5) begins

\[
E_{2m-1},\lambda_{2m-1},P_0
=(n,2,A_0,c_0,B_0),
\tag{NR12}
\]

so that equality really occurs at distance two. Hence

\[
\boxed{
M_2(\widehat\sigma_m)
={n(d-1)\over2}
={(10m+3)(8m+3)\over2}
},
\tag{NR13}
\]

with the unique maximizing pair

\[
\boxed{\{n,A_0\}=\{10m+3,8m+3\}}.
\tag{NR14}
\]

In particular,

\[
M_2(\widehat\sigma_m)-T
={(2m-1)(8m+3)\over2}>0.
\tag{NR15}
\]

### Pairs at positional distance three

Indexing a gap by the path it contains, a triple gap is

\[
E_{k-1},\lambda_{k-1},A_k,c_k,B_k,\rho_k,E_k,
\tag{NR16}
\]

and a singleton gap is

\[
E_{k-1},\lambda_{k-1},x_k,\rho_k,E_k.
\tag{NR17}
\]

Here \(k=0\) is interpreted cyclically. In (NR16), the only
distance-three pair forms, including those entering the next gap, are

\[
\begin{gathered}
E_{k-1}c_k,\quad \lambda_{k-1}B_k,\quad A_k\rho_k,\quad
c_kE_k,\quad B_k\lambda_k,\quad
\rho_k\operatorname{first}(P_{k+1})
\end{gathered}
\tag{NR18}
\]

for a triple, and

\[
E_{k-1}\rho_k,\quad \lambda_{k-1}E_k,\quad
x_k\lambda_k,\quad \rho_k\operatorname{first}(P_{k+1})
\tag{NR19}
\]

for a singleton. Thus the only distance-three pairs with no low endpoint are
\(E_{k-1}c_k\) and \(c_kE_k\). The two lists contain
\[
6(m+1)+4(m-1)=10m+2
\]
starts, exactly the core length. Since \(10m+2>6\), each unordered
distance-three pair has one forward orientation in the lists; none is
omitted or duplicated.

For \(1\le k\le m\), the products

\[
c_kE_k=(4m+2+k)(d+k)
\tag{NR20}
\]

increase strictly with \(k\), and \(E_{k-1}c_k<c_kE_k\). Put

\[
R=(5m+2)(9m+4)=c_mE_m.
\tag{NR21}
\]

The cyclic \(k=0\) candidate and the two remaining classes are all strictly
smaller, because

\[
\begin{aligned}
R-nc_0&=5m^2+6m+2,\\
R-2mn&=25m^2+32m+8,\\
R-(4m+1)(d-1)&=13m^2+18m+5.
\end{aligned}
\tag{NR22}
\]

The second line covers the terminal--low pairs in singleton gaps; the third
covers every remaining low--nonterminal pair. Thus

\[
\boxed{
M_3(\widehat\sigma_m)
={(5m+2)(9m+4)\over3}
},
\tag{NR23}
\]

with the unique maximizing pair

\[
\boxed{\{c_m,E_m\}=\{5m+2,9m+4\}}.
\tag{NR24}
\]

It lies strictly below the old threshold, since

\[
3T-(5m+2)(9m+4)=51m^2+46m+10>0.
\tag{NR25}
\]

### Distances at least four

For every pair at positional distance \(q\ge4\),

\[
{ij\over q}\le{n(n-1)\over4}.
\tag{NR26}
\]

The gap preceding \(n\) is now the singleton gap

\[
G_{2m-2}^{\rm rot}=(n-1,4,6m+1,3,n),
\tag{NR27}
\]

so the pair \(\{n-1,n\}\) has distance exactly four. Its complementary
arc has length \(10m-2>4\). Equality in (NR26) requires both this label pair
and \(q=4\), proving

\[
\boxed{
M_{\ge4}(\widehat\sigma_m)
={n(n-1)\over4}
},
\tag{NR28}
\]

with unique maximizing pair \(\{n-1,n\}\). Moreover,

\[
4T-n(n-1)=28m^2+62m+18>0.
\tag{NR29}
\]

### Canonical cut

Cut immediately before \(E_0=d\). The closing and opening words are

\[
\ldots,n,2,A_0,c_0,B_0,\rho_0
\mathbin{|}
E_0,\lambda_0,A_1,c_1,B_1,\rho_1,\ldots .
\tag{NR30}
\]

Listing the one-, two-, and three-step pairs crossing this cut gives the
exact maxima

\[
\boxed{
\begin{aligned}
C_1&=(4m+1)d
&&\text{on }\{\rho_0,E_0\},\\
C_2&={d(d-2)\over2}
&&\text{on }\{B_0,E_0\},\\
C_3&={d(4m+2)\over3}={d^2\over6}
&&\text{on }\{c_0,E_0\}.
\end{aligned}}
\tag{NR31}
\]

Each maximizing pair is unique within its closing distance class. In
particular,

\[
C_1=C_2=T-(4m+2)<T,
\qquad
C_3<T.
\tag{NR32}
\]

For the next three closing distances, direct listing gives

\[
\begin{aligned}
C_4&={d(d-1)\over4}
&&\text{on }\{A_0,E_0\},\\
C_5&={(d-2)(4m+3)\over5}={d^2-4\over10}
&&\text{on }\{B_0,c_1\},\\
C_6&={dn\over6}
&&\text{on }\{n,E_0\}.
\end{aligned}
\tag{NR33}
\]

These maxima are unique. Furthermore,

\[
C_4-C_5={3d^2-5d+8\over20}>0,
\qquad
C_4-C_6={d(4m+3)\over12}>0.
\tag{NR34}
\]

For every longer closing arc,

\[
{ij\over q}\le{n(n-1)\over7}
<{d(d-1)\over4},
\qquad q\ge7,
\tag{NR35}
\]

because

\[
7d(d-1)-4n(n-1)=48m^2+192m+60>0.
\tag{NR36}
\]

Hence the exact long-closing maximum is

\[
\boxed{
C_{\ge4}={d(d-1)\over4}={T\over2}
},
\tag{NR37}
\]

uniquely on \(\{d-1,d\}\) at distance four. Thus the linear presentation
has lost no cyclic pair in any distance class.

### Exact score and obstruction

The complete class table is

\[
\begin{array}{c|c|c}
\text{distance}&\text{exact maximum}&\text{unique maximizing pair}\\ \hline
1&T&\{d-1,4m+2\}\\
2&n(d-1)/2&\{n,d-1\}\\
3&(5m+2)(9m+4)/3&\{5m+2,9m+4\}\\
\ge4&n(n-1)/4&\{n-1,n\}.
\end{array}
\tag{NR38}
\]

Equations (NR15), (NR25), and (NR29) therefore prove

\[
\boxed{
W(\widehat\sigma_m)
={n(d-1)\over2}
={(10m+3)(8m+3)\over2}
}
\qquad(m\ge3),
\tag{NR39}
\]

and the only full-score saturating pair is

\[
\boxed{\{n,d-1\}}
\tag{NR40}
\]

at positional distance two. The exact symbolic obstruction is the forced
word \(n,2,d-1\) in (NR12): moving \(P_0\) across the canonical cut places
the largest terminal two steps from the largest middle label. Consequently,

\[
{W(\widehat\sigma_m)\over(10m+3)^2}
={8m+3\over2(10m+3)}
\longrightarrow {2\over5}
>{8\over25}.
\tag{NR41}
\]

Thus this one nonlocal reassignment is not merely non-improving: its
product-distance coefficient is worse by \(2/25\). The persistent adjacent
pair in (NR11) still attains \(T\), but it is no longer a full-score
saturator.

The already proved regular-direction implication supplies only the redundant
upper bound

\[
R_2^*(10m+3)
\le{(10m+2)W(\widehat\sigma_m)\over\pi}.
\tag{NR42}
\]

Because (NR41) is weaker than both the regular-direction \(8/(25\pi)\)
construction and its later \(143/(500\pi)\) shortcut refinement, no new
geometric consequence follows. In particular, this family-specific
surrogate obstruction is not a geometric lower bound and says nothing about
other orders, unequal directions, or non-regular configurations.

## Distinguished-Path Terminal-Gap Necessity

We now allow an arbitrary reassignment of complete middle paths, but derive
only a necessary local condition on the location of the distinguished path
\(P_0\). No reassignment is selected or scored. Let

\[
\alpha:\{0,\ldots,2m-1\}\longrightarrow\{0,\ldots,2m-1\}
\tag{PG1}
\]

be a bijection, where terminal gap \(G_j\) receives the unchanged oriented
path \(P_{\alpha(j)}\). Put \(v=2m\) and
\(j^+=j+1\pmod v\). The corresponding gap word is

\[
G_j^\alpha
=
(E_j,\lambda_j,P_{\alpha(j)},\rho_{j^+},E_{j^+}).
\tag{PG2}
\]

Write \(\sigma_\alpha\) for the cyclic core order obtained by expanding all
paths in (PG2) and identifying the shared terminal \(E_{j^+}\) with the
initial terminal of the next gap. Thus every terminal, low label, and middle
path occurs exactly as in the retained scaffold, with only the path-to-gap
bijection changed.

All terminal and low labels retain (NR4), and every path retains (NR2)--(NR3)
with its displayed orientation. Since the core has
\(n-1=10m+2\ge32\) positions, every one- or two-step arc used below is the
smaller cyclic distance, including across the canonical cut.

Suppose \(\alpha(j)=0\), and abbreviate

\[
A=A_0=d-1,
\qquad
c=c_0=4m+2={d\over2},
\qquad
B=B_0=d-2.
\tag{PG3}
\]

The complete local word is then

\[
Q_j=(E_j,\lambda_j,A,c,B,\rho_{j^+},E_{j^+}).
\tag{PG4}
\]

The placement-dependent adjacent pairs are
\(\lambda_jA,Ac,cB,B\rho_{j^+}\). The unchanged terminal--low scaffold
edges are already bounded by (NR7)--(NR8). Uniformly in \(j\),

\[
\begin{aligned}
\lambda_jA&\le4mA=T-2A,\\
Ac&=T,\\
cB&=T-c,\\
B\rho_{j^+}&\le B(4m+1)=T-(12m+4).
\end{aligned}
\tag{PG5}
\]

Thus insertion of \(P_0\) causes no adjacent violation in any gap. Its exact
local adjacent maximum is \(T\), uniquely on \(\{A,c\}\). In particular,
every whole-path reassignment preserving this path and its orientation has
full score at least \(T\).

At distance two, every pair without a terminal endpoint has product at most
\((d-1)(d-2)<d(d-1)=2T\). This also covers the unchanged scaffold pair
\(\rho_j\lambda_j\) across \(E_j\). Hence the only potentially restrictive
distance-two pairs caused by placing \(P_0\) in \(G_j\) are its two terminal
pairs. Their exact scores are

\[
L_j:={E_jA\over2}
=T+{j(d-1)\over2},
\tag{PG6}
\]

and

\[
R_j:={BE_{j^+}\over2}
=
\begin{cases}
T+\dfrac{j(d-2)-2}{2}
=T+j(4m+1)-1,
&0\le j\le2m-2,\\[6pt]
T-\dfrac d2,
&j=2m-1.
\end{cases}
\tag{PG7}
\]

The second line is genuinely cyclic: when \(j=2m-1\), the right terminal is
\(E_{j^+}=E_0=d\), not the nonexistent label \(E_{2m}\). Since
\(d-2=8m+2\ge26\), (PG6)--(PG7) give the exact one-sided conditions

\[
L_j\le T\quad\Longleftrightarrow\quad j=0,
\qquad
R_j\le T\quad\Longleftrightarrow\quad
j\in\{0,2m-1\}.
\tag{PG8}
\]

Moreover, \(L_j\) is the unique local distance-two maximum. Indeed, for a
nonclosing gap,

\[
E_jA-BE_{j+1}=j+2>0
\qquad(0\le j\le2m-2),
\tag{PG9}
\]

while at the closing gap

\[
nA-Bd=d+(2m-1)(d-1)>0.
\tag{PG10}
\]

All remaining distance-two products are nonterminal and were bounded above.
Consequently

\[
\boxed{
M^{\rm loc}_1(j)=T,
\qquad
M^{\rm loc}_2(j)
=T+{j(d-1)\over2}
}
\tag{PG11}
\]

with unique maximizers \(\{A,c\}\) and \(\{E_j,A\}\), respectively.

The boundary cases are explicit. At \(j=0\),

\[
L_0=T,
\qquad
R_0=T-1.
\tag{PG12}
\]

For every \(1\le j\le2m-2\), including the former triple/singleton
transition indices \(j=m-1,m,m+1\) whenever displayed, both terminal scores
are strictly above \(T\). At the closing index, the literal cyclic word is

\[
Q_{2m-1}
=(n,2,d-1,4m+2,d-2,4m+1,d),
\tag{PG13}
\]

and

\[
L_{2m-1}
=T+{(2m-1)(d-1)\over2}>T,
\qquad
R_{2m-1}=T-{d\over2}<T.
\tag{PG14}
\]

Thus the wrap repairs the right terminal inequality but retains the exact
left-hand word \(n,2,d-1\) from (NR12). At the smallest admitted parameter
\(m=3\), the indices are \(0,\ldots,5\): (PG12) covers \(G_0\), the
nonclosing range \(G_1,\ldots,G_4\) has two strict violations per gap, and
\(G_5\) is excluded by (PG14). Hence no endpoint or minimum-parameter case
is omitted.

We have proved the following **EXACT NECESSARY PLACEMENT THEOREM**:

\[
\boxed{
W^{(\le2)}(\sigma_\alpha)\le T
\quad\Longrightarrow\quad
\alpha(0)=0.
}
\tag{PG15}
\]

Equivalently, \(G_1,\ldots,G_{2m-1}\) are locally excluded for \(P_0\),
while \(G_0\) is the unique gap not excluded by the distance-one and
distance-two inequalities involving \(P_0\). The converse is deliberately
only local: placing \(P_0\) in \(G_0\) proves none of the constraints
involving the remaining reassigned paths and does not prove that a prescribed
partial reassignment extends to a full one. The canonical identity assignment
from (UC11) is a separately proved complete witness with \(P_0\subset G_0\);
the present theorem neither constructs nor establishes any nonidentity
reassignment. If a full reassignment with \(W\le T\) does exist, (PG5) also
forces its score to equal \(T\).

### Generic-path local relation

We now extend only the local calculation behind (PG15), without selecting or
scoring a complete reassignment. For every path index \(0\le k<2m\) and gap
index \(0\le j<2m\), let

\[
Q_{k,j}=(E_j,\lambda_j,P_k,\rho_{j^+},E_{j^+})
\tag{PG16}
\]

be the constant-size word obtained by inserting the retained oriented path
\(P_k\) in \(G_j\). Call \((k,j)\) **locally non-excluded** when every pair at
positional distance one or two determined by this single word has score at
most \(T\); otherwise call it **locally excluded**. The unchanged pairs across
a terminal are safe independently of \(k,j\), since

\[
E_i\rho_i\le d(4m+1)=T-{d\over2}<T,
\qquad
{\rho_i\lambda_i\over2}<T.
\tag{PG17}
\]

Thus (PG16), together with (PG17), accounts for every local pair at the two
requested distances.

#### Triple paths

Fix \(0\le k\le m\) and retain

\[
A_k=d-1-2k,
\qquad
c_k={d\over2}+k,
\qquad
B_k=A_k-1.
\tag{PG18}
\]

Because \(c_k>\lambda_j,\rho_{j^+}\) and
\(A_k>B_k>c_k\) throughout the stated domain, the path-bearing adjacent
maximum is \(A_kc_k\). More precisely, the complete adjacent maximum in
\(Q_{k,j}\) is

\[
M^{\rm tr}_1(k,j)
=\max\{E_j\lambda_j,E_{j^+}\rho_{j^+},A_kc_k\},
\qquad
A_kc_k=T-k(2k+1),
\tag{PG19}
\]

and each entry in the maximum is at most \(T\). The other path-bearing
adjacencies are strictly dominated by \(A_kc_k\). Hence distance one excludes
no triple/gap pair; equality in (PG19) occurs for \(k=0\), while every
\(k>0\) is strict.

The five distance-two pairs in (PG16) are

\[
{E_jA_k\over2},\quad
{\lambda_jc_k\over2},\quad
{A_kB_k\over2},\quad
{c_k\rho_{j^+}\over2},\quad
{B_kE_{j^+}\over2}.
\tag{PG20}
\]

The left terminal score strictly dominates the three nonterminal scores. It
also dominates the right terminal score. For a nonclosing gap,

\[
E_jA_k-B_kE_{j+1}=j+2k+2>0
\qquad(0\le j\le2m-2),
\tag{PG21}
\]

whereas the literal closing word and difference are

\[
Q_{k,2m-1}=(n,2,A_k,c_k,B_k,4m+1,d),
\qquad
nA_k-dB_k=(2m-1)A_k+d>0.
\tag{PG22}
\]

Consequently the exact distance-two maximum is unique and equals

\[
\boxed{
M^{\rm tr}_2(k,j)={E_jA_k\over2}
=T+{jA_k-2kd\over2}
}.
\tag{PG23}
\]

For completeness, the right terminal inequality itself is

\[
{B_kE_{j^+}\over2}\le T
\quad\Longleftrightarrow\quad
\begin{cases}
(j+1)B_k\le d(2k+1),&0\le j\le2m-2,\\
\text{always},&j=2m-1.
\end{cases}
\tag{PG24}
\]

It is never more restrictive than (PG23); in particular, cyclic closure
repairs the right side but need not repair the left side. The exact triple
condition is therefore

\[
\boxed{
(k,j)\text{ locally non-excluded}
\quad\Longleftrightarrow\quad
j(d-1-2k)\le2kd.
}
\tag{PG25}
\]

Equivalently, define the row and column cutoffs

\[
\ell_k=
\min\!\left\{2m-1,
\left\lfloor{2kd\over d-1-2k}\right\rfloor\right\},
\qquad
\kappa_j=
\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
\tag{PG26}
\]

Then \(P_k\) is locally non-excluded exactly in
\(G_0,\ldots,G_{\ell_k}\), or, equivalently, \(G_j\) locally permits exactly
the triple indices \(\kappa_j,\ldots,m\). Both descriptions include equality
at the cutoff; that equality is not confined to \((k,j)=(0,0)\). For
example, \((m,k,j)=(34,11,24)\) has
\(jA_k=24\cdot253=6072=2kd\). If \(j>\ell_k\), the explicit excluding witness is
\(\{E_j,A_k\}\) at distance two.

#### Singleton paths

Now fix \(m+1\le k\le2m-1\), so that

\[
P_k=(x_k),
\qquad
x_k={d\over2}+k=4m+2+k.
\tag{PG27}
\]

The exact adjacent maximum and a uniform strict bound are

\[
M^{\rm sing}_1(k,j)
=\max\{E_j\lambda_j,E_{j^+}\rho_{j^+},
x_k\lambda_j,x_k\rho_{j^+}\}<T,
\qquad
(4m+1)x_k\le(4m+1)(6m+1)
=T-(8m^2+18m+5)<T.
\tag{PG28}
\]

The two terminal pairs dominate the intervening low--low pair. Their exact
maximum changes side at the cyclic cut:

\[
\boxed{
M^{\rm sing}_2(k,j)=
\begin{cases}
\dfrac{x_k(d+j+1)}2,&0\le j\le2m-2,\\[5pt]
\dfrac{x_kn}2,&j=2m-1.
\end{cases}}
\tag{PG29}
\]

The right terminal is the unique maximizer in a nonclosing gap, while the
left terminal is the unique maximizer in the closing word
\((n,2,x_k,4m+1,d)\). Uniformly,

\[
d(d-1)-nx_k
\ge d(d-1)-n(6m+1)
=4m^2+28m+9>0.
\tag{PG30}
\]

Thus every singleton is strictly locally non-excluded in every gap.

#### Complete relation, boundaries, and quantifiers

Combining (PG25) and (PG30), the exact local relation is

\[
\boxed{
\mathcal R_{\rm loc}
=\{(k,j):0\le k\le m,\ 0\le j\le\ell_k\}
\mathbin\cup
\{(k,j):m+1\le k\le2m-1,\ 0\le j\le2m-1\}.
}
\tag{PG31}
\]

It has the following explicit extremes and transition indices.

- At \(j=0\), every path is locally non-excluded. For a triple,
  \(M^{\rm tr}_2(k,0)=T-kd\), so (PG15) is recovered by
  \(\ell_0=0\).
- At the last nonclosing gap,

  \[
  Q_{k,2m-2}=(n-1,4,A_k,c_k,B_k,3,n),
  \qquad
  \kappa_{2m-2}
  =\left\lceil{(m-1)(8m+3)\over10m+2}\right\rceil
  =\left\lfloor{4m+1\over5}\right\rfloor.
  \tag{PG32}
  \]

  At the closing gap, (PG22) holds and

  \[
  \kappa_{2m-1}
  =\left\lceil{(2m-1)(8m+3)\over2(10m+3)}\right\rceil
  =\left\lfloor{4m+3\over5}\right\rfloor
  =\left\lceil{4m-1\over5}\right\rceil.
  \tag{PG33}
  \]

  These floor forms follow by the five residue classes of \(m\). Since
  \(\kappa_j\) is nondecreasing, (PG33) is the first triple index locally
  permitted in every gap.
- Around the canonical triple/singleton gap transition, the same column rule
  remains valid without an exceptional branch:

  \[
  \begin{aligned}
  \kappa_{m-1}&=\left\lceil{(m-1)(8m+3)\over2(9m+3)}\right\rceil,\\
  \kappa_m&=\left\lceil{m(8m+3)\over2(9m+4)}\right\rceil,\\
  \kappa_{m+1}&=\left\lceil{(m+1)(8m+3)\over2(9m+5)}\right\rceil.
  \end{aligned}
  \tag{PG34}
  \]

  The path-type transition itself is between
  \(P_m=(6m+3,5m+2,6m+2)\) and \(P_{m+1}=(5m+3)\); both are locally
  non-excluded in every gap. The terminal path
  \(P_{2m-1}=(6m+1)\) is also universal.

At the minimum parameter \(m=3\), one has \(d=28\), \(T=378\), and the
complete relation is

\[
\begin{array}{c|c|c}
k&\text{type}&\text{locally non-excluded gap indices}\\ \hline
0&\text{triple}&\{0\}\\
1&\text{triple}&\{0,1,2\}\\
2&\text{triple}&\{0,1,2,3,4\}\\
3&\text{triple}&\{0,1,2,3,4,5\}\\
4,5&\text{singleton}&\{0,1,2,3,4,5\}.
\end{array}
\tag{PG35}
\]

In particular, \(P_2\) passes the last nonclosing gap with score
\(32\cdot23/2=368<T\), but the cyclic left pair in \(G_5\) has score
\(33\cdot23/2=759/2=T+3/2\). Thus neither the minimum row nor the cyclic
endpoint is hidden by the general cutoff notation.

Finally, the logical levels are separate. For a bijection \(\alpha\) already
given as in (PG1), the local decomposition proves the exact equivalence

\[
W^{(\le2)}(\sigma_\alpha)\le T
\quad\Longleftrightarrow\quad
(\alpha(j),j)\in\mathcal R_{\rm loc}
\quad\text{for every }j.
\tag{PG36}
\]

This does not make a single locally non-excluded pair extendible. Indeed,
\((k,0)\in\mathcal R_{\rm loc}\) for every \(k\), but \(P_0\) has only the
edge \((0,0)\); hence every relation-compatible bijection must use
\((0,0)\), and no \((k,0)\) with \(k>0\) can belong to one. Existence of at
least one relation-compatible bijection is a separate fact supplied by the
already proved canonical identity construction (UC11), not by an arbitrary
edge of (PG31). The local-relation calculation alone neither selects nor
classifies a new bijection; the next subsection addresses that matching
extendibility question separately. At this stage, the local-relation
calculation still leaves every distance-at-least-three pair to be controlled;
the full-score subsection below supplies that control.

### Edge extendibility in the Ferrers relation

We now classify which individual edges of (PG31) occur in at least one
relation-compatible bijection. This is a matching question inside
\(\mathcal R_{\rm loc}\) only. In particular, the bijections constructed
below are not scored at distances at least three in this subsection.

Put \(v=2m\), and extend the triple row cutoffs by

\[
L_k=
\begin{cases}
\ell_k,&0\le k\le m,\\
v-1,&m+1\le k\le v-1.
\end{cases}
\tag{PG37}
\]

Then (PG26)--(PG31) give the two equivalent Ferrers descriptions

\[
(k,j)\in\mathcal R_{\rm loc}
\quad\Longleftrightarrow\quad
j\le L_k
\quad\Longleftrightarrow\quad
k\ge\kappa_j,
\qquad
N(G_j)=\{P_{\kappa_j},\ldots,P_{v-1}\}.
\tag{PG38}
\]

The column thresholds have the precise elementary properties needed below.
Writing

\[
h_j={j(d-1)\over2(d+j)},
\qquad
\kappa_j=\lceil h_j\rceil,
\]

one has

\[
h_{j+1}-h_j
={d(d-1)\over2(d+j)(d+j+1)}>0,
\qquad
\kappa_0=0,
\qquad
\kappa_1=1.
\tag{PG39}
\]

Moreover, for \(2\le r\le v-1\),

\[
2(d+r)(r-1)-r(d-1)
=d(r-2)+2r^2-r>0,
\]

and hence

\[
1\le\kappa_r\le r-1
\quad(2\le r\le v-1),
\qquad
\kappa_{v-1}=\left\lfloor{4m+3\over5}\right\rfloor\le m.
\tag{PG40}
\]

Thus the identity is relation-compatible, every nonterminal positive-index
row has one unit of rightward Ferrers slack, and \(P_0\) has the sole
neighbor \(G_0\).

Call a local edge \((k,j)\) **extendible** if there is a bijection
\(\alpha:\{0,\ldots,v-1\}\to\{0,\ldots,v-1\}\) such that

\[
\alpha(j)=k,
\qquad
(\alpha(i),i)\in\mathcal R_{\rm loc}
\quad(0\le i<v).
\tag{PG41}
\]

Hall's condition can be evaluated exactly after fixing the edge. Delete
\(G_j\) and \(P_k\), let \(S\) be a nonempty set of residual gaps, and put
\(r=\min S\). The nested column neighborhoods in (PG38) give

\[
|N_{k,j}(S)|
=v-\kappa_r-\mathbf1_{\{k\ge\kappa_r\}},
\qquad
|S|\le v-r-\mathbf1_{\{j>r\}}.
\tag{PG42}
\]

For each fixed \(r\ne j\), the largest residual set with minimum \(r\) is
the corresponding suffix with \(G_j\) removed. Therefore residual Hall is
equivalent to

\[
\kappa_r+\mathbf1_{\{k\ge\kappa_r\}}
\le r+\mathbf1_{\{j>r\}}
\qquad(r\ne j).
\tag{PG43}
\]

Suppose first that \(j\ge1\) and \((k,j)\) is local. If \(r<j\),
monotonicity gives \(k\ge\kappa_j\ge\kappa_r\), and (PG43) reduces to
\(\kappa_r+1\le r+1\). If \(r>j\), then \(r\ge2\), and (PG40) gives
\(\kappa_r+\mathbf1_{\{k\ge\kappa_r\}}\le(r-1)+1=r\). Thus every local
edge in a positive gap passes residual Hall. The edge \((0,0)\) also passes:
for every residual \(r\ge1\), (PG39)--(PG40) give \(0<\kappa_r\), so the
indicator in (PG43) vanishes. In contrast, if \(j=0\) and \(k>0\), then \(r=1\)
gives \(\kappa_1+1=2>1\). Equivalently, after removing \(P_k\), the
\(v-1\) gaps \(G_1,\ldots,G_{v-1}\) have only the \(v-2\) neighbors
\(P_1,\ldots,P_{v-1}\) other than \(P_k\). This is the exact Hall
obstruction forced by \(N(P_0)=\{G_0\}\).

For existence we give explicit witnesses rather than invoke Hall
nonconstructively. If \(1\le j<k\), rotate the index interval
\([j,k]\) by setting

\[
\alpha_{k,j}(i)=
\begin{cases}
k,&i=j,\\
i-1,&j<i\le k,\\
i,&\text{otherwise}.
\end{cases}
\tag{PG44}
\]

This is a bijection and contains \((k,j)\). Its only nonidentity edges other
than the prescribed one are \((p,p+1)\), \(j\le p<k\). Here \(p\ge1\),
and (PG40) gives \(\kappa_{p+1}\le p\), so every such edge is local.

If \(j=k\), use the identity

\[
\alpha_{k,k}(i)=i.
\tag{PG45}
\]

Finally, if \(j>k\), locality implies
\(k\ge\kappa_j\ge1\). Rotate \([k,j]\) in the opposite direction:

\[
\alpha_{k,j}(i)=
\begin{cases}
i+1,&k\le i<j,\\
k,&i=j,\\
i,&\text{otherwise}.
\end{cases}
\tag{PG46}
\]

The added edges are \((p,p-1)\), \(k+1\le p\le j\), and they are local
because \(\kappa_{p-1}\le p-1<p\). Each construction fixes
\(\alpha(0)=0\); no shift crosses the canonical cut.

The constructions also expose every boundary explicitly. When (PG44)
crosses the path-type boundary, its only new triple-to-singleton-boundary
edge is \((m,m+1)\), valid because \(\kappa_{m+1}\le m\); all later rows
are universal singletons. In the opposite direction, (PG46) uses the
universal singleton edge \((m+1,m)\). For the terminal singleton
\(P_{v-1}\), every \(1\le j<v-1\) uses (PG44), while \(j=v-1\) uses the
identity. At the closing gap \(G_{v-1}\), a triple target is local exactly
for

\[
k\ge\kappa_{v-1}=\left\lfloor{4m+3\over5}\right\rfloor;
\tag{PG47}
\]

then (PG46) applies without wrapping. A singleton target is identical, except
that \(k=v-1\) uses (PG45). For a prescribed target in the closing column,
(PG46) or (PG45) therefore uses that column only at the target. There is one
other way a construction touches it: when (PG44) extends
\((v-1,j)\) with \(1\le j<v-1\), its final shifted edge is
\((v-2,v-1)\), safe because \(P_{v-2}\) is a universal singleton for
\(m\ge3\). No index interval wraps the canonical cut. The last nonclosing
threshold \(\lfloor(4m+1)/5\rfloor\) is handled in the same way.

At \(m=3\),

\[
(\kappa_0,\ldots,\kappa_5)=(0,1,1,2,2,3),
\tag{PG48}
\]

so the minimum parameter has no exceptional edge or shift.

Combining the Hall obstruction and the three constructions proves the
following **EXACT EDGE-EXTENDIBILITY THEOREM**:

\[
\boxed{
\begin{aligned}
\mathcal R_{\rm ext}
&=\{(0,0)\}
\mathbin\cup
\{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}\\
&=\{(0,0)\}
\mathbin\cup
\{(k,j):1\le k\le m,\ 1\le j\le\ell_k\}\\
&\hspace{2.7em}\mathbin\cup
\{(k,j):m+1\le k\le2m-1,\ 1\le j\le2m-1\}.
\end{aligned}}
\tag{PG49}
\]

Hence the candidate classification is true: \((0,0)\) and every local edge
with positive gap index are extendible, while the \(2m-1\) local edges
\((k,0)\), \(k>0\), are not. The off-diagonal constructions prove existence
of nonidentity relation-compatible bijections, but they do not classify all
such bijections. By (PG36), each constructed bijection passes exactly the
distance-one and distance-two local test. The matching theorem itself scores
no distance-at-least-three pair and has no geometric consequence. The next
subsection proves the stronger full-score statement for arbitrary compatible
bijections.

### Full score of arbitrary relation-compatible bijections

We now return to an arbitrary bijection \(\alpha\) in (PG1). In particular,
none of the interval-shift formulas (PG44)--(PG46) is assumed. Write
\(W^{(=3)}(\sigma)\) for the maximum defining \(W\) restricted to pairs of
circular positional distance exactly three. Put

\[
k_j=\alpha(j),
\qquad
j^+=j+1\pmod v,
\qquad
F_k=\operatorname{first}(P_k)
=
\begin{cases}
A_k,&0\le k\le m,\\
x_k,&m+1\le k<v.
\end{cases}
\]

To assign every forward start once, use the half-open gap block
\[
H_j=(E_j,\lambda_j,P_{k_j},\rho_{j^+});
\]
the shared terminal \(E_{j^+}\) is a start in \(H_{j^+}\), not in \(H_j\).
If \(P_{k_j}\) is a triple, the six forward pairs at positional distance
three whose first position belongs to \(H_j\) are exactly

\[
\begin{gathered}
\{E_j,c_{k_j}\},\quad
\{\lambda_j,B_{k_j}\},\quad
\{A_{k_j},\rho_{j^+}\},\quad
\{c_{k_j},E_{j^+}\},\\
\{B_{k_j},\lambda_{j^+}\},\quad
\{\rho_{j^+},F_{k_{j^+}}\}.
\end{gathered}
\tag{PG50}
\]

If \(P_{k_j}\) is a singleton, the corresponding four starts in \(H_j\)
give

\[
\{E_j,\rho_{j^+}\},\quad
\{\lambda_j,E_{j^+}\},\quad
\{x_{k_j},\lambda_{j^+}\},\quad
\{\rho_{j^+},F_{k_{j^+}}\}.
\tag{PG51}
\]

The two transition pairs in (PG50)--(PG51) can be displayed separately. If
the current and next path types are respectively triple/singleton, they are

\[
\begin{array}{c|c|c}
P_{k_j}&P_{k_{j^+}}&
\text{pairs crossing the gap transition}\\ \hline
\text{triple}&\text{triple}&
\{B_{k_j},\lambda_{j^+}\},\ \{\rho_{j^+},A_{k_{j^+}}\}\\
\text{triple}&\text{singleton}&
\{B_{k_j},\lambda_{j^+}\},\ \{\rho_{j^+},x_{k_{j^+}}\}\\
\text{singleton}&\text{triple}&
\{x_{k_j},\lambda_{j^+}\},\ \{\rho_{j^+},A_{k_{j^+}}\}\\
\text{singleton}&\text{singleton}&
\{x_{k_j},\lambda_{j^+}\},\ \{\rho_{j^+},x_{k_{j^+}}\}.
\end{array}
\tag{PG52}
\]

There are \(m+1\) triple paths and \(m-1\) singleton paths, independently
of their assignment. Thus (PG50)--(PG51) contain

\[
6(m+1)+4(m-1)=10m+2=|\sigma_\alpha|
\tag{PG53}
\]

forward starts. Since \(|\sigma_\alpha|>6\), every unordered pair at circular
positional distance three has exactly one of these forward orientations.
Hence the lists are exhaustive and contain no duplicate unordered pair.

The cyclic closing transition is also literal. If \(\alpha\) is
relation-compatible, then (PG38)--(PG40) force \(k_0=0\). For
\(k=k_{v-1}\le m\), (PG50) at \(j=v-1\) reads

\[
\{n,c_k\},\ \{2,B_k\},\ \{A_k,4m+1\},\
\{c_k,d\},\ \{B_k,4m\},\ \{4m+1,A_0\},
\tag{PG54}
\]

whereas for \(k>m\), (PG51) reads

\[
\{n,4m+1\},\ \{2,d\},\ \{x_k,4m\},\ \{4m+1,A_0\}.
\tag{PG55}
\]

No relation property is needed for the distance-three bound itself. The only
pairs in (PG50)--(PG51) having neither endpoint low are the terminal--connector
pairs \(\{E,c_k\}\). Every other pair is either terminal--low or
low--middle. Therefore, for every bijection \(\alpha\),

\[
\begin{aligned}
Ec_k&\le n c_m=n(5m+2),\\
E\,\text{low}&\le n(4m+1)<n(5m+2),\\
\text{low}\cdot\text{middle}
&\le(4m+1)(d-1)<n(5m+2),
\end{aligned}
\tag{PG56}
\]

where the second strict comparison is quantified by

\[
n(5m+2)-(4m+1)(d-1)=18m^2+15m+3>0.
\]

Consequently the candidate bound is true, and in fact does not require
relation-compatibility:

\[
\boxed{
W^{(=3)}(\sigma_\alpha)
\le {n(5m+2)\over3}<T,
\qquad
3T-n(5m+2)=46m^2+49m+12>0.
}
\tag{PG57}
\]

This bound is sharp even within the relation-compatible class. Equality in
the product bound can occur only on \(\{n,c_m\}\), and (PG50) shows that

\[
W^{(=3)}(\sigma_\alpha)={n(5m+2)\over3}
\quad\Longleftrightarrow\quad
\alpha(v-2)=m\ \text{ or }\ \alpha(v-1)=m.
\tag{PG58}
\]

Both alternatives occur in relation-compatible bijections: the edges
\((m,v-2)\) and \((m,v-1)\) are local, and the two instances of (PG46)
give explicit witnesses. Thus (PG57) is an exact maximum over that class,
not merely a convenient uniform estimate.

For every pair at positional distance \(q\ge4\), independently of \(\alpha\),

\[
{ij\over q}\le {n(n-1)\over4}<T,
\qquad
4T-n(n-1)=28m^2+62m+18>0.
\tag{PG59}
\]

Finally, every reassignment retains the oriented path \(P_0\), whose internal
adjacent pair satisfies

\[
A_0c_0=(d-1)(4m+2)=T.
\tag{PG60}
\]

Equations (PG57), (PG59), and (PG60) prove the stronger
**EXACT ARBITRARY-BIJECTION COLLAPSE THEOREM**

\[
\boxed{
W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha)
\quad\text{for every bijection }\alpha.
}
\tag{PG61}
\]

Combining (PG61) with the exact local equivalence (PG36) gives

\[
\boxed{
\begin{aligned}
\alpha\text{ is relation-compatible}
&\quad\Longleftrightarrow\quad
W^{(\le2)}(\sigma_\alpha)\le T\\
&\quad\Longleftrightarrow\quad
W(\sigma_\alpha)\le T
\quad\Longleftrightarrow\quad
W(\sigma_\alpha)=T.
\end{aligned}}
\tag{PG62}
\]

On this residue-three branch, (RC5) and (GC1) give \(W_n=T\). Hence every
relation-compatible bijection is a global full-distance minimizer of the
product-distance surrogate, while every incompatible bijection in this
scaffold has score strictly above \(T\). In particular, define the support of
full-optimal scaffold bijections by

\[
\mathcal R_{\rm full}
=\{(k,j):\text{some bijection }\alpha\text{ has }
\alpha(j)=k\text{ and }W(\sigma_\alpha)=T\}.
\]

Then (PG49) and (PG62) give the exact identity

\[
\boxed{
\mathcal R_{\rm full}=\mathcal R_{\rm ext}
=\{(0,0)\}\mathbin\cup
\{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
}
\tag{PG63}
\]

Thus (PG49) is exactly the edge support of full-optimal bijections in this
scaffold, although neither (PG49) nor (PG63) enumerates those bijections. The
interval shifts are now certified full-optimal as special witnesses, but the
proof applies to all relation-compatible bijections. This is a combinatorial
surrogate theorem; it does not identify a geometric optimum or improve the
already recorded regular-direction upper bound.

### Exact Ferrers count of full-optimal scaffold bijections

We now count the arbitrary bijections classified above. This is not an edge
count: it is the number of perfect matchings of the PG49 support. Keep
\(v=2m\), \(d=8m+4\), and the inclusive column thresholds

\[
\kappa_j=
\left\lceil{j(d-1)\over2(d+j)}\right\rceil
\qquad(0\le j<v).
\]

Define the set and its labelled cardinality by

\[
\mathfrak F_m
=\{\alpha:\{0,\ldots,v-1\}\to\{0,\ldots,v-1\}:
\alpha\text{ is bijective and }
(\alpha(j),j)\in\mathcal R_{\rm ext}\text{ for every }j\},
\qquad
\mathsf F_m^{\rm lab}=|\mathfrak F_m|.
\tag{PG64}
\]

Here the gaps \(G_j\) and the retained oriented paths \(P_k\) are indexed,
distinct objects. Thus \(\mathsf F_m^{\rm lab}\) is, by definition, a labelled
count. Repeated Ferrers thresholds do not identify rows or columns.

Let \(A_m=(a_{k,j})_{0\le k,j<v}\) be the support matrix, with rows indexed
by paths and columns by gaps, as in the preceding Ferrers convention. PG49
gives the exact matrix

\[
a_{k,j}=
\begin{cases}
1,&(k,j)=(0,0),\\
1,&1\le j<v\text{ and }k\ge\kappa_j,\\
0,&\text{otherwise}.
\end{cases}
\qquad
\mathsf F_m^{\rm lab}=\operatorname{per}(A_m).
\tag{PG65}
\]

In particular, row and column zero are forced. Deleting them leaves the
square board \(1\le j,k<v\), whose gap neighborhoods are the nested suffixes

\[
N(G_j)=\{P_{\kappa_j},\ldots,P_{v-1}\}
\qquad(1\le j<v).
\tag{PG66}
\]

Process these gaps in the order
\(G_{v-1},G_{v-2},\ldots,G_1\). When \(G_j\) is reached, the
\(v-1-j\) paths already used by the narrower columns all belong to
\(N(G_j)\), by monotonicity of \(\kappa_j\). Since
\(|N(G_j)|=v-\kappa_j\), the number of available paths is exactly

\[
(v-\kappa_j)-(v-1-j)=j+1-\kappa_j,
\tag{PG67}
\]

independently of which valid choices were made later in the suffix. Thus, if
\(C_{m,v}=1\) and \(C_{m,j}\) counts the injective assignments of
\(G_j,\ldots,G_{v-1}\), the exact recurrence is

\[
C_{m,j}=(j+1-\kappa_j)C_{m,j+1}
\quad(j=v-1,\ldots,1),
\qquad
\mathsf F_m^{\rm lab}=C_{m,1}.
\tag{PG68}
\]

Consequently the requested symbolic formula is

\[
\boxed{
\mathsf F_m^{\rm lab}
=\prod_{j=1}^{2m-1}
\left(
j+1-
\left\lceil{j(8m+3)\over2(8m+4+j)}\right\rceil
\right)
}
\qquad(m\ge3).
\tag{PG69}
\]

There is an equivalent row-threshold form. Put
\(q_m=\kappa_{2m-1}=\lfloor(4m+3)/5\rfloor\). This is the first path
index whose residual row contains every positive gap. For triple rows put

\[
\ell_k=
\min\!\left\{2m-1,
\left\lfloor{2k(8m+4)\over8m+3-2k}\right\rfloor\right\}
\qquad(1\le k\le m).
\]

After deleting the forced zero edge, such a row has the positive-gap
neighborhood \(G_1,\ldots,G_{\ell_k}\), whereas each singleton row has all
\(2m-1\) positive gaps. Applying the same recurrence to these nested initial
segments gives the independently readable identity

\[
\boxed{
\mathsf F_m^{\rm lab}
=(m-1)!\prod_{k=1}^{m}(\ell_k-k+1)
=(2m-q_m)!\prod_{k=1}^{q_m-1}(\ell_k-k+1).
}
\tag{PG70}
\]

Every boundary in the two products is literal.

- At column zero, PG49 forces \(\alpha(0)=0\); the omitted factor would be
  \(1-\kappa_0=1\). At the first positive column,
  \(\kappa_1=1\), so the factor is also one.
- For \(2\le j<v\), PG40 gives \(\kappa_j\le j-1\), so every factor in
  (PG69) is at least two. In particular, no formal Hall-zero factor is
  hidden.
- At the last nonclosing and closing columns, respectively,

  \[
  \kappa_{2m-2}=\left\lfloor{4m+1\over5}\right\rfloor,
  \qquad
  \kappa_{2m-1}=\left\lfloor{4m+3\over5}\right\rfloor,
  \tag{PG71}
  \]

  and (PG69) uses the factors
  \(2m-1-\lfloor(4m+1)/5\rfloor\) and
  \(2m-\lfloor(4m+3)/5\rfloor\). These formulas include all five residue
  classes of \(m\).
- Since \(q_m\le m\), all rows from \(P_{q_m}\) onward are universal on the
  positive gaps; this gives the second product in (PG70). At the displayed
  path-type transition, \(\ell_m=2m-1\), so the last triple row
  contributes \(m\). The first singleton row \(k=m+1\) contributes
  \(m-1\), and the terminal singleton \(k=2m-1\) contributes one. Thus the
  triple/singleton boundary and terminal row require no correction. The
  asserted saturation is exact because

  \[
  2m(8m+4)-(2m-1)(6m+3)=4m^2+8m+3>0.
  \]
- Equality at either a row or column cutoff is included by the floor/ceiling
  definitions. Hence the nontrivial equalities already allowed by PG26 are
  counted, not discarded.

At the minimum parameter, PG48 gives

\[
m=3:\qquad
(\kappa_0,\ldots,\kappa_5)=(0,1,1,2,2,3),
\qquad
\mathsf F_3^{\rm lab}=1\cdot2\cdot2\cdot3\cdot3=36.
\tag{PG72}
\]

This also checks the row form: the triple cutoffs are
\((\ell_0,\ell_1,\ell_2,\ell_3)=(0,2,4,5)\), and the two singleton rows are
universal.

It remains to identify exactly what the permanent counts. Every matching of
the PG49 board uses only edges of \(\mathcal R_{\rm loc}\), so PG36 makes it
relation-compatible. Conversely, every relation-compatible bijection uses
only extendible edges and is a matching of the PG49 board. Finally PG62,
whose quantifier is over arbitrary bijections rather than only the interval
shifts, gives

\[
\boxed{
\mathfrak F_m
=\{\alpha:\alpha\text{ is relation-compatible}\}
=\{\alpha:W(\sigma_\alpha)=T=W_n\}.
}
\tag{PG73}
\]

Thus (PG69)--(PG70) count exactly all full-optimal bijections in the fixed
scaffold classified by PG50--PG63, and no incompatible or merely
edge-extendible partial assignment is counted.

For clarity about symmetries, the formula remains a labelled count: no
rotation, reflection, path permutation, or automorphism of the Ferrers board
is quotiented out. Nevertheless, distinct \(\alpha\) give distinct canonical
dihedral core-order classes in this particular labelled scaffold. Indeed,
the label \(n=E_{v-1}\) fixes the rotation, its forward and backward
neighbors are respectively \(2=\lambda_{v-1}\) and
\(3=\rho_{v-1}\), and hence the displayed orientation is already the
canonical one with second entry smaller than the last. The word between each
\(\lambda_j\) and \(\rho_{j+1}\) then recovers the unique oriented path
\(P_{\alpha(j)}\). Reflection starts instead with \((n,3,\ldots,2)\) and
cannot be another displayed scaffold order. Therefore \(\mathsf F_m^{\rm lab}\)
also equals the number of dihedral classes represented by these full-optimal
scaffold orders, by injectivity rather than by division by a symmetry factor.
No assertion is made about alternative scaffolds or geometric optima.

### Asymptotics of the exact Ferrers count

All logarithms in this subsection are natural. We derive the asymptotic
directly from (PG69), without enumerating a path permutation or a matching.
For \(m\ge3\), put \(N=2m-1\) and, for \(1\le j\le N\), write

\[
h_{m,j}={j(8m+3)\over2(8m+4+j)},
\qquad
a_{m,j}=j+1-\lceil h_{m,j}\rceil .
\tag{PG74}
\]

Thus \(\mathsf F_m^{\rm lab}=\prod_{j=1}^N a_{m,j}\). The three comparison
factors needed below are

\[
c_{m,j}=j-h_{m,j}
={j(2j+8m+5)\over2(j+8m+4)},
\qquad
s_{m,j}=c_{m,j}+1,
\qquad
r_{m,j}={j(j+4m)\over j+8m}
=m f(j/m),
\tag{PG75}
\]

where \(f(x)=x(x+4)/(x+8)\). Here \(s_{m,j}=j+1-h_{m,j}\) is the factor
obtained by literally removing the ceiling, while \(c_{m,j}\) is a lower
comparison factor adapted to the integer rounding. These roles must not be
interchanged.

Since \(j+1\) is an integer,

\[
a_{m,j}=\lfloor c_{m,j}+1\rfloor=1+\lfloor c_{m,j}\rfloor,
\qquad
c_{m,j}<a_{m,j}\le c_{m,j}+1=s_{m,j}.
\tag{PG76}
\]

This is the complete effect of the ceiling, including equality at a cutoff.
Moreover \(c_{m,j}>j/2\), because the latter inequality reduces to
\(j+1>0\). Hence

\[
0\le
\sum_{j=1}^N\log s_{m,j}-\log\mathsf F_m^{\rm lab}
<\sum_{j=1}^N\log\left(1+{2\over j}\right)
=\log\bigl(m(2m+1)\bigr).
\tag{PG77}
\]

Thus the direct ceiling/no-ceiling change has the displayed sign and is
rigorously \(O(\log m)\); it is not being declared \(O(1)\). For the lower
comparator in (PG76), put

\[
\Theta_m=\sum_{j=1}^N\log{a_{m,j}\over c_{m,j}}.
\]

Then \(0<\Theta_m<\log(m(2m+1))\). This positive quantity is a comparison
with \(c_{m,j}\), not the direct ceiling effect in (PG77).

The remaining perturbation from the homogeneous factor is uniformly
summable. Direct cancellation gives

\[
{c_{m,j}\over r_{m,j}}
=
{1+5/(2(j+4m))\over1+4/(j+8m)}.
\tag{PG78}
\]

Since \(8m-3j>0\) for every \(1\le j\le2m-1\), this ratio is greater than
one. Also

\[
0<
\Delta_m:=\sum_{j=1}^N\log{c_{m,j}\over r_{m,j}}
<\sum_{j=1}^N{5\over2(j+4m)}
<{5\over4}.
\tag{PG79}
\]

Consequently

\[
\log\mathsf F_m^{\rm lab}
=\log Z_m+\Delta_m+\Theta_m,
\qquad
Z_m:=\prod_{j=1}^{2m-1}r_{m,j}
={(2m-1)!(6m-1)!(8m)!\over(4m)!(10m-1)!}.
\tag{PG80}
\]

The factorial identity in (PG80) isolates the endpoint singularity: the
factor \(j\) in \(r_{m,j}\) contains all of the \(\log(j/m)\) behavior as
\(j/m\to0\). No Euler--Maclaurin estimate uniform at zero is required. For
a completely elementary all-\(m\) bound, set

\[
u(x)=\log{x+4\over x+8},
\qquad
L_m=\sum_{j=1}^{2m-1}\log(j/m),
\qquad
U_m=\sum_{j=1}^{2m-1}u(j/m).
\]

The monotone integral bounds for \(\log x\), applied to \((2m)!\), and the
left and right Riemann sums for the increasing function \(u\) give

\[
\begin{aligned}
m(2\log2-2)+1-\log2
&\le L_m
\le m(2\log2-2)+1+\log m,\\
\log{5\over3}
&\le U_m-m\int_0^2u(x)\,dx
\le\log2.
\end{aligned}
\tag{PG81}
\]

These inequalities include the missing grid point \(x=2\), the first point
\(j=1\), and the fact that there are \(2m-1\), not \(2m\), product factors.
Since

\[
\begin{aligned}
C_{\rm F}
:=\int_0^2\log f(x)\,dx
&=(2\log2-2)
  +6\log6-4\log4-10\log10+8\log8\\
&=14\log2+6\log3-10\log5-2,
\end{aligned}
\tag{PG82}
\]

(PG81) yields

\[
1+\log{5\over6}-\log m
\le
\log Z_m-\bigl(2m\log m+C_{\rm F}m\bigr)
\le1+\log2.
\tag{PG83}
\]

Combining (PG79), the bound on \(\Theta_m\), and (PG83) proves the following
quantitative theorem for every integer \(m\ge3\):

\[
\boxed{
1+\log{5\over6}-\log m
<
\log\mathsf F_m^{\rm lab}
-\bigl(2m\log m+C_{\rm F}m\bigr)
<
{9\over4}+\log\bigl(2m(2m+1)\bigr).
}
\tag{PG84}
\]

In particular, the proposed linear coefficient is correct:

\[
\boxed{
\log\mathsf F_m^{\rm lab}
=2m\log m
+(14\log2+6\log3-10\log5-2)m
+O(\log m).
}
\tag{PG85}
\]

There is no hidden boundary correction in this derivation. Column zero has
the forced unit factor from PG65 and is deliberately outside (PG74), because
the homogeneous factor \(r_{m,0}\) vanishes. Column one has
\(\kappa_1=1\) and exact factor one; its nonuniform relative discrepancy is
covered by the first harmonic term in (PG77). The last two columns retain
the literal PG71 factors for all five residue classes of \(m\), and all the
inequalities above include \(j=2m-2,2m-1\).

The row form (PG70) supplies a separate audit of the path-type transition.
The first universal row index
\(q_m=\kappa_{2m-1}=\lfloor(4m+3)/5\rfloor\) is itself a triple row
throughout the domain, since \(q_m\le m\); it must not be identified with the
triple/singleton boundary. At that boundary,
\(\ell_m=2m-1\), because

\[
2m(8m+4)-(2m-1)(6m+3)=4m^2+8m+3>0.
\]

Thus the last triple contributes exactly \(m\), while the universal
singleton rows contribute \(m-1,m-2,\ldots,1\), namely the factor
\((m-1)!\). No transition or terminal correction is missing from (PG85).

Finally, (PG84)--(PG85) are theorems about the labelled cardinality defined
in PG64. The already proved canonical injectivity only identifies the same
number with the cardinality of the represented image of scaffold orders; it
is not a symmetry quotient and plays no role in the asymptotic proof. The
result gives no count for alternative scaffolds and no geometric conclusion.
The bounds in (PG84)--(PG85) alone do not determine a finer coefficient of
\(\log m\); the following argument supplies that missing coefficient.

### Sharp logarithmic coefficient for the exact Ferrers count

We retain the exact decomposition (PG80), including its signs:

\[
\log\mathsf F_m^{\rm lab}=\log Z_m+\Delta_m+\Theta_m,
\qquad
\Delta_m=\sum_{j=1}^{2m-1}\log{c_{m,j}\over r_{m,j}},
\qquad
\Theta_m=\sum_{j=1}^{2m-1}\log{a_{m,j}\over c_{m,j}}.
\tag{PG86}
\]

The first two terms have ordinary smooth expansions. From the exact gamma
quotient in (PG80) and Stirling's formula, used only at positive multiples of
\(m\),

\[
\boxed{
\log Z_m
=2m\log m+C_{\rm F}m-{1\over2}\log m
+{1\over2}\log{10\pi\over3}
+{53\over1440m}+O(m^{-3}).
}
\tag{PG87}
\]

Indeed, for \(a>0\) fixed and \(\epsilon\in\{0,1\}\),
\[
\log\Gamma(am+\epsilon)
=am(\log m+\log a-1)
+(\epsilon-\tfrac12)(\log m+\log a)
+\tfrac12\log(2\pi)+{1\over12am}+O(m^{-3}),
\]
and the five signed gamma factors are
\(\Gamma(2m)\Gamma(6m)\Gamma(8m+1)/
[\Gamma(4m+1)\Gamma(10m)]\). Thus the complete singular behavior near
\(j/m=0\) is already contained in an exact factorial product; no pointwise
endpoint expansion is being made there.

For the perturbation, put

\[
\alpha(x)={5\over2(x+4)},
\qquad
\beta(x)={4\over x+8}.
\]

Uniformly for \(0\le x\le2\), (PG78) gives

\[
\log{c_{m,j}\over r_{m,j}}
={\alpha(j/m)-\beta(j/m)\over m}
-{\alpha(j/m)^2-\beta(j/m)^2\over2m^2}
+O(m^{-3}).
\tag{PG88}
\]

Put \(g=\alpha-\beta\) and \(w=\alpha^2-\beta^2\). The composite
trapezoidal estimate, with both omitted endpoint half-weights kept, and the
ordinary Riemann estimate give

\[
{1\over m}\sum_{j=1}^{2m-1}g(j/m)
=\int_0^2g(x)\,dx-{g(0)+g(2)\over2m}+O(m^{-2}),
\]

\[
{1\over m}\sum_{j=1}^{2m-1}w(j/m)
=\int_0^2w(x)\,dx+O(m^{-1}).
\]

Here

\[
(\alpha-\beta)(0)={1\over8},
\qquad
(\alpha-\beta)(2)={1\over60},
\qquad
\int_0^2(\alpha^2-\beta^2)\,dx={29\over240}.
\]

Thus the coefficient of \(m^{-1}\) is
\(-\tfrac12(1/8+1/60)-\tfrac12(29/240)=-21/160\).

It follows that

\[
\boxed{
\Delta_m
=D_0-{21\over160m}+O(m^{-2}),
\qquad
D_0={5\over2}\log{3\over2}-4\log{5\over4}.
}
\tag{PG89}
\]

This estimate is uniform at both ends. If \(K=o(m)\), each summand with
\(j\le K\) is
\(1/(8m)+O(j/m^2+m^{-2})\), while each summand with
\(2m-j\le K\) is
\(1/(60m)+O((2m-j)/m^2+m^{-2})\). Either endpoint region therefore
contributes \(o(1)\); the global trapezoidal estimate supplies the integral
in (PG89) uniformly across the remaining indices. There is no floor,
ceiling, or residue-class dependence in this perturbation.

It remains to analyze the only nonsmooth term, \(\Theta_m\). Put
\(D=8m+4\) and use the exact identity

\[
c_{m,j}={j\over2}+\delta_m(j),
\qquad
\delta_m(x)={x(x+1)\over2(D+x)},
\qquad
e_{m,j}:=a_{m,j}-c_{m,j}=1-\{c_{m,j}\}.
\tag{PG90}
\]

Here \(1-\{c\}=1\) when \(c\) is an integer, exactly as required by
\(a=1+\lfloor c\rfloor\). If \(G(t)=1-\{t\}\), then

\[
e_{m,j}=
\begin{cases}
G(\delta_m(j)),&j\ \text{even},\\
G(\delta_m(j)+\tfrac12),&j\ \text{odd}.
\end{cases}
\]

Since \(0<e_{m,j}\le1\), the elementary inequality
\(0\le x-\log(1+x)\le x^2/2\), together with

\[
{2\over j}-{1\over c_{m,j}}
={2(j+1)\over j(2j+8m+5)},
\]

shows, uniformly in \(m\), that

\[
\boxed{
\Theta_m
=2\sum_{j=1}^{2m-1}{e_{m,j}\over j}+O(1).
}
\tag{PG91}
\]

Both discarded error sums are bounded: the logarithmic Taylor error is at
most a constant times \(\sum j^{-2}\), and the displayed reciprocal
difference sums to \(O(1)\).

First consider the slow initial region. Let
\(J=\lfloor\sqrt m\rfloor\). For \(j\le J\),
\(0<\delta_m(j)<1/2\), and hence

\[
e_{m,j}=
\begin{cases}
1-\delta_m(j),&j\ \text{even},\\
\tfrac12-\delta_m(j),&j\ \text{odd}.
\end{cases}
\]

Moreover

\[
\sum_{j\le J}{\delta_m(j)\over j}
={1\over2}\sum_{j\le J}{j+1\over D+j}=O(1).
\]

Separating the two parity classes in the harmonic sum therefore gives

\[
\boxed{
\sum_{j\le J}{e_{m,j}\over j}
={3\over4}\log J+O(1)
={3\over8}\log m+O(1).
}
\tag{PG92}
\]

The scale above \(\sqrt m\) requires a uniform floor/ceiling estimate. We
use the following elementary sawtooth lemma. Let
\(\psi(t)=1/2-\{t\}\), with \(\psi(k)=1/2\) at integers. If
\(\phi\) is increasing and convex on an integer block of length at most
\(X\), and

\[
0<\lambda\le\phi'(x)\le d<1,
\]

then every partial sum on that block satisfies

\[
\left|\sum\psi(\phi(k))\right|
\le C\left(Xd+{1\over\lambda}+1\right)
\tag{PG93}
\]

for an absolute constant \(C\). To prove this, compare the sum with the
integral over the corresponding unit cells. A cell not crossing an integer
of the phase costs at most \(d\), while on semi-open unit cells the number
of cells meeting a jump is \(O(Xd+1)\); this also includes samples lying
exactly at a jump. In the integral, the change of variable \(t=\phi(x)\)
produces the decreasing weight
\(1/\phi'(\phi^{-1}(t))\). Integration by parts against the bounded
one-periodic primitive of \(\psi\) costs at most a constant times
\(1/\lambda\), proving (PG93).

The phase in (PG90) has

\[
\delta_m'(x)
={x^2+2Dx+D\over2(D+x)^2},
\qquad
\delta_m''(x)={D(D-1)\over(D+x)^3}>0,
\qquad
{x\over2(D+x)}
\le\delta_m'(x)
\le{2x+1\over2(D+x)}.
\tag{PG94}
\]

Apply (PG93) separately to the phases
\(\delta_m(2k)\) and
\(\delta_m(2k-1)+1/2\). On a dyadic block \(j\asymp X\), with
\(J<j\le B:=\lfloor m/2\rfloor\), (PG94) gives
\(\lambda\asymp X/m\) and \(d\asymp X/m<1\). Thus the unweighted
centered partial sums are
\(O(X^2/m+m/X)\). Abel summation with weight \(1/j\) makes the block
contribution

\[
O\left({X\over m}+{m\over X^2}\right).
\]

The sum of these bounds over \(X=J,2J,4J,\ldots,B\) is \(O(1)\). Hence,
uniformly over both parities and all exact cutoff hits,

\[
\sum_{J<j\le B}{e_{m,j}-1/2\over j}=O(1),
\qquad
\sum_{J<j\le B}{e_{m,j}\over j}
={1\over2}\log{B\over J}+O(1)
={1\over4}\log m+O(1).
\tag{PG95}
\]

This covers every growing sublinear regime above \(\sqrt m\). The true bulk
needs no equidistribution assertion: because \(0<e_{m,j}\le1\),

\[
0<\sum_{B<j\le2m-1}{e_{m,j}\over j}
\le\sum_{B<j\le2m-1}{1\over j}=O(1).
\]

Combining this with (PG92), (PG95), and (PG91) proves the sharp rounding
estimate

\[
\boxed{
\sum_{j=1}^{2m-1}{e_{m,j}\over j}
={5\over8}\log m+O(1),
\qquad
\Theta_m={5\over4}\log m+O(1).
}
\tag{PG96}
\]

The arithmetic boundary cases do not hide another logarithm. An odd \(j\)
cannot satisfy \(\delta_m(j)+1/2\in\mathbb Z\): it would make
\(j(j+1)/(D+j)\) an odd integer, whereas division by the odd number
\(D+j\) cannot remove the factor two from \(j+1\). For even \(j\), exact
hits can occur, but strict monotonicity gives at most one hit for each
integer level \(q\). Since
\(\delta_m(j)\le j(j+1)/(16m+8)\), its hit index satisfies
\(j_q\gg\sqrt{mq}\); moreover
\(q\le\delta_m(2m-1)<m/5\). Consequently
\(\sum_q1/j_q=O(1)\). This agrees with, and is already covered by, the
jump-inclusive proof of (PG93).

The two right endpoint factors exhibit all five residue classes explicitly.
For \(m=5u+r\),

\[
\begin{array}{c|cc}
r&a_{m,2m-2}&a_{m,2m-1}\\ \hline
0&6u-1&6u\\
1&6u&6u+1\\
2&6u+2&6u+2\\
3&6u+3&6u+3\\
4&6u+4&6u+5
\end{array}
\tag{PG97}
\]

Each corresponding \(\log(a_{m,j}/c_{m,j})\) is \(O(m^{-1})\), because
\(c_{m,j}>j/2\) and \(0<e_{m,j}\le1\). At the left endpoint,

\[
a_{m,1}=1,
\qquad
c_{m,1}={1\over2}+{1\over8m+5},
\]

so its contribution is \(\log2+O(m^{-1})\); column zero remains the forced
unit factor outside (PG86). Thus neither endpoint, any class modulo five, nor
an exact internal cutoff changes (PG96).

Finally, (PG87), (PG89), and (PG96) give the requested theorem:

\[
\boxed{
\log\mathsf F_m^{\rm lab}
=2m\log m+C_{\rm F}m+{3\over4}\log m+O(1).
}
\tag{PG98}
\]

Thus the logarithmic coefficient exists and is uniquely
\(\gamma=3/4\). Equivalently,

\[
{\log\mathsf F_m^{\rm lab}-(2m\log m+C_{\rm F}m)\over\log m}
\longrightarrow{3\over4}.
\]

The three contributions to this coefficient are respectively
\(-1/2\) from \(Z_m\), zero from \(c_{m,j}/r_{m,j}\), and \(5/4\) from
the rounding \(a_{m,j}/c_{m,j}\). This bounded-remainder theorem does not
assert that the remaining \(O(1)\) term converges.

For comparison with the literal removal of the ceiling, recall
\(s_{m,j}=c_{m,j}+1\). The same reciprocal estimates used in (PG91) give

\[
\sum_{j=1}^{2m-1}\log{s_{m,j}\over c_{m,j}}
=2\log m+O(1),
\qquad
\boxed{
\sum_{j=1}^{2m-1}\log{a_{m,j}\over s_{m,j}}
=-{3\over4}\log m+O(1).
}
\tag{PG99}
\]

The negative coefficient in the second formula is the signed direct
ceiling/no-ceiling correction. It must not be confused with the positive
\(5/4\) coefficient of the lower-comparator rounding in (PG96). All results
in this sharpening remain statements about the labelled PG69 formula only;
no permutation or matching enumeration and no geometric inference enters
the proof.

### The descending-min representative of the PG49 board

We now select one deterministic matching of the PG49 Ferrers board. This is
not a search over its matchings. Retain \(v=2m\), \(d=8m+4\), and the exact
thresholds \(\kappa_j\) from (PG38). Define

\[
\alpha_{\min}(0)=0,
\]

and, for \(j=v-1,v-2,\ldots,1\), let \(\alpha_{\min}(j)\) be the least
path index not used at a later step and satisfying
\(\alpha_{\min}(j)\ge\kappa_j\). Put

\[
\Delta_j=\kappa_{j+1}-\kappa_j
\qquad(0\le j<v-1).
\tag{PG100}
\]

The increments are binary. Indeed, (PG39) gives strict increase of \(h_j\),
while

\[
0<h_{j+1}-h_j
={d(d-1)\over2(d+j)(d+j+1)}<1.
\]

Therefore

\[
\boxed{\Delta_j\in\{0,1\}.}
\tag{PG101}
\]

The following suffix invariant proves simultaneously that the prescription
is well defined and identifies every one of its choices. Immediately after
the columns \(G_j,G_{j+1},\ldots,G_{v-1}\) have been assigned, their used
positive path indices are exactly

\[
\boxed{
U_j=\{\kappa_j,\kappa_j+1,\ldots,
       \kappa_j+v-1-j\}.
}
\tag{PG102}
\]

For \(j=v-1\), the least admissible index is \(\kappa_{v-1}\), so (PG102)
holds. Suppose it holds at \(j+1\). If \(\Delta_j=1\), the new least
available index is the one immediately below \(U_{j+1}\), namely
\(\kappa_j\). If \(\Delta_j=0\), the old interval starts at
\(\kappa_j\), so the least available index is the one immediately above it,
\(\kappa_j+v-1-j\). In both cases adjoining that index gives (PG102).
There is no overflow: for \(j\ge2\), (PG40) gives
\(\kappa_j+v-1-j\le v-2\), while at \(j=1\) the endpoint is exactly
\(v-1\). Equivalently, before assigning \(G_j\) the number of available
indices in its neighborhood is the positive integer

\[
(v-\kappa_j)-(v-1-j)=j+1-\kappa_j.
\tag{PG103}
\]

At \(j=1\), (PG102) is \(U_1=\{1,\ldots,v-1\}\). Together with the
separately fixed value \(\alpha_{\min}(0)=0\), this proves that all and only
the \(v\) path indices are used. Thus the procedure has the closed form

\[
\boxed{
\begin{aligned}
\alpha_{\min}(0)&=0,\\
\alpha_{\min}(j)
&=\kappa_j+(1-\Delta_j)(v-1-j)
&& (1\le j\le v-2),\\
\alpha_{\min}(v-1)&=\kappa_{v-1}.
\end{aligned}}
\tag{PG104}
\]

Every positive-column value in (PG104) is at least its Ferrers threshold,
and column zero uses the sole extendible edge \((0,0)\). By (PG49),
\(\alpha_{\min}\) is therefore a relation-compatible bijection for every
integer \(m\ge3\). By the already proved, independent implication (PG62),
its product-distance score is \(W=T=W_n\). This last statement is only a
surrogate-score consequence; it is not a geometric conclusion.

There is also a useful dual reading of (PG104). Put

\[
q=\kappa_{v-1}=\left\lfloor{4m+3\over5}\right\rfloor,
\qquad
\ell_k=\left\lfloor{2k(8m+4)\over8m+3-2k}\right\rfloor
\quad(1\le k<q).
\tag{PG105}
\]

For every integer \(1\le k<q\), the ceiling definition and direct inversion
give the exact cutoff
\[
\kappa_j\le k
\quad\Longleftrightarrow\quad
h_j\le k
\quad\Longleftrightarrow\quad
j\le
\left\lfloor{2k(8m+4)\over8m+3-2k}\right\rfloor=\ell_k.
\]
Together with strict monotonicity of \(h_j\) and its increments below one,
this shows that

\[
\boxed{
\{j:1\le j\le v-2,\ \Delta_j=1\}
=\{\ell_1,\ldots,\ell_{q-1}\},
\qquad
\alpha_{\min}(\ell_k)=k.
}
\tag{PG106}
\]

The closing column receives \(P_q\). Reading the remaining positive gaps
in increasing order, the plateau columns receive
\(P_{v-1},P_{v-2},\ldots,P_{q+1}\). Thus (PG106) and this decreasing
plateau list describe the entire bijection without executing the recursion.
In particular,

\[
\alpha_{\min}(1)=v-1,
\qquad
\alpha_{\min}(2)=1.
\tag{PG107}
\]

For the two terminal columns put
\(p=\lfloor(4m+1)/5\rfloor\). Then

\[
\boxed{
\alpha_{\min}(v-1)=q,
\qquad
\alpha_{\min}(v-2)=
\begin{cases}
p,&m\equiv2,3\pmod5,\\
p+1,&m\equiv0,1,4\pmod5.
\end{cases}}
\tag{PG108}
\]

This explicitly includes the closing, preclosing, and all five residue
boundaries. At the minimum parameter,

\[
m=3:\qquad
(\kappa_0,\ldots,\kappa_5)=(0,1,1,2,2,3),
\qquad
\boxed{\alpha_{\min}=(0,5,1,4,2,3)}.
\tag{PG109}
\]

Equations (PG100)--(PG109) establish existence, bijectivity, and exact
relation compatibility only. The induced core-order objective \(K\) is a
different quantity and is evaluated separately in
`research/FIXED_ORDER_CYCLE_RATIO.md`; no assertion about it is smuggled
into the Ferrers proof.

### An explicit threshold-closing PG49 representative

We now fix a second deterministic matching of the same Ferrers board. It is
specified directly, not selected by a search. Retain \(v=2m\), \(d=8m+4\),
the thresholds in (PG38), and put

\[
q=\kappa_{v-1}=\left\lfloor{4m+3\over5}\right\rfloor.
\]

Define

\[
\boxed{
\alpha_*(0)=0,\qquad
\alpha_*(j)=
\begin{cases}
j,&1\le j<q,\\
j+1,&q\le j\le m-1,\\
3m-1-j,&m\le j\le2m-2,\\
q,&j=2m-1.
\end{cases}}
\tag{PG110}
\]

The five residue classes make every endpoint literal. If \(m\equiv r\pmod
5\), then

\[
q={4m+c_r\over5},
\qquad
(c_0,c_1,c_2,c_3,c_4)=(0,1,2,3,-1).
\tag{PG111}
\]

Thus \(3\le q\le m\), with \(q=m\) only at \(m=3\). The images of the
five pieces in (PG110) are

\[
\boxed{
\{0\},\quad[1,q-1],\quad[q+1,m],\quad
[m+1,2m-1],\quad\{q\}.
}
\tag{PG112}
\]

They are disjoint and cover \(\{0,\ldots,2m-1\}\), so \(\alpha_*\) is a
bijection. The interval \([q+1,m]\) is empty exactly in the minimum row;
this creates neither a duplicate nor a missing index.

It remains to prove Ferrers compatibility, rather than infer it from the
displayed permutation. Equations (PG39)--(PG40) give
\(\kappa_1=1\), \(\kappa_j\le j-1\) for \(2\le j<v\), monotonicity, and
\(\kappa_{v-1}=q\). Hence

\[
\boxed{
\begin{array}{c|c|c}
\text{column range}&\alpha_*(j)&\text{Ferrers comparison}\\ \hline
j=0&0&\alpha_*(0)=0\\
j=1&1&\alpha_*(1)=\kappa_1\\
2\le j<q&j&j>\kappa_j\\
q\le j\le m-1&j+1&j+1>\kappa_j\\
m\le j\le2m-2&3m-1-j&m+1>q\ge\kappa_j\\
j=2m-1&q&\alpha_*(j)=\kappa_{2m-1}.
\end{array}}
\tag{PG113}
\]

The last line is the genuine cyclic column; it does not replace its threshold
by the last nonclosing value. At \(m=3\), (PG48) and (PG110) read

\[
(\kappa_0,\ldots,\kappa_5)=(0,1,1,2,2,3),
\qquad
\boxed{\alpha_*=(0,1,2,5,4,3)}.
\tag{PG114}
\]

Equations (PG110)--(PG114), together with the exact support equivalence
(PG38)--(PG49), prove the **EXACT FERRERS-COMPATIBILITY THEOREM**: the
displayed \(\alpha_*\) is a relation-compatible bijection for every integer
\(m\ge3\). No full-score, geometric, or global-optimality consequence is
needed or inferred here. Its distinct induced-subset objective is evaluated
separately by (KPGSTAR-1)--(KPGSTAR-28).

## Verification Boundary And Open Questions

`tests/test_product_distance.py` checks exact rational comparisons, canonical
counts, every pair rather than only adjacent pairs, an independent full
permutation calculation for the smallest cases, deterministic work bounds,
the all-\(n\) adjacent formula against the explicit interleave construction,
the parity-specific equality classifier on the bounded `n=4..11` regression,
the exact incidence-lemma boundary arithmetic, the `n=12` local degree data,
the strict two-threshold floor and skip-one boundaries, cardinalities zero,
one, and two, an independent brute-force cycle enumerator restricted to tail
cardinality at most seven, the exact finite \(Q_n\) obstruction, the
compatible-low floor and even-square equality, the joint finite \(H_n\)
obstruction, the closed residue formula against both an independent
polynomial evaluation and the unchanged exact event inversion, the
residue-two saturation data at \(n=12,17,22\), every half-integer in the
three corresponding intervals \([H_n,J_n)\), the strict endpoint arithmetic
through a broad falsification sweep, the exact residue-two generator, both
parity branches, the separate distance-one through distance-three and
closing maxima, two independent all-pairs scorers, the
symbolic upper witness, the matching order generator, all fourteen
exceptional orders, their exact
distance-class and closing maxima, independent cyclic checks of the symbolic
family, the exact residue-one generator, its two parity branches, its exact
distance-one and distance-two maxima, its closing arcs, and the effective
full-distance tail comparison. The same test module now also checks the exact
residue formula against \(3B_n\ge n(n-1)\) through \(n=92\), its first
failure at \(n=93\), the requested label relocation, every one of the
\(\binom{92}{2}\) pair scores through two independent exact traversals, the
unique score above \(2850\), and the production scorers as a cross-check. A
six-row exact regression now also reverses one triple at selected endpoint
and interior parameters, checks the exact distance-one, distance-two,
distance-three, long-distance, and closing formulas, and compares two
independent all-pairs traversals with the production scorer. A
separate verifier builds the tails and incidence endpoints without production
support for all 872
orders on `n=3..7` over 34,160 half-integer states, and directly checks the
two-terminal-high equality case at `n=11`. Exact reproduction of both
truncated and full tables remains bounded to `n=3..11`; no cyclic-order
enumeration is performed beyond `n=11`. Independent construction diagnostics
checked the residue-one formula through `k=5000`; the repository regression
checks every `2<=k<=1000` in both residue-two parity branches and selected
full all-pairs scores. These finite diagnostics support but do not replace
the symbolic proofs above. The task-local standard-library diagnostic in
`ops/TASK-20260716__one_triple_reversal_obstruction/` independently
reconstructs the specialized block family and checks the same six rows
without importing project or test helpers.
The sole diagnostic added for the preceding fixed-rotation task is the standalone
standard-library script in
ops/TASK-20260717__nonlocal_middle_path_rotation/. It reconstructs only
the transformation fixed in (NR5), independently scores every unordered pair
at \(m=3,4,9,25\), and checks the exact permutation, distance-class maxima,
unique class maximizers, closing distances one through six, aggregate
long-closing maximum, full score, and sole full-score saturator. It imports no
project or test helper, performs no search, and does not extend enumeration.
The separate diagnostic for (PG15) is the standalone standard-library script
in ops/TASK-20260717__p0_terminal_gap_classification/. For each fixed
\(m\in\{3,4,9,25\}\), it scans only the \(2m\) gap indices, constructs only
the seven-label word (PG4), and checks the exact distance-one and distance-two
inequalities, both unique local maximizers, the one-sided placement sets, and
the literal closing word. It constructs no complete order, assigns no other
path, and enumerates no path permutation.
The sole diagnostic for (PG16)--(PG36) is the standalone standard-library
script in
ops/TASK-20260717__generic_path_terminal_gap_classification/. It scans only
the triples \((m,k,j)\) for \(m\in\{3,4,9,34\}\), constructs only the
constant-size local word, and compares every distance-one and distance-two
pair directly with both cutoff forms. It includes the minimum row, both
cyclic endpoint columns, the path-type transition, and the nontrivial equality
\((m,k,j)=(34,11,24)\). It constructs no complete order or bijection,
enumerates no path permutation, and imports no project or test helper.
The sole diagnostic for (PG37)--(PG49) is the standalone standard-library
script in
ops/TASK-20260717__local_edge_extendibility_classification/. At the fixed
rows \(m\in\{3,4,9,34\}\), it scans local edges only, constructs the one
interval shift prescribed by (PG44)--(PG46), and checks bijectivity, the
target edge, every resulting Ferrers edge, and the residual Hall formula. It
also checks the exact deficient suffix for \((k,0)\), \(k>0\), the
triple/singleton crossings, the terminal singleton, and the closing column.
It never searches over matchings or path permutations, constructs no cyclic
core order, scores no positional pair, and imports no project or test helper.
The sole diagnostic for (PG50)--(PG63) is the standalone standard-library
script in
ops/TASK-20260717__relation_compatible_full_score_classification/. At
\(m\in\{3,4,9,34\}\), it scans the polynomial local state space
\((j,k,h)\), compares the six/four symbolic forms with pairs read directly
from their local words, exercises all four ordered path-type transitions, and
checks the literal compatible closure. It separately constructs only the two
sharp PG46 witnesses with \(P_m\) in \(G_{2m-2}\) or \(G_{2m-1}\) and scores
their complete orders. It enumerates no path permutation or matching and
imports no project or test helper.
The sole diagnostic for (PG64)--(PG73) is the standalone standard-library
script in ops/TASK-20260718__ferrers_bijection_count/. For
\(m=3,\ldots,8\), it builds the PG49 support directly from integer
cross-multiplied inequalities and computes its reduced permanent by Ryser
inclusion--exclusion. It compares that independent value with both Ferrers
products and fixed expected integers, including every terminal-threshold
residue class and the minimum row. It enumerates column subsets, not path
permutations or matchings, and imports no project or test helper.
The sole diagnostic for the later closing-PG46 \(K\) evaluation is the
standalone standard-library script in
ops/TASK-20260718__pg46_closing_exact_k/. For \(m=3,\ldots,30\), it
reconstructs only the prescribed order, runs a max-plus increasing-path DP,
and checks every oriented shortcut arc; direct formula checks continue to
\(m=1000\). It enumerates no subsets, permutations, or matchings and imports
no project or test helper.
The sole diagnostic for the later preclosing-PG46 \(K\) evaluation is the
standalone standard-library script in
ops/TASK-20260718__pg46_preclosing_exact_k/. For \(m=3,\ldots,30\), it
reconstructs only the order placing \(P_m\) in \(G_{2m-2}\), runs a max-plus
increasing-path DP, and checks every oriented shortcut arc; direct score and
comparison checks continue through \(m=1000\). It enumerates no subsets,
permutations, or matchings and imports no project or test helper.
The sole diagnostic for (PG100)--(PG109) and (KPGMIN-1)--(KPGMIN-39) is the
standalone standard-library script in
ops/TASK-20260719__ferrers_greedy_exact_k/. It compares the literal
descending-min recursion with (PG104), checks every suffix interval and
Ferrers edge, reconstructs only this one core order, and runs a max-plus
increasing-path DP plus every oriented shortcut budget for
\(m=3,\ldots,30\). Exact formula and comparator checks continue through
\(m=1000\). It enumerates no subset, path permutation, or matching and
imports no project or test helper. Its absence of zero gains is explicitly
limited to the checked rows; (KPGMIN-19)--(KPGMIN-21) give an exact much
larger zero-gain counterexample.
The exact branchwise KPGZERO theorem, including primitive parameters,
integrality, domain, both half-open plateau ceilings, all boundary columns,
and finite quadratic scale windows, is (KPGZERO-1)--(KPGZERO-23).  It
reconstructs the giant left witness and proves existence of a right-hole
witness.  Its exact remaining obstruction (KPGZERO-24) is the cardinality of
a congruence-filtered one-sided convergent set for one irreducible cubic
root; it is not decided here.
The sole diagnostic for that KPGZERO Diophantine classification is the
standalone standard-library script in
ops/TASK-20260719__pg49_zero_gain_classification/. It scans literal rows only
through `m=500`, direct near-root denominators only through `100000`, and a
finite list of proposed cubic-root convergents with denominator at most
`10^200` and `g<=200`. Decimal arithmetic proposes candidates only; each
reported zero is accepted by exact integer reconstruction, both literal
half-open ceilings, and the corresponding literal gain. It finds 56 left and
eight right parameter triples, thereby furnishing exact witnesses in both
branches. These bounded counts prove neither finiteness nor infinitude; the
all-parameter result and continued-fraction obstruction are
(KPGZERO-1)--(KPGZERO-30).
The sole diagnostic for (PG110)--(PG114) and
(KPGSTAR-1)--(KPGSTAR-28) is the standalone standard-library script in
ops/TASK-20260719__explicit_pg49_star_exact_k/. It constructs only the
piecewise assignment (PG110), checks every Ferrers edge, and runs a direct
max-plus increasing-path DP plus every proper oriented arc, hence every
nontrivial shortcut, for \(m=3,\ldots,30\). Formula and comparator checks
continue through \(m=1000\). It enumerates no subset, path permutation, or
matching and imports no project or test helper.
The sole diagnostic for (KPG46Q-1)--(KPG46Q-29) is the standalone
standard-library script in
ops/TASK-20260719__pg46_threshold_closing_exact_k/. It constructs only the
closing interval shift \(\alpha_{q,2m-1}\), checks every Ferrers edge, and
runs a direct increasing-path max-plus DP plus every proper oriented arc for
\(m=3,\ldots,30\). Exact residue, singleton-inversion, formula, and
comparator checks continue through \(m=1000\). It enumerates no subset, path
permutation, matching, or cyclic-order family and imports no project or test
helper.

The following remain unresolved.

- **OPEN QUESTION:** can minimizing cyclic orders be characterized
  structurally in any residue class, beyond the displayed witnesses?
- **CLOSED LOCAL QUESTION:** under arbitrary whole-path reassignment with the
  present scaffold and orientations, (PG15) proves that \(P_0\) must remain
  in \(G_0\) whenever \(W^{(\le2)}\le T\). Every other gap is locally
  excluded, while \(G_0\) is only locally non-excluded.
- **CLOSED LOCAL QUESTION:** the complete generic path/gap relation at
  distances one and two is (PG31). Triple rows are the exact initial segments
  \(0\le j\le\ell_k\), and singleton rows contain every gap.
- **CLOSED LOCAL QUESTION:** the exact support of relation-compatible
  bijections is (PG49). The sole extendible edge in column zero is \((0,0)\);
  every local edge in a positive column is extendible by one of the explicit
  interval shifts. By itself this support theorem does not count the perfect
  matchings; (PG64)--(PG73) now supply that separate count.
- **CLOSED FULL-SCORE QUESTION:** (PG50)--(PG63) treat \(\alpha\) as arbitrary,
  classify every distance-three start and transition including cyclic closure,
  and prove \(W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha)\) for every
  bijection. Hence every relation-compatible bijection, including every shift
  above, has \(W=T=W_n\). Conversely, every full-optimal bijection in the
  scaffold is relation-compatible, so (PG49) is its exact edge support.
- **CLOSED COUNTING QUESTION:** (PG64)--(PG73) count those bijections exactly
  by the permanent of the reduced PG49 Ferrers board. The nested-neighborhood
  recurrence gives (PG69), with the dual row product (PG70), every endpoint
  and transition boundary, and the exact minimum value
  \(\mathsf F_3^{\rm lab}=36\).
  The count is labelled; it also equals the number of dihedral classes
  represented by this fixed scaffold because the canonical-order map is
  injective, not because a symmetry factor is removed.
- **CLOSED CORE-ORDER QUESTION:** the later theorem (KPG46-1)--(KPG46-21) in
  `research/FIXED_ORDER_CYCLE_RATIO.md` evaluates \(K\) exactly for the one
  PG46 shift placing \(P_m\) in \(G_{2m-1}\). Its unique maximizing subset,
  exact block sum, every shortcut boundary, minimum row, K825 crossover, and
  unchanged coefficient \(143/500\) are proved without inferring geometric
  or global optimality.
- **CLOSED CORE-ORDER QUESTION:** the later theorem
  (KPG46P-1)--(KPG46P-20) in `research/FIXED_ORDER_CYCLE_RATIO.md` evaluates
  \(K\) exactly for the other sharp PG46 shift, placing \(P_m\) in
  \(G_{2m-2}\). Its unique tail, terminal hole ranges, altered cyclic
  three-edge role, block sum, minimum row, and comparisons prove that it is
  strictly worse than both closing PG46 and K825 on every admitted row, with
  the same unchanged coefficient \(143/500\). No geometric or global
  conclusion follows.
- **CLOSED CORE-ORDER QUESTION:** (PG100)--(PG109) prove that the
  descending-min PG49 rule is a relation-compatible bijection for every
  \(m\ge3\). The separate theorem (KPGMIN-1)--(KPGMIN-39) evaluates its
  exact \(K\), classifies all maximizers including genuine zero-gain toggles,
  proves every exact comparison with K825 and the two PG46 witnesses, and
  proves that its cubic coefficient is transcendental and strictly worse
  than \(143/500\). No polynomial or eventual quasipolynomial formula and no
  geometric consequence result.
- **CLOSED CORE-ORDER QUESTION:** (PG110)--(PG114) prove that the explicit
  threshold-closing PG49-star assignment is a relation-compatible bijection
  for every \(m\ge3\). The separate theorem
  (KPGSTAR-1)--(KPGSTAR-28) proves its unique maximizing backbone, complete
  deletion-gain and shortcut audit including cyclic closure, five exact
  residue formulas, coefficient \(857/3000\), and strict improvement over
  K825 and both PG46 orders on every admitted row. No geometric or global
  optimality conclusion follows.
- **CLOSED CORE-ORDER QUESTION:** the interval shift (PG46) with target
  \((q,2m-1)\), \(q=\lfloor(4m+3)/5\rfloor\), keeps every residual path
  increasing. The separate theorem (KPG46Q-1)--(KPG46Q-29) proves its unique
  maximizing backbone, exact score and five residue formulas, every
  deletion gain and compressed shortcut, both cyclic-closing roles, and all
  comparisons with PG49-star, K825, and the two prior PG46 orders. Its exact
  excess over PG49-star is \(m(m-1)(m-2)/3\), so singleton reversal accounts
  for the full cubic PG49-star gain. No angular, geometric, or global
  minimizing-order conclusion follows.
- **OPEN QUESTION:** for which \(n\ge94\) is
  \(\mathcal M_n\subsetneq\mathcal M_n^{(\le2)}\)? Criterion (MS2)
  certifies equality whenever it holds, including \(n=94\), but no complete
  classification of subsequent indices is claimed.

No formula suggested by the nine values of \(W_n\) is promoted to a
conjecture. No geometric certificate, schema, serialized result artifact, or
CLI is created by this work.
