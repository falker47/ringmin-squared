# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** determine the precise logarithmic coefficient of the exact
  labelled PG69 Ferrers count.
- **Repository state at startup:** clean `main` worktree at commit
  `6e7a1b6e241899883d4432d670ef8c261b3ca02d`, tracking `origin/main`.
- **Implementation state:** the symbolic proof, uniform floor/ceiling lemma,
  residue/endpoint audit, formula-only diagnostic, authoritative
  synchronization, complete regressions, independent audits, and final diff
  hygiene are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Starting from PG69 and the PG74--PG85 decomposition, decide rigorously whether
there is a constant \(\gamma\) such that
\[
\log\mathsf F_m^{\rm lab}
=2m\log m+C_{\rm F}m+\gamma\log m+O(1),
\]
with separate factorial, smooth-perturbation, and rounding contributions.
The singular range \(j=o(m)\), bulk, exact cutoff hits, residue classes, and
endpoints are in scope. Permutation or matching enumeration, production code,
artifacts, alternative scaffolds, and geometry are out of scope.

## Exact Theorem

Put
\[
C_{\rm F}=14\log2+6\log3-10\log5-2.
\]
Then
\[
\boxed{
\log\mathsf F_m^{\rm lab}
=2m\log m+C_{\rm F}m+{3\over4}\log m+O(1).
}
\]
Consequently the logarithmic coefficient exists uniquely and
\[
\boxed{\gamma={3\over4}}.
\]
Equivalently, the residual divided by \(\log m\) tends to \(3/4\). The
theorem does not assert convergence of the remaining bounded residual.

## Component Certificate

For the exact PG80 decomposition
\[
\log\mathsf F_m^{\rm lab}=\log Z_m+\Delta_m+\Theta_m,
\]
the three pieces satisfy
\[
\log Z_m
=2m\log m+C_{\rm F}m-{1\over2}\log m
+{1\over2}\log{10\pi\over3}+{53\over1440m}+O(m^{-3}),
\]
\[
\Delta_m
=\sum_j\log{c_{m,j}\over r_{m,j}}
={5\over2}\log{3\over2}-4\log{5\over4}
-{21\over160m}+O(m^{-2}),
\]
and
\[
\Theta_m
=\sum_j\log{a_{m,j}\over c_{m,j}}
={5\over4}\log m+O(1).
\]
Thus the respective logarithmic coefficients are \(-1/2\), zero, and
\(5/4\). With \(s_{m,j}=c_{m,j}+1\), the signed literal
ceiling/no-ceiling correction is instead
\[
\sum_j\log{a_{m,j}\over s_{m,j}}
=-{3\over4}\log m+O(1).
\]

## Uniform Rounding Audit

- The exact identity
  \[
  c_{m,j}={j\over2}+{j(j+1)\over2(j+8m+4)}
  \]
  reduces \(a_{m,j}-c_{m,j}\) to one of two parity-shifted sawtooths.
- For \(j\le\lfloor\sqrt m\rfloor\), the even/odd weights are respectively
  \(1+O(\delta_{m,j})\) and \(1/2+O(\delta_{m,j})\), producing
  \((3/8)\log m\) before the outer factor two.
- Between \(\sqrt m\) and \(m/2\), a jump-inclusive sum--integral lemma and
  dyadic Abel summation give mean one half with weighted error \(O(1)\). On a
  block \(j\asymp X\), the error is
  \(O(X/m+m/X^2)\), summable over all blocks.
- The bulk \(j>m/2\) is \(O(1)\) directly. Exact odd hits are impossible;
  possible even hits have total harmonic weight \(O(1)\).
- The two right endpoint factors are explicit in every class modulo five and
  each contributes \(O(m^{-1})\). The left endpoint contributes
  \(\log2+O(m^{-1})\), and column zero is the forced omitted unit factor.

## Verification

- Three independent read-only audits found no mathematical error in
  PG86--PG99; their trapezoidal, semi-open-cell, hit-range, diagnostic, and
  wording suggestions were incorporated.
- The standalone standard-library component diagnostic passes on 25 formula
  rows from \(m=3\) through \(m=262144\), including all five residues on
  four growing blocks. It imports no project helper and constructs no
  permutation, matching, or geometric object.
- On the five terminal rows \(m=262140,\ldots,262144\), the centered total
  residual lies between `1.38013609747` and `1.38112123003`. These are bounded
  floating observations, not the proof and not a convergence claim.
- Diagnostic Ruff lint, format, and compile checks pass. Broader repository
  verification passes: 49 focused and 283 complete tests. The initial
  sandboxed full-suite run retained 252 passes and 31 basetemp setup errors;
  the approved identical rerun passed all 283. A broad Ruff probe retained
  four lint and 39 format findings in unrelated pre-existing files; the new
  script's scoped Ruff checks pass and no unrelated file changed.
- Exactly five authoritative files and four new dossier files are in scope.
  Final status, complete diff, whitespace, tag, generated-cache, and basetemp
  checks pass.

## Evidence Classification And Limitations

- PG87--PG99 and \(\gamma=3/4\) are **exact asymptotic theorems**.
- The 25 diagnostic rows are **bounded numerical observations**.
- The theorem concerns the labelled PG69 count. Prior canonical injectivity
  is only a downstream cardinality interpretation, not a symmetry quotient.
- No convergence or limit-point classification of the bounded remainder,
  alternative-scaffold count, global surrogate conclusion, or geometric
  conclusion is established.

## Files In Scope

- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260718__ferrers_log_gamma/`

## Proposed Next Task

After manual review and in a fresh STRICT chat, determine whether the bounded
residual after subtracting \((3/4)\log m\) converges, has distinct limit
points, or admits another explicit finer obstruction, without extrapolating
from the finite formula table.
