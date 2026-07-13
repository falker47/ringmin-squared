# All-n Bounds And Radius-One Insertion

Date: 2026-07-13

## Classification

- EXACT THEOREM: for every integer \(n\ge 3\),
  \[
  R_2^*(n)\ge {n(n+1)(n+2)\over 6\pi}-n^2.
  \]
- EXACT THEOREM: if \(n\ge 4\) and \(1\le m\le n-2\), then
  \[
  R_2^*(n)\ge {P_{m,n}\over \pi}-n^2,
  \]
  where
  \[
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  {(n-m+1)(m^2+4mn+m+n^2-n)\over 6}.
  \]
- EXACT THEOREM: within the specific relaxation "induced subset plus
  duplicated-multiset pairing plus
  \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\)", the best bound over all subsets of
  fixed cardinality \(q\) is achieved uniquely by the tail
  \(\{n-q+1,\dots,n\}\). Therefore no nonconsecutive subset improves the
  corresponding \(P_{m,n}\) bound inside this method.
- EXACT THEOREM: the discrete maximum of \(P_{m,n}\) over
  \(1\le m\le n-2\) is characterized exactly by
  \[
  \rho_n={\sqrt{8n^2+8n+1}-(2n+1)\over 2}.
  \]
  For \(n\ge 4\), if \(\rho_n\notin\mathbb Z\) the unique maximizer is
  \(m=\lfloor\rho_n\rfloor+1\); if \(\rho_n\in\mathbb Z\), the two maximizers
  are \(m=\rho_n\) and \(m=\rho_n+1\). For \(n=3\), the admissible set is the
  singleton \(m=1\).
- EXACT THEOREM:
  \[
  \liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}
  \ge
  4(\sqrt2-1)>1.
  \]
- EXACT THEOREM: if a configuration of the core radii
  \(2^2,\dots,n^2\) is feasible at central radius \(R>0\), then a circle of
  radius \(1\) can be inserted at the same central radius whenever
  \[
  \sum_{j=2}^n\theta_R(1,j^2)<\pi.
  \]
  The proof uses the measure of the union of all forbidden angular arcs and
  checks every new pairwise constraint.
- EXACT THEOREM: define \(R^*_{2:n}\) as the infimum feasible central radius
  for the core radii \(2^2,\dots,n^2\). Then
  \[
  R_2^*(n)=R^*_{2:n}\qquad(n\ge 12).
  \]
  In fact, for every \(n\ge12\), the full problem and the core problem have
  exactly the same set of feasible positive central radii. The threshold
  \(12\) is sufficient; no minimal-threshold claim is made.
- EXACT THEOREM: for every \(n\ge12\), the regular \((n-1)\)-gon construction
  for the core radii gives
  \[
  R_2^*(n)\le U_n,
  \]
  where
  \[
  U_n
  =
  \sqrt{
  n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
  +{(2n-1)^2\over4}}
  -{n^2+(n-1)^2\over2}.
  \]
  The construction verifies every core pair, including non-adjacent
  regular-polygon vertices, and then uses the exact radius-one insertion
  theorem.
- EXACT THEOREM:
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {1\over\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
  The \(\Theta(n^3)\) conclusion combines this construction with the
  induced-subset lower bound; it does not identify an exact leading constant.
- DISPROVED CLAIM:
  \[
  R_2^*(n)= {n^3\over 6\pi}(1+o(1)).
  \]
- DISPROVED CLAIM:
  \[
  R_2^*(n)= {n^3\over 6\pi}+O(n^2).
  \]

The lower-bound proof uses only necessary consequences of all-pairs feasibility.
The coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal for the specific relaxation
analyzed here. The regular-core construction gives a cubic upper bound with
coefficient \(1/\pi\), but the two coefficients do not match. Thus no exact
leading constant, limiting coefficient, or leading-term asymptotic formula is
proved.

## Domain And Definitions

Fix \(n\ge 3\). The Power-Ringmin radii are
\[
r_i=i^2,\qquad i=1,\dots,n.
\]

Let
\[
\mathcal F_n
=
\{R>0:\text{the radii }1^2,\dots,n^2\text{ are feasible at }R\}
\]
and
\[
\mathcal C_n
=
\{R>0:\text{the core radii }2^2,\dots,n^2\text{ are feasible at }R\}.
\]
In this note the optimum symbols mean infima:
\[
R_2^*(n)=\inf\mathcal F_n,
\qquad
R^*_{2:n}=\inf\mathcal C_n.
\]
No attainment assumption is used below.

For a central radius \(R>0\), the minimum central angle needed between two
peripheral circles of radii \(a,b>0\), both externally tangent to the central
circle, is
\[
\theta_R(a,b)
=
2\arcsin\sqrt{ab\over (R+a)(R+b)}.
\]
Thus for quadratic radii,
\[
\theta_R(i^2,j^2)
=
2\arcsin\left({ij\over \sqrt{(R+i^2)(R+j^2)}}\right).
\]

For \(n\ge 3\), a feasible configuration cannot have \(R=0\): at \(R=0\),
every center lies on a ray from the origin at distance \(i^2\), and two
peripheral circles of radii \(i^2,j^2\) are disjoint only when their rays are
opposite; three or more distinct peripheral circles cannot all be pairwise
opposite. Hence every feasible configuration relevant to \(R_2^*(n)\) has
\(R>0\), and the displayed angular formula applies.

## Combinatorial Pairing Lemma

Lemma. Let
\[
S=\{s_1<s_2<\cdots<s_q\}
\]
be a set of \(q\ge 3\) positive indices. Let
\[
M_S=\{s_1,s_1,s_2,s_2,\dots,s_q,s_q\}
\]
be sorted as
\[
x_1\le x_2\le \cdots\le x_{2q}.
\]
For every cyclic order \(\tau=(\tau_1,\dots,\tau_q)\) of \(S\),
\[
\sum_{\ell=1}^q \tau_\ell\tau_{\ell+1}
\ge
\sum_{\ell=1}^q x_\ell x_{2q+1-\ell},
\]
with \(\tau_{q+1}=\tau_1\).

Proof. First recall the standard rearrangement pairing form. Let
\[
x_1\le x_2\le \cdots \le x_{2q}
\]
be nonnegative real numbers. Among all partitions of these \(2q\) entries into
\(q\) unordered pairs, the sum of pair-products is minimized by pairing the
smallest entry with the largest, the second-smallest with the second-largest,
and so on:
\[
\sum_{\{p,r\}}x_px_r
\ge
\sum_{\ell=1}^q x_\ell x_{2q+1-\ell}.
\]
Indeed, in a minimizing pairing, if \(x_1\) is paired with \(x_j\) and
\(x_{2q}\) is paired with \(x_k\), where \(j<2q\), replacing those two pairs by
\(\{x_1,x_{2q}\}\) and \(\{x_j,x_k\}\) changes the product sum by
\[
\bigl(x_1x_j+x_kx_{2q}\bigr)
-
\bigl(x_1x_{2q}+x_kx_j\bigr)
=
(x_k-x_1)(x_{2q}-x_j)\ge 0.
\]
Thus some minimum has \(x_1\) paired with \(x_{2q}\), and induction gives the
claim.

The \(q\) adjacent edges of the cycle \(\tau\) use exactly two copies of every
index in \(S\), so they define a partition of \(M_S\) into \(q\) pairs, with
product sum \(\sum_\ell\tau_\ell\tau_{\ell+1}\). The rearrangement pairing
bound applies to that partition. The argument is a relaxation: it allows
pairings that need not be realizable as a Hamiltonian cycle, so equality is not
asserted.

For \(S=\{1,\dots,n\}\), this gives the older full-index bound
\[
\sum_{k=1}^n \sigma_k\sigma_{k+1}
\ge
{n(n+1)(n+2)\over 6}
\]
for every cyclic order \(\sigma\) of \(\{1,\dots,n\}\).

## Geometry To Induced Subset Gaps

Consider any feasible Power-Ringmin configuration for \(n\ge 3\) with central
radius \(R\). Let \(S\subseteq\{1,\dots,n\}\) have cardinality \(q\ge 3\).
Order only the centers whose indices lie in \(S\) by their polar angles around
the central center:
\[
\tau_1,\dots,\tau_q.
\]
Coincident polar angles cannot occur in a feasible configuration, since two
distinct peripheral centers on the same ray have distance
\(|i^2-j^2|<i^2+j^2\). Therefore the induced cyclic order is well-defined.

Let
\[
\Delta_\ell\in(0,2\pi),\qquad \ell=1,\dots,q,
\]
be the positive oriented angular gaps between consecutive \(S\)-centers in
this induced cyclic order. Each \(\Delta_\ell\) may contain centers whose
indices are not in \(S\), but the induced gaps still partition the full turn:
\[
\sum_{\ell=1}^q \Delta_\ell=2\pi.
\]

For the induced adjacent pair \(i=\tau_\ell\), \(j=\tau_{\ell+1}\), all-pairs
feasibility of the original configuration includes the non-overlap condition
for this pair. Their center distance must be at least \(i^2+j^2\). By the law
of cosines, with oriented central gap \(\Delta_\ell\), this condition is
equivalent to
\[
\sin^2{\Delta_\ell\over 2}
\ge
{i^2j^2\over (R+i^2)(R+j^2)}.
\]
Since \(R>0\), the right side is in \((0,1)\). With
\[
\theta_R(i^2,j^2)
=
2\arcsin\left({ij\over \sqrt{(R+i^2)(R+j^2)}}\right)
\in(0,\pi),
\]
the sine inequality and \(\Delta_\ell\in(0,2\pi)\) imply
\[
\Delta_\ell\in[\theta_R(i^2,j^2),\,2\pi-\theta_R(i^2,j^2)],
\]
and in particular
\[
\Delta_\ell\ge \theta_R(i^2,j^2).
\]
Summing over induced adjacent gaps gives
\[
2\pi
=
\sum_{\ell=1}^q\Delta_\ell
\ge
\sum_{\ell=1}^q\theta_R(\tau_\ell^2,\tau_{\ell+1}^2).
\]

This is the key strengthening over the full-cycle argument: the same adjacent
gap inequality applies to every induced subset \(S\), not only to
\(\{1,\dots,n\}\).

## Angular Inequality

For \(1\le i,j\le n\) and \(R>0\),
\[
\theta_R(i^2,j^2)
\ge
{2ij\over R+n^2}.
\]
Indeed, \(\arcsin x\ge x\) for \(x\in[0,1]\), and
\[
\sqrt{(R+i^2)(R+j^2)}\le R+n^2.
\]
Therefore
\[
2\arcsin\left({ij\over \sqrt{(R+i^2)(R+j^2)}}\right)
\ge
{2ij\over \sqrt{(R+i^2)(R+j^2)}}
\ge
{2ij\over R+n^2}.
\]

## Lower Bound From An Arbitrary Subset

Let \(S\subseteq\{1,\dots,n\}\) have \(q\ge 3\) indices, and let
\[
A(S)=\sum_{\ell=1}^q x_\ell x_{2q+1-\ell}
\]
be the anti-sorted pairing sum for the duplicated sorted multiset
\(M_S=\{x_1,\dots,x_{2q}\}\). Combining the induced-gap inequality, the angular
inequality, and the pairing lemma gives
\[
2\pi
\ge
\sum_{\ell=1}^q\theta_R(\tau_\ell^2,\tau_{\ell+1}^2)
\ge
{2\over R+n^2}
\sum_{\ell=1}^q\tau_\ell\tau_{\ell+1}
\ge
{2A(S)\over R+n^2}.
\]
Hence every feasible central radius \(R\) satisfies
\[
R\ge {A(S)\over\pi}-n^2.
\]
Taking the infimum over feasible \(R\) gives the same bound for \(R_2^*(n)\).

The pairing bound has the following explicit form. Write
\[
S=\{s_1<s_2<\cdots<s_q\}.
\]
If \(q=2t\) is even, then
\[
A(S)=2\sum_{a=1}^t s_a s_{2t+1-a}.
\]
If \(q=2t+1\) is odd, then
\[
A(S)=2\sum_{a=1}^t s_a s_{2t+2-a}+s_{t+1}^2.
\]
Indeed, in the duplicated sorted multiset, the two copies of each of the first
\(t\) indices are paired anti-sortingly with the two copies of the
corresponding last \(t\) indices. In the odd case one additional middle copy is
paired with the other middle copy, producing \(s_{t+1}^2\).

For \(S=\{1,\dots,n\}\), \(A(S)=n(n+1)(n+2)/6\), recovering
\[
R_2^*(n)\ge {n(n+1)(n+2)\over 6\pi}-n^2
\qquad(n\ge 3),
\]
and therefore the older consequence
\[
\liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}\ge 1.
\]

## Optimal Fixed-Cardinality Subsets In This Relaxation

Fix \(q\) with \(3\le q\le n\), and let
\[
T_q=\{n-q+1,n-q+2,\dots,n\}
\]
be the tail subset of cardinality \(q\). If
\[
S=\{s_1<s_2<\cdots<s_q\}\subseteq\{1,\dots,n\},
\]
then
\[
s_a\le n-q+a
\qquad(a=1,\dots,q).
\]
The explicit even and odd formulas for \(A(S)\) show that \(A\) is
coordinatewise nondecreasing for positive coordinates: each coordinate appears
in exactly one positive product, except for the odd middle coordinate, where it
appears as a positive square. Therefore
\[
A(S)\le A(T_q).
\]
The inequality is strict unless \(S=T_q\), because if \(S\ne T_q\) at least one
coordinate is strictly smaller than the corresponding tail coordinate and all
partner coordinates are positive.

Thus, among all subsets of a fixed cardinality \(q\), the method's best lower
bound is obtained uniquely by the consecutive tail. Writing
\[
m=n-q+1,
\]
this best fixed-cardinality pairing value is
\[
A(T_q)=A(\{m,m+1,\dots,n\})=P_{m,n}.
\]
Consequently, no nonconsecutive subset of \(\{1,\dots,n\}\) can improve on the
corresponding tail bound within the specific relaxation used here.

## Consecutive Large-Index Subsets

Now specialize to
\[
S=\{m,m+1,\dots,n\},
\qquad
1\le m\le n-2.
\]
The anti-sorted pairing of
\[
\{m,m,m+1,m+1,\dots,n,n\}
\]
pairs \(k\) with \(m+n-k\), counting both copies through the sum over
\(k=m,\dots,n\). Thus
\[
P_{m,n}
=
A(\{m,\dots,n\})
=
\sum_{k=m}^n k(m+n-k).
\]

Let \(q=n-m+1\). Since
\[
\sum_{k=m}^n k = {q(m+n)\over 2},
\]
and
\[
\sum_{k=m}^n k^2
=
{n(n+1)(2n+1)-(m-1)m(2m-1)\over 6},
\]
we get
\[
\begin{aligned}
P_{m,n}
&=
(m+n)\sum_{k=m}^n k-\sum_{k=m}^n k^2\\
&=
{(n-m+1)(m^2+4mn+m+n^2-n)\over 6}.
\end{aligned}
\]
Therefore, for \(n\ge 4\) and \(1\le m\le n-2\),
\[
R_2^*(n)\ge {P_{m,n}\over \pi}-n^2.
\]

## Exact Discrete Optimization Over Tails

For fixed \(n\), the best lower bound obtainable from this relaxation is
\[
{1\over\pi}\max_{1\le m\le n-2}P_{m,n}-n^2,
\]
with the trivial singleton domain \(m=1\) when \(n=3\). For \(n\ge 4\), the
discrete maximizers can be characterized exactly.

From the closed form, or directly by subtracting the tail sums,
\[
P_{m+1,n}-P_{m,n}
=
{n^2+n-m^2-(2n+1)m\over 2}.
\]
Denote this difference by \(D_{m,n}\). It is strictly decreasing in \(m\), since
\[
D_{m+1,n}-D_{m,n}=-(m+n+1)<0.
\]
Thus \(P_{m,n}\) is a discrete concave, unimodal sequence in \(m\).

The positive real root of \(D_{m,n}=0\) is
\[
\rho_n={\sqrt{8n^2+8n+1}-(2n+1)\over 2}.
\]
For \(n\ge 4\), one has \(1<\rho_n<n-2\), so the root lies inside the
admissible interval. The two inequalities follow by squaring the equivalent
positive comparisons
\[
\sqrt{8n^2+8n+1}>2n+3
\]
and
\[
\sqrt{8n^2+8n+1}<4n-3.
\]
They reduce respectively to \(4(n-2)(n+1)>0\) and
\(8(n^2-4n+1)>0\), both valid for \(n\ge 4\). Since \(D_{m,n}\ge 0\) exactly
when \(m\le\rho_n\), the maximizers are:

- if \(\rho_n\notin\mathbb Z\), the unique maximizer is
  \[
  m=\lfloor\rho_n\rfloor+1=\lceil\rho_n\rceil;
  \]
- if \(\rho_n\in\mathbb Z\), then \(D_{\rho_n,n}=0\), so
  \[
  P_{\rho_n,n}=P_{\rho_n+1,n},
  \]
  and the two maximizers are \(m=\rho_n\) and \(m=\rho_n+1\).

The tie cases are exactly those for which \(8n^2+8n+1\) is a square,
equivalently the Pell-type condition
\[
y^2-8r^2=1,\qquad r=\rho_n,\qquad n={2r-1+y\over 2}.
\]
No tie occurs otherwise.

## Asymptotic Optimization

Let
\[
m=\alpha n+O(1),
\qquad 0\le \alpha<1.
\]
Using the closed form for \(P_{m,n}\),
\[
P_{m,n}
=
{(1-\alpha)(\alpha^2+4\alpha+1)\over 6}\,n^3
+O(n^2).
\]
Define
\[
\phi(\alpha)
=
{(1-\alpha)(\alpha^2+4\alpha+1)\over 6}.
\]
Then
\[
\phi'(\alpha)
=
{1-2\alpha-\alpha^2\over 2},
\qquad
\phi''(\alpha)=-(1+\alpha)<0.
\]
The unique maximum on \([0,1]\) is therefore
\[
\alpha_0=\sqrt2-1.
\]
At this value,
\[
\alpha_0^2+4\alpha_0+1=2\sqrt2,
\qquad
1-\alpha_0=2-\sqrt2,
\]
so
\[
\phi(\alpha_0)
=
{2(\sqrt2-1)\over 3}.
\]

The rounding is harmless and explicit. Choose
\[
m_n=\lceil(\sqrt2-1)n\rceil
=(\sqrt2-1)n+\varepsilon_n,
\qquad 0\le\varepsilon_n<1.
\]
For \(n\ge 4\), this gives \(1\le m_n\le n-2\). Substituting
\(m_n=(\sqrt2-1)n+\varepsilon_n\) into the exact formula gives
\[
P_{m_n,n}
=
{2(\sqrt2-1)\over 3}n^3
+(\sqrt2-1)n^2
+{ -3\sqrt2\,\varepsilon_n^2+6\varepsilon_n+\sqrt2-2\over 6}\,n
+{(1-\varepsilon_n)(\varepsilon_n^2+\varepsilon_n)\over 6}.
\]
Because \(0\le\varepsilon_n<1\), the last two terms are \(O(n)\), uniformly in
\(n\). Hence
\[
P_{m_n,n}
=
{2(\sqrt2-1)\over 3}n^3+O(n^2),
\]
and the induced-subset lower bound gives
\[
R_2^*(n)
\ge
{2(\sqrt2-1)\over 3\pi}n^3
-O(n^2).
\]
Consequently,
\[
\liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}
\ge
4(\sqrt2-1)>1.
\]

The preceding fixed-cardinality and discrete-optimization results show a
method-specific optimality statement: the coefficient
\[
{2(\sqrt2-1)\over 3\pi}
\]
is the largest leading coefficient obtainable from the relaxation consisting
only of induced subsets, duplicated-multiset pairing, and
\(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\). This is not an upper bound and does not
assert that the same coefficient is the exact asymptotic leading constant for
Power-Ringmin.

This contradicts any asymptotic formula whose normalized ratio
\(6\pi R_2^*(n)/n^3\) tends to \(1\). Therefore
\[
R_2^*(n)= {n^3\over 6\pi}(1+o(1))
\]
is a disproved claim. The stronger target
\[
R_2^*(n)= {n^3\over 6\pi}+O(n^2)
\]
is also a disproved claim, since it would also force the normalized ratio to
tend to \(1\).

## Exact Radius-One Insertion

The following result turns the finite reduced-core observation into an exact
eventual theorem. Its proof does not use the checked cases \(n=5,6\).

### Forbidden-arc lemma

Consider a feasible configuration of the core radii \(2^2,\dots,n^2\) at
central radius \(R>0\). Let \(\phi_j\) be the polar angle of the center of the
circle of radius \(j^2\). On the angular circle
\(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let
\(d_{\mathbb T}\in[0,\pi]\) denote circular distance and define
\[
B_j
=
\{\alpha\in\mathbb T:
d_{\mathbb T}(\alpha,\phi_j)<\theta_R(1,j^2)\}.
\]
Because \(0<\theta_R(1,j^2)<\pi\), the set \(B_j\) is an open arc of angular
measure \(2\theta_R(1,j^2)\). Hence
\[
\mu\!\left(\bigcup_{j=2}^n B_j\right)
\le
\sum_{j=2}^n\mu(B_j)
=
2\sum_{j=2}^n\theta_R(1,j^2).
\]
If the angular sum is less than \(\pi\), the union has measure less than
\(2\pi\). Choose \(\alpha\) outside that union and place the new center at
polar coordinates \((R+1,\alpha)\).

This construction checks all constraints introduced by the new circle.

1. Its center is at distance \(R+1\) from the central center, so the new circle
   is externally tangent to the central circle.
2. For every \(j=2,\dots,n\), put
   \(\delta_j=d_{\mathbb T}(\alpha,\phi_j)\). Since
   \(\alpha\notin B_j\), one has
   \(\delta_j\ge\theta_R(1,j^2)\). The squared distance to the \(j\)-th
   center is
   \[
   d_j^2
   =
   (j^2-1)^2
   +4(R+1)(R+j^2)\sin^2(\delta_j/2).
   \]
   Because \(0\le\delta_j\le\pi\), the sine is increasing on the relevant
   half-angle interval. By the definition of \(\theta_R\),
   \[
   d_j^2
   \ge
   (j^2-1)^2+4j^2
   =
   (j^2+1)^2.
   \]
   Thus every one of the \(n-1\) new peripheral pairwise constraints
   \((1,j^2)\) holds; equality is permitted because tangent peripheral
   circles have disjoint interiors.
3. Every core-core pairwise constraint is unchanged.

There are no other new constraints. This proves the insertion criterion.

### Angular majorant

For \(R>0\) and \(j\ge2\), set
\[
x={j\over\sqrt{(R+1)(R+j^2)}}
\quad\text{and}\quad
y=\arcsin x.
\]
Since \(0<y<\pi/2\), one has \(y<\tan y\). Also
\[
(R+1)(R+j^2)-j^2=R(R+j^2+1).
\]
Therefore
\[
\theta_R(1,j^2)
=2\arcsin x
< {2x\over\sqrt{1-x^2}}
= {2j\over\sqrt{R(R+j^2+1)}}
< {2j\over R}.
\tag{1}
\]
In particular, with
\[
S_n=2\sum_{j=2}^n j=n(n+1)-2,
\]
equation (1) gives
\[
\sum_{j=2}^n\theta_R(1,j^2)<{S_n\over R}.
\tag{2}
\]

We use the elementary rational bounds
\[
{31\over10}<\pi<{22\over7}.
\tag{3}
\]
For completeness, the upper bound follows from the positive integral identity
\[
{22\over7}-\pi
=
\int_0^1{x^4(1-x)^4\over1+x^2}\,dx>0.
\]
For the lower bound, the perimeter of the regular dodecagon inscribed in the
unit circle gives
\[
\pi>3(\sqrt6-\sqrt2)>{31\over10}.
\]
The last comparison is purely algebraic; after two squarings of positive
quantities its strict margin is
\(6239^2-3\cdot3600^2=45121>0\).

### Configuration-level core lower bound

The induced-subset theorem above must be reapplied to a core configuration;
the scalar lower bound for the full optimum alone would not imply a lower
bound for the smaller core optimum. If \(R\in\mathcal C_n\) and
\(2\le m\le n-2\), apply the already-proved induced-gap and pairing argument
to the tail \(\{m,m+1,\dots,n\}\), which is present in the core. It gives
\[
R\ge {P_{m,n}\over\pi}-n^2,
\qquad
P_{m,n}=\sum_{k=m}^n k(m+n-k).
\tag{4}
\]
This is a statement about every feasible core configuration, not about an
unattained infimum.

### The boundary case \(n=12\)

For \(m=6\), one has \(P_{6,12}=539\). Equations (3)--(4) give, for every
\(R\in\mathcal C_{12}\),
\[
R\ge{539\over\pi}-144>{7\cdot539\over22}-144={55\over2}.
\]
Put \(R_0=55/2\). For \(j=2,\dots,12\), equation (1) is bounded at \(R_0\)
by \(k_j/1000\), using the following exact integer checks. The first
majorant in (1) is strictly decreasing in \(R\), so an upper bound at \(R_0\)
also bounds every feasible \(R>R_0\).

| \(j\) | \(k_j\) | \(k_j^2\,55(57+2j^2)-16{,}000{,}000j^2\) |
|---:|---:|---:|
| 2 | 134 | 192700 |
| 3 | 187 | 247125 |
| 4 | 229 | 698695 |
| 5 | 261 | 892085 |
| 6 | 285 | 291375 |
| 7 | 304 | 3846400 |
| 8 | 318 | 4936700 |
| 9 | 329 | 7762845 |
| 10 | 337 | 5297815 |
| 11 | 344 | 10035520 |
| 12 | 349 | 7173975 |

Every margin is positive, which after squaring positive quantities proves
\[
{2j\over\sqrt{R_0(R_0+j^2+1)}}<{k_j\over1000}.
\]
Since \(\sum_{j=2}^{12}k_j=3077\),
\[
\sum_{j=2}^{12}\theta_R(1,j^2)
<{3077\over1000}
<{31\over10}
<\pi.
\tag{5}
\]

### The boundary case \(n=13\)

Here \(P_{6,13}=680\), so every \(R\in\mathcal C_{13}\) satisfies
\[
R\ge{680\over\pi}-169>{521\over11}>47.
\]
For
\[
f_R(x)={x\over\sqrt{R+x^2+1}},
\]
one has \(f_R'(x)>0\). Hence the right-interval integral bound gives
\[
\sum_{j=2}^{13}f_R(j)
\le
\int_2^{14}f_R(x)\,dx
=
\sqrt{R+197}-\sqrt{R+5}.
\]
Combining this with (1) and rationalizing yields
\[
\sum_{j=2}^{13}\theta_R(1,j^2)
<
{384\over
\sqrt{R(R+197)}+\sqrt{R(R+5)}}.
\]
For \(R>47\), the denominator is greater than
\[
\sqrt{47\cdot244}+\sqrt{47\cdot52}
>107+49=156,
\]
because \(107^2<47\cdot244\) and \(49^2<47\cdot52\). Consequently
\[
\sum_{j=2}^{13}\theta_R(1,j^2)
<{384\over156}
={32\over13}
<3
<\pi.
\tag{6}
\]

### Uniform estimate for \(n\ge14\)

Let \(m=\lfloor n/2\rfloor\). If \(n=2t\), then
\[
P_{m,n}={t(t+1)(13t-1)\over6};
\]
if \(n=2t+1\), then
\[
P_{m,n}={t(t+2)(13t+7)\over6}.
\]
For \(t\ge7\), both cases satisfy
\[
P_{m,n}\ge {29\over7}n^2+n-2.
\tag{7}
\]
Indeed, after multiplying the difference in (7) by \(42\) and putting
\(u=t-7\ge0\), the even and odd cases respectively become
\[
91u^3+1299u^2+4718u+672>0
\]
and
\[
91u^3+1446u^2+6185u+3522>0.
\]
Using (3), (4), and (7), every \(R\in\mathcal C_n\) satisfies
\[
R
\ge {P_{m,n}\over\pi}-n^2
={P_{m,n}-\pi n^2\over\pi}
>{S_n\over\pi}.
\]
Equation (2) therefore gives
\[
\sum_{j=2}^n\theta_R(1,j^2)<{S_n\over R}<\pi
\qquad(n\ge14).
\tag{8}
\]

### Equality of feasible-radius sets and infima

Restriction of a full configuration to its core always gives
\(\mathcal F_n\subseteq\mathcal C_n\). Conversely, equations (5), (6), and
(8), followed by the forbidden-arc lemma, show that every
\(R\in\mathcal C_n\) also belongs to \(\mathcal F_n\) when \(n\ge12\).
Thus
\[
\mathcal F_n=\mathcal C_n\qquad(n\ge12).
\]
Taking infima of equal sets proves
\[
\boxed{R_2^*(n)=R^*_{2:n}\qquad(n\ge12)}.
\]
No core minimizer, full minimizer, or limiting configuration was assumed. The
argument does not prove that \(12\) is the least possible threshold. The same
chain of lower and upper bounds does not close \(n=11\), which is a limitation
of this proof and not a counterexample to equality at \(n=11\).

## Regular-Core Cubic Upper Bound

We now give an explicit feasible construction. This section checks every
pairwise constraint directly; checking only neighboring vertices would not be
sufficient.

### Worst pair at fixed radius

Fix \(n\ge12\) and \(R>0\), and define
\[
h_R(x)={x\over\sqrt{R+x^2}}\qquad(x>0).
\]
Then
\[
h_R'(x)={R\over(R+x^2)^{3/2}}>0.
\]
For distinct core indices \(2\le i<j\le n\),
\[
\theta_R(i^2,j^2)
=2\arcsin\bigl(h_R(i)h_R(j)\bigr).
\]
Both \(h_R\) and \(\arcsin\) are strictly increasing on the relevant
domains. Therefore the unique largest required angular separation among
distinct core radii is
\[
\theta_R((n-1)^2,n^2).
\tag{9}
\]
This is an exact fixed-\(R\) monotonicity statement, not a finite numerical
observation.

### Solving for a sufficient radius

Put
\[
\gamma_n={\pi\over n-1},\qquad A=(n-1)^2,\qquad B=n^2.
\]
For \(n\ge12\), one has \(0<\gamma_n<\pi/2\). Hence
\[
\theta_R(A,B)\le {2\pi\over n-1}
\]
is equivalent to
\[
{n(n-1)\over\sqrt{(R+A)(R+B)}}\le\sin\gamma_n,
\]
or
\[
(R+A)(R+B)\ge AB\csc^2\gamma_n.
\tag{10}
\]
Completing the square in (10) gives
\[
\left(R+{A+B\over2}\right)^2
\ge
AB\csc^2\gamma_n+{(B-A)^2\over4}.
\]
The left side is strictly increasing for \(R\ge0\). Since
\(\csc^2\gamma_n>1\), the unique nonnegative threshold is positive and equals
\[
\boxed{
U_n
=
\sqrt{
n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
+{(2n-1)^2\over4}}
-{n^2+(n-1)^2\over2}
}.
\tag{11}
\]
At \(R=U_n\), equality holds in (10), so
\[
\theta_{U_n}((n-1)^2,n^2)={2\pi\over n-1}.
\tag{12}
\]

### All-pairs feasibility of the regular core

Use the vertex directions of a regular \((n-1)\)-gon centered at the central
center. Explicitly, in one bijective assignment put
\[
\phi_i={2\pi(i-2)\over n-1}
\qquad(i=2,\dots,n)
\]
and place the center of the radius-\(i^2\) circle at
\[
(U_n+i^2)(\cos\phi_i,\sin\phi_i).
\]
Thus all polar angles are equally spaced, while the differing radial distances
correctly enforce external tangency to the central circle. Any permutation of
the radii among these directions has the same argument below.

Let two distinct vertices be separated by the smaller circular step \(q\),
where
\[
1\le q\le\left\lfloor{n-1\over2}\right\rfloor.
\]
Their smaller central angle is
\[
\delta={2\pi q\over n-1}\in(0,\pi],
\]
and therefore
\[
\delta\ge {2\pi\over n-1}.
\tag{13}
\]
For peripheral radii \(a,b>0\) at smaller central angle
\(\delta\in[0,\pi]\), the squared center distance is
\[
d^2
=(a-b)^2+4(U_n+a)(U_n+b)\sin^2(\delta/2).
\]
Consequently,
\[
d^2\ge(a+b)^2
\quad\Longleftrightarrow\quad
\sin^2(\delta/2)
\ge {ab\over(U_n+a)(U_n+b)}
\quad\Longleftrightarrow\quad
\delta\ge\theta_{U_n}(a,b).
\tag{14}
\]
By (9), (12), and (13), every pair \(2\le i<j\le n\) satisfies
\[
\delta
\ge {2\pi\over n-1}
=\theta_{U_n}((n-1)^2,n^2)
\ge\theta_{U_n}(i^2,j^2).
\]
Equation (14) proves non-overlap for all \(\binom{n-1}{2}\) core pairs.
This explicitly includes non-adjacent vertex pairs \(q>1\); they have more
available angular separation than an edge pair. Equality is allowed because
external tangency gives disjoint interiors. Hence \(U_n\in\mathcal C_n\).

### Insertion and asymptotic consequences

For \(n\ge12\), the exact radius-one theorem above proves
\(\mathcal C_n=\mathcal F_n\). Since the regular core is actually feasible at
\(U_n\), it follows directly that \(U_n\in\mathcal F_n\), and thus
\[
\boxed{R_2^*(n)\le U_n\qquad(n\ge12)}.
\tag{15}
\]
This implication uses equality of feasible-radius sets and does not assume
that either infimum is attained.

To evaluate (11), write
\[
X_n=n(n-1)\csc\!\left({\pi\over n-1}\right),
\quad
Y_n={2n-1\over2},
\quad
Z_n={n^2+(n-1)^2\over2},
\]
so that \(U_n=\sqrt{X_n^2+Y_n^2}-Z_n\). The standard limit
\(x/\sin x\to1\) gives
\[
{X_n\over n^3}
=
{(n-1)^2\over n^2}
{1\over (n-1)\sin(\pi/(n-1))}
\longrightarrow {1\over\pi},
\]
whereas \(Y_n/n^3\to0\) and \(Z_n/n^3\to0\). Therefore
\[
{U_n\over n^3}\longrightarrow {1\over\pi},
\qquad
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {1\over\pi}.
\tag{16}
\]
Combining (16) with the exact induced-subset lower bound already proved in
this note yields
\[
{2(\sqrt2-1)\over3\pi}
\le
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\le
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le {1\over\pi}.
\tag{17}
\]
In particular,
\[
\boxed{R_2^*(n)=\Theta(n^3)}.
\]
The coefficient gap in (17) remains open. Neither this construction nor the
lower bound proves that \(R_2^*(n)/n^3\) has a limit, and no exact leading
constant is claimed.

## Gap And Counterexample Audit

- The induced gaps are valid even when skipped non-\(S\) centers lie inside
  them: they are positive oriented arcs between consecutive \(S\)-centers and
  still sum to \(2\pi\).
- The induced adjacent endpoints need not be adjacent in the full order. This
  is not a gap, because all-pairs feasibility applies directly to every pair of
  endpoints in the original configuration.
- The sine condition gives both
  \(\Delta_\ell\ge\theta_R(i^2,j^2)\) and
  \(\Delta_\ell\le2\pi-\theta_R(i^2,j^2)\). The lower-bound proof uses only
  the first inequality.
- The pairing lemma is a relaxation over all pair partitions of the duplicated
  subset multiset. Relaxing the cyclic-order constraint can only lower the
  product sum used in a necessary lower bound, so it cannot invalidate the
  lower bound.
- The angular inequality uses \(R+n^2\), the largest radius scale in the full
  \(n\)-circle instance. This is weaker than using the maximum index in a
  smaller subset, but it is valid for all \(i,j\le n\) and is exactly what is
  needed for \(S=\{m,\dots,n\}\).
- The fixed-cardinality extremal result is a theorem about the pairing
  relaxation \(A(S)\), not about cyclic orders themselves. It proves that no
  nonconsecutive subset improves this method's bound, but it does not rule out
  stronger lower-bound methods.
- The asymptotic optimization uses an integer choice
  \(m_n=\lceil(\sqrt2-1)n\rceil\) with an explicit bounded rounding parameter
  \(\varepsilon_n\). The exact finite maximizers are characterized separately
  by \(\rho_n\), so no real-valued \(m\) is used as an index.
- The regular-core construction supplies a cubic upper bound, but not one
  matching the induced-subset lower coefficient. It must not be described as
  identifying the exact asymptotic leading constant for Power-Ringmin. The
  coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal only inside the lower-bound
  relaxation explicitly analyzed above.
- The radius-one theorem reapplies the configuration-level induced-subset
  argument to a subset already present in the core. Inferring a core lower
  bound only from the scalar full-problem lower bound would reverse the useful
  implication and would be invalid.
- The forbidden arcs are open and each has measure \(2\theta_R(1,j^2)\), not
  \(\theta_R(1,j^2)\). Their union may overlap; subadditivity is all that is
  needed.
- The equality for \(n\ge12\) is an exact all-configuration theorem, not an
  extrapolation from the checked cases \(n=5,6\).
- The threshold \(12\) is sufficient and explicit, not claimed minimal. No
  conclusion for \(n\le11\) follows from the failure of this proof chain.
- The worst-pair reduction assumes \(R>0\), as does the angular formulation.
  At \(R=0\), the strict monotonicity used in (9) would fail.
- The regular-core proof uses the smaller circular separation for every
  unordered vertex pair. Non-adjacent pairs are not inferred from neighboring
  constraints; they are checked directly through (13)--(14).
- The formula \(U_n\) is a feasible radius, not a claim that the regular core
  is optimal or that the full infimum is attained there.
