# EVIDENCE - TASK-20260804 / KR1G Fixed Recursive Count

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources; Git | PASS |
| EV-002 | proof / computation | Fixed-\(p\) finite theorem | authoritative proof | PASS |
| EV-003 | code / computation | Independent exact \(p=2\) checker | `exact_checker.py` | PASS |
| EV-004 | test / audit | Historical repository and final-diff verification | repository commands | PASS |
| EV-005 | proof / computation | Fixed-\(p\) Bellman and finite-minimum restoration | proof; `exact_checker.py` | PASS |
| EV-006 | test / audit | Bellman-repair local verification | repository commands | PASS |
| EV-007 | hosted CI | Baseline GitHub Actions verification | GitHub run 30937579466 | PASS AT BASELINE |

## EV-001 - Startup and source isolation

- **Date:** 2026-08-04
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, the relevant
  KR1G proof sections, and the preceding dossier; run `git status
  --short --branch` and `git rev-parse HEAD`.
- **Relevant output:** the accepted baseline is
  `069cb677278fc149e2f8fac49b43d3346949c19e`; the startup worktree was
  clean.
- **Interpretation:** no unrelated uncommitted work is mixed into this
  STRICT task.
- **Limitations:** this establishes local source state, not hosted CI state.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---strict-startup-and-fixed-count-isolation`.

## EV-002 - Fixed-p finite theorem

- **Date:** 2026-08-04
- **Method or command:** exact derivation from KR1G-5--KR1G-6; dynamic
  selected-prefix count; original-cycle deviation partition; simultaneous
  weighted Cauchy; two independent read-only proof audits; direct Python
  check of the \((q,\ell,p)=(7,3,2)\) recurrence and completion count.
- **Relevant output:** with \(|\mathcal R|=p\),
  \(m_p=q-\ell+p\),
  \(T^{(-\mathcal R)}=T-\sum_{\rho\in\mathcal R}d_\rho\), and
  \(Q^{(-\mathcal R)}=Q-\sum_{\rho\in\mathcal R}4/(2-\lambda_\rho)\),
  KR1G-98 gives
  \[
  \mathscr R_{k,n}(h)
  \ge\mathcal E_{\mathcal R}(h)
  +{(T^{(-\mathcal R)}_{k,n})^2\over
  Q^{(-\mathcal R)}_{k,n}+2m_p}.
  \]
  Every recursive term is nonnegative at arbitrary depth. The exact
  denominator identity yields KR1G-99, and fixed \((p,k)\) gives
  \(\tau_k^2/(\chi_k+2\mu_k)>0\) after \(n\to\infty\). The direct count
  check returned `42 15120 151200`: 42 target histories per canonical
  \(q=7\) cycle, 15,120 selected prefixes, and 151,200 one-label
  completions.
- **Interpretation:** the same universal lower-bound coefficient as the
  all-base theorem survives for every fixed \(p\), before the later
  \(k\to\infty\) limit.
- **Limitations:** there is no uniform threshold in \(p\) or \(k\), no
  theorem for \(p=p(n)\) or \(k=k(n)\), no closed-form evaluation or exact
  asymptotic value of the finite minima, and no geometric or
  minimizing-order consequence.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---fixed-p-finite-theorem-and-cubic-bound`.

## EV-003 - Independent exact p=2 checker

- **Date:** 2026-08-04
- **Method or command:**
  `python ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`;
  `python -m ruff check
  ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`;
  `python -m ruff format --check
  ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`.
- **Relevant output:** the two-weight-segment, one-completion-label fixture
  reports 360 cycles, 181,440 raw selected histories, 15,120 retained
  \(p=2\) prefixes, and 151,200 completions. Its three topology classes have
  5,040 histories each;
  5,040 selected targets and 30,240 completion targets have two inserted
  endpoints. Exact locked values are residual \(823/14\),
  position-sensitive bound \(21148/665\), and uniform bound \(81/5110\).
  The position sweep reports 2,520 raw and 1,296 retained histories with
  BBRR/BRBR/BRRB counts 720/360/216, relation counts 288 sibling, 576
  nested, and 432 different-root, plus 288 two-inserted targets. Its locked
  values are \(260/3\), \(589/21\), and \(25/24\). The checker prints PASS;
  Ruff lint and format checks pass.
- **Interpretation:** exact rational enumeration independently corroborated
  the generalized local identities, full KR1G-6 decomposition,
  nonnegativity, \(m_p\) partition, \(T,Q\) coordinate removal, radical and
  combined Cauchy, uniform positive-part bound, and a one-label instance of
  the arbitrary-completion recursion. EV-005 adds the required two-label
  Bellman audit.
- **Limitations:** the fixtures are bounded and rational; they are not
  rounded irrational all-middle rows and do not prove the all-\(q\) or
  asymptotic theorem. Their locked residual minima are fixture diagnostics,
  not exact infimum claims for the theorem's history classes.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---independent-exact-p2-checker`.

## EV-004 - Historical repository and final-diff verification

- **Date:** 2026-08-04
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  both recursive checker commands; Ruff commands from EV-003; exact
  recurrence and SymPy denominator identities; final equation-tag, display,
  roadmap/dossier-link, UTF-8/LF, trailing-whitespace, Git status, complete
  diff, and `git diff --check` audits.
- **Relevant output:** 283 tests pass in 65.79 seconds; all four checked
  artifacts pass with 76 local brackets and summary rows \(3,4,5,6\); all
  four focused schema tests pass. The new \(p=2\) and preceding \(p=1\)
  checkers pass, and Ruff reports no lint or format issue. Exact checks pass
  for the KR1G-89 \(p=0,p=1\) reductions and the \(p=2\) denominator
  identity. All 1,066 equation tags are unique; 40 Markdown links resolve,
  including 25 anchors; all eight changed text/code files are strict UTF-8
  without BOM or CR, end in LF, have balanced display/aligned delimiters,
  and contain no trailing whitespace. Final Git diff checks pass.
- **Interpretation:** the proof, stable memory, roadmap, status, independent
  checker, and unchanged production verification layer were consistent at
  committed baseline `0240613`. EV-006 records the rerun after the Bellman
  repair.
- **Limitations:** the first display-balance invocation counted every inline
  `\[`/`\]` occurrence in the long pre-existing proof and produced a false
  failure. The corrected audit counts exact display-delimiter lines and
  passes; the invocation defect did not expose a source defect. All checks
  are local rather than hosted CI, and bounded checker enumeration does not
  replace the symbolic theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---repository-verification-and-handoff`.

## EV-005 - Fixed-p Bellman and finite-minimum restoration

- **Date:** 2026-08-04
- **Method or command:** compare proof commits `069cb677` and `0240613`;
  rederive the Bellman induction on the full labelled cycle; derive the
  \(p=1\) specialization of \(A^{(q)}\); run
  `python ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`;
  run Ruff lint and format checks on that script.
- **Relevant output:** KR1G-91a restores
  \[
  V_j(C)=\min_{e=\{u,v\}\in E(C)}
  \max\{0,j(u+v)-uv+V_{j-1}(C\oplus_ej)\},
  \]
  and KR1G-91b is the exact finite minimum over
  \(\Pi_{q,\ell,p}\). The explicit identity
  \[
  A^{(q)}_{\ell,\ell-1}
  =\sum_{j=1}^{\ell-1}(q)_j(2j)(q-j)_{\ell-j-1}
  =(q)_{\ell-1}\ell(\ell-1)
  \]
  recovers the complete historical \(p=1\) formulation. The focused
  \(p=2\), \(s=3\) fixture checks one nonmonotone canonical base cycle, 504
  raw and 42 retained selected prefixes, both completion labels \(2,1\),
  and all 4,620 completions. The three selected topology counts are 14 each,
  the complete counts are 1,540 each, 1,680 completions use an
  inserted--inserted target, and the literal and independent Bellman
  fixture-global residual minima both equal \(1541/28\). The checker, Ruff
  lint, and Ruff format checks pass.
- **Interpretation:** the exact finite completion optimization is restored
  for every fixed \(p\) without altering KR1G-92--KR1G-101. The fixture
  directly verifies the two-label Bellman traversal and fixture-global
  prefix minimum identity.
- **Limitations:** the fixture is a bounded rational structural audit. Its
  Bellman excursion value is zero on every retained prefix because unused
  original edges permit negative completion steps; the nonzero fixture
  minimum peak is selected-window data. It does not replace the all-\(q\)
  induction or give a closed-form value for the general finite minimum.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---fixed-p-bellman-regression-correction`.

## EV-006 - Bellman-repair local verification

- **Date:** 2026-08-04
- **Method or command:**
  `python ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`;
  `python ops\TASK-20260724__kr1g_one_recursive_selected_split\exact_checker.py`;
  Ruff lint and format checks for both scripts; `python -m pytest -p
  no:cacheprovider`; `python -m pytest
  tests\test_n3_arb_interval_crosscheck.py -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  exact recurrence/denominator identities; final equation-tag, display,
  link, strict UTF-8/LF, trailing-whitespace, status, full-diff, and
  `git diff --check` audits.
- **Relevant output:** the fixed-\(p\) checker passes its 15,120-prefix
  structural fixture, focused 42-prefix/4,620-completion two-label Bellman
  fixture, and 1,296-history position sweep. The one-recursive checker
  passes 96,600 broad histories and 6,720 arbitrary completions. Ruff passes
  both scripts. The full suite reports 283 passed in 73.66 seconds; the
  focused Arb suite reports 3 passed; all four checked artifacts and 76
  local brackets verify with summary rows \(3,4,5,6\); all four schema tests
  pass. The \(A^{(q)}\) specializations pass on 75 finite rows and the
  fixed-\(p\) denominator identity simplifies to zero. A direct source-slice
  comparison confirms that KR1G-92--KR1G-101 are byte-for-byte unchanged.
  All 1,068 proof tags are unique; all 47 local Markdown links resolve,
  including 32 anchors; changed files are strict UTF-8/LF without trailing
  whitespace, and display environments are balanced. Final status/diff
  checks pass.
- **Interpretation:** the restored exact completion layer, unchanged
  KR1G-92--KR1G-101 bound, durable memory, historical correction, and
  unchanged production verification layer are locally consistent.
- **Limitations:** finite enumeration and symbolic spot checks corroborate
  but do not replace the general Bellman induction or asymptotic proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---bellman-repair-local-verification`.

## EV-007 - Baseline hosted GitHub Actions verification

- **Date:** 2026-08-04
- **Method or command:** query the public GitHub Actions API for exact
  baseline SHA `024061343070750a54661c80530b5a96dafdacd1`, then inspect run
  `30937579466` and its jobs through the connected GitHub service.
- **Relevant output:** the push-triggered `Verification` run was created at
  `2026-08-04T18:13:11Z`, completed at `2026-08-04T18:14:59Z`, and concluded
  `success`. Its Python 3.11, 3.12, and 3.13 jobs all completed successfully,
  including the full test suite, checked-artifact semantic verification,
  schema validation, and tracked-text whitespace step. Run URL:
  <https://github.com/falker47/ringmin-squared/actions/runs/30937579466>.
- **Interpretation:** hosted CI is green for the committed fixed-\(p\)
  baseline independently of the local checks.
- **Limitations:** the Bellman repair is an uncommitted working-tree delta,
  so no hosted run covers it. EV-006 is the authoritative verification for
  the current local changes; hosted CI must be rerun only after the user
  reviews and manually commits or pushes them.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---baseline-hosted-ci-record`.
