# Artifact Schemas

`fixed_order_result.schema.json` is the v1 canonical JSON Schema for one fixed cyclic order in Power-Ringmin.

The schema requires:

- explicit quadratic radius sequence metadata under `instance.radius_sequence`;
- explicit cyclic order metadata under `fixed_order`;
- decimal-string numerical values under `result`;
- precision and tolerance metadata under `precision`;
- repository, software, command, source-file, and randomness provenance under `provenance`;
- evidence classification and check records under `evidence`.

## Design Rules

- Numerical values are encoded as decimal strings, not JSON floats. This preserves high-precision `mpmath` values and avoids parser-dependent rounding.
- The natural radius sequence and the cyclic order are both recorded. Consumers must not infer the order from `n` alone.
- The fixed-order result scope is local to the supplied cyclic order. A valid fixed-order artifact is not a global optimum claim unless `evidence.claim.scope` explicitly says so and the evidence supports that stronger claim.
- Evidence classifications use the project labels from `AGENTS.md`, normalized to snake case in JSON: for example `verified_fact`, `numerical_observation`, and `computer_certified_result`.
- `problem.constraints.all_pairs_checked` records whether all pairwise non-overlap constraints were checked. Power-Ringmin result artifacts should set it to `true`.
- `provenance.repository.git_commit` may be `null` only for deliberately uncommitted exploratory artifacts. Review-grade artifacts should record a 40-character commit hash and whether the worktree was dirty when produced.

## Verifier Compatibility

The standalone `verify.py` payload can be derived from a v1 artifact by extracting:

- `fixed_order.radius_order` as the verifier order;
- `result.central_radius.decimal` as the claimed radius;
- `result.positions_rad`, when present, as optional witness positions.

The package module `power_ringmin.fixed_order_artifact` provides helpers for this contract:

- `export_full_result_artifact(...)` builds a v1 artifact from a float64 `FullResult`;
- `export_highprec_artifact(...)` builds a v1 artifact from high-precision fixed-order values;
- `load_fixed_order_artifact(...)` and `loads_fixed_order_artifact(...)` validate and load v1 JSON artifacts;
- `verifier_payload_from_artifact(...)` derives the minimal standalone-verifier payload.

## CLI Export

The package entry point `power-ringmin-export-fixed-order` exports one v1 artifact from one explicit fixed cyclic order:

```powershell
power-ringmin-export-fixed-order --order 16,1,9,4 --output artifact.json
power-ringmin-export-fixed-order --index-order 4,1,3,2 --backend mpmath --digits 80 --output artifact.json
```

`--order` accepts quadratic radius values. `--index-order` accepts the corresponding quadratic indices and converts them to radii. Both forms must contain exactly one permutation of `1..n` after index normalization.

The package entry point `power-ringmin-export-fixed-order-batch` exports one v1 artifact per explicit fixed cyclic order in a JSON list:

```powershell
power-ringmin-export-fixed-order-batch orders.json --output-dir artifacts
power-ringmin-export-fixed-order-batch index_orders.json --order-kind index --backend mpmath --digits 80 --output-dir artifacts
```

The JSON input may be a top-level list, for example `[[16, 1, 9, 4], [1, 4, 9]]`, or an object with an `orders` list. With `--order-kind index`, entries are interpreted as quadratic indices and converted to radii before artifact export.

The schema itself does not prove a result. Verification remains a separate evidence step, recorded in `evidence.checks` and in the task dossier for the run that produced the artifact.

See `examples/fixed_order_batch_end_to_end/` for a small reproducible batch example that exports high-precision artifacts and verifies the generated directory.

## Small-N Interval Certificates

`small_n_interval_certificate.schema.json` is the v1 structural JSON Schema for a finite global small-n interval certificate assembled from verified local fixed-order interval brackets.

The schema requires:

- explicit quadratic instance metadata and canonical cyclic-order coverage metadata;
- explicit aggregation method metadata naming the local verifier and regenerated order-space source;
- strict global lower and feasible upper bound records with source index orders;
- one human-readable local bracket summary per embedded local bracket;
- provenance and evidence blocks classified as `computer_certified_result`.

The JSON Schema is a structural contract only. It checks shape, required fields, value encodings, and selected constants; it does not prove interval enclosure, order-space coverage, source freshness, or aggregate correctness.

The package validator `power_ringmin.small_n_interval_certificate.validate_small_n_interval_certificate_artifact` is the semantic authority. It independently regenerates the canonical order space, re-verifies every embedded local fixed-order interval bracket with its recorded guarded interval backend metadata, recomputes summary diagnostics and aggregate bounds, and rejects artifacts whose evidence or aggregation metadata drift from the implemented verifier contract.

Before attempting `n=5` or larger certificate production, use the bounded general exporter in dry-run mode to record the canonical order-space size:

```powershell
power-ringmin-export-small-n-interval-certificate --n 5 --max-canonical-orders 12 --dry-run
```

Actual generation requires both `--output` and an explicit `--max-canonical-orders` ceiling:

```powershell
power-ringmin-export-small-n-interval-certificate --n 5 --max-canonical-orders 12 --output artifact.json
```

This command is work-count bounded by the canonical-order ceiling and local retry count. It has no wall-clock timeout. It still produces finite-`n` evidence only and does not prove an exact optimum, an asymptotic result, or a theorem for all `n`.

## Finite Results Summaries

`finite_results_summary.schema.json` is the v1 structural JSON Schema for a derived finite-results summary built from checked finite small-n interval certificates.

This is a separate contract from `small_n_interval_certificate.schema.json`:

- small-n interval certificates are primary evidence artifacts;
- finite-results summaries are derived analysis artifacts;
- candidate sets, excluded-order counts, exclusion gaps, identical serialized bracket groups, cross-`n` comparisons, and ratios to `n^3/(6*pi)` belong in the derived summary, not in the primary certificate schema.

The JSON Schema is structural only. The package validator `power_ringmin.finite_results.validate_finite_results_summary_artifact` is the semantic authority. It reloads every source certificate through `power_ringmin.small_n_interval_certificate.load_small_n_interval_certificate_artifact`, recomputes source `content_sha256` values, rederives all candidate sets and exclusion gaps, and rejects stale summaries when source content or derived content no longer match.

The `content_sha256` value is a cross-platform source-content digest, not a raw checkout-byte digest. It is the SHA-256 hex digest of the source certificate byte stream after normalizing every CRLF sequence and every lone CR byte to one LF byte. No character decoding or other byte normalization is performed, so every non-line-ending byte change remains digest-sensitive.

Evidence classifications in v1 are:

- `computer_certified_result` for certified global brackets, candidate-set membership, excluded-order counts, and defined exclusion gaps;
- `verified_fact` for identical serialized bracket groups;
- `numerical_observation` for ratios to `n^3/(6*pi)`;
- `empirical_pattern` for cross-`n` trends over the listed checked inputs;
- `unresolved_claim` for explicit scope limitations.

The checked example path is:

```powershell
examples/finite_results_summary_n3_n6.json
```

Regenerate it from the checked source certificates with a fixed timestamp when deterministic byte-for-byte output is required:

```powershell
power-ringmin-analyze-finite-results --created-at-utc 2026-07-12T00:00:00Z --output examples/finite_results_summary_n3_n6.json
```

The summary remains finite checked evidence only. Multiple candidate orders are not exact ties, identical serialized brackets are not exact equality claims, and ratio sequences do not establish behavior outside the listed inputs.

## Checked Artifact Verification

The package entry point `power-ringmin-verify-checked-artifacts` is the CI/local review path for checked finite certificate artifacts:

```powershell
power-ringmin-verify-checked-artifacts
```

It discovers `examples/small_n_interval_certificate_n*.json`, validates their JSON Schema structure, reloads them through semantic certificate validators, explicitly re-verifies embedded local interval brackets, validates `examples/finite_results_summary_n3_n6.json`, and fails if the summary sources do not match the discovered checked certificates. It does not generate certificates.

## Batch Standalone Verification

The package entry point `power-ringmin-verify-fixed-order-artifacts` validates every matching v1 artifact in a directory, derives the minimal standalone `verify.py` payload, and invokes root `verify.py` once per artifact:

```powershell
power-ringmin-verify-fixed-order-artifacts artifacts
power-ringmin-verify-fixed-order-artifacts artifacts --recursive --pattern "*.json"
```

When an artifact records `result.local_radius_bracket.eta_decimal`, the batch verifier passes that eta to `verify.py` by default. Use `--no-artifact-eta` to skip local bracket checks, `--eta` to use the same eta for every artifact, or `--stn-tol` to pass an explicit closed-STN diagonal tolerance to `verify.py` for tolerance-labeled numerical artifacts such as float64 exports.
