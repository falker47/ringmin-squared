# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** joint exact optimization of the generalized first-linear-block certificate.
- **Current task:** generalize CR28ax--CR28bg to
  \(r_n=\lfloor\alpha n\rfloor\) and solve the maximin in
  \((\alpha,\beta,\lambda)\), including finite rounding and every boundary.
- **Task dossier:**
  `ops/TASK-20260716__joint_linear_block_optimization/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- The certificate keeps \(m=1\) and now uses
  \[
  r_n=\lfloor\alpha n\rfloor,\qquad
  s_n=\lceil\beta n\rceil,\qquad
  \max(0,H)\ge\lambda H.
  \]
- Every split remains a literal current-edge split; intact original edges are
  charged at most once and recursive child-edge splits retain their inserted
  endpoint.
- No production source, API, artifact, schema, example, verifier, backend,
  enumerator, or enumeration limit changed.

## Exact Joint Certificate

- EXACT METHOD-SPECIFIC THEOREM: the proof-valid asymptotic region is
  \[
  0<\alpha<1,\qquad 0<\beta<\alpha,\qquad 0\le\lambda\le1.
  \]
  At fixed \(n\), the exact block conditions are
  \[
  2\le\lfloor\alpha n\rfloor\le n-2,\qquad
  1\le\lceil\beta n\rceil\le\lfloor\alpha n\rfloor-1.
  \]
- With
  \[
  p(\alpha)={(1-\alpha)(\alpha^2+4\alpha+1)\over6},
  \]
  the intact and recursive limiting local floors are
  \[
  g={\lambda\{4(1+\alpha)\beta-(1+\alpha)^2
                    -2\lambda\beta^2\}\over2(2-\lambda)},
  \qquad
  j=\lambda\{(1+\alpha)\beta-\alpha\}.
  \]
  Exact subtraction gives
  \[
  j-g={\lambda\{(1-\alpha)^2
              +2\lambda(\alpha-\beta)(1-\beta)\}\over2(2-\lambda)}>0
  \]
  whenever \(\lambda>0\). Thus \(g\), not \(j\), is always active.
- The global method coefficient is exactly
  \[
  C(\alpha,\beta,\lambda)
  =p(\alpha)+(\alpha-\beta)g(\alpha,\beta,\lambda).
  \]
- The strictly positive-residual region is exactly
  \[
  \alpha>{1\over3},\qquad
  {1+\alpha\over4}<\beta<\alpha,\qquad
  0<\lambda\le1,\qquad
  \lambda<{4(1+\alpha)\beta-(1+\alpha)^2\over2\beta^2}.
  \]

## Exact Maximin And Boundary Closure

- EXACT TEMPLATE-OPTIMAL THEOREM: the unique global maximizer is
  \[
  \alpha_*=1-{\sqrt3\over3},\qquad
  \beta_*={5\over6}-{\sqrt3\over4},\qquad
  \lambda_*={88-32\sqrt3\over73},
  \]
  and the candidate in the task statement is therefore confirmed.
- At that point,
  \[
  g_*={14-8\sqrt3\over9},\qquad
  (\alpha_*-\beta_*)g_*={26-15\sqrt3\over54},
  \]
  \[
  p(\alpha_*)={19\sqrt3-18\over54},\qquad
  C_*={4+2\sqrt3\over27}.
  \]
- For fixed \((\alpha,\beta)\), exact differentiation reduces the optimum in
  \(\lambda\) to \(0\), \(1\), or
  \(4-(1+\alpha)/\beta\). On the interior branch the unique cutoff is
  \(\beta=(9\alpha+1)/12\), and the reduced coefficient is strictly concave
  on \(1/3<\alpha<3/5\), with its unique stationary point at \(\alpha_*\).
- The faces \(\alpha\le1/3\), \(\alpha\ge3/5\), \(\lambda=0\),
  \(\lambda=1\), \(\beta=0\), \(\beta=\alpha\), \(g=0\), \(\alpha=0\),
  and \(\alpha=1\) are all explicitly evaluated or monotonically reduced.
  Every one is strictly below \(C_*\); hence there is no omitted boundary
  maximizer and global uniqueness is literal.

## Explicit Finite And Global Bounds

- Put
  \[
  r_n^*=\left\lfloor\left(1-{\sqrt3\over3}\right)n\right\rfloor,
  \qquad
  s_n^*=\left\lceil\left({5\over6}-{\sqrt3\over4}\right)n\right\rceil,
  \]
  \[
  F_n^*={\lambda_*\{4(n+r_n^*)s_n^*-(n+r_n^*)^2
                         -2\lambda_*(s_n^*)^2\}\over2(2-\lambda_*)}.
  \]
  The exact floor/ceiling theorem is uniform for every \(n\ge86\):
  \[
  \Lambda_n\ge\Gamma_n^{(r_n^*)}
  \ge\gamma_{1,n}^{(r_n^*)}
  \ge P_{r_n^*,n}+(r_n^*-s_n^*)F_n^*.
  \]
  The threshold \(86\) is minimal for the stated uniform block conditions;
  \(n=85\) has \(r_n^*=s_n^*=35\).
- With the exact parity term \(e(q)\) from CR28bh,
  \[
  \gamma_{1,n}^{(r_n^*)}-P^*_{r_n^*,n}
  \ge(r_n^*-s_n^*)F_n^*-e(n-r_n^*+1).
  \]
  For every \(n\ge90\), a simpler rounded polynomial bound is
  \[
  \gamma_{1,n}^{(r_n^*)}-P^*_{r_n^*,n}
  \ge {26-15\sqrt3\over54}n^3
      -{233-128\sqrt3\over72}n^2.
  \]
  This lower bound is positive from \(n=441\). Separately, the bounded exact
  diagnostic checks the sharper floor/ceil expression on \(176\le n\le440\)
  (and its failure at 175), while the coarse theorem covers every
  \(n\ge441\). Thus its exact sign transition is 175/176. This positivity
  threshold is not a new certificate domain.
- Combining the rounded pairing and residual terms gives, for \(n\ge90\),
  \[
  \Lambda_n\ge {4+2\sqrt3\over27}n^3
    +{13\sqrt3-19\over9}n^2-2n-{1\over6}
  \ge {4+2\sqrt3\over27}n^3,
  \]
  and
  \[
  R_2^*(n)>{4+2\sqrt3\over27\pi}n^3
  +\left({13\sqrt3-19\over9\pi}-1\right)n^2
  -{2n\over\pi}-{1\over6\pi}
  >{4+2\sqrt3\over27\pi}n^3-n^2.
  \]

## Bounded Exact Diagnostics

- The base-slack identity remains checked on every dihedral cycle of tail
  sizes three through six.
- Candidate histories at \(n=86,90,141,200,500,1000\) use exact
  \(\mathbb Q(\sqrt3)\) arithmetic and exercise intact and recursive splits.
- A separate \(n=141\) oracle exhausts all 6,972 literal depth-two histories,
  including all 166 recursive second splits, checking cycle linkage, edge
  updates, one-use charging, local floors, signed prefixes, and the weighted
  objective without production scorers or enumerators.
- An exact scan over every \(86\le n\le1000\) checks floor/ceil arithmetic,
  the minimal admissibility threshold, and both polynomial estimates.
- These are independent bounded diagnostics, not the all-\(n\) proof.

## Verification

- Complete fixed-order-cycle-ratio module: 69 passed.
- Complete local suite: 245 passed.
- Checked-artifact verifier: all 4 certificates, 76 local brackets, and the
  \(n=3,4,5,6\) summary verified.
- Checked-artifact schema selection: 4 passed.
- Ruff on the changed test module: passed.
- Repository-wide Ruff retains exactly four known findings in untouched
  files; no Ruff finding belongs to this task's diff.
- Final status, diff, whitespace, and protected-scope audits pass.
- Three independent read-only reviews checked the algebra, all boundary
  branches, finite rounding, test independence, synchronization, and scope.
  Their findings were corrected and the final reviews report no remaining
  defect.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md`: generalized algebra, admissible
  region, exact maximin, full boundary proof, finite theorem, limitations.
- `tests/test_fixed_order_cycle_ratio.py`: bounded independent exact
  \(\mathbb Q(\sqrt3)\) diagnostics only.
- `research/ALL_N_LOWER_BOUND.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md`: synchronized authoritative consequences.
- `CURRENT_STATUS.md` and the new STRICT task dossier: durable handoff.
- No production, artifact, schema, example, verifier, or limit file changed.

## Residual Limitations

- \((26-15\sqrt3)/54\) is a certified residual lower coefficient inside this
  template, not the exact residual coefficient of the selected block.
- \(C_*\) and \(C_*/\pi\) are method-specific lower coefficients, not exact
  leading constants or limits.
- No convergence, matching upper coefficient, or exact geometric constant is
  proved. Finite diagnostics corroborate arithmetic and linkage only.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh bounded task, extend the independent test-only Arb endpoint-sign
cross-check from the checked `n=3` artifact to the existing checked `n=4`
artifact without changing production verification, artifacts, schemas, or
certification claims.
