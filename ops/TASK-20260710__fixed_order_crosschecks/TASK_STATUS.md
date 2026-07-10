# TASK_STATUS - TASK-20260710 / Fixed-Order Crosschecks

Last update: 2026-07-10

## State

- **Mode:** STRICT.
- **Status:** READY_FOR_REVIEW.
- **Objective:** import radius-sequence-aware fixed-order SLSQP cross-checks and a standalone high-precision verifier scaffold, without importing the certified-search pipeline.
- **Expected output:** tested fixed-order SLSQP validation, standalone mpmath verifier CLI for explicit fixed-order payloads, and durable evidence of what remains out of scope.

## Scope

- **In scope:** `power_ringmin.crosscheck.slsqp_fixed_order`; optional NumPy/SciPy dependency metadata; standalone root `verify.py` using only stdlib and mpmath; tests for quadratic fixed-order SLSQP and verifier behavior; provenance/status updates.
- **Out of scope:** upstream unconstrained global SLSQP; certified search; frontier/pruning verification; result artifact schema; CLI package entry point; plots; original Ringmin results.

## Verified Facts

- Startup files and relevant task memory were read at task start.
- The local working tree was clean at task start.
- Upstream Ringmin was inspected read-only at commit `cc0327400819fe06b230d967cdcbafffe1648317`.
- Upstream `crosscheck.py` contains a reusable fixed-order SLSQP function and an original-radii unconstrained global helper.
- Upstream root `verify.py` is coupled to original Ringmin result artifacts and frontier certificates; only its standalone high-precision STN pattern was suitable for this task.
- `src/power_ringmin/crosscheck.py`, root `verify.py`, and `tests/test_crosscheck_and_verifier.py` have been added.
- The certified-search pipeline remains unimported.

## Assumptions / Inferences

- NumPy/SciPy should be optional package extras because the core fixed-order STN package only requires mpmath.
- The standalone verifier should accept explicit order/radius inputs and minimal JSON payloads before a Power-Ringmin artifact schema exists.
- Direct subprocess-based verifier tests are brittle under the local Windows/Python 3.14 pytest handle environment; testing `verify.main()` with patched argv plus direct shell invocations verifies the intended behavior with less harness noise.

## Decisions And Rationale

- Use STRICT mode because this task imports validation infrastructure and records numerical evidence.
- Export `slsqp_fixed_order` and `SLSQPCheckResult` at package top level; their module performs lazy NumPy/SciPy imports only when the optimizer is called.
- Use scale-aware SLSQP starting radii based on the actual radius sequence, not upstream's `4*n*n` original-radii bound.
- Omit `slsqp_unconstrained_global` because it hardcodes `range(1,n+1)` and belongs with a later radius-sequence-aware search design.
- Keep `verify.py` independent of `src/power_ringmin` so it can later serve as an independent verifier rather than a generator self-check.

## Plan And Expected Delta

- Completed: inspected upstream fixed-order SLSQP and verifier sources.
- Completed: added radius-sequence-aware fixed-order SLSQP cross-checks.
- Completed: added standalone high-precision fixed-order verifier scaffold.
- Completed: added tests and dependency metadata.
- Completed: verified and recorded scope boundaries.

## Verification

- **Checks:** package import/environment check; baseline and final `python -m pytest`; Python compilation; direct standalone verifier pass/fail invocations; source search for excluded search/frontier imports; final Git status/diff/diff-check.
- **Observed result:** final pytest passed 8 tests; Python compilation passed; direct verifier accepted the high-precision radius for `(1,4,9)` and rejected a radius smaller by `1e-8`; source search found no certified-search imports.
- **Limitations:** SLSQP tests are finite numerical cross-checks only; they establish no global optimum, no certificate, and no theorem. The verifier scaffold does not yet understand future Power-Ringmin artifact schemas or frontier certificates.

## Blockers / Risks

- No blocker currently known.
- Risk: SLSQP remains a numerical optimizer and can be sensitive to starts and tolerances for larger instances.
- Risk: the standalone verifier's JSON schema is intentionally minimal and may need migration once result artifacts are designed.

## Next Atomic Action

- Review this validation-layer diff and decide whether to commit manually.

## Handoff

- **Last verified result:** final verification checks passed and task is ready for review.
- **Files changed:** `pyproject.toml`, `requirements.txt`, `src/power_ringmin/__init__.py`, `src/power_ringmin/crosscheck.py`, `verify.py`, `tests/test_crosscheck_and_verifier.py`, `UPSTREAM_RINGMIN.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `src/power_ringmin/crosscheck.py`, `verify.py`, `tests/test_crosscheck_and_verifier.py`, and this dossier.
