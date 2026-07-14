# EVIDENCE - TASK-20260714__fixed_order_angular_stn_semantics / Fixed-Order Angular STN Semantics

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / review | Startup and three independent semantics audits | requested sources, tests, roadmap, clean Git status | PASS |
| EV-002 | proof / test / documentation | Authoritative proof, boundary tests, and synchronized sources | proof note, two tests, authoritative docs | PASS |
| EV-003 | command / test | Focused/full tests, verifier, schema, and lint checks | local Python 3.14.3 | PASS |
| EV-004 | review / hygiene | Final cross-document, changed-path, and diff audit | repository text and complete worktree diff | PASS |

## EV-001 - Startup And Independent Audits

- **Date:** 2026-07-14
- **Method or command:** Inspected `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the historical interval design,
  trust note, all six requested source modules, pertinent tests, roadmap, and
  read-only Git status; obtained independent mathematical, implementation, and
  documentation audits.
- **Relevant output:** The worktree was clean. All audits recover the same STN
  signs: `j -> i` has weight `-theta` and `i -> j` has weight `tau - theta`.
  They also agree that a lower sum upper bound of zero is undecided and must be
  rejected, while an upper slack lower bound of zero is valid for the closed
  non-overlap constraints.
- **Interpretation:** The intended proof and focused tests match current
  verifier behavior; no solver change is required.
- **Limitations:** Source inspection and sampled tests do not prove the guarded
  `mpmath.iv` backend correct.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---startup-and-independent-semantics-audit`

## EV-002 - Proof, Tests, And Synchronized Sources

- **Date:** 2026-07-14
- **Method:** Compared the exact geometric derivation against geometry.py,
  evaluator.py, highprec.py, interval_verifier.py,
  interval_bracket_exporter.py, and critical_structure.py; obtained independent
  mathematical and implementation audits; added focused equality-boundary
  tests; synchronized all authoritative descriptions that referred to the
  historical proof debt or bracket endpoints.
- **Relevant result:** The proof gives the all-pairs angular inequalities, the
  implemented difference-constraint orientation, negative-cycle equivalence,
  shortest-path potential recovery, strict radius monotonicity and continuity,
  fixed-order feasible-set closure, and the local/global half-open bracket
  theorem. The tests require strict negativity at the lower endpoint and
  permit equality at the upper endpoint.
- **Classification:** The real-arithmetic STN and enclosure implications are
  EXACT THEOREMS. Their application to checked artifacts is a CONDITIONAL
  COMPUTER-CERTIFIED RESULT under the documented guarded mpmath.iv premise.
- **Interpretation:** No solver change, certificate generation, or optimum
  assumption is needed to close the mathematical proof obligation.
- **Limitations:** This evidence does not independently prove the interval
  backend, endpoint extraction, scalar mpf arithmetic, or guard correct.

## EV-003 - Local Verification

- **Date:** 2026-07-14
- **Environment:** Python 3.14.3 on the local Windows host.
- **Commands and results:**
  - Focused pytest invocation over interval verifier, interval bracket
    exporter, and critical structure with no cache provider and workspace
    basetemp: PASS, 28 tests.
  - Full pytest invocation with no cache provider and workspace basetemp:
    PASS, 173 tests; a separate collection count confirmed 173 tests in 22
    files.
  - PYTHONPATH=src python -m power_ringmin.verify_checked_artifacts: PASS,
    4 certificates, 76 local brackets, summary n=3,4,5,6.
  - Schema-validation pytest invocation: PASS, 4 tests.
  - python -m ruff check tests/test_interval_verifier.py: PASS, All checks
    passed.
- **Failed checks preserved:** Two prior focused invocations each reported five
  setup errors before the affected test bodies ran. The sandbox denied the
  default user temp directory on the first and C:\tmp on the second. A
  workspace-local basetemp resolved the environmental issue; task-created temp
  directories were removed.
- **Interpretation:** All relevant executable verification passes; the earlier
  errors were isolated to temp-directory permissions rather than code.
- **Limitations:** Hosted Python 3.11-3.13 CI and an independent interval
  backend were not run.

## EV-004 - Final Hygiene And Diff Review

- **Date:** 2026-07-14
- **Method:** Inspected the complete tracked diff and every new file; checked
  Git status and Git diff whitespace; scanned 252 repository text paths with
  strict UTF-8 decoding; checked forbidden control characters, lone carriage
  returns, trailing whitespace, final newlines, display-math balance, and
  uniqueness of all 43 proof equation tags; searched authoritative sources for
  stale fixed-order debt claims; confirmed cited implementation functions and
  documentation paths exist.
- **Relevant output:** All hygiene checks pass. Git status lists only the
  intended documentation, one test file, current status, and task dossier.
  No src, example, schema, certificate, generated analysis artifact, or temp
  path changed.
- **Interpretation:** The final worktree is internally consistent and ready for
  manual review.
- **Limitations:** Read-only local review does not substitute for hosted CI or
  an independent interval-backend audit.
