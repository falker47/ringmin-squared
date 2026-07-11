# PROJECT_KNOWLEDGE - power-ringmin

Last reviewed: 2026-07-11

## Project Identity

- VERIFIED FACT: working repository name is `power-ringmin`.
- VERIFIED FACT: project title is Power-Ringmin: Quadratic Radii.
- VERIFIED FACT: author is Maurizio Falconi.
- VERIFIED FACT: repository status is an independent research project, not a Ringmin worktree or branch.
- VERIFIED FACT: the authoritative project brief is `start.md`.

## Mathematical Definitions

- DEFINITION: peripheral radii are \(r_k=k^2\), for \(k=1,\dots,n\).
- DEFINITION: \(R_2^*(n)\) is the minimum feasible central radius for externally tangent peripheral circles with pairwise disjoint interiors.
- DEFINITION: for peripheral radii \(r_i,r_j\) and central radius \(R\),
  \[
  \theta_R(r_i,r_j)
  =
  2\arcsin
  \sqrt{
  \frac{r_i r_j}
  {(R+r_i)(R+r_j)}
  }.
  \]
- DEFINITION: for quadratic radii,
  \[
  \theta_R(i^2,j^2)
  =
  2\arcsin
  \left(
  \frac{ij}
  {\sqrt{(R+i^2)(R+j^2)}}
  \right).
  \]
- CONJECTURE: the principal research target is
  \[
  R_2^*(n)=\frac{n^3}{6\pi}(1+o(1)).
  \]
- UNRESOLVED CLAIM: a possible stronger target is
  \[
  R_2^*(n)=\frac{n^3}{6\pi}+O(n^2).
  \]
- HEURISTIC: in the expected regime \(R\asymp n^3\), \(\theta_R(i^2,j^2)\approx 2ij/R\).
- HEURISTIC: a Supnick-type or alternating chain may suggest a leading adjacent weight of order \(\sum ij\sim n^3/6\).

## Evidence Classification Rules

Every material mathematical or computational claim must be classified where relevant as one of:

- definition;
- verified fact;
- exact theorem;
- computer-certified result;
- numerical observation;
- empirical pattern;
- heuristic;
- conjecture;
- unresolved claim;
- disproved claim.

Rules:

- finite computation is not proof for all `n`;
- a conjecture must not be used as an established lemma;
- conditional arguments must be labeled conditional;
- all-pairs constraints must be checked, not only adjacent pairs;
- numerical precision, parameters, solver, seeds, environment, and code version must be recorded when relevant;
- contradictory evidence must be preserved and investigated.

## Upstream Reference

- VERIFIED FACT: upstream Ringmin local path is `C:\Users\Falker\Desktop\Code\circle\ringmin`.
- VERIFIED FACT: upstream public repository URL is `https://github.com/falker47/ringmin.git`.
- VERIFIED FACT: upstream inspected commit is `cc0327400819fe06b230d967cdcbafffe1648317`.
- VERIFIED FACT: upstream Ringmin studies the original radii \(1,2,\dots,n\), not the quadratic radii problem.
- VERIFIED FACT: upstream Ringmin includes source code, tests, scripts, result artifacts, figures, paper assets, a standalone verifier, and an MIT license file.
- RULE: Ringmin is prior work and a read-only upstream reference.
- RULE: future imports from Ringmin must preserve provenance and relevant license notices.
- RULE: Ringmin mathematical results and observed structural patterns do not automatically transfer to quadratic radii.
- VERIFIED FACT: the 2026-07-10 import audit found that upstream `geometry.py`, `evaluator.py`, `highprec.py`, and parts of `patterns.py` are primarily radius-value based and are the safest code foundation to import/adapt first.
- VERIFIED FACT: the 2026-07-10 import audit found original-radii assumptions in upstream search wrappers, lower-bound components, verifier/result paths, unconstrained SLSQP helper, scripts, result artifacts, and paper/report assets.
- RECOMMENDATION: import the Ringmin geometric/STN foundation before importing the certified-search pipeline; keep original Ringmin results as reference-only unless a later task explicitly creates a provenance-labeled reference area.

See `UPSTREAM_RINGMIN.md` for provenance details.

## Computational Foundation

- VERIFIED FACT: the Python package import name is `power_ringmin`.
- VERIFIED FACT: the initial package metadata is in `pyproject.toml`; package source is under `src/power_ringmin/`; tests are under `tests/`.
- VERIFIED FACT: substantial imported/adapted code is licensed under MIT and records upstream Ringmin commit `cc0327400819fe06b230d967cdcbafffe1648317` in module docstrings.
- VERIFIED FACT: `src/power_ringmin/geometry.py` provides positive-radius validation, `quadratic_radii(n)`, `theta(R,a,b)`, cyclic adjacent pairs, and cycle-equivalence helpers.
- VERIFIED FACT: `src/power_ringmin/evaluator.py` provides a float64 fixed-order evaluator using all-pairs STN feasibility, scale-aware radius bracketing, recovered positions, Cartesian validation, essential tight-pair detection, and floating-radius detection.
- VERIFIED FACT: `src/power_ringmin/highprec.py` provides an independent mpmath fixed-order feasibility verifier, high-precision full-radius bisection, position recovery, and pair slack checks.
- VERIFIED FACT: `src/power_ringmin/patterns.py` provides selected generic order constructors: sequential, zigzag, interleave, Supnick maximum-tour form, Supnick minimum-tour form, and JSON order loading.
- VERIFIED FACT: `src/power_ringmin/crosscheck.py` provides a radius-sequence-aware fixed-order SLSQP cross-check using all-pairs Cartesian non-overlap constraints and explicit fixed-order angle variables.
- VERIFIED FACT: the upstream unconstrained global SLSQP helper was not imported because it hardcodes the original radii `1,\dots,n` and belongs with a later radius-sequence-aware search design.
- VERIFIED FACT: root `verify.py` is a standalone high-precision fixed-order verifier scaffold that imports only the Python standard library and `mpmath`; it accepts explicit order/radius inputs or minimal JSON payloads and can check optional witness positions, local radius brackets, and an explicit closed-STN diagonal tolerance override via `--stn-tol`.
- VERIFIED FACT: `schemas/fixed_order_result.schema.json` defines the v1 JSON artifact schema for one fixed-order numerical result, requiring explicit radius sequence, cyclic order, precision/tolerance metadata, provenance, and evidence classification.
- VERIFIED FACT: `schemas/README.md` documents fixed-order artifact schema design rules and verifier compatibility.
- VERIFIED FACT: `src/power_ringmin/fixed_order_artifact.py` provides package helpers for `power-ringmin.fixed_order_result.v1` artifacts: construction from float64 `FullResult`, construction from high-precision fixed-order values, semantic validation, JSON dump/load helpers, and standalone-verifier payload derivation.
- VERIFIED FACT: `src/power_ringmin/export_fixed_order_cli.py` provides the `power-ringmin-export-fixed-order` CLI for exporting one v1 fixed-order artifact from either an explicit quadratic radius order (`--order`) or an explicit quadratic index order (`--index-order`).
- VERIFIED FACT: `power-ringmin-export-fixed-order` uses the float64 fixed-order evaluator by default, supports an optional `mpmath` backend with `--digits` and `--local-radius-eta`, records CLI provenance, and refuses to write an artifact whose exported radius is infeasible at the requested precision.
- VERIFIED FACT: after the n=4 high-precision export rejection investigation, the `mpmath` exporter path stabilizes the serialized decimal radius before artifact construction by adaptively nudging a near-boundary computed radius upward until the exact decimal to be written is feasible under the requested STN tolerance.
- VERIFIED FACT: `src/power_ringmin/export_fixed_order_batch_cli.py` provides the `power-ringmin-export-fixed-order-batch` CLI for exporting one v1 fixed-order artifact per explicit order in a JSON list.
- VERIFIED FACT: `power-ringmin-export-fixed-order-batch` accepts a top-level JSON list or an object with an `orders` list, treats orders as quadratic radius orders by default, supports `--order-kind index` for quadratic index orders, writes deterministic `fixed_order_####_n#.json` artifact names, and refuses to overwrite generated files unless `--overwrite` is passed.
- VERIFIED FACT: `power-ringmin-export-fixed-order-batch` reuses the single-order fixed-order exporter, supports the same `float64` and `mpmath` backend options, and records batch CLI provenance in each generated artifact.
- VERIFIED FACT: `src/power_ringmin/verify_fixed_order_artifacts_cli.py` provides the `power-ringmin-verify-fixed-order-artifacts` CLI for checking a directory of v1 fixed-order artifacts with root `verify.py`.
- VERIFIED FACT: `power-ringmin-verify-fixed-order-artifacts` validates each matching v1 artifact, derives the minimal standalone-verifier payload, invokes root `verify.py` as a subprocess, prints per-artifact PASS/FAIL lines, and returns a nonzero exit code when any artifact fails.
- VERIFIED FACT: `power-ringmin-verify-fixed-order-artifacts` supports directory glob patterns, recursive scans, verifier precision digits, per-artifact recorded local eta checks by default, an eta override, and an explicit `--stn-tol` pass-through for tolerance-labeled numerical artifacts.
- VERIFIED FACT: `src/power_ringmin/search_small_n.py` provides canonical quadratic index-order enumeration modulo rotation and reflection, canonicalization, quadratic index-to-radius conversion, exhaustive float64 small-n search over canonical orders, and v1 small-n search JSON helpers.
- VERIFIED FACT: `power-ringmin-search-small-n` is the CLI for exhaustive float64 small-n search over canonical quadratic index orders; it writes a JSON summary classified as `numerical_observation`.
- VERIFIED FACT: small-n search artifacts use schema version `power-ringmin.small_n_search_result.v1`, record explicit radius-sequence and order-space metadata, and reject `computer_certified_result` classification for the float64 baseline.
- VERIFIED FACT: small-n search artifacts classify their claim scope as `finite_exhaustive_float64_order_search` and explicitly disclaim certified global optimality.
- VERIFIED FACT: small-n search now rechecks the float64 incumbent and float64 tie set with `mpmath` by default, recording the results in a `high_precision_recheck` artifact block.
- VERIFIED FACT: `power-ringmin-search-small-n` supports `--highprec-recheck-digits` for the mpmath recheck precision and `--no-highprec-recheck` for speed-sensitive exploratory runs.
- VERIFIED FACT: small-n search artifact validation requires the search-method recheck metadata to match the top-level `high_precision_recheck` block; when recheck records are present, they must cover exactly the float64 tie set.
- INTERPRETATION: small-n high-precision incumbent/tie rechecks are still numerical observations, not computer-certified global optimum evidence, unless a later interval verifier supplies certified bounds across the order space.
- VERIFIED FACT: `ops/TASK-20260711__interval_verifier_semantics/DESIGN.md` records the design semantics for a future high-precision interval verifier for finite small-n certification.
- DESIGN DECISION: a future finite small-n `computer_certified_result` should require outward interval enclosures, strict sign checks, one verified fixed-order interval bracket per canonical order, and independent regeneration of the canonical order space.
- DESIGN DECISION: certified feasible upper endpoints should be checked by explicit all-pairs witness slacks using upper angular bounds; certified infeasible lower endpoints should be checked by explicit negative cycles in a relaxed STN using lower angular bounds.
- DESIGN DECISION: tolerance-based `mpmath` STN acceptance such as `margin >= -tol` is not sufficient for `computer_certified_result`; it remains numerical evidence unless replaced by interval signs.
- PROOF OBLIGATION: the interval-verifier implementation still needs locally recorded justifications for the angular formula, monotonicity of `theta_R(a,b)` in `R`, fixed-order angular/STN equivalence, and negative-cycle infeasibility.
- VERIFIED FACT: `src/power_ringmin/interval_verifier.py` implements local fixed-order interval bracket verifier semantics for one canonical quadratic index order.
- VERIFIED FACT: the local interval bracket verifier checks the radius order against the index-order squares, rejects noncanonical index orders, rejects tolerance-based interval metadata, checks a lower endpoint by an explicit negative cycle using relaxed interval edge upper weights, and checks an upper endpoint by explicit all-pairs witness slacks using theta upper bounds.
- VERIFIED FACT: `MPMathIntervalAngularOracle` provides a guarded `mpmath.iv` angular interval backend using `atan2(x, sqrt(1-x^2))` for the inverse-sine step and records backend precision, guard, outward-enclosure, and no-tolerance metadata.
- INTERPRETATION: local fixed-order interval bracket verification is a certification building block only; it does not by itself certify a global small-n optimum, cover every cyclic order, or establish a theorem for all `n`.
- VERIFIED FACT: `src/power_ringmin/interval_bracket_exporter.py` provides a fixed-order interval bracket generator/exporter for records consumed by `src/power_ringmin/interval_verifier.py`.
- VERIFIED FACT: the fixed-order interval bracket exporter accepts one canonical quadratic index order, computes a high-precision `mpmath` fixed-order radius proposal, widens a local bracket as needed, extracts an explicit lower-endpoint negative cycle, constructs an upper-endpoint strict witness by solving a padded STN, and refuses to return or write the record unless `verify_fixed_order_interval_bracket` accepts it.
- VERIFIED FACT: fixed-order interval bracket JSON helpers verify records before serialization and after loading by reconstructing the recorded `MPMathIntervalAngularOracle` metadata.
- INTERPRETATION: generated fixed-order interval bracket records are local fixed-order certificate building blocks only; they do not certify a global small-n optimum unless a later global verifier covers every canonical order.
- VERIFIED FACT: `src/power_ringmin/small_n_interval_certificate.py` provides a finite small-n interval certificate aggregator that embeds local fixed-order interval bracket records, independently regenerates the canonical cyclic index-order space, verifies exactly one local bracket per canonical order, and computes a finite global radius bracket from the verified local endpoints.
- VERIFIED FACT: `build_n3_interval_certificate_fixture` generates the tiny n=3 interval certificate fixture by building and aggregating a local interval bracket for the single canonical n=3 index order `(3,1,2)` / radius order `(9,1,4)`.
- VERIFIED FACT: `export_n3_interval_certificate_artifact` and the `power-ringmin-export-n3-interval-certificate` CLI build, validate, write, and reload the finite n=3 interval certificate artifact using the same small-n interval certificate validator.
- VERIFIED FACT: `examples/small_n_interval_certificate_n3.json` is a checked finite n=3 interval certificate artifact generated by `power-ringmin-export-n3-interval-certificate --output examples/small_n_interval_certificate_n3.json --digits 80 --guard-decimal 1e-70 --radius-eta 1e-4 --created-at-utc 2026-07-11T00:00:00Z`.
- COMPUTER-CERTIFIED RESULT: under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` interval backend contract, the n=3 interval certificate fixture verifies one local fixed-order interval bracket for every canonical n=3 cyclic order and aggregates them into a finite global bracket.
- COMPUTER-CERTIFIED RESULT: under the same local interval-verifier semantics and guarded `mpmath.iv` interval backend contract, `examples/small_n_interval_certificate_n3.json` verifies one local fixed-order interval bracket for every canonical n=3 cyclic order and records the finite global bracket `(0.3832870361393696523322205393924377858638763427734375, 0.383487036139369685816546962087159045040607452392578125]`.
- INTERPRETATION: the n=3 global interval certificate fixture is finite n=3 evidence only; it is not a theorem for all `n`, not an asymptotic result, and still carries the interval-backend provenance limitation documented for the local verifier/exporter.
- VERIFIED FACT: the 2026-07-11 n=4 finite-certificate next-step design task regenerated the n=4 canonical cyclic index-order space as three orders: `(4, 1, 2, 3)`, `(4, 1, 3, 2)`, and `(4, 2, 1, 3)`.
- VERIFIED FACT: an in-memory n=4 design probe at 80 digits with `guard_decimal=1e-70` and `radius_eta=1e-4` generated local interval bracket records for all three canonical orders and `build_small_n_interval_certificate(..., n=4)` accepted the aggregate in 0.8 seconds.
- VERIFIED FACT: the in-memory n=4 design probe's aggregate bracket was `(1.4955284118749971877804227915476076304912567138671875, 1.4957284118749971657535979829845018684864044189453125]`.
- INTERPRETATION: the n=4 probe is readiness evidence for a runtime-bounded certificate artifact task; it is not yet a checked durable n=4 certificate artifact.
- DESIGN DECISION: the next finite-certificate step should be a runtime-bounded n=4 interval certificate attempt before broad verifier/format hardening for larger certificates.
- VERIFIED FACT: `examples/fixed_order_batch_end_to_end/` provides a small reproducible batch example with explicit n=3 and n=4 quadratic index orders, README commands for `power-ringmin-export-fixed-order-batch` and `power-ringmin-verify-fixed-order-artifacts`, and no checked-in generated result artifacts.
- VERIFIED FACT: `examples/fixed_order_batch_end_to_end/README.md` documents that generated example artifacts are finite fixed-order numerical observations, not global optimum certificates, and gives local eta guidance: choose an absolute offset above STN/serialization noise but small relative to the reported radius scale, then verify `R`, `R + eta`, and `R - eta` when applicable.
- VERIFIED FACT: `examples/fixed_order_result_n3.json` is a checked schema fixture for the fixed cyclic order `(1,4,9)` and is classified as a `numerical_observation`, not as a global optimum certificate.
- VERIFIED FACT: as of the fixed-order batch end-to-end example task, the certified-search pipeline, frontier verifier, plots, and original Ringmin result artifacts have not been imported.
- VERIFIED FACT: `ops/TASK-20260711__small_n_cyclic_order_search_design/DESIGN.md` records the design for a future radius-sequence-aware small-n cyclic-order search.
- DESIGN DECISION: the planned small-n search should represent cyclic orders by quadratic index order and explicit radius order separately, using canonical index orders modulo rotation and reflection.
- DESIGN DECISION: the first planned implementation should be an exhaustive float64 baseline over canonical quadratic index orders, with output classified as finite numerical observation unless later independent high-precision interval evidence supports a stronger global claim.
- UNRESOLVED CLAIM: pruned or frontier-certified quadratic-radii search needs a local proof and verifier for any subset-chain or floating-candidate lower bounds before it can support `computer_certified_result` claims.
- VERIFIED FACT: `pyproject.toml` defines optional `crosscheck` dependencies for NumPy/SciPy; `requirements.txt` includes NumPy/SciPy for the local development/test environment.
- VERIFIED FACT: `pyproject.toml` registers the console script `power-ringmin-export-fixed-order`.
- VERIFIED FACT: `pyproject.toml` registers the console script `power-ringmin-export-fixed-order-batch`.
- VERIFIED FACT: `pyproject.toml` registers the console script `power-ringmin-export-fixed-order-interval-bracket`.
- VERIFIED FACT: `pyproject.toml` registers the console script `power-ringmin-export-n3-interval-certificate`.
- VERIFIED FACT: `pyproject.toml` registers the console script `power-ringmin-verify-fixed-order-artifacts`.
- VERIFIED FACT: `pyproject.toml` registers the console script `power-ringmin-search-small-n`.
- VERIFIED FACT: `python -m pytest` passed 5 adapted quadratic smoke tests on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 8 tests after the fixed-order crosscheck import on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 11 tests after the fixed-order artifact schema design on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 14 tests after the fixed-order artifact exporter/loader implementation on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 18 tests after the fixed-order artifact CLI implementation on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 23 tests after the batch fixed-order artifact export implementation on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 28 tests after the batch standalone-verifier artifact check implementation on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 29 tests after the fixed-order batch end-to-end example implementation on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 30 tests after the n=4 high-precision export stabilization on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 30 tests after the finite artifact/local eta documentation note on 2026-07-11.
- VERIFIED FACT: `python -m pytest tests\test_search_small_n.py` passed 7 small-n search tests on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 37 tests after the small-n float64 search implementation on 2026-07-11.
- VERIFIED FACT: `python -m pytest tests\test_search_small_n.py` passed 7 small-n search tests after adding incumbent/tie high-precision rechecks on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 37 tests after adding small-n incumbent/tie high-precision rechecks on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 37 tests after the interval verifier semantics design task on 2026-07-11.
- VERIFIED FACT: `python -m pytest tests\test_interval_verifier.py` passed 6 local interval verifier tests on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 43 tests after the local fixed-order interval bracket verifier implementation on 2026-07-11.
- VERIFIED FACT: `python -m pytest tests\test_interval_bracket_exporter.py` passed 5 fixed-order interval bracket exporter tests on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 48 tests after the fixed-order interval bracket exporter implementation on 2026-07-11.
- VERIFIED FACT: `python -m pytest tests\test_small_n_interval_certificate.py` passed 4 finite n=3 interval certificate tests on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 52 tests after the n=3 global interval certificate fixture implementation on 2026-07-11.
- VERIFIED FACT: `python -m pytest tests\test_small_n_interval_certificate.py` passed 7 finite n=3 interval certificate artifact/CLI tests on 2026-07-11.
- VERIFIED FACT: `python -m pytest` passed 55 tests after the n=3 interval certificate artifact/CLI implementation on 2026-07-11.
- INTERPRETATION: passing finite smoke tests verifies the imported implementation behavior on tested cases only; it is not a theorem about all quadratic-radii instances.

## Verified Environment Facts

- VERIFIED FACT: repository root during bootstrap is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- VERIFIED FACT: before bootstrap, the only project file in the new repository folder was `AGENTS_GENERIC_TEMPLATE_v2.md`.
- VERIFIED FACT: Git was initialized directly in this folder on branch `main`.
- VERIFIED FACT: no Git remote is configured for this repository as of bootstrap.
- VERIFIED FACT: Python reported version `3.14.3` during the 2026-07-10 foundation import.
- VERIFIED FACT: mpmath reported version `1.3.0` during the 2026-07-10 foundation import.
- VERIFIED FACT: during the 2026-07-10 fixed-order crosscheck import, NumPy reported version `2.4.3`, SciPy reported version `1.17.1`, and mpmath reported version `1.3.0`.

## Canonical Commands

- `python -m pytest`

Read-only repository inspection commands used during bootstrap:

- `git status`;
- `git diff`;
- `git diff --check`;
- `git rev-parse --show-toplevel`;
- `git rev-parse --git-common-dir`;
- `git branch --show-current`;
- `git remote -v`.

## Current Established Results

- VERIFIED FACT: the foundation smoke tests include finite quadratic-radii computations for fixed orders, including `(1,4,9)` and sampled orders from `quadratic_radii(6)` and `quadratic_radii(7)`.
- VERIFIED FACT: the fixed-order crosscheck tests include a finite numerical comparison where SLSQP matches the STN fixed-order radius for the quadratic order `(16,1,9,4)` within the test tolerance.
- VERIFIED FACT: the standalone verifier accepted the high-precision fixed-order radius for `(1,4,9)` and rejected a radius smaller by `1e-8` during the 2026-07-10 verification.
- VERIFIED FACT: the fixed-order artifact schema fixture `examples/fixed_order_result_n3.json` records an explicit radius sequence, fixed cyclic order, high-precision radius/positions, precision tolerances, provenance, and evidence classification for `(1,4,9)`.
- VERIFIED FACT: the fixed-order artifact exporter/loader tests round-trip a float64 `FullResult` artifact for order `(16,1,9,4)`, round-trip a high-precision artifact for `(1,4,9)`, derive a standalone-verifier payload, and reject a fixed-order radius/index mismatch.
- VERIFIED FACT: the fixed-order artifact CLI tests export a float64 artifact from radius order `(16,1,9,4)`, export a high-precision artifact from index order `(1,2,3)`, verify that the high-precision exporter stabilizes the serialized radius for index order `(4,1,3,2)`, derive a standalone-verifier payload, reject non-quadratic radius input, and verify the console script registration.
- VERIFIED FACT: the batch fixed-order artifact CLI tests export two float64 artifacts from a JSON list of radius orders, export a high-precision artifact from a JSON object with `index_orders`, reject non-quadratic radius input, refuse overwrite without `--overwrite`, allow overwrite with `--overwrite`, and verify the console script registration.
- VERIFIED FACT: the batch standalone-verifier artifact tests accept a high-precision artifact directory with recorded local eta, accept a float64 artifact with explicit `--stn-tol`, report a deliberately weakened artifact as failed, reject an empty artifact directory, and verify the console script registration.
- VERIFIED FACT: the fixed-order batch end-to-end example test exports high-precision artifacts, including the n=4 index order `(4,1,3,2)`, from `examples/fixed_order_batch_end_to_end/index_orders.json` into a temporary directory and verifies them through the batch standalone-verifier CLI module path.
- NUMERICAL OBSERVATION: the small-n float64 search smoke artifact `ops/TASK-20260711__small_n_float64_search/small_n_search_n3_smoke.json` enumerates the single canonical n=3 index order `(3,1,2)`, corresponding to radius order `(9,1,4)`, and records `R_full = 0.38338703613939273`.
- INTERPRETATION: the n=3 small-n smoke artifact is a finite float64 numerical observation, not a computer-certified global optimum certificate.
- NUMERICAL OBSERVATION: the small-n high-precision recheck smoke artifact `ops/TASK-20260711__small_n_highprec_rechecks/small_n_search_n3_highprec_recheck_smoke.json` enumerates the single canonical n=3 index order `(3,1,2)`, records float64 `R_full = 0.38338703613939273`, and rechecks the incumbent/tie order at 80 mpmath digits with `mpmath_R_full = 0.38338703613936966604628713672532649776985422245654228331612995273239552892574553`.
- INTERPRETATION: the n=3 high-precision recheck smoke artifact remains a finite numerical observation because it does not include interval lower bounds for every canonical order.
- NUMERICAL OBSERVATION: for index order `(4,1,3,2)` / radius order `(16,1,9,4)` at 80 digits, the raw `full_radius_mp` result has an STN margin within the default `1e-40` tolerance, while its direct 80-significant-digit decimal serialization can round slightly downward and fail that same tolerance check; this was fixed as exporter robustness, not interpreted as mathematical infeasibility.
- VERIFIED FACT: the local interval verifier test fixture verifies a fixed-order bracket for the canonical n=3 index order `(3,1,2)` / radius order `(9,1,4)` under the guarded interval oracle.
- INTERPRETATION: the n=3 local interval verifier fixture is a fixed-order endpoint semantics test, not a global small-n certificate artifact.
- VERIFIED FACT: the fixed-order interval bracket exporter tests generate and verify a local interval bracket record for the canonical n=3 index order `(3,1,2)` / radius order `(9,1,4)`, round-trip it through JSON dump/load helpers, reject a deliberately broken witness, export the record through the CLI, reject noncanonical index order `(1,2,3)`, and verify the console script registration.
- INTERPRETATION: the generated n=3 interval bracket test record is local fixed-order evidence only; it is not a global n=3 certificate until a later verifier confirms coverage of the full canonical order space.
- VERIFIED FACT: the small-n interval certificate tests build an n=3 fixture, verify that it covers the single canonical order `(3,1,2)`, round-trip the self-contained JSON artifact, reject missing/duplicate/wrong-n local coverage, and reject tampering with an embedded local witness or aggregate upper endpoint.
- COMPUTER-CERTIFIED RESULT: the n=3 fixture produced by `build_n3_interval_certificate_fixture` is a finite global interval certificate for n=3 under the local interval-verifier semantics because it verifies a local interval bracket for every canonical n=3 order and records the resulting strict lower and feasible upper endpoints.
- VERIFIED FACT: `examples/small_n_interval_certificate_n3.json` loads through `load_small_n_interval_certificate_artifact`, covers the single canonical n=3 order `(3,1,2)`, and retains `computer_certified_result` classification with claim scope `finite_global_small_n_interval_bracket`.
- COMPUTER-CERTIFIED RESULT: `examples/small_n_interval_certificate_n3.json` is a checked finite global interval certificate artifact for n=3 under the local interval-verifier semantics; it is not an exact optimum value and not a theorem for all `n`.
- VERIFIED FACT: no certified quadratic-radii optimum has yet been established in this repository.
- VERIFIED FACT: no quadratic-radii theorem has yet been established in this repository.
- VERIFIED FACT: no production-scale global quadratic-radii certificate artifact beyond the checked finite n=3 example has yet been checked in.
