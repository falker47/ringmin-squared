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
  threshold tails \(U_T,V_T\) and cyclic gap packing give a finite
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
- **VERIFIED FACT (finite exhaustive exact computation):** the table below
  gives the objectives truncated at positional distances at most one and two,
  as well as \(W_n\), for \(3\le n\le11\). Non-adjacent constraints first
  change the optimum at \(n=9\), while distance-two constraints already
  recover \(W_n\) throughout this bounded range. This is not an all-\(n\)
  theorem, a geometric certificate, or a claim of exact geometric optimality.
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

This conclusion is purely combinatorial. It does not give a formula for
\(B_n\) or \(W_n\), does not show that \(B_n=W_n\) beyond the bounded table,
and does not by itself improve a geometric radius bound for Power-Ringmin.

## Quantitative Two-Threshold Obstruction For \(B_n\)

The preceding strictness theorem compares \(B_n\) with \(A_n\), but gives no
size for the gap. We now prove an independent quantitative obstruction using
only positional distances one and two.

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

### Cyclic gap lemma

Let \(S_2(\sigma)=W^{(\le2)}(\sigma)\). Suppose that a cyclic core order
\(\sigma\) satisfies

\[
S_2(\sigma)\le T
\tag{TT5}
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
\tag{TT6}
\]

Every distinct pair in \(U_T\) has product greater than \(T\). Therefore
\(g_i=1\) would give a distance-one score greater than \(T\), contradicting
(TT5). Hence every \(g_i\ge2\).

If both endpoints of a gap lie in \(V_T\), their product is greater than
\(2T\). If that gap were at most two, their smaller circular distance would
also be at most two and their score would be at least their product divided
by two, again greater than \(T\). Thus a \(V_T\)-to-\(V_T\) induced gap is
at least three.

It remains to count how many such gaps are forced. Mark the \(v\) positions
of the cyclic \(U_T\)-word that belong to \(V_T\), and let \(e_{VV}\) be
the number of cyclic marked-marked adjacencies, counting the two directed
cyclic gaps separately when \(u=2\). If \(e_{V\bar V}\) is the number of
mixed adjacencies, incidence counting gives

\[
2v=2e_{VV}+e_{V\bar V},
\qquad
e_{V\bar V}\le2(u-v).
\]

Consequently

\[
e_{VV}\ge\max(0,2v-u).
\tag{TT7}
\]

This is the exact minimum. If \(v\le u-v\), place at least one unmarked
position between consecutive marked positions and obtain no marked-marked
adjacency. If \(v>u-v\), isolate every unmarked position between marked
positions; the remaining marked runs have exactly
\(v-(u-v)=2v-u\) marked-marked cyclic edges.

Using the baseline cost two for every induced gap and one additional position
for each marked-marked gap, (TT6)--(TT7) prove the candidate lemma:

\[
\boxed{
n-1\ge2u+\max(0,2v-u)
}
\qquad(u\ge2).
\tag{TT8}
\]

There is no exceptional small cycle hidden in this proof. For \(u=2\), the
two induced oriented gaps still sum to \(N\), and if both positions are
marked, (TT7) correctly counts both gaps as marked-marked.

Define

\[
\Phi_n(T)=2u+\max(0,2v-u)=\max(2u,u+2v).
\tag{TT9}
\]

The degenerate cases extend the necessary inequality to every \(u\): for
\(u=0\), both sides contributed by the tails are zero; for \(u=1\), the
result above gives \(v=0\), so \(\Phi_n(T)=2\le n-1\). Therefore

\[
S_2(\sigma)\le T
\quad\Longrightarrow\quad
n-1\ge\Phi_n(T)
\tag{TT10}
\]

for every \(n\ge3\) and every exact \(T\ge0\). Equivalently, the exact
finite condition \(\Phi_n(T)>n-1\) certifies \(B_n>T\).

### Finite exact obstruction

Every distance-at-most-two pair score has denominator one or two. Hence
\(B_n\in\tfrac12\mathbb Z_{\ge0}\). Define

\[
Q_n
=
\min\left\{
{q\over2}:q\in\mathbb Z_{\ge0},\quad
\Phi_n(q/2)\le n-1
\right\}.
\tag{TT11}
\]

This set is nonempty: at \(T=n(n-1)\), one has \(u=1,v=0\). Moreover the
minimum is a genuinely finite calculation. The tails change only when
\(T=k(k+1)\) or \(2T=k(k+1)\), and strictness makes the change occur at
the equality itself. Thus (TT11) is equivalently the minimum over

\[
E_n
=
\{0\}\cup
\left\{
{k(k+1)\over2},\ k(k+1):2\le k\le n-1
\right\}.
\tag{TT12}
\]

The finite order space attains \(B_n\). Applying (TT10) at \(T=B_n\) shows
that \(B_n\) belongs to the admissible half-integer set in (TT11), so

\[
\boxed{B_n\ge Q_n},
\qquad
\boxed{B_n\ge\max(A_n,Q_n)}.
\tag{TT13}
\]

The implementation functions `two_threshold_tail_packing` and
`two_threshold_lower_obstruction` evaluate (TT1)--(TT4), (TT9), and
(TT11)--(TT12) with integers and `Fraction` only.

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
\tag{TT14}
\]

Put \(T=Q_n\), \(a=a_T\), and \(b=b_T\). The upper bound in (TT14) gives
\(a\le n-1\) and \(b\le n\), so \(u=n-a+1\ge2\) and
\(v=n-b+1\ge1\). Since \(\Phi_n(Q_n)\le n-1\), (TT9) yields both
\(2u\le n-1\) and \(u+2v\le n-1\). In particular,

\[
a\ge{n+3\over2}>2,
\qquad
a+2b\ge2n+4.
\tag{TT15}
\]

Minimality in (TT1)--(TT2), now with valid predecessors at least two, gives

\[
(a-1)a\le Q_n,
\qquad
(b-1)b\le2Q_n.
\]

Hence \(a\le1+\sqrt{Q_n}\) and
\(b\le1+\sqrt{2Q_n}\). Combining these estimates with (TT15),

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
asymptotic constant is slightly larger than the new distance-two constant:

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
\(n\ge33\). This tail argument does not decide the full values \(W_n\) for
\(12\le n\le32\); the independent distance-two theorem (DT9)--(DT10) now
proves strictness throughout that interval without determining those values.

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

The exact comparison table is below. The \(A_n,Q_n,L_n\) columns are exact
formula evaluations; the \(B_n,W_n\) columns and minimizer counts are the
bounded exhaustive results.

| \(n\) | \(A_n\) | \(Q_n\) | \(\max(A_n,Q_n)\) | \(B_n=W_n^{(\le2)}\) | \(L_n\) | \(W_n\) | minimizers \((\le1,\le2)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | \(6\) | \(6\) | \(6\) | \(6\) | -- | \(6\) | \(1,1\) |
| 4 | \(12\) | \(12\) | \(12\) | \(12\) | \(25/3\) | \(12\) | \(1,1\) |
| 5 | \(15\) | \(12\) | \(15\) | \(15\) | \(23/2\) | \(15\) | \(1,1\) |
| 6 | \(20\) | \(20\) | \(20\) | \(20\) | \(76/5\) | \(20\) | \(2,2\) |
| 7 | \(24\) | \(21\) | \(24\) | \(24\) | \(58/3\) | \(24\) | \(2,2\) |
| 8 | \(30\) | \(30\) | \(30\) | \(30\) | \(170/7\) | \(30\) | \(4,4\) |
| 9 | \(35\) | \(30\) | \(35\) | \(36\) | \(59/2\) | \(36\) | \(4,12\) |
| 10 | \(42\) | \(42\) | \(42\) | \(45\) | \(320/9\) | \(45\) | \(24,72\) |
| 11 | \(48\) | \(45\) | \(48\) | \(50\) | \(42\) | \(50\) | \(24,24\) |

Thus the new obstruction does not improve the already exact adjacent lower
bound within this bounded table, even though (TT17) proves a strictly larger
asymptotic lower coefficient. The \(L_n\) values happen to be below \(Q_n\)
in every displayed admissible case, but only \(Q_n\) is proved to lower-bound
\(B_n\); \(L_n\) remains a full-distance obstruction as stated in (TT18).

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

## Verification Boundary And Open Questions

`tests/test_product_distance.py` checks exact rational comparisons, canonical
counts, every pair rather than only adjacent pairs, an independent full
permutation calculation for the smallest cases, deterministic work bounds,
the all-\(n\) adjacent formula against the explicit interleave construction,
the parity-specific equality classifier on the bounded `n=4..11` regression,
the exact incidence-lemma boundary arithmetic, the `n=12` local degree data,
the strict two-threshold floor boundaries and empty/singleton tails, the exact
finite \(Q_n\) obstruction, the effective full-distance tail comparison,
zigzag and tail values, and exact reproduction of both truncated and full
`n=3..11` tables. No cyclic-order enumeration is performed beyond `n=11`.

The following remain unresolved.

- **OPEN QUESTION:** what is the asymptotic behavior of \(W_n/n^2\), and does
  a limit exist?
- **OPEN QUESTION:** can a symbolic order family improve the zigzag
  coefficient while approaching the tail obstruction?
- **OPEN QUESTION:** can stronger combinatorial obstructions narrow the finite
  and asymptotic gap between \(L_n\) and \(W_n\)?
- **OPEN QUESTION:** what are exact formulas or sharper bounds for \(B_n\) and
  \(W_n\)? The theorem here gives a quantitative all-\(n\) lower bound for
  \(B_n\), but not its exact value or a matching upper construction.
- **OPEN QUESTION:** at what \(n\), if any, do positional distances at least
  three first change the optimum? They do not do so for \(3\le n\le11\).

No formula suggested by the nine values of \(W_n\) is promoted to a
conjecture. No geometric certificate, schema, serialized result artifact, or
CLI is created by this work.
