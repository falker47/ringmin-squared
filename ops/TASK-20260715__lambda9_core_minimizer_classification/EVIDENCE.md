# EVIDENCE - TASK-20260715__lambda9_core_minimizer_classification / Lambda_9 Core Minimizer Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection / exact derivation | Clean startup and classification design | authoritative files and exact read-only probes | PASS |
| EV-002 | proof | Equality-tail and placement classification | proof note | PASS |
| EV-003 | exact computation / test | Independent 2,520-core oracle and argmax records | focused test module | PASS |
| EV-004 | verification / hygiene | Full local suite and final review | repository checks | PASS |

## EV-001 - Startup And Classification Design

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the accepted `n=9` and
  index-one task dossiers, the cyclic-ratio proof, focused tests, roadmap,
  templates, production boundary, and hosted workflow configuration; inspected
  `git status`, `git log`, and `HEAD`; used independent exact integer-only
  read-only probes to classify equality cases, placements, and argmax sets.
- **Relevant output:** Git reported clean `main...origin/main` at
  `849ff6bf70fc3d56c81d50c9fba5d2319909e34e`. The derivation gives 28 core
  minimizer classes, with 27 having sole argmax \(S_6\) and one also having
  the full core; exact insertion gives 224 complete classes.
- **Interpretation:** The task can be completed with a finite proof and a
  test-only independent oracle while preserving the public `n<=8` boundary.
- **Limitations:** Exploratory probes are design evidence, not the final proof
  or regression. No hosted CI result was inspected.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---startup-and-exact-classification-design`

## EV-002 - Equality And Placement Proof

- **Date:** 2026-07-15
- **Method:** Classified equality in the finite \(S_6/S_5\) lemma. The
  nonexceptional branch would require an impossible \(7\)--\(7\) loop in the
  equality pairing; the \(\{8,9\}\) branch is too large; and the
  \(\{7,9\}\) table has one admissible row. For the forced cycle
  \(\Omega=(9,5,8,6,7,4)\), evaluated the six insertions of label \(3\),
  compressed all shortcut gains for the four admissible cases, and bounded
  insertion of label \(2\) by
  \(2(a+b)-ab=4-(a-2)(b-2)\).
- **Relevant result:** A core order has \(K=239\) if and only if label \(3\)
  is placed in one of the four gaps of \(\Omega\) not incident to label \(4\)
  and label \(2\) is placed in any of the seven resulting gaps. This gives 28
  dihedral classes. Twenty-seven have sole argmax
  \(S_6=\{4,\ldots,9\}\); `(9,4,7,6,8,3,2,5)` also has the full core.
  Exact label-one insertion gives \(28\cdot8=224\) complete minimizer
  classes, with no argmax containing label \(1\).
- **Classification:** EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION).
- **Limitations:** The theorem is finite and combinatorial. It gives no exact
  \(R_2^*(9)\), geometric minimizer classification, all-\(n\) formula, or
  asymptotic claim.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---equality-and-shortcut-gain-classification`

## EV-003 - Independent 2,520-Core Oracle

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3; exact integer
  arithmetic.
- **Oracle design:** Generate `(9,*tail)` directly for all permutations of
  `2..8` and retain `order[1] < order[-1]`. This gives \(7!/2=2{,}520\)
  core dihedral classes without calling `canonical_core_orders`, any
  repository canonicalizer, the public enumerator, or the production Karp
  scorer. Score all 255 nonempty induced subsets literally and retain every
  argmax in every row.
- **Relevant output:** 2,520 rows and 642,600 subset evaluations give minimum
  239 and exactly the hard-coded 28 canonical minimizers. Twenty-seven have
  sole argmax \(S_6\), while one also has the full core. Across the complete
  record, 2,412 rows have one argmax and 108 have two. The deterministic
  84,395-byte serialization has SHA-256
  `557226668a82f6489274571148572076e373d49baefaa61e6d1f5a458bb857a2`.
- **Command:**
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp .tmp_pytest_lambda9_classification_focused`
- **Relevant test output:** `28 passed in 13.89s`.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** This is independent finite implementation evidence, not
  the source of the proof, a public \(n=9\) complete-order enumeration, or a
  geometric certificate. The production domain remains `n<=8`.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---independent-core-oracle`

## EV-004 - Complete Local Verification And Hygiene

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3. Hosted GitHub Actions on
  Ubuntu/Python 3.11--3.13 was not run or independently inspected for this
  worktree.
- **Commands and relevant output:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp .tmp_pytest_lambda9_classification_focused`
    -> `28 passed in 15.10s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider --basetemp .tmp_pytest_lambda9_classification_full`
    -> `201 passed in 55.99s`.
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
    -> accepted 4 certificates, 76 local brackets, and the checked
    `n=3..6` summary.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py --basetemp .tmp_pytest_lambda9_classification_schema`
    -> `4 passed in 0.99s`.
  - `$env:PYTHONPATH='src'; python -m ruff check tests\\test_fixed_order_cycle_ratio.py`
    -> `All checks passed!`.
  - `python -m compileall -q tests\\test_fixed_order_cycle_ratio.py`
    -> exit code 0 with no output.
  - Final changed-file trailing-whitespace scan, `git status`, complete
    `git diff` inspection, and `git diff --check` -> PASS. Pytest temporary
    directories were removed after their resolved paths were confirmed inside
    the workspace. The only Git diagnostic was the harmless sandbox warning
    about the inaccessible global excludes file; it is not a diff defect.
- **Independent audits:** separate mathematical, oracle, and documentation
  reviews accept the equality proof, the human-checkable placement rule, the
  hard-coded 28 representatives, 224 count, full argmax serialization and
  checksum, Python 3.11 syntax, Markdown structure, and explicit separation
  from geometry and public enumeration.
- **Interpretation:** All repository-local checks required by this task pass,
  and the intended changes are ready for manual review.
- **Limitations:** Local success does not establish hosted CI status. The
  computation is a finite combinatorial oracle, not a geometric certificate;
  existing checked geometric artifacts and their backend trust boundary are
  unchanged.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---complete-local-verification-and-handoff`
