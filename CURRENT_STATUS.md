# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** evaluate the induced-subset objective \(K\) exactly for the
  PG46 bijection that places \(P_m\) in the preclosing gap \(G_{2m-2}\) on
  \(n=10m+3\), \(m\ge3\).
- **Repository state at startup:** clean main worktree at commit
  113d6f9173213c9ff2363328cec823fb32b2377a, tracking origin/main.
- **Implementation state:** order reconstruction, exact optimizer
  classification, seven-range hole proof, complete shortcut and cyclic-closure
  audit, block sum, minimum row, pointwise and asymptotic comparisons, one
  independent diagnostic, authoritative synchronization, repository
  regressions, and independent reviews are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For the fixed PG46 assignment
\[
\alpha_m^{\rm pre}(j)=
\begin{cases}
j,&0\le j<m,\\
j+1,&m\le j<2m-2,\\
m,&j=2m-2,\\
2m-1,&j=2m-1,
\end{cases}
\]
determine the exact value of \(K\), classify every maximizing subset, and
compare pointwise and asymptotically with both closing PG46 and canonical
K825. Relation compatibility and full optimality for \(W\) are prior inputs.
Other PG46 witnesses, geometry, angular-threshold ordering, global
minimization, production code, tests, artifacts, schemas, and certificates
are outside this task.

## Exact Theorem

Put
\[
S_m=\{4m+1,\ldots,10m+3\}.
\]
For every \(m\ge3\),
\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,10m+3\}}
P(U)=\{S_m\}
}
\]
and
\[
\boxed{
K={572m^3+631m^2+235m+22\over2}.
}
\]
There is no parity branch, boundary correction, exceptional minimum row,
tie, or second maximizing subset.

## Block, Hole, And Shortcut Certificate

- Deleting \(H_m=\{2,\ldots,4m\}\) leaves the \(m\) unshifted triples, the
  shortened shifted-singleton chain, \(P_m\) in \(G_{2m-2}\), the closing
  singleton \(P_{2m-1}\), and \(4m+1\).
- Seven exhaustive hole-position classes have positive deletion gain. The
  exact global minimum is \(28m+12\), attained at \(\lambda_0\).
- Every compressed oriented path has positive shortcut margin. Endpoint-hole,
  two-edge low/high-middle, three-edge, and at-least-four-edge roles are
  covered separately.
- The changed cyclic two-edge \(4m+1\) role has margin
  \(8m^2+2m+1\). The sole pair that weakens the old three-edge adjacency
  bound is \((6m+1,4m+1)\); its literal cyclic path has margin
  \(36m^2-2m-4\).
- The exact global nontrivial shortcut margin remains \(12m+4\), attained at
  \(c_0\). Direct block summation then yields the displayed cubic.
- At \(m=3\), the order is determined by
  \(\alpha_3^{\rm pre}=(0,1,2,4,3,5)\), the unique maximizer is
  \(\{13,\ldots,33\}\), \(K=10925\), and the minimum hole and shortcut
  margins are \(96\) and \(40\).

## Exact Comparisons

The closing-PG46 and K825 values on the same rows satisfy
\[
K_{\rm pre}-K_{\rm cl}=6m,
\qquad
K_{\rm pre}-K_{825}=m^2-4.
\]
Thus the preclosing witness is strictly worse than both for every \(m\ge3\).
The complete ordering is
\[
\begin{cases}
K_{\rm cl}<K_{825}<K_{\rm pre},&3\le m\le6,\\
K_{825}<K_{\rm cl}<K_{\rm pre},&m\ge7.
\end{cases}
\]
In terms of \(n=10m+3\),
\[
K_{\rm pre}
={286n^3+581n^2+542n-3577\over1000},
\]
\[
K_{\rm pre}-K_{\rm cl}={3(n-3)\over5},
\qquad
K_{\rm pre}-K_{825}={n^2-6n-391\over100}.
\]
All three retain cubic coefficient \(143/500\). The two PG46 witnesses share
quadratic coefficient \(581/1000\), while K825 has \(571/1000\);
preclosing is worse than closing linearly and worse than K825 quadratically.

## Verification

- The sole dossier-local standard-library diagnostic reconstructs the order
  without production or test imports.
- For \(m=3,\ldots,30\), a max-plus increasing-path DP independently finds
  the stated score, exactly one optimizer, and \(S_m\); an all-oriented-arc
  audit checks every hole and shortcut condition.
- Direct score, formula, closing-PG46, and K825 comparisons continue through
  \(m=1000\).
- The diagnostic passes with 36,989,498 DP transitions and 958,916 oriented
  shortcut arcs; in-memory compile and Ruff lint/format checks pass.
- The complete test suite passes 283 tests; the schema regression passes four
  tests; checked-artifact verification accepts four certificates and 76 local
  brackets.
- Three independent read-only reviews checked proof algebra, shortcut-role
  completeness, diagnostic independence, comparisons, claim limits, and
  synchronization. Two notation/boundary findings were corrected and
  re-audited; final structure, whitespace, diff, and path-scope checks pass.

## Evidence Classification And Limitations

- The order reconstruction, maximizing-subset classification, formula, hole
  gains, shortcut inequalities, cyclic closure, block sum, boundary treatment,
  comparisons, and asymptotic coefficients are **exact theorems**.
- The diagnostic is a **bounded exact computation** that corroborates but
  does not prove the all-\(m\) theorem.
- The result concerns one explicit full-\(W\)-optimal core order. It proves no
  geometric feasibility or optimality, no exact angular-threshold ordering,
  no global \(K\)-minimizer classification, and no improved all-residue
  coefficient.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260718__pg46_preclosing_exact_k/

## Proposed Next Task

After manual review and in a fresh STRICT chat, derive the leading asymptotics
of \(\log\mathsf F_m^{\rm lab}\) from the exact PG49 Ferrers product, with a
rigorous error term and cutoff control, without permutation or matching
enumeration and without geometric interpretation.
