# EVIDENCE - TASK-20260718 / Preclosing PG46 Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup, scope, and exact order | repository sources and Git | PASS |
| EV-002 | exact theorem | Hole/shortcut certificate and block sum | fixed-order proof | PROVED |
| EV-003 | bounded exact computation | Independent max-plus and shortcut audit | exact_diagnostic.py | PASS |
| EV-004 | source inspection | Authoritative synchronization | research/root notes | PASS |
| EV-005 | tests / checks | Final repository verification | commands below | PASS |
| EV-006 | review | Final diff and independent audits | complete diff | PASS |

## EV-001 - Startup Scope And Order

- **Date:** 2026-07-18
- **Method or command:** read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, relevant PG46, closing-PG46, and K825 sources/dossiers;
  ran git status --short --branch, git rev-parse HEAD, and targeted source
  searches.
- **Relevant output:** clean main tracking origin/main; HEAD
  113d6f9173213c9ff2363328cec823fb32b2377a; PG46 specialized to target
  \((m,2m-2)\) gives one explicit non-wrapping interval shift.
- **Interpretation:** safe STRICT startup and an unambiguous fixed-order task.
- **Limitations:** source inspection alone proves no induced-subset optimum.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---strict-startup-and-order-reconstruction.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-18
- **Method or command:** exact substitution into the PG46 blocks; exhaustive
  isolated-hole gains; compressed-path shortcut audit split by endpoint and
  edge count; literal cyclic-closure calculation; direct block summation and
  terminal-block cancellation against closing PG46.
- **Relevant output:** the unique optimizer is
  \(S_m=\{4m+1,\ldots,10m+3\}\),
  \(K=(572m^3+631m^2+235m+22)/2\), minimum hole gain \(28m+12\), and
  minimum nontrivial shortcut margin \(12m+4\). Exact differences are
  \(K-K_{\rm cl}=6m\) and \(K-K_{825}=m^2-4\).
- **Interpretation:** exact all-\(m\), construction-specific theorem; the
  preclosing witness is strictly worse than both comparators for every
  admitted row and retains coefficient \(143/500\).
- **Limitations:** this proves no angular, geometric, or global-minimization
  statement and does not compare exact fixed-order angular thresholds.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---symbolic-certificate-derived.

## EV-003 - Bounded Exact Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  python ops/TASK-20260718__pg46_preclosing_exact_k/exact_diagnostic.py.
- **Relevant output:** PASS; 28 max-plus/shortcut rows \(m=3,\ldots,30\);
  36,989,498 DP transitions; 958,916 oriented shortcut arcs; 998 direct
  formula rows through \(m=1000\); minimum row
  \((K_{\rm pre},K_{\rm cl},K_{825})=(10925,10907,10920)\).
- **Interpretation:** independently corroborates the exact order, value, sole
  optimizer, hole/shortcut minima, both comparison identities, and leading
  coefficient. The increasing-path DP enumerates neither subsets,
  permutations, nor matchings.
- **Limitations:** bounded exact computation is not the source of the
  all-\(m\) proof. It imports only the standard-library Fraction class and no
  project or test helper.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---bounded-diagnostic-passed.

## EV-004 - Authoritative Synchronization

- **Date:** 2026-07-18
- **Method or command:** line-by-line cross-source inspection of
  research/FIXED_ORDER_CYCLE_RATIO.md,
  research/PRODUCT_DISTANCE_SURROGATE.md,
  research/NEXT_RESEARCH_STEPS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, and this task dossier.
- **Relevant output:** all sources agree on the order, sole tail, cubic,
  \(n\)-form, \(6m\) and \(m^2-4\) differences, pointwise ordering, cubic and
  quadratic coefficients, minimum row, diagnostic scope, and claim limits.
  The roadmap and durable memory now recommend the Ferrers-count logarithmic
  asymptotic as the next separate task.
- **Interpretation:** the prior closing theorem remains intact and the new
  preclosing result is classified separately. No \(W\)-to-\(K\), angular,
  geometric, or global-optimality implication is introduced.
- **Limitations:** historical append-only dossiers are not rewritten.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---synchronization-regressions-and-review.

## EV-005 - Final Repository Verification

- **Date:** 2026-07-18
- **Method or command:** the EV-003 diagnostic; in-memory compile;
  python -m ruff check and python -m ruff format --check on the diagnostic;
  python -m pytest -p no:cacheprovider;
  python -m pytest -p no:cacheprovider
  tests/test_checked_artifact_schema_validation.py;
  python -m power_ringmin.verify_checked_artifacts; a standalone
  source/tag/LaTeX/UTF-8/newline/cache audit; git status, full diff inspection,
  and git diff --check.
- **Relevant output:** diagnostic PASS; compile PASS; Ruff PASS; complete
  pytest 283 passed in 61.29 seconds; schema 4 passed; artifact verifier
  certificates=4, local_brackets=76, summary values 3,4,5,6; source structure
  PASS on 10 paths, 530 fixed-order tags, all 20 KPG46P tags, and Sections
  1--13; diff check has no output.
- **Corrected failed checks:** an initial structure one-liner incorrectly
  required whole-file display-delimiter counts in a long historical note;
  the added Section 12 itself is balanced and the corrected scoped check
  passes. A second draft incorrectly required tag uniqueness across every
  research file, although unrelated notes reuse simple numeric tags; the
  corrected authoritative-file audit finds 530 unique tags and the exact
  KPG46P-1--KPG46P-20 sequence.
- **Interpretation:** the new proof/diagnostic and existing repository
  behavior verify together; the failed draft checks were checker-scope
  defects and exposed no source or theorem defect.
- **Limitations:** hosted CI was not inspected. The finite diagnostic remains
  corroborative rather than the infinite proof.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---synchronization-regressions-and-review.

## EV-006 - Independent Review And Diff Audit

- **Date:** 2026-07-18
- **Method or command:** three independent read-only audits of proof algebra,
  hole and shortcut-role completeness, cyclic closure, diagnostic semantics
  and independence, comparison/asymptotic arithmetic, claim limits,
  synchronization, and complete changed-path scope.
- **Relevant output:** reviewers independently reproduced the formula,
  optimizer, margins, and comparisons. They found one missing pair of
  LaTeX backslashes in KPG46P-9 and a boundary-ambiguous ellipsis in the
  KPG46P-2 backbone at \(m=3\). Both were corrected with explicit
  backslashes before both qquad commands and a boundary-safe indexed
  concatenation, then re-audited PASS. Final scope is six authoritative
  Markdown files plus this
  four-file dossier; no production, test, artifact, schema, certificate,
  cache, or upstream path changed.
- **Interpretation:** the exact theorem, finite corroboration, limitations,
  and durable handoff are READY_FOR_REVIEW.
- **Limitations:** user review and commit are manual; no Git staging or commit
  was performed.
- **Linked log entry:**
  TASK_LOG.md#2026-07-18---synchronization-regressions-and-review.
