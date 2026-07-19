# Power-Ringmin: Quadratic Radii

Working repository name: `power-ringmin`

Author: Maurizio Falconi

Status: independent mathematical research project

This file is the authoritative project brief.

## Summary

Power-Ringmin studies the quadratic-radii extension of Ringmin. Given peripheral circles with radii

\[
1^2,2^2,\dots,n^2,
\]

place all of them externally tangent to one central circle while requiring pairwise-disjoint peripheral interiors.

Definition: \(R_2^*(n)\) is the infimum feasible central radius. No general
attainment assumption is needed for the current theorems.

The quadratic-radii computational foundation has been implemented. Checked
finite interval certificate artifacts currently exist for `n=3,4,5,6`; they
provide finite global radius brackets under the documented guarded `mpmath.iv`
interval-backend contract. A separate test-only 384-bit Arb path through
python-flint independently corroborates the decisive endpoint signs and
complete embedded coverage of the checked `n=3` record. It does not cover
`n=4,5,6` or change any production backend, artifact, bracket, schema,
classification, or certified claim.

The fixed-order certification semantics are now proved independently in
`research/FIXED_ORDER_ANGULAR_STN.md`: exact all-pairs geometry is equivalent
to the implemented difference constraints, negative cycles characterize
infeasibility, shortest paths recover feasible potentials, and a verified
interval bracket has exact endpoint meaning \((L,U]\). The proof is real
mathematics; applying it to checked artifacts remains conditional on the
guarded `mpmath.iv` trust contract.

For \(n\ge3\), the complete fixed-order STN now also has an exact maximum
cyclic ratio. For a complete order \(\sigma\), let \(q(C)\) count `wrap_upper` edge
occurrences, while \(S(C)\) sums endpoint-index products over all directed
edge occurrences, with multiplicity. Then
\[
\Lambda(\sigma)=\max_C{S(C)\over q(C)}
\]
is well-defined because every directed cycle has \(q(C)\ge1\), and
the score is exactly one-wrap saturated. Writing
\(\Lambda^{(1)}(\sigma)=\max_{q(C)=1}S(C)\), one has
\[
\Lambda(\sigma)=\Lambda^{(1)}(\sigma)
=
\max_{|T|\ge2}
\sum_r\sigma_{i_r}\sigma_{i_{r+1\bmod |T|}}
=\max_{T\ne\varnothing}P_\sigma(T),
\]
where \(i_0<\cdots<i_{|T|-1}\) are the positions induced by \(T\),
\(P_\sigma(T)\) denotes the displayed cyclic sum, singleton sums use
\(P_\sigma(\{i\})=\sigma_i^2\), and a two-element subset counts its product
twice. This is an exact theorem for every complete order, so the scores are
integers. If \(\tau\) is the core order obtained by deleting label \(1\),
define
\[
K(\tau)=
\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U).
\]
Treating separately \(\{1\}\), \(\{1,j\}\), and subsets in which \(1\)
has two core neighbors proves the exact insertion-independent reduction
\[
\Lambda(\sigma)=K(\tau),
\qquad
\Lambda_n=\min_\tau K(\tau).
\]
The accepted same-order comparison then gives
\[
\Lambda_n\le(n-1)W_n,
\qquad
R_2^*(n)<{\Lambda_n\over\pi}
\le{(n-1)W_n\over\pi}
\quad(n\ge3).
\]
The last chain is an upper bound and does not identify the \(K\)- and
\(W\)-minimizers. Moreover,
\[
{\Lambda(\sigma)\over\pi}-n^2
<\rho_\sigma
<{\Lambda(\sigma)\over\pi}.
\]
For \(\Lambda_n=\min_\sigma\Lambda(\sigma)\), the same strict sandwich holds
globally for \(n\ge3\) and gives
\(0<\Lambda_n-\pi R_2^*(n)<\pi n^2\). An exact `Fraction` scorer uses
descending-path compression and maximum-cycle-mean dynamic programming, not
cycle enumeration. Bounded exhaustive computation for `n=3..8` gives
\((12,26,47,77,118,172)\). A test-only subset/path oracle independent of
Karp verifies the saturation property on all 2,956 bounded canonical orders,
without increasing the production limit. A second test-only regression checks
all 437 canonical core orders and 2,957 insertion gaps, including the explicit
two-arc \(n=3\) case, and recovers core minimizer counts
`(1,1,1,3,4,12)`. This finite table is not a closed-form evaluation of the
reduced minimum, and \(K\) remains distinct from the regular-direction core
surrogate \(W\).

The reduced problem is now classified exactly at \(n=9\), still without
moving the production boundary. Equality in the finite \(S_6/S_5\) lemma
forces the induced cycle
\(\Omega=(9,5,8,6,7,4)\) up to dihedral symmetry. Label \(3\) must occupy
one of the four gaps of \(\Omega\) not incident to label \(4\), after which
label \(2\) may occupy any of the seven resulting gaps. Thus
\[
\Lambda_9=239,
\qquad
\#\{\text{dihedral core minimizers}\}=28.
\]
Exact label-one elimination/insertion gives \(28\cdot8=224\) complete
dihedral minimizer classes. All 28 core classes maximize on
\(S_6=\{4,\ldots,9\}\); 27 do so uniquely, while the class represented by
`(9,4,7,6,8,3,2,5)` also maximizes on the full core. An independent
test-only oracle directly checks all \(7!/2=2{,}520\) core classes and all
255 nonempty subsets of each, recording every argmax, without calling the
public enumerator or production scorer. The public complete-order domain
remains `n<=8`. These are finite exact combinatorial results, not an exact
value of \(R_2^*(9)\), a geometric classification, or an all-\(n\) formula.

The next reduced value is also exact, still with no production change. For
every cycle on \(\{4,\ldots,10\}\), the duplicated-pairing relaxation on
\(\{5,\ldots,10\}\), its complete human-checkable classification at the
only relevant values 320--322, and the exact label-four insertion correction
prove
\[
\max\{P_\omega(\{4,\ldots,10\}),P_\omega(\{5,\ldots,10\})\}\ge323.
\]
The shortcut-gain certificate for
\(\tau=(10,2,3,4,7,8,6,9,5)\) gives \(K(\tau)=323\), with exactly the two
maximizing subsets \(\{5,\ldots,10\}\) and \(\{3,\ldots,10\}\). Hence
\[
\Lambda_{10}=323.
\]
Equality in the seven-label lemma is also classified structurally. The tail
score can only be 322 or 323. In the first branch the unique low cyclic
signature permits only the insertion edge \(\{7,9\}\); in the second branch,
the four possible nonpositive corrections lead to fixed-edge pairing floors
that eliminate \(\{8,10\}\) and \(\{9,10\}\), while the unique residual
equality signature eliminates \(\{8,9\}\), leaving only \(\{7,10\}\). Thus
the equality classes are exactly those
represented by `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`. Independent
test-only arithmetic confirms this list over all 360 lemma classes and checks
all 511 nonempty witness subsets without calling the public enumerator or
production scorer.

Labels `3` and `2` are now classified exactly over those two equality
cycles. For the partial induced-subset maximum \(K_{\ge3}\), the label-three
insertion formula and complete shortcut-gain certificates leave exactly
eleven of the fourteen partial cycles at score 323. Inserting label \(2\)
in their 88 labelled gaps, the exact variation
\(2(a+b)-ab=4-(a-2)(b-2)\), the recorded argmaxes, and the same pruning
certificates prove that exactly 87 have \(K=323\). The sole exception is
`(10,3,2,4,7,8,6,9,5)`, obtained by splitting \(\{3,4\}\) in
`(10,3,4,7,8,6,9,5)`; it has score 325. The 88 candidates are distinct
dihedral core classes, so there are exactly 87 core minimizer classes.
Only after this classification, exact label-one insertion gives
\(87\cdot9=783\) complete dihedral minimizer classes. Independent test-only
arithmetic checks all 88 core orders and all 511 nonempty subsets of each,
including every argmax and the dihedral counts, without using production
enumerators, scorers, or canonicalizers. The public complete-order domain
remains `n<=8`.

A strengthened all-`n` mathematical lower bound has been proved from induced
subsets of cyclic gaps. For every `n>=4` and `1<=m<=n-2`,

\[
R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
\qquad
P_{m,n}
=
\sum_{k=m}^n k(m+n-k)
=
\frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
\]

Choosing \(m=\lceil(\sqrt2-1)n\rceil\) gives

\[
R_2^*(n)
\ge
\frac{2(\sqrt2-1)}{3\pi}n^3-O(n^2),
\]

and therefore

\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
\ge
4(\sqrt2-1)>1.
\]

The method has now been characterized exactly: for a fixed subset cardinality,
the duplicated-multiset pairing bound is uniquely maximized by the largest
indices \(\{n-q+1,\dots,n\}\), and the remaining discrete maximum over tails is
governed by
\[
\rho_n=\frac{\sqrt{8n^2+8n+1}-(2n+1)}2.
\]
Thus \(2(\sqrt2-1)/(3\pi)\) is optimal only within this specific lower-bound
relaxation, not necessarily for Power-Ringmin itself.

The first relational refinement between consecutive tails has also been
settled exactly. For \(S_m=\{m,\ldots,n\}\), deleting \(m\) leaves a simple
cycle \(C\) on \(S_{m+1}\) and a distinguished edge \(\{a,b\}\), with
\[
P_\sigma(S_m)-P_\sigma(S_{m+1})
=m(a+b)-ab
=m^2-(a-m)(b-m).
\]
Let \(\beta_{m,n}\) minimize
\(P(C)+[m(a+b)-ab]_+\) over all such cycle/edge pairs, and put
\(\beta_n^{(2)}=\max_{1\le m\le n-3}\beta_{m,n}\). This is the strongest
universal lower obstruction using only one pair \(S_m,S_{m+1}\). Pairing
signatures must form one connected loopless degree-two spanning graph; degree
conditions alone do not exclude disjoint subcycles. An explicit alternating
simple cycle proves
\[
P_{m+1,n}\le\beta_{m,n}\le P_{m+1,n}+n^2,
\]
and hence
\[
\beta_n^{(2)}
={2(\sqrt2-1)\over3}n^3+O(n^2).
\]
Thus the two-tail scheme can strengthen finite terms, but cannot improve the
leading coefficient. This limitation is specific to one optimized pair of
consecutive tails and is not an asymptotic evaluation of \(\Lambda_n\).
The strict cyclic-ratio sandwich also gives the geometric finite bound
\(R_2^*(n)>\beta_n^{(2)}/\pi-n^2\).

The exact obstruction from three consecutive tails is now reduced as well.
For \(n\ge5\), \(1\le m\le n-4\), deleting \(m\) and then \(m+1\) leaves a
simple base cycle \(C\) on \(S_{m+2}\) and two compatible edge splits. If
their corrections are \(A\) and \(B\), then
\[
\gamma^*_{m,n}
=
\min_{C,e,f}
\left[P(C)+\max\{0,A,A+B\}\right].
\]
The second split is exhaustively nested in the first edge, on a surviving
incident base edge, or on a disjoint base edge. Base, intermediate, and final
pairing signatures must be linked by the literal splits and must each form
one connected simple spanning cycle. Writing \(P^*_{m+2,n}\) for the exact
minimum base-cycle score, one has uniformly
\[
0\le\gamma^*_{m,n}-P^*_{m+2,n}<2n^2.
\]
The analogous squeeze against the duplicated-pairing floor \(P_{m+2,n}\)
shows that optimizing this three-tail obstruction still gives
\[
\max_m\gamma^*_{m,n}
={2(\sqrt2-1)\over3}n^3+O(n^2).
\]
This is a method-specific limitation, not an asymptotic evaluation of
\(\Lambda_n\) or \(R_2^*(n)\).

The entire consecutive-tail hierarchy is now parametrized on the ordinary
simple-cycle domain. For
\(2\le r\le n-2\), \(1\le m\le n-r-1\), put
\(\ell=m+r-1\). A cycle on \(S_m\) is uniquely a simple base cycle on
\(S_\ell\) followed by insertion of
\(\ell-1,\ell-2,\ldots,m\) through compatible edge splits. If the
successive corrections are \(A_1,\ldots,A_{r-1}\), the exact block score is
\[
P(C)+\max_{0\le j\le r-1}\sum_{i=1}^j A_i.
\]
Every intermediate cycle and literal split linkage is required. In
particular, recursively nested child-edge dominoes are admissible and cannot
in general be replaced by distinct base edges. Writing \(P^*_{\ell,n}\) for
the exact inner simple-cycle minimum, the resulting exact obstruction obeys
\[
0\le\gamma^{(r)}_{m,n}-P^*_{\ell,n}
\le\sum_{t=m}^{\ell-1}[t^2-2]_+
<(r-1)n^2,
\]
and the duplicated-pairing comparison is
\[
P_{\ell,n}\le\gamma^{(r)}_{m,n}<P_{\ell,n}+rn^2.
\]
Thus every fixed block, and more generally every \(r=r(n)=o(n)\), preserves
the coefficient \(2(\sqrt2-1)/3\) for this separately optimized one-block
method. Linear \(r=\Theta(n)\) is the first scale not excluded by the error
bound alone. A bounded exact test-local oracle for
\((m,n,r)=(2,7,4)\) matches all 60 compatible triple-split histories with all
60 outer dihedral cycles and obtains \((106,107,118)\) for the pairing floor,
inner cycle minimum, and four-tail obstruction. Production code and limits
remain unchanged.

For the generalized linear block, put \(m=1\),
\(r_n=\lfloor\alpha n\rfloor\),
\(s_n=\lceil\beta n\rceil\), and use prefix weight \(\lambda\). Charging
each intact base split against the exact quadratic edge slack
\[
P(C)-P_{r_n,n}
=
{1\over2}\sum_{\{u,v\}\in E(C)}
(u+v-n-r_n)^2,
\]
and treating every recursive split separately gives the total cubic lower
coefficient
\[
\mathcal C(\alpha,\beta,\lambda)
={(1-\alpha)(\alpha^2+4\alpha+1)\over6}
+(\alpha-\beta)
{\lambda\left(4(1+\alpha)\beta-(1+\alpha)^2
-2\lambda\beta^2\right)\over2(2-\lambda)}.
\]
Complete exact boundary analysis gives the unique global optimizer
\[
\alpha_*=1-{\sqrt3\over3},
\qquad
\beta_*={5\over6}-{\sqrt3\over4},
\qquad
\lambda_*={88-32\sqrt3\over73}.
\]
With \(r_n^*=\lfloor\alpha_*n\rfloor\), the exact floor/ceiling domain is
uniform for \(n\ge86\), and for \(n\ge90\) the finite residual bound is
\[
\gamma^{(r_n^*)}_{1,n}-P^*_{r_n^*,n}
\ge
{26-15\sqrt3\over54}n^3
-{233-128\sqrt3\over72}n^2.
\]
The cubic coefficient here is a certified residual lower coefficient, not the
exact block residual. More importantly, the earlier pointwise block comparison
and CR28bg give, explicitly and without exchanging a maximum and a minimum,
\[
\Lambda_n
\ge\Gamma_n^{(r_n^*)}
\ge\gamma^{(r_n^*)}_{1,n}
\ge P_{r_n^*,n}+(r_n^*-s_n^*)F_n^*
\qquad(n\ge86).
\]
Here \(P_{r_n^*,n}\) is the nonstarred duplicated-pairing floor. Exact rounding
then gives the finite consequences
\[
\Lambda_n
\ge {4+2\sqrt3\over27}n^3
\qquad(n\ge90),
\]
\[
R_2^*(n)
>{4+2\sqrt3\over27\pi}n^3-n^2
\qquad(n\ge90).
\]
Thus \((4+2\sqrt3)/27\), and that value divided by \(\pi\), are the unique
one-prefix-template-optimal total lower coefficients. Neither is asserted to
be an exact leading coefficient, and no limit or production-computation
result follows.

Selecting two prefixes gives a strict further improvement without duplicating
the base slack. For
\[
H_1=\sum_{t=s_1}^{r-1}A_t,
\qquad
H_2=\sum_{t=s_2}^{r-1}A_t,
\]
use exactly
\[
\max(0,H_1,H_2)\ge
(\lambda_{\rm hi}-\lambda_{\rm lo})H_1+\lambda_{\rm lo}H_2.
\]
After this combination, every original base edge is charged only at its
unique split, and every recursive child edge remains covered by its local
floor. The resulting coefficient is
\[
C_2=p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_{\rm hi})
+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_{\rm lo}).
\]
Exact reduction of the ordered weights leaves six branches and no pooled
interior KKT branch. Complete density, transition, face, and collision
analysis gives the unique global maximizer
\[
\left(
{629-23\sqrt{143}\over829},
{2286-77\sqrt{143}\over3316},
{2010-59\sqrt{143}\over3316},
{6264-288\sqrt{143}\over5281},
{3888-192\sqrt{143}\over4273}
\right),
\]
in the order
\((\alpha,\beta_1,\beta_2,\lambda_{\rm hi},\lambda_{\rm lo})\). Its exact
coefficient is
\[
C_{2,*}
={491596+6578\sqrt{143}\over2061723}
=0.276592655350947\ldots .
\]
Consequently
\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{2,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{2,*}\over\pi}.
\]
The earlier exact rational witness
\[
(\alpha,\beta_1,\beta_2,\lambda_{\rm hi},\lambda_{\rm lo})
=\left({3\over7},{2\over5},{3\over8},{1\over2},{1\over4}\right)
\]
gives
\[
C_2={72825421\over263424000}>{4+2\sqrt3\over27}.
\]
Its minimal uniform two-prefix threshold is \(n=59\), and exact rounding
proves
\[
\Lambda_n\ge {72825421\over263424000}n^3,
\qquad
R_2^*(n)>{72825421\over263424000\pi}n^3-n^2
\quad(n\ge59).
\]
This rational specialization remains the earlier explicit finite two-prefix
theorem. Finite rounding of the irrational two-prefix optimizer has not been
performed. Neither coefficient is an exact residual, limit, or geometric
leading coefficient.

Selecting three prefixes improves the asymptotic template again while using
the base-slack pool only once. For ordered weights
\(0\le\lambda_3\le\lambda_2\le\lambda_1\le1\),
\[
\max(0,H_1,H_2,H_3)
\ge(\lambda_1-\lambda_2)H_1
+(\lambda_2-\lambda_3)H_2+\lambda_3H_3.
\]
After expanding this combination, each split lies in exactly one weighted
segment; all recursive and fully nested child edges retain their local floor.
The three individual clipped weight optima are automatically ordered. With
\[
A=3\alpha-1,
\qquad
X_i=4\beta_i-(1+\alpha),
\]
the exact compact-simplex maximum is uniquely
\[
\left({X_1\over A},{X_2\over A},{X_3\over A}\right)
=
\left({1058\over1263},{276\over421},{184\over421}\right).
\]
The remaining one-variable compact optimization gives
\[
\alpha_*={685623-421\sqrt{377823}\over993423}
\]
and the exact coefficient
\[
C_{3,*}
={753972193324+106042322\sqrt{377823}\over2960667770787}
=0.276678647461945\ldots>C_{2,*}.
\]
Consequently
\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{3,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{3,*}\over\pi}.
\]
This irrational optimizer also has an exact finite specialization. With
\[
b_i={1+\alpha_*+x_i(3\alpha_*-1)\over4},
\quad
(x_1,x_2,x_3)
=\left({1058\over1263},{276\over421},{184\over421}\right),
\]
put \(r_n=\lfloor\alpha_*n\rfloor\),
\(s_{i,n}=\lceil b_i n\rceil\), and \(S_n=n+r_n\). The exact finite
middle-clipped weights give
\[
\widehat F_{i,n}={(4s_{i,n}-S_n)^2\over2}
\]
and the literal charging expression
\[
\begin{aligned}
\mathcal B_{3,n}={}&P_{r_n,n}
 +(r_n-s_{1,n})\widehat F_{1,n}\\
&+(s_{1,n}-s_{2,n})\widehat F_{2,n}
 +(s_{2,n}-s_{3,n})\widehat F_{3,n}.
\end{aligned}
\]
Let \(\mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil\). Because
\(\Lambda_n\) is integral, this is the stronger finite lower expression.
The minimal uniform threshold is \(n=159\): the first segment is empty at
\(n=158\), exact arithmetic covers \(159\le n\le170\), and the symbolic
tail starts at \(171\). For every \(n\ge159\),
\[
\Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
\qquad
R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2.
\]
The controlled remainder is
\[
\mathcal B_{3,n}
>C_{3,*}n^3+\kappa_*n^2-{\alpha_*+5\over3}n-{1\over15},
\quad
\kappa_*
={-535396585939+1466777893\sqrt{377823}\over986889256929}>{1\over3}.
\]
This is a finite three-prefix template theorem, not an exact residual, limit,
or geometric leading coefficient, and it does not extend charging to four
prefixes.

The separate direct charging argument does extend exactly to four selected
prefixes. For
\[
0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1,
\]
the five coefficients
\[
1-\lambda_1,\quad
\lambda_1-\lambda_2,\quad
\lambda_2-\lambda_3,\quad
\lambda_3-\lambda_4,\quad
\lambda_4
\]
combine \(0,H_1,H_2,H_3,H_4\) before any slack assignment and telescope to
four disjoint weighted segments. One canonical edge-indexed partition then
uses every original base slack exactly once or leaves it unused. The
boundary-independent recursive invariant covers every nested child edge,
including edges whose two endpoints were inserted earlier. With
\(r=\lfloor\alpha n\rfloor\), \(s_i=\lceil\beta_i n\rceil\), and
\(F_{i,n}=G_{n,\lambda_i}(s_i)\), every finite admissible cutoff tuple obeys
\[
\begin{aligned}
\gamma^{(r)}_{1,n}\ge{}& P_{r,n}
+(r-s_1)F_{1,n}
+(s_1-s_2)F_{2,n}\\
&+(s_2-s_3)F_{3,n}
+(s_3-s_4)F_{4,n}.
\end{aligned}
\]
The corresponding fixed-parameter coefficient is
\[
\begin{aligned}
C_4={}&p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)\\
&+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)
+(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3)\\
&+(\beta_3-\beta_4)g(\alpha,\beta_4,\lambda_4).
\end{aligned}
\]
The resulting continuous parameter problem has now been optimized globally.
On the compact ordered density/weight closure, the four weights reduce to
their individual clipped optima. There are exactly fifteen regimes
\(H^hM^m0^{4-h-m}\); the fixed-\(\alpha\) winner moves through
\(0000,MMMM,HMMM,HHMM,HHHM\), while `HHHH` would begin only beyond
\(\alpha=1\). Every transition, density collision, and compact facet is
classified. The unique global point lies strictly in `MMMM`. With

\[
\alpha_*={18170840871749-3666143\sqrt{2903456040383}
 \over27631313622349},
\qquad A_*=3\alpha_*-1,
\]

\[
(x_1,x_2,x_3,x_4)
={1\over3666143}(3190338,2672508,2091528,1394352),
\]

its remaining coordinates are

\[
\beta_{i,*}={1+\alpha_*+x_iA_*\over4},
\qquad
\lambda_{i,*}={x_iA_*\over\beta_{i,*}},
\]

and the exact optimum is

\[
\boxed{
C_{4,*}
={597580022071777213687318156
 +21288970076515705538\sqrt{2903456040383}
 \over2290468477489828247376833403}
=0.276736149860989\ldots>C_{3,*}.
}
\]

Therefore

\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{4,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{4,*}\over\pi}.
\]

No finite rounding or five-prefix conclusion is part of that optimization.
The historical standalone oracle checks all 840 literal four-split histories
of one bounded base. A separate standard-library exact diagnostic checks
clipping-gap factorizations, joins, branch transitions, collision reductions,
the simplex certificate, end-to-end surd maximum, and strict comparison with
\(C_{3,*}\).

The separate direct one-use theorem now holds for every arbitrary finite
number \(k\ge1\) of selected prefixes. With \(\lambda_{k+1}=0\), the
\(k+1\) convex coefficients combine \(0,H_1,\ldots,H_k\) before any slack is
assigned and telescope to \(k\) disjoint weighted segments. Each literal
history gives one canonical original-edge charged/unused partition. A
descending induction on inserted labels contains no frontier count, so the
recursive endpoint invariant survives every finite number of boundaries and
every nested history. The exact result is
\[
\gamma^{(r)}_{1,n}\ge
P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i),
\qquad s_0=r.
\]
By itself it gives no rounding or uniform growing-\(k\) control. Its separate
fixed-\(k\) instances are combined below with the normalized optimizer. The
sole dossier-local oracle is limited to \(k=6\) and checks all 332,640
histories of one six-edge base without changing production enumeration.

Independently of that charging theorem, the normalized prefix simplex is
solved exactly in every fixed dimension. For \(k\ge1\), let

\[
F_k(x_1,\ldots,x_k)
=\sum_{i=1}^k(x_{i-1}-x_i)x_i^2,
\qquad x_0=1,
\]

and

\[
M_k=\max_{1\ge x_1\ge\cdots\ge x_k\ge0}F_k(x_1,\ldots,x_k),
\qquad M_0=0.
\]

The maximum exists and has a unique strictly interior maximizer
\(1>x_1>\cdots>x_k>0\). If \(q_1=2/3\) and

\[
q_{m+1}={2\over3-q_m^2},
\]

then its ratios satisfy

\[
r_i={x_i\over x_{i-1}}=q_{k-i+1},
\qquad
r_k={2\over3},
\qquad
r_i={2\over3-r_{i+1}^2}.
\]

The exact value recurrence is

\[
M_k={q_k^2\over3}
={4\over27(1-M_{k-1})^2},
\qquad
M_k\nearrow{1\over3}.
\]

The first five rows agree exactly with the optimized prefix-simplex cases;
the fifth also supplies the rational witness used below:

| \(k\) | unique maximizer | \(M_k\) | \(M_k/8\) |
|---:|---|---:|---:|
| 1 | \((2/3)\) | \(4/27\) | \(1/54\) |
| 2 | \((18/23,12/23)\) | \(108/529\) | \(27/1058\) |
| 3 | \((1058/1263,276/421,184/421)\) | \(1119364/4785507\) | \(279841/9571014\) |
| 4 | \((3190338,2672508,2091528,1394352)/3666143\) | \(3392752184748/13440604496449\) | \(848188046187/26881208992898\) |
| 5 | \((26881208992898,23392470652668,19595592993288,15335681473008,10223787648672)/30143556935103\) | \(722599396919860307414438404/2725902074099388500860861827\) | \(180649849229965076853609601/5451804148198777001721723654\) |

Writing

\[
p(\alpha)={(1-\alpha)(\alpha^2+4\alpha+1)\over6},
\qquad
E_k(\alpha)=p(\alpha)+{M_k\over8}(3\alpha-1)^3,
\]

the envelopes converge uniformly and monotonically on \([1/3,1]\) to

\[
E_\infty(\alpha)
=p(\alpha)+{(3\alpha-1)^3\over24}.
\]

The formal normalized-polynomial envelope has its unique maximum on the full
compact interval at the degenerate endpoint \(E_\infty(1)=1/3\); on
\([1/3,1)\) this is only a nonattained supremum. On the limiting all-middle
closure \([1/3,1/2]\), the unique maximum is

\[
\alpha={13-2\sqrt2\over23},
\qquad
E_\infty(\alpha)={434+4\sqrt2\over1587}.
\]

The complete clipped family, rather than only this all-middle restriction, is
also solved for arbitrary finite \(k\). If \(\Phi_{1+\alpha}\) is the exact
coordinatewise clipped floor and \(\phi\) its normalized form from
(CR28dw15), then

\[
\mathscr H_k(\alpha)
=p(\alpha)+(1+\alpha)^3V_k\!\left({\alpha\over1+\alpha}\right),
\qquad
V_m(t)=\max_{0\le x\le t}
\bigl((t-x)\phi(x)+V_{m-1}(x)\bigr),
\quad V_0=0.
\]

There are exactly \((k+1)(k+2)/2\) ordered regimes \(H^hM^m0^z\).
The Bellman values are finite lower Darboux sums for the increasing clipped
floor, and their pointwise supremum is

\[
\mathscr H_{\rm fin}(\alpha)=
\begin{cases}
p(\alpha),&0\le\alpha\le1/3,\\
(23\alpha^3-39\alpha^2+21\alpha+3)/24,
 &1/3\le\alpha\le1/2,\\
(5\alpha^3-21\alpha^2+15\alpha+17)/72,
 &1/2\le\alpha\le1.
\end{cases}
\]

The outer pieces are exactly dominated by a feasible one-prefix all-middle
value. Therefore every finite \(k\) has one strict all-middle global
maximizer, with value \(C_{k,*}\), and

\[
C_{k,*}\nearrow C_{\mathrm{AF}}
={434+4\sqrt2\over1587}.
\]

Thus the formal endpoint \(E_\infty(1)=1/3\) is not a clipped-family value:
\(C_{\mathrm{AF}}\) is the exact, unattained supremum of the complete
continuous finite-prefix template family.

The statements about \(M_k\) and \(E_k\) are exact normalized-polynomial
theorems, while the \(\mathscr H_k\) result is the separate full clipped
continuous optimization. Neither supplies charging; the direct finite-\(k\)
theorem above is a third independent input. Together they nevertheless have
the following exact all-fixed-\(k\) consequence. Fix

\[
\alpha_\infty={13-2\sqrt2\over23},
\qquad
A_\infty=3\alpha_\infty-1,
\qquad
S_\infty=1+\alpha_\infty.
\]

For each finite \(k\), use its unique normalized optimizer \(x^{(k)}\) and
define

\[
\beta_i={S_\infty+A_\infty x_i^{(k)}\over4},
\qquad
\lambda_i={A_\infty x_i^{(k)}\over\beta_i}.
\]

Because \(1/3<\alpha_\infty<1/2\) and
\(1>x_1^{(k)}>\cdots>x_k^{(k)}>0\),

\[
\beta_i-{S_\infty\over4}={A_\infty x_i^{(k)}\over4}>0,
\quad
\alpha_\infty-\beta_i
={A_\infty(1-x_i^{(k)})\over4}>0,
\]

\[
{S_\infty\over3}-\beta_i
>{1-2\alpha_\infty\over3}>0.
\]

Thus the cutoffs and weights are strictly ordered and strictly all-middle:

\[
0<\beta_k<\cdots<\beta_1<\alpha_\infty<1,
\qquad
0<\lambda_k<\cdots<\lambda_1<1.
\]

For each fixed \(k\), some tuple-dependent threshold \(N_k\) makes the
integer cutoffs admissible. The charging theorem and fixed-parameter liminf
then give

\[
L_\Lambda:=\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge p(\alpha_\infty)+{A_\infty^3M_k\over8}.
\]

This scalar inequality holds for every fixed finite \(k\). Taking its
supremum and using \(M_k\nearrow1/3\) proves

\[
\boxed{
L_\Lambda\ge{434+4\sqrt2\over1587},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{434+4\sqrt2\over1587\pi}.
}
\]

No \(k=k(n)\) is used, no threshold uniform in \(k\) is needed, and no
limits are interchanged. The operation is only the supremum of scalar
inequalities already proved one fixed \(k\) at a time. The formal endpoint
value \(1/3\) at \(\alpha=1\) is not promoted, and the supremum above gives
no new uniformly rounded finite-\(n\) theorem.

At fixed \(k=5\), the full continuous coefficient can nevertheless be
optimized without a growing-\(k\) interchange. Coordinatewise weight clipping
reduces the complete eleven-parameter compact closure to 21 ordered regimes.
Every clipping transition, density/weight collision, and compact face is
audited. The unique global point is strictly all-middle, with

\[
\alpha_{5,*}
={422413777961580309772684503
 -10047852311701\sqrt{183342238504950468196395903}
 \over661485317418210151348973103}.
\]

For the fifth simplex coordinates \(x_i=N_i/D\) displayed below and
\(A_*=3\alpha_{5,*}-1\), its five exact pairs are

\[
\beta_{i,*}={1+\alpha_{5,*}+x_iA_*\over4},
\qquad
\lambda_{i,*}={x_iA_*\over\beta_{i,*}}
\quad(1\le i\le5).
\]

The exact optimum is

\[
\boxed{
C_{5,*}
={346693217780244687187063490332457027500975566238012204
 +1228130489996268437333105902690103574002
  \sqrt{183342238504950468196395903}
 \over1312688475479610714750859896048564873968757997852345827}
>C_{5,\mathrm{rat}}>C_{4,*}.
}
\]

Thus

\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{5,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{5,*}\over\pi}.
\]

One standalone exact diagnostic checks the 21 regimes, five transition rows,
optimizer and coefficient polynomials and isolating intervals, strict branch
inequalities, coefficient identity, and comparison margins. No finite
rounding at this irrational optimizer is asserted. The number \(C_{5,*}\)
remains the exact optimum of the fixed \(k=5\) template, but
\[
C_{5,*}<{277\over1000}<{434+4\sqrt2\over1587},
\]
so it is not the current all-fixed-\(k\) lower coefficient.

At the single fixed value \(k=5\), however, the two separate exact theorems
may be combined without any limiting interchange. Put

\[
D=30143556935103,
\]

\[
(N_1,\ldots,N_5)
=(26881208992898,23392470652668,19595592993288,
15335681473008,10223787648672).
\]

For \(\alpha=13/30\), \(s=43/30\), \(A=3/10\), and \(x_i=N_i/D\), choose

\[
\beta_i={s+Ax_i\over4},
\qquad
\lambda_i={Ax_i\over\beta_i}.
\]

The fifth simplex row proves that these rational parameters satisfy

\[
0<\beta_5<\cdots<\beta_1<\alpha<1,
\qquad
{s\over4}<\beta_i<{s\over3},
\qquad
0<\lambda_5<\cdots<\lambda_1<1.
\]

Thus the point is strictly all-middle and eventually satisfies every integer
cutoff condition. Its exact coefficient is

\[
\boxed{
C_{5,\mathrm{rat}}
={2263404122555368590593580404287
 \over8177706222298165502582585481000}
>{75\over271}>C_{4,*}.
}
\]

The fixed-parameter charging limit and the existing additive cyclic-ratio relation
therefore give

\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{5,\mathrm{rat}},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{C_{5,\mathrm{rat}}\over\pi}.
\]

This is one explicit rational five-prefix witness, now proved strictly below
the global value. Its derivation itself is not a global optimization, and it
remains the tuple with the finite theorem below.

The same fixed tuple also has an exact finite floor/ceiling theorem. Put

\[
r_n=\left\lfloor{13n\over30}\right\rfloor,
\qquad
s_{i,n}=\lceil\beta_i n\rceil,
\qquad
s_{0,n}=r_n,
\qquad
S_n=n+r_n,
\]

and retain the original rational weights in

\[
F_{i,n}
=G_{n,\lambda_i}(s_{i,n})
={\lambda_i(4S_ns_{i,n}-S_n^2-2\lambda_i s_{i,n}^2)
 \over2(2-\lambda_i)}.
\]

The minimal uniform threshold for complete admissibility, strict cutoff
order, five nonempty segments, and all five finite middle branches is
\(n=234\); at \(n=233\), \(r_n=s_{1,n}=100\). With

\[
\mathcal B_{5,n}
=P_{r_n,n}+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})F_{i,n},
\qquad
\mathcal I_{5,n}=\left\lceil\mathcal B_{5,n}\right\rceil,
\]

exact floor/ceiling algebra proves

\[
\boxed{
\Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
>C_{5,\mathrm{rat}}n^3
\qquad(n\ge234),
}
\]

\[
\boxed{
R_2^*(n)>{\mathcal I_{5,n}\over\pi}-n^2
>{C_{5,\mathrm{rat}}\over\pi}n^3-n^2
\qquad(n\ge234).
}
\]

The five middle inequalities classify the rounded cutoffs; the fixed
\(\lambda_i\) are not replaced by finite reoptimized clipped weights. The
exact remainder is a statement about \(\mathcal B_{5,n}\), not the unknown
true residual of the block or of \(\Lambda_n\).

There is also an exact eventual radius-one insertion theorem. Let
\(R^*_{2:n}\) be the infimum feasible central radius for only the core radii
\(2^2,\dots,n^2\). A core configuration at radius \(R\) admits insertion of
the radius-\(1\) circle whenever
\[
\sum_{j=2}^n\theta_R(1,j^2)<\pi.
\]
Rigorous angular majorants combined with the configuration-level
induced-subset lower bound prove
\[
R_2^*(n)=R^*_{2:n}\qquad(n\ge12).
\]
In fact, the full and core feasible-radius sets coincide in that range. The
threshold \(12\) is sufficient and is not claimed minimal; the proof is
independent of the checked cases \(n=5,6\).

For every \(n\ge12\), assigning the core centers to the equally spaced polar
directions of a regular \((n-1)\)-gon gives the order-independent all-pairs
feasible baseline
\[
U_n
=
\sqrt{
n^2(n-1)^2\csc^2\!\left(\frac{\pi}{n-1}\right)
+\frac{(2n-1)^2}{4}}
-\frac{n^2+(n-1)^2}{2}.
\]
The zigzag assignment \((n,2,n-1,3,\dots)\) sharpens this baseline. Defining
\[
M_n=n\left(\left\lfloor\frac n2\right\rfloor+1\right),
\qquad
V_n=\frac{(n-1)M_n}{\pi},
\]
an exact product-distance lemma proves that every core pair is feasible at
\(V_n\). The insertion theorem therefore gives
\[
R_2^*(n)\le V_n\qquad(n\ge12),
\]
and \(V_n/n^3\to1/(2\pi)\). Combined with the induced-subset lower bound,
this settles the order of growth:
\[
R_2^*(n)=\Theta(n^3).
\]
The proof, including the general angular majorant, zigzag closing arc, every
non-adjacent constraint, and the earlier baseline, is recorded in
`research/ALL_N_LOWER_BOUND.md`.

The regular-direction construction now has an exact combinatorial surrogate.
For a cyclic core order \(\sigma\), let \(d_\sigma(i,j)\) be smaller circular
positional distance and define
\[
W(\sigma)=\max_{2\le i<j\le n}{ij\over d_\sigma(i,j)},
\qquad W_n=\min_\sigma W(\sigma).
\]
The core is strictly all-pairs feasible at \((n-1)W(\sigma)/\pi\), and the
accepted insertion theorem transfers this radius to the full problem for
\(n\ge12\). For every \(2\le m\le n-2\), oriented positional gaps on the
induced tail prove the exact obstruction
\[
W(\sigma)\ge {P_{m,n}\over n-1}.
\]
The adjacent relaxation
\[
A_n=\min_\sigma\max_k\sigma_k\sigma_{k+1}
\]
is now characterized exactly:
\[
A_3=6,
\qquad
A_n=
\left(\left\lfloor{n\over2}\right\rfloor+1\right)
\left(\left\lceil{n\over2}\right\rceil+2\right)
\quad(n\ge4).
\]
A rigorous high/low internal-edge count proves the lower bound, and
`patterns.interleave` realizes it for every \(n\). Moreover,
\[
\lim_{n\to\infty}{A_n\over n^2}={1\over4}
<
{2(\sqrt2-1)\over3}
=
\lim_{n\to\infty}{L_n\over n^2}.
\]
The explicit tail \(m=\lceil2n/5\rceil\) proves \(L_n>A_n\) for every
\(n\ge33\); exact rational evaluation gives \(L_n\le A_n\) through \(n=32\).
The equality cases are now characterized exactly. For even \(n=2t\), the
only high-high edge is \(\{t+1,t+2\}\); for odd \(n=2t+1\), the only
high-high edges form the forced segment \(t+2,t+1,t+3\). There are no
low-low edges, and removing the forced edge or segment leaves an alternating
path whose gaps are labelled by the low vertices.

Writing \(B_n=W_n^{(\le2)}\), a terminal-high incidence theorem, plus a
separate exact degree argument for `n=12`, proves
\[
B_n=A_n\quad(3\le n\le8),
\qquad
B_n>A_n\quad(n\ge9).
\]
Thus \(W_n>A_n\) for every \(n\ge9\), with no cyclic-order enumeration beyond
the existing `n=3..11` regression.
An independent quantitative obstruction now uses two exact product tails.
For a threshold \(T\), let \(a_T,b_T\) be the least integers at least two
with \(a_T(a_T+1)>T\) and \(b_T(b_T+1)>2T\), and put
\(U_T=\{a_T,\dots,n\}\), \(V_T=\{b_T,\dots,n\}\), with sizes \(u,v\)
after intersection with the core. The induced cyclic gaps between labels in
\(U_T\) cost at least two positions. The compatible graph \(xy\le2T\) on
\(U_T\) is a split threshold graph with nested prefix neighborhoods, and its
exact minimum number of incompatible cyclic adjacencies is
\[
\eta_n(T)=\max(0,2v-u+\delta_n(T)),
\]
where
\[
\delta_n(T)
=
\mathbf1_{\{a_T<b_T\le n-1,\ 2T<b_T^2-1\}}
\]
is the strict skip-one correction. Inverting the exact requirement
\(n-1\ge2u+\eta_n(T)\) gives a finite half-integer obstruction
\(Q_n\le B_n\) and, for every \(n\ge9\),
\[
B_n\ge Q_n\ge
{36-16\sqrt2\over49}\left(n+{1\over2}\right)^2.
\]
Consequently
\[
\liminf_{n\to\infty}{B_n\over n^2}
\ge {36-16\sqrt2\over49}>{1\over4}.
\]
In fact,
\[
Q_n={36-16\sqrt2\over49}n^2+O(n),
\]
so the exact nested-neighborhood refinement can improve finite values but
does not improve this subproblem's asymptotic coefficient.
A stronger terminal-high incidence theorem applies at every exact threshold:
if an order has distance-two score at most \(T\), then
\[
2v\le
C_n(T)
=
\#\{\ell\in\{2,\dots,a_T-1\}:\ell b_T\le T\}.
\]
Keeping \(Q_n\) unchanged, combine this with
\(\Psi_n(T)=2u+\eta_n(T)\le n-1\) and let \(H_n\) be the least admissible
half-integer threshold. Then
\[
B_n\ge H_n\ge Q_n,
\qquad
H_n={8\over25}n^2+O(n),
\qquad
\liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}.
\]
The coefficient \(8/25\) is proved by matching all-\(n\) inequalities; it is
not inferred from finite data. A matching explicit construction now turns it
into the exact asymptotic coefficient of both \(B_n\) and \(W_n\). With
\[
d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T_n={d_n(d_n-1)\over2},
\]
there is an explicit cyclic core order \(\sigma_n\) for every \(n\ge9\)
such that \(W(\sigma_n)\le T_n\). The symbolic five-residue block family
covers every \(n\ge33\) and ten earlier values; fourteen displayed initial
witnesses cover the rest. Adjacent products, distances two and three,
closing arcs, and automatic distances at least four are proved separately in
`research/PRODUCT_DISTANCE_SURROGATE.md`. Therefore
\[
{B_n\over n^2}\longrightarrow{8\over25},
\qquad
{W_n\over n^2}\longrightarrow{8\over25}.
\]
For \(n\ge12\), the insertion theorem transfers the same construction and
gives
\[
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{8\over25\pi}.
\]
This remains the exact regular-direction product-distance coefficient. A
later shortcut-budget theorem evaluates the induced-subset objective on the
same canonical core order. On its symbolic domain the unique maximizer is
\[
U_n^*=
\begin{cases}
\{2v+1,\ldots,n\},&e=4,5,\\
\{2v+1,\ldots,n\}\setminus\{2v+2\},&e=6,7,8,
\end{cases}
\]
and each of the fourteen explicit initial orders has a unique maximizing
tail. The exact quasipolynomial gives
\[
K(\tau_n)={143\over500}n^3+O(n^2).
\]
Exact label-one elimination and the fixed-order angular sandwich therefore
sharpen the current global upper coefficients to
\[
\limsup_{n\to\infty}{\Lambda_n\over n^3}\le{143\over500},
\qquad
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{143\over500\pi}.
\]
These are upper coefficients, not exact asymptotic constants or convergence
theorems.
On the sharper exact-threshold residue-one order
\(\tau_n^{(1)}=\operatorname{residue\_one\_product\_distance\_order}(n)\),
write \(n=5k+1\), \(k\ge2\), and \(\varepsilon=k\bmod2\). Its unique
maximizing subset is
\[
\{2k+1,2k+2,\ldots,5k+1\},
\]
and the exact value is
\[
K(\tau_n^{(1)})
={857k^3+891k^2+214k
 +\varepsilon(27k^2-51k-18)\over24}
={857\over3000}n^3+O(n^2).
\]
This is strictly smaller than the canonical K825 value on every admissible
residue-one row, including the explicit rows \(k=2,3,4,5\) and the K825
boundary row \(k=6\); there is no crossover. Exact label-one elimination and
the fixed-order sandwich give
\[
\limsup_{k\to\infty}{\Lambda_{5k+1}\over(5k+1)^3}
\le{857\over3000},
\qquad
\limsup_{k\to\infty}{R_2^*(5k+1)\over(5k+1)^3}
\le{857\over3000\pi}.
\]
These are residue-one subsequential upper bounds. They do not improve the
all-residue limsup coefficient, identify a global minimizing order, compare
the exact angular thresholds of the two constructed orders, or identify an
exact quadratic geometric term.
On the exact-threshold residue-two order
\(\tau_n^{(2)}=\operatorname{residue\_two\_product\_distance\_order}(n)\),
write \(n=5k+2\), \(k\ge2\), with the same
\(\varepsilon=k\bmod2\). Its sole maximizing subset is
\[
\{2k+1,2k+2,\ldots,5k+2\},
\]
and
\[
K(\tau_n^{(2)})
={286k^3+459k^2+198k+16
 +\varepsilon(-10k^2+40k+27)\over8}
={143\over500}n^3+O(n^2).
\]
The exact shortcut-budget proof handles both parity branches and the
smallest rows \(k=2,3,4\), with no exceptional argmax or score correction.
This value is strictly smaller than K825 on every residue-two row, including
the five explicit rows and the K825 boundary \(k=7\); there is no crossover,
but
\[
K_{825}(n)-K(\tau_n^{(2)})={21\over100}n^2+O(n).
\]
Thus both families retain cubic coefficient \(143/500\). Label-one
elimination and the fixed-order sandwich give only the corresponding exact
fixed-order score, its width-\(n^2\) angular bounds, and the residue-two
subsequential upper bounds. Label-one elimination also shows that the same
tail is the unique complete-order \(\Lambda\)-maximizing subset after every
insertion. These facts do not order the exact angular thresholds, identify a
global minimizing order or active geometric subsystem, or improve the cubic
all-residue bound.
The same threshold now gives an exact residue-class classification of the
lower obstruction. For every \(n\ge9\), with \(d=d_n\),
\[
H_n=
\begin{cases}
d(d-1)/2,&n\equiv0,3,4\pmod5,\\
(d-1)^2/2,&n\equiv1\pmod5,\\
(d-1)(d-2)/2,&n\equiv2\pmod5,\ n\ge17,
\end{cases}
\]
and \(H_{12}=56\). Combining the uniform construction with separate
search-free orders in residues one and two proves
\[
B_n=W_n
=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
d_n(d_n-2)/2,&n\equiv2\pmod5
\end{cases}
\qquad(n\ge9).
\]
The residue-one branch begins at \(n=11\) and is realized by a separate
search-free cyclic order whose score is exactly \((d_n-1)^2/2\). Its proof
checks adjacency, distances two and three, closing arcs, and automatic
distances at least four separately. In residue two, put
\(J_n=d_n(d_n-2)/2\). A saturation argument proves
\[
B_{12}\ge60=J_{12},
\qquad
B_n\ge J_n
\quad(n\equiv2\pmod5,\ n\ge17).
\]
A parity-aware symbolic order \(\sigma_n^{(2)}\), valid for
\(n=5k+2\), \(k\ge2\), is a permutation and has
\(W(\sigma_n^{(2)})=J_n\). Its proof separately checks adjacency,
distances two and three, the closing cut, and every distance at least four
using \(4J_n-n(n-1)=7k^2+33k+14>0\). Hence the displayed lower bounds
match and give \(B_n=W_n=J_n\) at \(n=12\) and throughout the class from
\(n=17\). The \(n=7\) value remains supplied by the bounded exact table.
An exact, no-floating-point canonical enumeration bounded to `n=3..11` gives
\[
(W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50),
\]
with canonical minimizer counts \((1,1,1,2,2,4,12,72,24)\). The proof,
complete table, representatives, and finite/all-`n` classification are in
`research/PRODUCT_DISTANCE_SURROGATE.md`.
For the same bounded cases, the distance-one objectives are
\[
(6,12,15,20,24,30,35,42,48),
\]
and the distance-two objectives equal \(W_n\) in every row. This finite table
also gives
\[
(H_3,\dots,H_{11})=(6,12,15,20,21,30,36,45,50),
\qquad
\max(A_n,H_n)=B_n
\]
row by row. The last equality is a bounded exact comparison, not an all-\(n\)
formula. The table agrees with the theorem: the first non-adjacent gap is
\(A_9=35<36=W_9\), already accounted for by positional distance two. Exact
values of \(B_n\) and \(W_n\) are therefore known in every residue class for
\(n\ge9\). Combining that formula with the exact table for \(3\le n\le11\)
gives the global classification
\[
W_n^{(\le2)}=B_n=W_n\qquad(n\ge3).
\]
Thus distances at least three never change the optimum value. Let
\(\mathcal M_n\) and \(\mathcal M_n^{(\le2)}\) denote the full and
distance-two minimizer sets. Every omitted pair has score at most
\(n(n-1)/3\). Exact evaluation of the residue-class formula proves
\[
\mathcal M_n=\mathcal M_n^{(\le2)}
\qquad(3\le n\le92).
\]
At \(n=93\), moving label \(54\) in
\(\operatorname{eight\_twenty\_fifths\_order}(93)\) from the segment
\((92,4,54,3,93)\) to between the consecutive labels \(16,48\) gives
\[
W^{(\le2)}=2850=B_{93},
\qquad
W=2852
\]
because \((92,93)\) is then at distance three. Hence
\(\mathcal M_{93}\subsetneq\mathcal M_{93}^{(\le2)}\), so \(93\) is the
first minimizer-restriction index. This is an exact combinatorial result,
uses no canonical enumeration beyond \(n=11\), and makes no geometric claim.

One explicit perturbation of the matching upper construction is now
classified symbolically. For \(n=10m+3\), \(m\ge3\), write
\(d=8m+4\), \(T=d(d-1)/2\), and reverse only the two outer entries of one
triple path \(P_s\), \(0\le s\le m\). The full-distance score is exactly
\[
W(\tau_{m,s})=
\begin{cases}
(d^2-1)/2=T+(d-1)/2,&s=0,\\
T,&1\le s\le m.
\end{cases}
\]
Adjacency, distance two, distance three, distances at least four, and all
pairs crossing the displayed cut are proved separately. Thus every parameter
choice has coefficient \(8/25\): the family gives an exact obstruction, not
an improved upper coefficient. The subsequent regular-direction geometric
inequality is only an upper bound and does not obstruct non-regular geometry.

A second perturbation is now closed, after fixing its transformation before
direct scoring. On the same branch, leave the terminal/low scaffold and each
oriented middle path unchanged, but let terminal gap \(G_j\) receive
\(P_{j+1\bmod2m}\). This is a permutation of the core labels. Its exact
distance-class maxima are
\[
T,\qquad
{n(d-1)\over2},\qquad
{(5m+2)(9m+4)\over3},\qquad
{n(n-1)\over4}
\]
for distances \(1,2,3,\ge4\), respectively, with a unique maximizing pair
in every class. The full score is
\[
W(\widehat\sigma_m)
={n(d-1)\over2}
={(10m+3)(8m+3)\over2},
\]
uniquely saturated by \(\{n,d-1\}\) at distance two. The exact obstruction is
the closing-gap word \(n,2,d-1\), created when \(P_0\) wraps into
\(G_{2m-1}\). Thus \(W/n^2\to2/5>8/25\). This is one
family-specific surrogate obstruction; its regular-direction transfer is
only a weaker upper bound and yields no new geometric consequence.

The distinguished path now has an exact local placement classification under
arbitrary whole-path reassignments of the same scaffold. If gap \(G_j\)
contains the unchanged oriented path
\(P_0=(d-1,4m+2,d-2)\), its unique local maxima at distances one and two are
\[
M^{\rm loc}_1(j)=T,
\qquad
M^{\rm loc}_2(j)=T+{j(d-1)\over2}.
\]
Hence every reassignment with distance-two score at most \(T\) must fix
\(P_0\) in \(G_0\). All other gaps are locally excluded; \(G_0\) is only
locally non-excluded. This necessary lemma does not classify the remaining
path assignment or establish a nonidentity completion. The canonical identity
assignment is a separate previously proved witness.

The same calculation is now complete for every remaining path. For a triple
\(P_k=(d-1-2k,4m+2+k,d-2-2k)\), \(0\le k\le m\), the exact
distance-two maximum in \(G_j\) is
\[
{(d+j)(d-1-2k)\over2},
\]
and distance one is always safe. Hence the locally non-excluded gaps are
exactly \(G_0,\ldots,G_{\ell_k}\), where
\[
\ell_k=
\min\!\left\{2m-1,
\left\lfloor{2kd\over d-1-2k}\right\rfloor\right\}.
\]
Equivalently, \(G_j\) permits the triple indices
\[
k\ge
\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
\]
Every singleton \(P_k=(4m+2+k)\), \(m+1\le k\le2m-1\), is strictly
locally non-excluded in every gap. The cyclic closing word, both terminal
columns, the triple/singleton transition, and \(m=3\) are explicit in the
proof.

The matching support of this Ferrers relation is now exact as well. A local
edge belongs to at least one relation-compatible path-to-gap bijection exactly
when it is \((0,0)\) or its gap index is positive:
\[
\mathcal R_{\rm ext}
=\{(0,0)\}
\cup\{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
\]
The saturated suffix \(G_1,\ldots,G_{2m-1}\) gives the Hall obstruction for
every \((k,0)\), \(k>0\). Conversely, rotating one integer interval gives an
explicit compatible bijection through every positive-column local edge, with
separate formulas for \(j<k\), \(j=k\), and \(j>k\). The proof treats the
triple/singleton crossing, terminal singleton, closing column, and \(m=3\)
without enumerating path permutations.

The full-score question is now closed for every such bijection, not only for
the interval shifts. If \(\alpha\) is any path-to-gap bijection, the complete
six-form triple and four-form singleton classification proves the sharp bound
\[
W^{(=3)}(\sigma_\alpha)\le {n(5m+2)\over3}<T.
\]
Equality in this distance-three bound occurs exactly when \(P_m\) lies in
\(G_{2m-2}\) or \(G_{2m-1}\), and both placements have compatible PG46
witnesses. Every distance at least four is universally below \(T\), while the
internal adjacent pair of \(P_0\) equals \(T\). Therefore, for every
bijection,
\[
W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha),
\]
and relation-compatibility is equivalent to
\(W(\sigma_\alpha)=T=W_n\). Thus the Ferrers support above is exactly the
edge support of full-optimal scaffold bijections. This classifies all
compatible bijections by score without enumerating them and has no new
geometric consequence.

The remaining counting question is now closed as well. Put \(v=2m\),
\(d=8m+4\), and
\[
\kappa_j=
\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
\]
PG49 forces \(P_0\) into \(G_0\). On the residual Ferrers board, processing
the nested columns from \(G_{v-1}\) back to \(G_1\) leaves exactly
\(j+1-\kappa_j\) choices at column \(j\), independently of the previous
suffix choices. Hence the exact labelled count is
\[
\boxed{
\mathsf F_m^{\rm lab}
=\prod_{j=1}^{2m-1}(j+1-\kappa_j)
}
\qquad(m\ge3).
\]
Equivalently, with the retained triple cutoffs \(\ell_k\),
\[
\mathsf F_m^{\rm lab}
=(m-1)!\prod_{k=1}^{m}(\ell_k-k+1).
\]
The proof includes the forced zero column, first positive column, both
terminal thresholds, the triple/singleton transition, the terminal singleton,
inclusive cutoff equalities, and \(m=3\), where the count is \(36\). PG36
and PG62 identify these perfect matchings with exactly the relation-compatible,
equivalently full-optimal, scaffold bijections. The formula is a labelled
count of indexed gaps and oriented paths; no symmetry quotient is taken.
Distinct assignments nevertheless give distinct canonical dihedral core
orders in this fixed scaffold, so the same integer also counts the represented
dihedral classes by injectivity, not by division. One bounded standard-library
Ryser diagnostic checks \(m=3,\ldots,8\) without enumerating path
permutations or matchings. No geometric or alternative-scaffold consequence
is inferred.

The logarithm of this exact labelled count now has a direct all-\(m\)
asymptotic theorem. With
\[
C_{\rm F}=14\log2+6\log3-10\log5-2,
\]
one has, for every \(m\ge3\),
\[
1+\log{5\over6}-\log m
<\log\mathsf F_m^{\rm lab}-(2m\log m+C_{\rm F}m)
<{9\over4}+\log\bigl(2m(2m+1)\bigr),
\]
and therefore
\[
\log\mathsf F_m^{\rm lab}=2m\log m+C_{\rm F}m+O(\log m).
\]
The logarithmic remainder is now sharp:
\[
\boxed{
\log\mathsf F_m^{\rm lab}
=2m\log m+C_{\rm F}m+{3\over4}\log m+O(1).
}
\]
The exact factorial product contributes \(-\tfrac12\log m\), the smooth
perturbation converges to a constant, and the floor/ceiling rounding
contributes \(\tfrac54\log m+O(1)\). The rounding proof treats
\(j\le\sqrt m\), the intermediate phase-cycling range, the bulk, exact
cutoff hits, all five terminal residue classes, and both endpoints
separately. The signed literal ceiling/no-ceiling change is instead
\(-\tfrac34\log m+O(1)\). Two standalone formula diagnostics sum only the
explicit factors and audit the comparison components. This is a
labelled-count theorem; canonical injectivity remains a downstream
interpretation, and no geometric conclusion follows. Convergence of the
remaining bounded term is not claimed.

One of the two sharp PG46 witnesses is now evaluated exactly for the
induced-subset objective. For the shift that sends \(P_m\) to the closing gap
\(G_{2m-1}\), the corresponding core order has the unique maximizing subset
\[
S_m=\{4m+1,\ldots,10m+3\}
\]
and
\[
K={572m^3+631m^2+223m+22\over2}
\qquad(m\ge3).
\]
An exhaustive symbolic isolated-hole and compressed-shortcut audit proves
uniqueness, and an exact block sum gives the formula. On the same rows,
\[
K-K_{825}=m^2-6m-4,
\]
so the order improves K825 exactly at \(m=3,4,5,6\), is worse for every
\(m\ge7\), and has no integer tie. In terms of \(n\), both leading cubic
coefficients are \(143/500\), while this PG46 value is eventually larger by
\(n^2/100+O(n)\). This is a fixed-core-order theorem only; it proves no
geometric or global optimality statement.

The other sharp PG46 witness is now evaluated as well. Specializing PG46 so
that \(P_m\) occupies \(G_{2m-2}\) leaves \(P_{2m-1}\) in the closing gap.
The same tail \(S_m\) is the unique maximizing subset, but
\[
K={572m^3+631m^2+235m+22\over2}.
\]
The exact comparisons are
\[
K-K_{\rm closing}=6m,\qquad K-K_{825}=m^2-4,
\]
so this witness is strictly worse than both comparators for every \(m\ge3\).
The proof treats seven hole ranges, every compressed-shortcut length, the
altered cyclic three-edge path, and the minimum row. It retains cubic
coefficient \(143/500\) and proves no geometric or global optimality
statement.

A distinct explicit PG49 representative is now exact too. Put
\(q=\lfloor(4m+3)/5\rfloor\), send \(P_q\) to the closing gap, shift the
remaining triples by one, and place the singleton paths in decreasing order
as in (PG110). The map is a Ferrers-compatible bijection for every
\(m\ge3\), with exact equality in the cyclic closing column. Its unique
maximizing subset is
\[
B_m=\{4m+1,\ldots,10m+3\},
\]
and
\[
K={1714m^3+1863m^2+24mq+617m+12q^2+48q+66\over6}.
\]
The five \(m\bmod5\) branches have coefficient \(857/3000\) in \(n\), and
the value is strictly below K825 and both PG46 orders for every \(m\ge3\).
The proof audits every deletion gain and compressed shortcut, including both
roles of the cyclic closure. This is a fixed-core-order theorem only; it
proves no geometric or global optimality statement.

The paired monotone interval shift is now exact as well. With the same
\(q=\lfloor(4m+3)/5\rfloor\), use (PG46) to send \(P_q\) to the closing
gap while leaving all other paths in increasing order. Its sole maximizing
subset is the same \(B_m\), and
\[
K={572m^3+619m^2+8mq+207m+4q^2+16q+22\over2}.
\]
The five residue branches retain coefficient \(143/500\). This value is
strictly below K825 and preclosing PG46 on every row, below closing PG46 for
\(m\ge4\), and equal to closing PG46 only at \(m=3\). PG49-star is smaller
by exactly
\[
{m(m-1)(m-2)\over3}
={ (n-3)(n-13)(n-23)\over3000}.
\]
The two orders differ only on the singleton block, so its reversal supplies
the whole cubic improvement from \(143/500\) to \(857/3000\), although the
individual gap contributions have mixed signs. The deletion, shortcut, and
cyclic-closure proof is exact and has no angular, geometric, or global
optimality consequence.

The odd-\(v\) parity analogue is now exact separately at the \(W\)-level.
On \(n=10m+8\), \(m\ge1\), put
\(q=\lfloor(4m+5)/5\rfloor=\kappa_{2m}\) and use the fixed map (PGODD-6):
shift the remaining triples and the doubleton, reverse only the actual
singleton block, and place \(P_q\) in the genuine closing gap. The five
image blocks partition every path index, all values satisfy the exact odd
Ferrers thresholds, and the boundary row is \((0,2,1)\). The literal closing
word and every cyclic distance class give
\[
W={(8m+8)(8m+7)\over2}.
\]
This theorem does not evaluate \(K\) and has no angular, geometric, or
global-optimality consequence.

Separately, prior global results disprove the former target
\(R_2^*(n)=n^3/(6\pi)(1+o(1))\). The stronger target
\(R_2^*(n)=n^3/(6\pi)+O(n^2)\) is also disproved.

The checked-artifact verification path is now a project foundation: the
repository has a GitHub Actions matrix for tests, checked-artifact semantic
verification, schema checks, and whitespace hygiene. Successful local checks
are recorded in the trust-layer and cross-platform hash task dossiers. The
later green hosted-run statement was user-reported without a commit SHA, run
identifier, URL, or independent inspection, so it establishes no hosted
status for a specific commit. GitHub Actions status for the current `HEAD` has
not been independently verified.

## Asymptotic Status

DISPROVED CLAIM:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}\bigl(1+o(1)\bigr).
\]

DISPROVED CLAIM:

\[
R_2^*(n)
=
\frac{n^3}{6\pi}+O(n^2).
\]

The cubic order is exact, but existence of a limiting coefficient, a
leading-term asymptotic formula, and an upper bound matching the current
linear-block lower coefficient remain unresolved. Current exact bounds give
\[
\frac{434+4\sqrt2}{1587\pi}
\le
\liminf_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le
\limsup_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le\frac{143}{500\pi}.
\]

## Scope And Guardrails

In scope:

- the two-dimensional quadratic-radii problem;
- exact geometric formulation;
- cyclic orders and all-pairs non-overlap constraints;
- numerical optimization and independent verification;
- certified finite cases where feasible;
- asymptotic lower and upper bound research.

Out of scope:

- treating finite computation as a proof for all `n`;
- treating checked brackets as exact optimum values;
- treating the fixed-\(k\) normalized simplex lemma as the source of the
  separate direct finite-\(k\) charging theorem, treating that theorem as
  uniform for \(k=k(n)\), interchanging \(k\) with \(n\), or improving any
  bound for \(\Lambda_n\) or \(R_2^*(n)\) without a separate argument; the
  all-fixed-\(k\) supremum proof above is that required separate argument;
- silently generalizing Ringmin results to quadratic radii;
- modifying the original Ringmin repository.

## Angular Constraint

For peripheral radii \(r_i,r_j\) and central radius \(R\), the minimum angular separation is

\[
\theta_R(r_i,r_j)
=
2\arcsin
\sqrt{
\frac{r_i r_j}
{(R+r_i)(R+r_j)}
}.
\]

For quadratic radii:

\[
\theta_R(i^2,j^2)
=
2\arcsin
\left(
\frac{ij}
{\sqrt{(R+i^2)(R+j^2)}}
\right).
\]

All-pairs non-overlap constraints are part of the problem, not merely adjacent-pair constraints.

## Fixed-Order Angular And STN Semantics

For a fixed counterclockwise order \((r_0,\dots,r_{m-1})\), \(m\ge3\),
anchor \(p_0=0\). Exact all-pairs feasibility is equivalent to

\[
\theta_R(r_i,r_j)
\le p_j-p_i
\le2\pi-\theta_R(r_i,r_j)
\qquad(0\le i<j<m).
\]

The lower inequality is the directed edge \(j\to i\) of weight
\(-\theta_{ij}\); the upper is \(i\to j\) of weight
\(2\pi-\theta_{ij}\). The system is feasible exactly when it has no negative
directed cycle, and shortest-path distances recover a feasible potential.
Moreover, \(\theta_R\) is continuous and strictly decreasing in \(R\), so the
feasible-radius set is monotone upward.

Under genuine interval enclosures, a relaxed cycle whose recomputed weight
upper bound is strictly negative excludes the lower endpoint \(L\) and a right
neighborhood. An explicit all-pairs witness whose recomputed slack lower bounds
are nonnegative includes the upper endpoint \(U\). Thus the fixed-order
threshold infimum lies in \((L,U]\), without assuming an unproved optimum.
The same half-open semantics holds after exhaustive finite order aggregation.
`research/FIXED_ORDER_ANGULAR_STN.md` contains the proof, and
`docs/INTERVAL_BACKEND_TRUST.md` states the separate backend assumptions.

## Fixed-Order Maximum Cyclic Ratio

For a complete quadratic index order \(\sigma=(\sigma_0,\dots,\sigma_{n-1})\),
an STN edge \(u\to v\) contributes \(\sigma_u\sigma_v\) to \(S(C)\), and it
contributes one to \(q(C)\) exactly when \(u<v\). Edge occurrences are counted
with multiplicity; a two-cycle on labels \(i,j\) therefore has
\(S=2ij\) and \(q=1\). Lower-only edges strictly decrease position, so every
closed walk has \(q\ge1\). Closed-walk decomposition reduces the maximum to
the finite simple-cycle set.

For a nonempty subset of positions
\(T=\{i_0<\cdots<i_{m-1}\}\), put
\[
P_\sigma(T)=
\sum_{r=0}^{m-1}\sigma_{i_r}\sigma_{i_{r+1\bmod m}}.
\]
For \(m=1\) this is \(\sigma_{i_0}^2\), while for \(m=2\) the same
unordered product occurs twice.
A `q=1` cycle is forced to traverse those positions as
\(i_0,i_{m-1},\dots,i_1,i_0\), so
\[
\Lambda^{(1)}(\sigma)
=\max_{q(C)=1}S(C)
=\max_{|T|\ge2}P_\sigma(T)
=\max_{T\ne\varnothing}P_\sigma(T).
\]
Here the singleton convention is \(P_\sigma(\{i\})=\sigma_i^2\); singleton
scores never change the maximum for \(n\ge3\).
The full induced order has score at least
\(n(n+1)(n+2)/6\). By \(2ij\le i^2+j^2\), every vertex-simple cycle
with \(q\ge2\) has ratio at most
\[
{1\over2}\sum_{i=1}^n i^2
={n(n+1)(n+2)\over6}-{n(n+1)\over4}
<{n(n+1)(n+2)\over6}.
\]
Therefore the full ratio is one-wrap saturated for every complete order:
\[
\Lambda(\sigma)=\Lambda^{(1)}(\sigma),
\]
and \(\Lambda(\sigma)\) and \(\Lambda_n\) are integers. The strict separation
is for vertex-simple multi-wrap cycles; a general closed walk may repeat a
maximizing one-wrap component.

For a cyclic core order \(\tau\) of \(\{2,\ldots,n\}\), let
\[
K(\tau)=
\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U).
\]
If \(\tau\) is obtained from \(\sigma\) by deleting label \(1\), then every
subset avoiding \(1\) retains its score. The subsets containing \(1\) split
into three cases: \(\{1\}\) has score \(1<4\); \(\{1,j\}\) has score
\(2j\le j^2\); and when \(1\) has distinct core neighbors \(a,b\), deleting
it increases the induced cyclic sum by
\(ab-a-b=(a-1)(b-1)-1\ge1\). Therefore
\[
\Lambda(\sigma)=K(\tau)
\]
independently of the insertion gap. Deletion and insertion then give
\[
\Lambda_n=\min_\tau K(\tau).
\]
Singletons do not maximize \(K\), so the accepted same-order comparison gives
\[
K(\tau)\le\Lambda_{\rm same}(\tau)\le(n-1)W(\tau),
\qquad
\Lambda_n\le(n-1)W_n.
\]
This comparison does not assert equality or common minimizers.

The exact angular comparisons
\[
{2ij\over R+n^2}<\theta_R(i^2,j^2)<{2ij\over R}
\]
and the fixed-order negative-cycle theorem give the requested weak sandwich
and its strict refinement
\[
{\Lambda(\sigma)\over\pi}-n^2
<\rho_\sigma
<{\Lambda(\sigma)\over\pi}
\qquad(n\ge3).
\]
Minimizing over complete orders gives
\[
{\Lambda_n\over\pi}-n^2
<R_2^*(n)
<{\Lambda_n\over\pi},
\qquad
0<\Lambda_n-\pi R_2^*(n)<\pi n^2.
\]
Consequently
\[
R_2^*(n)<{\Lambda_n\over\pi}
\le{(n-1)W_n\over\pi}
\qquad(n\ge3).
\]
`research/FIXED_ORDER_CYCLE_RATIO.md` contains the definitions, saturation
and elimination proofs, scorer algorithm, the exact reduced values
\(\Lambda_9=239\) and \(\Lambda_{10}=323\), their complete finite core
minimizer classifications, independent bounded oracles, comparison with
\(W\), the exact arbitrary consecutive-tail split-history theorem through
every sublinear block length, the positive cubic residual for the first
explicit linear block, its global lower-bound corollary, the exact two- and
three-prefix optimizations, the minimal-threshold finite theorem at the
irrational three-prefix optimizer, the exact four-prefix one-use theorem and
its global compact optimization, two independent four-prefix diagnostics, the
exact one-use theorem for every finite number of selected prefixes, its
bounded six-prefix dossier oracle, the historical five-prefix oracle, the
exact normalized prefix-simplex lemma
for every fixed \(k\), its envelope classification, the full clipped
arbitrary-\(k\) Bellman envelope and global all-middle theorem, the exact
all-fixed-\(k\) supremum corollary and its strict admissibility/quantifier
audit, plus the
exact global \(k=5\) compact optimization, all 21
clipping regimes and compact faces, its unique eleven-parameter quadratic-surd
optimizer, strict comparison \(C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*}\), and
standalone exact diagnostic. One-wrap saturation
and insertion independence concern the product ratio; they do not reduce
exact angular-STN feasibility to one-wrap cycle checks or make \(\rho_\sigma\)
insertion-independent. The `n=10` proof classifies equality in the
seven-label lemma, then labels `3` and `2`, and only afterward derives the
783 complete classes by inserting label `1`.

## Current Knowledge Status

- COMPUTER-CERTIFIED RESULT: checked finite global interval brackets exist for `n=3,4,5,6` under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` backend contract.
- EXACT THEOREM: for every fixed labelled cyclic order of at least three
  positive radii, the exact all-pairs angular system is equivalent to the
  implemented STN; feasibility is equivalent to absence of a negative cycle,
  shortest paths recover a feasible potential, and the fixed-order
  feasible-radius set is an upper interval.
- EXACT THEOREM (ABSTRACT ENCLOSURE IMPLICATION): genuine lower angular bounds
  and upper \(2\pi\) bounds make a strictly negative relaxed cycle decisive;
  genuine upper angular bounds and a lower \(2\pi\) bound make nonnegative
  all-pairs witness slacks decisive. The threshold infimum then lies in
  \((L,U]\): \(L\) is excluded and \(U\) is included.
- CONDITIONAL COMPUTER-CERTIFIED RESULT: current checked artifacts instantiate
  that implication only under the documented guarded `mpmath.iv` contract.
- EXACT THEOREM: the complete fixed-order maximum cyclic ratio satisfies
  \[
  {\Lambda(\sigma)\over\pi}-n^2
  <\rho_\sigma
  <{\Lambda(\sigma)\over\pi},
  \]
  and its global minimum satisfies the analogous strict sandwich with
  \(R_2^*(n)\). Thus \(0<\Lambda_n-\pi R_2^*(n)<\pi n^2\).
- EXACT THEOREM (ONE-WRAP SATURATION): for every complete order and `n>=3`,
  \[
  \Lambda(\sigma)=\Lambda^{(1)}(\sigma)
  =\max_{|T|\ge2}P_\sigma(T)
  =\max_{T\ne\varnothing}P_\sigma(T),
  \]
  where \(P_\sigma(T)\) is the cyclic adjacent-product sum on the order
  induced by the position subset \(T\), with a two-element product counted
  twice. Every vertex-simple cycle with `q>=2` is strictly below the one-wrap
  maximum. Consequently \(\Lambda(\sigma)\) and \(\Lambda_n\) are integers.
- EXACT THEOREM (INDEX-ONE ELIMINATION): for a core order \(\tau\), define
  \(K(\tau)\) as the maximum cyclic adjacent-product sum over its nonempty
  induced subsets, with singleton squares and twice-counted two-element
  products. If deleting label \(1\) from \(\sigma\) gives \(\tau\), then
  \[
  \Lambda(\sigma)=K(\tau)
  \]
  independently of the insertion gap. Hence
  \[
  \Lambda_n=\min_\tau K(\tau),
  \qquad
  \Lambda_n\le(n-1)W_n,
  \qquad
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{(n-1)W_n\over\pi}.
  \]
  The insertion independence is not a statement about exact angular
  thresholds or feasible-radius sets.
- EXACT THEOREM (TWO NESTED TAILS): for `n>=4` and `1<=m<=n-3`, the exact
  obstruction based only on \(S_m,S_{m+1}\) is
  \[
  \beta_{m,n}
  =\min_{\substack{C\text{ simple on }S_{m+1}\\
                    \{a,b\}\in E(C)}}
  \left(P(C)+[m(a+b)-ab]_+\right).
  \]
  Every cycle/edge pair extends to a complete order, so
  \(\Lambda_n\ge\beta_n^{(2)}=\max_m\beta_{m,n}\). A valid
  duplicated-pairing signature must be connected and loopless, in addition to
  its automatic degree-two condition; when a fixed edge is restored, the full
  signature must pass this audit. Exact alternating cycles give
  \[
  P_{m+1,n}\le\beta_{m,n}\le P_{m+1,n}+n^2,
  \qquad
  \beta_n^{(2)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
  Hence this specific two-tail scheme does not improve the old cubic
  coefficient, although it may improve finite values. It also gives
  \(R_2^*(n)>\beta_n^{(2)}/\pi-n^2\), with the same leading geometric
  coefficient.
- EXACT THEOREM (THREE NESTED TAILS): for \(n\ge5\) and
  \(1\le m\le n-4\), deletion of \(m\), then \(m+1\), gives a bijection
  between cycles on \(S_m\) and a simple cycle \(C\) on \(S_{m+2}\) followed
  by two compatible edge splits. With
  \(\delta_t(u,v)=t(u+v)-uv\), their exact score is
  \[
  \gamma^*_{m,n}
  =
  \min_{C,e,f}
  \left[
  P(C)+
  \max\{0,\delta_{m+1}(e),
           \delta_{m+1}(e)+\delta_m(f)\}
  \right].
  \]
  The second split is nested, distinct-incident, or distinct-disjoint. Every
  signature must be connected, loopless, degree two, and linked to its
  neighbors by the literal split identities.
- EXACT METHOD-SPECIFIC THEOREM: if
  \(P^*_{m+2,n}=\min_{C\text{ simple on }S_{m+2}}P(C)\), then
  \[
  0\le\gamma^*_{m,n}-P^*_{m+2,n}<2n^2,
  \qquad
  P_{m+2,n}\le\gamma^*_{m,n}<P_{m+2,n}+2n^2.
  \]
  Therefore the optimized obstruction
  \(\Gamma_n^{(3)}=\max_m\gamma^*_{m,n}\) satisfies
  \[
  \Gamma_n^{(3)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
  This is not an asymptotic claim about \(\Lambda_n\) or \(R_2^*(n)\).
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): compatible double splits
  cover all 60 dihedral cycles for \((m,n)=(2,7)\), with interaction counts
  24 nested, 24 distinct-incident, and 12 distinct-disjoint. Exact rows
  \((P_{m+2,n},P^*_{m+2,n},\gamma^*_{m,n})\) are
  \((46,47,47)\), \((116,117,118)\), \((235,237,239)\), and
  \((320,322,323)\) for the checked small cases. These are test-local finite
  checks, not the all-\(n\) proof.
- EXACT THEOREM (ARBITRARY NESTED-TAIL BLOCK): for
  \(2\le r\le n-2\), \(1\le m\le n-r-1\), and
  \(\ell=m+r-1\), deletion followed by reverse insertion is a bijection
  between cycles on \(S_m\) and a base cycle on \(S_\ell\) with
  \(r-1\) compatible descending edge splits. With exact corrections
  \(A_i\),
  \[
  \gamma^{(r)}_{m,n}
  =\min_{\text{compatible histories}}\left[P(C)+
  \max_{0\le j\le r-1}\sum_{i=1}^jA_i\right].
  \]
  Every intermediate signature must be a connected simple spanning cycle and
  satisfy the literal split identity. Long nested domino histories remain
  admissible; the three-tail reduction to distinct base edges is not a
  general parametrization.
- EXACT METHOD-SPECIFIC THEOREM: uniformly,
  \[
  0\le\gamma^{(r)}_{m,n}-P^*_{m+r-1,n}
  \le\sum_{t=m}^{m+r-2}[t^2-2]_+<(r-1)n^2,
  \]
  and
  \[
  P_{m+r-1,n}\le\gamma^{(r)}_{m,n}
  <P_{m+r-1,n}+rn^2.
  \]
  Consequently fixed \(r\) gives the old cubic coefficient with
  \(O_r(n^2)\) error, every \(r=o(n)\) gives the same coefficient with
  \(o(n^3)\) error, and linear \(r=\Theta(n)\) is only the first scale not
  excluded from changing it by this uniform estimate.
- EXACT METHOD-SPECIFIC THEOREM (JOINTLY OPTIMIZED ONE-PREFIX LINEAR BLOCK): for
  \(m=1\), \(r_n=\lfloor\alpha n\rfloor\),
  \(s_n=\lceil\beta n\rceil\), the proof-valid region is exactly
  \[
  0<\alpha<1,
  \qquad 0<\beta<\alpha,
  \qquad 0\le\lambda\le1.
  \]
  Complete boundary analysis proves the unique maximin parameters
  \[
  \alpha_*=1-{\sqrt3\over3},
  \qquad
  \beta_*={5\over6}-{\sqrt3\over4},
  \qquad
  \lambda_*={88-32\sqrt3\over73}.
  \]
  With \(r_n^*=\lfloor\alpha_*n\rfloor\) and
  \(s_n^*=\lceil\beta_*n\rceil\), the exact floor/ceiling domain is
  \(n\ge86\). For \(n\ge90\), the finite slack/prefix bound implies
  \[
  \gamma^{(r_n^*)}_{1,n}-P^*_{r_n^*,n}
  \ge
  c_{{\rm res},*}n^3-Q_*n^2,
  \qquad
  c_{{\rm res},*}={26-15\sqrt3\over54}>0,
  \]
  where \(Q_*=(233-128\sqrt3)/72\). Every original base edge is charged at
  most once, recursive child edges have a separate local floor, and the
  exact maximum over all prefixes retains the selected prefix. Hence the
  certified residual is genuinely cubic. It is not the exact residual.
  Moreover, for \(n\ge86\),
  \[
  \Lambda_n
  \ge\Gamma_n^{(r_n^*)}
  \ge\gamma^{(r_n^*)}_{1,n}
  \ge P_{r_n^*,n}+(r_n^*-s_n^*)F_n^*,
  \]
  with no max--min exchange. It follows that
  \[
  \Lambda_n\ge{4+2\sqrt3\over27}n^3
  \quad(n\ge90),
  \qquad
  R_2^*(n)>{4+2\sqrt3\over27\pi}n^3-n^2.
  \]
  The total coefficient is uniquely optimal only within the one-prefix
  specialization of CR28ax--CR28bg; it is not an exact leading coefficient,
  and convergence and production claims do not follow.
- EXACT METHOD-SPECIFIC THEOREM (TWO SELECTED PREFIXES): for
  \(0<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1\), combining the two
  selected prefix heights before charging gives
  \[
  C_2=p(\alpha)
  +(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_{\rm hi})
  +(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_{\rm lo}).
  \]
  The base-slack partition uses every original edge at most once across both
  segments, and the recursive floor covers every child-edge split. The
  ordered weights reduce exactly to independent clipped optima because their
  order is automatic. The six resulting branches, both transition surfaces,
  every density collision, and every compact boundary face give the unique
  global optimizer
  \[
  \left(
  \alpha_*,\beta_{1,*},\beta_{2,*},
  \lambda_{{\rm hi},*},\lambda_{{\rm lo},*}
  \right)
  =
  \left(
  {629-23\sqrt{143}\over829},
  {2286-77\sqrt{143}\over3316},
  {2010-59\sqrt{143}\over3316},
  {6264-288\sqrt{143}\over5281},
  {3888-192\sqrt{143}\over4273}
  \right),
  \]
  with
  \[
  C_{2,*}={491596+6578\sqrt{143}\over2061723}.
  \]
  Hence
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{2,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{2,*}\over\pi}.
  \]
  At the rational witness \((3/7,2/5,3/8,1/2,1/4)\), the smaller exact
  coefficient \(72825421/263424000\) retains the explicit finite theorem.
  With \(r_n=\lfloor3n/7\rfloor\),
  \(s_{1,n}=\lceil2n/5\rceil\), and
  \(s_{2,n}=\lceil3n/8\rceil\), the exact uniform threshold is \(n=59\),
  and
  \[
  \Lambda_n\ge C_2n^3,
  \qquad
  R_2^*(n)>{C_2\over\pi}n^3-n^2
  \quad(n\ge59).
  \]
  No finite rounding theorem for the irrational two-prefix optimizer is
  asserted, and \(C_{2,*}\) is a template-optimal lower coefficient rather
  than an exact residual or geometric leading coefficient.
- EXACT METHOD-SPECIFIC THEOREM (THREE SELECTED PREFIXES): for
  \(0<\beta_3<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_3\le\lambda_2\le\lambda_1\le1\), combining all three
  prefix heights before charging assigns one weight to each disjoint segment.
  One base-slack partition then uses every original edge at most once, while
  the recursive floor covers every child edge through both boundaries,
  including fully nested edges with two inserted endpoints. The exact
  coefficient is
  \[
  C_3=p(\alpha)
  +(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)
  +(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)
  +(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3).
  \]
  The three clipped individual optima are automatically ordered. Exact
  optimization on the full compact closure gives the unique normalized point
  \[
  \left({X_1\over A},{X_2\over A},{X_3\over A}\right)
  =
  \left({1058\over1263},{276\over421},{184\over421}\right),
  \]
  with
  \[
  \alpha_*={685623-421\sqrt{377823}\over993423},
  \qquad
  C_{3,*}
  ={753972193324+106042322\sqrt{377823}\over2960667770787}.
  \]
  Hence
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{3,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{3,*}\over\pi},
  \]
  and \(C_{3,*}>C_{2,*}\). The exact floor/ceiling theorem at this optimizer
  has minimal uniform threshold \(159\). Its finite clipped weights and
  literal expression \(\mathcal B_{3,n}\) and integer closure
  \(\mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil\) satisfy
  \[
  \Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
  \qquad
  R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2
  \quad(n\ge159).
  \]
  The explicit polynomial remainder has quadratic coefficient
  \(\kappa_*>1/3\). This is a finite template theorem, not an exact residual
  or geometric leading coefficient, and no charging beyond three prefixes is
  asserted.
- EXACT METHOD-SPECIFIC THEOREM (FOUR SELECTED PREFIXES): for
  \(0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1\), the five
  convex coefficients combine all four selected heights before any original
  edge slack is assigned. They telescope to weights
  \(\lambda_1,\lambda_2,\lambda_3,\lambda_4\) on four disjoint segments.
  The literal history induces one canonical partition of original edges into
  injectively charged and unused edges, and the recursive invariant covers
  every nested child split through all three boundaries. Thus
  \[
  \begin{aligned}
  \gamma^{(r)}_{1,n}\ge{}& P_{r,n}
  +(r-s_1)F_{1,n}
  +(s_1-s_2)F_{2,n}\\
  &+(s_2-s_3)F_{3,n}
  +(s_3-s_4)F_{4,n}.
  \end{aligned}
  \]
  The compact coefficient problem reduces all four ordered weights exactly.
  Its fifteen clipping regimes, winning transitions, density collisions, and
  compact facets are completely audited. The unique strict `MMMM` optimizer
  gives
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403}
  >C_{3,*},
  \]
  and hence
  \(\liminf\Lambda_n/n^3\ge C_{4,*}\) and
  \(\liminf R_2^*(n)/n^3\ge C_{4,*}/\pi\). No finite rounding is claimed;
  the separate arbitrary finite-prefix theorem below makes no coefficient
  claim by itself.
- EXACT FINITE METHOD-SPECIFIC THEOREM (ARBITRARILY MANY FINITE SELECTED
  PREFIXES): fix any integer \(k\ge1\) and
  \[
  0<\beta_k<\cdots<\beta_1<\alpha<1,
  \qquad
  0\le\lambda_k\le\cdots\le\lambda_1\le1.
  \]
  Let \(r=\lfloor\alpha n\rfloor\),
  \(s_i=\lceil\beta_i n\rceil\), \(s_0=r\), and
  \(\lambda_{k+1}=0\). The \(k+1\) convex coefficients combine
  \(0,H_1,\ldots,H_k\) before charging and telescope to the \(k\) disjoint
  segments \(I_i=\{s_i,\ldots,s_{i-1}-1\}\). Every literal history
  canonically partitions the original edges into injectively charged and
  unused edges. A descending induction on inserted labels is independent of
  the number of segment boundaries and covers arbitrary nesting. On the
  finite domain
  \[
  2\le r\le n-2,
  \qquad
  1\le s_k<\cdots<s_1\le r-1,
  \]
  one has
  \[
  \gamma^{(r)}_{1,n}\ge
  P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
  \]
  The case \(k=1\) recovers the one-prefix theorem and \(k=5\) recovers the
  former five-segment statement. No positivity of the individual floors is
  required. Pointwise validity for every finite admissible row supplies no
  uniform cutoff, rounding, or parameter control for \(k=k(n)\), and no
  \(k\to\infty\) passage. Its individual fixed-\(k\) consequences are
  combined with the normalized theorem below.
- EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (EXPLICIT FIVE-PREFIX WITNESS):
  with \(D=30143556935103\) and
  \[
  (N_1,\ldots,N_5)
  =(26881208992898,23392470652668,19595592993288,
  15335681473008,10223787648672),
  \]
  the fifth simplex point is \(x_i=N_i/D\). At
  \(\alpha=13/30\), \(s=43/30\), and \(A=3/10\), define
  \[
  \beta_i={s+Ax_i\over4},
  \qquad
  \lambda_i={Ax_i\over\beta_i}.
  \]
  Exact ordering gives
  \[
  0<\beta_5<\cdots<\beta_1<\alpha<1,
  \quad
  {s\over4}<\beta_i<{s\over3},
  \quad
  0<\lambda_5<\cdots<\lambda_1<1.
  \]
  Thus this fixed rational tuple is strictly all-middle and eventually
  integer-admissible. Its coefficient and exact comparison are
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000}
  >{75\over271}>C_{4,*}.
  \]
  Consequently
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{5,\mathrm{rat}},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{5,\mathrm{rat}}\over\pi}.
  \]
  The global theorem below proves this rational specialization is strict
  suboptimal; it remains the tuple with the finite theorem.
- EXACT METHOD-SPECIFIC THEOREM (GLOBALLY OPTIMIZED FIVE PREFIXES): the full
  eleven-parameter compact closure clips coordinatewise to 21 ordered regimes.
  Every transition, density and weight collision, and compact face is audited.
  The unique point is strictly all-middle, with
  \[
  \alpha_{5,*}
  ={422413777961580309772684503
   -10047852311701\sqrt{183342238504950468196395903}
   \over661485317418210151348973103},
  \]
  the five exact pairs (CR28dz37)--(CR28dz38), and
  \[
  C_{5,*}
  ={346693217780244687187063490332457027500975566238012204
   +1228130489996268437333105902690103574002
    \sqrt{183342238504950468196395903}
   \over1312688475479610714750859896048564873968757997852345827}
  >C_{5,\mathrm{rat}}>C_{4,*}.
  \]
  Hence the two liminf bounds hold with \(C_{5,*}\). This is fixed \(k=5\)
  and is the exact optimum of that template; it supplies no finite rounding
  at the irrational point or growing-\(k\) passage. The all-fixed-\(k\)
  corollary below gives a strictly larger general lower coefficient.
- EXACT FINITE METHOD-SPECIFIC THEOREM (FIXED RATIONAL FIVE-PREFIX WITNESS):
  retain the preceding rational parameters, define
  \(r_n=\lfloor13n/30\rfloor\) and
  \(s_{i,n}=\lceil\beta_i n\rceil\), and keep the original fixed weights in
  \(F_{i,n}=G_{n,\lambda_i}(s_{i,n})\). The minimal uniform threshold for
  the block conditions, strict order, five nonempty segments, and all five
  finite middle branches is \(234\); at \(233\), the first segment is
  empty. The literal expression
  \[
  \mathcal B_{5,n}
  =P_{r_n,n}+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})F_{i,n}
  \]
  and \(\mathcal I_{5,n}=\lceil\mathcal B_{5,n}\rceil\) satisfy
  \[
  \Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
  >C_{5,\mathrm{rat}}n^3
  \qquad(n\ge234).
  \]
  The fixed weights generally differ from the finite clipped optima; the
  exact rounded-bound remainder is not the true block residual.
- EXACT THEOREM (NORMALIZED PREFIX SIMPLEX): for every fixed \(k\ge1\),
  \[
  M_k=\max_{1\ge x_1\ge\cdots\ge x_k\ge0}
  \sum_{i=1}^k(x_{i-1}-x_i)x_i^2,
  \qquad x_0=1,
  \]
  has a unique maximizer with \(1>x_1>\cdots>x_k>0\). With \(M_0=0\),
  \[
  q_k={2\over3(1-M_{k-1})},
  \qquad
  M_k={q_k^2\over3}
  ={4\over27(1-M_{k-1})^2}
  \nearrow{1\over3}.
  \]
  Its ratios obey
  \[
  r_i=q_{k-i+1},
  \qquad
  q_1=r_k={2\over3},
  \qquad
  q_{m+1}={2\over3-q_m^2},
  \qquad
  r_i={2\over3-r_{i+1}^2}.
  \]
  The first five rows are
  \[
  \begin{array}{c|c|c|c}
  k&(x_1,\ldots,x_k)&M_k&M_k/8\\ \hline
  1&(2/3)&4/27&1/54\\
  2&(18/23,12/23)&108/529&27/1058\\
  3&(1058/1263,276/421,184/421)&1119364/4785507&279841/9571014\\
  4&(3190338,2672508,2091528,1394352)/3666143
    &3392752184748/13440604496449&848188046187/26881208992898\\
  5&(26881208992898,23392470652668,19595592993288,
     15335681473008,10223787648672)/30143556935103
    &722599396919860307414438404/2725902074099388500860861827
    &180649849229965076853609601/5451804148198777001721723654
  \end{array}
  \]
  The first five agree exactly with the optimized one- through five-prefix
  simplex cases; the fifth also supplies the explicit rational witness above.
- EXACT NORMALIZED-ENVELOPE CLASSIFICATION: on \([1/3,1]\),
  \[
  E_k(\alpha)
  =p(\alpha)+{M_k\over8}(3\alpha-1)^3
  \nearrow
  E_\infty(\alpha)
  =p(\alpha)+{(3\alpha-1)^3\over24}
  \]
  uniformly. The formal normalized-polynomial envelope has the unique
  maximum \(1/3\) at \(\alpha=1\); on \([1/3,1)\) it is only a supremum. The
  limiting all-middle closure \([1/3,1/2]\) has the unique maximum
  \((434+4\sqrt2)/1587\) at \((13-2\sqrt2)/23\).
- EXACT GLOBAL CLIPPED FINITE-PREFIX CLASSIFICATION: for every finite \(k\),
  coordinatewise clipping gives the compact Bellman envelope
  \[
  \mathscr H_k(\alpha)
  =p(\alpha)+(1+\alpha)^3V_k\!\left({\alpha\over1+\alpha}\right).
  \]
  Its \((k+1)(k+2)/2\) regimes are finite lower Darboux sums for the
  increasing clipped floor. The integral envelope is the explicit
  three-piece polynomial in (CR28dw20). Its outer pieces cannot win, so the
  unique global maximizer at every finite \(k\) is strict all-middle, with
  value \(C_{k,*}\), and
  \(C_{k,*}\nearrow(434+4\sqrt2)/1587\). This unattained limit is the exact
  supremum of the entire continuous finite-prefix family.
- EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (ALL FIXED \(k\)): at
  \(\alpha_\infty=(13-2\sqrt2)/23\), define from each unique optimizer
  \(x^{(k)}\)
  \[
  \beta_i={1+\alpha_\infty+(3\alpha_\infty-1)x_i^{(k)}\over4},
  \qquad
  \lambda_i={(3\alpha_\infty-1)x_i^{(k)}\over\beta_i}.
  \]
  For every finite \(k\), these parameters are strictly ordered and
  all-middle. A tuple-dependent threshold \(N_k\) suffices for charging, and
  the fixed-parameter limit gives
  \[
  L_\Lambda\ge
  p(\alpha_\infty)+{(3\alpha_\infty-1)^3M_k\over8}.
  \]
  Taking the supremum of these scalar inequalities proves
  \[
  \boxed{
  L_\Lambda\ge{434+4\sqrt2\over1587},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}
  \ge{434+4\sqrt2\over1587\pi}.
  }
  \]
  No \(k=k(n)\), uniform threshold, or interchange of limits occurs.
  Moreover
  \(C_{5,*}<277/1000<(434+4\sqrt2)/1587\), so \(C_{5,*}\) remains only the
  exact fixed-\(k=5\) template optimum.
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC): a standalone `Fraction`
  diagnostic independently checks the value and ratio recurrences, direct
  objectives, stationarity, strict feasibility, and the first four exact
  rows for \(k=1,\ldots,8\). Literal denominator-12 enumeration and a
  separate discrete Bellman calculation agree on all 203,489 grid tuples.
  This bounded check corroborates the proof but is not the all-real theorem.
- LIMITATION: the normalized simplex theorem is independent of the charging
  argument. A separate direct proof establishes one-use charging for every
  finite admissible \(k\). Neither result supplies control uniform in a
  growing \(k=k(n)\) or an interchange between \(k\) and \(n\); neither is
  needed for the all-fixed-\(k\) supremum corollary. No finite rounded theorem
  at its unattained supremum coefficient is asserted.
- VERIFIED FACT (FINITE EXACT DOSSIER ORACLE): the standalone
  ops/TASK-20260716__four_prefix_charging/literal_oracle.py imports no
  project or test helper and checks all 840 literal four-split histories from
  \(C_0=(11,14,12,13)\). It verifies the convex telescoping identity, the
  canonical original-edge slack partition, all recursive floors, 840
  distinct final cycles, and 120 fourth splits with two previously inserted
  endpoints. This bounded check corroborates but does not prove the
  all-history theorem.
- VERIFIED FACT (FINITE EXACT FIVE-PREFIX DOSSIER ORACLE): the standalone
  `ops/TASK-20260717__five_prefix_charging/literal_oracle.py` imports only
  standard-library exact arithmetic and checks all 15,120 five-split local
  histories of \(C_0=(13,17,14,16,15)\). All final cycles are distinct. It
  covers 120 histories charging all five original edges and 2,520 fifth
  splits between two previously inserted labels, and verifies every linkage,
  convex, partition, invariant, local-floor, and five-segment assertion. This
  bounded check corroborates but does not prove the all-history theorem.
- VERIFIED FACT (FINITE EXACT SIX-PREFIX DOSSIER ORACLE): the sole new
  dossier-local script uses only standard-library exact arithmetic and checks
  all 332,640 literal histories of
  \(C_0=(15,20,16,19,17,18)\). It includes 720 histories charging all six
  original edges and 60,480 sixth splits between two inserted labels. Every
  indexed convex, partition, invariant, local-floor, and six-segment assertion
  passes. This bounded computation changes no production enumerator and does
  not prove the arbitrary finite-\(k\) theorem.
- VERIFIED FACT (INDEPENDENT EXACT FOUR-PREFIX OPTIMIZATION DIAGNOSTIC): the
  standalone standard-library script at
  ops/TASK-20260717__global_four_prefix_optimization/exact_diagnostic.py
  checks exact clipping-gap factorizations on rational grids, both \(C^1\)
  joins, all fifteen branch witnesses, exact transition weights and collision
  reductions, the specialized \(k=4\) simplex certificate, end-to-end
  original-objective evaluation at the quadratic-surd optimizer, its
  primitive irreducible polynomial and isolating interval, and the separator from
  \(C_{3,*}\). It imports no project, production, or test helper and
  corroborates rather than replaces the compact proof.
- VERIFIED FACT (INDEPENDENT EXACT FIVE-PREFIX RATIONAL DIAGNOSTIC): the
  standalone standard-library script at
  ops/TASK-20260717__five_prefix_explicit_asymptotic_witness/fraction_diagnostic.py
  uses only fractions.Fraction. It checks \(q_5,M_5\), the direct simplex
  objective and stationarity, every reduced cutoff and weight, strict
  all-middle admissibility, equality of the direct and normalized coefficient
  evaluations, and the two positive integer margins proving
  \(C_{5,\mathrm{rat}}>75/271>C_{4,*}\). It corroborates but does not replace
  the written proof.
- VERIFIED FACT (INDEPENDENT GLOBAL FIVE-PREFIX OPTIMIZATION DIAGNOSTIC):
  the standalone standard-library script at
  ops/TASK-20260717__global_five_prefix_optimization/exact_diagnostic.py
  checks all 21 clipped words, five transition rows, collision identities,
  primitive optimizer and coefficient polynomials, rational isolating
  intervals, strict all-middle inequalities, coefficient identity, and exact
  comparison margins. It imports no project, test, production, artifact,
  backend, certificate, or enumeration helper.
- VERIFIED FACT (FINITE EXACT FIVE-PREFIX FLOOR/CEILING DIAGNOSTIC): the
  standalone standard-library script at
  `ops/TASK-20260717__five_prefix_finite_theorem/exact_diagnostic.py` checks
  the exact boundary rows \(233\) through \(246\), predicate-by-predicate
  last failures, symbolic-tail margins, fixed-weight local floors, integer
  closure, stationarity cancellation, exact remainder, and uniform sign. It
  imports no project or test helper and corroborates rather than proves the
  symbolic tail.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): a test-local Fraction
  oracle checks all 46,620 depth-three histories from one bounded base,
  including 70 distinct recursive second-step prefixes (2,590 full-history
  occurrences), 4,970 recursive third splits, and 70 fully nested third
  splits. Separate exact grids verify the ordered-weight
  reduction, all ten clipped regimes, the compact closure, and the simplex
  factorization. Test-local \(\mathbb Q(\sqrt{377823})\) arithmetic verifies
  the optimizer, strict domain, coefficient polynomial, isolating interval,
  and strict comparison with \(C_{2,*}\), without production code or a limit
  change.
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260716__three_prefix_finite_theorem/exact_diagnostic.py`
  independently implements \(\mathbb Q(\sqrt{377823})\), exact surd
  floor/ceil, and finite clipped weights. It scans \(1\le n\le170\), checks
  the boundary rows \(158,159,170,171\), verifies the symbolic tail
  thresholds, and checks the literal, polynomial, and
  \(C_{3,*}n^3\) comparisons through \(n=1000\). This bounded exact
  computation corroborates the finite arithmetic; the written charging and
  symbolic tail prove the all-\(n\ge159\) theorem.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): independent rational and
  \(\mathbb Q(\sqrt{143})\) diagnostics verify the ordered-weight reduction,
  all six branches, exact transitions \(77/139\) and \(301/419\), the cubic
  simplex maximum, the optimizer coordinates and their minimal polynomials,
  the coefficient polynomial
  \(6185169z^2-2949576z+342644\), exact rational isolating intervals, and a
  bounded rational grid over the compact closure. These checks use no
  production scorer or floating-point premise.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): test-local
  \(\mathbb Q(\sqrt3)\) arithmetic checks the optimizer, boundary identities,
  every rounded finite bound for \(86\le n\le1000\), and deterministic
  intact/recursive histories at six sizes. A separate \(n=141\) oracle covers
  all 6,972 literal depth-two histories, including all 166 recursive second
  splits, without production code or an enumeration-limit change.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): rational test-local
  diagnostics verify all 1,260 literal depth-two histories at \(n=59\),
  including all 70 recursive second splits, plus a fully nested history across
  the high/low boundary and deterministic base/recursive policies at four
  sizes. They check one-use charging, the deliberately invalid double-charge
  route, local floors, linkage, exact coefficient arithmetic, the threshold
  at 58/59, and finite rounding through \(n=1000\), without production code.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): at
  \((m,n,r)=(2,7,4)\), all 60 compatible triple-split histories agree
  signature by signature with all 60 directly generated outer cycles, and
  \[
  (P_{5,7},P^*_{5,7},\gamma^{(4)}_{2,7})=(106,107,118).
  \]
  Bounded specializations for \(r=2,3\), a multi-base \(r=4\) row, and an
  exact admissible-domino prefix are also checked test-locally without
  production code.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the exact bounded
  `Fraction` scorer gives
  \((\Lambda_3,\dots,\Lambda_8)=(12,26,47,77,118,172)\) over all 2,956
  canonical complete orders. A separate exact subset/path oracle and literal
  induced-subset maximization verify one-wrap saturation on every bounded
  order without using the production Karp recurrence or increasing its
  `n<=8` limit. A further exact regression checks all 437 canonical core
  orders and 2,957 insertion gaps and gives core minimizer counts
  `(1,1,1,3,4,12)`, while the complete counts remain
  `(1,3,4,15,24,84)`. This is not the all-order proof, a closed-form
  evaluation of the reduced minimum, or a geometric exact-optimum
  computation.
- EXACT THEOREM (FINITE \(n=9\) CORE CLASSIFICATION): equality in the
  \(S_6/S_5\) lemma forces the induced cycle
  \(\Omega=(9,5,8,6,7,4)\) up to dihedral symmetry. The exact core
  minimizers are obtained by inserting label \(3\) in one of the four gaps
  not incident to label \(4\), then inserting label \(2\) in any of the
  seven resulting gaps. Hence \(\min_\tau K(\tau)=\Lambda_9=239\), there are
  28 dihedral core minimizers, and exact label-one insertion gives 224
  complete minimizer classes. Of the core classes, 27 have sole argmax
  \(S_6\); the canonical
  class `(9,4,7,6,8,3,2,5)` also has the full core as an argmax.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a test-only direct
  generator checks all \(7!/2=2{,}520\) dihedral core classes at \(n=9\),
  literally scores all 255 nonempty subsets of each, records every maximizing
  subset, and recovers exactly the proved 28 classes and their \(27+1\)
  argmax pattern. It calls no repository canonicalizer, public enumerator, or
  production Karp scorer. The production complete-order limit remains
  `n<=8`.
- INTERPRETATION: the \(n=9\) classification is finite and combinatorial. It
  gives no exact value of \(R_2^*(9)\), geometric minimizer classification,
  all-\(n\) formula, or asymptotic claim.
- EXACT THEOREM (FINITE \(n=10\) SEVEN-LABEL LEMMA): every cyclic order
  \(\omega\) on \(\{4,\ldots,10\}\) satisfies
  \[
  \max\{P_\omega(\{4,\ldots,10\}),
        P_\omega(\{5,\ldots,10\})\}\ge323.
  \]
  The proof classifies exactly the eight duplicated-pairing signatures at
  values 320--322 and checks the six possible label-four insertion
  corrections in the sole cyclic signature.
- EXACT THEOREM (FINITE \(n=10\) SEVEN-LABEL EQUALITY CLASSIFICATION):
  equality in the preceding lemma holds in exactly the two dihedral classes
  represented by `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`, with
  \((P(T_7),P(T_6))=(321,323)\) and \((323,322)\), respectively. The proof
  separates the two tail-score branches, audits every needed label-four
  correction, and uses fixed-edge residual pairing bounds rather than the
  360-class sweep.
- EXACT THEOREM (FINITE \(n=10\) LABEL-THREE INSERTION-GAP CLASSIFICATION):
  for the partial maximum \(K_{\ge3}\) over nonempty subsets of labels
  \(3,\ldots,10\), inserting label \(3\) into
  `(10,4,7,8,6,9,5)` gives 326 on \(\{4,7\}\) and 323 on every other
  gap. Inserting it into `(10,5,9,4,7,8,6)` gives 326 on
  \(\{4,9\}\), 328 on \(\{4,7\}\), and 323 on every other gap. The
  proof uses the exact correction
  \(3(a+b)-ab=9-(a-3)(b-3)\) and complete shortcut-gain certificates.
  On the first cycle, the \(\{4,10\}\) insertion maximizes on both
  \(\{5,\ldots,10\}\) and the full partial label set; its other admissible
  gaps maximize only on \(\{5,\ldots,10\}\). Every admissible insertion in
  the second cycle maximizes only on \(\{4,\ldots,10\}\).
- EXACT THEOREM (FINITE \(n=10\) CORE MINIMIZER CLASSIFICATION): the eleven
  surviving label-three cycles give 88 pairwise distinct dihedral core
  classes after label \(2\) is inserted. Exactly 87 have \(K=323\); the
  sole exception is `(10,3,2,4,7,8,6,9,5)`, with \(K=325\) and sole
  argmax \(\{2,\ldots,10\}\). Among the 87 core minimizers, seven have
  exactly the two argmaxes \(\{5,\ldots,10\}\) and
  \(\{3,\ldots,10\}\), 40 have sole argmax \(\{5,\ldots,10\}\),
  and 40 have sole argmax \(\{4,\ldots,10\}\). Exact label-one
  elimination/insertion then gives exactly 783 complete dihedral minimizer
  classes.
- VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT): the exact shortcut-gain
  certificate for `(10,2,3,4,7,8,6,9,5)` gives \(K=323\), with precisely
  \(\{5,\ldots,10\}\) and \(\{3,\ldots,10\}\) as argmax subsets. Thus the
  accepted reduction gives \(\Lambda_{10}=323\).
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): independent test-only
  code confirms the proved equality list over all \(6!/2=360\) lemma classes,
  independently checks the pairing/correction branch data, and literally
  evaluates all 511 nonempty witness subsets. Separate literal oracles check
  all 14 label-three insertions and all \(14(2^8-1)=3{,}570\) corresponding
  subset scores, then all 88 label-two insertions and all
  \(88(2^9-1)=44{,}968\) corresponding subset scores, recording every
  argmax. Test-local dihedral keys also confirm 88 distinct core classes and
  783 distinct label-one insertions. These paths call no repository
  canonicalizer, public enumerator, or production Karp scorer, and the public
  `n<=8` boundary is unchanged.
- INTERPRETATION: the \(n=10\) result is finite and combinatorial. It gives
  no exact value of \(R_2^*(10)\), geometric minimizer statement, all-\(n\)
  formula, or asymptotic claim. The exceptional score-325 class is unique
  among the 88 candidates forced by the earlier equality classifications,
  not among all nonminimizing core orders.
- EXACT THEOREM: for every `n>=3`,
  \[
  R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2,
  \]
- EXACT THEOREM: for every `n>=4` and `1<=m<=n-2`,
  \[
  R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
  \qquad
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  \frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
  \]
- EXACT THEOREM:
  \[
  \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
  \ge
  4(\sqrt2-1)>1.
  \]
- EXACT THEOREM: if \(R^*_{2:n}\) denotes the core infimum, then
  \(R_2^*(n)=R^*_{2:n}\) for every \(n\ge12\), with equality already at the
  level of feasible-radius sets.
- EXACT THEOREM: the core with polar directions from a regular
  \((n-1)\)-gon is all-pairs feasible at the displayed radius \(U_n\),
  including all non-adjacent direction pairs, and the radius-one theorem gives
  \(R_2^*(n)\le U_n\) for every \(n\ge12\).
- EXACT THEOREM: for \(R>0\) and positive indices \(i,j\),
  \(\theta_R(i^2,j^2)<2ij/R\). In the zigzag core order
  \((n,2,n-1,3,\dots)\), indices at circular distance \(q\) satisfy
  \(ij\le qM_n\), where
  \(M_n=n(\lfloor n/2\rfloor+1)\). Hence the regular-direction core is
  all-pairs feasible at \(V_n=(n-1)M_n/\pi\), and
  \(R_2^*(n)\le V_n\) for every \(n\ge12\).
- EXACT THEOREM:
  \[
  \limsup_{n\to\infty}\frac{R_2^*(n)}{n^3}\le\frac1{2\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
  The zigzag coefficient remains a valid historical bound; the matching
  product-distance construction below improves it, and the still later
  shortcut evaluation improves the variable-spacing upper coefficient again.
- EXACT THEOREM: for every cyclic order \(\sigma\) of the core, the
  product-distance score
  \(W(\sigma)=\max_{i<j}ij/d_\sigma(i,j)\) gives strict all-pairs core
  feasibility at \((n-1)W(\sigma)/\pi\). For `n>=12`, insertion gives
  \(R_2^*(n)\le(n-1)W_n/\pi\), where \(W_n=\min_\sigma W(\sigma)\).
- EXACT THEOREM: for every `2<=m<=n-2`, oriented positional gaps induced by
  the tail \(\{m,\dots,n\}\) give
  \(W(\sigma)\ge P_{m,n}/(n-1)\).
- EXACT THEOREM: the adjacent relaxation satisfies
  \[
  A_3=6,
  \qquad
  A_n=
  \left(\left\lfloor{n\over2}\right\rfloor+1\right)
  \left(\left\lceil{n\over2}\right\rceil+2\right)
  \quad(n\ge4),
  \]
  and `patterns.interleave` realizes the formula for every \(n\).
- EXACT THEOREM: adjacent equality cycles have no low-low edges. For even
  `n=2t`, their only high-high edge is `{t+1,t+2}`; for odd `n=2t+1`, their
  only high-high edges are `{t+1,t+2}` and `{t+1,t+3}`. Removing the forced
  edge or segment leaves the parity-specific alternating active high path.
- EXACT THEOREM: with \(B_n=W_n^{(\le2)}\),
  \[
  B_n=A_n\quad(3\le n\le8),
  \qquad
  B_n>A_n\quad(n\ge9).
  \]
  Consequently \(W_n>A_n\) for every \(n\ge9\). The proof uses no
  cyclic-order enumeration beyond `n=11`.
- EXACT THEOREM: on the threshold tail \(U_T\), the exact minimum number of
  cyclic adjacencies with product greater than \(2T\) is
  \(\eta_n(T)=\max(0,2v-u+\delta_n(T))\), where
  \(\delta_n(T)\in\{0,1\}\) is the strict skip-one correction. Thus the
  exact cyclic packing requirement is \(n-1\ge2u+\eta_n(T)\). Its finite
  half-integer inversion \(Q_n\)
  satisfies \(Q_n\le B_n\), and for every \(n\ge9\),
  \[
  B_n\ge Q_n\ge
  {36-16\sqrt2\over49}\left(n+{1\over2}\right)^2.
  \]
  Hence
  \[
  \liminf_{n\to\infty}{B_n\over n^2}
  \ge {36-16\sqrt2\over49}>{1\over4}.
  \]
  Moreover, \(Q_n=((36-16\sqrt2)/49)n^2+O(n)\), so this exact refinement
  leaves the leading obstruction coefficient unchanged.
- EXACT THEOREM: every order with distance-at-most-two score at most \(T\)
  satisfies the terminal-high compatible-low incidence bound
  \[
  2v\le
  C_n(T)
  =
  \#\{\ell\in\{2,\dots,a_T-1\}:\ell b_T\le T\}
  =
  \max\left(0,\left\lfloor{T\over b_T}\right\rfloor-1\right).
  \]
  Keeping \(Q_n\) unchanged, let \(H_n\) be the least nonnegative
  half-integer satisfying both this incidence bound and
  \(\Psi_n(T)\le n-1\). Then
  \[
  B_n\ge H_n\ge Q_n,
  \qquad
  H_n={8\over25}n^2+O(n),
  \qquad
  \liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}.
  \]
  The all-\(n\) proof treats \(n=3\), \(v=0\), \(v=1\), empty tails, strict
  tail thresholds, non-strict compatible equality, and the exact floor.
  By itself this is only a lower bound; the explicit matching construction
  below supplies the reverse asymptotic inequality.
- EXACT THEOREM: for every \(n\ge9\), the explicit cyclic order
  \(\sigma_n\) with threshold \(T_n=d_n(d_n-1)/2\) satisfies
  \(W(\sigma_n)\le T_n\). Consequently,
  \[
  \lim_{n\to\infty}{B_n\over n^2}
  =\lim_{n\to\infty}{W_n\over n^2}
  ={8\over25}.
  \]
  For \(n\ge12\), regular-direction core feasibility and insertion give
  \[
  R_2^*(n)\le{(n-1)T_n\over\pi},
  \qquad
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{8\over25\pi}.
  \]
  This is the exact regular-direction product-distance coefficient and is an
  upper bound only.
- EXACT THEOREM: for the same canonical core order \(\tau_n\), the induced
  subset objective has a unique maximizer for every \(n\ge9\). On the
  symbolic rows it is the tail from \(2v+1\), with connector \(2v+2\)
  additionally deleted exactly for \(e=6,7,8\); the fourteen explicit rows
  have unique maximizing tails. Its exact quasipolynomial satisfies
  \[
  K(\tau_n)={143\over500}n^3+O(n^2).
  \]
  Hence
  \[
  \limsup_{n\to\infty}{\Lambda_n\over n^3}\le{143\over500},
  \qquad
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{143\over500\pi}.
  \]
  The proof uses exact shortcut gains and block inequalities; bounded
  max-plus and local-margin computation only corroborates it.
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260718__canonical_eight_twenty_fifths_k/exact_diagnostic.py`
  imports no project helper, reconstructs the block order, and checks every
  \(9\le n\le120\). Its increasing-path max-plus DP checks 8,495,284
  transitions, while its shortcut audit checks 561,568 oriented arcs. All
  112 rows have the unique predicted maximizer, and a formula-only tail check
  continues through \(n=1000\). This bounded computation enumerates neither
  subsets nor permutations and does not replace the symbolic proof.
- EXACT THEOREM (RESIDUE-ONE EXACT-THRESHOLD \(K\)): for
  \(n=5k+1\), \(k\ge2\), the order returned by
  `residue_one_product_distance_order(n)` has the unique maximizing subset
  \(\{2k+1,\ldots,n\}\) and exact value
  \[
  {857k^3+891k^2+214k
   +(k\bmod2)(27k^2-51k-18)\over24}.
  \]
  Its coefficient is \(857/3000\), exactly \(1/3000\) below the canonical
  \(143/500\). The exact pointwise difference is positive for every
  \(k\ge2\), so there is no crossover; parity changes only lower-order
  terms. Label-one elimination and the fixed-order sandwich yield only the
  fixed-order identities/inequalities and the residue-one subsequential
  global upper bounds, not an all-residue limsup improvement.
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260718__residue_one_exact_k/exact_diagnostic.py` imports no
  project helper. On \(2\le k\le30\), independent max-plus DPs check both
  fixed orders, every residue-one row has exactly one predicted maximizer,
  and all 234,030 oriented shortcut arcs pass. Direct formula and comparison
  checks continue through \(k=1000\). The computation enumerates neither
  subsets nor permutations and corroborates rather than replaces the all-
  \(k\) proof.
- EXACT THEOREM (RESIDUE-TWO EXACT-THRESHOLD \(K\)): for
  \(n=5k+2\), \(k\ge2\), the order returned by
  `residue_two_product_distance_order(n)` has the unique maximizing subset
  \(\{2k+1,\ldots,n\}\). With \(\varepsilon=k\bmod2\), its value is
  \[
  {286k^3+459k^2+198k+16
   +\varepsilon(-10k^2+40k+27)\over8}.
  \]
  It is strictly below K825 for every \(k\ge2\), without crossover, but the
  two cubic coefficients are both \(143/500\); their difference is
  \(21n^2/100+O(n)\). Exact label-one elimination and the fixed-order
  sandwich yield only the fixed-order identities, width-\(n^2\) bounds, and
  residue-two subsequential upper bounds; the unique core argmax also remains
  the unique complete-order \(\Lambda\)-maximizing subset after every
  insertion. This proves no global equality, angular ordering, active
  geometric/STN classification, or improved cubic coefficient.
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260718__residue_two_exact_k/exact_diagnostic.py` imports no
  project or test helper and independently reconstructs both block orders.
  On \(2\le k\le30\), its two increasing-path max-plus DPs each check
  4,623,615 transitions, every residue-two row has the sole predicted
  maximizer, and all 238,670 oriented shortcut arcs pass with minimum hole
  and path margins \(26\) and \(7\). Direct formula and K825 comparisons
  continue through \(k=1000\), with no crossover. This bounded exact
  computation enumerates neither subsets nor cyclic orders and does not
  replace the symbolic theorem.
- EXACT THEOREM: for \(n\ge9\), the terminal-high obstruction has the exact
  residue-class form
  \[
  H_n=
  \begin{cases}
  d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
  (d_n-1)^2/2,&n\equiv1\pmod5,\\
  (d_n-1)(d_n-2)/2,&n\equiv2\pmod5,\ n\ge17,
  \end{cases}
  \qquad H_{12}=56.
  \]
  The matching upper construction in residues zero, three, and four, together
  with separate search-free residue-one and residue-two constructions, gives
  \[
  B_n=W_n
  =
  \begin{cases}
  d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
  (d_n-1)^2/2,&n\equiv1\pmod5,\\
  d_n(d_n-2)/2,&n\equiv2\pmod5
  \end{cases}
  \qquad(n\ge9).
  \]
  The residue-one and residue-two branches start at \(n=11\) and \(n=12\),
  respectively.
- EXACT THEOREM: in residue two, put
  \(J_n=d_n(d_n-2)/2\). Saturation of all terminal-high incidences below
  \(J_n\), followed by the forced low--\((d_n-2)\)--low component, proves
  \[
  B_{12}\ge60=J_{12},
  \qquad
  B_n\ge J_n
  \quad(n\equiv2\pmod5,\ n\ge17).
  \]
  A symbolic order \(\sigma_n^{(2)}\), generated without search for every
  \(n=5k+2\), \(k\ge2\), satisfies
  \[
  W(\sigma_n^{(2)})=J_n.
  \]
  Therefore \(B_n=W_n=J_n\) at \(n=12\) and for every
  \(n\equiv2\pmod5\), \(n\ge17\). The proof treats permutation, adjacency,
  distances two and three, closing pairs, and distances at least four
  separately. It introduces no new geometric claim or asymptotic coefficient.
- EXACT THEOREM:
  \[
  \lim_{n\to\infty} A_n/n^2
  =1/4<2(\sqrt2-1)/3
  =\lim_{n\to\infty} L_n/n^2.
  \]
  The tail obstruction proves \(L_n>A_n\) for every \(n\ge33\).
- VERIFIED FACT (FINITE EXACT COMPUTATION): \(L_n\le A_n\) for
  \(4\le n\le32\), so \(33\) is the first index where the tail obstruction
  alone proves strictness of the adjacent relaxation.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): bounded canonical
  enumeration with integer/Fraction scoring gives
  \((W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50)\) and canonical
  minimizer counts \((1,1,1,2,2,4,12,72,24)\). This is not an all-`n`
  formula, a geometric certificate, or an exact geometric-optimum claim.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): for `n=3..11`,
  \[
  (W_3^{(\le1)},\dots,W_{11}^{(\le1)})
  =(6,12,15,20,24,30,35,42,48),
  \]
  and \(W_n^{(\le2)}=W_n\) in every case. The first non-adjacent gap is
  \(A_9=35<36=W_9\). The distance-two and full canonical minimizer sets also
  coincide throughout this bounded range.
- EXACT THEOREM (FINITE-EXHAUSTIVE PLUS SYMBOLIC): combining the preceding
  table with the exact residue-class formula for every \(n\ge9\) proves
  \[
  W_n^{(\le2)}=B_n=W_n\qquad(n\ge3).
  \]
  Hence distances at least three never change the optimum value.
- EXACT THEOREM: every pair omitted from the distance-two objective has score
  at most \(n(n-1)/3\). Combining this bound with the exact values of \(B_n\)
  proves
  \[
  \mathcal M_n=\mathcal M_n^{(\le2)}
  \qquad(3\le n\le92).
  \]
  At \(n=93\), the requested relocation of label \(54\) in
  \(\operatorname{eight\_twenty\_fifths\_order}(93)\) has
  \(W^{(\le2)}=2850=B_{93}\) and \(W=2852\), uniquely above \(B_{93}\)
  through the pair \((92,93)\) at distance three. Therefore
  \[
  \mathcal M_{93}\subsetneq\mathcal M_{93}^{(\le2)},
  \]
  and \(93\) is the first restriction index. No assertion is made that strict
  inclusion persists at every later index.
- EXACT THEOREM (ONE-TRIPLE REVERSAL OBSTRUCTION): for
  \(n=10m+3\), \(m\ge3\), put \(d=8m+4\),
  \(T=d(d-1)/2\), and reverse the outer entries of exactly one symbolic
  triple \(P_s\), \(0\le s\le m\). The resulting full-distance score is
  \[
  W(\tau_{m,s})=
  \begin{cases}
  (d^2-1)/2,&s=0,\\
  T,&1\le s\le m.
  \end{cases}
  \]
  Its adjacent maximum is always \(T\); its distance-two maximum is the
  displayed full score; its distance-three maximum is exactly
  \((5m+2)(9m+5)/3<T\);
  its distance-at-least-four maximum is \(n(n-1)/4<T\); and its three
  closing maxima are explicit and strict. Hence every choice \(s=s(m)\) has
  \(W/n^2\to8/25\). This is a family-specific surrogate obstruction, not a
  geometric lower bound or an exact geometric asymptotic statement.
- EXACT THEOREM (NONLOCAL ONE-GAP PATH-ROTATION OBSTRUCTION): on the same
  branch, keep the terminal/low scaffold and all path orientations fixed and
  assign \(P_{j+1\bmod2m}\) to terminal gap \(G_j\). The resulting
  \(\widehat\sigma_m\) is a permutation. Its exact distance-class maxima,
  each with one unordered maximizing pair, are
  \[
  M_1=T,\qquad
  M_2={n(d-1)\over2},\qquad
  M_3={(5m+2)(9m+4)\over3},\qquad
  M_{\ge4}={n(n-1)\over4}.
  \]
  The unique class maximizers are respectively
  \[
  \{d-1,4m+2\},\quad
  \{n,d-1\},\quad
  \{5m+2,9m+4\},\quad
  \{n-1,n\}.
  \]
  At the canonical cut,
  \[
  C_1=(4m+1)d,\quad
  C_2={d(d-2)\over2},\quad
  C_3={d^2\over6},\quad
  C_{\ge4}={T\over2},
  \]
  again with unique class maximizers. Hence
  \[
  W(\widehat\sigma_m)={n(d-1)\over2},
  \qquad
  {W(\widehat\sigma_m)\over n^2}\longrightarrow{2\over5}>{8\over25},
  \]
  and \(\{n,d-1\}\) is the only full-score saturating pair. The precise
  obstruction is the word \(n,2,d-1\) forced by moving \(P_0\) to the
  closing gap. No other reassignment is classified by this theorem, and its
  regular-direction implication is only a weaker existing upper bound.
- EXACT NECESSARY PLACEMENT THEOREM (DISTINGUISHED PATH): allow an arbitrary
  bijection assigning the unchanged oriented paths to the same terminal gaps.
  If \(P_0=(d-1,4m+2,d-2)\) occupies \(G_j\), then its exact local
  distance-class maxima are
  \[
  M^{\rm loc}_1(j)=T,
  \qquad
  M^{\rm loc}_2(j)=T+{j(d-1)\over2},
  \]
  uniquely on \(\{d-1,4m+2\}\) and \(\{E_j,d-1\}\). The right terminal
  distance-two score is \(T+[j(d-2)-2]/2\) for
  \(0\le j\le2m-2\), but becomes \(T-d/2\) at the cyclic closing gap.
  Therefore every global reassignment with \(W^{(\le2)}\le T\), and hence
  every one with \(W\le T\), must assign \(P_0\) to \(G_0\). Gaps
  \(G_1,\ldots,G_{2m-1}\) are locally excluded, while \(G_0\) is locally
  non-excluded but is not by itself a completion theorem. The known identity
  assignment is a separate witness; no nonidentity reassignment is asserted.
- VERIFIED FACT (FINITE EXACT LOCAL-GAP DIAGNOSTIC): the standalone
  standard-library script in
  `ops/TASK-20260717__p0_terminal_gap_classification/` scans only the gap
  indices at \(m=3,4,9,25\). It reconstructs the seven-label local word,
  verifies both exact maxima and the cyclic closure, and returns the sole
  locally non-excluded index \(j=0\) without constructing a complete order,
  assigning another path, or enumerating a path permutation. This bounded
  check corroborates but does not prove the all-\(m\) theorem.
- EXACT LOCAL RELATION THEOREM (GENERIC PATHS): retain the same arbitrary
  whole-path bijection, scaffold, and orientations. For a triple
  \(0\le k\le m\), the exact distance-two maximum caused by
  \(P_k\subset G_j\) is
  \[
  M^{\rm tr}_2(k,j)={(d+j)(d-1-2k)\over2}.
  \]
  Distance one is always safe, so the pair is locally non-excluded exactly
  when
  \[
  j(d-1-2k)\le2kd.
  \]
  Equivalently, its row consists of \(0\le j\le\ell_k\), with
  \[
  \ell_k=\min\!\left\{2m-1,
  \left\lfloor{2kd\over d-1-2k}\right\rfloor\right\},
  \]
  and its column form is
  \(k\ge\lceil j(d-1)/(2(d+j))\rceil\). Every singleton
  \(m+1\le k\le2m-1\) is strictly locally non-excluded in every gap; its
  exact distance-two maximum is \(x_k(d+j+1)/2\) off the cut and \(x_kn/2\)
  at closure. The last nonclosing and closing triple thresholds are
  \(\lfloor(4m+1)/5\rfloor\) and
  \(\lfloor(4m+3)/5\rfloor\), respectively.
- EXACT EDGE-EXTENDIBILITY THEOREM: in the Ferrers relation above, a local
  edge occurs in at least one relation-compatible bijection exactly when
  \[
  (k,j)=(0,0)
  \quad\text{or}\quad
  j\ge1.
  \]
  Equivalently,
  \[
  \mathcal R_{\rm ext}
  =\{(0,0)\}\cup
  \{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
  \]
  Residual Hall fails for every \((k,0)\), \(k>0\), because the remaining
  \(2m-1\) positive-index gaps have only \(2m-2\) available positive-index
  paths. For every positive-column local edge, a deterministic rotation of
  the interval between \(j\) and \(k\) supplies a compatible bijection. The
  three formulas for \(j<k\), \(j=k\), and \(j>k\) preserve \((0,0)\) and
  cover the triple/singleton crossing, terminal singleton, and cyclic closing
  column without wrapping the matching shift.
- EXACT ARBITRARY-BIJECTION FULL-SCORE THEOREM: for every path-to-gap
  bijection \(\alpha\), the six triple and four singleton distance-three
  forms, including all four path-type transitions and cyclic closure, give
  \[
  W^{(=3)}(\sigma_\alpha)
  \le {n(5m+2)\over3}<T.
  \]
  The bound is sharp exactly when \(P_m\) lies in \(G_{2m-2}\) or
  \(G_{2m-1}\); both placements occur in compatible PG46 shifts. Every pair
  at distance at least four has score at most \(n(n-1)/4<T\), while
  \(A_0c_0=T\). Hence
  \[
  W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha)
  \]
  for every bijection, and relation-compatibility is equivalent to
  \(W(\sigma_\alpha)=T=W_n\).
- EXACT FULL-OPTIMAL SUPPORT THEOREM: define \(\mathcal R_{\rm full}\) as the
  path/gap edges that occur in some scaffold bijection with full score \(T\).
  Then
  \[
  \mathcal R_{\rm full}=\mathcal R_{\rm ext}
  =\{(0,0)\}\cup
  \{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
  \]
  Thus the interval shifts are full-optimal witnesses, and every compatible
  bijection is full-optimal, although the bijections themselves are not
  enumerated. This is a surrogate theorem and gives no new geometric
  conclusion.
- EXACT FERRERS COUNT THEOREM: with
  \[
  \kappa_j=
  \left\lceil{j(8m+3)\over2(8m+4+j)}\right\rceil,
  \]
  the number of labelled relation-compatible bijections, equivalently all
  full-optimal bijections in the fixed scaffold, is
  \[
  \mathsf F_m^{\rm lab}
  =\prod_{j=1}^{2m-1}(j+1-\kappa_j).
  \]
  The nested-column recurrence computes the reduced PG49 permanent without
  permutation enumeration. The dual row product is
  \((m-1)!\prod_{k=1}^{m}(\ell_k-k+1)\). Every endpoint, transition, and
  inclusive-cutoff boundary is explicit, and \(\mathsf F_3^{\rm lab}=36\).
  No quotient by symmetries is used. Because each assignment has a distinct
  canonical representative rooted at \(n\) with neighbors \(2<3\), the same
  integer also counts the dihedral classes represented by this scaffold.
- EXACT FERRERS LOG-ASYMPTOTIC THEOREM: put
  \[
  C_{\rm F}=14\log2+6\log3-10\log5-2.
  \]
  Directly from the exact product, for every \(m\ge3\),
  \[
  1+\log{5\over6}-\log m
  <\log\mathsf F_m^{\rm lab}-(2m\log m+C_{\rm F}m)
  <{9\over4}+\log\bigl(2m(2m+1)\bigr).
  \]
  Hence
  \[
  \boxed{
  \log\mathsf F_m^{\rm lab}
  =2m\log m+C_{\rm F}m+{3\over4}\log m+O(1).
  }
  \]
  The coefficient \(3/4\) splits as \(-1/2+0+5/4\) from the exact
  factorial product, the smooth perturbation, and the lower-comparator
  rounding. A jump-inclusive sawtooth estimate controls the singular,
  intermediate, bulk, exact-cutoff, residue-class, and endpoint regions.
  The direct ceiling/no-ceiling correction is
  \(-\tfrac34\log m+O(1)\). The primary object is the labelled count;
  equality with the represented canonical image is only by prior
  injectivity. No convergence of the bounded remainder and no geometric
  statement is claimed.
- EXACT CLOSING-PG46 CORE-ORDER THEOREM: for the PG46 bijection placing
  \(P_m\) in \(G_{2m-1}\), the exact induced-subset argmax is the singleton
  family \(\{\{4m+1,\ldots,10m+3\}\}\), and

  \[
  K={572m^3+631m^2+223m+22\over2}.
  \]

  The exact canonical comparison is \(K-K_{825}=m^2-6m-4\). Hence the
  PG46 order is better exactly on \(m=3,4,5,6\), worse on \(m\ge7\), never
  tied, and retains coefficient \(143/500\). The theorem covers every block,
  shortcut, closure, and minimum-row boundary; it is not a geometric or
  global optimality result.
- EXACT PRECLOSING-PG46 CORE-ORDER THEOREM: for the other sharp PG46
  bijection, placing \(P_m\) in \(G_{2m-2}\), the exact induced-subset argmax
  is again the singleton family
  \(\{\{4m+1,\ldots,10m+3\}\}\), and

  \[
  K={572m^3+631m^2+235m+22\over2}.
  \]

  It exceeds the closing value by \(6m\) and K825 by \(m^2-4\), so it is
  strictly worse than both for every \(m\ge3\), with no parity, tie, or
  minimum-row exception. Both PG46 witnesses share cubic and quadratic
  coefficients; the preclosing one is worse by a linear term. The theorem
  covers every hole, shortcut, closure, and boundary but has no geometric or
  global-optimality consequence.
- EXACT DESCENDING-MIN PG49 THEOREM: fixing \(\alpha_{\min}(0)=0\) and,
  for \(j=2m-1,\ldots,1\), choosing the least unused
  \(k\ge\kappa_j\) is always well defined. The used suffix is exactly
  \([\kappa_j,\kappa_j+2m-1-j]\), so the result is a bijective,
  relation-compatible PG49 assignment for every \(m\ge3\). Its closed form
  is (PG104), with binary threshold jumps only.
- EXACT DESCENDING-MIN CORE-ORDER THEOREM: for the resulting core order,
  \[
  K=K_{825}+D_m+G_m,
  \]
  with the exact floor/positive-part terms in (KPGMIN-4)--(KPGMIN-8). If
  \(B_m=\{4m+1,\ldots,10m+3\}\), \(\mathcal P_m\) contains the positive-
  gain lows, and \(\mathcal Z_m\) the zero-gain lows, then every maximizer is
  exactly
  \[
  B_m\cup\mathcal P_m\cup Z',\qquad Z'\subseteq\mathcal Z_m,
  \]
  and there are \(2^{|\mathcal Z_m|}\). Universal uniqueness is false: the
  exact row \(m=101805057120180546870\) in (KPGMIN-19)--(KPGMIN-21) has a
  genuine zero-gain \(\lambda_j\). The value beats K825 and preclosing only
  at \(m=4\), never beats closing, and never ties. Its cubic coefficient is
  \(0.2881683105370884612\ldots>143/500\); the exact coefficient is
  transcendental, so no polynomial or eventual quasipolynomial formula
  exists. This is a combinatorial fixed-order theorem only.
- EXACT DESCENDING-MIN ZERO-GAIN CLASSIFICATION: the left and right equations
  defining \(\mathcal Z_m\) are classified separately by
  (KPGZERO-1)--(KPGZERO-23).  They have unique primitive \((g,u,w)\)
  parameters, one exact integrality congruence, four domain inequalities,
  distinct integral plateau residuals with every half-open endpoint audited,
  and explicit finite quadratic windows in \(g\).  Every admitted \(u/w\)
  is a regular convergent of the irreducible cubic root
  \(\xi\in(7/5,10/7)\) of \(50+51t-27t^2-24t^3\).  The prior giant left
  witness is reconstructed, and (KPGZERO-27)--(KPGZERO-30) give an exact
  primitive right witness.  Thus right holes exist.  Each fixed
  \(\mathcal Z_m\) is finite, but the cardinality of
  \(\bigcup_{m\ge3}\mathcal Z_m\) remains the explicit
  congruence-filtered one-sided-convergent obstruction (KPGZERO-24); no
  finite sweep settles it.  This has no geometric or global
  \(K\)-minimality consequence.
- EXACT EXPLICIT PG49-STAR THEOREM: put
  \(q=\lfloor(4m+3)/5\rfloor\) and use (PG110). Its five image blocks
  partition \(\{0,\ldots,2m-1\}\), every value passes its exact Ferrers
  threshold, and \(\alpha_*(2m-1)=q=\kappa_{2m-1}\). Thus it is a
  relation-compatible bijection for every \(m\ge3\). For the resulting core
  order,
  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
  =\bigl\{\{4m+1,\ldots,10m+3\}\bigr\},
  \]
  and
  \[
  K={1714m^3+1863m^2+24mq+617m+12q^2+48q+66\over6}.
  \]
  All low deletion gains are positive with exact minimum \(28m+12\), and
  every compressed shortcut is strict with exact minimum \(12m+4\). The
  five residue formulas have coefficient \(857/3000\) in \(n\). The value
  strictly improves K825 and both PG46 orders for every admitted row, with no
  tie. These are fixed-order combinatorial statements only.
- EXACT ODD-\(v\) PG49-STAR PARITY \(W\) THEOREM: on
  \(n=10m+8\), \(m\ge1\), put
  \(q=\lfloor(4m+5)/5\rfloor=\kappa_{2m}\) and use (PGODD-6). The five
  image blocks partition \(\{0,\ldots,2m\}\); all positive-column images
  pass the exact odd Ferrers thresholds; the residual Hall calculation gives
  the full odd PG49 support; and the genuine closing column holds at
  equality. The minimum row is \(\alpha^\circ=(0,2,1)\), including its
  doubleton and empty singleton range. The exact fixed-order score is
  \[
  W(\sigma_{\alpha^\circ})={(8m+8)(8m+7)\over2}.
  \]
  This is only a construction, compatibility, and product-distance theorem:
  \(K\), geometry, and global optimality are not evaluated.
- EXACT MONOTONE THRESHOLD-CLOSING PG46 THEOREM: put
  \(q=\lfloor(4m+3)/5\rfloor\) and specialize (PG46) to
  \((q,2m-1)\). The resulting assignment moves \(P_q\) to the closing gap
  and leaves every other path increasing. Its complete induced-subset
  classification is
  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
  =\bigl\{\{4m+1,\ldots,10m+3\}\bigr\},
  \]
  and
  \[
  K={572m^3+619m^2+8mq+207m+4q^2+16q+22\over2}.
  \]
  Seven exhaustive deletion-gain classes have unique minimum \(28m+12\),
  and every nontrivial compressed shortcut is positive with unique minimum
  \(12m+4\). The closing hole and retained \(b_q-L-E_0\) role are audited
  separately. All five residue formulas have coefficient \(143/500\) in
  \(n\). Exact subtraction gives
  \[
  K_\uparrow-K_*={m(m-1)(m-2)\over3},
  \]
  so reversal of the singleton block supplies exactly the entire cubic
  PG49-star improvement. The monotone order is below K825 and preclosing on
  every row, below closing for \(m\ge4\), and tied with closing only at
  \(m=3\). No angular, geometric, or global-minimizer conclusion follows.
- VERIFIED FACT (FINITE EXACT GENERIC-PATH DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260717__generic_path_terminal_gap_classification/ scans only
  the triples \((m,k,j)\) for \(m=3,4,9,34\). It compares every local
  distance-one and distance-two pair with both exact cutoff forms, including
  cyclic closure, the path-type transition, the complete \(m=3\) relation,
  and the nontrivial equality \((34,11,24)\). It constructs no complete
  order or bijection, imports no project/test helper, and enumerates no path
  permutation.
- VERIFIED FACT (FINITE EXACT EDGE-EXTENDIBILITY DIAGNOSTIC): the sole
  standalone standard-library script in
  ops/TASK-20260717__local_edge_extendibility_classification/ scans only the
  established local edges at \(m=3,4,9,34\). For every candidate it evaluates
  the residual Hall inequalities and directly constructs the prescribed
  interval shift, checking the target and every resulting Ferrers edge. It
  checks the deficient zero-column suffix and all stated boundaries without
  searching over matchings, enumerating path permutations, constructing a
  cyclic core order, or scoring a positional pair.
- VERIFIED FACT (FINITE EXACT FULL-SCORE DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260717__relation_compatible_full_score_classification/ scans the
  polynomial local state \((j,k,h)\) at \(m=3,4,9,34\), checks the complete
  distance-three lists, all four transition types, the literal compatible
  closure, the sharp equality placements, and exactly two PG46 full-order
  witnesses per row. It enumerates no path permutation or matching and
  imports no project or test helper.
- VERIFIED FACT (FINITE EXACT FERRERS-COUNT DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260718__ferrers_bijection_count/ builds the PG49 support directly
  from cross-multiplied integer inequalities for \(m=3,\ldots,8\). Ryser
  inclusion--exclusion over column subsets independently recovers the two
  Ferrers products and the exact counts
  \(36,720,21600,725760,46448640,3292047360\). It enumerates no path
  permutation or matching, constructs no core order, scores no positional
  pair, and imports no project or test helper.
- VERIFIED FACT (FINITE EXACT CLOSING-PG46 K DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260718__pg46_closing_exact_k/ reconstructs the specified core
  order and, for \(m=3,\ldots,30\), checks its score, unique optimizer with a
  max-plus increasing-path DP, all isolated-hole gains, and every oriented
  shortcut arc. Direct score/formula comparisons continue through \(m=1000\).
  It enumerates no subsets, permutations, or matchings and imports no project
  or test helper. This bounded check corroborates rather than proves the
  all-\(m\) theorem.
- VERIFIED FACT (FINITE EXACT PRECLOSING-PG46 K DIAGNOSTIC): the sole
  standalone standard-library script in
  ops/TASK-20260718__pg46_preclosing_exact_k/ reconstructs only the order
  placing \(P_m\) in \(G_{2m-2}\). For \(m=3,\ldots,30\), it checks the exact
  score, unique optimizer through an increasing-path max-plus DP, every
  isolated-hole gain, and every oriented shortcut arc. Direct score and
  comparison checks continue through \(m=1000\). It enumerates no subsets,
  permutations, or matchings and imports no project or test helper. This
  bounded check corroborates rather than proves the all-\(m\) theorem.
- VERIFIED FACT (FINITE EXACT DESCENDING-MIN PG49 K DIAGNOSTIC): the sole
  standalone standard-library script in
  ops/TASK-20260719__ferrers_greedy_exact_k/ checks the literal and closed
  assignments, suffix intervals, the one prescribed core, a max-plus
  increasing-path DP, and every oriented shortcut arc for
  \(m=3,\ldots,30\); exact formula and comparator checks continue through
  \(m=1000\). It enumerates no subset, permutation, or matching. Its
  zero-free statement is explicitly bounded and does not supersede the exact
  large counterexample.
- VERIFIED FACT (BOUNDED EXACT PG49 ZERO-GAIN DIAGNOSTIC): the sole
  standard-library script in
  ops/TASK-20260719__pg49_zero_gain_classification/ scans literal rows only
  through \(m=500\), a direct near-root denominator range only through
  \(10^5\), and finitely proposed convergents only through denominator
  \(10^{200}\) and \(g\le200\).  All accepted candidates are rechecked by
  exact integer parameter formulas, both literal ceilings, and the literal
  branch gain.  It reports 56 left and eight right parameter triples,
  including the two recorded witnesses.  The counts are bounded
  falsification evidence and imply neither finiteness nor infinitude.
- VERIFIED FACT (FINITE EXACT PG49-STAR K DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260719__explicit_pg49_star_exact_k/ constructs only (PG110).
  For \(m=3,\ldots,30\), a direct increasing-path max-plus DP checks the
  score, unique backbone, every isolated-hole gain, and all 958,916 proper
  oriented arcs, including every nontrivial shortcut and cyclic closure.
  Ferrers, formula, and comparator checks continue through \(m=1000\). It
  enumerates no subset, path permutation, or matching. This bounded
  computation corroborates rather than proves the all-\(m\) theorem.
- VERIFIED FACT (BOUNDED EXACT ODD-\(v\) PG49-STAR \(W\) DIAGNOSTIC): the
  sole standalone integer script in
  ops/TASK-20260719__pg49_star_parity_w/ constructs only (PGODD-6).
  Formula, image, and threshold checks cover \(m=1,\ldots,1000\); literal
  local-word and residual-Hall checks cover \(m=1,\ldots,40\); and exact
  all-pairs cyclic scoring covers \(m=1,\ldots,80\). It checks 8,906,280
  unordered cyclic pairs without enumerating an order family, matching, path
  permutation, or subset. The computation corroborates rather than proves
  the all-\(m\) theorem.
- VERIFIED FACT (FINITE EXACT MONOTONE THRESHOLD-CLOSING K DIAGNOSTIC): the
  sole standalone standard-library script in
  ops/TASK-20260719__pg46_threshold_closing_exact_k/ constructs only
  \(\alpha_{q,2m-1}\). On \(m=3,\ldots,30\), its increasing-path max-plus
  DP checks the exact score and unique backbone, while a direct audit checks
  all 958,916 proper oriented arcs, including every nontrivial shortcut and
  cyclic-cut arc. It performs 36,989,498 max-plus transitions. Ferrers,
  residue, inversion-delta, formula, and comparator checks continue through
  \(m=1000\). It enumerates no subset, path permutation, matching, or order
  family. The bounded computation corroborates rather than proves the
  symbolic theorem.
- VERIFIED FACT (FINITE EXACT FORMULA EVALUATION):
  \((Q_3,\dots,Q_{11})=(6,12,12,20,21,30,63/2,42,45)\). In this bounded table
  \(\max(A_n,Q_n)=A_n\); this does not affect the strictly improved
  asymptotic lower coefficient for \(B_n\).
- VERIFIED FACT (FINITE EXACT FORMULA EVALUATION):
  \[
  (H_3,\dots,H_{11})=(6,12,15,20,21,30,36,45,50).
  \]
  Combined with the existing finite exhaustive distance-two table,
  \(\max(A_n,H_n)=B_n\) for every displayed \(3\le n\le11\). This is not an
  all-\(n\) formula and uses no order enumeration beyond \(n=11\).
- EXACT THEOREM: within the single-subset induced-tail plus duplicated-pairing plus
  \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\) relaxation, no nonconsecutive subset
  improves the tail bounds \(P_{m,n}\); the best discrete tail is characterized
  by \(\rho_n=(\sqrt{8n^2+8n+1}-(2n+1))/2\), with adjacent ties exactly when
  \(\rho_n\) is an integer.
- VERIFIED FACT (WORKFLOW CONFIGURATION): checked-artifact verification is
  wired into local review and `.github/workflows/verification.yml`.
- LOCAL VERIFIED FACT: successful local tests, checked-artifact verification,
  workflow inspection, and hygiene checks are recorded in
  `ops/TASK-20260712__verification_trust_layer_ci/` and
  `ops/TASK-20260712__cross_platform_finite_hash_ci/`; these are not hosted-run
  results.
- HISTORICAL USER-REPORTED STATUS: the 2026-07-12 roadmap task recorded a green
  hosted run after the cross-platform fix, but no commit SHA, run identifier,
  URL, or independently inspected result was recorded; it establishes no
  hosted status for a specific commit.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.
- INTERPRETATION: these are finite certificates only; they are not exact optimum proofs, all-`n` theorems, or asymptotic results.
- INTERPRETATION: the all-`n` theorems and regular-direction constructions are
  independent of the finite certificates; the upper and lower leading
  coefficients do not currently match.
- INTERPRETATION: the coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal for the
  documented single-subset relaxation. The exact consecutive-tail block
  extension has the same leading coefficient for every fixed length and for
  every \(r=o(n)\). This method-specific result is not a proved exact
  asymptotic coefficient for Power-Ringmin. Joint optimization of the
  one-prefix linear block \(m=1\), \(r_n=\lfloor\alpha n\rfloor\), yields
  \(\alpha_*=1-\sqrt3/3\), a positive certified cubic residual, and the
  global lower coefficient \((4+2\sqrt3)/(27\pi)\). Its total
  coefficient \((4+2\sqrt3)/27\) is optimal only inside the one-prefix
  specialization of CR28ax--CR28bg; the
  associated residual contribution is \((26-15\sqrt3)/54\), not a separately
  optimized residual. The globally optimized two-prefix CR28bw template
  further raises the lower coefficient to
  \[
  {491596+6578\sqrt{143}\over2061723\pi}.
  \]
  The globally optimized three-prefix template raises it further to
  \[
  {753972193324+106042322\sqrt{377823}
   \over2960667770787\pi}.
  \]
  The globally optimized four-prefix template raises it again to
  \[
  {597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403\pi}.
  \]
  The fixed rational five-prefix witness at \(\alpha=13/30\) first improves
  the established lower coefficient to
  \[
  {2263404122555368590593580404287
   \over8177706222298165502582585481000\pi}.
  \]
  The globally optimized five-prefix template raises its fixed-\(k=5\)
  optimum further to
  \[
  {346693217780244687187063490332457027500975566238012204
   +1228130489996268437333105902690103574002
    \sqrt{183342238504950468196395903}
   \over1312688475479610714750859896048564873968757997852345827\pi}.
  \]
  Finally, applying the independent normalized optimizer and charging theorem
  at every fixed finite \(k\), then taking the supremum of the resulting
  scalar inequalities, raises the current lower coefficient to
  \[
  {434+4\sqrt2\over1587\pi}.
  \]
  The full clipped Bellman classification proves separately that the scalar
  numerator is the exact unattained supremum of the complete continuous
  finite-prefix template family and that every finite-\(k\) maximizer is
  uniquely strict all-middle. The charging step uses no \(k=k(n)\), uniform
  threshold, or interchange of limits; the five-prefix surd remains the exact
  optimum of its template.
  All four irrational multi-prefix optimizers are exact and unique in their
  respective templates. The older rational witness remains the finite two-prefix theorem
  from \(n=59\); the irrational three-prefix optimizer now has the stronger
  finite theorem \(\Lambda_n>C_{3,*}n^3\) from the minimal uniform threshold
  \(159\). The fixed rational five-prefix witness has its own exact finite
  theorem from the minimal uniform threshold \(234\), while the irrational
  global five-prefix point has no finite rounding theorem. None of these
  coefficients is an exact
  residual or leading coefficient; convergence, finite rounding at the
  irrational two-, four-, and five-prefix optimizers, and exact block
  residuals remain unresolved.
- LIMITATION: the interval-backend trust/provenance limitation remains explicit
  and unresolved for public production claims. The bounded test-only Arb
  cross-check covers checked `n=3` only and is not a full backend audit.
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))\).
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)\).
