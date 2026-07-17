# TASK_STATUS - TASK-20260717__local_edge_extendibility_classification / Local Edge Extendibility Classification

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** classify exactly which edges of the established local
  path-to-gap relation \(\mathcal R_{\rm loc}\) for
  \(n=10m+3\), \(m\ge3\), belong to at least one relation-compatible
  bijection.
- **Expected output:** an exact Hall/Ferrers theorem, explicit interval-shift
  bijections for \(j<k\), \(j=k\), and \(j>k\), complete boundary treatment,
  one bounded exact diagnostic, synchronized durable memory, and complete
  verification.

## Scope

- **In scope:** the proved relation (PG31), residual Hall conditions, Ferrers
  row/column structure, deterministic matching witnesses, triple/singleton
  transitions, the terminal singleton, minimum parameter, and cyclic closing
  column.
- **Out of scope:** enumerating path permutations or all compatible
  bijections; scoring any distance-at-least-three pair; proving
  \(W(\sigma_\alpha)\le T\) for a nonidentity shift; geometric consequences;
  production code, tests, APIs, artifacts, schemas, backends, certificates,
  or enumeration limits.

## Verified Facts

- With \(v=2m\), the complete local relation is Ferrers:
  \[
  (k,j)\in\mathcal R_{\rm loc}
  \quad\Longleftrightarrow\quad
  k\ge\kappa_j,
  \qquad
  \kappa_j=\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
  \]
- The thresholds are nondecreasing and satisfy
  \(\kappa_0=0\), \(\kappa_1=1\), and
  \(1\le\kappa_r\le r-1\) for \(2\le r\le v-1\).
- Residual Hall after fixing a local edge \((k,j)\) is equivalent to
  \[
  \kappa_r+\mathbf1_{\{k\ge\kappa_r\}}
  \le r+\mathbf1_{\{j>r\}}
  \qquad(r\ne j).
  \]
- The candidate is true:
  \[
  \mathcal R_{\rm ext}
  =\{(0,0)\}\cup
  \{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
  \]
  Forcing \((k,0)\), \(k>0\), leaves the residual suffix of \(v-1\) gaps
  with only \(v-2\) neighbors. Every positive-column local edge has an
  explicit one-interval-shift completion.
- The bounded exact diagnostic passes at \(m=3,4,9,34\), directly checking
  22, 42, 234, and 3547 constructed witnesses, respectively. The local-edge
  counts are 27, 49, 251, and 3614; the differences \(5,7,17,67\) are exactly
  the nonextendible zero-column edges.

## Assumptions / Inferences

- The already proved exact local relation is fixed input.
- The finite diagnostic corroborates the constructions and Hall arithmetic;
  it is not the all-\(m\) proof.

## Decisions And Rationale

- Use the nested column neighborhoods to state and prove residual Hall
  exactly, rather than relying only on the visible degree-one obstruction.
- Supply deterministic shifts as constructive witnesses even though Hall
  already proves existence.
- Keep the closing-gap local condition inside \(\mathcal R_{\rm loc}\); the
  matching shifts themselves never wrap the canonical cut.
- Add one task-local standard-library diagnostic and no production or test
  helper.

## Plan And Expected Delta

- Complete STRICT startup and inspect predecessor definitions. COMPLETE.
- Derive and independently audit Hall and shift constructions. COMPLETE.
- Record the proof and sole bounded diagnostic. COMPLETE.
- Synchronize stable memory, current state, and roadmap. COMPLETE.
- Run static checks, regressions, artifact verification, independent audits,
  and final diff inspection. COMPLETE.

## Verification

- **Checks completed:** exact diagnostic; in-memory Python compilation; Ruff
  lint/format; focused product-distance regression; isolated provenance
  regression; schema regression; complete suite; checked-artifact semantic
  verification; three independent proof/code/scope audits; expected-path,
  one-diagnostic, encoding, tag, cache, full-diff, and whitespace checks.
- **Observed result:** diagnostic PASS for \(m=3,4,9,34\); syntax and Ruff
  PASS; 49 focused tests, 1 isolated provenance test, 4 schema tests, and all
  283 repository tests PASS; 4 certificates and 76 local brackets verify.
  PG37--PG49 and the nine-file scope pass independent audit.
- **Retained failed check:** the first complete-suite run was concurrent with
  other provenance-aware commands and returned 282 PASS / 1 FAIL because the
  regenerated summary transiently observed `git_commit=null`. The failed test
  passed immediately in isolation, and the serial complete-suite rerun passed
  all 283 tests.
- **Limitations:** finite checks do not replace the symbolic theorem or user
  review.

## Blockers / Risks

- No blocker.
- Residual mathematical risk is limited to ordinary human review. The audits
  explicitly checked gap-to-path direction, path zero, closure, and the
  separation from full-distance feasibility.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the exact theorem, deterministic constructions,
  repository regressions, checked artifacts, independent audits, and final
  hygiene checks pass.
- **Files changed:** research/PRODUCT_DISTANCE_SURROGATE.md,
  research/NEXT_RESEARCH_STEPS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, and the four files in this STRICT dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md, then this
  dossier.
