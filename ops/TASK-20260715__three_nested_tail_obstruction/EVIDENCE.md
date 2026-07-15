# EVIDENCE - TASK-20260715__three_nested_tail_obstruction / Three Nested-Tail Obstruction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection | Clean startup and independent reduction audit | authoritative files and prior dossier | PASS |
| EV-002 | exact proof | Base-cycle double-split theorem and uniform squeeze | cyclic-ratio proof note | PASS |
| EV-003 | exact computation / test | Bounded compatibility, score, and squeeze checks | focused cyclic-ratio tests | PASS |
| EV-004 | verification / review | Full local regression and final diff hygiene | local commands and diff | PASS |

## EV-001 - Startup And Reduction Audit

- **Date:** 2026-07-15
- **Method or command:** Read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, the previous nested-tail dossier, and relevant
  proof/roadmap/test sources; ran read-only Git inspection; obtained three
  independent derivations.
- **Relevant output:** the initial tree was clean on main at c99c9b8b00ba;
  all derivations agreed on the prefix-sum reduction, interaction cases, and
  uniform quadratic error.
- **Interpretation:** the bounded STRICT task could proceed without
  production changes.
- **Limitations:** startup establishes scope, not the theorem.
- **Linked log entry:** TASK_LOG.md, Startup And Independent Reduction.

## EV-002 - Exact Three-Tail Proof

- **Date:** 2026-07-15
- **Method:** Delete \(m\), then \(m+1\), record the unique base cycle and
  split edges, compute the three exact prefix sums, audit literal linkage,
  and compare with both the exact base minimum and pairing floor.
- **Relevant output:**
  \[
  \gamma^*_{m,n}
  =\min_{C,e,f}\left[P(C)+\max(0,A,A+B)\right],
  \]
  \[
  0\le\gamma^*_{m,n}-P^*_{m+2,n}<2n^2,
  \qquad
  \Gamma_n^{(3)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
- **Independent review:** the final proof audit passed the domain, bijection,
  count, interaction taxonomy, nested-split dominance, signature conditions,
  uniform algebra, and discrete optimization. A transient proposed collapse
  to the two-tail obstruction was rejected after correcting
  \(\delta_m(a,m+1)=m^2+m-a\).
- **Classification:** EXACT THEOREM / EXACT METHOD-SPECIFIC LIMITATION.
- **Limitations:** no exact asymptotic value or convergence claim for
  \(\Lambda_n\) or \(R_2^*(n)\) follows.
- **Linked log entry:** TASK_LOG.md, Exact Three-Tail Theorem.

## EV-003 - Focused Exact Checks

- **Date:** 2026-07-15
- **Environment:** local Windows host; exact integer arithmetic only in the
  new test paths.
- **Oracle design:** generate base dihedral cycles independently, split every
  first and second edge literally, verify all cyclic sums and linkage
  identities, audit connected simple signatures, and compare with direct
  outer cycles.
- **Relevant output:** at \((m,n)=(2,7)\), 60 double splits equal all 60
  outer cycles, with 24 nested, 24 distinct-incident, and 12
  distinct-disjoint interactions. Exact
  \((P_{m+2,n},P^*_{m+2,n},\gamma^*_{m,n})\) rows are
  \((46,47,47)\), \((116,117,118)\), \((235,237,239)\), and
  \((320,322,323)\). The alternating construction passes its bounded grid.
- **Commands and output:** focused selection, 3 passed and 37 deselected;
  complete cyclic-ratio module, 40 passed; induced-subset module, 7 passed.
- **Classification:** VERIFIED FACT (FINITE EXACT TEST-ONLY COMPUTATION).
- **Limitations:** bounded computation verifies formulas and coverage only.
- **Linked log entry:** TASK_LOG.md, Exact Checks And Synchronization.

## EV-004 - Full Verification And Final Audits

- **Date:** 2026-07-15
- **Environment:** local Windows host; repository Python environment.
- **Commands and output:** complete local pytest suite, 216 passed;
  checked-artifact verifier, all 4 certificates and 76 local brackets
  verified; schema suite, 4 passed; Ruff, final focused tests, and diff
  hygiene pass.
- **Independent review:** separate proof, test, and adversarial scope audits
  pass. They confirm the exact \(P^*\) distinction, uniform bound algebra,
  production isolation, and absence of forbidden exact asymptotic claims.
- **Boundary inspection:** no src path changed; production complete-order
  enumeration remains bounded to \(n\le8\).
- **Classification:** VERIFIED FACT (LOCAL REGRESSION) plus independent manual
  review of the EXACT THEOREM and method-specific limitation.
- **Limitations:** hosted GitHub Actions were not run for this worktree.
- **Linked log entry:** TASK_LOG.md, Full Verification And Handoff.
