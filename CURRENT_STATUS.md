# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** exact five-prefix one-use charging on the normalized linear
  block.
- **Repository state at startup:** clean `main` worktree at commit
  `1116b1274949475da8462994f296ebd22d0a7bf3`, tracking `origin/main`.
- **Implementation state:** the exact theorem, sole standalone oracle, proof
  note, stable knowledge, project brief, roadmap, and dossier are synchronized;
  all regressions, three independent audits, and final diff checks pass.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Determine whether direct combined-height charging extends from four to exactly
five selected prefixes under
\[
0<\beta_5<\beta_4<\cdots<\beta_1<\alpha<1,
\qquad
0\le\lambda_5\le\cdots\le\lambda_1\le1.
\]
The task permits one standalone exact local-history oracle. Coefficient
optimization, finite rounding, \(k\to\infty\), a theorem for six or more
prefixes, new geometric claims, production code, tests, artifacts, schemas,
backends, certificates, and enumeration limits are out of scope.

## Exact Five-Prefix Result

Put \(r=\lfloor\alpha n\rfloor\),
\(s_i=\lceil\beta_i n\rceil\), \(s_0=r\),
\(I_i=\{s_i,\ldots,s_{i-1}-1\}\), and
\[
H_i=\sum_{t=s_i}^{r-1}A_t.
\]
The six nonnegative coefficients
\[
1-\lambda_1,\quad\lambda_1-\lambda_2,\quad
\lambda_2-\lambda_3,\quad\lambda_3-\lambda_4,\quad
\lambda_4-\lambda_5,\quad\lambda_5
\]
sum to one and give
\[
\max(0,H_1,\ldots,H_5)
\ge
\sum_{i=1}^4(\lambda_i-\lambda_{i+1})H_i+\lambda_5H_5
=
\sum_{i=1}^5\lambda_i\sum_{t\in I_i}A_t.
\]

Every literal history induces an injective map from selected base splits to
original edges. Hence each original slack is canonically charged once or left
unused. Immediately before inserting \(t\), every current edge is either an
untouched original edge or contains an endpoint in
\(\{t+1,\ldots,r-1\}\). Splitting preserves this invariant through all four
boundaries and arbitrary nesting, including edges with two earlier inserted
endpoints.

With \(F_{i,n}=G_{n,\lambda_i}(s_i)\), the complete finite conditions
\[
2\le r\le n-2,
\qquad
1\le s_5<s_4<s_3<s_2<s_1\le r-1
\]
give the exact theorem
\[
\boxed{
\begin{aligned}
\gamma^{(r)}_{1,n}\ge{}&P_{r,n}
+(r-s_1)F_{1,n}+(s_1-s_2)F_{2,n}+(s_2-s_3)F_{3,n}\\
&+(s_3-s_4)F_{4,n}+(s_4-s_5)F_{5,n}.
\end{aligned}
}
\]
No sign assumption on the individual floors is needed. There is no literal
five-split counterexample.

## Standalone Exact Oracle

- The only new standalone oracle is
  `ops/TASK-20260717__five_prefix_charging/literal_oracle.py`.
- It uses only `collections.Counter` and `fractions.Fraction`.
- The five-edge base \((n,r,C_0)=(17,13,(13,17,14,16,15))\) is the minimum
  edge cardinality permitting five simultaneous original-edge charges.
- All 15,120 five-split histories pass and have distinct final cycles.
- Split counts are base \((5,20,100,600,4200)\), recursive
  \((0,10,110,1080,10920)\), and inserted-pair
  \((0,0,10,180,2520)\).
- Exactly 120 histories charge all five original edges. The five local floors
  sum to \(253523/1155\), and the checked finite bound is \(1541348/1155\).

## Verification

- Oracle execution: 15,120 histories pass.
- Ruff lint and format check: pass.
- Focused `tests/test_fixed_order_cycle_ratio.py`: pass.
- Complete local suite: 283 tests pass. An initial five-second command timeout
  was non-diagnostic; the immediate rerun completed successfully.
- Checked-artifact semantic verifier: 4 certificates and 76 local brackets
  pass.
- Checked-artifact schema regression: 4 tests pass.
- Proof-note structural check: 321 equation tags are unique; standalone
  display delimiters, `aligned`, and `array` environments balance. An initial
  substring-based display count was invalid because it counted bracket escapes
  inside formulas; the corrected line-delimiter check passes.

## Evidence Classification And Limitations

- The convex identity, canonical one-use partition, recursive invariant, and
  finite five-segment inequality are **exact method-specific theorems**.
- The 15,120-history oracle is a **verified bounded exact computation**; it
  corroborates but does not prove the theorem.
- The normalized simplex remains logically independent and supplies no
  charging theorem by itself.
- No coefficient optimization, finite rounding, result for six or more
  prefixes, uniform \(k\)-to-\(n\) interchange, asymptotic coefficient,
  convergence, exact residual, or geometric consequence is added.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260717__five_prefix_charging/

## Proposed Next Task

In a fresh STRICT task, prove or refute the exact six-prefix one-use theorem,
still without coefficient optimization, finite rounding, a limiting-prefix
passage, or geometric claims.
