# TASK_LOG - TASK-20260715__lambda9_core_minimizer_classification / Lambda_9 Core Minimizer Classification

Append-only. Add a new entry to correct previous information.

## 2026-07-15 - Startup And Exact Classification Design

- **Action:** Completed the STRICT startup protocol on a clean worktree, read
  the accepted `n=9` value proof and index-one reduction, inspected the focused
  tests and roadmap, and independently derived the equality and placement
  conditions with exact integer arithmetic.
- **Result:** Equality forces the six-label cycle `(9,5,8,6,7,4)` up to
  dihedral symmetry. Label `3` has four admissible gaps and label `2` has all
  seven resulting gaps, giving 28 core classes and 224 complete classes after
  insertion of label `1`.
- **Interpretation:** The requested result is a bounded exact combinatorial
  classification and needs no production enumeration or geometric change.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-classification-design`
- **Next step:** implement the independent test-only oracle.

## 2026-07-15 - Equality And Shortcut-Gain Classification

- **Action:** Refined the \(S_6/S_5\) lemma to its equality case, ruled out
  the unattainable rearrangement equality in the nonexceptional branch,
  extracted the unique six-label dihedral cycle, and applied exact shortcut
  gains plus the label-two deletion identity to every placement.
- **Result:** Label \(3\) has exactly four admissible gaps and label \(2\)
  has all seven resulting gaps. These are all and only 28 core minimizer
  classes. Exactly one has the full core as a second argmax, and exact
  insertion of label \(1\) gives 224 complete minimizer classes.
- **Interpretation:** This is an exact finite combinatorial proof, independent
  of the exhaustive oracle and unrelated to exact geometric minimizers.
- **Evidence:** `EVIDENCE.md#ev-002---equality-and-placement-proof`
- **Next step:** implement and run the independent full-core oracle.

## 2026-07-15 - Independent Core Oracle

- **Action:** Added a direct test-local \(7!/2\) core generator and literal
  scorer for all 255 nonempty subsets of every row, including every argmax,
  the hard-coded 28 canonical minimizers, the placement parametrization, and a
  deterministic full-record checksum.
- **Result:** All 2,520 core classes and 642,600 subset evaluations recover
  minimum 239, exactly 28 minimizers, and the \(27+1\) argmax pattern. The
  exact insertion theorem then gives 224 complete classes by eight-gap
  insertion. All 28 focused tests pass.
- **Interpretation:** The oracle independently audits the proof without
  calling any repository canonicalizer, public enumerator, or production
  scorer; the public complete-order domain remains `n<=8`.
- **Evidence:** `EVIDENCE.md#ev-003---independent-2520-core-oracle`
- **Next step:** synchronize durable memory and run complete verification.

## 2026-07-15 - Complete Local Verification And Handoff

- **Action:** Synchronized the proof note, project brief, stable knowledge,
  roadmap, current status, and STRICT dossier; ran the focused and complete
  local test suites, checked-artifact and schema regressions, targeted static
  checks, three independent audits, and final diff/whitespace hygiene.
- **Result:** Focused pytest passes 28 tests, full pytest passes 201 tests,
  explicit schema validation passes 4 tests, checked-artifact verification
  accepts 4 certificates and 76 local brackets, Ruff and compilation pass,
  and final diff hygiene is clean. The independent audits reproduce and
  accept the exact 28-class list, 224 complete count, argmax record, checksum,
  proof boundaries, and unchanged production `n<=8` limit.
- **Interpretation:** The bounded task is complete and ready for manual review.
  All reported verification is local Windows/Python 3.14.3 evidence; hosted
  GitHub Actions on Ubuntu/Python 3.11--3.13 was not run or inspected for this
  worktree.
- **Evidence:** `EVIDENCE.md#ev-004---complete-local-verification-and-hygiene`
- **Next step:** user review and manual commit decision.
