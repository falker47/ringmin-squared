# TASK_STATUS - TASK-20260717__generic_path_terminal_gap_classification / Generic Path Terminal-Gap Classification

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** extend (PG15) to the exact distance-one and distance-two
  local placement relation for every unchanged oriented path \(P_k\) in the
  symbolic \(n=10m+3\), \(m\ge3\), scaffold.
- **Expected output:** separate triple/singleton formulas, explicit cyclic and
  boundary treatment, rigorous local-versus-bijection semantics, one bounded
  exact diagnostic, synchronized durable memory, and complete verification.

## Scope

- **In scope:** the retained scaffold, paths, orientations, threshold
  \(T=d(d-1)/2\), and constant-size local words indexed by \((m,k,j)\).
- **Out of scope:** choosing, scoring, or enumerating a complete path
  reassignment; classifying nonidentity bijections; changing production code,
  tests, APIs, artifacts, schemas, backends, certificates, or limits.

## Verified Facts

- For a triple \(0\le k\le m\), the unique local distance-two maximum in
  \(G_j\) is
  \[
  {(d+j)(d-1-2k)\over2},
  \]
  and the exact condition is \(j(d-1-2k)\le2kd\).
- Equivalently, the locally non-excluded row is
  \[
  0\le j\le\ell_k=
  \min\!\left\{2m-1,
  \left\lfloor{2kd\over d-1-2k}\right\rfloor\right\},
  \]
  while the column threshold is
  \(k\ge\lceil j(d-1)/(2(d+j))\rceil\).
- Every singleton \(m+1\le k\le2m-1\) is strictly locally non-excluded in
  every gap.
- The last nonclosing and closing triple thresholds are
  \(\lfloor(4m+1)/5\rfloor\) and
  \(\lfloor(4m+3)/5\rfloor\). The path-type transition and complete
  \(m=3\) relation are explicit.
- Local exclusion, local non-exclusion, edge extendibility,
  relation-compatible bijections, and the full \(W\le T\) condition are
  logically separate. No nonidentity bijection is selected or classified.

## Assumptions / Inferences

- None beyond the retained definitions and the stated domain \(m\ge3\).
- The four diagnostic rows are finite exact corroboration, not the all-\(m\)
  proof.

## Decisions And Rationale

- Retain the generic assignment notation only to state a conditional
  equivalence; do not choose its values.
- Include \(m=34\) in the diagnostic because \((34,11,24)\) is a
  nontrivial equality case on the exact admissible boundary.
- Treat the previously proved identity only as a separate existence witness,
  not as a newly selected or evaluated reassignment.

## Plan And Expected Delta

- Complete STRICT startup and inspect retained definitions. COMPLETE.
- Derive and independently audit the theorem. COMPLETE.
- Add the sole bounded exact diagnostic. COMPLETE.
- Synchronize proof note, stable memory, state, roadmap, and dossier. COMPLETE.
- Run diagnostic, static checks, regressions, full suite, and artifact
  verification. COMPLETE.
- Complete final scope, hygiene, and diff inspection. COMPLETE.

## Verification

- **Checks completed:** exact diagnostic; Python compilation; Ruff
  lint/format; focused product-distance regression; schema regression;
  complete suite; checked-artifact semantic verifier; independent proof/code
  audits; protected-scope and sole-diagnostic checks.
- **Observed result:** diagnostic PASS for \(m=3,4,9,34\); compilation and
  Ruff PASS; 49 focused tests, 4 schema tests, and all 283 repository tests
  PASS; 4 certificates and 76 local brackets verify.
- **Retained corrections:** the first Ruff format check required one
  mechanical reformat; an independent audit found and corrected the false
  ordering \(A_k>c_k>B_k\) to \(A_k>B_k>c_k\); a redirected pycache compile
  attempt failed under \(C:\mathrm{tmp}\), after which ordinary compilation
  passed and its generated cache was removed.
- **Final inspection:** expected nine-file scope, one diagnostic, no generated
  cache, UTF-8/delimiter delta, unique PG16--PG36 tags, complete diff, and
  final whitespace checks PASS.
- **Limitations:** finite diagnostics and repository tests corroborate but do
  not replace the exact proof or user review.

## Blockers / Risks

- No blocker.
- Residual mathematical risk is limited to ordinary human review of the exact
  proof; three independent audits agree after the recorded ordering
  correction.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact local relation and all requested automated
  and manual verification pass.
- **Files changed:** five project Markdown files plus this four-file STRICT
  dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md, then this
  dossier.
