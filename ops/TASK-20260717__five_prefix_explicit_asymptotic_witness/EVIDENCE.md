# EVIDENCE - Five-Prefix Explicit Asymptotic Witness

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | STRICT startup and task isolation | authoritative memory and Git | pass |
| EV-002 | exact theorem | Rational all-middle \(k=5\) specialization | primary proof derivation | proved |
| EV-003 | exact computation | Standalone Fraction diagnostic | fraction_diagnostic.py | pass |
| EV-004 | regression / static | Tests, artifacts, lint, and source structure | commands / source | pass after one format correction |
| EV-005 | audit / scope | Independent proof, synchronization, and final diff | source / Git | pass |

## EV-001 - Startup And Isolation

- **Date:** 2026-07-17
- **Method or command:** read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, relevant proof sections and dossiers; inspect Git status,
  branch, and current commit.
- **Relevant output:** clean main tracking origin/main at
  \(8dc7d2313349136c5c1fc21e098829dcffb2b742\).
- **Interpretation:** verified task isolation and exact prior inputs.
- **Limitations:** source inspection does not prove the new specialization.
- **Linked log entry:** TASK_LOG.md, STRICT Startup And Isolation.

## EV-002 - Exact Rational Specialization

- **Date:** 2026-07-17
- **Method or command:** independent symbolic derivations from CR28cr--CR28cw,
  CR28dr--CR28dw, CR28dq11, CR28ap, and CR28.
- **Relevant output:** the fifth simplex row gives strict all-middle parameters
  at \(\alpha=13/30\), and
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000}
  >{75\over271}>C_{4,*}.
  \]
- **Interpretation:** exact method-specific asymptotic lower witness and exact
  strict improvement over the globally optimized four-prefix coefficient.
- **Limitations:** no finite rounding, global \(k=5\) optimization,
  growing-\(k\) uniformity, exact leading constant, or new geometric input.
- **Linked log entry:** TASK_LOG.md, Exact Five-Prefix Derivation.

## EV-003 - Standalone Fraction Diagnostic

- **Date:** 2026-07-17
- **Method or command:**
  python -B ops\TASK-20260717__five_prefix_explicit_asymptotic_witness\fraction_diagnostic.py
- **Relevant output:** PASS; \(q_5\), \(M_5\), \(C_{5,\mathrm{rat}}\), the
  separator, radical gap, and squared margin match the written exact values.
- **Interpretation:** verified exact computation covering recurrence, direct
  objective, stationarity, rational parameters, strict branch conditions,
  both coefficient routes, and comparison algebra.
- **Limitations:** corroboration only; the written identities prove the
  all-real result.
- **Linked log entry:** TASK_LOG.md, Standalone Exact Diagnostic.

## EV-004 - Regression And Static Verification

- **Date:** 2026-07-17
- **Method or command:** Ruff check/format; focused and full pytest;
  checked-artifact verifier; schema tests; equation-tag, Markdown/LaTeX,
  encoding, and whitespace audits.
- **Relevant output:** Ruff PASS after one mechanical format correction; 101
  focused and 283 full tests PASS; verifier accepts 4 certificates and 76
  local brackets; 4 schema tests PASS; 327 equation tags are unique and all
  changed-source environments balance.
- **Corrected failed checks:** the first Ruff format check requested
  reformatting and passed after the formatter ran. The first display-count
  regex ignored indented delimiters; a corrected whitespace-aware count
  balances every file. Initial dossier creation interpreted four LaTeX escape
  sequences as control bytes; the status and evidence files were rewritten
  and are subject to the final byte audit.
- **Interpretation:** repository behavior, proof structure, and source hygiene
  pass after correcting diagnostic/formatting defects.
- **Limitations:** hosted GitHub Actions were not inspected.
- **Linked log entry:** TASK_LOG.md, Synchronization And Regression.

## EV-005 - Independent Audits And Final Scope

- **Date:** 2026-07-17
- **Method or command:** three read-only audits of mathematics, asymptotics,
  synchronization/scope, plus complete tracked/untracked diff and encoding
  inspection.
- **Relevant output:** mathematical and asymptotic audits PASS; the first
  synchronization audit correctly rejected stale CURRENT_STATUS/dossier files
  and four control bytes. After correction, the synchronization/scope audit
  PASS confirms exactly the ten intended files, cross-source agreement of all
  exact values and conclusions, clean encodings and environments, one sole
  diagnostic, no protected-path changes, and a clean `git diff --check`.
- **Interpretation:** the corrected tree is internally synchronized and ready
  for manual review.
- **Limitations:** manual user review and commit decision remain.
- **Linked log entry:** TASK_LOG.md, Final Audit And Handoff.
