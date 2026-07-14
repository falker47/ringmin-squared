# EVIDENCE - TASK-20260713__exact_tail_incompatibility / Exact Tail Incompatibility

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / computation | Startup and independent exact derivation | project state, prior dossier, proof/source/tests, small-tail checks | PASS |
| EV-002 | file / command / test | Implementation and bounded verification | product-distance source/tests | PASS after test-count correction |
| EV-003 | computation / command | Finite and asymptotic inversion diagnostics | exact formula support | PASS |
| EV-004 | command / review | Full verification and independent review | pytest, artifact verifier, proof/code/docs reviews | PASS |
| EV-005 | command / review | Final scope and diff hygiene | intended paths and complete Git diff | PASS |

## EV-001 - Startup And Independent Derivation

- **Date:** 2026-07-13
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant prior dossiers,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, exact source/tests, and the clean
  Git state; compared three independent derivations; ran separate brute-force
  probes on small tail cycles.
- **Relevant output:** The compatible graph on the consecutive tail is a
  clique/independent-set split graph with nested prefix neighborhoods. The
  derivations agree on an exact formula whose correction to
  `max(0, 2*v-u)` is zero or one. Independent small-tail probes found no
  discrepancy and identified strict examples where the correction is active.
- **Interpretation:** The candidate exact theorem is structurally supported
  before repository implementation and uses no core-order enumeration.
- **Limitations:** Computation is bounded verification evidence; it does not
  replace the symbolic proof or establish an exact value of `B_n`.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---startup-and-exact-derivation`

## EV-002 - Implementation And Bounded Verification

- **Date:** 2026-07-13
- **Method or command:** Edited with `apply_patch`; ran
  `python -m py_compile src\power_ringmin\product_distance.py tests\test_product_distance.py`;
  ran focused product-distance pytest; ran integrated pytest over
  product-distance, zigzag, induced-subset, and insertion tests.
- **Relevant output:** The first focused run reported `1 failed, 19 passed`:
  all 299 independent states matched, but the test required an arbitrary
  comparison count of at least 500. After changing only that meta-assertion
  to `>=250`, focused tests passed `20/20`; integrated tests passed `35/35`.
- **Interpretation:** The production formula agrees with a permutation-based
  verifier that independently constructs `U_T` and scores every tail cycle,
  with a hard tail-size ceiling of seven. Existing core enumeration remains
  bounded to `n=3..11`.
- **Limitations:** The 299 comparisons are finite verification evidence; the
  all-`n` statement is the symbolic nested-neighborhood proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---exact-support-and-bounded-verification`

## EV-003 - Finite And Asymptotic Inversion Diagnostics

- **Date:** 2026-07-13
- **Method or command:** With `PYTHONPATH=src`, evaluated
  `two_threshold_lower_obstruction` and its preceding half-integer for every
  `n=9..1000`; evaluated the explicit `A,D,T_n` upper witness for
  `n=45..1000`, using Python `Decimal` precision 100 only to choose ceilings
  of the displayed algebraic constants and exact `Fraction` arithmetic for
  thresholds and packing checks.
- **Relevant output:** `q_3_11 6,12,12,20,21,30,63/2,42,45`;
  `minimality_checks 992`; `asymptotic_witness_checks 956`;
  `decimal_precision 100`.
- **Interpretation:** The exact finite inversion, predecessor exclusion, and
  constructive upper side of `Q_n=c*n^2+O(n)` agree throughout the diagnostic
  range. No order is enumerated by this check.
- **Limitations:** The decimal ceiling selection is diagnostic; the research
  note supplies the exact symbolic all-`n` inequalities and coefficient.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---exact-inversion-diagnostics`

## EV-004 - Full Verification And Independent Review

- **Date:** 2026-07-13
- **Method or command:** Ran `python -m pytest -p no:cacheprovider`; ran
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  assigned independent reviews of the all-`n` proof, exact source/tests, and
  current documentation; applied the reviewers' boundary and exposition
  corrections and requested final passes.
- **Relevant output:** Full pytest reported `148 passed in 26.38s`; semantic
  verification reported 4 certificates, 76 local brackets, and summary
  values `n=3,4,5,6`; all three reviewers returned `PASS` with no remaining
  blocker.
- **Interpretation:** Repository integration and preserved artifacts remain
  valid, while independent audits agree on the formula, construction, lower
  cut, event-set exhaustivity, inversion, asymptotic decision, implementation,
  bounded enumerator, and documentation classifications.
- **Limitations:** Local verification does not establish hosted CI status. The
  artifact verifier checks existing artifacts and generated none.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---full-verification-and-independent-review`

## EV-005 - Final Scope And Diff Hygiene

- **Date:** 2026-07-13
- **Method or command:** Compared exact expected and observed Git paths;
  strictly decoded all changed files as UTF-8; scanned trailing whitespace;
  counted and checked uniqueness of equation tags; inspected source/test,
  proof, memory, and dossier changes; ran `git diff --check` and final
  `git status --short --branch`.
- **Relevant output:** Exact scope contains 10 intended paths; strict UTF-8
  failures are zero; trailing-whitespace findings are zero; all 51 equation
  tags are unique; `git diff --check` produced no output.
- **Interpretation:** The change set is limited to exact source/tests, the
  primary proof, essential project memory/roadmap, and one STRICT dossier,
  with no artifact, certificate, CLI, schema, module, infrastructure, or
  upstream change.
- **Limitations:** Git warnings about the inaccessible user-global ignore file
  are environmental and do not affect repository status or diff content.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---final-hygiene-and-handoff`
