# TASK_STATUS - TASK-20260717__nonlocal_middle_path_rotation / Nonlocal Middle-Path Rotation

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** analyze one fixed deterministic nonlocal reassignment of the
  middle paths in the symbolic \(n=10m+3\), \(m\ge3\), branch of the
  eight-twenty-fifths product-distance construction.
- **Outcome:** exact family-specific obstruction, with a permutation proof,
  complete distance/cut classification, all saturators, and bounded
  independent exact corroboration.

## Scope

- **In scope:** only the path assignment
  \(G_j\leftarrow P_{j+1\bmod 2m}\), with the terminal/low scaffold and every
  path orientation unchanged; exact symbolic proof for every \(m\ge3\);
  bounded exact corroboration after the family was fixed.
- **Out of scope:** every other path permutation or perturbation; cyclic-order
  enumeration; production source, public API, artifacts, schemas, verifier
  backends, certificates, or limits; geometric consequences beyond the
  already proved regular-direction upper bound.

## Verified Facts

- The required startup files, predecessor construction, and relevant task
  memory were inspected; the initial Git worktree was clean.
- Before any new direct-scoring experiment, the sole family was fixed:
  \(G_j\leftarrow P_{j+1\bmod 2m}\). Equivalently,
  \(P_k\to G_{k-1\bmod 2m}\), so \(P_0\to G_{2m-1}\).
- The resulting order is a permutation for every \(m\ge3\).
- Its exact distance-class maxima and unique unordered class maximizers are
  \[
  \begin{array}{c|c|c}
  1&T&\{d-1,4m+2\}\\
  2&n(d-1)/2&\{n,d-1\}\\
  3&(5m+2)(9m+4)/3&\{5m+2,9m+4\}\\
  \ge4&n(n-1)/4&\{n-1,n\}.
  \end{array}
  \]
- The canonical-cut maxima are
  \(C_1=(4m+1)d\), \(C_2=d(d-2)/2\), \(C_3=d^2/6\),
  \(C_4=d(d-1)/4\), \(C_5=(d^2-4)/10\), \(C_6=dn/6\), and
  \(C_{\ge4}=T/2\), with every class maximizer identified exactly.
- The full score is
  \[
  W(\widehat\sigma_m)
  ={n(d-1)\over2}
  ={(10m+3)(8m+3)\over2},
  \]
  uniquely saturated by \(\{n,d-1\}\) at distance two.
- The word \(n,2,d-1\), forced when \(P_0\) wraps into the canonical closing
  gap, is the exact obstruction. The normalized coefficient tends to
  \(2/5>8/25\), so this family is strictly worse.
- The sole standard-library all-pairs diagnostic passes on the fixed exact
  rows \(m=3,4,9,25\).

## Evidence Classification

- **Exact theorem:** permutation property, every symbolic class/cut maximum,
  uniqueness of every maximizer, exact full score, sole saturator, and
  asymptotic obstruction for all \(m\ge3\).
- **Finite exact corroboration:** independent all-pairs scoring at
  \(m=3,4,9,25\).
- **Restated prior result only:** the regular-direction geometric upper bound.
- **Not claimed:** a classification of other reassignments or a new geometric
  consequence.

## Decisions And Rationale

- The one-step cyclic reassignment is deterministic, genuinely nonlocal at
  the canonical cut, has no search parameter, and changes only the assignment
  of complete middle paths to terminal gaps.
- The symbolic proof is primary. The diagnostic is bounded corroboration and
  is not used as an all-\(m\) premise.

## Plan And Expected Delta

- Derive the exact permutation and distance-class formulas. COMPLETE.
- Add one independent standard-library all-pairs diagnostic. COMPLETE.
- Synchronize proof note, roadmap, project state, and dossier. COMPLETE.
- Run proportional verification and inspect the complete diff. COMPLETE.

## Verification

- Task-local exact diagnostic: PASS on \(m=3,4,9,25\).
- Python compilation and Ruff lint/format: PASS.
- Focused product-distance regression: 49 tests passed.
- Complete suite outside the restricted sandbox: 283 tests passed.
- Retained restricted-sandbox run: 31 setup errors, all caused by denied
  pytest temporary-directory access; no test body failed.
- Checked-artifact semantic verifier: PASS, 4 certificates and 76 local
  brackets.
- Schema-selection regression: 4 tests passed.
- UTF-8, trailing-whitespace, display-math, proof-tag, protected-scope,
  one-diagnostic, cross-source, complete-diff, and git-diff checks: PASS.
- Three independent read-only audits: PASS after correcting one symbolic
  index range and formatting the diagnostic.

## Blockers / Risks

- No blocker.
- The exact theorem is intentionally limited to the one fixed rotation.
- The four finite rows corroborate but do not prove the symbolic theorem.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact obstruction
  \(W=(10m+3)(8m+3)/2\), with sole saturator
  \(\{10m+3,8m+3\}\), coefficient \(2/5\), and all checks passing.
- **Files changed:** research/PRODUCT_DISTANCE_SURROGATE.md, start.md,
  PROJECT_KNOWLEDGE.md, research/NEXT_RESEARCH_STEPS.md, CURRENT_STATUS.md,
  and ops/TASK-20260717__nonlocal_middle_path_rotation/.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md,
  CURRENT_STATUS.md, and this dossier.
