# CURRENT_STATUS - power-ringmin

Last update: 2026-07-12

- **Current phase:** all-`n` lower-bound proof integrated; matching upper-bound proof work remains open.
- **Current task:** Formalize and integrate the all-`n` Power-Ringmin lower bound from adjacent product sums.
- **Task dossier:** `ops/TASK-20260712__all_n_lower_bound/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** formulate and test a candidate all-pairs upper-bound inequality family for one explicit structured cyclic order, without generating `n=7`.
- **Awaiting user review:** yes.

## Current Stable Artifacts

`research/ALL_N_LOWER_BOUND.md` records the self-contained exact theorem:
for every `n>=3`,

\[
R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2,
\]

and therefore

\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}\ge 1.
\]

The proof uses a rearrangement-pairing lower bound for
\(\sum_k\sigma_k\sigma_{k+1}\), the adjacent-gap consequence of all-pairs
feasibility, and the inequality
\(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\). It does not require non-adjacent
constraint control; non-adjacent control remains necessary for a matching
upper-bound construction.

`examples/finite_results_summary_n3_n6.json` is the checked derived finite-results summary under `power-ringmin.finite_results_summary.v1`. Its source certificate `content_sha256` values are line-ending-normalized source-content SHA-256 digests: CRLF and lone CR are normalized to LF before hashing, while all other byte changes remain digest-sensitive.

`ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json` records deterministic structural diagnostics for certified candidate orders at `n=3..6` under `power-ringmin.critical_structure_analysis.v1`.

`research/FINITE_RESULTS.md` summarizes the checked finite results, critical-cycle cores, upper-witness slack observations, weak-constraint proxy labels, conjectures, open questions, and warnings.

`research/NEXT_RESEARCH_STEPS.md` is the current research roadmap. It now treats the lower-bound constant as proved and ranks all-pairs upper-bound domination work ahead of larger exhaustive enumeration.

`docs/INTERVAL_BACKEND_TRUST.md` records the current guarded `mpmath.iv` interval-backend trust contract, tested coverage, unproved/audited gaps, classification implications, and future stronger trust paths.

`power-ringmin-verify-checked-artifacts` is the CI/local checked-artifact verification command. Locally it has verified 4 checked certificates with 76 embedded local brackets and the `n=3..6` finite-results summary. Current task context reports the hosted GitHub Actions workflow is green after the cross-platform finite-summary hash fix; this task did not independently query GitHub.

`.github/workflows/verification.yml` defines the GitHub Actions workflow and installs both `test` and `crosscheck` extras before running the full suite, checked-artifact semantic verification, schema validation tests, and whitespace hygiene checks.

## Current Research Finding

The all-`n` lower-bound side of the conjectured leading constant is proved:

\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}\ge 1.
\]

This is independent of the checked finite certificates and should not be
described as an exact optimum result or as the full asymptotic conjecture. The
remaining mathematical bottleneck is the matching upper-bound direction, where
every non-adjacent pair constraint must be controlled for a proposed structured
order and gap allocation.

## Proposed Next Task

Formulate and test a candidate all-pairs upper-bound inequality family for one
explicit structured cyclic order.

Acceptance criteria:

- state one explicit order family and gap-allocation rule;
- prove or diagnose the adjacent leading sum at the target radius;
- translate every non-adjacent pair into a symbolic interval-sum inequality;
- use finite checks only as diagnostics, not as all-`n` proof;
- update durable memory without generating `n=7`.

Stopping conditions:

- fixed-order STN/geometric equivalence has an unresolved endpoint or wrap semantics gap;
- non-adjacent inequalities fail for small symbolic subfamilies or checked finite diagnostics;
- angular error terms cannot be made uniform in the target radius regime;
- the only reason to continue would be that `n=7` is the next integer.
