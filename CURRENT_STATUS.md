# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** exact two-prefix extension of the first linear-block
  certificate.
- **Current task:** generalize CR28ax--CR28bg to two selected prefixes,
  verify the supplied rational witness, and derive its finite/global
  consequences without optimizing five parameters.
- **Task dossier:** `ops/TASK-20260716__two_prefix_linear_block/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- Added the exact two-prefix theorem for
  \(r_n=\lfloor\alpha n\rfloor\),
  \(s_{1,n}=\lceil\beta_1n\rceil\), and
  \(s_{2,n}=\lceil\beta_2n\rceil\), with
  \(0<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1\).
- Used exactly
  \[
  \max(0,H_1,H_2)\ge
  (\lambda_{\rm hi}-\lambda_{\rm lo})H_1+\lambda_{\rm lo}H_2.
  \]
- Added exact rational witness arithmetic, a minimal uniform floor/ceiling
  threshold, global lower corollaries, and independent test-local diagnostics.
- No production source, API, artifact, schema, example, verifier, backend,
  certificate, enumerator, or enumeration limit changed.
- No global optimization over the five two-prefix parameters was performed.

## Exact Charging Result

Let
\[
H_1=\sum_{t=s_1}^{r-1}A_t,
\qquad
H_2=\sum_{t=s_2}^{r-1}A_t.
\]
Expanding the prescribed linear form before charging gives weight
\(\lambda_{\rm hi}\) on \([s_1,r-1]\) and
\(\lambda_{\rm lo}\) on \([s_2,s_1-1]\).

- Every selected intact-base split is mapped injectively to its original base
  edge. Once split, that edge is removed and cannot be recreated with the same
  two original endpoints.
- The quadratic slack of each original base edge is therefore used exactly
  once: beside its unique selected split or in the unused nonnegative pool.
- Every recursive current edge contains a previously inserted endpoint in
  \(\{t+1,\ldots,r-1\}\), including fully nested child edges crossing the
  prefix boundary. CR28ba and \(J_{n,\lambda}\ge G_{n,\lambda}\) cover all of
  them.
- Summing two independently charged copies of CR28be is explicitly rejected:
  it would duplicate the same base-slack pool.

Consequently,
\[
\gamma^{(r)}_{1,n}
\ge P_{r,n}
+(r-s_1)G_{n,\lambda_{\rm hi}}(s_1)
+(s_1-s_2)G_{n,\lambda_{\rm lo}}(s_2).
\]

## Coefficient And Witness

The certified total coefficient is
\[
C_2=p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_{\rm hi})
+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_{\rm lo}).
\]
For
\[
(\alpha,\beta_1,\beta_2,\lambda_{\rm hi},\lambda_{\rm lo})
=\left({3\over7},{2\over5},{3\over8},{1\over2},{1\over4}\right),
\]
exact arithmetic gives
\[
p={284\over1029},
\qquad
g_{\rm hi}={52\over3675},
\qquad
g_{\rm lo}={199\over87808},
\]
\[
\boxed{C_2={72825421\over263424000}>{4+2\sqrt3\over27}.}
\]
The comparison is proved by
\[
\left({27C_2-4\over2}\right)^2-3
={12748069910521\over30840979456000000}>0.
\]

## Finite And Global Theorem

Put
\[
r_n=\left\lfloor{3n\over7}\right\rfloor,
\qquad
s_{1,n}=\left\lceil{2n\over5}\right\rceil,
\qquad
s_{2,n}=\left\lceil{3n\over8}\right\rceil.
\]
The minimal uniform threshold with both selected segments nonempty is
\(n=59\). Indeed,
\[
r_n-s_{1,n}\ge{n-58\over35},
\qquad
s_{1,n}-s_{2,n}\ge{n-35\over40},
\]
whereas \((r_{58},s_{1,58},s_{2,58})=(24,24,22)\).

For every \(n\ge59\), with the explicit rational floors \(F_{1,n},F_{2,n}\),
\[
\Lambda_n
\ge\Gamma_n^{(r_n)}
\ge\gamma^{(r_n)}_{1,n}
\ge P_{r_n,n}
+(r_n-s_{1,n})F_{1,n}
+(s_{1,n}-s_{2,n})F_{2,n}.
\]
Exact rounding gives
\[
\Lambda_n
\ge C_2n^3+{106196857\over263424000}n^2
-{1520\over1029}n-{22\over343}
\ge C_2n^3,
\]
and the strict cyclic-ratio sandwich gives
\[
R_2^*(n)>{C_2\over\pi}n^3-n^2.
\]
The separate residual lower polynomial is positive for \(n\ge327\); it is
not the exact residual or its exact coefficient.

## Independent Diagnostics

- Exhaustive \(n=59\) depth-two oracle: all 1,260 literal histories pass;
  exactly 70 have a recursive second split.
- Fully nested \(n=100\) domino: recursive child edges cross the high/low
  boundary, including edges whose two endpoints were inserted earlier.
- Deterministic intact-base and recursive policies pass at
  \(n=59,100,200,1000\).
- An explicit negative regression shows that two separately charged prefix
  inequalities overdraw an edge by exactly its base slack.
- Exact coefficient, surd comparison, threshold 58/59, finite rounding
  through \(n=1000\), and coarse residual signs at 326/327 pass using only
  test-local integer and `Fraction` arithmetic.

## Verification

- Two-prefix focused selection: 20 passed.
- Complete fixed-order-cycle-ratio module: 89 passed.
- Complete local suite: 265 passed.
- Checked-artifact verifier: all 4 certificates, 76 local brackets, and the
  \(n=3,4,5,6\) summary verified.
- Checked-artifact schema selection: 4 passed.
- Ruff on the changed test module: passed.
- Repository-wide Ruff retains exactly four known findings in untouched
  files; none belongs to this task.
- `git diff --check` and the protected-scope audit pass.
- Three independent read-only audits found no charging, arithmetic, finite,
  recursive-coverage, or test defect before final synchronization.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md`: two-prefix charging theorem,
  coefficient, witness, finite/global consequences, and limitations.
- `tests/test_fixed_order_cycle_ratio.py`: independent exact base/recursive
  diagnostics only.
- `research/ALL_N_LOWER_BOUND.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md`: synchronized authoritative consequences.
- `CURRENT_STATUS.md` and the new STRICT task dossier: durable handoff.

## Residual Limitations

- \(C_2\) is one certified rational witness, not the global optimum of the
  five two-prefix parameters.
- The residual polynomial is a lower bound, not the exact block residual.
- No convergence, exact leading coefficient, matching upper coefficient,
  production computation, artifact, or certificate claim follows.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh STRICT task, optimize the five two-prefix parameters globally,
including every boundary face, while preserving combined one-use charging and
keeping production, artifacts, schemas, and limits unchanged.
