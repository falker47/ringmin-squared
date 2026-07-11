# TASK_STATUS - TASK-20260711__n3_global_interval_certificate_fixture / N=3 Global Interval Certificate Fixture

Last update: 2026-07-11

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Implement a tiny global n=3 interval certificate aggregator/fixture that verifies one local bracket for every canonical order.
- **Expected output:** Package helper, focused tests, durable evidence, and updated global status.

## Scope

- **In scope:** Finite n=3 aggregation; independent canonical order-space regeneration; verification of each embedded local fixed-order interval bracket; finite global bracket computation; JSON round-trip helpers if useful.
- **Out of scope:** Production-scale n certification, new interval arithmetic backend, theorem-for-all-n claims, CLI polish, Git staging or commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- `CURRENT_STATUS.md` identified this task as the proposed next atomic action after the fixed-order interval bracket exporter.
- Existing local fixed-order interval verification is implemented in `src/power_ringmin/interval_verifier.py`.
- Existing one-order interval bracket generation is implemented in `src/power_ringmin/interval_bracket_exporter.py`.
- Existing canonical order enumeration is implemented in `src/power_ringmin/search_small_n.py`.

## Assumptions / Inferences

- The requested fixture should certify finite n=3 coverage under the repository's local interval-verifier semantics, not establish a theorem for all n.
- The aggregator should embed local records so validation can re-run local verification and coverage checks from one artifact.

## Decisions And Rationale

- Use `STRICT` mode because this task creates finite certificate aggregation logic.
- Keep the aggregator small and package-level; no CLI is needed for the n=3 fixture task.

## Plan And Expected Delta

- Create this task dossier. COMPLETE.
- Implement a small global interval certificate aggregator and n=3 fixture helper. COMPLETE.
- Add focused tests for n=3 coverage, round-trip validation, and rejection paths. COMPLETE.
- Run focused tests, full tests, and final diff checks. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests\test_small_n_interval_certificate.py`; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`; trailing-whitespace scan over changed tracked files and new untracked files.
- **Observed result:** Focused tests passed with `4 passed in 1.07s`; full test suite passed with `52 passed in 9.31s`; `git diff --check` produced no output; the trailing-whitespace scan found no matches.
- **Limitations:** The fixture certifies finite n=3 coverage under the repository's local interval-verifier semantics only. It does not prove a theorem for all `n`, establish an asymptotic result, or resolve interval-backend provenance for production publication.

## Blockers / Risks

- No current blocker.
- Residual risk: the certificate remains finite n=3 evidence under the documented guarded `mpmath.iv` interval-backend contract; backend provenance remains a future production-certification concern.

## Next Atomic Action

- User reviews the n=3 global interval certificate fixture diff and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed 52 tests.
- **Files changed:** `src/power_ringmin/small_n_interval_certificate.py`, `tests/test_small_n_interval_certificate.py`, `src/power_ringmin/__init__.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `src/power_ringmin/small_n_interval_certificate.py`, `tests/test_small_n_interval_certificate.py`.
