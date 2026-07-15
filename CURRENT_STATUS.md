# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact optimization of the first-linear-block
  slack/prefix certificate.
- **Current task:** optimize CR28ax--CR28bg over the cutoff and prefix weight,
  with literal recursive linkage and one-use base-edge charging.
- **Task dossier:**
  `ops/TASK-20260715__optimize_linear_block_certificate/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- The block remains
  \[
  m=1,
  \qquad
  r_n=\lfloor(\sqrt2-1)n\rfloor.
  \]
- The former fixed choices \(s_n=\lceil2n/5\rceil\) and
  \(\max(0,H)\ge H/2\) are replaced in the certificate by
  \(s_n=\lceil\beta n\rceil\) and
  \(\max(0,H)\ge\lambda H\).
- Every split still uses a literal current edge. Each intact original base
  edge is charged at most once, and every recursive child-edge split retains
  its previously inserted endpoint.
- No production source, API, scorer, canonicalizer, enumerator, enumeration
  limit, artifact, schema, example, verifier, backend, or certificate contract
  changed.

## Exact Parameter Regions And Local Floors

- EXACT METHOD-SPECIFIC THEOREM: the proof-valid asymptotic parameter region is
  exactly
  \[
  \mathcal A=(0,\sqrt2-1)\times[0,1].
  \]
  At fixed \(n\), the exact cutoff condition is
  \[
  1\le\lceil\beta n\rceil
  \le\lfloor(\sqrt2-1)n\rfloor-1.
  \]
- EXACT METHOD-SPECIFIC THEOREM: the parameters producing a strictly positive
  cubic certificate are exactly
  \[
  {\sqrt2\over4}<\beta<\sqrt2-1,
  \qquad
  0<\lambda<{2\sqrt2\,\beta-1\over\beta^2}.
  \]
- For \(S=n+r_n\), the intact-base and recursive local floors are
  \[
  G_{n,\lambda}(t)
  ={\lambda(4St-S^2-2\lambda t^2)\over2(2-\lambda)},
  \qquad
  J_{n,\lambda}(t)
  =\lambda((S-1)t-n(r_n-1)).
  \]
  Both increase along the selected prefix, and the exact finite identity
  \[
  J_{n,\lambda}(t)-G_{n,\lambda}(t)
  ={\lambda\bigl((n-r_n)^2+4(n-t)
  +2\lambda(r_n-1-t)(n-t)\bigr)\over2(2-\lambda)}
  \]
  proves that the recursive floor is strictly larger for \(\lambda>0\) and
  every selected \(t\le r_n-1\).

## Exact Maximin Result

- EXACT TEMPLATE-OPTIMAL THEOREM: the unique maximizer is
  \[
  \beta_*={3\sqrt2\over4}-{2\over3},
  \qquad
  \lambda_*={88-48\sqrt2\over49}.
  \]
  The limiting active local floor and residual coefficient are
  \[
  g_*={68-48\sqrt2\over9},
  \qquad
  c_*={99\sqrt2-140\over27}
  \approx2.645435161633\times10^{-4}.
  \]
- The former coefficient is not optimal inside this template:
  \[
  c_*-{389-275\sqrt2\over375}
  ={14850\sqrt2-21001\over3375}>0,
  \]
  with exact square gap \(2\cdot14850^2-21001^2=2999\).
- This is template optimality only. It is not the exact residual coefficient
  of the block.

## Explicit Finite And Global Bounds

- Put
  \[
  s_n^*=\left\lceil
  \left({3\sqrt2\over4}-{2\over3}\right)n
  \right\rceil,
  \qquad
  k_n^*=r_n-s_n^*.
  \]
  With
  \[
  F_n^*=
  {\lambda_*\left(
  4(n+r_n)s_n^*-(n+r_n)^2-2\lambda_*(s_n^*)^2
  \right)\over2(2-\lambda_*)},
  \]
  the exact floor/ceiling statement is
  \[
  \gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
  \ge k_n^*F_n^*-e(n-r_n+1)
  \]
  whenever \(s_n^*\le r_n-1\), where \(e\) retains its exact parity formula.
- The simple uniform domain \(n\ge99\) is sufficient. On it,
  \[
  \gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
  \ge c_*n^3-Q_*n^2,
  \qquad
  Q_*={1097-768\sqrt2\over72}.
  \]
  This displayed bound is positive for every \(n\ge572\).
- EXACT GLOBAL LOWER COROLLARY: without a max--min exchange,
  \[
  \Lambda_n
  \ge\Gamma_n^{(r_n)}
  \ge\gamma^{(r_n)}_{1,n}
  \ge P_{r_n,n}+k_n^*F_n^*,
  \]
  and hence, for \(n\ge99\),
  \[
  \Lambda_n
  \ge {117\sqrt2-158\over27}n^3
  -{136-96\sqrt2\over9}n^2,
  \]
  \[
  R_2^*(n)
  >{117\sqrt2-158\over27\pi}n^3
  -\left(1+{136-96\sqrt2\over9\pi}\right)n^2.
  \]
  The corresponding liminf lower coefficients are
  \((117\sqrt2-158)/27\) and that value divided by \(\pi\).

## Bounded Exact Diagnostics

- VERIFIED FACT (FINITE EXACT TEST-ONLY COMPUTATION): the base-slack identity
  is still checked on every dihedral cycle of tail sizes three through six.
- Optimized deterministic histories at \(n=99,141,200,500,1000\) exercise
  intact-base and forced-recursive policies using exact
  \(\mathbb Q(\sqrt2)\) pair arithmetic.
- A separate \(n=141\) oracle exhausts all 7,140 literal depth-two histories
  from one base cycle, including all 168 recursive second splits. It checks
  connected cycle signatures, exact edge updates, one-use charging, local
  floors, signed prefixes, and the weighted-prefix objective.
- A bounded exact scan over every \(99\le n\le1000\) verifies the optimized
  floor/ceiling arithmetic and both finite polynomial bounds.
- These diagnostics call no production scorer, canonicalizer, or enumerator
  and are not the all-\(n\) proof.

## Verification

- First-linear-block focused selection: 18 passed.
- Complete fixed-order-cycle-ratio module: 66 passed.
- Complete local suite: 242 passed.
- Checked-artifact verification: all 4 certificates and 76 local brackets
  verified.
- Checked-artifact schema selection: 4 passed.
- Ruff on the changed test module: passed.
- Repository-wide Ruff retains the same four findings in untouched files.
- Git diff hygiene and the no-production/no-limit-change audit pass.
- Three independent read-only reviews found no mathematical, test-oracle, or
  synchronization defect after the recorded notation cleanup.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` contains the exact generalized proof,
  maximin solution, finite bounds, and limitations.
- `tests/test_fixed_order_cycle_ratio.py` contains only independent bounded
  exact diagnostics.
- `research/ALL_N_LOWER_BOUND.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize the stable consequence and
  roadmap.
- `CURRENT_STATUS.md` and the new STRICT task dossier record this handoff.
- No production, artifact, schema, example, verifier, or enumeration-limit
  file changed.

## Residual Limitations

- The coefficient \(c_*\) is the best certified by this template, not the
  exact residual coefficient of the selected block.
- The global and geometric coefficients are certified lower coefficients,
  not exact leading coefficients or limits.
- Neither normalized sequence is proved to converge, and no matching upper
  coefficient is known.
- Other linear densities and starting indices remain unclassified.
- Finite diagnostics corroborate arithmetic and linkage only; they are not the
  all-\(n\) proof.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh bounded task, extend the independent test-only Arb endpoint-sign
cross-check from the checked `n=3` artifact to the existing checked `n=4`
artifact without changing production verification, artifacts, schemas, or
certification claims.
