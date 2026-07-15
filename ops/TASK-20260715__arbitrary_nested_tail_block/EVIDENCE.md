# EVIDENCE - TASK-20260715__arbitrary_nested_tail_block / Arbitrary Nested-Tail Block

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / test | Clean startup, scope audit, and focused baseline | authoritative files and cyclic-ratio tests | PASS |
| EV-002 | exact proof | General split-history bijection and prefix formula | cyclic-ratio proof note | PASS |
| EV-003 | exact proof / audit | Uniform \(O(rn^2)\) squeeze and sublinear asymptotics | cyclic-ratio proof note | PASS |
| EV-004 | exact computation / test | Bounded \(r=4\) coverage and admissible domino | cyclic-ratio tests | PASS |
| EV-005 | verification / review | Full regression, independent audits, and final hygiene | local commands and diff | PASS WITH RECORDED UNRELATED LINT |

## EV-001 - Startup, Scope, And Baseline

- **Date:** 2026-07-15
- **Method or command:** Read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, the preceding three-tail dossier, the relevant proof,
  roadmap, and test sources; inspected Git; ran
  `python -m pytest tests/test_fixed_order_cycle_ratio.py -q`.
- **Relevant output:** initial tree clean on `main` at `006aa61c71ad`;
  focused baseline 40 passed.
- **Interpretation:** the bounded STRICT task can proceed without mixing
  unrelated changes.
- **Limitations:** startup and a passing baseline do not establish the new
  theorem.
- **Linked log entry:** TASK_LOG.md, Startup And Scope.

## EV-002 - Exact Split-History Parametrization

- **Date:** 2026-07-15
- **Method:** Put \(\ell=m+r-1\), start from a simple cycle on
  \(S_\ell\), insert \(\ell-1,\ldots,m\) into literal current edges, and
  reverse the process by deleting \(m,\ldots,\ell-1\). Audit the exact edge
  linkage and count both sides modulo dihedral symmetry.
- **Relevant output:** every outer cycle is uniquely one compatible history;
  the count is
  \((q-1)!q(q+1)\cdots(q+r-2)/2=(q+r-2)!/2\). If \(H_j\) is the
  \(j\)-th correction prefix, the exact objective is
  \(P(C)+\max_jH_j\).
- **Classification:** EXACT THEOREM.
- **Limitations:** the ordinary simple-cycle statement requires the inner
  tail to contain at least three labels; the two-label exception is outside
  the stated domain.
- **Linked log entry:** TASK_LOG.md, Exact Split-History Theorem.

## EV-003 - Uniform Error And Asymptotic Audit

- **Date:** 2026-07-15
- **Method:** Use distinct positive endpoint offsets to obtain
  \(\Delta_t\le t^2-2\), bound a signed prefix maximum by the sum of positive
  corrections, add the exact alternating-cycle excess, and keep the max/min
  order fixed during optimization.
- **Relevant output:**
  \[
  0\le\gamma^{(r)}_{m,n}-P^*_{m+r-1,n}
  \le\sum_{t=m}^{m+r-2}[t^2-2]_+<(r-1)n^2,
  \]
  \[
  \Gamma_n^{(r(n))}
  ={2(\sqrt2-1)\over3}n^3+O(r(n)n^2)
  ={2(\sqrt2-1)\over3}n^3+o(n^3)
  \quad(r=o(n)).
  \]
- **Independent review:** three read-only derivations agreed on the domain,
  bijection, bound, sublinear conclusion, and the linear first non-excluded
  scale. They also required preserving nested histories and forbade exchanging
  \(\max_m\) with \(\min_\sigma\).
- **Classification:** EXACT METHOD-SPECIFIC THEOREM / LIMITATION.
- **Limitations:** the estimate does not determine the optimized linear-scale
  block or an exact leading constant for the full problem.
- **Linked log entry:** TASK_LOG.md, Uniform Bound And Growth Scale.

## EV-004 - Bounded Exact Oracle

- **Date:** 2026-07-15
- **Environment:** local Windows host; exact integer arithmetic only in the
  new paths.
- **Oracle design:** generate base dihedral cycles test-locally, recursively
  split every current edge, audit every correction/score/linkage/signature,
  and compare the full final signature map with independently generated outer
  cycles. No production scorer, canonicalizer, or enumerator is called.
- **Relevant output:** five bounded rows cover \(r=2,3,4\). The main new row
  \((m,n,r)=(2,7,4)\) has 60 histories, 60 outer classes, four minimizers,
  and \((106,107,118)\). At \((2,8,4)\), three base classes expand to 360
  outer classes and give \((164,165,172)\). Twelve fully nested histories
  occur in the three-label-base \(r=4\) rows, and a literal domino attains
  \(E_{2,5}=23\).
- **Commands and output:** new-test selection 7 passed; complete cyclic-ratio
  module 47 passed; focused Ruff passed.
- **Classification:** VERIFIED FACT (FINITE EXACT TEST-ONLY COMPUTATION).
- **Limitations:** finite arithmetic and coverage checks do not prove the
  all-\(n\) theorem.
- **Linked log entry:** TASK_LOG.md, Bounded General-Block Oracle.

## EV-005 - Full Verification And Final Audits

- **Date:** 2026-07-15
- **Environment:** local Windows host; repository Python environment.
- **Commands and output:** complete pytest run succeeded over 223 collected
  tests; cyclic-ratio module 47 passed; checked-artifact verifier confirmed 4
  certificates and 76 local brackets; schema suite 4 passed; focused Ruff on
  the modified Python file passed.
- **Recorded failed check:** repository-wide Ruff reports four findings in
  files untouched by this task: unused defaultdict and local n in
  src/power_ringmin/critical_structure.py, unused sys in
  src/power_ringmin/fixed_order_artifact.py, and an unused imported formatter
  in tests/test_finite_results.py. These files have no task diff and were not
  modified.
- **Independent review:** proof audit passes every domain, indexing,
  bijection, count, correction, prefix, bound, max/min, asymptotic, and domino
  claim after two corrections: extending \(P^*_{\ell,n}\) to
  \(1\le\ell\le n-2\), and explicitly extending each outer tail cycle to a
  complete order. Oracle and synchronization audits also pass.
- **Boundary inspection:** no source, schema, example, verifier,
  configuration, or production path changed. Production complete-order
  enumeration remains \(3\le n\le8\) with ceiling 2,520.
- **Classification:** VERIFIED FACT (LOCAL REGRESSION) plus independent
  review of the EXACT THEOREM and method-specific limitation.
- **Limitations:** hosted GitHub Actions were not run for this worktree; the
  four repository-wide Ruff findings remain outside this task.
- **Linked log entry:** TASK_LOG.md, Full Verification And Handoff.
