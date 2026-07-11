# DESIGN - N=4 Finite-Certificate Next Step

## Question

Choose the next finite-certificate step for `n=4`:

- a runtime-bounded interval certificate attempt; or
- verifier/format hardening before attempting larger certificates.

## Decision

Proceed next with a runtime-bounded `n=4` interval certificate attempt.

Do not start broad verifier/format hardening before the `n=4` artifact attempt. The existing local interval bracket verifier and small-n aggregate validator already support the required `n=4` semantics, and a bounded in-memory probe generated and validated all three canonical `n=4` local brackets quickly.

## Basis

- VERIFIED FACT: `n=4` has three canonical cyclic index orders under the repository convention:
  `(4, 1, 2, 3)`, `(4, 1, 3, 2)`, and `(4, 2, 1, 3)`.
- VERIFIED FACT: an in-memory probe using `digits=80`, `guard_decimal=1e-70`, and `radius_eta=1e-4` generated one verified local interval bracket for each of those three orders.
- VERIFIED FACT: the same probe accepted the aggregate through `build_small_n_interval_certificate(..., n=4)` and `validate_small_n_interval_certificate_artifact`.
- INTERPRETATION: this is readiness evidence for a checked `n=4` artifact task, not a durable checked `n=4` artifact yet.

## Next Task Shape

Implement the smallest reproducible `n=4` certificate promotion:

- add a bounded export path for a finite small-n interval certificate at `n=4`;
- generate exactly the three canonical `n=4` local interval brackets;
- aggregate them with the existing small-n interval certificate validator;
- check in `examples/small_n_interval_certificate_n4.json` only if validation passes;
- add focused tests that load the checked artifact, verify coverage count `3`, and reject tampering;
- preserve `computer_certified_result` classification only under the documented local interval-verifier semantics and guarded `mpmath.iv` backend contract.

The export path may either be a narrow `n=4` command or a small generalization of the current `n=3` command, but it must not silently open the door to unbounded larger-`n` certificate generation. If generalized, it should include an explicit ceiling such as `--max-canonical-orders` with a default that admits `n=4` but prevents accidental larger runs.

## Runtime Bound

The `n=4` task should be bounded by:

- expected canonical order count: exactly `3`;
- local bracket generator `max_attempts`: keep an explicit finite value;
- precision parameters recorded in the artifact: start with `digits=80`, `guard_decimal=1e-70`, and `radius_eta=1e-4`;
- no checked partial artifact on timeout or failed local verification.

## Verification Plan

The `n=4` implementation task should run:

- focused small-n interval certificate tests;
- a checked-artifact load/validation test for `examples/small_n_interval_certificate_n4.json`;
- full `python -m pytest`;
- `git diff --check`;
- final status and diff inspection.

## Deferred Hardening

After a checked `n=4` artifact exists, the next hardening task should review:

- whether the certificate schema should be declared independently of the implementation module;
- whether the guarded `mpmath.iv` backend needs a stronger outward-rounding audit or a different interval backend;
- whether aggregate artifacts should store external local-bracket files instead of embedding every local record;
- whether larger `n` runs need resumable batch generation and per-order failure reports.

Those are real issues, but they are better informed by one nontrivial checked artifact beyond `n=3`.
