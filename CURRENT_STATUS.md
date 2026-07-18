# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** formalize the all-fixed-\(k\) corollary from
  CR28cr--CR28dd and CR28dr--CR28dw.
- **Repository state at startup:** clean `main` worktree at commit
  `6c5eb5b49e40f763a88580656f04a4143b2b4852`, tracking `origin/main`.
- **Implementation state:** the exact corollary, strict admissibility proof,
  authoritative synchronization, relevant dossier corrections, sole
  standalone exact diagnostic, regressions, independent audits, and final
  source/diff verification are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Fix

\[
\alpha_\infty={13-2\sqrt2\over23}.
\]

For every finite \(k\), use the unique normalized optimizer \(x^{(k)}\) to
define

\[
\beta_i={1+\alpha_\infty+(3\alpha_\infty-1)x_i^{(k)}\over4},
\qquad
\lambda_i={(3\alpha_\infty-1)x_i^{(k)}\over\beta_i}.
\]

Prove strict order and all-middle admissibility, apply the direct charging
theorem at each fixed \(k\), and take the supremum of the resulting scalar
liminf inequalities. Synchronize all authoritative sources that denied this
consequence or described \(C_{5,*}\) as the current general coefficient.

Production, tests, artifacts, schemas, backends, certificates, and enumeration
limits remain unchanged. The only new executable is a dossier-local exact
diagnostic.

## Exact Strict Admissibility

Put

\[
A_\infty=3\alpha_\infty-1,
\qquad
S_\infty=1+\alpha_\infty.
\]

The exact bounds \(1/3<\alpha_\infty<1/2\) and the normalized theorem give

\[
1=x_0^{(k)}>x_1^{(k)}>\cdots>x_k^{(k)}>0.
\]

For every \(i\),

\[
\beta_i-{S_\infty\over4}={A_\infty x_i^{(k)}\over4}>0,
\qquad
\alpha_\infty-\beta_i
={A_\infty(1-x_i^{(k)})\over4}>0,
\]

\[
{S_\infty\over3}-\beta_i
={S_\infty-3A_\infty x_i^{(k)}\over12}
>{1-2\alpha_\infty\over3}>0.
\]

The map
\(x\mapsto4A_\infty x/(S_\infty+A_\infty x)\) is strictly increasing.
Therefore

\[
0<\beta_k<\cdots<\beta_1<\alpha_\infty<1,
\qquad
0<\lambda_k<\cdots<\lambda_1<1,
\]

and every cutoff lies strictly in the middle clipping branch.

## Exact All-Fixed-k Corollary

For every fixed finite \(k\), the strict margins provide a finite threshold
\(N_k\), allowed to depend on the complete tuple. CR28dw and CR28ap then give

\[
L_\Lambda:=\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge p(\alpha_\infty)+{A_\infty^3M_k\over8}.
\]

Since this scalar inequality holds for every fixed finite \(k\) and
\(M_k\nearrow1/3\),

\[
\boxed{
L_\Lambda
\ge{434+4\sqrt2\over1587}
=:C_{\mathrm{AF}}.
}
\]

The additive cyclic-ratio relation gives the geometric consequence

\[
\boxed{
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{434+4\sqrt2\over1587\pi}.
}
\]

The exact simplification uses

\[
p(\alpha_\infty)={9038+722\sqrt2\over36501},
\qquad
{A_\infty^3\over24}={944-630\sqrt2\over36501}.
\]

## Quantifier And Limit Audit

- For every fixed \(k\), there is a possibly different threshold \(N_k\).
- The fixed-parameter \(n\to\infty\) liminf is taken before any supremum in
  \(k\).
- The same scalar \(L_\Lambda\) is at least every coefficient \(C_k\), hence
  it is at least \(\sup_k C_k\).
- No sequence \(k=k(n)\) is selected.
- No threshold uniform in \(k\) is asserted or needed.
- No \(n\)-limit and \(k\)-limit are interchanged.
- Since \(M_k<1/3\) for every finite \(k\), no finite rounded theorem at
  \(C_{\mathrm{AF}}\) is claimed.

## Fixed Five-Prefix Status

The full eleven-parameter optimization remains exact and unique inside the
fixed \(k=5\) template. Its coefficient is unchanged and satisfies

\[
C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*}.
\]

It is no longer the current cross-\(k\) lower coefficient, because

\[
C_{5,*}
<{276777463862377\over10^{15}}
<{277\over1000}
<{434+4\sqrt2\over1587}.
\]

The rational finite theorem from the minimal threshold \(234\), and the lack
of finite rounding at the irrational five-prefix optimizer, remain unchanged.

## Verification

- The new standalone \(\mathbb Q(\sqrt2)\) diagnostic passes exact checks for
  \(k=1,\ldots,8\).
- Ruff check and final format check pass for the sole new diagnostic; its
  initial format check correctly requested one mechanical reformat.
- The historical normalized-simplex diagnostic passes 203,489 exact grid
  states, the arbitrary-charging oracle passes 332,640 histories, and the
  global-five diagnostic passes all 21 regimes.
- The focused fixed-order suite passes 101 tests and the full suite passes 283
  tests. The artifact verifier passes four certificates and 76 local brackets;
  the schema suite passes four tests.
- Source structure passes strict UTF-8/LF/final-newline/trailing-whitespace,
  balanced-display/fence/environment, and 378-unique-equation-tag checks.
  Repository-wide stale-claim and scope audits pass.
- Three independent read-only audits confirm the mathematics, authoritative
  synchronization, diagnostic independence, and protected-path scope.
- Final `git status`, complete diff inspection, and `git diff --check` pass;
  only the requested Markdown/dossier files and sole dossier-local diagnostic
  are changed.

## Evidence Classification And Limitations

- Strict admissibility, the fixed-\(k\) coefficient identity, the supremum
  argument, geometric transfer, and comparison with \(C_{5,*}\) are **exact
  method-specific theorems**.
- The new script is a **verified bounded exact computation** that corroborates
  but does not replace the all-real proof.
- The result is a liminf lower coefficient, not convergence, an exact leading
  constant, an exact residual, or a finite rounded theorem at the supremum.
- No production, test, artifact, schema, backend, certificate, or enumeration
  claim changes.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/ALL_N_LOWER_BOUND.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260716__normalized_prefix_simplex/
- ops/TASK-20260717__arbitrary_finite_prefix_charging/
- ops/TASK-20260717__global_five_prefix_optimization/TASK_STATUS.md
- ops/TASK-20260718__all_fixed_k_corollary/

## Proposed Next Task

In a fresh STRICT task, derive an exact symbolic count of
relation-compatible, equivalently full-optimal, scaffold bijections from the
nested Ferrers thresholds, without enumerating path permutations.
