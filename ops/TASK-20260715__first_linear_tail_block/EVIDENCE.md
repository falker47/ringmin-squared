# EVIDENCE - TASK-20260715__first_linear_tail_block / First Linear Tail Block

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / test | Clean startup, scope, and focused baseline | authoritative files and cyclic-ratio tests | PASS |
| EV-002 | exact proof / independent audit | Positive cubic residual for the named linear block | cyclic-ratio proof note | PASS |
| EV-003 | bounded exact test-local diagnostic | Slack identity and intact/recursive prefix arithmetic | cyclic-ratio tests | PASS |
| EV-004 | verification / review | Complete regression, scope, and final hygiene | local worktree | PASS WITH RECORDED UNRELATED LINT |
| EV-005 | exact correction / verification | Global lower corollary and coefficient algebra | proof notes, memory, roadmap, dossier, and tests | PASS WITH RECORDED UNRELATED LINT |
| EV-006 | notation correction / verification | Disambiguated block-local floor and reserved full-distance symbol | synchronized sources, repository audit, and tests | PASS |

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
- **Limitations:** \(c_0\) is not claimed optimal and is not the exact
  residual coefficient. The global and geometric lower consequences omitted
  in this original entry are supplied by the correcting EV-005; no exact
  leading coefficient, convergence, general-density, or production result
  follows.
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

## EV-005 - Corrected Global Lower Corollary

- **Date:** 2026-07-15
- **Method:** For every fixed admissible block start \(m\), minimize the
  pointwise inequality
  \(\Lambda(\sigma)\ge\max_jP_\sigma(S_{m+j})\); only afterward maximize the
  resulting scalar lower bounds. Select \(m=1\), apply the nonstarred pairing
  floor in CR28bg, expand \(P_{r_n,n}\) with its exact floor remainder, and
  transfer through the strict global cyclic-ratio sandwich.
- **Relevant exact output:** for every \(n\ge141\),
  \[
  \Lambda_n
  \ge\Gamma_n^{(r_n)}
  \ge\gamma^{(r_n)}_{1,n}
  \ge P_{r_n,n}+(r_n-s_n)F_n^{\mathrm{blk}},
  \]
  \[
  \Lambda_n
  \ge {139-25\sqrt2\over375}n^3
  -{40\sqrt2-54\over75}n^2,
  \]
  and
  \[
  R_2^*(n)
  >{139-25\sqrt2\over375\pi}n^3
  -\left(1+{40\sqrt2-54\over75\pi}\right)n^2.
  \]
  Hence the liminf lower coefficients are
  \((139-25\sqrt2)/375\) and that number divided by \(\pi\).
- **Exact test-local audit:** a local \(\mathbb Q(\sqrt2)\) pair arithmetic
  check verifies
  \[
  {2(\sqrt2-1)\over3}
  +{389-275\sqrt2\over375}
  ={139-25\sqrt2\over375},
  \]
  the quadratic remainder \(2d=(40\sqrt2-54)/75\), and both positivity
  comparisons without floating point or a new dependency.
- **Commands and results:**
  - `python -m pytest tests\test_fixed_order_cycle_ratio.py -q -k
    "first_linear_density"`: 9 passed.
  - `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`: 57 passed.
  - `python -m pytest`: 233 passed.
  - `python -m power_ringmin.verify_checked_artifacts` with
    `PYTHONPATH=src`: all 4 certificates and 76 local brackets verified.
  - `python -m pytest tests\test_checked_artifact_schema_validation.py -q`:
    4 passed.
  - `python -m ruff check tests/test_fixed_order_cycle_ratio.py`: passed.
  - `python -m ruff check .`: the same four existing findings in untouched
    files recorded by EV-004.
  - `git diff --check`: passed.
  - `git diff --name-only -- src schemas examples verify.py pyproject.toml
    .github`: no output.
- **Independent review:** separate read-only mathematical and synchronization
  audits checked the quantifier order, nonstarred/starred distinction, exact
  floor expansion, finite constants, strict geometric transfer, coefficient
  algebra, limitations, and requested scope. The mathematical audit found no
  flaw; final synchronization findings are reflected in the handoff files.
- **Classification:** EXACT GLOBAL LOWER-BOUND COROLLARY plus VERIFIED FACT
  (EXACT TEST-LOCAL ALGEBRA); PASS WITH RECORDED UNRELATED LINT.
- **Limitations:** the displayed numbers are exact coefficients of proved
  lower bounds, not exact asymptotic leading coefficients. Neither normalized
  sequence is proved to converge; other linear densities and the exact
  residual coefficient remain open. No production, artifact, schema,
  verifier, backend, certificate, or enumeration limit changed.
- **Linked log entry:** TASK_LOG.md, Corrected Global Consequence And Handoff.

## EV-006 - Notation Collision Correction And New Handoff

- **Date:** 2026-07-15
- **Question:** does any repository source still use the full-distance symbol
  ambiguously for the first-linear-block local floor after synchronization?
- **Method:** classified every tracked occurrence before editing, changed only
  the 28 block-local references to \(F_n^{\mathrm{blk}}\), preserved the
  canonical full-distance definition and references, searched tracked and
  non-cache repository files for primary and alternate spellings, and
  inspected the complete diff for scope.
- **Result:** no block-local use of \(L_n\) remains. Every residual occurrence
  denotes the full-distance obstruction or explicitly states that the name is
  reserved for it. The authoritative and stable-memory definitions of the
  local minimum now use \(F_n^{\mathrm{blk}}\), and every named synchronized
  source carries the same notation. Tags, arguments,
  coefficients, domains, mathematical tests, and production files are
  unchanged.
- **Commands and results:**
  - `python -m pytest tests\test_fixed_order_cycle_ratio.py -q -k
    "first_linear_density"`: 9 passed.
  - `python -m pytest
    tests\test_product_distance.py::test_tail_obstruction_first_dominates_adjacent_formula_at_33
    -q`: 1 passed.
  - `python -m pytest`: 233 passed.
  - repository-wide `git grep`/`rg` audit of \(L_n\), alternate spellings,
    and `min\{G_n(`: no ambiguous local use remains.
  - `git diff --name-only -- src tests examples schemas verify.py`: no output.
  - `git diff --check`: passed.
- **Classification:** VERIFIED FACT (REPOSITORY-WIDE NOTATION AUDIT) and
  VERIFIED FACT (LOCAL REGRESSION); PASS.
- **Limitations:** tests do not parse Markdown notation, so synchronization is
  established by exhaustive source search and diff inspection. Hosted GitHub
  Actions have not run these documentation-only changes.
- **Linked log entry:** TASK_LOG.md, Notation Collision Correction And New
  Handoff.
