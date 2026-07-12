# CURRENT_STATUS - power-ringmin

Last update: 2026-07-12

- **Current phase:** verification trust-layer hardening and CI for checked finite artifacts.
- **Current task:** Fix cross-platform finite-results source-content digests and install crosscheck extras in hosted CI.
- **Task dossier:** `ops/TASK-20260712__cross_platform_finite_hash_ci/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user reviews the normalized digest implementation, regenerated finite-results summary, tests, documentation, and workflow update, then decides whether to commit manually.
- **Awaiting user review:** yes.

## Current Stable Artifacts

`examples/finite_results_summary_n3_n6.json` remains the checked derived finite-results summary under `power-ringmin.finite_results_summary.v1`. Its source certificate `content_sha256` values are line-ending-normalized source-content SHA-256 digests: CRLF and lone CR are normalized to LF before hashing, while all other byte changes remain digest-sensitive.

`ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json` records deterministic structural diagnostics for certified candidate orders at `n=3..6` under `power-ringmin.critical_structure_analysis.v1`.

`research/FINITE_RESULTS.md` summarizes the checked finite results, critical-cycle cores, upper-witness slack observations, weak-constraint proxy labels, conjectures, open questions, and warnings.

`docs/INTERVAL_BACKEND_TRUST.md` records the current guarded `mpmath.iv` interval-backend trust contract, tested coverage, unproved/audited gaps, classification implications, and future stronger trust paths.

`power-ringmin-verify-checked-artifacts` is the CI/local checked-artifact verification command. Locally it verified 4 checked certificates with 76 embedded local brackets and the `n=3..6` finite-results summary.

`.github/workflows/verification.yml` defines the GitHub Actions workflow and now installs both `test` and `crosscheck` extras before running the claimed full test suite, but no hosted GitHub run has been observed or claimed yet.

## Current Verification-Trust Finding

The local fixed-order interval bracket verifier now requires exact local `artifact_type` and exact backend metadata matching for every field declared by the active oracle, including `rounding_policy`. Structural JSON Schema validation is tested for checked artifacts, but semantic Python validators remain authoritative for interval verification, source freshness, and derived summary consistency. The finite-results source freshness check is intentionally invariant under checkout line-ending differences only.

Current small-n certificate generation remains work-count bounded by explicit canonical-order and local retry ceilings; no wall-clock timeout has been added.

## Proposed Next Task

After manual review/commit, run or inspect the hosted GitHub Actions workflow result on GitHub and confirm the Linux checkout accepts the regenerated finite-results summary without changing mathematical claims.

Explicitly not next: `n=7` generation, `n=7` preflight, or larger exhaustive enumeration.
