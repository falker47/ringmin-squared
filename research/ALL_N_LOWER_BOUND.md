# All-n Induced-Subset Lower Bound

Date: 2026-07-12

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
analyzed here. This does not prove an exact leading constant, a matching upper
bound, or optimality for Power-Ringmin itself.

## Domain And Definitions

Fix \(n\ge 3\). The Power-Ringmin radii are
\[
r_i=i^2,\qquad i=1,\dots,n.
\]

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
- This proof does not supply a matching upper bound and must not be described
  as identifying the exact asymptotic leading constant for Power-Ringmin. The
  coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal only inside the relaxation
  explicitly analyzed above.
