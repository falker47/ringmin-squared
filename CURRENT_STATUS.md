# CURRENT_STATUS - power-ringmin

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** evaluate exactly the induced-subset objective \(K\) for
  the already fixed odd-\(v\) map (PGODD-6) on \(n=10m+8\), \(m\ge1\),
  without changing the candidate.
- **Repository state at startup:** clean main worktree at commit
  513f294d6c7e79e899d953f8b197ae3e23cded73.
- **Implementation state:** the literal core, unique maximizing subset,
  all elimination gains, every compressed shortcut and equality case, exact
  score, residue formulas, boundary rows, and same-subsequence K825
  comparison are proved and synchronized.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For the fixed map

\[
q=\left\lfloor{4m+5\over5}\right\rfloor,\qquad
\alpha^\circ(j)=
\begin{cases}
0,&j=0,\\
j,&1\le j<q,\\
j+1,&q\le j\le m,\\
3m+1-j,&m+1\le j\le2m-1,\\
q,&j=2m,
\end{cases}
\]

reconstruct its cyclic core order and determine \(K\), every maximizing
subset, all boundary exceptions, and the exact comparison with canonical
K825. The task includes doubleton, singleton block, cyclic closure, every
shortcut length, and every equality case.

The task excludes candidate modification or search, alternative order
families, angular or geometric claims, global \(K\)-minimality, and global
optimality.

## Exact Core And Maximizer

With the retained symbols from (PGODD-2)--(PGODD-3), the fixed core is

\[
\tau_m^\circ
=\mathop{\bigcirc}_{j=0}^{2m}
(E_j,\lambda_j,P_{\alpha^\circ(j)},\rho_{j+1\bmod(2m+1)}).
\]

Put

\[
L=4m+3,\qquad
H_m=\{2,\ldots,4m+2\},\qquad
B_m=\{L,\ldots,10m+8\}.
\]

Deleting \(H_m\) gives the exact cyclic backbone

\[
\left(
L,(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
E_m,a,b,
(E_j,x_{3m+1-j})_{j=m+1}^{2m-1},
E_{2m},P_q
\right),
\]

with every empty range literal. The all-domain theorem is

\[
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^\circ}(U)=\{B_m\}.
\]

Thus the maximizing subset is unique for every \(m\ge1\).

## Exact Score, Residues, And K825 Comparison

\[
\boxed{
K(\tau_m^\circ)
={1714m^3+4467m^2+24mq+3749m+12q^2+60q+1032\over6}.}
\]

The only required split is \(m\bmod5\), with

\[
q={4m+c_r\over5},\qquad
(c_0,c_1,c_2,c_3,c_4)=(5,1,2,3,4).
\]

These classes correspond to \(n\bmod50=8,18,28,38,48\), respectively.
All five branches have coefficient \(857/3000\) in \(n\).

On the same rows, canonical K825 specializes to

\[
K_{825}(m)={572m^3+1497m^2+1279m+354\over2},
\]

and

\[
K(\tau_m^\circ)-K_{825}(m)
={-m^3-12m^2+12mq-44m+6q^2+30q-15\over3}<0.
\]

There is no tie or crossover. The fixed-family coefficients are
\(857/3000\) and \(858/3000=143/500\), respectively. This comparison is
not a global coefficient or minimizing-order theorem.

## Gains, Shortcuts, And Boundaries

- The nine exhaustive elimination-gain classes are all strict. Their unique
  minimum is \(28m+26\), attained only by \(\lambda_0=4m+2\).
- Every nontrivial compressed shortcut is strict. Its exact unique minimum
  is
  \[
  \begin{cases}
  4,&m=1,\ C=(12,7,16),\\
  30,&m=2,\ C=(18,11,24),\\
  12m+10,&m\ge3,\ C=(A_0,c_0,B_0).
  \end{cases}
  \]
- The doubleton has two separate positive two-edge margins and the exact
  three-edge window \(2(m+1)(17m+26)\). Singleton, terminal, outer-label,
  all three-edge, all longer, and every cyclic-cut role are separate.
- At \(m=1\), \(\alpha^\circ=(0,2,1)\), the singleton range is empty,
  \(K=1843\), and K825 is \(1851\).
- At \(m=2\), \(\alpha^\circ=(0,1,3,4,2)\), singleton reversal is
  order-neutral, \(K=6729\), and K825 is \(6738\).
- Neither minimum row is an exception to the formula or unique argmax; only
  the identity of the minimum shortcut changes.

## Verification

- The sole standalone standard-library diagnostic constructs only
  (PGODD-6) and passes: 1,000 formula/residue rows; 5,012,000 literal core
  entries; 30 max-plus rows with 39,461,580 transitions; 1,007,210 proper
  oriented arcs, including 1,000,460 nontrivial compressed shortcuts.
- Standalone syntax and scoped Ruff lint pass. The first Ruff format check
  found one mechanical formatting delta; formatting was applied and the
  final check passes.
- Full pytest passes: 283 passed.
- The focused checked-artifact schema suite passes: 4 passed.
- The standalone checked-artifact verifier passes for four certificates,
  76 local brackets, and \(n=3,4,5,6\).
- The scoped source audit passes with 36 sequential unique KPGODD tags,
  42 balanced displays, balanced aligned/array/cases/gathered environments,
  and no control characters or unescaped TeX token.
- Two independent mathematical audits and one independent diagnostic audit
  report no remaining defect after wording hardening.
- Final Git status, complete tracked/untracked diff inspection, and
  `git diff --check` pass. Git emitted only the sandbox-specific warning that
  the user-level exclude file outside the repository was unreadable; every
  repository-local command completed with exit code zero.

## Evidence Classification And Limitations

- (KPGODD-1)--(KPGODD-36) are an **exact combinatorial theorem** about one
  fixed cyclic core order.
- The standalone diagnostic is **bounded exact computation** used only for
  independent corroboration.
- No angular, geometric, global-minimizer, global-optimality, or upstream
  Ringmin conclusion is asserted or inferred.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260719__pgodd_exact_k/

## Proposed Next Task

In a fresh STRICT task, attack the filtered cubic-convergent obstruction
(KPGZERO-23)--(KPGZERO-24): construct an infinite congruence-compatible
subsequence entering an exact \(g\)-window, prove eventual exclusion, or
record a strictly sharper exact obstruction. Finite continued-fraction
extension remains diagnostic only.
