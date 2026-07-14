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

## Ranked Work

Completed:

- Documented and proved fixed-order angular/STN equivalence and certificate
  endpoint semantics, including monotonicity and continuity in `R`,
  negative-cycle infeasibility, feasible-potential recovery, upper-witness
  meaning, and the interval-backend trust boundary.

Immediate:

- Design an independent interval-backend cross-verification path for the
  existing checked artifacts before making public production-grade certificate
  claims.

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
- Leading-order LP work in the induced-subset proof task.
- Any claim that \(8/(25\pi)\) is the exact geometric asymptotic constant.
- Any claim that the radius-one threshold \(12\) is minimal.

## Recommended Next Atomic Task

Task: design an independent interval-backend cross-verification path for the
existing checked finite artifacts.

Acceptance criteria:

- choose one independently implemented outward-enclosure backend or a small
  exact rational enclosure pipeline for the operations actually required;
- specify how every existing local cycle and witness would be recomputed
  without trusting the current `mpmath.iv` path;
- keep generator, verifier, and artifact provenance roles separate;
- begin with a bounded checked fixture and explicit platform/version
  requirements;
- do not generate a larger-\(n\) certificate or change any current certified
  claim during the design task.
