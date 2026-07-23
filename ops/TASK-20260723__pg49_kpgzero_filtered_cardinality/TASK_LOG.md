# TASK_LOG - TASK-20260723 / PG49 KPGZERO Filtered Cardinality

Append-only. Add a new entry to correct previous information.

## 2026-07-23 - Strict Startup And Exact Scope

- **Action:** verified a clean Git tree at
  `4180e63940ae810e39f443213c41935877638390`; read the repository contract,
  stable memory, current status, roadmap, PG49 support proof, KPGMIN,
  KPGZERO-1--KPGZERO-30, KPGSTAR, and the predecessor dossier.
- **Result:** the open cardinality is exactly the count of filtered
  convergent/scale pairs for the descending-min family. PG49 already supports
  that bijection for every \(m\), so it contributes no missing arithmetic
  condition.
- **Interpretation:** support \(W\), induced \(K\), and geometry must be
  separated before asking for an infinite supported family.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-exact-problem`.
- **Next step:** formalize the fibres and test whether support can determine
  their cardinality.

## 2026-07-23 - Support-Only And Fixed-Direction No-Go

- **Action:** defined the filtered per-row fibres and the marked
  descending-min family; compared descending-min with PG49-star at the exact
  left witness; derived an infinite affine conic/support ray and checked its
  two plateau residuals symbolically.
- **Result:** induced-\(K\) maximizer cardinality is not constant among
  supported bijections on one PG49 board, every fixed primitive direction
  admits only finitely many filtered scales, and the affine support-only ray
  fails the literal plateau at every index.
- **Interpretation:** bare PG49 supportedness cannot replace the induced-\(K\)
  maximizer test, and scaling finitely many primitive directions cannot
  supply an infinite filtered family. The absolute arithmetic dichotomy
  remains KPGZERO-24.
- **Evidence:** `EVIDENCE.md#ev-002---filtered-cardinality-and-no-go`.
- **Next step:** implement a small exact diagnostic on the discriminating
  true and false instances.

## 2026-07-23 - Independent Exact Diagnostic

- **Action:** added the standalone standard-library
  `exact_diagnostic.py`; checked a PG49 equality boundary, one direct
  all-pairs supported core, discriminating affine-ray rows, exact accepted
  and rejected filtered parameters, and the same-board
  descending-min/PG49-star comparison.
- **Result:** every exact check passes, Ruff passes, and no matching, subset,
  path-assignment, or permutation-family enumeration is performed.
- **Interpretation:** the diagnostic corroborates the proved separations; it
  is not a convergent sweep and does not choose either side of KPGZERO-24.
- **Evidence:** `EVIDENCE.md#ev-003---independent-exact-diagnostic`.
- **Next step:** synchronize durable documents and run repository
  verification.

## 2026-07-23 - Verification And Ready For Review

- **Action:** synchronized the authoritative proof, PG49 summary, stable
  knowledge, roadmap, current status, and dossier; obtained two independent
  read-only audits; ran the full test suite, schema check, checked-artifact
  verifier, static check, and final Git diff audit.
- **Result:** both audits found no substantive mathematical error after
  parity, domain, and terminology clarifications. A first concurrent test
  run had one transient Git-provenance mismatch; the isolated test and the
  sequential full suite then passed, with 283 tests green. The schema and
  artifact checks pass, and final diff hygiene is clean.
- **Interpretation:** the bounded task is complete and
  `READY_FOR_REVIEW`. Production, public tests, schemas, and artifacts are
  unchanged.
- **Evidence:** `EVIDENCE.md#ev-004---regression-and-hygiene`.
- **Next step:** user review and manual commit decision; do not begin the
  deferred absolute arithmetic question in this task.
