# Interval Backend Trust

This note records the current trust contract for checked finite interval
certificate artifacts. It does not upgrade any result classification.

The exact mathematical interface is proved independently in
`research/FIXED_ORDER_ANGULAR_STN.md`: genuine angular and \(2\pi\)
enclosures imply strict lower-endpoint exclusion through a negative cycle and
closed upper-endpoint inclusion through an all-pairs witness. This trust note
records the separate, unproved premise that the current backend and bound
post-processing provide those genuine enclosures.

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
used in the Power-Ringmin constraints. The trust boundary continues through
endpoint extraction, conversion to `mp.mpf`, decimal parsing, scalar bound
arithmetic, and the final sign comparisons; these steps have not been replaced
by a separately audited exact-arithmetic pipeline.

## Bounded Independent Arb Cross-Check

LOCAL VERIFIED FACT (FINITE TEST-ONLY INDEPENDENT BACKEND CROSS-CHECK):
`tests/test_n3_arb_interval_crosscheck.py` independently rechecks the existing
checked `n=3` artifact with Arb through python-flint. This path is test-only;
the production/default verifier remains `MPMathIntervalAngularOracle` with
backend identifier `mpmath_iv_guarded_atan2_v1`.

The test reads `examples/small_n_interval_certificate_n3.json` directly with
the standard JSON parser. It imports no production verifier, artifact loader,
geometry helper, or high-precision proposal code, and it neither calls
`MPMathIntervalAngularOracle` nor reads its theta/tau enclosures or stored
mpmath-derived sign summaries. Every artifact decimal used in the check is
passed to Arb as its original string, never through binary float. At 384-bit
working precision the test independently evaluates

\[
\theta_R(a,b)
=
2\arcsin\sqrt{\frac{ab}{(R+a)(R+b)}}
\]

with Arb's direct `sqrt` and `asin`, and independently evaluates
\(2\pi=2\operatorname{arb.pi}()\). Arb ball operations and directed
`lower()` / `upper()` extraction provide the outward bounds used by this
cross-check.

The embedded-data coverage contract is exact and bounded: one canonical
`n=3` local bracket, all three serialized lower-cycle edge occurrences, all
three unordered upper-witness pairs, and both directional slacks for each pair
(six slack lower bounds). The recomputed relaxed-cycle upper bound is

```text
-0.000345795701878590132147302156819834911873698761077819835981980
```

and the least recomputed upper-witness slack lower bound is

```text
7.81249999999907777683967055517418065596493567633097672062408e-5
```

so the lower sign is strictly negative and every upper-witness slack lower
bound is nonnegative.

The reproducibility record for the 2026-07-15 local Windows run is:

```text
Python:       3.14.3
python-flint: 0.9.0
FLINT:        3.6.0
Arb precision: 384 bits

python -m pip install -e ".[test,crosscheck]"
  PASS; installed power-ringmin 0.1.0 editable and python-flint 0.9.0

python -m pytest tests\test_n3_arb_interval_crosscheck.py -vv
  3 passed in 0.14s

python -m pytest
  204 passed in 61.24s

$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts
  verified checked artifacts certificates=4 local_brackets=76
  summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6
```

This result independently corroborates the decisive endpoint signs for the
single checked `n=3` record. It does not audit or prove python-flint, FLINT,
Arb, decimal-to-Arb conversion, or the test implementation correct; it does
not cover `n=4,5,6`; and it is not a publication-grade verification of the
complete checked-artifact set. No checked artifact, schema, bracket,
production-supported backend, or certified claim is changed or reclassified.

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

The checked-artifact and default production loading paths reject
tolerance-based interval metadata, missing or extra backend metadata keys,
backend strings other than the supported guarded `mpmath.iv` backend, and
tampered `rounding_policy` text. The local artifact type must also be exactly
`fixed_order_interval_bracket`. Unit tests may inject a protocol-compatible
oracle with matching test metadata; that does not add a supported production
backend.

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
- conversion of interval endpoints to `mp.mpf` and subsequent scalar sums and
  differences preserve the conservative direction required by each bound;
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
- a recomputed lower cycle-sum upper bound equal to zero is rejected, while a
  recomputed upper witness slack lower bound equal to zero is accepted because
  the geometric constraints are closed;
- local decimal parsing is performed at oracle precision even when ambient
  global `mpmath` precision is lowered;
- small-n certificate validation reloads embedded local brackets and rejects
  stale summaries or tampered embedded verifier metadata;
- checked `n=3,4,5,6` finite certificates reload through semantic validators;
- the checked finite-results summary reloads its source certificates, recomputes
  source content digests and derived content, and rejects stale summaries;
- JSON Schema tests validate the structural contract for checked examples.
- the bounded test-only Arb path independently recomputes the checked `n=3`
  lower cycle and all upper-witness slacks, requires complete embedded-record,
  edge, and pair coverage, and obtains decisive signs without the production
  oracle or its enclosures.

## What Has Not Been Proved

The repository has not formally proved or independently audited:

- the implementation correctness of `mpmath.iv`;
- the directed-rounding behavior of `mpmath.iv` on every platform and version;
- the interval correctness of the `atan2(x, sqrt(1 - x*x))` inverse-sine
  formulation for all inputs in the certificate domain;
- conservative rounding of interval endpoint extraction and the later scalar
  `mp.mpf` bound arithmetic on every supported platform;
- a machine-checkable proof that the guard magnitude compensates for every
  possible backend issue;
- an independent interval-backend re-verification of the full checked artifact
  set; the bounded test-only Arb path covers `n=3` only, not `n=4,5,6`;
- exact optimum values, matching upper bounds, or asymptotic equality
  theorems.

The all-\(n\) induced-subset lower theorem in
`research/ALL_N_LOWER_BOUND.md` is independent of this interval backend. Its
coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal only inside that theorem's
explicit relaxation, not a backend-certified finite result and not a proved
Power-Ringmin asymptotic constant.

## Classification Implication

The checked finite brackets are therefore phrased as computer-certified results
under the repository's documented guarded `mpmath.iv` backend contract. They are
finite `n=3,4,5,6` certificates only. They are not exact optimum values, not
publication-grade independently audited certificates, and not evidence strong
enough to prove a matching upper bound, an asymptotic equality theorem, or an
exact leading constant. Their exact endpoint meaning is half-open: each strict
lower endpoint is excluded and each upper witness endpoint is included, so the
certified threshold infimum lies in \((L,U]\).

The bounded Arb `n=3` result is additional independent implementation evidence
for one checked record. It does not alter the preceding classification because
the production verifier and serialized artifact contract remain unchanged and
the other checked artifacts have not been independently cross-verified.

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

A bounded Arb/FLINT cross-check now exists for checked `n=3`. Possible future
trust paths include extending independently reviewed Arb coverage to the
remaining checked artifacts, MPFI-like interval arithmetic, a small custom
rational interval implementation for the required formulas, or independent
high-precision interval verification in another language.

## Bounded Generation Meaning

Current small-n certificate generation is work-count bounded. The general
exporter requires an explicit `--max-canonical-orders` ceiling, and each local
bracket search has a bounded retry count through `--local-max-attempts`.

There is no current wall-clock timeout in the mathematical verifier or
certificate generator. Adding one would be an operational control, not a change
to certificate semantics. It should be implemented only if it can be tested
deterministically and kept separate from semantic interval verification.
