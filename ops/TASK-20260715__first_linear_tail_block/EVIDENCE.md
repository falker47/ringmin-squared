# EVIDENCE - TASK-20260715__first_linear_tail_block / First Linear Tail Block

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / test | Clean startup, scope, and focused baseline | authoritative files and cyclic-ratio tests | PASS |
| EV-002 | exact proof / independent audit | Positive cubic residual for the named linear block | cyclic-ratio proof note | PASS |
| EV-003 | bounded exact test-local diagnostic | Slack identity and intact/recursive prefix arithmetic | cyclic-ratio tests | PASS |
| EV-004 | verification / review | Complete regression, scope, and final hygiene | local worktree | PASS WITH RECORDED UNRELATED LINT |

## EV-001 - Startup, Scope, And Baseline

- **Date:** 2026-07-15
- **Method or command:** Read AGENTS.md, start.md,
  PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, the arbitrary-block dossier,
  relevant proof/roadmap/test sources, and Git state; ran
  python -m pytest tests/test_fixed_order_cycle_ratio.py -q.
- **Relevant output:** initial tree clean on main at
  9c39f6a621c1eca41277b2ae72a60c634aa59fe4; baseline 47 passed.
- **Interpretation:** the STRICT task can proceed without mixing unrelated
  work.
- **Limitations:** startup and baseline do not prove the new theorem.
- **Linked log entry:** TASK_LOG.md, Startup And Scope.

## EV-002 - Exact Linear-Block Lower Obstruction

- **Date:** 2026-07-15
- **Method:** Apply the exact split-history formula at
  \(m=1\), \(r_n=\lfloor(\sqrt2-1)n\rfloor\). Use the base slack identity,
  charge every intact base edge at most once, bound recursive child-edge
  splits separately, and compare zero with the selected prefix.
- **Relevant output:** for \(n\ge141\),
  \[
  \gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
  \ge
  c_0n^3-C_0n^2,
  \]
  with
  \[
  c_0={389-275\sqrt2\over375}>0,
  \qquad
  C_0={2(20\sqrt2-27)\over75}+{1\over8}.
  \]
  The finite right-hand side is positive for every \(n\ge655\).
- **Independent review:** two read-only audits reconstructed the proof,
  verified every factor \(1/2\), the one-use base linkage, recursive endpoint
  range, monotonic local floors, parity formula for the alternating excess,
  cutoff domain, and positive constant; no flaw was found.
- **Classification:** EXACT METHOD-SPECIFIC THEOREM.
- **Limitations:** \(c_0\) is not claimed optimal; no exact residual
  coefficient, general density, \(\Lambda_n\), geometry, or production
  result follows.
- **Linked log entry:** TASK_LOG.md, Exact Cubic Residual.

## EV-003 - Bounded Exact Diagnostics

- **Date:** 2026-07-15
- **Environment:** local Windows host; integer and exact Fraction arithmetic.
- **Oracle design:** check the base-slack identity on every dihedral cycle of
  tail sizes three through six. At \(n=141,200,500,1000\), build one
  alternating base and run deterministic policies that prefer intact base
  edges or force recursive child edges, auditing exact rounding, linkage,
  every local contribution, prefix averaging, and the finite lower bound.
- **Relevant output:** focused selection reports 9 passed.
- **Additional read-only diagnostic:** fixed seed 20260715, 200 randomly
  selected compatible prefix histories across the same four \(n\)-values;
  every exact identity and lower inequality passed.
- **Classification:** VERIFIED FACT (BOUNDED EXACT TEST-LOCAL COMPUTATION).
- **Limitations:** these finite checks are not the all-\(n\) proof and call no
  production scorer, canonicalizer, or enumerator.
- **Linked log entry:** TASK_LOG.md, Bounded Diagnostics And Documentation.

## EV-004 - Complete Verification And Final Review

- **Date:** 2026-07-15
- **Commands and results:**
  - `python -m pytest tests/test_fixed_order_cycle_ratio.py -q`: 56 passed.
  - `python -m pytest`: 232 passed.
  - `python -m power_ringmin.verify_checked_artifacts` with `PYTHONPATH=src`:
    all 4 certificates and 76 local brackets verified.
  - `python -m pytest tests/test_checked_artifact_schema_validation.py -q`:
    4 passed.
  - `python -m ruff check tests/test_fixed_order_cycle_ratio.py`: passed.
  - `python -m ruff check .`: four existing findings, all in untouched files
    (`critical_structure.py`, `fixed_order_artifact.py`, and
    `test_finite_results.py`).
  - `git diff --check`: passed.
  - `git diff --name-only -- src schemas examples verify.py pyproject.toml
    .github`: no output.
- **Review:** independently reconstructed the exact lower proof and inspected
  the final definitions, domain, rounding, factors, cutoff, constants,
  compatibility language, prefix maximum, roadmap, and non-consequences.
- **Interpretation:** the changed work passes proportional local verification
  and remains within the requested proof-note/test-local/documentation scope.
- **Limitations:** the repository-wide Ruff findings predate and lie outside
  this task; hosted GitHub Actions have not run the worktree changes.
- **Classification:** PASS WITH RECORDED UNRELATED LINT.
