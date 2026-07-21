# EVIDENCE - Two-Block Finite-Prefix Charging

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / confirmation | Startup and bounded scope | project memory / Git | pass |
| EV-002 | exact theorem | Two-pool finite charging | CR28dw30--CR28dw34 | proved |
| EV-003 | exact theorem | Normalized objective and sharp upper | CR28dw35--CR28dw39 | proved |
| EV-004 | exact bounded computation | Independent literal-history oracle | literal_oracle.py | pass |
| EV-005 | regression / audit | Repository verification and final diff | commands / Git | pass |

## EV-001 - Startup And Scope

- **Date:** 2026-07-21
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`,
  CR28ax--CR28dw29, and prior finite-prefix dossiers; run
  `git status --short --branch` and `git rev-parse HEAD`.
- **Relevant output:** clean `main` worktree at
  `3390215b751c3b67fed1fd8d7f37a00ec1df275d`; no unrelated changes.
- **Interpretation:** the STRICT task started isolated and is limited to
  mathematical proof/documentation plus one dossier-local oracle.
- **Limitations:** source inspection alone proves no new theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-21---strict-startup-and-ansatz-formalization`.

## EV-002 - Exact Two-Pool Finite Theorem

- **Date:** 2026-07-21
- **Method or command:** exact convex bridge, history-relative first-split
  partition, injectivity of original-edge charging, and descending
  child-edge induction.
- **Relevant output:** (CR28dw33) assigns every original slack exactly once;
  (CR28dw34) proves
  \[
  \Lambda_n\ge\gamma^{(r)}_{1,n}\ge P_{r,n}
  +\sum_i L_i^+G_{n,\lambda_i^+}(s_i^+)
  +\sum_j L_j^-G_{n,\lambda_j^-}(s_j^-)
  \]
  on every finite admissible row.
- **Interpretation:** exact method-specific theorem. Pool separation does not
  reset the recursive base or duplicate parent slack.
- **Limitations:** this is one selected-tail charging ansatz, not an exact
  value or upper bound for \(\Lambda_n\).
- **Linked log entry:** `TASK_LOG.md#2026-07-21---exact-two-pool-charging-theorem`.

## EV-003 - Exact Normalized Classification

- **Date:** 2026-07-21
- **Method or command:** fixed-parameter \(n^{-3}\) limit, effective-weight
  concatenation, inverse bridge factorization on the strict domain, equality
  of the weak-order compact closures, coordinate clipping, and the
  increasing-\(\phi\) lower-Darboux integral bound.
- **Relevant output:** the normalized objective is (CR28dw35), its exact
  clipped form is (CR28dw37), and
  \[
  \max C^{\mathrm{2B}}_{k_+,k_-}=C_{k_++k_-,*}<C_{\mathrm{AF}},
  \qquad
  \sup_{k_+,k_-\ge1}C^{\mathrm{2B}}_{k_+,k_-}
  =C_{\mathrm{AF}}={434+4\sqrt2\over1587}.
  \]
- **Interpretation:** exact method-specific upper classification; the
  requested outcome is the upper-bound branch, with no stronger rational
  witness in this ansatz.
- **Limitations:** the result does not upper-bound the true \(\Lambda_n\) and
  supplies no common finite threshold at the unattained supremum.
- **Linked log entry:** `TASK_LOG.md#2026-07-21---exact-normalized-upper-classification`.

## EV-004 - Standalone Exact Oracle

- **Date:** 2026-07-21
- **Method or command:**
  `python -B ops\TASK-20260721__two_block_finite_prefix\literal_oracle.py`;
  final `python -m ruff check` and
  `python -m ruff format --check` on that file.
- **Relevant output:** PASS on 840 histories and 840 distinct final cycles;
  504 histories use both pools, 24 charge all four original edges, 576
  lower-block recursive splits inherit an upper-pool root, and 64 are deep
  descendants without a direct upper-label endpoint. All charge counters are
  zero or one. The exact local-floor sum is \(9239/72\), giving finite bound
  \(53879/72\). Final Ruff checks pass.
- **Corrected check:** the first Ruff format check requested one mechanical
  reformat; the oracle and theorem assertions already passed, and both final
  Ruff checks pass after formatting.
- **Interpretation:** verified bounded exact computation, independent of
  project source and test helpers.
- **Limitations:** exhaustive coverage of this one small base corroborates
  but does not prove the all-history or all-real theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-21---independent-bounded-accounting-oracle`.

## EV-005 - Repository Verification And Final Diff

- **Date:** 2026-07-21
- **Method or command:** rerun the new oracle and final Ruff checks; run
  `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`,
  `python -m pytest`, the checked-artifact verifier, focused schema
  pytest, the arbitrary-charging, global-clipped-envelope, and
  all-fixed-\(k\) exact diagnostics; audit equation tags, display/environment
  balance, UTF-8/LF/final-newline state, stale scope, and protected paths;
  obtain three independent read-only reviews; inspect all changed/new files;
  run `git status --short --untracked-files=all`,
  `git diff`, and `git diff --check`.
- **Relevant output:** focused pytest PASS 101 and full pytest PASS 283; four
  certificates with 76 local brackets and four schema tests PASS; historical
  diagnostics PASS on 332,640 six-prefix histories, 300 clipped Bellman
  states with 12 exact rows, and all-fixed-\(k\) rows \(1,\ldots,8\).
  Structural audit PASS with 856 unique equation tags, exactly one occurrence
  of each CR28dw30--CR28dw39 tag, 1,353 balanced standalone display pairs,
  and balanced relevant environments. All nine intended files pass the
  encoding/newline audit. Three independent mathematical/accounting/oracle
  reviews, protected-scope inspection, complete diff inspection, and final
  Git checks pass.
- **Corrected checks and review findings:** the initial Ruff format check
  requested one mechanical rewrite. Two preliminary structure commands
  overescaped the tag regex and then counted non-delimiter bracket
  occurrences; corrected commands pass. Reviewers found a missing
  \(\alpha<1\) qualifier, overbroad surjectivity wording before the compact
  closure was stated, and stale document dates; each was corrected and all
  final reviews pass. No mathematical formula, oracle result, production
  path, artifact, or certificate changed as a result.
- **Interpretation:** the exact theorem, sharp ansatz upper bound, bounded
  corroboration, synchronization, and protected scope are READY_FOR_REVIEW.
- **Limitations:** hosted CI is outside local verification.
- **Linked log entry:** `TASK_LOG.md#2026-07-21---regressions-audits-and-handoff`.
