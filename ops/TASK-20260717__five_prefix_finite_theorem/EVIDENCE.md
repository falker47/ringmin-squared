# EVIDENCE - Five-Prefix Finite Floor/Ceiling Theorem

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | STRICT startup and task isolation | authoritative memory and Git | pass |
| EV-002 | exact theorem | Uniform threshold and exact rounded remainder | primary derivation | proved |
| EV-003 | exact computation | Sole standalone Fraction diagnostic | `exact_diagnostic.py` | pass |
| EV-004 | regression / static | Tests, artifacts, lint, and source structure | commands / source | pass after format/command corrections |
| EV-005 | audit / scope | Independent proof, synchronization, and final diff | source / Git | pass |

## EV-001 - Startup And Isolation

- **Date:** 2026-07-17
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, CR28az, CR28dr--CR28dw,
  CR28dx--CR28dz3, prior finite/asymptotic dossiers, and templates; inspect
  repository root, branch, commit, and worktree.
- **Relevant output:** clean `main` tracking `origin/main` at
  `941d0b6f5a7be00f71552bfd3771a841a7c05782`.
- **Interpretation:** verified task isolation and exact prior inputs.
- **Limitations:** source inspection does not prove the new finite theorem.
- **Linked log entry:** `TASK_LOG.md`, STRICT Startup And Isolation.

## EV-002 - Exact Threshold And Remainder

- **Date:** 2026-07-17
- **Method or command:** exact rational derivation from CR28az, CR28dr--CR28dw,
  CR28dx--CR28dz3, CR28ap, CR12h, and the pairing-floor identity.
- **Relevant output:** the exact rows \(234\) through \(246\) and a symbolic
  tail from \(247\) prove that \(234\) is the minimal uniform threshold; at
  \(233\), \(r_n=s_{1,n}=100\). With fixed \(\lambda_i\),
  \[
  \mathcal B_{5,n}
  =P_{r_n,n}+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})G_{n,\lambda_i}(s_{i,n}),
  \qquad
  \mathcal I_{5,n}=\lceil\mathcal B_{5,n}\rceil.
  \]
  The exact remainder has quadratic coefficient
  \(13/30+K\eta_n\) with
  \[
  K={34730769300472139183348711
   \over90863402469979616695362060900}>0,
  \]
  and satisfies
  \[
  \mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
  >{13\over30}n^2-{25\over2}n-{109\over6}>0
  \quad(n\ge234).
  \]
- **Interpretation:** exact finite method-specific theorem with the original
  rational parameters unchanged and no failure row on the valid domain.
- **Limitations:** the remainder belongs to the literal lower bound, not the
  unknown true block residual.
- **Linked log entry:** `TASK_LOG.md`, Exact Threshold And Remainder Completed.

## EV-003 - Sole Standalone Exact Diagnostic

- **Date:** 2026-07-17
- **Method or command:**
  `python -B ops\TASK-20260717__five_prefix_finite_theorem\exact_diagnostic.py`.
- **Relevant output:** PASS; minimal threshold `234`; failure row `233`;
  symbolic tail `247`; bridge `234..246`; exact coefficient; and
  `I_5,234=3569767`. The script checks the last failures of both block bounds,
  the first segment, four internal orders, five upper-middle predicates, and
  the absence of last-cutoff and lower-middle failures.
- **Interpretation:** verified exact computation covering every requested
  boundary predicate, fixed-weight local floors, integer closure,
  stationarity cancellation, and exact remainder.
- **Limitations:** bounded corroboration only; the written inequalities prove
  the all-\(n\ge234\) tail.
- **Linked log entry:** `TASK_LOG.md`, Standalone Diagnostic And
  Synchronization.

## EV-004 - Regression And Static Verification

- **Date:** 2026-07-17
- **Method or command:** Ruff check/format; focused and full pytest;
  checked-artifact verifier; schema tests; equation-tag and Markdown/LaTeX
  structure checks.
- **Relevant output:** Ruff PASS after two recorded mechanical format passes;
  101 focused and 283 full tests PASS; verifier accepts 4 certificates and 76
  local brackets; 4 schema tests PASS; 343 equation tags are unique; display
  and aligned environments balance across every changed Markdown source.
- **Corrected failed checks:** Ruff initially requested formatting and did so
  again after substantive diagnostic edits. One first PowerShell environment
  audit had an empty-pipe parser error; the corrected command produced the
  recorded counts. No mathematical assertion or repository regression
  failed.
- **Interpretation:** repository behavior, exact diagnostic, proof structure,
  and source structure pass after mechanical corrections.
- **Limitations:** hosted GitHub Actions were not inspected.
- **Linked log entry:** `TASK_LOG.md`, Regression And Audit Corrections and
  Failed Checks Preserved.

## EV-005 - Independent Audits And Final Scope

- **Date:** 2026-07-17
- **Method or command:** independent read-only audits of threshold/minimality,
  exact remainder/sign, and authoritative synchronization/scope; complete
  tracked/untracked diff, encoding, and protected-path inspection.
- **Relevant output:** threshold and remainder audits PASS. The first
  synchronization audit correctly found two stale finite-rounding statements
  and a diagnostic-coverage wording mismatch; all were corrected. The stable
  final audit confirms exactly ten intended files, no protected-path change,
  cross-source agreement of every exact value and domain, 343 unique tags,
  balanced source environments, strict UTF-8/LF encoding, no trailing
  whitespace, and a clean `git diff --check`.
- **Corrected failed checks:** one independent byte pipeline timed out and one
  first expected-path comparison accidentally nested its arrays; efficient
  corrected reruns passed all byte and exact-path assertions.
- **Interpretation:** no mathematical or scope defect remains; the tree is
  ready for manual review.
- **Limitations:** manual user review and commit decision remain.
- **Linked log entry:** `TASK_LOG.md`, Regression And Audit Corrections and
  Final Audit And Handoff.
