# All-n Adjacent-Product Lower Bound

Date: 2026-07-12

## Classification

- EXACT THEOREM: for every integer \(n\ge 3\),
  \[
  R_2^*(n)\ge {n(n+1)(n+2)\over 6\pi}-n^2.
  \]
- EXACT THEOREM:
  \[
  \liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}\ge 1.
  \]

These statements use only the defining all-pairs feasibility condition through
its adjacent-pair consequences. They do not prove a matching upper bound.

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

If a feasible configuration has cyclic index order
\[
\sigma=(\sigma_1,\dots,\sigma_n),
\]
indices are read modulo \(n\), so \(\sigma_{n+1}=\sigma_1\).

## Combinatorial Lemma

Lemma. For every cyclic order \(\sigma\) of \(\{1,\dots,n\}\),
\[
\sum_{k=1}^n \sigma_k\sigma_{k+1}
\ge
{n(n+1)(n+2)\over 6}.
\]

Proof. First recall the standard rearrangement pairing form. Let
\[
x_1\le x_2\le \cdots \le x_{2m}
\]
be nonnegative real numbers. Among all partitions of these \(2m\) entries into
\(m\) unordered pairs, the sum of pair-products is minimized by pairing the
smallest entry with the largest, the second-smallest with the second-largest,
and so on:
\[
\sum_{\{p,q\}}x_px_q
\ge
\sum_{p=1}^m x_p x_{2m+1-p}.
\]
Indeed, in a minimizing pairing, if \(x_1\) is paired with \(x_j\) and
\(x_{2m}\) is paired with \(x_k\), where \(j<2m\), replacing those two pairs by
\(\{x_1,x_{2m}\}\) and \(\{x_j,x_k\}\) changes the product sum by
\[
\bigl(x_1x_j+x_kx_{2m}\bigr)
-
\bigl(x_1x_{2m}+x_kx_j\bigr)
=
(x_k-x_1)(x_{2m}-x_j)\ge 0.
\]
Thus some minimum has \(x_1\) paired with \(x_{2m}\), and induction gives the
claim.

Apply this to the sorted multiset
\[
M_n=\{1,1,2,2,\dots,n,n\}.
\]
The \(n\) adjacent edges of the cycle \(\sigma\) use exactly two copies of every
index, so they define a partition of \(M_n\) into \(n\) pairs, with product sum
\(\sum_k\sigma_k\sigma_{k+1}\). Therefore this cyclic product sum is bounded
below by the anti-sorted pairing sum for \(M_n\).

If \(n=2m\), this anti-sorted sum is
\[
2\sum_{i=1}^m i(2m+1-i)
=
{n(n+1)(n+2)\over 6}.
\]
If \(n=2m-1\), it is
\[
2\sum_{i=1}^{m-1} i(2m-i)+m^2
=
{n(n+1)(n+2)\over 6}.
\]
This proves the lemma. The argument is a relaxation: it allows pairings that
need not be realizable as a Hamiltonian cycle, so equality is not asserted.

## Geometry To Adjacent Gaps

Consider any feasible Power-Ringmin configuration for \(n\ge 3\) with central
radius \(R\). Let the peripheral centers be ordered by their polar angles around
the central center:
\[
\sigma_1,\dots,\sigma_n.
\]
Coincident polar angles cannot occur in a feasible configuration, since two
distinct peripheral centers on the same ray have distance
\(|i^2-j^2|<i^2+j^2\). Let
\[
\delta_k\in(0,2\pi),\qquad k=1,\dots,n,
\]
be the positive oriented angular gaps between consecutive centers in this
cyclic order. Then
\[
\sum_{k=1}^n\delta_k=2\pi.
\]

For the adjacent pair \(i=\sigma_k\), \(j=\sigma_{k+1}\), all-pairs feasibility
includes the non-overlap condition for this pair. Their center distance must be
at least \(i^2+j^2\). By the law of cosines, with central gap \(\delta_k\),
this condition is equivalent to
\[
\sin^2{\delta_k\over 2}
\ge
{i^2j^2\over (R+i^2)(R+j^2)}.
\]
Since \(R>0\), the right side is in \((0,1)\). Let
\[
\theta_R(i^2,j^2)
=
2\arcsin\left({ij\over \sqrt{(R+i^2)(R+j^2)}}\right)
\in(0,\pi).
\]
For \(\delta_k\in(0,2\pi)\), the last sine inequality implies
\[
\delta_k\in[\theta_R(i^2,j^2),\,2\pi-\theta_R(i^2,j^2)],
\]
and in particular
\[
\delta_k\ge \theta_R(i^2,j^2).
\]
Summing over adjacent gaps gives the adjacent-chain lower bound
\[
2\pi
=
\sum_{k=1}^n\delta_k
\ge
\sum_{k=1}^n\theta_R(\sigma_k^2,\sigma_{k+1}^2).
\]

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

## Lower Bound For \(R_2^*(n)\)

Combining the adjacent-gap inequality, the angular inequality, and the
combinatorial lemma,
\[
2\pi
\ge
\sum_{k=1}^n\theta_R(\sigma_k^2,\sigma_{k+1}^2)
\ge
{2\over R+n^2}
\sum_{k=1}^n\sigma_k\sigma_{k+1}
\ge
{2\over R+n^2}\,{n(n+1)(n+2)\over 6}.
\]
Hence every feasible central radius \(R\) satisfies
\[
R+n^2\ge {n(n+1)(n+2)\over 6\pi},
\]
or
\[
R\ge {n(n+1)(n+2)\over 6\pi}-n^2.
\]
Taking the infimum, and therefore also the minimum when the minimum is known to
exist, gives
\[
R_2^*(n)\ge {n(n+1)(n+2)\over 6\pi}-n^2
\qquad(n\ge 3).
\]

Finally,
\[
{6\pi R_2^*(n)\over n^3}
\ge
{n(n+1)(n+2)\over n^3}-{6\pi\over n}
=
1+{3\over n}+{2\over n^2}-{6\pi\over n},
\]
so
\[
\liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}\ge 1.
\]

## Role Of Non-Adjacent Constraints

This lower bound is valid because every all-pairs feasible configuration is, in
particular, adjacent-pair feasible along its cyclic order. The proof deliberately
relaxes the full problem to adjacent gaps only; relaxing constraints can only
make lower bounds weaker, not invalid.

The same relaxation is not enough for a matching upper bound. To prove
\[
R_2^*(n)\le {n^3\over 6\pi}(1+o(1))
\]
or the stronger \(n^3/(6\pi)+O(n^2)\) target, one must construct actual
placements or fixed-order angle variables satisfying all non-adjacent pair
constraints as well as adjacent ones. In other words, non-adjacent checks are
not needed for this lower bound, but they remain the main obstruction for the
matching upper-bound direction.
