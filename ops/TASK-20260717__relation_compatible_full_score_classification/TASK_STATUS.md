# TASK_STATUS - TASK-20260717__relation_compatible_full_score_classification / Relation-Compatible Full-Score Classification

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine whether every relation-compatible path-to-gap
  bijection on the symbolic \(n=10m+3\), \(m\ge3\), scaffold has full
  product-distance score \(T\), treating the bijection as arbitrary.
- **Expected output:** a complete symbolic distance-three classification,
  exact full-score theorem or counterexample, one polynomial local diagnostic,
  synchronized proof note and durable memory, and complete verification.

## Scope

- **In scope:** arbitrary path-to-gap bijections, the established Ferrers
  relation (PG31)/(PG36), every triple/singleton distance-three type, all four
  gap transitions, cyclic closure, the universal long-distance bound, exact
  optimality within the product-distance surrogate, and PG49 support.
- **Out of scope:** enumerating path permutations or matchings; changing
  production code, tests, enumeration limits, artifacts, schemas, interval
  backends, certificates, CLIs, or configuration; claiming a geometric
  optimum.

## Verified Facts

- The startup worktree was clean at commit
  \(9664e342964e27c36b8e203f0dc646c811c66409\).
- The predecessor theorems PG31, PG36, and PG49 are fixed inputs.
- Independent symbolic derivations agree that the candidate distance-three
  bound is true, sharp, and valid even without relation-compatibility.
- The exhaustive symbolic lists contain six starts for every triple gap and
  four for every singleton gap, totaling the core length \(10m+2\).
- For every bijection,
  \[
  W^{(=3)}(\sigma_\alpha)\le {n(5m+2)\over3}<T,
  \qquad
  W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha).
  \]
  The first bound is sharp exactly when \(P_m\) lies in \(G_{2m-2}\) or
  \(G_{2m-1}\).
- Relation-compatibility is equivalent to \(W(\sigma_\alpha)=T=W_n\), and
  \(\mathcal R_{\rm full}=\mathcal R_{\rm ext}\) as given by PG49.

## Assumptions / Inferences

- Paths retain their displayed orientations and only their gap assignment is
  changed, exactly as in PG1--PG2.
- Finite diagnostic rows corroborate but do not prove the all-\(m\) result.

## Decisions And Rationale

- Classify distance-three pairs by their forward start in each expanded gap;
  the count then proves exhaustiveness.
- Scan local path/path-transition types polynomially and construct only the
  two explicit sharp PG46 witnesses; do not enumerate bijections.
- Keep full surrogate optimality separate from geometric feasibility.

## Plan And Expected Delta

- Complete STRICT startup and independent derivations. COMPLETE.
- Record the exact symbolic theorem and create the sole diagnostic. COMPLETE.
- Synchronize proof note, project memory, current state, and roadmap. COMPLETE.
- Run focused and complete verification plus independent audits. COMPLETE.

## Verification

- **Checks:** polynomial exact diagnostic; in-memory compilation; Ruff
  lint/format; focused and complete pytest regressions; schema regression;
  checked-artifact semantic verification; three independent proof/code/scope
  audits; expected-path, tag, encoding, cache, full-diff, and whitespace
  inspection.
- **Observed result:** diagnostic PASS for \(m=3,4,9,34\); compile and Ruff
  PASS after one retained initial format-check failure and mechanical reformat;
  49 focused tests, all 283 repository tests, and 4 schema tests PASS; 4
  certificates and 76 local brackets verify; all three audits and final
  hygiene pass on the exact nine-file scope.
- **Limitations:** finite rows cannot replace the all-\(m\) proof or user
  review.

## Blockers / Risks

- No blocker.
- Residual risk is ordinary human review. The theorem is symbolic; finite
  diagnostics do not replace its proof.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the exact arbitrary-bijection theorem, sharpness,
  full-optimal equivalence, PG49 support identity, regressions, artifact
  checks, independent audits, and final hygiene all pass.
- **Files changed:** research/PRODUCT_DISTANCE_SURROGATE.md,
  research/NEXT_RESEARCH_STEPS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, and the four files in this dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md, then this
  dossier.
