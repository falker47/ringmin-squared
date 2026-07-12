# CURRENT_STATUS - power-ringmin

Last update: 2026-07-12

- **Current phase:** synthesis and structural proof planning after checked-artifact CI stabilization.
- **Current task:** Create a concise next-research roadmap from checked `n=3..6` certificates, candidate/critical-structure evidence, verifier limitations, CI status, combinatorial growth, and the asymptotic conjecture.
- **Task dossier:** `ops/TASK-20260712__research_roadmap/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** prove or disprove the reduced-core insertion hypothesis on the existing checked `n=5,6` candidate orders, without generating `n=7`.
- **Awaiting user review:** yes.

## Current Stable Artifacts

`examples/finite_results_summary_n3_n6.json` is the checked derived finite-results summary under `power-ringmin.finite_results_summary.v1`. Its source certificate `content_sha256` values are line-ending-normalized source-content SHA-256 digests: CRLF and lone CR are normalized to LF before hashing, while all other byte changes remain digest-sensitive.

`ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json` records deterministic structural diagnostics for certified candidate orders at `n=3..6` under `power-ringmin.critical_structure_analysis.v1`.

`research/FINITE_RESULTS.md` summarizes the checked finite results, critical-cycle cores, upper-witness slack observations, weak-constraint proxy labels, conjectures, open questions, and warnings.

`research/NEXT_RESEARCH_STEPS.md` is the current research roadmap. It ranks reduced-core fixed-order analysis and all-pairs proof work ahead of larger exhaustive enumeration.

`docs/INTERVAL_BACKEND_TRUST.md` records the current guarded `mpmath.iv` interval-backend trust contract, tested coverage, unproved/audited gaps, classification implications, and future stronger trust paths.

`power-ringmin-verify-checked-artifacts` is the CI/local checked-artifact verification command. Locally it has verified 4 checked certificates with 76 embedded local brackets and the `n=3..6` finite-results summary. Current task context reports the hosted GitHub Actions workflow is green after the cross-platform finite-summary hash fix; this task did not independently query GitHub.

`.github/workflows/verification.yml` defines the GitHub Actions workflow and installs both `test` and `crosscheck` extras before running the full suite, checked-artifact semantic verification, schema validation tests, and whitespace hygiene checks.

## Current Research Finding

The checked `n=5` and `n=6` multiple-candidate cases point to a reduced lower-cycle core on indices `2..n`, with index `1` absent from the lower-core proxy but still present in some upper-witness near-critical constraints. This is a heuristic structural direction, not a certified floating-circle or all-`n` theorem.

The recommended next step is to test a precise reduced-core insertion hypothesis on the existing checked `n=5,6` candidates. This has higher research value than automatic `n=7` enumeration because it tries to explain the current candidate multiplicities and targets the all-pairs proof bottleneck behind the asymptotic conjecture.

## Proposed Next Task

Prove or disprove the reduced-core insertion hypothesis on the existing checked `n=5,6` candidate orders.

Acceptance criteria:

- define the fixed-order reduced-subsystem statement and endpoint semantics;
- compare each full candidate with its induced subsystem on indices `2..n`;
- report all constraints incident to index `1` with slack margins and evidence classifications;
- state whether the hypothesis is supported, falsified, or unresolved;
- update durable memory without generating `n=7`.

Stopping conditions:

- fixed-order STN equivalence has an unresolved wrap or endpoint-semantics gap;
- reduced systems do not reproduce the observed shared lower cores;
- constraints incident to index `1` are active or too close to classify under current precision;
- the only reason to continue would be that `n=7` is next.

Explicitly not next: `n=7` generation, `n=7` preflight, or larger exhaustive enumeration.
