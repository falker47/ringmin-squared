# EVIDENCE - TASK-20260715__nested_tail_cyclic_ratio_lower_bound / Nested-Tail Cyclic-Ratio Lower Bound

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection | Clean startup and scope reduction | authoritative files and relevant proof/test sources | PASS |
| EV-002 | exact proof | Sharp two-tail obstruction and optimized coefficient | cyclic-ratio and geometric proof notes | PASS |
| EV-003 | exact computation / test | Independent signature, insertion, and construction checks | focused cyclic-ratio tests | PASS |
| EV-004 | verification / review | Full local regression, hygiene, and independent audits | local commands and final diff | PASS |

## EV-001 - Startup And Scope Reduction

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant prior dossiers,
  `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/ALL_N_LOWER_BOUND.md`, focused test helpers, and roadmap context;
  ran `git status --short --branch` and `git rev-parse --short=12 HEAD`.
- **Relevant output:** startup worktree was clean on `main...origin/main` at
  `118d1494f6d2`; the public cyclic-ratio enumerator remains bounded to
  `n<=8` and need not change.
- **Interpretation:** no unrelated change or missing dependency blocks the
  bounded STRICT task.
- **Limitations:** startup inspection establishes scope, not the requested
  all-`n` theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---startup-and-scope-reduction`.

## EV-002 - Exact Two-Tail Proof

- **Date:** 2026-07-15
- **Method:** Delete label \(m\) from the induced cycle on \(S_m\), retain the
  resulting simple cycle on \(S_{m+1}\) and its distinguished split edge,
  and use the exact correction
  \(m(a+b)-ab=m^2-(a-m)(b-m)\). Minimize over all cycle/edge pairs, then
  bound the result below by the duplicated-pairing floor and above by a
  literal alternating simple cycle.
- **Relevant output:**
  \[
  P_{m+1,n}\le\beta_{m,n}\le P_{m+1,n}+n^2,
  \qquad
  \beta_n^{(2)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
  The proof explicitly requires a loopless connected degree-two full
  signature after any fixed insertion edge is restored. The global sandwich
  gives \(R_2^*(n)>\beta_n^{(2)}/\pi-n^2\).
- **Independent review:** three independent derivations agreed on the exact
  obstruction, insertion formula, signature conditions, uniform subcubic
  squeeze, optimizer \(\sqrt2-1\), and method-specific interpretation.
- **Classification:** EXACT THEOREM / EXACT METHOD-SPECIFIC LIMITATION.
- **Limitations:** no exact asymptotic value for \(\Lambda_n\) or
  \(R_2^*(n)\), and no statement about a number of coupled tails growing with
  \(n\), follows.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---exact-two-tail-theorem`.

## EV-003 - Independent Exact Checks

- **Date:** 2026-07-15
- **Environment:** local Windows host; exact integer arithmetic only in the
  new test paths.
- **Oracle design:** pair two test-local copies of every label, independently
  generate rooted/reflection-reduced simple cycles, compare their edge
  signatures for tail sizes three through six, insert \(m\) literally in
  every gap of four bounded cases, and evaluate the explicit alternating
  construction directly. No new path calls a production scorer,
  canonicalizer, or enumerator.
- **Relevant output:** total pairing-signature counts `(5,17,73,388)`, valid
  simple-cycle counts `(1,3,12,60)`, and exact
  `(pairing floor, minimum cycle, beta)` rows `(25,26,26)`, `(76,77,77)`,
  `(170,172,172)`, `(320,322,323)`. The alternating-cycle excess identities
  and \(8g(q)\le q^2\) hold on the checked grid.
- **Command:** `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py -k "pairing_signatures_require or nested_tail_bound or alternating_tail_cycle" --basetemp .tmp_pytest_nested_tail_focused`
  -> `3 passed, 34 deselected in 0.35s`.
- **Classification:** VERIFIED FACT (FINITE EXACT TEST-ONLY COMPUTATION).
- **Limitations:** bounded checks are verification only and do not replace the
  all-`n` proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---independent-exact-checks-and-documentation`.

## EV-004 - Full Verification And Final Audits

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3; production support
  remains Python 3.11+.
- **Commands and relevant output:** complete
  `tests/test_fixed_order_cycle_ratio.py` -> `37 passed`; complete
  `tests/test_induced_subset_lower_bound.py` -> `7 passed`; full
  `python -m pytest -p no:cacheprovider` -> `213 passed`; checked-artifact
  verifier -> all 4 certificates and 76 local brackets verified; schema suite
  -> `4 passed`; final focused selection -> `3 passed, 34 deselected`.
- **Static and hygiene checks:** Ruff passes; the changed test compiles;
  `git diff --check` and an explicit trailing-whitespace scan pass;
  task-created temporary output was removed; no path under `src/` changed; no
  staging or prohibited Git write occurred.
- **Independent review:** separate proof, test, and documentation/scope audits
  pass. The only audit finding was an omitted domain in the opening summary;
  the summary now states \(n\ge4\), \(1\le m\le n-3\), matching the proof and
  excluding the exceptional two-vertex double-edge convention.
- **Classification:** VERIFIED FACT (LOCAL REGRESSION) plus independent manual
  review of the EXACT THEOREM and EXACT METHOD-SPECIFIC LIMITATION.
- **Limitations:** GitHub Actions were not run for the uncommitted worktree;
  finite regression remains verification rather than proof of the all-`n`
  result.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---full-verification-and-handoff`.
