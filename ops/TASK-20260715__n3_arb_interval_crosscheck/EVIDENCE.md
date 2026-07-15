# EVIDENCE - TASK-20260715__n3_arb_interval_crosscheck / Independent Arb Cross-Check For Checked n=3 Artifact

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source/command | Startup, source, artifact, trust, and dependency audit | project memory; interval sources/dossiers; checked `n=3` artifact; official python-flint documentation; `git status` | PASS |
| EV-002 | file/test | Test-only Arb cross-check implementation | `tests/test_n3_arb_interval_crosscheck.py`; `pyproject.toml` | PASS |
| EV-003 | command/test | Focused and full local verification | Arb diagnostics; focused/full pytest; semantic verifier; schema tests; pip check | PASS |
| EV-004 | file/command | Trust documentation, durable memory, and final hygiene | trust/research/global memory; Git/source/hygiene checks | PASS |

## EV-001 - Startup, Source, And Dependency Audit

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant prior dossiers, `research/FIXED_ORDER_ANGULAR_STN.md`, `docs/INTERVAL_BACKEND_TRUST.md`, `src/power_ringmin/interval_verifier.py`, `examples/small_n_interval_certificate_n3.json`, relevant tests, `pyproject.toml`, `.github/workflows/verification.yml`, and dossier templates.
- **Method or command:** `git status --short --branch`.
- **Relevant output:** `## main...origin/main`; no modified or untracked files.
- **Method or command:** `python -c "import flint; print(flint.__version__); print(flint.ctx)"`.
- **Relevant output:** Failed with `ModuleNotFoundError: No module named 'flint'`.
- **Method or command:** Inspected official python-flint PyPI metadata and Arb API documentation.
- **Source:** `https://pypi.org/project/python-flint/0.9.0/`; `https://python-flint.readthedocs.io/en/stable/arb.html`.
- **Relevant output:** Current `python-flint` release line `0.9` supports the repository's Python range; Arb exposes fixed-precision ball arithmetic, direct `asin`, `sqrt`, `pi`, and directed `lower()` / `upper()` bounds.
- **Interpretation:** The initial dependency absence is environmental evidence. A test-only optional dependency and a direct Arb formula can supply an implementation-independent bounded cross-check.
- **Limitations:** Documentation inspection is not a local Arb execution and does not prove the backend correct.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-design-audit`

## EV-002 - Test-Only Arb Implementation

- **Date:** 2026-07-15
- **Method or command:** File edits with `apply_patch` to `pyproject.toml` and `tests/test_n3_arb_interval_crosscheck.py`.
- **Relevant output:** `python-flint==0.9.0` is present only in `[project.optional-dependencies].test`; no runtime dependency or production backend registration changed.
- **Relevant output:** The test module uses only the standard library, pytest, and optional `flint`; it reads the checked JSON directly, parses decimal strings directly as Arb balls, and calls no `power_ringmin` module.
- **Relevant output:** Direct formula is `2 * ((a*b)/((R+a)*(R+b))).sqrt().asin()`; `2*pi` is recomputed through `2 * arb.pi()` at 384-bit precision.
- **Relevant output:** The lower path checks connected directed edge occurrences and uses `-theta.lower()` / `tau.upper()-theta.lower()` before requiring the total upper bound `<0`. The upper path checks every `i<j` pair and both lower-bounded slacks before requiring each `>=0`.
- **Method or command:** `python -m py_compile tests\test_n3_arb_interval_crosscheck.py`.
- **Relevant output:** Passed with no output.
- **Method or command:** Initial `python -m pytest tests\test_n3_arb_interval_crosscheck.py -q -rs` before installing python-flint.
- **Relevant output:** `.ss`; the pure embedded-data test passed and both Arb tests skipped with `python-flint is an optional test dependency`.
- **Interpretation:** Optional-dependency absence is explicit, while installed test environments exercise the independent native backend. The implementation is structurally separate from production verification.
- **Limitations:** Source separation and tests do not prove the test implementation or Arb correct.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---test-only-arb-implementation`

## EV-003 - Focused And Full Local Verification

- **Date:** 2026-07-15
- **Method or command:** `python -m pip install -e ".[test,crosscheck]"`.
- **Relevant output:** Successfully installed editable `power-ringmin-0.1.0` and `python-flint-0.9.0` from the CPython 3.14 Windows x86-64 wheel.
- **Method or command:** Backend/version query using `importlib.metadata` and exposed flint attributes.
- **Relevant output:** Python `3.14.3`; python-flint `0.9.0`; `flint.__version__` `0.9.0`; FLINT `3.6.0` / release `30600`; default context restored at 53 bits outside the 384-bit test context.
- **Method or command:** Deterministic diagnostic extraction from the test-local helpers at 384 bits.
- **Relevant output:** `records=1 cycle_edges=3 witness_pairs=3 witness_slacks=6`.
- **Relevant output:** `cycle_sum_upper=-0.000345795701878590132147302156819834911873698761077819835981980`.
- **Relevant output:** `min_slack_lower=7.81249999999907777683967055517418065596493567633097672062408e-5`; all six slack lower bounds were nonnegative.
- **Method or command:** `python -m pytest tests\test_n3_arb_interval_crosscheck.py -vv`.
- **Relevant output:** Final run: `3 passed in 0.14s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** Final run: `204 passed in 61.24s`.
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Method or command:** `python -m pytest tests\test_checked_artifact_schema_validation.py -vv`.
- **Relevant output:** Final run: `4 passed in 1.11s`.
- **Method or command:** `python -m ruff check tests\test_n3_arb_interval_crosscheck.py`; `python -m py_compile tests\test_n3_arb_interval_crosscheck.py`.
- **Relevant output:** Ruff reported `All checks passed!`; compilation passed with no output.
- **Method or command:** `python -m pip check`.
- **Relevant output:** `No broken requirements found.`
- **Interpretation:** The test-only Arb recomputation establishes the required bounded signs and coverage as local independent implementation evidence, while the existing production artifact path remains green and unchanged.
- **Limitations:** These are local Windows results, not hosted CI; the cross-check covers only `n=3` and trusts Arb/FLINT, bindings, conversion, and test code.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---arb-signs-and-repository-verification`

## EV-004 - Trust Documentation, Durable Memory, And Final Hygiene

- **Date:** 2026-07-15
- **Method or command:** Updated documentation and durable memory with `apply_patch`.
- **Relevant output:** The trust note records method, version/backend, precision, commands, results, exact coverage, signs, classification, and limitations. Project-wide documents preserve the production guarded `mpmath.iv` contract and unchanged certified claims.
- **Method or command:** `python -c` TOML dependency-scope assertion.
- **Relevant output:** `dependency_scope=PASS`; runtime dependencies remain exactly `mpmath>=1.3`, and python-flint is present only in the optional `test` extra.
- **Method or command:** `git diff --exit-code -- examples schemas src .github`.
- **Relevant output:** Exit code 0 with no output; checked artifacts, schemas, production source, and workflow have no tracked changes.
- **Method or command:** Complete `git diff` inspection plus full reads of the new test and dossier files.
- **Relevant output:** Only the intended implementation, dependency, documentation, status, and dossier delta is present. The test contains no production-package or mpmath imports and does not name `MPMathIntervalAngularOracle`.
- **Method or command:** Changed/new-file `rg -n "[ \t]+$" ...` scan; `git diff --check`.
- **Relevant output:** `No trailing whitespace`; `git diff --check` passed with no output.
- **Method or command:** `git status --short --branch`; `git diff --cached --name-only`.
- **Relevant output:** Status contains only the intended modified and new files under `main...origin/main`; no staged path was reported.
- **Interpretation:** Documentation reflects the bounded evidence without overclaiming, protected production/certificate surfaces are unchanged, and the final worktree is ready for review.
- **Limitations:** Hosted GitHub Actions did not run locally and is not claimed as successful.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---final-verification-and-handoff`
