# TASK_STATUS - TASK-20260723 / KPGZERO Local CF Criterion

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** refine KPGZERO-24 into an exact admission criterion on the
  local continued-fraction data of each convergent of \(\xi\), without
  scanning \(m\), while preserving both branches and every half-open
  endpoint.
- **Expected output:** signed complete-quotient error identity; four
  branch/sign scale windows; exact congruence-domain integer interval and
  residue-aware admission discriminant; a fixed-case standard-library
  falsification diagnostic; synchronized proof, synopsis, roadmap, status,
  stable memory, and dossier.

## Scope

- **In scope:** KPGZERO-20--KPGZERO-24; regular convergents of the fixed
  irreducible cubic root; exact scale congruence and domain; all four
  branch/sign quadratics; half-open rounding; direct reconstruction of
  \(m\); fixed non-generative diagnostic cases.
- **Out of scope:** a theorem deciding global finiteness or infinitude;
  generated convergent or \(m\)-sweeps; production code, public tests,
  schemas, artifacts, support classification, induced-\(K\) reevaluation, or
  geometry.

## Verified Facts

- The exact signed error is
  \[
  \xi-{p_\nu\over q_\nu}
  ={(-1)^\nu\over
    q_\nu^2(\alpha_{\nu+1}+q_{\nu-1}/q_\nu)}.
  \]
- Factoring the cubic at \(\xi\) makes the sign of \(\Phi(p_\nu,q_\nu)\)
  equal to \((-1)^\nu\) and expresses its magnitude through the same local
  complete-quotient data.
- Each sign/branch case is one convex integer quadratic
  \(A_\nu g^2-bg+C\le0\), with the constants \(21,31,39\) retaining the
  audited half-open semantics.
- Domain and congruence reduce all candidate scales to one finite arithmetic-
  progression interval. The integer admission discriminant
  \(\mathfrak D_{\delta,\nu}\) is nonnegative exactly when that interval is
  nonempty.
- Every admitted scale reconstructs \(m\) directly; no \(m\)-scan is part
  of the criterion.

## Assumptions / Inferences

- The prior exact KPGZERO parametrization and proof that every admitted
  primitive ratio is a regular convergent remain inputs.
- No inference from the fixed diagnostic cases to the global frequency of
  admitted convergents is permitted.

## Decisions And Rationale

- Keep the four quadratic rows separate rather than hiding branch or sign
  in a single asymptotic coefficient.
- Distinguish the ordinary quadratic discriminant from the discrete,
  residue-aware admission discriminant; the former alone need not admit an
  integer in the required class.
- Use `isqrt` and signed integer ceiling division in the diagnostic so
  square and nonsquare radical endpoints receive exact closed-boundary
  semantics.
- Retain KPGZERO-24 as an unresolved global frequency statement after
  closing the local decision problem.

## Plan And Expected Delta

- Complete STRICT startup and inspect predecessor proof/dossier. COMPLETE.
- Derive and independently audit the local criterion. COMPLETE.
- Add the fixed-case standard-library diagnostic. COMPLETE.
- Synchronize proof, synopsis, stable memory, roadmap, and status. COMPLETE.
- Run repository regression, artifact verification, and final diff audit.
  COMPLETE.

## Verification

- **Checks:** new exact diagnostic; Ruff; predecessor KPGZERO diagnostics;
  full pytest; schema test; checked-artifact verifier; KPGZERO tag/reference
  audit; Git status/diff/diff-check.
- **Observed result:** all three KPGZERO diagnostics PASS; scoped Ruff PASS;
  full suite 283 passed; schema test 4 passed; four checked certificates and
  76 local brackets verified; independent mathematical and cross-document
  audit PASS; tag/reference and final diff hygiene PASS.
- **Limitations:** fixed examples can falsify a transcription or endpoint
  error but cannot prove the symbolic theorem or decide global frequency.

## Blockers / Risks

- No workflow blocker.
- Residual scientific uncertainty: no theorem here decides whether
  \(\mathfrak D_{\delta,\nu}\ge0\) for infinitely many convergents.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** (KPGZERO-24a)--(KPGZERO-24h) give the exact local
  test; every required diagnostic, regression, artifact, source, and diff
  check passes.
- **Files changed:** `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`,
  `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, and this four-file task dossier.
- **Files to read first:** the KPGZERO-23--KPGZERO-24 subsection of
  `research/FIXED_ORDER_CYCLE_RATIO.md`, then `EVIDENCE.md`.
