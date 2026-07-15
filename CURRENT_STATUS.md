# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** bounded independent interval-backend trust cross-check.
- **Current task:** independently cross-check the checked `n=3` artifact with
  Arb through python-flint, strictly outside the production verifier.
- **Task dossier:**
  `ops/TASK-20260715__n3_arb_interval_crosscheck/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- `tests/test_n3_arb_interval_crosscheck.py` directly loads
  `examples/small_n_interval_certificate_n3.json` with the standard JSON
  parser and imports no production verifier, artifact loader, geometry helper,
  or high-precision proposal code.
- At a fixed 384-bit working precision it recomputes every required
  \(\theta_R(a,b)\) with Arb `sqrt` and direct `asin`, and recomputes
  \(2\pi\) with `arb.pi()`.
- It requires complete bounded coverage: one embedded canonical local bracket,
  three lower-cycle edge occurrences, all three unordered upper-witness pairs,
  and six directional slack lower bounds.
- `python-flint==0.9.0` is declared only in the optional `test` extra. Arb is
  not a runtime dependency or supported production verifier backend.
- No checked artifact, schema, bracket, generator, production verifier,
  supported backend, classification, or certified claim changed.

## Independent Endpoint Results

- LOCAL VERIFIED FACT (FINITE TEST-ONLY INDEPENDENT BACKEND CROSS-CHECK): on
  local Windows/Python 3.14.3 with python-flint 0.9.0, FLINT 3.6.0, and
  384-bit Arb, the recomputed relaxed-cycle upper bound is
  `-0.000345795701878590132147302156819834911873698761077819835981980`,
  which is strictly negative.
- All six independently recomputed upper-witness slack lower bounds are
  nonnegative. The minimum is
  `7.81249999999907777683967055517418065596493567633097672062408e-5`.
- INTERPRETATION: this corroborates the decisive endpoint signs for the single
  checked `n=3` record. It does not audit Arb/FLINT, cover `n=4,5,6`, or
  upgrade the guarded `mpmath.iv` production certificate contract.

## Verification

- Optional-extra installation passed:
  `python -m pip install -e ".[test,crosscheck]"`.
- Backend query reported Python `3.14.3`, python-flint `0.9.0`, and FLINT
  `3.6.0`; `python -m pip check` reported no broken requirements.
- Focused Arb module passed all 3 tests in 0.14 seconds.
- The complete repository suite passed all 204 tests in 61.24 seconds.
- Explicit checked-artifact schema validation passed all 4 tests in 1.11
  seconds.
- The unchanged semantic verifier accepted 4 certificates, 76 embedded local
  brackets, and the checked `n=3..6` summary.
- Targeted Ruff and Python compilation passed. The optional-dependency scope
  audit confirmed that runtime dependencies remain unchanged.
- The complete tracked diff and all new files were inspected; the production
  `src/`, `examples/`, `schemas/`, and `.github/` trees have no tracked diff.
  The changed/new-file trailing-whitespace scan and `git diff --check` passed,
  and nothing is staged.
- CURRENT HOSTED STATUS: GitHub Actions on Ubuntu/Python 3.11-3.13 has not
  been run or independently verified for this worktree.

## Files Changed

- `tests/test_n3_arb_interval_crosscheck.py` adds the isolated checker and
  deterministic coverage/sign tests.
- `pyproject.toml` adds python-flint only to the optional test extra.
- `docs/INTERVAL_BACKEND_TRUST.md` records backend/version, method, commands,
  results, classification, and limitations.
- `research/FIXED_ORDER_ANGULAR_STN.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `start.md`, and `PROJECT_KNOWLEDGE.md` synchronize the bounded result and
  preserve its non-consequences.
- The STRICT task dossier records chronology and independently understandable
  evidence.

## Residual Limitations

- The cross-check covers only the existing checked `n=3` artifact.
- Arb/FLINT, python-flint, decimal conversion, and the test implementation are
  trusted dependencies, not formally audited or machine-proved here.
- The complete checked `n=3..6` artifact set has not received independent Arb
  coverage.
- Hosted GitHub Actions for this worktree has not been run or independently
  verified.

## Proposed Next Task

In a fresh chat, extend the same bounded test-only Arb method to the existing
checked `n=4` artifact, without changing artifacts, schemas, brackets,
production verification, supported backends, or certified claims.
