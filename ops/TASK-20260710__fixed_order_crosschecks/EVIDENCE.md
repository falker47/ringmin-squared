# EVIDENCE - TASK-20260710 / Fixed-Order Crosschecks

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | command/source | Startup and scope | project root | Startup files read; local tree clean |
| EV-002 | source | Upstream validation inspection | upstream Ringmin | Fixed-order pieces selected; search/artifact pieces excluded |
| EV-003 | file/source | Implementation | project root | Crosscheck, verifier, tests, and metadata added |
| EV-004 | test/command | Failed and discarded checks | project root | Subprocess harness failed; node check inapplicable |
| EV-005 | test/command | Final verification | project root | Tests, compilation, verifier commands, and exclusion search passed |
| EV-006 | command/source | Handoff | project root | Memory and diff checks completed |

## EV-001 - Startup And Scope

- **Date:** 2026-07-10
- **Method or command:** `git rev-parse --show-toplevel`
- **Relevant output:** `C:/Users/Falker/Desktop/Code/circle/ringmin-squared`.
- **Method or command:** `Get-Content -Raw AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `ops/TASK-20260710__foundation_import/*`.
- **Relevant output:** required startup files and relevant prior task memory were read.
- **Method or command:** `git status --short`
- **Relevant output:** no output.
- **Interpretation:** The task began in the intended repository with no unrelated uncommitted changes.
- **Limitations:** Startup inspection does not verify new implementation behavior.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---startup-and-scope`

## EV-002 - Upstream Validation Inspection

- **Date:** 2026-07-10
- **Method or command:** `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin -c core.excludesfile= status --short`
- **Relevant output:** no output.
- **Method or command:** `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin -c core.excludesfile= rev-parse HEAD`
- **Relevant output:** `cc0327400819fe06b230d967cdcbafffe1648317`.
- **Method or command:** `Get-Content -Raw` on upstream `src/ringmin/crosscheck.py`, root `verify.py`, `scripts/highprec_verify.py`, `src/ringmin/artifacts.py`, `src/ringmin/search.py`, and `tests/test_m1.py`.
- **Relevant output:** fixed-order SLSQP accepts explicit radius orders; unconstrained global SLSQP hardcodes original radii; verifier/frontier checks are coupled to upstream result artifacts.
- **Interpretation:** Import only the fixed-order SLSQP cross-check and a minimal standalone verifier scaffold.
- **Limitations:** Upstream tests were inspected but not run.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---upstream-validation-inspection`

## EV-003 - Implementation

- **Date:** 2026-07-10
- **Method or command:** local file edits through patch.
- **Relevant output:** added `src/power_ringmin/crosscheck.py`, root `verify.py`, and `tests/test_crosscheck_and_verifier.py`; updated `pyproject.toml`, `requirements.txt`, and `src/power_ringmin/__init__.py`.
- **Interpretation:** The repository now has radius-sequence-aware fixed-order SLSQP cross-checks and a standalone high-precision verifier scaffold.
- **Limitations:** File creation alone does not prove correctness; tests and direct verifier checks are recorded separately.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---implementation`

## EV-004 - Failed And Discarded Checks

- **Date:** 2026-07-10
- **Method or command:** initial `python -m pytest` after the first implementation.
- **Relevant output:** 6 tests passed and 2 failed; both failures were `OSError: [WinError 6] Handle non valido` while pytest spawned `subprocess.run(..., capture_output=True)`.
- **Interpretation:** The verifier subprocess test harness failed in this Windows/Python 3.14 environment. Tests were rewritten to call `verify.main()` with patched argv, and direct shell invocations were kept for standalone CLI evidence.
- **Method or command:** `node --check verify.py`
- **Relevant output:** failed with `ERR_UNKNOWN_FILE_EXTENSION` for `.py`.
- **Interpretation:** This check is inapplicable to Python and was discarded.
- **Limitations:** Failed checks are diagnostic evidence, not validation.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---test-harness-correction`

## EV-005 - Final Verification

- **Date:** 2026-07-10
- **Method or command:** `python -c "import numpy, scipy, mpmath; print('numpy', numpy.__version__); print('scipy', scipy.__version__); print('mpmath', mpmath.__version__)"`
- **Relevant output:** `numpy 2.4.3`; `scipy 1.17.1`; `mpmath 1.3.0`.
- **Method or command:** baseline `python -m pytest`
- **Relevant output:** `5 passed in 0.22s`.
- **Method or command:** final `python -m pytest`
- **Relevant output:** `8 passed in 1.22s`.
- **Method or command:** `python -m py_compile verify.py src\power_ringmin\crosscheck.py tests\test_crosscheck_and_verifier.py`
- **Relevant output:** no output.
- **Method or command:** `python verify.py --order 1,4,9 --radius 0.38338703613936966604628713672532649776985422245654228331612995273239552892574553 --digits 80 --eta 1e-20`
- **Relevant output:** `fixed_order=PASS local=PASS witness=SKIP n=3 ... margin=-1.0e-40`.
- **Method or command:** `python verify.py --order 1,4,9 --radius 0.38338702613936966604628713672532649776985422245654228331612995273239552892574553 --digits 80`
- **Relevant output:** exit code 1; `fixed_order=FAIL ... margin=-6.91526441244e-8`.
- **Method or command:** `rg -n "certified|SearchResult|ringmin\.search|slsqp_unconstrained|stage_a|frontier|results" src verify.py tests`
- **Relevant output:** matches only explanatory text and the test asserting `slsqp_unconstrained_global` is absent.
- **Method or command:** `rg -n "from power_ringmin import|from power_ringmin\.|import power_ringmin" verify.py`
- **Relevant output:** no matches; command returned exit code 1, ripgrep's no-match status.
- **Interpretation:** The new finite test coverage and direct verifier checks pass; the standalone verifier does not import the package; certified-search imports are absent.
- **Limitations:** SLSQP is numerical and finite-test evidence only; no certified optimum or theorem is established.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---verification`

## EV-006 - Handoff

- **Date:** 2026-07-10
- **Method or command:** `git status --short -uall`, `git diff`, and `git diff --check`.
- **Relevant output:** final status and diff were inspected; diff check passed.
- **Interpretation:** The review set is understood and ready for manual review.
- **Limitations:** The user still needs to review and commit manually if desired.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---handoff`
