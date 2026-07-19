# EVIDENCE - TASK-20260719 / Descending-Min PG49 Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / proof | Startup and Ferrers greedy theorem | product-distance note | PROVED |
| EV-002 | exact theorem | Exact score and all maximizers | fixed-order note | PROVED |
| EV-003 | counterexample | Exact zero-gain row | integer substitution | VERIFIED |
| EV-004 | exact theorem | K825 and PG46 comparisons | Abel bound | PROVED |
| EV-005 | exact theorem | Cubic coefficient and formula class | integrals / algebra | PROVED |
| EV-006 | bounded computation | Independent max-plus/shortcut diagnostic | exact_diagnostic.py | PASS |
| EV-007 | tests / checks | Final repository verification | recorded commands | PASS |
| EV-008 | review | Independent proof and diff audit | complete sources | PASS |

## EV-001 - Startup And Ferrers Greedy Theorem

- **Date:** 2026-07-19
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the PG37--PG99 proof chain,
  fixed-order K825/PG46 theorems, relevant dossiers, and clean Git status at
  `c310228d86fd0f0598dee1ff7984b5100726337b`.
- **Relevant output:** \(\Delta_j\in\{0,1\}\) and the descending induction
  gives the exact used suffix
  \([\kappa_j,\kappa_j+2m-1-j]\). At \(j=1\), it is
  \(\{1,\ldots,2m-1\}\); adding \(\alpha(0)=0\) gives a bijection whose
  every positive value is at least \(\kappa_j\).
- **Interpretation:** the rule is well defined and relation-compatible for
  every \(m\ge3\); (PG104) is its exact closed form.
- **Limitations:** this proves \(W=T\) only through the previously separate
  PG62 theorem and says nothing about \(K\) or geometry.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---strict-startup-and-greedy-invariant`.

## EV-002 - Exact Score And All Maximizers

- **Date:** 2026-07-19
- **Method or command:** direct block cancellation against the identity
  K825 backbone; exhaustive triple/singleton insertion gains; signed
  isolated-hole arc identity; two-, three-, four-, and long-edge shortcut
  bounds including low endpoints and cyclic closure.
- **Relevant output:** (KPGMIN-9) gives
  \(K=K_{825}+D_m+G_m\). Every nonnegative insertion gain occurs among the
  two lows in an early plateau singleton. Equations (KPGMIN-14)--(KPGMIN-15)
  give all maximizers and their exact number \(2^{|\mathcal Z_m|}\).
- **Interpretation:** complete all-subset classification without subset,
  matching, or permutation enumeration.
- **Limitations:** the finite diagnostic is not used in this proof; the
  result concerns only the one prescribed core order.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---exact-k-and-zero-gain-correction`.

## EV-003 - Exact Zero-Gain Counterexample

- **Date:** 2026-07-19
- **Method or command:** integer evaluation of both ceiling residuals,
  plateau assignment, and insertion gains at (KPGMIN-19); independent
  substitution by two read-only proof audits.
- **Relevant output:** at
  \(m=101805057120180546870\),
  \(j=29025982843749082380\), and
  \(\kappa_j=\kappa_{j+1}=14013559766810587979\), the assigned singleton is
  \(k=188597691163422599338\), with \(L_{m,j}=0\) and
  \(R_{m,j}=-1685934016300259008265\).
- **Interpretation:** universal uniqueness is an exact disproved claim. The
  low label \(\lambda_j\) can be independently included or omitted in an
  optimum.
- **Limitations:** the construction proves one zero row, not a classification
  or infinitude theorem for all zero rows.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---exact-k-and-zero-gain-correction`.

## EV-004 - Exact Comparisons

- **Date:** 2026-07-19
- **Method or command:** Abel summation of
  \(\sum_k(\alpha^{-1}(k)-k)r_k\), exact prefix-displacement bounds from the
  jump/plateau inverse, and five residue substitutions for
  \(q=\lfloor(4m+3)/5\rfloor\).
- **Relevant output:** \(D_m>m^2-4\) for \(m\ge5\). Initial exact pairs are
  \((D_3,G_3)=(12,0)\), \((D_4,G_4)=(-4,0)\), and
  \((D_5,G_5)=(56,0)\). Thus the order is below K825 and preclosing exactly
  at \(m=4\), above closing for every \(m\ge3\), and never tied.
- **Interpretation:** exact pointwise all-\(m\) comparison, independent of the
  bounded diagnostic.
- **Limitations:** these are \(K\)-comparisons of explicit orders, not global
  minimizing-order or geometric comparisons.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---comparators-coefficient-and-non-quasipolynomiality`.

## EV-005 - Cubic Coefficient And Formula Classification

- **Date:** 2026-07-19
- **Method or command:** weighted jump/plateau limits with
  \(f(x)=4x/(8+x)\), exact rational integration, positive-part boundary at
  the unique root \(a\in(0,1)\), algebraic field intersection, and
  Hermite--Lindemann.
- **Relevant output:** tail coefficient
  \(287.0007222855239280603\ldots\), insertion correction
  \(1.1675882515645331532\ldots\), total
  \(C=288.1683105370884612135\ldots\) in \(m^3\), and
  \(C/1000=0.2881683105370884612\ldots\) in \(n^3\). The exact expression
  has a nonzero logarithm of an algebraic number and is transcendental.
- **Interpretation:** the coefficient is strictly worse than \(143/500\),
  and no integer-valued eventual polynomial or quasipolynomial can equal the
  exact score function. Formula (KPGMIN-9) is the exact replacement.
- **Limitations:** displayed decimals are illustrations of the exact radical,
  algebraic-root, and logarithmic expressions.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---comparators-coefficient-and-non-quasipolynomiality`.

## EV-006 - Bounded Independent Diagnostic

- **Date:** 2026-07-19
- **Method or command:**
  `python ops/TASK-20260719__ferrers_greedy_exact_k/exact_diagnostic.py`.
- **Relevant output:** PASS; 28 max-plus/shortcut rows \(m=3,\ldots,30\);
  36,989,498 max-plus transitions; 958,916 oriented shortcut arcs; 998
  formula/comparator rows through \(m=1000\); exact anchor values at
  \(m=3,4,6,8,13,30\).
- **Interpretation:** independent integer corroboration of the closed greedy
  assignment, bounded uniqueness, exact score formula, comparator signs, and
  shortcut budgets. The increasing-path DP enumerates no subset, matching,
  or permutation.
- **Limitations:** no zero gain occurs only on checked rows
  \(m=3,\ldots,1000\). The diagnostic is bounded and standard-library-only;
  it does not replace any all-\(m\) proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---bounded-independent-diagnostic`.

## EV-007 - Final Repository Verification

- **Date:** 2026-07-19
- **Method or command:**
  - `python -m pytest -p no:cacheprovider`;
  - `python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py`;
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  - `python -m ruff check ops/TASK-20260719__ferrers_greedy_exact_k/exact_diagnostic.py`;
  - `python -m ruff format --check ops/TASK-20260719__ferrers_greedy_exact_k/exact_diagnostic.py`;
  - in-memory Python compile, source/tag audit, `git status --short`,
    complete `git diff`, and `git diff --check`.
- **Relevant output:** 283 complete tests passed in 65.04 seconds; four focused
  schema tests passed in 0.74 seconds; checked-artifact verification passed
  for four certificates and 76 local brackets; scoped Ruff lint/format,
  in-memory compile, exact PG100--PG109 and KPGMIN-1--KPGMIN-39 tag checks,
  whitespace, and final diff inspection passed.
- **Interpretation:** no regression, schema, artifact, syntax, formatting,
  structural, or diff-hygiene failure remains.
- **Limitations:** hosted CI was not run. The final proof-note edits are
  documentation-only and do not enlarge the bounded diagnostic.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---final-strict-verification-and-handoff`.

## EV-008 - Independent Review And Diff Audit

- **Date:** 2026-07-19
- **Method or command:** independent read-only audits of the greedy invariant,
  gain signs, exact zero row, signed shortcuts, Abel comparison, asymptotic
  integrals, field/transcendence argument, and claim boundaries.
- **Relevant output:** all listed arguments reproduced independently. Audits
  caught the false provisional universal-uniqueness inference, required the
  bounded diagnostic wording to state its finite range, and requested
  explicit proofs for the plateau \(k\le j\) implication, the dual cutoff,
  the \(O(m^2)\) asymptotic remainder, and the singleton exclusion. Every
  point is incorporated in the final sources.
- **Interpretation:** the mathematical core is independently corroborated and
  contradictory evidence is durably preserved.
- **Limitations:** independent review is still human-readable proof review,
  not machine formalization.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---final-strict-verification-and-handoff`.
