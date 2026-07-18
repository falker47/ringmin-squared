# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** derive the leading asymptotics of the exact labelled PG69
  Ferrers count.
- **Repository state at startup:** clean `main` worktree at commit
  `3472b47e2f10e721b44c504ce3db9355e89ceac6`, tracking `origin/main`.
- **Implementation state:** the symbolic proof, explicit all-\(m\) remainder
  envelope, ceiling/singularity/endpoint/transition audit, standalone
  diagnostic, authoritative synchronization, complete regressions, and
  independent audits are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Starting only from
\[
\mathsf F_m^{\rm lab}
=\prod_{j=1}^{2m-1}
\left(
j+1-
\left\lceil{j(8m+3)\over2(8m+4+j)}\right\rceil
\right),
\]
verify or correct the proposed linear coefficient in
\(\log\mathsf F_m^{\rm lab}\), with a rigorous error term for every
\(m\ge3\). The exact ceiling, \(j/m\to0\) singularity, forced and terminal
columns, and dual triple/singleton transition are in scope. Permutation and
matching enumeration, production code, tests, artifacts, schemas,
alternative scaffolds, global optimization, and geometry are out of scope.

## Exact Theorem

Put
\[
C_{\rm F}=14\log2+6\log3-10\log5-2.
\]
For every integer \(m\ge3\),
\[
\boxed{
1+\log{5\over6}-\log m
<
\log\mathsf F_m^{\rm lab}-(2m\log m+C_{\rm F}m)
<
{9\over4}+\log\bigl(2m(2m+1)\bigr).
}
\]
Consequently the proposed formula is correct:
\[
\boxed{
\log\mathsf F_m^{\rm lab}
=2m\log m
+(14\log2+6\log3-10\log5-2)m
+O(\log m).
}
\]

## Proof Certificate

For \(1\le j\le2m-1\), let \(h_{m,j}\) be the rational inside the ceiling,
\(a_{m,j}=j+1-\lceil h_{m,j}\rceil\), and
\[
c_{m,j}=j-h_{m,j},
\qquad
s_{m,j}=c_{m,j}+1,
\qquad
r_{m,j}={j(j+4m)\over j+8m}.
\]

- Exact integer rounding gives
  \(a_{m,j}=1+\lfloor c_{m,j}\rfloor\) and
  \(c_{m,j}<a_{m,j}\le s_{m,j}\), including cutoff equality.
- The literal no-ceiling product uses \(s_{m,j}\), and
  \[
  0\le\sum_j\log s_{m,j}-\log\mathsf F_m^{\rm lab}
  <\log(m(2m+1)).
  \]
  This direct ceiling delta has the opposite sign from the positive
  lower-comparator correction and is only bounded at logarithmic scale.
- The homogeneous perturbation satisfies
  \(0<\sum_j\log(c_{m,j}/r_{m,j})<5/4\).
- Its exact product is
  \[
  Z_m=\prod_{j=1}^{2m-1}r_{m,j}
  ={(2m-1)!(6m-1)!(8m)!\over(4m)!(10m-1)!}.
  \]
  This isolates the complete \(\log(j/m)\) singularity. Monotone integral
  bounds, not a nonuniform endpoint expansion, yield the displayed theorem.

## Endpoint And Transition Audit

- Column zero is the forced unit factor and is correctly omitted from the
  homogeneous comparison, where the corresponding factor would vanish.
- Column one has \(\kappa_1=1\) and exact factor one.
- The final thresholds remain exactly
  \(\lfloor(4m+1)/5\rfloor\) and \(\lfloor(4m+3)/5\rfloor\), covering every
  residue class.
- The first universal row is itself a triple row throughout \(m\ge3\) and is
  not the triple/singleton boundary. At the actual boundary
  \(\ell_m=2m-1\), so the final triple contributes \(m\), while the singleton
  block contributes exactly \((m-1)!\), namely the factors
  \(m-1,\ldots,1\).

## Verification

- The standalone standard-library diagnostic evaluates direct exact ceiling
  factors on thirteen rows from \(m=3\) through \(m=262144\), including all
  five terminal residue classes and geometric growth.
- It checks exact endpoint formulas, the dual triple/singleton product,
  separate ceiling and comparator envelopes, and the all-\(m\) residual
  bounds without importing project helpers or enumerating permutations or
  matchings.
- The observed residual rises from `2.38777979993` at \(m=3\) to
  `10.7381128464` at \(m=262144\), while the estimated linear coefficient
  moves to `-1.79860390184`; these are bounded numerical observations, not a
  finer asymptotic theorem.
- The predecessor Ryser oracle, compile, Ruff lint/format, 49 focused tests,
  complete 283-test suite, four schema tests, and checked-artifact verifier
  all pass. Three independent audits found no mathematical error and their
  finite-scope and clarity findings were incorporated.
- The first full-suite run retained 252 passes and 31 sandbox setup errors
  from denied access to its isolated `C:\tmp` basetemp; the approved rerun of
  the same suite passed all 283 tests. Generated cache and formatting findings
  were removed before final inspection.

## Evidence Classification And Limitations

- The residual envelope and asymptotic formula are **exact theorems** for all
  \(m\ge3\).
- The diagnostic rows are **bounded numerical observations** that
  corroborate but do not prove or sharpen the theorem.
- The theorem concerns the labelled count. Prior canonical injectivity only
  gives the equal cardinality of the represented image; it is not a symmetry
  quotient and is not used in the proof.
- No coefficient of a finer \(\log m\) term, alternative-scaffold count,
  global surrogate conclusion, or geometric conclusion is established.

## Files In Scope

- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260718__ferrers_log_asymptotics/`

## Proposed Next Task

After manual review and in a fresh STRICT chat, determine whether the direct
ceiling correction has a precise logarithmic coefficient and whether PG85
can be sharpened to
\(2m\log m+C_{\rm F}m+\gamma\log m+O(1)\), without extrapolating the bounded
residual table.
