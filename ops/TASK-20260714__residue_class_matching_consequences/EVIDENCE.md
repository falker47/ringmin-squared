# EVIDENCE - TASK-20260714__residue_class_matching_consequences / Residue-Class Matching Consequences

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / independent review | Startup and symbolic residue derivation | project memory, proof/source/tests, three read-only audits | PASS |
| EV-002 | source / proof / test | Exact support, proof, and formula tests | product-distance source/tests and proof note | PASS |
| EV-003 | command / test / independent review | Automated verification and final audits | focused/integrated/full tests, artifact verifier, three audits | PASS after environment rerun |
| EV-004 | documentation / hygiene | Minimal memory and final diff audit | nine changed paths | PASS |

## EV-001 - Startup And Independent Symbolic Derivation

- **Date:** 2026-07-14
- **Method or command:** Inspected all required startup state, the terminal-high
  and upper-construction predecessor dossiers, the primary proof note, exact
  source/tests, and read-only Git status; obtained independent mathematical,
  implementation, and documentation audits; evaluated exact threshold-tail
  data on boundary representatives without enumerating cyclic orders.
- **Relevant output:** Initial worktree clean. All derivations give
  `H_n=T_n` in residues `0,3,4`, `(d_n-1)^2/2` in residue `1`, and
  `(d_n-1)(d_n-2)/2` in residue `2` from `n=17`; at `n=12`, the generic
  value `55` and its next half-step fail packing while `56` is admissible.
- **Interpretation:** The exact theorem and implementation delta had
  independent pre-edit support and were subsequently verified.
- **Limitations:** Finite evaluations support but do not replace the symbolic
  all-`n` proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---startup-and-symbolic-derivation`

## EV-002 - Exact Support, Proof, And Formula Tests

- **Date:** 2026-07-14
- **Method or command:** Added
  `terminal_high_incidence_closed_form(n)` alongside the unchanged event-set
  inversion; added a separate polynomial oracle in the tests; compared both
  exact paths on `n=9..200`; checked the formula/gaps on `n=9..5000`; wrote
  RC1--RC6 in `research/PRODUCT_DISTANCE_SURROGATE.md`.
- **Relevant output:** Every comparison passes. The implementation returns a
  `Fraction`, validates the theorem domain, treats `n=12` before residue two,
  and performs no search. RC1--RC4 prove the formula; RC5 proves exact values
  for `B_n,W_n` in residues `0,3,4`; RC6 gives widths `(2n+3)/5`,
  `(4n+7)/5`, and `10` at `n=12`.
- **Interpretation:** This is exact source support and an exact symbolic
  theorem, not a conjecture inferred from finite data.
- **Limitations:** Formula diagnostics above `n=11` are arithmetic checks, not
  cyclic-order enumeration. No exact `B_n,W_n` formula is proved beyond the
  bounded table in residues `1,2`.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---exact-support-and-residue-class-proof`

## EV-003 - Automated Verification And Independent Audits

- **Date:** 2026-07-14
- **Method or command:** Ran `py_compile`; focused product-distance pytest;
  integrated product-distance/zigzag/tail/insertion pytest; full pytest; the
  checked-artifact semantic verifier; Ruff; and independent mathematical,
  implementation, and documentation audits.
- **Relevant output:** Compile PASS; focused `28/28`; integrated `43/43`;
  full suite `156/156` outside the sandbox; artifact verifier accepts 4
  certificates, 76 local brackets, and the `n=3..6` summary; Ruff PASS. The
  mathematical and implementation audits report PASS. The documentation
  audit's stale-status and bounded-table qualification findings were applied.
- **Failed check retained:** The sandboxed full suite produced 31 setup errors
  because pytest could not use the system temporary directory and one
  deterministic-summary failure because Git provenance was inaccessible.
  Rerunning the identical suite outside the sandbox passed every test.
- **Interpretation:** All executable and independent-review checks pass; the
  failed sandbox run is environment-permission evidence, not a changed-code
  failure.
- **Limitations:** Hosted GitHub Actions for the current worktree was not
  inspected.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---full-verification-and-independent-audits`

## EV-004 - Minimal Memory And Final Diff Audit

- **Date:** 2026-07-14
- **Method or command:** Updated only the primary proof note, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier in
  addition to source/tests; inspected the complete diff; checked strict UTF-8,
  trailing whitespace, equation-tag uniqueness, display-math balance, exact
  changed-path scope, and `git diff --check`.
- **Relevant output:** Exactly nine intended paths are changed. All decode as
  strict UTF-8 and contain no trailing whitespace. The proof note has 94
  unique equation tags and 195 opening/closing display pairs. Complete diff
  inspection and `git diff --check` pass.
- **Interpretation:** Durable memory states the exact theorem, its scope, its
  verification basis, and the remaining two residue classes consistently.
- **Limitations:** The worktree is intentionally unstaged and uncommitted for
  manual review; hosted CI remains unchecked.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---minimal-memory-and-final-handoff`
