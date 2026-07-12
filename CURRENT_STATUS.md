# CURRENT_STATUS - power-ringmin

Last update: 2026-07-12

- **Current phase:** induced-subset all-`n` lower-bound strengthening integrated; exact asymptotic leading constant and matching upper bound remain open.
- **Current task:** Strengthen the all-`n` lower bound using induced subsets of circles and determine the status of the former \(n^3/(6\pi)\) targets.
- **Task dossier:** `ops/TASK-20260712__induced_subset_lower_bound/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Stable Artifacts

`research/ALL_N_LOWER_BOUND.md` records the self-contained induced-subset lower
bound. For every subset \(S\) of at least three indices in an all-pairs feasible
configuration, the induced cyclic order has positive gaps summing to \(2\pi\);
all-pairs feasibility applies to each induced adjacent pair; and the duplicated
multiset pairing lemma gives the product lower bound.

For every `n>=4` and `1<=m<=n-2`,

\[
R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
\qquad
P_{m,n}
=
\sum_{k=m}^n k(m+n-k)
=
\frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
\]

Choosing \(m=\lceil(\sqrt2-1)n\rceil\) gives

\[
R_2^*(n)
\ge
\frac{2(\sqrt2-1)}{3\pi}n^3-O(n^2),
\]

and therefore

\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
\ge
4(\sqrt2-1)>1.
\]

Consequently the former conjectural target
\[
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))
\]
is a DISPROVED CLAIM, and the former stronger target
\[
R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)
\]
is also a DISPROVED CLAIM.

`tests/test_induced_subset_lower_bound.py` contains finite diagnostic tests for
the formula \(P_{m,n}\), the moderate-`n` discrete maximizer over \(m\), and
pairing bounds on some nonconsecutive subsets and induced orders. These tests
are finite verifications only; they are not the all-`n` proof.

`examples/finite_results_summary_n3_n6.json` is the checked derived finite-results summary under `power-ringmin.finite_results_summary.v1`. Its source certificate `content_sha256` values are line-ending-normalized source-content SHA-256 digests: CRLF and lone CR are normalized to LF before hashing, while all other byte changes remain digest-sensitive.

`ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json` records deterministic structural diagnostics for certified candidate orders at `n=3..6` under `power-ringmin.critical_structure_analysis.v1`.

`research/FINITE_RESULTS.md` summarizes the checked finite results, critical-cycle cores, upper-witness slack observations, weak-constraint proxy labels, conjectures, open questions, and warnings.

`research/NEXT_RESEARCH_STEPS.md` is the current research roadmap. It no longer treats \(n^3/(6\pi)\) as an open target; it treats that asymptotic target and the \(n^3/(6\pi)+O(n^2)\) target as disproved claims and defers upper-bound construction work.

`docs/INTERVAL_BACKEND_TRUST.md` records the current guarded `mpmath.iv` interval-backend trust contract, tested coverage, unproved/audited gaps, classification implications, and future stronger trust paths.

`power-ringmin-verify-checked-artifacts` is the CI/local checked-artifact verification command. In the induced-subset lower-bound task it verified 4 checked certificates with 76 embedded local brackets and the `n=3..6` finite-results summary.

`.github/workflows/verification.yml` defines the GitHub Actions workflow and installs both `test` and `crosscheck` extras before running the full suite, checked-artifact semantic verification, schema validation tests, and whitespace hygiene checks.

## Current Research Finding

The all-`n` induced-subset lower bound strictly exceeds the former leading
target after normalization:

\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
\ge
4(\sqrt2-1)>1.
\]

This is independent of the checked finite certificates and should not be
described as an exact optimum result, a matching upper bound, or an exact
asymptotic leading constant.

## Proposed Next Task

Build a finite diagnostic comparison between the checked `n=3..6` brackets and
the best finite induced-subset lower bound
\[
\max_{1\le m\le n-2}\left(\frac{P_{m,n}}{\pi}-n^2\right).
\]

Acceptance criteria:

- compute the best induced-subset lower bound for `n=3..6` using exact integer
  \(P_{m,n}\) arithmetic and high-precision decimal output;
- compare it with the checked finite lower and upper endpoints without changing
  any finite-certificate classification;
- state clearly that the table is a finite diagnostic, not an all-`n` proof or
  an upper-bound construction;
- update durable memory and task evidence without generating new certificates.

Stopping conditions:

- source finite summaries fail semantic verification;
- the comparison requires changing certificate artifacts;
- the task drifts into upper-bound construction, leading-order LP work, or new
  certificate generation.
