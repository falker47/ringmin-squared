# EVIDENCE - Three-Prefix Linear Block

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Check: startup source inspection, clean Git state, and focused regression.
- Evidence: `git status --short --branch` showed only the clean `main`
  tracking line; HEAD was `ebc4f6f`; the focused test module passed all 94
  tests.
- Interpretation: the STRICT task starts from an isolated verified state.

## EV-02 - Single-Use Charging And Recursive Coverage

- Classification: exact method-specific theorem.
- Check: expand the three-height ordered linear form before partitioning the
  base-slack identity.
- Result: each original edge slack has multiplicity at most one across all
  three selected segments. Every recursive edge contains a previously
  inserted label, including nested edges across both boundaries and edges with
  two inserted endpoints.
- Invalid route excluded: three separately slack-charged copies overdraw one
  reused edge by twice its slack.

## EV-03 - Exact Ordered-Weight Reduction

- Classification: exact method-specific reduction.
- Check: differentiate each active summand, clip its unique individual optimum
  to \([0,1]\), and use monotonicity in the ordered cutoffs.
- Result: the three individual optima already satisfy
  \(0\le\lambda_3\le\lambda_2\le\lambda_1\le1\); there is no pooled KKT
  branch. All ten clipped regimes and every collision face are covered.

## EV-04 - Compact-Closure Optimum

- Classification: exact template-optimal theorem.
- Exact normalized point:
  \[
  \left({X_1\over A},{X_2\over A},{X_3\over A}\right)
  =
  \left({1058\over1263},{276\over421},{184\over421}\right).
  \]
- Exact density and coefficient:
  \[
  \alpha_*={685623-421\sqrt{377823}\over993423},
  \qquad
  C_{3,*}
  ={753972193324+106042322\sqrt{377823}\over2960667770787}.
  \]
- The second critical density is a local minimum; both compact endpoints are
  strictly smaller. At the maximizing point all three densities and weights
  are strictly ordered in the middle clipped branch, so the global upper
  envelope is attained uniquely.
- Exact extension of the strict two-prefix optimizer gives
  \(C_{3,*}>C_{2,*}\).

## EV-05 - Independent Exact Arithmetic

- Classification: verified bounded exact test-local computation.
- A bounded oracle checks all 46,620 depth-three histories, with 70 distinct
  recursive second-step prefixes (2,590 complete-history occurrences), 4,970
  recursive third splits, and 70 fully nested third splits.
- Exact rational grids check the ordered-weight region, ten clipped regimes,
  compact closure, and the three-term nonnegative simplex factorization.
- Test-local \(\mathbb Q(\sqrt{377823})\) arithmetic verifies the strict
  domain, coefficient reconstruction, coefficient equation
  \[
  79938029811249z^2-40714498439496z+5145490327924=0,
  \]
  rational isolating interval, and strict comparison with \(C_{2,*}\).
- Limitation: bounded computations corroborate but do not replace the written
  all-real proof.

## EV-06 - Asymptotic Corollary And Scope

- Classification: exact method-specific lower-bound theorem.
- Result:
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{3,*},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{3,*}\over\pi}.
  \]
- No finite floor/ceiling rounding theorem was derived. The rational
  two-prefix witness remains the explicit finite theorem from \(n=59\).
- No exact residual, convergence, exact leading coefficient, production,
  artifact, or certificate claim follows.

## EV-07 - Verification And Final Review

- Classification: verified computation and source inspection.
- Results: focused three-prefix selection 7 passed; fixed-cycle module 101
  passed; full suite 277 passed; checked-artifact verifier passed 4
  certificates and 76 brackets; schema selection 4 passed; changed-test Ruff
  passed.
- Repository-wide Ruff reports the same four known findings in untouched
  files. Final git diff --check, equation-tag uniqueness, delimiter-delta
  check, changed-path inspection, and protected-scope audit pass.
- Three independent read-only audits checked algebra, compact closure,
  charging, recursive histories, exact arithmetic, synchronization, and
  scope. Two wording ambiguities were corrected; no substantive defect
  remained.
- Failed-check evidence: an audit full-suite process overlapped an in-progress
  variable rename and observed two transient `NameError` failures against the
  partially patched test file. After the atomic rename completed, stable
  reruns passed 8 focused checks, 101 module tests, and the complete 277-test
  suite. The failure was a concurrent intermediate-state race and is not
  reproducible on the final diff.
- Hosted GitHub Actions remain unverified. The user retains all staging and
  commit authority.
