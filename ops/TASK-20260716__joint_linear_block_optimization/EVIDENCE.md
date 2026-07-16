# EVIDENCE - Joint Linear-Block Optimization

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Check: clean startup state and focused baseline.
- Evidence: `git status --short` was empty; HEAD was `2a978f5`; the original
  fixed-order-cycle-ratio test module passed 66 tests.
- Interpretation: the task began from an isolated reviewed state, and later
  changes can be attributed to this bounded task.

## EV-02 - Exact Coefficient And Active Floor

- Classification: exact method-specific theorem.
- Definitions:
  \[
  p(\alpha)={(1-\alpha)(\alpha^2+4\alpha+1)\over6},
  \]
  \[
  g={\lambda\{4(1+\alpha)\beta-(1+\alpha)^2
                    -2\lambda\beta^2\}\over2(2-\lambda)},
  \qquad
  j=\lambda\{(1+\alpha)\beta-\alpha\}.
  \]
- Exact check:
  \[
  j-g={\lambda\{(1-\alpha)^2
              +2\lambda(\alpha-\beta)(1-\beta)\}\over2(2-\lambda)}>0.
  \]
- Result: the intact floor is active and the global certificate coefficient is
  \(C=p+(\alpha-\beta)g\).
- Limitation: this is a certified lower coefficient of one proof template,
  not an evaluation of the true residual or global optimum.

## EV-03 - Admissible And Positive Regions

- Classification: exact method-specific theorem.
- Proof-valid region:
  \(0<\alpha<1\), \(0<\beta<\alpha\), \(0\le\lambda\le1\).
- Strictly positive-residual region:
  \[
  \alpha>{1\over3},\quad {1+\alpha\over4}<\beta<\alpha,\quad
  0<\lambda\le1,\quad
  \lambda<{4(1+\alpha)\beta-(1+\alpha)^2\over2\beta^2}.
  \]
- Exact finite block conditions:
  \(2\le\lfloor\alpha n\rfloor\le n-2\) and
  \(1\le\lceil\beta n\rceil\le\lfloor\alpha n\rfloor-1\).

## EV-04 - Interior Maximum

- Classification: exact template-optimal theorem.
- Exact derivative in the weight:
  \[
  {\partial C\over\partial\lambda}
  ={(\alpha-\beta)(1+\alpha-\lambda\beta)
          (4\beta-1-\alpha-\lambda\beta)\over(2-\lambda)^2}.
  \]
- Interior reduction:
  \[
  \lambda=4-{1+\alpha\over\beta},\qquad
  \beta={9\alpha+1\over12},\qquad
  \lambda={8(3\alpha-1)\over9\alpha+1},\quad {1\over3}<\alpha<{3\over5}.
  \]
- Reduced coefficient and derivatives:
  \[
  \bar C(\alpha)={9\alpha^3-27\alpha^2+18\alpha+4\over27},
  \quad
  \bar C'={3\alpha^2-6\alpha+2\over3},
  \quad
  \bar C''=2(\alpha-1)<0.
  \]
- Unique solution:
  \[
  \alpha_*=1-{\sqrt3\over3},\quad
  \beta_*={5\over6}-{\sqrt3\over4},\quad
  \lambda_*={88-32\sqrt3\over73},\quad
  C_*={4+2\sqrt3\over27}.
  \]

## EV-05 - Boundary Closure And Uniqueness

- Classification: exact template-optimal theorem.
- For \(\alpha\le1/3\), the envelope is \(p(\alpha)\), increasing to
  \(22/81\).
- For \(\alpha\ge3/5\), the optimum lies on \(\lambda=1\), with unique
  \[
  \beta_1=\alpha+{2\over3}
       -{\sqrt{6\alpha^2+12\alpha+10}\over6};
  \]
  its envelope is strictly decreasing and starts at \(878/3375\).
- The remaining faces reduce to the pairing ceiling
  \(p_{\max}=2(\sqrt2-1)/3\), or to the explicitly smaller endpoint values
  \(1/6\) and \((-34+14\sqrt7)/27\).
- Exact positive gaps include
  \[
  C_*-{22\over81}={6\sqrt3-10\over81},\qquad
  C_*-{878\over3375}={250\sqrt3-378\over3375},
  \]
  \[
  C_*-{2(\sqrt2-1)\over3}
  ={2(11+\sqrt3-9\sqrt2)\over27}>0.
  \]
- Interpretation: no boundary ties the interior value; strict concavity then
  proves global uniqueness.

## EV-06 - Finite Rounded Form

- Classification: exact finite method-specific theorem.
- Candidate integer parameters:
  \[
  r_n^*=\lfloor(1-\sqrt3/3)n\rfloor,\qquad
  s_n^*=\lceil(5/6-\sqrt3/4)n\rceil.
  \]
- The exact block theorem is valid for every \(n\ge86\), and \(n=85\)
  fails because \(r_{85}^*=s_{85}^*=35\). For all \(n\ge90\), the proof
  follows uniformly from
  \(r_n^*-s_n^*\ge(2-\sqrt3)n/12-2>0\); the four cases 86--89 are checked
  exactly.
- Exact lower chain:
  \[
  \Lambda_n\ge\Gamma_n^{(r_n^*)}\ge\gamma_{1,n}^{(r_n^*)}
  \ge P_{r_n^*,n}+(r_n^*-s_n^*)F_n^*.
  \]
- Polynomial consequence for \(n\ge90\):
  \[
  k_n^*F_n^*-e(q_n^*)
  \ge {26-15\sqrt3\over54}n^3
      -{233-128\sqrt3\over72}n^2.
  \]
  The right-hand side is positive for every \(n\ge441\), with exact square
  gap \(15055^2-3\cdot8692^2=433\) at \(n=441\), and is negative at 440.
  Also,
  \[
  \Lambda_n\ge C_*n^3+{13\sqrt3-19\over9}n^2-2n-{1\over6}
  \ge C_*n^3.
  \]
- A bounded exact test-local sign audit verifies
  \(k_n^*F_n^*-e(q_n^*)>0\) for every \(176\le n\le440\) and verifies
  failure at \(n=175\). The exact residual polynomial above is positive
  for every \(n\ge441\), so together these establish the 175/176 sign
  transition without treating the finite diagnostic as the all-\(n\) proof.

## EV-07 - Verification

- Classification: verified computation and source inspection.
- Commands and results:
  - `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`: 69 passed.
  - `python -m pytest`: 245 passed.
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`:
    4 certificates, 76 local brackets, and the `n=3,4,5,6` summary verified.
  - `python -m pytest tests\test_checked_artifact_schema_validation.py -q`:
    4 passed.
  - `python -m ruff check tests\test_fixed_order_cycle_ratio.py`: passed.
  - `python -m ruff check .`: four known findings, all in untouched files.
  - `git status --short`, `git diff`, `git diff --check`, and changed-path
    inspection: clean whitespace and requested protected scope.
- Three independent read-only reviews checked the symbolic reduction, all
  boundary regimes, finite thresholds, exact test arithmetic, source
  synchronization, and file scope. Their findings were corrected before a
  final no-defect review.
- Interpretation: the requested method-specific result and its reproducible
  bounded diagnostics are ready for manual review.
- Limitation: hosted GitHub Actions have not run these worktree changes, and
  the user retains all staging and commit authority.
