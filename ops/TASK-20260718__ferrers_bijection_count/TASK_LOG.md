# TASK_LOG - TASK-20260718__ferrers_bijection_count / Ferrers Bijection Count

Append-only. Add a new entry to correct previous information.

## 2026-07-18 - STRICT startup and scope

- **Action:** Read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, the retained PG26--PG63 proof, the two predecessor task
  dossiers, the roadmap, templates, and Git state.
- **Result:** The worktree was clean on `main` at
  `b1a4054d1fac75443cf1929921dddb38f9750a5f`. The requested task matched the
  recorded next atomic task and required no production or geometric change.
- **Interpretation:** PG49 and PG62 were stable exact inputs; the missing
  result was a perfect-matching count, not another support classification.
- **Evidence:** `EVIDENCE.md#ev-001---startup-scope-and-independent-derivation`.
- **Next step:** derive the Ferrers permanent without enumerating path
  permutations.

## 2026-07-18 - Independent symbolic derivation

- **Action:** Derived the nested-column recurrence locally and commissioned
  independent count, symmetry, and diagnostic-design analyses.
- **Result:** All derivations agreed on
  \(\mathsf F_m^{\rm lab}=\prod_{j=1}^{2m-1}(j+1-\kappa_j)\), the dual row
  product, the forced zero edge, every required boundary, exact equivalence
  to the PG50--PG63 full-optimal class, and the labelled convention.
- **Interpretation:** The choice count at each restrictive-to-broad column is
  independent of the preceding suffix assignment because the neighborhoods
  are nested. Distinct labelled assignments also give distinct canonical
  dihedral representatives, without a quotient.
- **Evidence:** `EVIDENCE.md#ev-001---startup-scope-and-independent-derivation`.
- **Next step:** write the proof and an independent bounded permanent oracle.

## 2026-07-18 - Proof and sole bounded diagnostic

- **Action:** Added PG64--PG73 to the proof note and created one
  standard-library diagnostic that builds PG49 by cross multiplication and
  evaluates the reduced permanent by Ryser subset inclusion--exclusion.
- **Result:** For \(m=3,\ldots,8\), Ryser and both Ferrers products agree at
  \(36,720,21600,725760,46448640,3292047360\). The first Ruff format check
  reported that the file would be reformatted; mechanical formatting was
  applied, after which lint, format, and the diagnostic passed.
- **Interpretation:** The finite oracle is independent of the recurrence's
  counting method and enumerates subsets rather than path permutations or
  matchings. The initial format failure is retained as non-mathematical
  evidence.
- **Evidence:** `EVIDENCE.md#ev-002---bounded-independent-ryser-diagnostic`.
- **Next step:** synchronize authoritative sources, complete audits, and run
  repository verification.

## 2026-07-18 - Authoritative synchronization in progress

- **Action:** Updated the proof note, project brief, durable knowledge, and
  research roadmap; commissioned separate proof, code, and cross-file audits.
- **Result:** The exact count, scope, labelled/dihedral distinction, sole
  diagnostic, and proposed next atomic task are synchronized in the edited
  sources. Audits and repository regressions remain in progress.
- **Interpretation:** No geometric inference or alternative scaffold has been
  introduced.
- **Evidence:** `EVIDENCE.md#ev-004---proof-code-synchronization-scope-hygiene-and-final-diff`.
- **Next step:** incorporate any audit corrections, update CURRENT_STATUS.md,
  run final checks, and close READY_FOR_REVIEW.

## 2026-07-18 - Final verification and handoff

- **Action:** Incorporated the synchronization audit's row/column convention
  correction; reran the diagnostic, static checks, and code audit; ran the
  focused and full repository regressions, schema tests, checked-artifact
  verifier, three independent audits, final hygiene checks, complete diff
  inspection, `git status`, and `git diff --check`; synchronized
  CURRENT_STATUS.md and the dossier.
- **Result:** PG65 and the diagnostic now consistently use path rows and gap
  columns. The diagnostic, compile, and Ruff checks pass; 49 focused tests,
  all 283 repository tests, and four schema tests pass; four certificates and
  76 local brackets verify; all audits and final scope/hygiene checks pass.
  The exact nine-file task scope is READY_FOR_REVIEW.
- **Interpretation:** The requested symbolic count and exact full-optimal
  class identity are complete, with no production, geometric, or
  alternative-scaffold change.
- **Evidence:** `EVIDENCE.md#ev-003---static-checks-regressions-suite-schemas-and-artifacts`;
  `EVIDENCE.md#ev-004---proof-code-synchronization-scope-hygiene-and-final-diff`.
- **Next step:** user review and manual commit decision.

## 2026-07-18 - Final hygiene harness correction

- **Action:** Investigated the first final-hygiene failure, compared display
  token counts with `HEAD`, removed one dossier trailing space and the
  audit-generated Python cache, and reran the corrected delta-aware harness.
- **Result:** The proof-note delta adds 14 opening and 14 closing display
  tokens; the full-file difference of two is unchanged from `HEAD` and is not
  introduced by this task. The local whitespace and cache findings were
  removed, and the exact nine-path hygiene check passed.
- **Interpretation:** The first display warning was a pre-existing global-file
  condition exposed by an overbroad harness, while the two task-local hygiene
  findings were real and corrected. All three observations remain recorded.
- **Evidence:** `EVIDENCE.md#ev-004---proof-code-synchronization-scope-hygiene-and-final-diff`.
- **Next step:** user review and manual commit decision.

## 2026-07-18 - Display-delta criterion refinement

- **Action:** Corrected the preceding delta-equality criterion after it
  rejected the rewritten CURRENT_STATUS.md for removing, rather than
  preserving, its inherited two-token display imbalance.
- **Result:** The final comparison requires each tracked file to have no
  larger display imbalance than its `HEAD` version. CURRENT_STATUS.md is now
  balanced, the proof-note inherited difference is unchanged, every other
  intended file is balanced, and the nine-path harness passes.
- **Interpretation:** Equal deltas are sufficient but not necessary when a
  task improves a pre-existing imbalance. The non-worsening criterion captures
  both the balanced task additions and that improvement.
- **Evidence:** `EVIDENCE.md#ev-004---proof-code-synchronization-scope-hygiene-and-final-diff`.
- **Next step:** user review and manual commit decision.
