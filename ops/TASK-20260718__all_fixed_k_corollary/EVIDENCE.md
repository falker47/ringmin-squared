# EVIDENCE - All-Fixed-k Corollary

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | STRICT startup and stale-claim audit | authoritative memory / Git | pass |
| EV-002 | exact theorem | All-fixed-\(k\) lower corollary | CR28cr--dd / CR28dr--dw | proved |
| EV-003 | exact computation | Standalone \(\mathbb Q(\sqrt2)\) diagnostic | `exact_diagnostic.py` | pass |
| EV-004 | source | Authoritative synchronization and scope | requested Markdown files | pass |
| EV-005 | regression / audit | Repository verification and final diff | commands / Git | pass |

## EV-001 - Startup And Source Audit

- **Date:** 2026-07-18
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, CR28cr--CR28dd,
  CR28dr--CR28dw, and the normalized-simplex, arbitrary-charging, and global
  five-prefix dossiers; run `git status --short --branch`, `git rev-parse
  HEAD`, and targeted `rg` audits.
- **Relevant output:** clean `main` tracking `origin/main` at
  `6c5eb5b49e40f763a88580656f04a4143b2b4852`. Stale denials and current-
  coefficient claims were mapped across all requested authoritative sources.
- **Interpretation:** the task began isolated and the correction scope is
  documentation/proof plus one dossier-local diagnostic.
- **Limitations:** source inspection does not prove the new corollary.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---strict-startup-and-defect-isolation`.

## EV-002 - Exact All-Fixed-k Theorem

- **Date:** 2026-07-18
- **Method or command:** exact derivation from the unique normalized optimizer,
  the all-middle clipping formulas, CR28dw, CR28ap, and the additive geometric
  relation.
- **Relevant output:** for each fixed finite \(k\), the requested parameters
  are strictly ordered and all-middle, and
  \[
  L_\Lambda\ge p(\alpha_\infty)
  +{(3\alpha_\infty-1)^3M_k\over8}.
  \]
  Since \(M_k\nearrow1/3\),
  \[
  L_\Lambda\ge{434+4\sqrt2\over1587},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{434+4\sqrt2\over1587\pi}.
  \]
- **Interpretation:** exact method-specific theorem. The quantifiers are
  \(\forall k\,\exists N_k\), followed by a supremum of scalar inequalities.
- **Limitations:** no growing \(k=k(n)\), common threshold, limit interchange,
  finite rounding at the supremum, convergence, or exact leading constant.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---exact-all-fixed-k-derivation`.

## EV-003 - Standalone Exact Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python -B ops\TASK-20260718__all_fixed_k_corollary\exact_diagnostic.py`.
- **Relevant output:** `PASS: exact all-fixed-k diagnostic (k=1..8)`.
  Exact \(\mathbb Q(\sqrt2)\) arithmetic checks the density root, derivative,
  direct coefficient simplification, normalized recurrence, strict cutoff and
  weight order, all-middle margins, direct \(g\)-formula, segment telescope,
  monotone coefficient rows, and the rational separator from \(C_{5,*}\).
- **Interpretation:** verified bounded exact computation, independent of
  project production and test helpers.
- **Limitations:** the \(k\le8\) loop is corroboration; the written proof
  handles every fixed finite \(k\).
- **Linked log entry:** `TASK_LOG.md#2026-07-18---authoritative-synchronization-and-exact-diagnostic`.

## EV-004 - Authoritative Synchronization

- **Date:** 2026-07-18
- **Method or command:** source editing and repository-wide stale-claim audit.
- **Relevant output:** the primary proof, `research/ALL_N_LOWER_BOUND.md`,
  `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, roadmap, and
  relevant dossiers distinguish the all-fixed-\(k\) coefficient from the
  fixed-five template optimum.
- **Interpretation:** every requested authoritative source records the same
  theorem, quantifier order, scope, and limitations.
- **Limitations:** historical negative wording remains in append-only logs and
  evidence, but dated correction entries explicitly supersede it.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---authoritative-synchronization-and-exact-diagnostic`.

## EV-005 - Repository Verification And Final Diff

- **Date:** 2026-07-18
- **Method or command:** run the new diagnostic and its Ruff checks; rerun the
  normalized-simplex, arbitrary-charging, and global-five exact diagnostics;
  run focused and full pytest, checked-artifact verification, schema pytest,
  strict UTF-8/Markdown/LaTeX structure checks, repository-wide stale-claim
  searches, three independent read-only audits, `git status`, complete diff
  inspection, and `git diff --check`.
- **Relevant output:** new diagnostic PASS for \(k=1,\ldots,8\); historical
  diagnostics PASS (203,489 normalized grid states, 332,640 charging
  histories, all 21 global-five regimes); focused pytest PASS 101; full pytest
  PASS 283; four artifact certificates with 76 local brackets PASS; schema
  pytest PASS 4; 378 primary equation tags are unique; structural, stale-claim,
  scope, independent-proof/source/diagnostic audits, and final diff checks
  PASS.
- **Corrected failures:** the first Ruff format check reported that it would
  reformat the new diagnostic; Ruff formatting was applied and both final
  checks pass. Three preliminary PowerShell structure commands failed because
  of audit-script defects (a colon after a variable name, a regex that treated
  `t` literally, and missing spaces in compact `foreach` syntax); the
  corrected strict command passes and identifies no file defect.
- **Interpretation:** the requested documentation/proof correction is
  implemented and verified without protected-path changes; status is
  READY_FOR_REVIEW.
- **Limitations:** hosted CI is outside local verification scope; the user must
  inspect and commit manually.
- **Linked log entry:** `TASK_LOG.md#2026-07-18---regressions-independent-audits-and-handoff`.
