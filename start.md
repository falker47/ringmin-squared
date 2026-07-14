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

The quadratic-radii computational foundation has been implemented. Checked finite interval certificate artifacts currently exist for `n=3,4,5,6`; they provide finite global radius brackets under the documented guarded `mpmath.iv` interval-backend contract.

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
This is a geometric upper coefficient, not an exact geometric asymptotic
constant.
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
and \(H_{12}=56\). Combining this formula with the construction proves
\[
B_n=W_n={d_n(d_n-1)\over2}
\qquad(n\ge9,\ n\equiv0,3,4\pmod5).
\]
In residues one and two, the exact widths from \(H_n\) to the uniform theorem
threshold \(T_n\) are \((2n+3)/5\) and \((4n+7)/5\), respectively, with
width \(10\) at \(n=12\). These are bound widths, not asserted optimality
gaps. This residue analysis proposes no replacement construction and proves
no all-\(n\) exact formula, or new value beyond the bounded \(n\le11\) table,
in those two classes.
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
values of \(B_n\) and \(W_n\) are now known in residue classes zero, three,
and four; beyond the bounded table they remain unresolved in classes one and
two.

Consequently the former target
\(R_2^*(n)=n^3/(6\pi)(1+o(1))\) is a disproved claim. The stronger target
\(R_2^*(n)=n^3/(6\pi)+O(n^2)\) is also a disproved claim.

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
leading-term asymptotic formula, and an upper bound matching the induced-subset
lower coefficient remain unresolved. Current exact bounds give
\[
\frac{2(\sqrt2-1)}{3\pi}
\le
\liminf_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le
\limsup_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le\frac8{25\pi}.
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

## Current Knowledge Status

- COMPUTER-CERTIFIED RESULT: checked finite global interval brackets exist for `n=3,4,5,6` under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` backend contract.
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
  product-distance construction below improves the current upper coefficient.
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
  The geometric statement is an upper bound only.
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
  Hence the matching upper construction gives
  \[
  B_n=W_n={d_n(d_n-1)\over2}
  \qquad(n\ge9,\ n\equiv0,3,4\pmod5).
  \]
  The exact widths to the uniform threshold \(T_n\) in the unresolved
  classes are \((2n+3)/5\) for residue one and \((4n+7)/5\) for residue two
  from \(n=17\), with width \(10\) at \(n=12\). These are not asserted
  optimality gaps.
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
  \(A_9=35<36=W_9\). Equality of the distance-two and full objectives beyond
  `n=11` is not claimed.
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
- EXACT THEOREM: within the induced-subset plus duplicated-pairing plus
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
  documented relaxation only; it is not a proved exact asymptotic coefficient
  for Power-Ringmin.
- LIMITATION: the interval-backend trust/provenance limitation remains explicit and unresolved for public production claims.
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))\).
- DISPROVED CLAIM: \(R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)\).
