# TASK_STATUS - TASK-20260719 / Descending-Min PG49 Exact K

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove that the descending-min rule on the PG49 Ferrers board
  is a relation-compatible bijection for every \(m\ge3\), then determine the
  exact induced-subset objective \(K\), all maximizing subsets, its exact
  formula and cubic coefficient, and all comparisons with K825 and the two
  PG46 witnesses.
- **Expected output:** an all-\(m\) symbolic theorem, one bounded independent
  max-plus/shortcut diagnostic, exact preservation of any counterexample,
  and synchronized durable memory without prohibited enumeration or
  geometric inference.

## Scope

- **In scope:** the one deterministic descending-min PG49 assignment on
  \(n=10m+3\), \(m\ge3\); its suffix invariant, closed form, core order,
  isolated insertion gains, signed shortcut equality cases, exact score,
  all maximizers, K825/closing/preclosing comparisons, asymptotic coefficient,
  and polynomial/quasipolynomial classification.
- **Out of scope:** other PG49 matchings, optimization across the Ferrers
  class, enumeration of subsets/permutations/matchings, production code,
  geometric realizability, angular-threshold identities, and global
  minimizing-order claims.

## Verified Facts

- Startup found a clean main worktree at
  `c310228d86fd0f0598dee1ff7984b5100726337b`, tracking `origin/main`.
- The suffix invariant is
  \(\{\alpha(t):j\le t\le2m-1\}
    =[\kappa_j,\kappa_j+2m-1-j]\); it proves well-definedness,
  bijectivity, and relation compatibility.
- The exact value is \(K=K_{825}+D_m+G_m\), with \(D_m\) the explicit
  path-connection sum and \(G_m\) the positive part of the two early-plateau
  singleton insertion gains.
- All maximizers are
  \(B_m\cup\mathcal P_m\cup Z'\), \(Z'\subseteq\mathcal Z_m\), so their
  exact number is \(2^{|\mathcal Z_m|}\).
- Universal uniqueness is disproved by the exact zero-gain row
  \(m=101805057120180546870\); this contradicts, and correctly supersedes,
  the pattern on small rows.
- The order improves K825 and preclosing PG46 only at \(m=4\), never improves
  closing PG46, and never ties any comparator.
- The \(m^3\) coefficient is
  \(288.1683105370884612135\ldots\), hence the \(n^3\) coefficient is
  \(0.2881683105370884612\ldots>143/500\). It is transcendental, so the
  exact function is neither polynomial nor eventual quasipolynomial.

## Assumptions / Inferences

- The previously proved PG49 Ferrers support, PG62 full-\(W\) equivalence,
  and general cyclic shortcut identity are used as inputs.
- Bounded computation is corroborative only; no finite row range is used as
  the all-\(m\) proof.
- No geometric consequence is inferred from relation compatibility or the
  core-order calculation.

## Decisions And Rationale

- Preserve zero gains symbolically rather than assume uniqueness; the exact
  large counterexample is promoted as a disproved-claim correction.
- Use insertion gains in the theorem and a signed shortcut equality audit,
  so positive, negative, and zero labels have unambiguous roles.
- Give the exact finite floor/positive-part formula and prove that the
  requested polynomial/quasipolynomial alternative does not exist.
- Keep the sole standalone diagnostic standard-library-only and bounded:
  max-plus/shortcut through \(m=30\), lighter exact checks through \(m=1000\).

## Plan And Expected Delta

- Complete STRICT startup and source inspection. COMPLETE.
- Prove the Ferrers greedy invariant and closed bijection. COMPLETE.
- Derive exact \(K\), argmax classification, comparisons, and asymptotics.
  COMPLETE.
- Add and run the independent diagnostic. COMPLETE.
- Synchronize authoritative notes and task dossier. COMPLETE.
- Run repository verification and inspect the full diff. COMPLETE.

## Verification

- **Checks:** standalone diagnostic, scoped Ruff and in-memory compile,
  complete regressions, schema validation, checked-artifact verification,
  source/tag structure, whitespace, Git status/diff, and independent proof
  audits all completed.
- **Observed result:** diagnostic PASS on 28 max-plus/shortcut rows,
  36,989,498 DP transitions, 958,916 oriented shortcut arcs, and 998 formula
  rows through \(m=1000\). The complete suite passed 283 tests, the focused
  schema suite passed four, and checked-artifact verification passed for four
  certificates and 76 local brackets. Independent symbolic audits agree on
  the greedy invariant, exact zero counterexample, signed shortcut
  classification, comparator proof, coefficient, and non-quasipolynomial
  argument after all requested rigor clarifications were incorporated.
- **Limitations:** the diagnostic does not and cannot certify the all-\(m\)
  theorem; hosted CI and geometric computation are out of scope.

## Blockers / Risks

- No blocker. Residual risk is ordinary human review of a long symbolic
  proof and of the exact enormous zero-gain witness.
- The finite diagnostic has no zero gain on checked rows only; it must never
  be read as an all-\(m\) uniqueness statement.

## Next Atomic Action

- User manual review and commit decision.

## Handoff

- **Last verified result:** the complete symbolic theorem, exact
  counterexample, bounded diagnostic, regressions, source structure, and final
  diff hygiene all pass.
- **Files changed:** six authoritative Markdown files and this four-file
  STRICT dossier; no production, tests, artifacts, schemas, certificates, or
  upstream path.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`, then this
  dossier's `EVIDENCE.md`.
