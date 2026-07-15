# Next Research Steps

This roadmap synthesizes the checked `n=3..6` certificates, candidate-set
diagnostics, critical-structure analysis, checked-artifact verification tooling
and workflow configuration, the induced-subset all-\(n\) lower bound, and the
exact eventual radius-one insertion theorem, the regular-direction baseline
and zigzag cubic upper bound, the exact bounded product-distance surrogate
analysis through `n=11`, the matching all-\(n\) symbolic surrogate
constructions, and the global classification
\(W_n^{(\le2)}=B_n=W_n\) for every \(n\ge3\).
It also records the exact first minimizer-set restriction:
\(\mathcal M_n=\mathcal M_n^{(\le2)}\) for \(3\le n\le92\), while
\(\mathcal M_{93}\subsetneq\mathcal M_{93}^{(\le2)}\).
The fixed-order certification debt is now closed mathematically by
`research/FIXED_ORDER_ANGULAR_STN.md`, which proves exact angular/STN
equivalence, the negative-cycle criterion, potential recovery, radius
dependence, and half-open bracket semantics while preserving the guarded
`mpmath.iv` trust boundary.
A bounded independent test-only path now also cross-checks the checked `n=3`
record with 384-bit Arb through python-flint. It recomputes every required
theta and `2*pi`, all three lower-cycle edges, and all three upper-witness
pairs without the production oracle. This corroborates one finite record and
does not change the guarded production contract or any certified claim.
The complete fixed-order maximum cyclic ratio is now formalized separately in
`research/FIXED_ORDER_CYCLE_RATIO.md`. Its exact global relation
\[
0<\Lambda_n-\pi R_2^*(n)<\pi n^2
\]
makes \(\Lambda_n/\pi\), for \(n\ge3\), an additive-\(n^2\) combinatorial approximation to
the geometric infimum, while proving neither a new exact constant nor
convergence. Exact canonical enumeration is deliberately bounded to
`n=3..8` and gives \((12,26,47,77,118,172)\).
The one-wrap saturation question is also closed exactly. If
\[
\Lambda^{(1)}(\sigma)=\max\{S(C):q(C)=1\},
\]
then \(\Lambda^{(1)}(\sigma)\) is the maximum cyclic adjacent-product sum
over orders induced on subsets of at least two positions, equivalently over
all nonempty subsets when a singleton has cyclic sum \(i^2\), and
\[
\Lambda(\sigma)=\Lambda^{(1)}(\sigma)
\]
for every complete order and every \(n\ge3\). This all-order theorem makes
the scores integers. A test-only subset/path oracle, independent of the
production Karp scorer, verifies the equality on all 2,956 canonical orders
for `n=3..8` without changing the production bound. The finite regression is
not the proof of the theorem and produces no new geometric or asymptotic
claim.

The index-one reduction is now also closed exactly. For a core order
\(\tau\), let
\[
K(\tau)=
\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U).
\]
If \(\tau\) is obtained from a complete order \(\sigma\) by deleting label
\(1\), the singleton \(\{1\}\), the pairs \(\{1,j\}\), and the subsets in
which \(1\) has two distinct core neighbors give the exact theorem
\[
\Lambda(\sigma)=K(\tau),
\qquad
\Lambda_n=\min_\tau K(\tau).
\]
The result is independent of the insertion gap of \(1\). Applying the
accepted same-order comparison to the core gives
\[
\Lambda_n\le(n-1)W_n,
\qquad
R_2^*(n)<{\Lambda_n\over\pi}
\le{(n-1)W_n\over\pi}
\qquad(n\ge3).
\]
This route recovers the upper coefficient \(8/(25\pi)\) without using the
radius-one insertion theorem; it does not prove convergence, equality, or
common minimizing orders. An exact test-only sweep covers all 437 canonical
core orders and 2,957 insertion gaps through `n=8`, representing the same
2,956 complete classes. The duplicate is the explicit two-arc `n=3` case.

The reduced formulation has now yielded one exact value beyond the public
enumeration boundary, without moving that boundary. For
\(S_6=\{4,\ldots,9\}\) and \(S_5=\{5,\ldots,9\}\), a finite hand-checkable
lemma proves
\[
\max\{P_\omega(S_6),P_\omega(S_5)\}\ge239
\]
for every cyclic order \(\omega\) on \(S_6\). Therefore every core order has
\(K(\tau)\ge239\). The explicit witness
\(\tau=(9,2,3,5,8,6,7,4)\) has \(K(\tau)=239\), with the unique maximizing
subset \(S_6\), so
\[
\Lambda_9=239.
\]
The equality conditions and a shortcut-gain certificate now give the full
finite classification. Up to dihedral symmetry the induced six-cycle is
forced to be \(\Omega=(9,5,8,6,7,4)\). Label \(3\) occupies exactly one of
the four gaps not incident to label \(4\), and label \(2\) then occupies any
of the seven resulting gaps. Hence there are exactly 28 dihedral core
minimizers. Exact label-one elimination/insertion gives exactly 224 complete
minimizer classes. All core minimizers maximize on \(S_6\); 27 do so
uniquely, while `(9,4,7,6,8,3,2,5)` also maximizes on the full core.
This is an **EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION)**.

An independent test-only oracle directly checks all
\(7!/2=2{,}520\) dihedral core classes and all 255 nonempty subsets of each,
recording every maximizing subset and recovering exactly the proved 28
classes. It calls neither a repository canonicalizer, the public enumerator,
nor the production scorer. The public complete-order domain remains
`n<=8`. No exact value of \(R_2^*(9)\), all-\(n\) formula, geometric
classification, or asymptotic claim follows.

The same reduced method now gives the next exact value without changing
production. A finite pairing lemma proves
\[
\max\{P_\omega(\{4,\ldots,10\}),P_\omega(\{5,\ldots,10\})\}\ge323
\]
for every cycle on \(\{4,\ldots,10\}\). Its human-checkable proof starts at
the duplicated-pairing baseline 320, classifies exactly the eight signatures
at the only relevant values 320--322, and checks the label-four insertion
correction in the sole cyclic signature. The exact shortcut-gain certificate
for \((10,2,3,4,7,8,6,9,5)\) attains 323, so
\[
\Lambda_{10}=323.
\]
Equality in the seven-label lemma is now classified structurally. Separating
tail scores 322 and 323 and applying exact label-four corrections plus
fixed-edge residual pairing bounds and the residual equality-signature
recurrence leave exactly the two dihedral classes represented by
`(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`. Independent
test-only arithmetic confirms this proved list over all 360 lemma classes and
checks all 511 nonempty witness subsets without a repository canonicalizer,
public enumerator, or production scorer.

The label-three and label-two insertion steps over these classes are also
closed. The label-three correction and complete shortcut-gain certificates
leave eleven partial cycles at \(K_{\ge3}=323\). Their 88 label-two
insertions form 88 distinct dihedral core classes. The exact variation
\(2(a+b)-ab=4-(a-2)(b-2)\), the recorded partial argmaxes, and the pruning
certificates prove that exactly 87 have \(K=323\); the sole exception is
`(10,3,2,4,7,8,6,9,5)`, with score 325. Only after this proof, exact
label-one insertion gives 783 complete dihedral minimizer classes. Separate
literal oracles check all 14-by-255 label-three cases and all 88-by-511
label-two cases, including every argmax and the dihedral counts. The public
domain remains `n<=8`.

As of 2026-07-14, the former asymptotic target
\[
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))
\]
is a DISPROVED CLAIM. The stronger former target
\[
R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)
\]
is also a DISPROVED CLAIM.

The best leading coefficient obtainable from the specific relaxation
"induced subset plus duplicated-multiset pairing plus
\(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\)" is exactly
\[
\frac{2(\sqrt2-1)}{3\pi}.
\]
This is a method-specific optimality statement, not a matching upper bound and
not a proved exact asymptotic constant for Power-Ringmin.

The zigzag regular-direction construction historically improved the proved
upper coefficient from \(1/\pi\) to \(1/(2\pi)\). It is now superseded by the
product-distance construction below, which gives \(8/(25\pi)\). Neither upper
bound matches the induced-subset geometric lower coefficient. The zigzag
theorem itself generated no leading-order LP, new finite certificate, `n=7`
certificate, preflight artifact, permutation optimization, or exhaustive
enumeration.

The product-distance surrogate now optimizes the regular-direction sufficient
radius combinatorially. Exact canonical enumeration, deliberately bounded to
`n=3..11`, gives
\[
(W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50).
\]
This finite exact result improves on zigzag for every enumerated `n=6..11`,
but the finite table alone is not an all-`n` formula or a geometric
certificate. A separate symbolic theorem now supplies explicit orders for
every \(n\ge9\): with
\[
d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T_n={d_n(d_n-1)\over2},
\]
the constructed order \(\sigma_n\) satisfies
\(W(\sigma_n)\le T_n\). Consequently
\[
{B_n\over n^2}\longrightarrow{8\over25},
\qquad
{W_n\over n^2}\longrightarrow{8\over25},
\qquad
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le {8\over25\pi}.
\]

The adjacent relaxation is now fully characterized. If
\[
A_n=\min_\sigma\max_k\sigma_k\sigma_{k+1},
\]
then \(A_3=6\) and
\[
A_n=
\left(\left\lfloor{n\over2}\right\rfloor+1\right)
\left(\left\lceil{n\over2}\right\rceil+2\right)
\qquad(n\ge4).
\]
The existing `patterns.interleave` constructor realizes the formula for all
\(n\). Equality cycles are also characterized exactly: even cycles have the
single forced high-high edge \(\{t+1,t+2\}\), while odd cycles have the
forced segment \(t+2,t+1,t+3\); removing it leaves an alternating active
high path in both cases. The comparison with the tail obstruction is strict
asymptotically:
\[
\lim_{n\to\infty} {A_n\over n^2}={1\over4}
< {2(\sqrt2-1)\over3}
=\lim_{n\to\infty} {L_n\over n^2}.
\]
In fact, the explicit tail \(m=\lceil2n/5\rceil\) proves \(L_n>A_n\) for
every \(n\ge33\), while exact rational formula evaluation gives
\(L_n\le A_n\) through \(n=32\).

Writing \(B_n=W_n^{(\le2)}\), the equality structure gives the exact theorem
\[
B_n=A_n\quad(3\le n\le8),
\qquad
B_n>A_n\quad(n\ge9).
\]
The proof uses terminal-high incidences and a separate degree obstruction at
`n=12`, with no cyclic-order enumeration beyond `n=11`. Consequently
\(W_n>A_n\) for every \(n\ge9\). The bounded exact table gives
\(B_n=W_n\) for `n=3..11`, while the residue-class theorem below gives the
same equality for every \(n\ge9\). Since the two domains cover every
\(n\ge3\),
\[
W_n^{(\le2)}=B_n=W_n\qquad(n\ge3).
\]
Thus distances at least three never change the optimum value. The bounded
table is no longer the endpoint of the minimizer-set result: the universal
omitted-pair bound \(ij/q\le n(n-1)/3\), combined with the exact residue
formula, proves equality of the distance-two and full minimizer sets through
\(n=92\). The requested moved-label order at \(n=93\) has truncated score
\(2850\) and full score \(2852\), so \(93\) is the first strict-inclusion
index.

A separate two-threshold cyclic packing theorem now gives a quantitative
lower obstruction for \(B_n\). The graph of compatible products \(xy\le2T\)
on the first exact tail has nested prefix neighborhoods, and its exact cyclic
incompatibility is \(\eta_n(T)=\max(0,2v-u+\delta_n(T))\), where
\(\delta_n(T)=\mathbf1_{\{a_T<b_T\le n-1,\ 2T<b_T^2-1\}}\) is the
skip-one correction, with the tail notation defined in
`research/PRODUCT_DISTANCE_SURROGATE.md`. Inverting
\(n-1\ge2u+\eta_n(T)\) yields a finite
half-integer bound \(Q_n\le B_n\), and for every \(n\ge9\),
\[
B_n\ge Q_n\ge
{36-16\sqrt2\over49}\left(n+{1\over2}\right)^2.
\]
Therefore
\[
\liminf_{n\to\infty}{B_n\over n^2}
\ge {36-16\sqrt2\over49}>{1\over4}.
\]
The inversion satisfies
\(Q_n=((36-16\sqrt2)/49)n^2+O(n)\). Thus the exact graph theorem improves
some finite thresholds but proves that the clique coefficient is already
optimal for this tail-cycle subproblem.
A further terminal-high compatible-low incidence theorem applies at every
exact threshold and gives \(2v\le C_n(T)\). Keeping \(Q_n\) unchanged, its
combination with \(\Psi_n(T)\le n-1\) defines \(H_n\), with
\[
B_n\ge H_n\ge Q_n,
\qquad
H_n={8\over25}n^2+O(n),
\qquad
\liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}.
\]
The coefficient \(8/25\) follows from matching all-\(n\) inequalities and is
not inferred from the bounded table. Combined with the explicit upper
construction, it is now the exact leading coefficient of both \(B_n\) and
\(W_n\). The full-distance tail obstruction \(L_n\le W_n\) remains logically
separate and is not redefined or transferred by this theorem.

The residue-class roadmap is now sharper. For every \(n\ge9\), with
\(d_n=\lceil(4n+8)/5\rceil\), the exact obstruction is

\[
H_n=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
(d_n-1)(d_n-2)/2,&n\equiv2\pmod5,\ n\ge17,
\end{cases}
\qquad H_{12}=56.
\]

The uniform upper construction attains this value in residues zero, three,
and four. Separate search-free orders attain the residue-one value for every
\(n=5k+1\), \(k\ge2\), and the sharper residue-two value
\[
J_n={d_n(d_n-2)\over2}.
\]
A saturation obstruction proves
\[
B_{12}\ge60=J_{12},
\qquad
B_n\ge J_n
\quad(n\equiv2\pmod5,\ n\ge17),
\]
while a parity-aware order \(\sigma_n^{(2)}\), valid for every
\(n=5k+2\), \(k\ge2\), satisfies \(W(\sigma_n^{(2)})=J_n\). Therefore
\[
B_n=W_n=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
d_n(d_n-2)/2,&n\equiv2\pmod5
\end{cases}
\qquad(n\ge9).
\]
The former residue-one and residue-two widths now measure only slack in the
superseded uniform order; they are not objective gaps. Together with the
bounded exact table, this proves the displayed global distance-two
saturation for every \(n\ge3\).

## Evidence Basis

- COMPUTER-CERTIFIED RESULT: checked finite interval certificates exist for
  `n=3,4,5,6` under the documented local interval-verifier semantics and
  guarded `mpmath.iv` backend contract.
- EXACT THEOREM (ABSTRACT ENCLOSURE IMPLICATION):
  `research/FIXED_ORDER_ANGULAR_STN.md` proves that fixed-order
  all-pairs geometry is equivalent to the implemented difference constraints,
  an STN is feasible exactly when it has no negative directed cycle, and
  shortest-path distances recover a feasible potential. It also proves that
  \(\theta_R\) is continuous and strictly decreasing in \(R\). Given genuine
  enclosures, a strict lower cycle and closed upper witness give
  \(\rho_\sigma\in(L_\sigma,U_\sigma]\). Finite exhaustive order coverage
  yields the same half-open global semantics.
- CONDITIONAL COMPUTER-CERTIFIED RESULT: applying these implications to
  checked artifacts is conditional on the documented guarded `mpmath.iv`
  enclosure contract.
- EXACT THEOREM: `research/FIXED_ORDER_CYCLE_RATIO.md` defines
  \(q(C)\), \(S(C)\), and
  \(\Lambda(\sigma)=\max_C S(C)/q(C)\), with edge multiplicity and two-cycles
  included. Every cycle has \(q(C)\ge1\), and
  \[
  {\Lambda(\sigma)\over\pi}-n^2
  <\rho_\sigma
  <{\Lambda(\sigma)\over\pi}.
  \]
  Minimizing over complete orders gives, for \(n\ge3\), the analogous global
  inequalities and \(0<\Lambda_n-\pi R_2^*(n)<\pi n^2\). Consequently normalized limit points
  transfer after the factor \(\pi\), but existence of a limit does not.
- EXACT THEOREM: the same note defines
  \(\Lambda^{(1)}(\sigma)=\max_{q(C)=1}S(C)\), writes
  \(P_\sigma(T)\) for the induced cyclic product sum, and proves
  \[
  \Lambda(\sigma)=\Lambda^{(1)}(\sigma)
  =
  \max_{\substack{T\subseteq\{0,\dots,n-1\}\\|T|\ge2}}
  \sum_r\sigma_{i_r}\sigma_{i_{r+1\bmod |T|}}
  =\max_{T\ne\varnothing}P_\sigma(T),
  \]
  where \(i_0<\cdots<i_{|T|-1}\), singleton cyclic sums are squares, and
  cardinality two counts the product twice. The proof is all-order: the
  complete induced cycle has score at
  least \(n(n+1)(n+2)/6\), while every vertex-simple cycle with \(q\ge2\)
  has ratio at most half of \(\sum_{i=1}^n i^2\), smaller by
  \(n(n+1)/4\). Thus \(\Lambda(\sigma)\) and \(\Lambda_n\) are integers.
- EXACT THEOREM: deleting label \(1\) from \(\sigma\) gives a core order
  \(\tau\) for which
  \[
  \Lambda(\sigma)=K(\tau),
  \qquad
  K(\tau)=
  \max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U).
  \]
  The proof treats \(\{1\}\), \(\{1,j\}\), and subsets with two distinct
  core neighbors \(a,b\) of \(1\); in the last case deletion raises the score
  by \(ab-a-b\ge1\). Thus the score is independent of the insertion gap,
  \(\Lambda_n=\min_\tau K(\tau)\), and the same-order comparison gives
  \[
  \Lambda_n\le(n-1)W_n,
  \qquad
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{(n-1)W_n\over\pi}.
  \]
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a descending-path/Karp
  `Fraction` scorer, independently checked by direct simple-cycle enumeration
  on every canonical order through `n=6`, gives
  \((\Lambda_3,\dots,\Lambda_8)=(12,26,47,77,118,172)\) over all 2,956
  canonical complete orders. The production enumerator hard-rejects `n>8`.
  This finite result is neither a closed-form evaluation of the reduced
  minimum nor a geometric certificate.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a separate exact
  subset/path dynamic program and literal induced-subset oracle agree with one
  another and with production on all 2,956 canonical complete orders for
  `n=3..8`. Neither oracle uses the production descending closure, macro
  graph, or Karp recurrence; the production domain and ceiling remain
  unchanged. This verifies the bounded implementation, not the all-order
  proof.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): every one of the 437
  canonical core orders and all 2,957 cyclic insertion gaps for `n=3..8`
  satisfy \(\Lambda(\sigma)=K(\tau)\) under both literal subset scoring and
  the production scorer. These trials cover all 2,956 complete classes. Core
  minimizer counts are `(1,1,1,3,4,12)` and complete minimizer counts are
  `(1,3,4,15,24,84)`. At `n=3`, the two insertions into
  \(\tau=(3,2)\) are reflections and give the same canonical complete class.
- EXACT THEOREM (FINITE SIX-LABEL LEMMA): for every cyclic order \(\omega\)
  on \(S_6=\{4,\ldots,9\}\), with \(S_5=\{5,\ldots,9\}\),
  \[
  \max\{P_\omega(S_6),P_\omega(S_5)\}\ge239.
  \]
  The proof starts from the exact rearrangement bound
  \(P_\omega(S_5)\ge235\), uses
  the insertion identity
  \(P_\omega(S_6)-P_\omega(S_5)=16-(a-4)(b-4)\) for the two neighbors
  \(a,b\) of label four, and checks only the exceptional pairs \(\{7,9\}\) and
  \(\{8,9\}\) by twelve displayed integer sums.
- VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT): the six-label lemma and
  the exact shortcut-gain certificate for
  \(\tau=(9,2,3,5,8,6,7,4)\) prove \(\Lambda_9=239\) through the accepted
  reduction. The sole maximizing witness subset is
  \(\{4,5,6,7,8,9\}\). An independent test-only oracle checks all 60
  six-label dihedral classes, while a separate literal computation checks all
  255 nonempty witness subsets and records their maxima by cardinality.
  Production enumeration remains hard-bounded to `n<=8`.
- EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION): equality in the lemma
  uniquely fixes the induced \(S_6\) cycle up to dihedral symmetry. In the
  orientation \((9,5,8,6,7,4)\), label \(3\) may occupy exactly the four gaps
  not incident to label \(4\), and label \(2\) may then occupy every one of
  the seven resulting gaps. These \(4\cdot7=28\) classes are all and only the
  core orders with \(K=239\). Exact insertion of label \(1\) gives
  \(28\cdot8=224\) complete minimizer classes. Exactly one core class,
  canonically `(9,4,7,6,8,3,2,5)`, has the full core as a second argmax
  beside \(S_6\).
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a direct test-local
  generator covers all \(7!/2=2{,}520\) \(n=9\) core dihedral classes and
  literally evaluates all 255 nonempty subsets of each, recording every
  argmax. It recovers minimum 239, exactly 28 minimizers, and the proved
  \(27+1\) argmax pattern without calling a repository canonicalizer, public
  enumerator, or production Karp scorer. This is 2,520 **core** classes, not
  an extension of the public complete-order domain beyond `n=8`.
- EXACT THEOREM (FINITE SEVEN-LABEL LEMMA): for every cyclic order on
  \(\{4,\ldots,10\}\),
  \[
  \max\{P_\omega(\{4,\ldots,10\}),
        P_\omega(\{5,\ldots,10\})\}\ge323.
  \]
  The pairing relaxation on the duplicated multiset of labels 5 through 10
  has baseline 320. The exact least-entry recurrence has one, three, and four
  terminal signatures at values 320, 321, and 322; only one 322 signature is
  a simple cycle, and all six insertions of label four add at least one.
- EXACT THEOREM (FINITE SEVEN-LABEL EQUALITY CLASSIFICATION): the only
  dihedral equality classes are represented by `(10,4,7,8,6,9,5)` and
  `(10,5,9,4,7,8,6)`, with tail scores 323 and 322, respectively. The proof
  handles those branches separately. In the tail-323 branch, exact correction
  signs leave four candidate insertion edges; fixed-edge pairing floors and
  their unique residual equality signatures leave only \(\{7,10\}\). This
  proof uses no sweep over cyclic orders.
- EXACT THEOREM (FINITE LABEL-THREE INSERTION-GAP CLASSIFICATION): for the
  partial induced-subset score \(K_{\ge3}\) on labels \(3,\ldots,10\), the
  first equality cycle has value 326 on \(\{4,7\}\) and 323 on every other
  gap. The second has value 326 on \(\{4,9\}\), 328 on \(\{4,7\}\), and
  323 on every other gap. The proof uses the exact insertion formula and a
  complete shortcut-gain certificate and records every maximizing subset.
- EXACT THEOREM (FINITE `n=10` CORE MINIMIZER CLASSIFICATION): the eleven
  surviving partial cycles and their eight label-two gaps give 88 distinct
  dihedral core classes. Exactly 87 have \(K=323\); the sole exception is
  `(10,3,2,4,7,8,6,9,5)`, with \(K=325\). The proof uses
  \(2(a+b)-ab=4-(a-2)(b-2)\), the exact constrained argmaxes inherited from
  the shortcut certificates, and a separate dihedral-equivalence argument.
  Exact label-one elimination/insertion gives 783 complete dihedral minimizer
  classes. Every core and complete argmax is classified.
- VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT): the shortcut-gain table
  for \(\tau=(10,2,3,4,7,8,6,9,5)\) proves \(K(\tau)=323\), with exactly
  \(\{5,\ldots,10\}\) and \(\{3,\ldots,10\}\) maximizing. Hence the
  accepted reduction gives \(\Lambda_{10}=323\).
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): direct test-local
  generation confirms the proved equality list over all \(6!/2=360\) lemma
  classes, independently audits the low-pairing and fixed-edge correction
  data, and checks all 511 nonempty witness subsets. Separate literal oracles
  check the 14 label-three insertions and all 3,570 corresponding subset
  scores, then the 88 label-two insertions and all 44,968 corresponding
  subset scores, independently of the proof certificates. Test-local
  dihedral keys recover 88 core candidate classes and 783 complete minimizer
  classes. These paths call no repository canonicalizer, public enumerator,
  or production scorer.
- EXACT THEOREM: `research/ALL_N_LOWER_BOUND.md` proves the induced-subset
  lower-bound theorem. In particular, for every `n>=4` and `1<=m<=n-2`,
  \[
  R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
  \qquad
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  \frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
  \]
- EXACT THEOREM: choosing \(m=\lceil(\sqrt2-1)n\rceil\) gives
  \[
  R_2^*(n)
  \ge
  \frac{2(\sqrt2-1)}{3\pi}n^3-O(n^2),
  \]
  and hence
  \[
  \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
  \ge
  4(\sqrt2-1)>1.
  \]
- EXACT THEOREM: for \(S=\{s_1<\cdots<s_q\}\), the duplicated-multiset pairing
  bound is
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+1-a}
  \quad(q=2t),
  \]
  and
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+2-a}+s_{t+1}^2
  \quad(q=2t+1).
  \]
  At fixed \(q\), this is uniquely maximized by the tail
  \(\{n-q+1,\dots,n\}\), so nonconsecutive subsets do not improve this
  relaxation.
- EXACT THEOREM: the discrete maximizers of \(P_{m,n}\) over
  \(1\le m\le n-2\) are characterized by
  \[
  \rho_n=\frac{\sqrt{8n^2+8n+1}-(2n+1)}2.
  \]
  For \(n\ge4\), the unique maximizer is \(\lfloor\rho_n\rfloor+1\) unless
  \(\rho_n\) is an integer, in which case the two maximizers are
  \(\rho_n\) and \(\rho_n+1\).
- EXACT THEOREM: writing \(R^*_{2:n}\) for the infimum central radius of the
  core radii \(2^2,\dots,n^2\),
  \[
  R_2^*(n)=R^*_{2:n}\qquad(n\ge12).
  \]
  The proof uses the exact forbidden-arc insertion criterion
  \(\sum_{j=2}^n\theta_R(1,j^2)<\pi\), rigorous angular majorants, and the
  configuration-level induced-subset lower bound. It proves equality of the
  full and core feasible-radius sets and does not assume a minimizer.
- EXACT THEOREM: for every \(n\ge12\), `research/ALL_N_LOWER_BOUND.md` proves
  the order-independent baseline in which the core uses regular
  \((n-1)\)-gon polar directions and is all-pairs feasible at
  \[
  U_n
  =
  \sqrt{
  n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
  +{(2n-1)^2\over4}}
  -{n^2+(n-1)^2\over2}.
  \]
  The accepted insertion theorem gives \(R_2^*(n)\le U_n\) for \(n\ge12\),
  with \(U_n/n^3\to1/\pi\).
- EXACT THEOREM: for every \(R>0\) and positive \(i,j\),
  \(\theta_R(i^2,j^2)<2ij/R\). For
  \[
  M_n=n\left(\left\lfloor{n\over2}\right\rfloor+1\right),
  \qquad
  V_n={(n-1)M_n\over\pi},
  \]
  the core indices in zigzag order \((n,2,n-1,3,\dots)\) satisfy
  \(ij\le qM_n\) at circular distance \(q\). Thus all core pairs are feasible
  at \(V_n\), the insertion theorem gives \(R_2^*(n)\le V_n\) for \(n\ge12\),
  and
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {1\over2\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
- EXACT THEOREM: `research/PRODUCT_DISTANCE_SURROGATE.md` defines
  \(W(\sigma)=\max ij/d_\sigma(i,j)\), proves strict all-pairs core
  feasibility at \((n-1)W(\sigma)/\pi\), transfers it to the full problem for
  `n>=12`, and proves the tail obstruction
  \[
  W(\sigma)\ge {P_{m,n}\over n-1}
  \qquad(2\le m\le n-2)
  \]
  using induced oriented positional gaps that sum to `n-1`.
- EXACT THEOREM: for every \(n\ge9\), the same note gives an explicit cyclic
  core order \(\sigma_n\) satisfying
  \[
  W(\sigma_n)\le
  T_n={d_n(d_n-1)\over2},
  \qquad
  d_n=\left\lceil{4n+8\over5}\right\rceil.
  \]
  The symbolic family covers all but 14 stated base cases; those cases use
  explicit exact orders. Separate all-\(n\) arguments control adjacent pairs,
  positional distances two and three, closing pairs, and automatic distances
  at least four. Together with \(H_n\le B_n\le W_n\), this proves
  \(B_n/n^2\to8/25\) and \(W_n/n^2\to8/25\). The regular-direction majorant
  and radius-one insertion theorem then give the geometric upper coefficient
  \(8/(25\pi)\), without asserting a matching geometric lower bound.
- EXACT THEOREM: in residue one, write \(n=5k+1\), \(k\ge2\), and
  \(D=d_n-1=4k+2\). A separate explicit order, generated without search, has
  \[
  W(\sigma_n^{(1)})={D^2\over2}=H_n.
  \]
  Its proof controls adjacent pairs, positional distances two and three, all
  pairs crossing the displayed cut, and distances at least four separately.
  Consequently \(B_n=W_n=H_n\) in residue one. Canonical factorial
  enumeration remains bounded to \(n\le11\).
- EXACT THEOREM: in residue two, every hypothetical threshold
  \(H_n\le T<J_n=d_n(d_n-2)/2\) saturates the injection of the \(2v\)
  terminal-high incidences into the compatible lows. The component containing
  \(d_n-2\) is then low--\((d_n-2)\)--low, and its two distinct terminal
  extensions would both have to carry the label \(d_n-1\), a contradiction.
  The exceptional case uses the exact interval \(56=H_{12}\le T<60=J_{12}\).
  Therefore
  \[
  B_{12}\ge60,
  \qquad
  B_n\ge J_n\quad(n\equiv2\pmod5,\ n\ge17),
  \]
  A separate parity-aware symbolic order, valid for every \(n=5k+2\),
  \(k\ge2\), has score exactly \(J_n\). Its proof separately checks
  permutation, adjacency, positional distances two and three, all closing
  pairs, and distances at least four using
  \(4J_n-n(n-1)=7k^2+33k+14>0\). Thus \(B_n=W_n=J_n\) at \(n=12\) and
  throughout residue two from \(n=17\), completing the exact residue-class
  formula without extending canonical enumeration.
- EXACT THEOREM: the same note proves the adjacent formula for \(A_n\) by a
  high/low internal-edge count and an explicit all-`n` cycle whose edges have
  endpoint sums at most \(n+3\); source inspection identifies that cycle with
  `patterns.interleave`.
- EXACT THEOREM: the equality cases force one high-high edge for even `n` and
  the two-edge high segment for odd `n`, with no low-low edges. The resulting
  active high path and a terminal-high incidence count prove
  \(B_n=A_n\) exactly for `3<=n<=8` and \(B_n>A_n\) for every `n>=9`; the
  exceptional incidence parameter `n=12` is covered by a separate exact
  four-degree argument.
- EXACT THEOREM: the exact two-threshold tail graph has nested neighborhoods
  and cyclic incompatibility
  \(\eta_n(T)=\max(0,2v-u+\delta_n(T))\). The resulting packing obstruction
  \(n-1\ge2u+\eta_n(T)\) has a finite half-integer inversion \(Q_n\) that
  lower-bounds \(B_n\), proves the explicit quadratic bound and liminf
  coefficient strictly above \(1/4\), and satisfies
  \(Q_n=((36-16\sqrt2)/49)n^2+O(n)\).
- EXACT THEOREM: every order with distance-two score at most \(T\) satisfies
  \(2v\le C_n(T)\), with
  \[
  C_n(T)=\max\left(0,\left\lfloor{T\over b_T}\right\rfloor-1\right).
  \]
  The joint finite obstruction \(H_n\) preserves \(Q_n\) and combines this
  incidence condition with \(\Psi_n(T)\le n-1\). It satisfies
  \(B_n\ge H_n\ge Q_n\) and
  \[
  H_n={8\over25}n^2+O(n),
  \qquad
  \liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}.
  \]
  The proof includes all strict/non-strict boundaries and degenerate tails;
  By itself it gives no matching upper bound and no statement about \(L_n\) or
  the geometric optimum; the separate explicit construction supplies the
  matching upper coefficient for \(B_n\) and \(W_n\).
- EXACT THEOREM: \(A_n/n^2\to1/4\), while
  \(L_n/n^2\to2(\sqrt2-1)/3\). A residue-class proof with
  \(m=\lceil2n/5\rceil\) gives \(L_n>A_n\) for every \(n\ge33\).
- VERIFIED FACT (FINITE EXACT COMPUTATION): exact rational tail-formula
  evaluation gives \(L_n\le A_n\) for `n=4..32`; this is not cyclic-order
  enumeration.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): exact canonical
  enumeration of `204557` rotation/reflection classes for `n=3..11` gives
  the displayed \(W_n\) values and minimizer counts
  \((1,1,1,2,2,4,12,72,24)\), with representatives and comparisons recorded
  in `research/PRODUCT_DISTANCE_SURROGATE.md`. No floating point, serialized
  artifact, schema, CLI, or geometric certificate is involved.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): for `n=3..11`, the
  distance-one objectives are
  \((6,12,15,20,24,30,35,42,48)\), while every distance-two objective,
  minimizer count, and minimizer set equals its full-surrogate counterpart.
  The first adjacent/full gap is at `n=9`.
- EXACT THEOREM (FINITE-EXHAUSTIVE PLUS SYMBOLIC): the preceding bounded
  equality and the residue-class formula on `n>=9` cover every `n>=3` and
  prove
  \(W_n^{(\le2)}=B_n=W_n\). For every integer \(q\ge2\), monotonicity also
  gives \(W_n^{(\le q)}=W_n\).
- EXACT THEOREM: every omitted pair has score at most \(n(n-1)/3\). Exact
  residue arithmetic proves
  \(\mathcal M_n=\mathcal M_n^{(\le2)}\) for \(3\le n\le92\). At \(n=93\),
  relocating label \(54\) from between \(4,3\) to between \(16,48\) in
  \(\operatorname{eight\_twenty\_fifths\_order}(93)\) gives
  \(W^{(\le2)}=2850=B_{93}\) but \(W=2852\), attained by \((92,93)\) at
  distance three. Thus \(93\) is the first minimizer-restriction index, with
  no enumeration beyond \(n=11\) and no geometric conclusion.
- VERIFIED FACT: `examples/finite_results_summary_n3_n6.json` derives
  candidate sets, exclusion gaps, repeated serialized bracket groups, and
  small-`n` ratios from the checked finite certificates.
- VERIFIED FACT: `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json`
  records deterministic critical-structure diagnostics for certified candidate
  orders only.
- LOCAL VERIFIED FACT: successful local tests, checked-artifact verification,
  workflow inspection, and hygiene checks are recorded in
  `ops/TASK-20260712__verification_trust_layer_ci/` and
  `ops/TASK-20260712__cross_platform_finite_hash_ci/`; they do not establish
  hosted GitHub Actions status.
- HISTORICAL USER-REPORTED STATUS: the 2026-07-12 roadmap task recorded a green
  hosted run after the cross-platform fix, but no commit SHA, run identifier,
  URL, or independently inspected result was recorded; it establishes no
  hosted status for a specific commit.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.
- LIMITATION: none of the finite certificates proves an exact optimum,
  coefficient-matching upper bound, or leading-term asymptotic formula; the
  new asymptotic conclusions instead come from separate all-\(n\) theorems.

## Consequences

1. The induced-subset lower bound supersedes the older full-cycle lower bound
   \(\liminf 6\pi R_2^*(n)/n^3\ge 1\). The older statement remains true but is
   no longer sharp enough to describe the current obstruction.

2. Any future asymptotic upper-bound target must be compatible with
   \[
   \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
   \ge
   4(\sqrt2-1)>1.
   \]
   This roadmap deliberately does not propose a new exact constant.

3. The proof uses induced cyclic orders on subsets, not only adjacent pairs in
   the full cyclic order. For any subset \(S\) of at least three indices, the
   induced gaps sum to \(2\pi\), all-pairs feasibility applies to each induced
   adjacent endpoint pair, and the duplicated-multiset pairing lemma supplies
   the product lower bound.

4. The finite tests added with the proof are diagnostic checks only: they
   verify the formula for \(P_{m,n}\), the explicit formula for \(A(S)\), the
   fixed-cardinality optimality of tails by exhaustive small-`n` subset
   enumeration, the integer characterization of the discrete maximizers, the
   zigzag product lemma on a substantial finite interval, and sampled
   geometric all-pairs feasibility. They are not the all-\(n\) proofs.

5. The former reduced-core observation now has an exact eventual consequence:
   for \(n\ge12\), adding radius \(1\) does not change any feasible central
   radius. This does not validate the finite lower-cycle proxy as an exact
   contact graph, does not settle \(n\le11\), and is not based on the checked
   cases \(n=5,6\).

6. The symbolic product-distance construction supersedes zigzag and gives the
   rigorous liminf/limsup bracket
   \[
   {2(\sqrt2-1)\over3\pi}
   \le
   \liminf_{n\to\infty}{R_2^*(n)\over n^3}
   \le
   \limsup_{n\to\infty}{R_2^*(n)\over n^3}
   \le {8\over25\pi}.
   \]
   The upper value is a limsup coefficient, not an exact leading constant; the
   construction does not prove convergence.

7. The product-distance surrogate isolates exactly what the angular majorant
   needs from a regular-direction order. The explicit \(T_n\) family proves
   the exact leading coefficient \(8/25\) for both \(B_n\) and \(W_n\).
   Matching constructions now determine their exact values in every residue
   class for \(n\ge9\); in residue two the value is
   \(B_n=W_n=J_n=d_n(d_n-2)/2\). Combined with the exact bounded table, this
   proves \(W_n^{(\le2)}=B_n=W_n\) for every \(n\ge3\). Global structural
   classifications of minimizers remain open, but their first long-distance
   restriction is now exact: the sets agree through \(n=92\) and differ at
   \(n=93\). Any geometric matching coefficient remains open. The best tail
   obstruction remains strict in all enumerated cases where it is defined.

8. The adjacent relaxation by itself has coefficient \(1/4\), strictly below
   both the earlier two-threshold coefficient \((36-16\sqrt2)/49\) and the
   stronger terminal-high incidence coefficient \(8/25\). Distance-two
   constraints leave it exact through `n=8`, make it strict for every
   `n>=9`, and obey the stronger explicit lower bound. The nested tail-cycle
   subproblem still has coefficient \((36-16\sqrt2)/49\), while the added
   incidence constraint raises the combined necessary coefficient to
   \(8/25\), and the explicit order families match it from above. This settles
   the leading coefficients and every residue class exactly for \(n\ge9\).
   The residue-two saturation argument raises the lower endpoint from \(H_n\)
   to \(J_n\), and the separate symbolic order attains that endpoint.

9. The full fixed-order cyclic ratio is one-wrap saturated for every complete
   order. This replaces a possible finite pattern by an exact theorem and
   explains why the bounded `Fraction` outputs have denominator one. It does
   not reduce exact angular-STN feasibility to one-wrap cycles: those weights
   contain nonlinear \(\theta_R\) terms rather than only the separable
   products used by \(\Lambda\). Exact elimination of label \(1\) further
   reduces \(\Lambda_n\) to \(\min_\tau K(\tau)\) and proves
   \(\Lambda_n\le(n-1)W_n\). The reduction by itself is not a closed-form
   all-\(n\) evaluation or a general minimizer classification, although the
   additional finite equality/shortcut argument now classifies all \(n=9\)
   core \(K\)-minimizers and a separate pairing/shortcut argument proves the
   value \(\Lambda_{10}=323\) and exactly classifies equality in its
   seven-label lemma. The subsequent exact insertion analyses classify labels
   `3` and `2`, prove that 87 of the 88 forced candidates are precisely the
   dihedral core minimizers, and derive 783 complete minimizer classes only
   after that proof. Insertion independence for
   \(\Lambda\) does not transfer to the exact angular threshold. The resulting
   geometric upper bound recovers the known coefficient \(8/(25\pi)\); it
   proves no exact geometric optimum or new coefficient.

## Updated Research Questions

- OPEN QUESTION: what geometric upper-bound construction, if any, narrows or
  matches the induced-subset lower coefficient up to lower-order terms?
- OPEN QUESTION: can the previous reduced-core observations at checked
  `n=5,6` be related to the exact feasible-radius-set equality for
  \(n\ge12\), or are their lower-cycle proxies a separate finite phenomenon?
- OPEN QUESTION: is \(12\) the least threshold for
  \(R_2^*(n)=R^*_{2:n}\), or can the remaining \(n\le11\) cases be settled by
  stronger exact estimates or counterexamples?
- OPEN QUESTION: can the gap between the induced-subset geometric lower
  coefficient and the product-distance upper coefficient \(8/(25\pi)\) be
  narrowed by a sharper angular construction or a stronger lower bound?
- OPEN QUESTION: for which \(n\ge94\) do positional distances at least three
  strictly restrict the minimizer set? The sufficient equality criterion
  \(n(n-1)/3\le B_n\) holds again at \(n=94\), so no persistence from the
  first strict index onward is asserted.
- CLOSED QUESTION: the fixed-order STN/geometric equivalence, endpoint
  semantics, and negative-cycle proof obligations are now recorded
  independently of every asymptotic claim in
  `research/FIXED_ORDER_ANGULAR_STN.md`.
- CLOSED QUESTION: the complete fixed-order cyclic ratio, its exact
  fixed/global sandwich, endpoint strictness, exact scorer, and bounded
  `n=3..8` prediction are recorded in
  `research/FIXED_ORDER_CYCLE_RATIO.md`. The one-wrap induced-subset
  equivalence, all-order saturation, exact index-one elimination,
  core-minimum reduction, and one-sided comparison with \(W_n\) are also
  closed there, with separate Karp-independent and all-insertion bounded
  oracles. Their distinction from exact angular-STN cycle criticality and
  their asymptotic non-consequences remain explicit.
- CLOSED FINITE QUESTION: the first reduced value beyond the public
  cyclic-ratio enumeration boundary is \(\Lambda_9=239\). All minimizing
  core orders are exactly the 28 placement classes recorded in
  `research/FIXED_ORDER_CYCLE_RATIO.md`, and exact label-one insertion gives
  224 complete minimizer classes. The independent 2,520-core oracle records
  every argmax and recovers the same classification. This closes only the
  specified finite combinatorial case, not any geometric or all-\(n\) case.
- CLOSED FINITE VALUE AND CORE CLASSIFICATION: the next reduced value is
  \(\Lambda_{10}=323\), proved by the seven-label pairing lemma and exact
  witness shortcut certificate in `research/FIXED_ORDER_CYCLE_RATIO.md` and
  independently checked on 360 lemma classes and 511 witness subsets. A
  separate structural branch proof now establishes exactly the two
  seven-label equality cycles. Exact insertion and shortcut certificates
  classify all label-three gaps over them, leaving eleven partial cycles with
  \(K_{\ge3}=323\). Exact label-two variation and constrained shortcut
  certificates then classify 87 core minimizer classes and one score-325
  exception among their 88 gaps; only afterward, label-one insertion gives
  783 complete classes. Independent 14-by-255 and 88-by-511 oracles confirm
  every score, argmax, and dihedral count.

## Ranked Work

Completed:

- Documented and proved fixed-order angular/STN equivalence and certificate
  endpoint semantics, including monotonicity and continuity in `R`,
  negative-cycle infeasibility, feasible-potential recovery, upper-witness
  meaning, and the interval-backend trust boundary.
- Formalized the complete fixed-order maximum cyclic ratio, proved the exact
  additive-\(n^2\) fixed/global sandwich, implemented the independent exact
  scorer, and bounded its canonical enumeration to `n=3..8`.
- Proved exact one-wrap saturation for every complete order, identified the
  one-wrap score with induced-subset cyclic product sums, and verified the
  bounded property using a test-only exact oracle independent of production
  Karp scoring, without enlarging the production enumeration domain.
- Proved exact elimination of label \(1\), reduced
  \(\Lambda_n\) to \(\min_\tau K(\tau)\), derived
  \(\Lambda_n\le(n-1)W_n\) and its all-\(n\) geometric upper bound, and
  checked every canonical core order and insertion gap through `n=8` without
  changing production limits or certification claims.
- Proved the finite exact value \(\Lambda_9=239\) from a hand-checkable
  six-label lower-bound lemma and an exact core witness, then independently
  checked the 60 six-label cyclic classes and all 255 witness subsets without
  changing the public `n<=8` enumerator.
- Classified all 28 dihedral \(n=9\) core minimizers through the equality
  conditions and a shortcut-gain placement proof, derived the 224 complete
  minimizer classes by exact label-one insertion, and independently checked
  all 2,520 core classes and their maximizing subsets without changing the
  public `n<=8` enumerator.
- Proved the finite exact value \(\Lambda_{10}=323\) from a human-checkable
  pairing classification at levels 320--322 and an exact shortcut-gain
  witness, then independently checked all 360 lemma classes and all 511
  witness subsets without changing production or classifying all core
  minimizers.
- Classified structurally the two and only two seven-label equality cycles at
  `n=10` by separating tail scores 322 and 323, auditing exact label-four
  corrections, and using fixed-edge residual pairing bounds; retained the
  360-class sweep solely as an independent test oracle.
- Classified all 14 insertions of label `3` over those two equality cycles by
  the exact insertion formula and complete shortcut-gain certificates. The
  first cycle excludes only \(\{4,7\}\); the second excludes exactly
  \(\{4,9\}\) and \(\{4,7\}\); every other partial score is 323. A separate
  literal oracle checks all 3,570 induced subsets and every argmax without
  production code.
- Classified all 88 label-two insertions over the eleven surviving partial
  cycles by the exact variation and constrained shortcut-gain certificates.
  Exactly 87 are the distinct dihedral core minimizers; the sole exception
  has score 325. Derived 783 complete classes only after the proof and checked
  all 44,968 core subset scores, every argmax, and the dihedral counts with an
  independent test-only oracle.
- Implemented the first bounded independent interval-backend cross-check:
  checked `n=3` is recomputed directly with 384-bit Arb through python-flint,
  with exact coverage of one record, three lower-cycle edges, three witness
  pairs, and six slacks, while production verification and claims remain
  unchanged.

Immediate:

- In a fresh bounded task, extend the independent test-only Arb endpoint-sign
  cross-check from the checked `n=3` artifact to the existing checked `n=4`
  artifact, without changing production verification or certification claims.

Next:

- Seek a geometric all-pairs construction or lower obstruction that narrows
  the remaining coefficient gap without relying on larger exhaustive finite
  certificates.
- Keep the exact radius-one theorem separate from finite critical-cycle proxy
  claims and from any assumption that an optimum is attained.

Later:

- Reduce bracket widths or add independent fixed-order analysis for the
  multiple candidates at `n=5,6` if exact tie questions become important.
- Consider larger finite certificates only after a structural prediction gives
  a precise discriminator.
- Revisit whether the sufficient radius-one threshold can be lowered below
  \(12\), using exact inequalities or a genuine counterexample rather than
  finite-certificate extrapolation.

Deliberately deferred:

- `n=7` exhaustive certificate generation.
- Larger exhaustive enumeration without a precise discriminator.
- Product-distance enumeration beyond the explicit `n=11` boundary.
- Public/production fixed-order cyclic-ratio enumeration beyond the explicit
  `n=8` complete-order boundary.
- Leading-order LP work in the induced-subset proof task.
- Any claim that \(8/(25\pi)\) is the exact geometric asymptotic constant.
- Any claim that the radius-one threshold \(12\) is minimal.

## Recommended Next Atomic Task

Task: extend the independent test-only Arb endpoint-sign cross-check to the
existing checked `n=4` interval certificate.

Acceptance criteria:

- read the checked `n=4` artifact directly and account for every embedded
  local bracket, lower-cycle edge occurrence, upper-witness pair, and
  directional slack;
- recompute the decisive endpoint signs with fixed high-precision Arb
  arithmetic independently of the production interval oracle and its stored
  enclosures;
- record exact coverage and deterministic test evidence, with optional
  python-flint absence handled consistently with the existing `n=3` test;
- make no production-backend, artifact, bracket, schema, classification, or
  certification-claim change.
