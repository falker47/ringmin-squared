# EVIDENCE - TASK-20260723 / Two-Prefix Label-Aware Capacity

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source audit | Scope and accepted starting theorems | contract, proof, prior dossiers, Git status | VERIFIED |
| EV-002 | exact theorem | Coupled finite nested-capacity inequality | CR28dw69--CR28dw73 | PROVED |
| EV-003 | exact optimization | Full compact two-prefix classification | CR28dw74--CR28dw81 | PROVED |
| EV-004 | bounded exact computation | Independent finite discriminant rows | `exact_diagnostic.py` | PASS |
| EV-005 | regression / hygiene | Repository verification and final diff | repository root | VERIFIED |

## EV-001 - Scope And Source Audit

- **Date:** 2026-07-23
- **Method or command:** inspected `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, the roadmap, the arbitrary-finite-prefix theorem, the
  two-block no-go, the one-prefix label-aware proof and dossier, actual source
  files, read-only Git history, and clean `git status`.
- **Relevant output:** the requested class is one \(k=2\) height telescope
  with two nested capacity rows over one original-edge pool, not two reset
  blocks and not one total cardinality.
- **Interpretation:** production, tests, artifacts, schemas, enumeration
  limits, and geometric claims remain outside scope.
- **Limitations:** no broader structural-filter classification is claimed.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---strict-startup-and-exact-derivation`.

## EV-002 - Finite Two-Prefix Theorem

- **Date:** 2026-07-23
- **Method or command:** exact one-use slack partition, binary-type
  realizability, two simultaneous capacity inequalities, labelwise order
  statistics, and discrete first differences.
- **Relevant output:** (CR28dw72) is an exact all-order inequality with no
  double charging.  Its coupled allocation cost has the quadratic
  first-difference (CR28dw73), including endpoint, linear-weight, and
  adjacent-tie collisions.
- **Interpretation:** the two cutoff capacities remain separate and jointly
  constrain one integer \(q\).
- **Limitations:** sharpness concerns retained binary floor data, not
  simultaneous geometric equality.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---strict-startup-and-exact-derivation`.

## EV-003 - Exact Compact No-Go

- **Date:** 2026-07-23
- **Method or command:** exact Riemann normalization, continuity and collision
  audit, inactive clipped-envelope comparison, active rational endpoint and
  Bernstein certificate, and exact rational/radical separators.
- **Relevant output:** the complete compact objective exists and satisfies
  \[
  C_{\rm LA,*}
  <{2769\over10000}
  <C_{\rm 2LA,*}
  <{434+4\sqrt2\over1587}=C_{\rm AF}.
  \]
  The active side is below \(69/250\); a capacity-inactive rational witness
  has exact value \(588926561981/2126250000000\).
- **Interpretation:** exact strict improvement over one prefix, but exact
  no-go against the arbitrary-finite-prefix coefficient.
- **Limitations:** this is not an upper bound on \(\Lambda_n\) and makes no
  geometric claim.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---strict-startup-and-exact-derivation`.

## EV-004 - Independent Finite Diagnostic

- **Date:** 2026-07-23
- **Method or command:**
  `python -B ops/TASK-20260723__two_prefix_label_aware_capacity/exact_diagnostic.py`.
- **Relevant output:** PASS on six exact rows and 208 admissible binary type
  histories.  The rows cover an inactive singleton, both allocation
  endpoints, a five-point interval with an interior quadratic minimum, an
  exact adjacent tie, equal-weight linear degeneration, and an active outer
  capacity.  Every row checks both nested capacity inequalities, the closed
  cumulative sums, the quadratic leading coefficient and discriminant,
  monotone first differences, and exhaustive history minima.
- **Interpretation:** standalone bounded corroboration importing only the
  Python standard library and no project, production, test, enumerator,
  artifact, or certificate helper.
- **Limitations:** bounded rows do not replace the all-history proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---independent-diagnostic-and-synchronization`.

## EV-005 - Repository Verification And Final Diff

- **Date:** 2026-07-23
- **Method or command:** reran the diagnostic; ran Ruff lint and format
  checks, `python -m pytest`,
  `python -m pytest tests/test_checked_artifact_schema_validation.py`, and
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  audited equation tags, standalone display delimiters, control characters,
  task-local generated files, protected scope, Git status, the complete diff,
  and `git diff --check`.
- **Relevant output:** diagnostic PASS on 208 histories; Ruff PASS; full
  suite `283 passed`; focused schema suite `4 passed`; checked-artifact
  verifier PASS for 4 certificates and 76 local brackets; 965 equation tags
  are unique; standalone display delimiters balance 1,477/1,477; zero
  forbidden control characters; exactly the 8 authorized files changed; no
  production, test, schema, artifact, enumerator, enumeration-limit, or
  geometric source changed; complete diff and whitespace checks PASS.
- **Failed check and resolution:** the first Ruff format check requested one
  mechanical reformat of the diagnostic.  Ruff formatting was applied, then
  lint, format, diagnostic, and all regressions passed.
- **Interpretation:** the exact proof, compact classification, independent
  diagnostic, and repository integration are ready for human review.
- **Limitations:** hosted CI cannot inspect an uncommitted diff.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---final-verification-and-handoff`.
