# EVIDENCE - TASK-20260715__lambda10_exact_finite_value / Exact Finite Value of Lambda_10

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection / exact probe | Clean startup and reduction | authoritative files and read-only arithmetic | PASS |
| EV-002 | proof | Pairing lemma and witness certificate | proof note | PASS |
| EV-003 | exact computation / test | 360-class and 511-subset independent checks | focused test module | PASS |
| EV-004 | verification / hygiene | Full suite and final review | repository checks | PASS |

## EV-001 - Startup And Reduction

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant accepted dossiers,
  the cyclic-ratio proof and scorer, focused tests, roadmap, and task
  templates; ran read-only Git inspection and exact integer-only exploratory
  probes.
- **Relevant output:** Git reports clean `main...origin/main` at
  `f5d056113d54`. The accepted reduction gives
  `Lambda_10=min_tau K(tau)`. The six-label pairing baseline is `320`; the
  only low levels requiring classification are `320`, `321`, and `322`.
- **Interpretation:** The requested result has a bounded proof-and-test path
  that leaves production scoring and its public `n<=8` boundary unchanged.
- **Limitations:** Exploratory arithmetic is design evidence, not the final
  recorded proof or regression.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-exact-reduction`.

## EV-002 - Pairing Lemma And Witness Certificate

- **Date:** 2026-07-15
- **Method:** Applied the exact duplicated-multiset rearrangement bound to the
  six labels `5..10`. For every partial pairing, paired the least remaining
  entry with each distinct mate and pruned exactly when partial cost plus the
  rearrangement lower bound on the remainder exceeded 322. Classified the
  eight leaves and then computed all 63 nontrivial oriented shortcut gains of
  the supplied nine-label witness.
- **Relevant output:** The pairing recurrence has surviving state counts
  `(1,2,3,6,6,10,8)` and terminal distribution one signature at 320, three at
  321, and four at 322. Only the signature
  `{5-9,5-10,6-8,6-10,7-8,7-9}` is a simple spanning cycle. Its six
  label-four insertion corrections are `(10,11,1,4,8,4)`, all positive.
  The witness has complete sum 319; its only positive nontrivial gains are
  `g(10,3)=4`, `g(10,4)=2`, and `g(10,7)=4`, and it has no nontrivial zero
  gain. Hence `K=323` with exactly the tails `5..10` and `3..10` maximizing.
- **Independent review:** a separate mathematical audit reconstructed the
  complete recurrence, all eight leaves, the unique cyclic signature, six
  corrections, all 63 gains, all complementary-gain identities, the subset
  decomposition including cardinality two, and both equality subsets.
- **Classification:** the lower lemma is an EXACT THEOREM (FINITE
  SEVEN-LABEL LEMMA); `Lambda_10=323` is a VERIFIED FACT (FINITE EXACT
  COMBINATORIAL RESULT).
- **Limitations:** no exact `R_2^*(10)`, geometric, all-`n`, asymptotic, or
  full core-minimizer classification follows.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---pairing-lemma-and-exact-witness`.

## EV-003 - Independent Finite Checks

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3; exact integer
  arithmetic only in the new paths.
- **Oracle design:** Fix label `10`, directly permute labels `4..9`, and keep
  the orientation whose second label is smaller than its last, giving exactly
  `6!/2=360` classes. Separately pair two local copies of labels `5..10`,
  retain every distinct low signature, and recognize loopless connected
  degree-two signatures. Literal position combinations score every one of the
  `2^9-1=511` nonempty witness subsets.
- **Relevant output:** The 360-class minimum is 323, with equality rows
  `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`. The independent pairing oracle
  reproduces all eight proof signatures and all six corrections. The 511
  subsets reproduce per-cardinality maxima
  `(100,180,242,288,318,323,321,323,319)` and exactly the two proved global
  argmax subsets.
- **Commands and output:** focused `-k lambda10` reports `2 passed in 0.16s`;
  the complete cyclic-ratio module reports `30 passed in 15.17s`.
- **Independent review:** an alternative all-`7!` orbit audit found exactly
  360 dihedral classes, each of size 14. A separate degree-two multigraph
  enumeration reproduced the `1/3/4` low signatures, and a direct bitmask
  oracle reproduced all 511 witness scores. The tests still pass when every
  imported production canonicalizer, enumerator, and scorer is replaced by a
  failing stub.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** this is finite implementation evidence and a proof audit,
  not the source of the lemma, a production `n=10` enumeration, or a geometric
  certificate.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---independent-test-only-oracles`.

## EV-004 - Complete Verification And Handoff

- **Date:** 2026-07-15
- **Environment:** local Windows host, Python 3.14.3. Hosted GitHub Actions on
  Ubuntu/Python 3.11--3.13 was not run or independently inspected for this
  worktree.
- **Commands and relevant output:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py -k lambda10 --basetemp .tmp_pytest_lambda10_focused`
    -> `2 passed, 28 deselected in 0.16s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp .tmp_pytest_lambda10_module`
    -> `30 passed in 15.17s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider --basetemp .tmp_pytest_lambda10_full`
    -> `206 passed in 66.94s`.
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
    -> accepted 4 certificates, 76 local brackets, and the checked `n=3..6`
    summary.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py --basetemp .tmp_pytest_lambda10_schema`
    -> `4 passed in 0.79s`.
  - `$env:PYTHONPATH='src'; python -m ruff check tests/test_fixed_order_cycle_ratio.py`
    -> `All checks passed!`.
  - `python -m compileall -q tests/test_fixed_order_cycle_ratio.py`
    -> exit code 0 with no output.
  - Final changed-file whitespace scan, `git status`, complete `git diff`,
    `git diff -- src`, and `git diff --check` -> PASS.
- **Independent audits:** mathematical, test, and documentation reviews found
  no remaining proof, coverage, independence, classification, or scope defect.
  Their terminology and roadmap-clarity suggestions were applied. Python 3.11
  syntax and used APIs were audited; a local Python 3.11 runtime was not
  available.
- **Temporary-path hygiene:** every task-created pytest base directory was
  resolved inside the workspace and removed after execution.
- **Interpretation:** the proof, exact finite oracles, documentation, and
  durable handoff are locally verified and ready for manual review.
- **Limitations:** local success does not establish hosted CI status. The
  result is finite and combinatorial; existing checked geometric artifacts and
  their guarded backend trust boundary are unchanged.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---complete-verification-and-handoff`.
