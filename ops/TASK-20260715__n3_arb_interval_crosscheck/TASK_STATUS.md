# TASK_STATUS - TASK-20260715__n3_arb_interval_crosscheck / Independent Arb Cross-Check For Checked n=3 Artifact

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Independently cross-check the checked `n=3` interval artifact with Arb through the optional test dependency `python-flint`, without calling the production `MPMathIntervalAngularOracle` or reusing its enclosures.
- **Expected output:** A test-only Arb cross-check with deterministic embedded-data coverage and endpoint-sign assertions, optional dependency metadata, trust-note documentation, and reproducible verification evidence.

## Scope

- **In scope:** `examples/small_n_interval_certificate_n3.json`; test-local direct JSON parsing; test-local canonical `n=3` order regeneration; outward Arb recomputation of every required `theta_R` and `2*pi`; lower negative-cycle upper bound; all-pairs upper-witness slack lower bounds; optional test dependency; documentation and durable memory.
- **Out of scope:** `n>3`; changes to checked artifacts, schemas, certificate brackets, production verifier code, supported production backends, generators, or certified claims; Git staging, commits, pushes, merges, rebases, resets, or history edits.

## Verified Facts

- The repository root and mandatory startup files were inspected.
- Initial `git status --short --branch` reported only `## main...origin/main`; the worktree was clean.
- The checked `n=3` artifact embeds one local bracket, a three-edge lower negative cycle, and one three-position upper witness.
- `python-flint` was not installed in the initial local environment.
- The current production backend remains `MPMathIntervalAngularOracle` / `mpmath_iv_guarded_atan2_v1`.

## Assumptions / Inferences

- A test-local implementation using only the standard library, pytest, and `flint.arb` is the smallest enforceable separation from the production verifier.
- Adding `python-flint` only to the `test` extra keeps Arb outside runtime and production-backend dependencies.
- The result will be classified as a local verified finite test-only cross-check, not as an upgraded certificate classification.

## Decisions And Rationale

- Use Arb's rigorous real ball arithmetic at a fixed 384-bit working precision.
- Evaluate the angular formula directly with Arb `sqrt` and `asin`, which is independent of the production `mpmath.iv` guarded `atan2` implementation.
- Parse every artifact decimal from its string representation and never through binary float.
- Require exact coverage of all embedded `n=3` records, lower-cycle edge occurrences, upper-witness pairs, and both slacks per pair.

## Plan And Expected Delta

- Complete startup, source, artifact, trust, and dependency inspection. COMPLETE.
- Create this STRICT task dossier. COMPLETE.
- Add the isolated Arb test module and optional test dependency. COMPLETE.
- Install the test extra and run focused plus full verification. COMPLETE.
- Update the trust note and durable project memory. COMPLETE.
- Inspect final status, diff, and hygiene; set `READY_FOR_REVIEW`. COMPLETE.

## Verification

- **Checks:** Python compile; optional-extra install; backend/version query; focused Arb tests; diagnostic bound extraction; `pip check`; full pytest; checked-artifact semantic verifier; explicit schema tests; Ruff; dependency-scope audit; production-tree invariant diff; status/diff inspection; changed/new-file trailing-whitespace scan; `git diff --check`.
- **Observed result:** python-flint 0.9.0 / FLINT 3.6.0 installed under Python 3.14.3; focused module `3 passed`; full suite `204 passed`; schema module `4 passed`; semantic verifier accepted 4 certificates and 76 local brackets; decisive Arb bounds have the required strict/non-strict signs; all final source, diff, and hygiene checks passed.
- **Limitations:** The cross-check covers only checked artifact `n=3` and does not audit Arb/FLINT, python-flint, decimal conversion, or the test implementation itself.

## Blockers / Risks

- No current blocker. Hosted CI has not been run for this worktree.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** All implementation, focused/full tests, invariant production checks, documentation, diff, and hygiene verification pass locally; task status is `READY_FOR_REVIEW`.
- **Files changed:** `tests/test_n3_arb_interval_crosscheck.py`, `pyproject.toml`, `docs/INTERVAL_BACKEND_TRUST.md`, `research/FIXED_ORDER_ANGULAR_STN.md`, `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this dossier.
- **Files to read first:** `docs/INTERVAL_BACKEND_TRUST.md`, `examples/small_n_interval_certificate_n3.json`, `tests/test_n3_arb_interval_crosscheck.py`, and this dossier.
