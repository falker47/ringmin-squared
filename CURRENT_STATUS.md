# CURRENT_STATUS - power-ringmin

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** evaluate the explicit threshold-closing PG49-star order on
  `n=10m+3`, `m>=3`.
- **Repository state at startup:** clean `main` worktree at commit
  `fded0cc29029b5d2e725f1609f71ea17b4468e38`, tracking `origin/main`.
- **Implementation state:** Ferrers compatibility, the exact fixed-order `K`
  theorem, all maximizing subsets, five residue formulas, cubic coefficient,
  comparator theorem, complete gain/shortcut audit, cyclic closure, and the
  sole bounded independent diagnostic are complete. Repository-wide
  regressions, independent audits, and final diff hygiene all pass.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For `n=10m+3`, `v=2m`, and
`q=floor((4m+3)/5)=kappa_{v-1}`, evaluate the one piecewise bijection
`alpha_*` in (PG110). Prove Ferrers compatibility first; then determine the
exact induced-subset objective `K`, every maximizing subset, all five
`m mod 5` formulas, the cubic coefficient in `n`, and exact comparisons with
K825 and the closing and preclosing PG46 orders. Only this explicit
combinatorial core order is in scope. No geometric, exact-angular, or global
minimizing-order conclusion is authorized.

## Exact Ferrers Theorem

The exact support threshold is

\[
\kappa_j=
\left\lceil{j(8m+3)\over2(8m+4+j)}\right\rceil.
\]

The images of the five branches of `alpha_*` are

\[
\{0\},\quad[1,q-1],\quad[q+1,m],\quad
[m+1,2m-1],\quad\{q\},
\]

so the map is bijective. Equations (PG39)--(PG40) give
`kappa_1=1`, `kappa_j<=j-1` for `j>=2`, monotonicity, and
`kappa_{2m-1}=q`. Every branch therefore satisfies its Ferrers inequality,
and the genuine cyclic closing column has exact equality

\[
\alpha_*(2m-1)=q=\kappa_{2m-1}.
\]

Thus (PG110) is a relation-compatible bijection for every `m>=3`.

## Exact K And All Maximizers

Let

\[
B_m=\{4m+1,\ldots,10m+3\}.
\]

Every low label `2,...,4m` is isolated. Its deletion gain is positive, with
exact unique minimum `28m+12` at `lambda_0`. Every nontrivial compressed
shortcut has positive margin, with exact minimum `12m+4` on
`(A_0,c_0,b_0)`. The closing low gain and the separate shortcut through
`rho_0=4m+1` are audited literally. The strict shortcut identity proves

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
=\{B_m\}.
}
\]

Hence all and only the maximizing subsets consist of the single set `B_m`.
No conjecture supplied in the task is false.

## Exact Formula And Cubic Coefficient

The exact value is

\[
\boxed{
K(\tau_m^*)=P_{\tau_m^*}(B_m)
={1714m^3+1863m^2+24mq+617m+12q^2+48q+66\over6}.
}
\]

For `r=m mod 5`, write `c_r=(0,1,2,3,-1)`. Then

\[
q={4m+c_r\over5},
\]

and

\[
K(\tau_m^*)
={42850m^3+47247m^2+(16385+216c_r)m
  +1650+240c_r+12c_r^2\over150}.
\]

Thus the five `(linear coefficient, constant)` pairs are

\[
(16385,1650),\ (16601,1902),\ (16817,2178),\
(17033,2478),\ (16169,1422).
\]

Since `n=10m+3`,

\[
K(\tau_m^*)={857\over3000}n^3+O(n^2).
\]

## Exact Comparisons

Direct subtraction gives (KPGSTAR-26). Using only `q<=m` proves that the
three differences from K825, closing PG46, and preclosing PG46 are strictly
negative for every `m>=3`. There is no tie or crossover involving the new
order. The complete ordering is

\[
K_*<K_{\rm cl}<K_{825}<K_{\rm pre}
\quad(3\le m\le6),
\]

and

\[
K_*<K_{825}<K_{\rm cl}<K_{\rm pre}
\quad(m\ge7).
\]

At the minimum row, the values are

\[
10905<10907<10920<10925.
\]

Relative to each comparator, the fixed-family leading improvement is
`-n^3/3000+O(n^2)`.

## Verification

- The sole standalone standard-library diagnostic passes on 28 max-plus and
  shortcut rows `m=3,...,30`.
- It checks 36,989,498 max-plus transitions and all 958,916 proper oriented
  arcs, including every nontrivial shortcut and cyclic-cut orientation, and
  finds the unique optimizer `B_m` on every row.
- Exact Ferrers, formula, and comparator checks pass on 998 rows through
  `m=1000`.
- The diagnostic constructs only the prescribed order and enumerates no
  subset, path permutation, or matching.
- `python -m pytest -p no:cacheprovider` passes all 283 tests.
- The focused checked-artifact schema suite passes all 4 tests, and the
  standalone artifact verifier confirms 4 certificates and 76 local
  brackets for `n=3,4,5,6`.
- Ruff lint/format, scoped source-tag and delimiter audits, Python compile,
  and `git diff --check` pass.
- Three independent audits pass: mathematical proof, diagnostic design, and
  synchronized-source scope/classification. No blocking residue remains.

## Evidence Classification And Limitations

- PG110--PG114 are an **exact Ferrers/bijection theorem**.
- KPGSTAR-1--KPGSTAR-28 are an **exact fixed-order combinatorial theorem**,
  including the unique maximizer, score, formulas, coefficient, and
  comparisons.
- Diagnostic rows are **bounded exact computations** that corroborate but do
  not prove the all-`m` theorem.
- A generic whole-file delimiter count still sees the same inherited two
  surplus display openers in `PRODUCT_DISTANCE_SURROGATE.md` in both `HEAD`
  and the working copy; the new PG110--PG114 section is balanced and the
  count is not caused by this task.
- There is no counterexample to preserve because all three initial
  conjectures are true.
- No geometric feasibility, exact angular-threshold comparison, global
  `K`-minimality, or Power-Ringmin optimum follows.

## Files In Scope

- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/FIXED_ORDER_CYCLE_RATIO.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260719__explicit_pg49_star_exact_k/`

## Proposed Next Task

In a fresh STRICT task, evaluate the monotone PG46 interval shift that sends
the same threshold path `P_q` to the closing gap but leaves the remaining
paths increasing. Determine exactly which part of the PG49-star improvement
comes from reversing the singleton block, with the same complete gain,
shortcut, and cyclic-closure audit and no geometric or global-optimality
inference.
