# TASK_STATUS - TASK-20260718__ferrers_bijection_count / Ferrers Bijection Count

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** derive the exact symbolic number of relation-compatible
  path-to-gap bijections on the \(n=10m+3\), \(m\ge3\), scaffold directly
  from the PG49 Ferrers support, and prove that these are exactly the
  full-optimal scaffold bijections classified by PG50--PG63.
- **Expected output:** a non-enumerative permanent recurrence and exact
  formula, complete boundary and symmetry conventions, one bounded
  independent standard-library diagnostic, synchronized authoritative notes,
  and a STRICT dossier.

## Scope

- **In scope:** the retained indexed gaps and oriented paths, PG26/PG31/PG36,
  PG38--PG40, PG49, PG50--PG63, perfect matchings of the nested Ferrers board,
  labelled versus dihedral counting, all symbolic endpoints and the minimum
  parameter, and one small exact diagnostic.
- **Out of scope:** permutation or matching enumeration; alternative
  scaffolds; geometric consequences; production code, tests, artifacts,
  schemas, backends, certificates, CLIs, or enumeration limits; asymptotics
  of the new count.

## Verified Facts

- Startup found a clean `main` worktree at
  `b1a4054d1fac75443cf1929921dddb38f9750a5f`, tracking `origin/main`.
- PG49 forces \((0,0)\); after deleting row and column zero, the support is
  \(k\ge\kappa_j\) for \(1\le j,k<2m\), with nested gap neighborhoods.
- Processing columns from \(2m-1\) down to \(1\) leaves exactly
  \(j+1-\kappa_j\) choices at column \(j\), independently of the later
  choices.
- The resulting exact labelled count is
  \[
  \mathsf F_m^{\rm lab}
  =\prod_{j=1}^{2m-1}
  \left(
  j+1-
  \left\lceil{j(8m+3)\over2(8m+4+j)}\right\rceil
  \right).
  \]
- The dual row form is
  \[
  \mathsf F_m^{\rm lab}
  =(m-1)!\prod_{k=1}^{m}(\ell_k-k+1),
  \]
  equivalently
  \((2m-q_m)!\prod_{k=1}^{q_m-1}(\ell_k-k+1)\), where
  \(q_m=\lfloor(4m+3)/5\rfloor\).
- PG36 and PG62 identify the perfect matchings counted with exactly all
  relation-compatible, equivalently full-optimal, bijections in the fixed
  scaffold.
- The formula is a labelled count. Distinct assignments have distinct
  canonical dihedral representatives rooted at \(n\) with neighbors
  \(2<3\), so the integer also equals the number of represented dihedral
  classes by injectivity; no symmetry factor is removed.
- The minimum row has
  \((\kappa_0,\ldots,\kappa_5)=(0,1,1,2,2,3)\) and
  \(\mathsf F_3^{\rm lab}=36\).

## Assumptions / Inferences

- PG26, PG36, PG39--PG40, PG49, and PG62 are used as retained exact theorems.
- The finite diagnostic corroborates but does not prove the symbolic
  all-\(m\) formula.

## Decisions And Rationale

- Count perfect matchings, not PG49 support edges.
- Use the nested-column recurrence for the proof and record the dual row
  product as an exact cross-formulation.
- Use Ryser inclusion--exclusion over column subsets as the independent
  bounded oracle; enumerate no path permutation or matching.
- State labelled counting as primary and prove dihedral-class injectivity
  separately, rather than dividing by a presumed symmetry factor.

## Plan And Expected Delta

- Complete STRICT startup and reconstruct the retained Ferrers/full-score
  theorems. COMPLETE.
- Derive and independently audit the exact permanent formulas and all
  boundaries. COMPLETE.
- Add PG64--PG73 and the sole bounded diagnostic. COMPLETE.
- Synchronize authoritative project notes and dossier. COMPLETE.
- Run focused and complete verification, inspect the full diff, and close at
  READY_FOR_REVIEW. COMPLETE.

## Verification

- **Checks:** exact diagnostic on \(m=3,\ldots,8\); in-memory compilation;
  Ruff lint/format; 49 focused and 283 complete pytest regressions; four schema
  tests; checked-artifact semantic verification; three independent proof,
  code, and synchronization audits; encoding, tag, cache, expected-path,
  complete-diff, and whitespace inspection.
- **Observed result:** Ryser, both Ferrers products, and fixed expected
  integers agree at
  \(36,720,21600,725760,46448640,3292047360\); static checks, all tests,
  artifacts, audits, and final hygiene pass. One initial Ruff format failure
  and one row/column wording correction are retained in the evidence.
- **Limitations:** finite diagnostic rows cannot replace the all-\(m\) proof
  or user review.

## Blockers / Risks

- No blocker.
- Residual risk is ordinary human review. The theorem is symbolic and the
  finite diagnostic does not replace it.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the exact symbolic products, class identity,
  bounded Ryser oracle, complete regressions, independent audits, and final
  hygiene checks pass.
- **Files changed:** research/PRODUCT_DISTANCE_SURROGATE.md,
  research/NEXT_RESEARCH_STEPS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, and the four files in this task dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md, then this
  dossier.
