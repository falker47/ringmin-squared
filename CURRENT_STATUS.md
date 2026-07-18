# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** evaluate the induced-subset objective \(K\) exactly for the
  PG46 bijection that places \(P_m\) in the closing gap \(G_{2m-1}\) on
  \(n=10m+3\), \(m\ge3\).
- **Repository state at startup:** clean main worktree at commit
  963aa533e254cc94e17c1d5e7cd81284df13d552, tracking origin/main.
- **Implementation state:** exact optimizer classification, shortcut-budget
  proof, block sum, minimum row, all boundary ranges, K825 comparison, one
  independent diagnostic, authoritative synchronization, repository
  regressions, and independent audits are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For the fixed PG46 assignment
\[
\alpha(j)=
\begin{cases}
j,&0\le j<m,\\
j+1,&m\le j<2m-1,\\
m,&j=2m-1,
\end{cases}
\]
determine the exact value of \(K\), classify all maximizing subsets, and
compare pointwise and asymptotically with canonical K825. Relation
compatibility and full optimality for \(W\) are prior inputs. Other PG46
witnesses, geometry, angular realizability, global minimization, production
code, artifacts, schemas, and certificates are outside this task.

## Exact Theorem

Put
\[
S_m=\{4m+1,\ldots,10m+3\}.
\]
For every \(m\ge3\), the complete maximizing-subset classification is
\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,10m+3\}}
P(U)=\{S_m\}
}
\]
and
\[
\boxed{
K={572m^3+631m^2+223m+22\over2}.
}
\]
There is no parity branch, exceptional minimum row, or second maximizing
subset.

## Block And Shortcut Certificate

- Deleting the isolated holes \(H_m=\{2,\ldots,4m\}\) leaves an explicit
  cyclic backbone consisting of the \(m\) unshifted triples, the shifted
  singleton chain, the closing triple \(P_m\), and \(4m+1\).
- Five exhaustive hole-position ranges have positive deletion gain. Their
  exact global minimum is \(28m+12\).
- Every compressed oriented path has positive shortcut margin. Endpoint-hole,
  high-middle, \(L\), three-edge, and at-least-four-edge roles have separate
  symbolic bounds, proving the exact global minimum \(12m+4\).
- Direct summation of the unshifted triple blocks, shifted singleton blocks,
  and combined cyclic closing block yields the displayed cubic formula.
- At \(m=3\), the unique maximizer is \(\{13,\ldots,33\}\),
  \(K=10907\), and the minimum hole and shortcut margins are \(96\) and
  \(40\). Thus the least admitted row obeys the same theorem.

## Exact K825 Comparison

On the same \(n=10m+3\) rows,
\[
K_{825}={572m^3+629m^2+235m+30\over2}
\]
and therefore
\[
\boxed{K-K_{825}=m^2-6m-4.}
\]
The closing PG46 order is strictly better for \(m=3,4,5,6\), strictly worse
for every \(m\ge7\), and never tied. In terms of \(n\),
\[
K={286n^3+581n^2-58n-1777\over1000},
\qquad
K-K_{825}={n^2-66n-211\over100}.
\]
Consequently its cubic coefficient is still \(143/500\); there is no
coefficient improvement, and the family is eventually worse by
\(n^2/100+O(n)\).

## Verification

- The sole dossier-local standard-library diagnostic reconstructs the order
  without production imports.
- For \(m=3,\ldots,30\), a max-plus increasing-path DP independently finds
  the stated score, one optimizer, and the stated subset; an all-oriented-arc
  audit independently checks the hole and shortcut certificate.
- Direct score/formula and K825 comparisons continue through \(m=1000\).
- The diagnostic passes with 36,989,498 DP transitions and 958,916 oriented
  shortcut arcs; Ruff lint and format checks pass.
- Focused regressions pass 150 tests; the complete suite passes 283 tests;
  the schema regression passes four tests; checked-artifact verification
  accepts four certificates and 76 local brackets.
- Three independent read-only audits pass after one local exact-minimum proof
  gap was corrected. KPG46 tags, added Markdown/LaTeX structure, whitespace,
  final diff, and Git status checks pass.

## Evidence Classification And Limitations

- The optimizer classification, formula, block sum, shortcut inequalities,
  boundary treatment, K825 comparison, and coefficient decision are **exact
  theorems**.
- The diagnostic is a **bounded exact computation** that corroborates but
  does not prove the all-\(m\) theorem.
- The result concerns one explicit full-\(W\)-optimal core order. It proves no
  geometric feasibility or optimality, no global \(K\)-minimizer
  classification, no improvement of an all-residue coefficient, and no
  statement about the other sharp PG46 witness.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260718__pg46_closing_exact_k/

## Proposed Next Task

After manual review and in a fresh STRICT chat, evaluate \(K\) exactly for
the other sharp PG46 witness, which places \(P_m\) in \(G_{2m-2}\), and
compare it pointwise and asymptotically with both the closing-PG46 formula and
canonical K825. Classify every maximizing subset and boundary without
permutation or matching enumeration and without geometric or global claims.
