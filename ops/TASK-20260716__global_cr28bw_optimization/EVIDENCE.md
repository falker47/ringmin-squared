# EVIDENCE - Global CR28bw Optimization

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Check: startup source inspection, clean Git state, and focused regression.
- Evidence: `git status --short --branch` showed only the clean `main`
  tracking line; HEAD was
  `b121fa2e0fc4ec1b2c06f10536b82021292c40e7`;
  `python -m pytest tests\test_fixed_order_cycle_ratio.py -q` passed all 89
  tests.
- Interpretation: the STRICT task starts from an isolated verified state.

## EV-02 - Ordered Weight Reduction

- Classification: exact method-specific reduction.
- Check: differentiate each active CR28bw weight summand on `[0,1]`, prove
  strict concavity, clip its unique stationary point, and compare the two
  clipped optima using `beta_2 < beta_1`.
- Result: the order constraint is automatically satisfied and introduces no
  pooled interior branch. Six saturation/interior branch pairs remain.
- Interpretation: the ordered \(\lambda\)-problem is reduced exactly before
  any density optimization.

## EV-03 - Complete Branch, Transition, And Face Classification

- Classification: exact method-specific theorem.
- Result: after normalization by \(1+\alpha\), the fixed-\(\alpha\) global
  branch sequence is `00`, `MM`, `HM`, `HH`, with exact transitions
  \(1/3\), \(77/139\), and \(301/419\).
- Result: `M0` and `H0` are the nonwinning one-prefix strata; every density
  transition, the \(\alpha=0,1\) faces, all three density collisions, all
  ordered-weight faces, and zero-length-segment weight nonuniqueness are
  classified.
- Exact closure branch maxima:
  \[
  \left(
  {2(\sqrt2-1)\over3},
  {4+2\sqrt3\over27},
  {13\over48},
  C_{2,*},
  {59\over216},
  {13\over48}
  \right).
  \]
- Interpretation: no boundary, collision, or transition face can tie the
  interior global value.

## EV-04 - Exact Global Maximum

- Classification: exact template-optimal theorem.
- Global relaxation:
  \[
  C_2\le
  p(\alpha)+{27(3\alpha-1)^3\over1058}
  ={829\alpha^3-1887\alpha^2+1158\alpha+224\over1587}.
  \]
- Unique equality data:
  \[
  {X\over3\alpha-1}={18\over23},
  \qquad
  {Y\over3\alpha-1}={12\over23},
  \qquad
  829\alpha^2-1258\alpha+386=0.
  \]
- Exact maximizer:
  \[
  \left(
  {629-23\sqrt{143}\over829},
  {2286-77\sqrt{143}\over3316},
  {2010-59\sqrt{143}\over3316},
  {6264-288\sqrt{143}\over5281},
  {3888-192\sqrt{143}\over4273}
  \right).
  \]
- Exact coefficient:
  \[
  C_{2,*}={491596+6578\sqrt{143}\over2061723}.
  \]
- Interpretation: this is the unique maximizer in the original strict
  five-parameter domain, derived without assuming the numerical candidate.

## EV-05 - Independent Exact Arithmetic

- Classification: verified bounded exact test-local computation.
- Checks: ordered-weight rational scan; all six branch pairs; exact
  transitions; `HM`/`HH` stationary equations; the \(\alpha=1\) quartic;
  the \(\lambda_{\rm hi}=1\) face derivative identity; denominator-46
  simplex maximization; denominator-32 compact-closure scan.
- \(\mathbb Q(\sqrt{143})\) checks: strict domain inequalities, all five
  coordinate minimal polynomials, coefficient reconstruction, coefficient
  polynomial
  \(6185169z^2-2949576z+342644\), rational isolating intervals, and exact
  comparison with the prior witness.
- Pure-integer separator checks:
  \[
  143(13156000)^2-(156940819)^2=120067379609239>0,
  \]
  \[
  6931^2-3(4000)^2=38761>0,
  \qquad
  5659^2-2(4000)^2=24281>0.
  \]
- Limitation: bounded rational grids corroborate but do not replace the
  written all-real proof.

## EV-06 - Asymptotic Corollary And Finite-Scope Separation

- Classification: exact method-specific lower-bound theorem.
- Result:
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{2,*},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{2,*}\over\pi}.
  \]
- Scope distinction: no finite floor/ceiling rounding theorem was derived for
  the irrational optimizer. The rational coefficient
  \(72825421/263424000\) remains the explicit \(n\ge59\) theorem.
- Limitation: \(C_{2,*}\) is a CR28bw template optimum, not an exact block
  residual, limit, or geometric leading coefficient.

## EV-07 - Verification

- Classification: verified computation.
- `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`: 94 passed.
- `python -m pytest`: 270 passed.
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`:
  4 certificates, 76 local brackets, and the \(n=3,4,5,6\) summary verified.
- `python -m pytest tests\test_checked_artifact_schema_validation.py -q`:
  4 passed.
- `python -m ruff check tests\test_fixed_order_cycle_ratio.py`: passed.
- `python -m ruff check .`: exactly four known findings in untouched files.
- `git diff --check`: passed.
- Interpretation: all relevant focused, global, artifact, schema, style, and
  whitespace checks completed successfully.

## EV-08 - Scope And Independent Review

- Classification: verified source inspection.
- Changed scope: proof/research notes, stable memory/status/roadmap, one
  test-local module, and this dossier only.
- Protected scope: no production source, API, artifact, schema, example,
  verifier, backend, certificate, enumerator, or enumeration-limit path
  changed.
- Three independent read-only audits checked algebra, every branch and face,
  exact arithmetic, formatting, synchronization, finite/asymptotic
  distinctions, and protected scope. All reported defects were corrected;
  final audits found none remaining.
- Hosted GitHub Actions remain unverified. The user retains staging and commit
  authority.
