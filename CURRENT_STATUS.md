# CURRENT_STATUS - power-ringmin

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** evaluate the descending-min PG49 representative on the
  residue branch \(n=10m+3\), \(m\ge3\).
- **Repository state at startup:** clean `main` worktree at commit
  `c310228d86fd0f0598dee1ff7984b5100726337b`, tracking `origin/main`.
- **Implementation state:** the all-\(m\) Ferrers proof, exact \(K\) formula,
  complete maximizer classification, comparator theorem, asymptotic formula
  class, one bounded independent diagnostic, durable synchronization,
  complete regressions, independent audits, and final diff hygiene are
  complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Fix \(\alpha_{\min}(0)=0\). For
\(j=2m-1,\ldots,1\), assign to \(G_j\) the least unused path index
\(k\ge\kappa_j\). Prove that this recursion is a relation-compatible
bijection for every \(m\ge3\); determine the exact induced-subset objective
\(K\), all maximizing subsets, the exact formula class and cubic coefficient;
and compare it exactly with K825 and the closing and preclosing PG46 orders.
Only this explicit combinatorial core order is in scope. Permutation,
matching, or subset enumeration and geometric or global-optimality
consequences are out of scope.

## Exact Ferrers Theorem

With \(v=2m\) and
\[
\Delta_j=\kappa_{j+1}-\kappa_j\in\{0,1\},
\]
the suffix after assigning \(G_j,\ldots,G_{v-1}\) is exactly
\[
\{\alpha_{\min}(t):j\le t\le v-1\}
=[\kappa_j,\kappa_j+v-1-j].
\]
Consequently every step exists, every chosen index satisfies its Ferrers
threshold, and
\[
\alpha_{\min}(j)
=\kappa_j+(1-\Delta_j)(v-1-j)
\quad(1\le j\le v-2),
\qquad
\alpha_{\min}(v-1)=\kappa_{v-1}.
\]
Together with \(\alpha_{\min}(0)=0\), this is a relation-compatible
bijection for every integer \(m\ge3\).

## Exact K And All Maximizers

The resulting rooted core order \(\tau_m^{\min}\) satisfies
\[
\boxed{
K(\tau_m^{\min})=K_{825}(m)+D_m+G_m,
}
\]
where \(D_m\) is the exact path-connection sum (KPGMIN-4) and \(G_m\) is the
positive-part sum of the two early-plateau singleton gains
(KPGMIN-7)--(KPGMIN-8). This is an exact \(O(m)\) integer evaluation, not a
search.

Let
\[
B_m=\{4m+1,\ldots,10m+3\},
\]
and let \(\mathcal P_m,\mathcal Z_m\) be respectively the positive- and
zero-gain low-label sets in (KPGMIN-13). All and only the maximizing subsets
are
\[
\boxed{
B_m\cup\mathcal P_m\cup Z',
\qquad Z'\subseteq\mathcal Z_m,
}
\]
so their exact number is \(2^{|\mathcal Z_m|}\). A signed shortcut proof,
not subset enumeration, establishes the equality cases.

Universal uniqueness is a **disproved claim**. The exact row
\[
\begin{aligned}
m&=101805057120180546870,\\
j&=29025982843749082380,\\
\kappa_j=\kappa_{j+1}&=14013559766810587979
\end{aligned}
\]
assigns singleton index \(188597691163422599338\) and has
\(L_{m,j}=0\). It therefore has a genuine independent zero-gain toggle.

## Exact Comparisons

Write \(H_m=D_m+G_m\). Then
\[
\begin{aligned}
K(\tau_m^{\min})-K_{825}&=H_m,\\
K(\tau_m^{\min})-K(\tau_m^{\rm cl})
 &=H_m-(m^2-6m-4),\\
K(\tau_m^{\min})-K(\tau_m^{\rm pre})
 &=H_m-(m^2-4).
\end{aligned}
\]
Exact Abel bounds prove \(D_m>m^2-4\) for every \(m\ge5\), while the initial
rows give
\[
(D_3,G_3)=(12,0),\qquad
(D_4,G_4)=(-4,0).
\]
Thus the descending-min order is below K825 and preclosing PG46 exactly at
\(m=4\), above both at \(m=3\) and every \(m\ge5\), above closing PG46 for
every \(m\ge3\), and never tied.

## Cubic Coefficient And Formula Class

Let \(a\in(0,1)\) be the unique root of
\[
a^3-30a^2-216a+64=0.
\]
The exact coefficient is
\[
\begin{aligned}
C={}&206\sqrt{41}-{2546\over3}
+128\bigl(56\log2+10\log5-19\log(13+\sqrt{41})\bigr)\\
&+{24\over5}a^2-{3212\over5}a+{1616\over15}
+2176\log{a+8\over8},
\end{aligned}
\]
and
\[
K(\tau_m^{\min})
=Cm^3+O(m^2),
\qquad
C=288.1683105370884612135\ldots.
\]
Since \(n=10m+3\), the \(n^3\) coefficient is
\[
{C\over1000}
=0.2881683105370884612135\ldots>{143\over500}.
\]
The logarithms combine as \(128\log Q\) for the nonunit algebraic number
\(Q\) in (KPGMIN-39). Hermite--Lindemann makes \(C\) transcendental.
Therefore this integer-valued exact score is neither polynomial nor eventual
quasipolynomial; (KPGMIN-9) is the exact replacement.

## Verification

- The standalone standard-library diagnostic passes on 28
  max-plus/shortcut rows \(m=3,\ldots,30\), checking 36,989,498 max-plus
  transitions and 958,916 oriented shortcut arcs. Formula and comparator
  checks pass on 998 rows through \(m=1000\).
- The diagnostic constructs only the prescribed greedy order. It enumerates
  no subset, permutation, or matching. Its absence of zero gains through
  \(m=1000\) is explicitly bounded and does not override the exact large
  counterexample.
- Scoped Ruff lint and format checks and an in-memory compile pass.
- The complete repository suite passes: 283 tests in 65.04 seconds. The
  focused checked-artifact schema suite passes four tests in 0.74 seconds.
  Semantic checked-artifact verification passes for four certificates and
  76 local brackets.
- Independent read-only audits reproduce PG100--PG109 and KPGMIN-1--KPGMIN-39,
  including the exact counterexample, signed equality cases, Abel comparison,
  uniform \(O(m^2)\) remainder, and transcendence argument.
- Source tags, final status, complete diff, whitespace, and
  `git diff --check` pass.

## Evidence Classification And Limitations

- PG100--PG109 are an **exact Ferrers/bijection theorem**.
- KPGMIN-1--KPGMIN-39 are an **exact fixed-order combinatorial theorem**,
  including all maximizers, pointwise comparisons, asymptotics, and formula
  classification.
- The enormous zero row is an **exact counterexample** to universal
  uniqueness.
- Diagnostic rows are **bounded exact computations** that corroborate but do
  not prove the all-\(m\) theorem.
- No geometric feasibility, angular-threshold equality, global
  \(K\)-minimality, or Power-Ringmin optimum follows.

## Files In Scope

- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/FIXED_ORDER_CYCLE_RATIO.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260719__ferrers_greedy_exact_k/`

## Proposed Next Task

After manual review and in a fresh STRICT chat, classify the exact
Diophantine zero-gain rows of the descending-min PG49 order. Determine whether
\(\mathcal Z_m\ne\varnothing\) occurs finitely or infinitely often and
characterize both equations \(L_{m,j}=0\) and \(R_{m,j}=0\) under the exact
plateau inequalities, without using a bounded sweep as an infinite proof.
