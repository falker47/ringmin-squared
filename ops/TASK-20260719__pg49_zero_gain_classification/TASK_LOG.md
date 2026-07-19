# TASK_LOG - TASK-20260719 / PG49 Zero-Gain Classification

Append-only. Add a new entry to correct previous information.

## 2026-07-19 - Strict Startup And Exact Reduction

- **Action:** read the repository contract, startup memory, current status,
  the descending-min PG49 proof, PG49 threshold definitions, prior dossier,
  and clean Git state; separated the left and right gain equations.
- **Result:** both zero equations reduce uniquely to primitive square-factor
  parameters `(g,u,w)`, with exact formulas for `(m,j,r)`, a single
  integrality congruence, and four elementary domain inequalities.
- **Interpretation:** KPGMIN-21 was complete only for the left branch; the
  right branch has distinct constants and cannot be silently inferred.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-primitive-parameterization`.
- **Next step:** impose both literal ceilings and audit all endpoints.

## 2026-07-19 - Plateau Boundaries And Cubic Obstruction

- **Action:** substituted each branch into both half-open ceiling residuals,
  proved the residual reduction and boundary behavior, and derived uniform
  Legendre bounds around the irreducible cubic root.
- **Result:** exact polynomial plateau tests are necessary and sufficient;
  every zero ratio is a regular cubic-root convergent and each ratio admits
  only finitely many scales `g`.
- **Interpretation:** global cardinality is exactly a filtered one-sided
  cubic continued-fraction problem.  The conic zero equation alone cannot
  produce a plateau family.
- **Evidence:** `EVIDENCE.md#ev-002---exact-plateau-and-boundary-audit` and
  `EVIDENCE.md#ev-003---continued-fraction-obstruction`.
- **Next step:** run the sole bounded falsification diagnostic and preserve
  contradictory evidence.

## 2026-07-19 - Bounded Diagnostic And Right-Hole Discovery

- **Action:** created and ran the sole standalone standard-library
  diagnostic; extended only its finite convergent bound after the first pass
  to search explicitly for missing right holes; rechecked every reported
  candidate by literal integer ceilings and gains.
- **Result:** the known left witness is recovered.  The bounded run reports
  56 left and eight right exact parameter triples, including a new exact
  right witness at the smallest `m` found in that bounded run.
- **Interpretation:** universal right-hole nonexistence is disproved.  The
  finite multiplicity is evidence only and does not establish an infinite
  family or settle cardinality.
- **Evidence:** `EVIDENCE.md#ev-004---sole-bounded-diagnostic` and
  `EVIDENCE.md#ev-005---exact-left-and-right-witnesses`.
- **Next step:** synchronize only pertinent sources and perform full
  verification.

## 2026-07-19 - Independent Audit Corrections

- **Action:** audited the unified formulas, both branch residuals, the
  Legendre bounds, all ceiling endpoints, exterior columns, and both large
  witnesses independently.
- **Result:** renamed the cubic root to \(\xi\) to avoid collision with the
  descending-min permutation; exposed all four exact sign-dependent
  quadratic \(g\) windows; supplied the small-denominator exclusion in the
  left Legendre bound; made jump, \(j=0\), \(r=1\), \(j=m-1\), \(j\ge m\),
  and closing boundaries explicit; and clarified that the right witness
  records a singleton path index rather than its label.
- **Interpretation:** the exact classification is unchanged, but the
  cardinality obstruction and every boundary are now self-contained in the
  authoritative proof.
- **Evidence:** EV-002 and EV-003.
- **Next step:** run the sole diagnostic and repository verification, then
  close the STRICT dossier.

## 2026-07-19 - Regression And Blocked Handoff

- **Action:** reran the sole diagnostic; ran full and focused pytest,
  checked-artifact verification, scoped Ruff, source/tag/notation audits,
  independent proof review, complete diff inspection, final Git status, and
  whitespace checks.
- **Result:** the bounded diagnostic passes; pytest reports 283 full and 4
  focused passes; 4 certificates and 76 local brackets verify; Ruff and
  source audits pass; the independent audit finds no mathematical defect;
  final diff hygiene passes.
- **Failed check retained:** a cleanup probe after focused pytest found that
  pytest had already removed its basetemp, so path resolution failed and
  there was nothing to remove.
- **Interpretation:** the exact classification, witnesses, and obstruction
  are reviewable.  The task status is BLOCKED solely because the requested
  global finite/infinite dichotomy is equivalent to an unresolved filtered
  cubic-convergent problem.
- **Evidence:** EV-006.
- **Next step:** user review; any attack on the residual obstruction belongs
  to a fresh STRICT task.
