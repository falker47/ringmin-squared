# TASK_LOG - TASK-20260713__adjacent_product_distance_relaxation / Adjacent Product-Distance Relaxation

Append-only. Add a new entry to correct previous information.

## 2026-07-13 - Startup And Exact Derivation

- **Action:** Read required memory, previous surrogate evidence, source, tests, patterns, and research note; checked the clean Git tree; derived parity-specific lower bounds and the interleave upper construction.
- **Result:** The target A_n formula is true. The tail comparison has asymptotic constants 1/4 and 2(sqrt(2)-1)/3, and the explicit tail m=ceil(2n/5) proves strictness from n=33 onward.
- **Interpretation:** The all-n adjacent theorem is independent of finite enumeration; the effective tail threshold does not determine W_n for n=12..32.
- **Evidence:** EVIDENCE.md#ev-001---startup-and-symbolic-derivation
- **Next step:** compute the permitted truncated tables and implement exact support.

## 2026-07-13 - Exact Truncated Implementation And Focused Tests

- **Action:** Ran exact distance-one/distance-two probes, added the truncated score/enumerator and adjacent formula, and extended focused tests.
- **Result:** The first naive probe timed out after 30 seconds because it repeatedly allocated all pair-score records. A one-pass integer/rational probe completed in 4 seconds and reproduced the exact n=3..11 tables. Focused tests passed 12/12.
- **Interpretation:** The timeout was a probe-efficiency failure, not mathematical counterevidence. The repository implementation retains the same hard n<=11 boundary and deterministic work ceiling as the full enumerator.
- **Evidence:** EVIDENCE.md#ev-002---truncated-table-implementation-and-focused-tests
- **Next step:** finish research and durable-memory updates, then run full verification.

## 2026-07-13 - Research Memory And Full Verification

- **Action:** Added the all-n adjacent proof, effective tail comparison,
  truncated table, classifications, roadmap updates, and durable project
  memory; ran focused/full pytest and checked-artifact verification.
- **Result:** Focused tests passed 22/22, full pytest passed 140/140, and the
  artifact verifier accepted 4 certificates, 76 local brackets, and the
  n=3..6 summary. A direct second check matched 80 residue-polynomial
  identities.
- **Interpretation:** The implementation, exact finite table, symbolic proof,
  and existing artifact path are mutually consistent.
- **Evidence:** EVIDENCE.md#ev-003---full-verification-and-command-audit
- **Next step:** complete final scope, encoding, whitespace, and diff review.

## 2026-07-13 - Final Hygiene And Handoff

- **Action:** Inspected the complete tracked diff and untracked dossier; checked
  exact path scope, strict UTF-8, trailing whitespace, equation tags, Git
  status, and `git diff --check`; aligned task and project status.
- **Result:** All 11 intended paths exist and decode as strict UTF-8, trailing
  whitespace count is zero, all 19 equation tags are unique, and
  `git diff --check` produced no output.
- **Interpretation:** The bounded STRICT task is complete and ready for user
  review; no certificate, artifact, schema, CLI, or beyond-n=11 order
  enumeration was introduced.
- **Evidence:** EVIDENCE.md#ev-004---final-scope-encoding-whitespace-and-diff-review
- **Next step:** Stop for user review and manual commit decision.
