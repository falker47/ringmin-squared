# EVIDENCE - TASK-20260723 / KPGZERO Local CF Criterion

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / reduction | Startup and local problem | KPGZERO proof and predecessor dossier | VERIFIED |
| EV-002 | exact theorem | Local continued-fraction admission criterion | fixed-order proof | PROVED |
| EV-003 | bounded exact computation | Fixed falsification diagnostic | `exact_diagnostic.py` | VERIFIED |
| EV-004 | independent audit | Formula and synchronization audit | proof, synopsis, diagnostic | VERIFIED |
| EV-005 | regression / hygiene | Repository and artifact verification | repository root | VERIFIED |

## EV-001 - Startup And Local Problem

- **Date:** 2026-07-23
- **Method or command:** clean `git status`; read `AGENTS.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`,
  `research/NEXT_RESEARCH_STEPS.md`, KPGZERO-1--KPGZERO-41, the PG49
  synopsis, and the predecessor KPGZERO dossiers and diagnostics.
- **Relevant output:** KPGZERO-23 is an exact convergent/scale bijection;
  KPGZERO-20--KPGZERO-21 give four finite real quadratic windows, while
  KPGZERO-24 retained the unresolved global filtered-convergent frequency.
- **Interpretation:** a scan-free criterion for one convergent is a strict
  refinement that does not choose the global finite/infinite alternative.
- **Limitations:** source inspection alone does not establish the new
  formulas.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---strict-startup-and-exact-scope`.

## EV-002 - Exact Local Continued-Fraction Criterion

- **Date:** 2026-07-23
- **Method or command:** determinant identity for regular convergents;
  complete-quotient Möbius formula; exact factorization
  \(\phi(t)=(\xi-t)\Gamma(t,\xi)\); integer reduction of the four
  KPGZERO scale quadratics; exact signed ceiling and residue-class
  intersection; convex minimization on an arithmetic progression.
- **Relevant output:** (KPGZERO-24a)--(KPGZERO-24h) give the signed error,
  four normalized and integer windows, domain threshold, congruence class,
  exact finite scale interval, and
  \[
  \mathfrak D_{\delta,\nu}
  =\Delta_{\delta,\nu}-(2A_\nu g_*-b_{\delta,\nu})^2
  =-4A_\nu f_{\delta,\nu}(g_*).
  \]
  After domain and congruence compatibility, admission is equivalent to
  \(\mathfrak D_{\delta,\nu}\ge0\).
- **Interpretation:** this is an exact theorem for the individual
  convergent. Each admitted scale reconstructs \(m\) directly.
- **Limitations:** the theorem does not control how often the discriminator
  is nonnegative as \(\nu\to\infty\).
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---exact-local-criterion`.

## EV-003 - Fixed Falsification Diagnostic

- **Date:** 2026-07-23
- **Method or command:**
  `python ops/TASK-20260723__kpgzero_local_cf_criterion/exact_diagnostic.py`;
  `python -m ruff check
  ops/TASK-20260723__kpgzero_local_cf_criterion/exact_diagnostic.py`.
- **Relevant output:** `KPGZERO local-CF criterion diagnostic: PASS`;
  five fixed convergents and zero generated convergents; singleton fibres
  `L-/g=4`, `L+/g=1`, `R-/g=19`; one residue miss with integer window
  \([1,4]\); one positive ordinary discriminant with empty positive integer
  window; half-open residuals \(-1,0,D-1,D\); Ruff `All checks passed!`.
- **Interpretation:** exact fixed cases exercise every formula class and both
  half-open boundaries without an \(m\)- or \(g\)-scan.
- **Limitations:** the rational generic complete tail checks the universal
  identity, not the numerical value of the actual infinite complete quotient
  of \(\xi\). Finite cases can falsify but cannot prove the theorem or infer
  global frequency.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---fixed-standard-library-diagnostic`.

## EV-004 - Synchronization And Independent Audit

- **Date:** 2026-07-23
- **Method or command:** three independent read-only derivations/audits;
  direct comparison with KPGZERO-5--KPGZERO-14 and KPGZERO-20--KPGZERO-23;
  randomized in-memory comparison of the vertex discriminator with direct
  minima on 200,000 synthetic integer quadratic/progression cases; bounded
  in-memory comparison against the 354 historical proposed convergents.
- **Relevant output:** all audits agree on the complete-quotient sign, four
  coefficient rows, domain floor, reduced congruence, exact `isqrt`
  interval, and residue-aware discriminator. The historical bounded proposal
  set reproduces exactly its recorded 56 left and eight right scale pairs.
  Audit caught and corrected a notation collision and one copied predecessor
  denominator before final verification.
- **Interpretation:** independent derivations and discriminating comparisons
  corroborate the symbolic proof and diagnostic implementation.
- **Limitations:** randomized and bounded comparisons remain computational
  corroboration; the all-parameter claim rests on the proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---durable-synchronization`.

## EV-005 - Regression And Hygiene

- **Date:** 2026-07-23
- **Method or command:** the three KPGZERO diagnostic commands; scoped
  `python -m ruff check`; `python -m pytest`;
  `python -m pytest tests\test_checked_artifact_schema_validation.py`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; KPGZERO tag/reference audit;
  `git status --short`; `git diff`; `git diff --check`.
- **Relevant output:** all three diagnostics PASS; Ruff `All checks
  passed!`; full suite `283 passed`; schema test `4 passed`; verifier
  accepted four certificates, 76 local brackets, and the \(n=3,4,5,6\)
  summary; independent final audit PASS; tag/reference and diff hygiene
  clean.
- **Interpretation:** the final repository state passes every task-relevant
  regression, artifact, formula, synchronization, and hygiene check.
- **Limitations:** software and fixed-case checks do not decide the global
  arithmetic frequency; that remains exactly the unresolved statement
  KPGZERO-24.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---verification-and-ready-for-review`.
