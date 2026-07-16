# EVIDENCE - Normalized Prefix Simplex

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Evidence: initial `git status --short` was empty; branch `main` was at
  `726c8f0`; the focused command
  `python -m pytest tests\\test_fixed_order_cycle_ratio.py -q -k "two_prefix_global or three_prefix_global_simplex or three_prefix_global_compact or first_linear_density_parameter_optimization"`
  passed 8/8.
- Interpretation: the task began from an isolated reviewed state.

## EV-02 - Exact Global Certificate

- Classification: exact theorem.
- With \(q_m=2/[3(1-M_{m-1})]\), the proof establishes
  \[
  M_k-F_k(x)=\sum_{i=1}^k(1-M_{k-i})
  (x_i-q_{k-i+1}x_{i-1})^2
  \left(x_i+{q_{k-i+1}x_{i-1}\over2}\right).
  \]
- Every summand is nonnegative, and equality forces all ratios. This proves
  global uniqueness and strict interiority, not merely stationarity.

## EV-03 - Recurrences, Monotonicity, And Limit

- Classification: exact theorem.
- Result:
  \[
  M_0=0,
  \qquad M_k={4\over27(1-M_{k-1})^2},
  \]
  \[
  r_k={2\over3},
  \qquad r_i={2\over3-r_{i+1}^2}.
  \]
- Exact monotonicity certificate:
  \[
  {4\over27(1-u)^2}-u
  ={(1-3u)^2(4-3u)\over27(1-u)^2}>0
  \quad(0\le u<1/3).
  \]
- Result: \(M_k\) is strictly increasing, stays below \(1/3\), and converges
  to \(1/3\).

## EV-04 - Exact Historical Comparison

- Classification: exact source comparison.
- Rows:
  \[
  \begin{array}{c|c|c}
  k&(x_1,\ldots,x_k)&M_k\\ \hline
  1&(2/3)&4/27\\
  2&(18/23,12/23)&108/529\\
  3&(1058/1263,276/421,184/421)&1119364/4785507
  \end{array}
  \]
- Their scale factors \(M_k/8\) are exactly
  \(1/54\), \(27/1058\), and \(279841/9571014\), matching the one-, two-,
  and three-prefix proof-note envelopes.

## EV-05 - Limiting Envelope

- Classification: exact normalized-polynomial theorem.
- On \([1/3,1]\),
  \[
  E_\infty(\alpha)
  =p(\alpha)+{(3\alpha-1)^3\over24},
  \qquad
  {1\over3}-E_\infty(\alpha)
  ={(1-\alpha)(23\alpha^2-16\alpha+5)\over24}.
  \]
- Result: the unique compact maximum is \(1/3\) at \(\alpha=1\); the strict
  domain has a nonattained supremum.
- On the limiting all-middle closure \([1/3,1/2]\), the unique maximum is
  \((434+4\sqrt2)/1587\) at \((13-2\sqrt2)/23\).
- Limitation: neither value is a certified prefix coefficient or a bound for
  \(\Lambda_n\) or \(R_2^*(n)\).

## EV-06 - Independent `Fraction` Diagnostic

- Classification: verified bounded exact computation.
- Command:
  `python -B ops\\TASK-20260716__normalized_prefix_simplex\\fraction_diagnostic.py`.
- Result: all direct-objective, recurrence, stationarity, strict-order, and
  documented-case assertions passed for \(k=1,\ldots,8\) under local Python
  3.14.3. No local Python 3.11 execution is claimed.
- Independent grid result at denominator 12:
  \[
  \left(
  {4\over27},{13\over64},{403\over1728},{1\over4},
  {151\over576},{235\over864},{161\over576},{247\over864}
  \right).
  \]
  Literal enumeration and discrete Bellman optimization agree on all eight
  values after 203,489 literal grid tuples, and every grid value is at most the
  corresponding exact \(M_k\).
- Limitation: the finite grid is a counterexample diagnostic, not the all-real
  proof; the written certificate supplies that proof.

## EV-07 - Scope

- Classification: verified source inspection.
- Intended changed scope: the cyclic-ratio proof note, research roadmap,
  and this new task dossier including its standalone diagnostic.
- `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the all-\(n\)
  proof note are intentionally unchanged under the task-specific file scope.
- Protected scope: no charging extension, new asymptotic/geometric bound,
  production source, test module, API, artifact, schema, example, verifier,
  backend, certificate, enumerator, or enumeration-limit change.

## EV-08 - Complete Verification And Review

- Classification: verified computation and source inspection.
- Results:
  - dossier-local Fraction diagnostic: passed;
  - focused historical simplex selection: 8 passed;
  - complete fixed-order-cycle-ratio module: 101 passed;
  - complete local suite: 277 passed;
  - checked artifacts: 4 certificates, 76 local brackets, and the finite
    \(n=3,4,5,6\) summary verified;
  - checked-artifact schema selection: 4 passed;
  - Ruff and `py_compile` on the diagnostic: passed;
  - 273 equation tags with no duplicate, 429/429 proof displays, 59/59
    roadmap displays, no trailing whitespace, and clean `git diff --check`.
- Three independent read-only audits found no residual defect after two
  mathematical wording clarifications and two evidence-scope clarifications
  were applied.
- Interpretation: the normalized lemma and reproducible bounded diagnostics
  are ready for manual review.
- Limitation: hosted GitHub Actions have not run these worktree changes; no
  local Python 3.11 runtime was available, so the diagnostic's executed
  environment was Python 3.14.3.
