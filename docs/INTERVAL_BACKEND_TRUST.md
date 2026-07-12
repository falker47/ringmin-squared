# Interval Backend Trust

This note records the current trust contract for checked finite interval
certificate artifacts. It does not upgrade any result classification.

## Current Backend

The local fixed-order interval verifier uses
`MPMathIntervalAngularOracle` from `src/power_ringmin/interval_verifier.py`.
That oracle is recorded in artifacts as:

```text
backend: mpmath_iv_guarded_atan2_v1
```

For each angular separation, the oracle asks `mpmath.iv` to evaluate interval
arithmetic at the recorded decimal precision. Because the local environment
does not expose `mpmath.iv.asin`, the oracle evaluates
`asin(x)` as `atan2(x, sqrt(1 - x*x))` on the interval input. It then widens
the final lower and upper endpoints by the recorded nonnegative
`guard_decimal`.

The verifier currently trusts `mpmath.iv` to provide interval arithmetic whose
computed interval endpoints enclose the real results of the operations used by
the oracle at the requested precision. The project additionally assumes that
the guarded `atan2` formulation encloses the mathematical angular separation
used in the Power-Ringmin constraints.

## Metadata Contract

Checked local interval brackets must declare backend metadata exactly matching
the oracle that verifies them:

- `backend`
- `precision_digits`
- `rounding_policy`
- `outward_enclosure`
- `certification_capable`
- `tolerance_based`
- `guard_decimal`

The verifier rejects tolerance-based interval metadata, missing or extra backend
metadata keys, backend strings other than the supported guarded `mpmath.iv`
backend, and tampered `rounding_policy` text. The local artifact type must also
be exactly `fixed_order_interval_bracket`.

## Guards

`guard_decimal` is a decimal widening applied after interval evaluation. It is
not a proof of backend correctness. Its role is to provide an explicit outward
margin around the interval endpoints used by the verifier. Current checked
finite artifacts use this guard as part of the documented backend contract.

## Assumed Outward-Enclosure Properties

For the current certificates to be interpreted as computer-certified finite
results under this backend contract, the project assumes:

- the interval returned for each `theta_R(a,b)` encloses the true angular
  separation for the positive decimal inputs;
- the interval returned for `2*pi` encloses the true value of `2*pi`;
- endpoint widening by `guard_decimal` preserves enclosure;
- decimal strings are parsed at the verifier's oracle precision, not at ambient
  global `mpmath` precision;
- the lower-endpoint negative-cycle check uses upper bounds that are genuinely
  outward with respect to the implemented STN inequalities;
- the upper-endpoint witness check uses lower slack bounds that are genuinely
  conservative for all pairwise constraints.

## What Has Been Tested

The repository tests check that:

- sampled `mpmath.iv` angular intervals contain independent high-precision
  `mpmath` evaluations for the tested cases;
- local interval brackets reject noncanonical orders, bad witness positions,
  nonnegative lower cycles, tolerance-based backend metadata, local artifact
  type tampering, and backend metadata tampering;
- local decimal parsing is performed at oracle precision even when ambient
  global `mpmath` precision is lowered;
- small-n certificate validation reloads embedded local brackets and rejects
  stale summaries or tampered embedded verifier metadata;
- checked `n=3,4,5,6` finite certificates reload through semantic validators;
- the checked finite-results summary reloads its source certificates, recomputes
  source hashes and derived content, and rejects stale summaries;
- JSON Schema tests validate the structural contract for checked examples.

## What Has Not Been Proved

The repository has not formally proved or independently audited:

- the implementation correctness of `mpmath.iv`;
- the directed-rounding behavior of `mpmath.iv` on every platform and version;
- the interval correctness of the `atan2(x, sqrt(1 - x*x))` inverse-sine
  formulation for all inputs in the certificate domain;
- a machine-checkable proof that the guard magnitude compensates for every
  possible backend issue;
- an independent interval-backend re-verification of the checked artifacts;
- exact optimum values, all-`n` theorems, or asymptotic theorems.

## Classification Implication

The checked finite brackets are therefore phrased as computer-certified results
under the repository's documented guarded `mpmath.iv` backend contract. They are
finite `n=3,4,5,6` certificates only. They are not exact optimum values, not
publication-grade independently audited certificates, and not evidence strong
enough to change any all-`n` or asymptotic classification.

## Stronger Trust Requirements

A stronger publication-grade trust claim would require at least one of the
following:

- an independently audited interval backend with documented directed rounding
  guarantees for the operations used here;
- cross-verification of all checked artifacts using an independent backend;
- a rational or algebraic conservative enclosure pipeline whose rounding steps
  are locally inspectable;
- platform/version pinning plus reproducible containers and independent reruns;
- machine-checkable proof artifacts for the interval transformations and STN
  implications;
- published review of the backend contract and generated certificates.

Possible future backends or cross-check paths include Arb/FLINT interval
arithmetic, MPFI-like interval arithmetic, a small custom rational interval
implementation for the required formulas, or independent high-precision
interval verification in another language.

## Bounded Generation Meaning

Current small-n certificate generation is work-count bounded. The general
exporter requires an explicit `--max-canonical-orders` ceiling, and each local
bracket search has a bounded retry count through `--local-max-attempts`.

There is no current wall-clock timeout in the mathematical verifier or
certificate generator. Adding one would be an operational control, not a change
to certificate semantics. It should be implemented only if it can be tested
deterministically and kept separate from semantic interval verification.
