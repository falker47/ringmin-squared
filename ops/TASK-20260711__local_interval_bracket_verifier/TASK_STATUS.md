# TASK_STATUS - TASK-20260711__local_interval_bracket_verifier / Local Interval Bracket Verifier

Last update: 2026-07-11

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Implement local fixed-order interval bracket verifier semantics before attempting a full global small-n certificate.
- **Expected output:** Package-local verifier helpers, focused tests, durable evidence, and updated global status.

## Scope

- **In scope:** One fixed-order interval bracket record; explicit negative-cycle lower endpoint checks; explicit witness-position upper endpoint checks; strict sign semantics; backend metadata that refuses tolerance-only certification; focused tests.
- **Out of scope:** Global small-n certificate aggregation; JSON schema for global certificates; production certified result artifacts; proving all mathematical obligations; Git staging or commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- Prior design is in `ops/TASK-20260711__interval_verifier_semantics/DESIGN.md`.
- Current high-precision and standalone verifiers use `mpmath` tolerance-based STN acceptance and are numerical evidence only.
- `src/power_ringmin/interval_verifier.py` now implements local fixed-order interval bracket checks with strict signs and no STN diagonal tolerance.
- The focused test fixture verifies one local n=3 bracket for canonical index order `(3,1,2)` / radius order `(9,1,4)`.

## Assumptions / Inferences

- The requested implementation is the local fixed-order bracket layer, not a global finite small-n certificate.
- The implementation exposes strict local semantics while avoiding any global optimum claim.
- A backend whose interval enclosure is not certification-capable must be rejected for certified local bracket verification.

## Decisions And Rationale

- Use `STRICT` mode because this task affects future certification semantics.
- Keep the new verifier package-local and focused on one bracket record.
- Require explicit edge kinds and explicit witness positions so serialized evidence does not depend on implicit STN edge order.
- Use a guarded `mpmath.iv` backend for the first angular interval oracle, with backend metadata documenting precision, guard, outward enclosure, and no-tolerance semantics.

## Plan And Expected Delta

- Create this task dossier. COMPLETE.
- Implement local interval bracket verifier helpers. COMPLETE.
- Add tests for accepted and rejected local brackets. COMPLETE.
- Run focused tests, full tests, and final diff checks. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests\test_interval_verifier.py`; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`; trailing-whitespace scan over changed tracked files and new untracked files.
- **Observed result:** Focused tests passed with `6 passed in 0.52s`; final full suite passed with `43 passed in 4.73s`; `git diff --check` produced no output; the trailing-whitespace scan found no matches.
- **Limitations:** Verification covers implementation behavior and one local n=3 fixture only. It does not generate a production interval artifact, aggregate every canonical order, certify a global optimum, or prove a theorem for all `n`.

## Blockers / Risks

- No current blocker.
- Residual risk: the first interval backend relies on `mpmath.iv` plus explicit guard widening; backend provenance should be revisited before production certificate publication.

## Next Atomic Action

- Implement a fixed-order interval bracket generator/exporter that emits records consumed by `src/power_ringmin/interval_verifier.py`.

## Handoff

- **Last verified result:** `python -m pytest` passed 43 tests; final diff checks passed.
- **Files changed:** `src/power_ringmin/interval_verifier.py`, `src/power_ringmin/__init__.py`, `tests/test_interval_verifier.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `ops/TASK-20260711__interval_verifier_semantics/DESIGN.md`, `src/power_ringmin/interval_verifier.py`, `tests/test_interval_verifier.py`.
