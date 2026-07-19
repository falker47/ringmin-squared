# CURRENT_STATUS - power-ringmin

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** evaluate the monotone threshold-closing PG46 interval
  shift `alpha_{q,2m-1}` on `n=10m+3`, `m>=3`.
- **Repository state at startup:** clean `main` worktree at commit
  `e4dae3ee5c44587c4a93fd04ca68c486a1505b70`, tracking `origin/main`.
- **Implementation state:** the exact order, unique maximizing subset,
  score, five residue formulas, deletion gains, compressed shortcuts, cyclic
  closure, comparator theorem, singleton-inversion decomposition, and sole
  bounded independent diagnostic are complete. Full tests, checked artifacts,
  scoped lint/format/compile, source audits, and three independent reviews
  pass. The complete final diff and whitespace hygiene pass.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For `n=10m+3`, `m>=3`, put

\[
q=\left\lfloor{4m+3\over5}\right\rfloor=\kappa_{2m-1}
\]

and evaluate the single PG46 interval shift

\[
\alpha_m^\uparrow(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le2m-2,\\
q,&j=2m-1.
\end{cases}
\]

This moves `P_q` to the cyclic closing gap and leaves all other paths in
increasing order. Only its induced-subset objective `K`, maximizing subsets,
five residue formulas, deletion/shortcut/closure proof, and comparisons with
PG49-star, K825, closing PG46, and preclosing PG46 are in scope. Exact
angular thresholds, geometry, global `K`-minimality, and minimizing-order
classification are excluded.

## Exact Maximizer And Score

Let

\[
B_m=\{4m+1,\ldots,10m+3\}.
\]

The exact theorem is

\[
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
=\{B_m\},
\]

so `B_m` is the only maximizing subset, and

\[
K_\uparrow
={572m^3+619m^2+8mq+207m+4q^2+16q+22\over2}.
\]

Every one of the `4m-1` low labels is an isolated hole. The seven exact
deletion-gain classes have unique minimum `28m+12` at `lambda_0`. Every
nontrivial compressed shortcut is strict, with unique minimum `12m+4` on
`(A_0,c_0,b_0)`. The proof treats separately the closing hole
`lambda_{2m-1}=2`, the retained closing role `b_q-L-E_0`, every longer arc
crossing the cyclic cut, and the minimum row `m=3`.

## Five Residue Formulas

For `r=m mod 5`, let `c_r=(0,1,2,3,-1)`. Then

\[
q={4m+c_r\over5},
\]

and

\[
K_\uparrow
={14300m^3+15699m^2+(5495+72c_r)m
  +550+80c_r+4c_r^2\over50}.
\]

The five `(linear coefficient, constant)` pairs in the numerator are

\[
(5495,550),\ (5567,634),\ (5639,726),\ (5711,826),\ (5423,474).
\]

All branches have

\[
K_\uparrow={143\over500}n^3+O(n^2).
\]

## Exact Comparisons And Singleton Reversal

Direct subtraction gives

\[
K_\uparrow-K_*
={m(m-1)(m-2)\over3}
={ (n-3)(n-13)(n-23)\over3000}>0,
\]

\[
K_\uparrow-K_{825}
=2q^2+4mq+8q-5m^2-14m-4<0,
\]

\[
K_\uparrow-K_{\rm cl}=-2(m-q)(3m+q+4)\le0,
\]

with equality only at `m=3`, and

\[
K_\uparrow-K_{\rm pre}
=-2(m-q)(3m+q+4)-6m<0.
\]

Hence

\[
\begin{array}{ll}
m=3:&K_*<K_\uparrow=K_{\rm cl}<K_{825}<K_{\rm pre},\\
4\le m\le6:&K_*<K_\uparrow<K_{\rm cl}<K_{825}<K_{\rm pre},\\
m\ge7:&K_*<K_\uparrow<K_{825}<K_{\rm cl}<K_{\rm pre}.
\end{array}
\]

The monotone order and PG49-star differ only on the singleton block. The
per-gap deltas have mixed signs, but their aggregate is exactly
`m(m-1)(m-2)/3`. Thus singleton reversal supplies the complete cubic
`n^3/3000+O(n^2)` PG49-star advantage, while the monotone shift's gains over
the three coefficient-`143/500` comparators are only quadratic.

## Verification

- The sole standalone standard-library diagnostic passes on 28 max-plus and
  shortcut rows `m=3,...,30`.
- It checks 36,989,498 max-plus transitions and all 958,916 proper oriented
  arcs, including every nontrivial compressed shortcut and cyclic-cut arc.
- Exact Ferrers, score, five-residue, inversion-delta, and comparator checks
  pass on 998 rows through `m=1000`.
- The diagnostic constructs only the prescribed shift and enumerates no
  subset, path permutation, matching, or cyclic-order family.
- `python -m pytest -p no:cacheprovider --basetemp <workspace-local-path>`
  passes all 283 tests. The first two attempts are retained as failed evidence:
  the default Windows temp directory and `C:\tmp` each caused the same 31
  `tmp_path` setup errors after 252 passes because both paths were denied.
- The focused schema suite passes all 4 tests, and the standalone artifact
  verifier confirms 4 certificates and 76 local brackets for `n=3,4,5,6`.
- Scoped Ruff lint/format and Python compile pass for the sole new Python
  file. Whole-tree Ruff reports four lint findings and 39 formatting
  candidates, all in pre-existing unchanged files; no unrelated code was
  modified.
- The source audit confirms 29 sequential unique KPG46Q tags, balanced
  displays/environments, no duplicate primary tags, clean control/BOM checks,
  and exactly one diagnostic. Three independent reviews find no remaining
  theorem, diagnostic, source-sync, scope, or classification defect.
- Complete diff inspection, generated-file cleanup, final Git status, scoped
  source audit, and `git diff --check` pass.

## Evidence Classification And Limitations

- KPG46Q-1--KPG46Q-29 are an **exact fixed-order combinatorial theorem**.
- Diagnostic rows are **bounded exact computations** that corroborate but do
  not prove the all-`m` theorem.
- There is no exact angular-threshold comparison, geometric consequence,
  global `K`-minimality claim, or minimizing-order classification.
- No Ringmin theorem is generalized.

## Files In Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md`
- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260719__pg46_threshold_closing_exact_k/`

## Proposed Next Task

In a fresh STRICT task, classify the exact Diophantine zero-gain set
`Z_m` for the descending-min PG49 order, retaining both left- and right-hole
equations and the exact plateau inequalities. Do not infer an infinite or
finite classification from bounded sweeps.
