# Fixed-Order Result Artifact Schema

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

The schema itself does not prove a result. Verification remains a separate evidence step, recorded in `evidence.checks` and in the task dossier for the run that produced the artifact.
