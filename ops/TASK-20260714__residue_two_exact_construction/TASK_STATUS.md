# TASK_STATUS - TASK-20260714__residue_two_exact_construction / Residue-Two Exact Construction

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** construct a search-free cyclic core order with score at most
  \(J_n=d_n(d_n-2)/2\) for \(n=5k+2\), \(k\ge2\), and combine it only with
  the accepted residue-two obstruction.
- **Expected output:** a symbolic parity-aware generator; separate proof of
  permutation, distances one through three, closing arcs, and all distances
  at least four; two independent all-pairs scorers; tests and durable memory.

## Scope

- **In scope:** the residue class \(n\equiv2\pmod5\), \(n\ge12\); the finite
  witness seeds only as falsification and structure clues; exact source,
  tests, proof, project memory, and task evidence.
- **Out of scope:** canonical enumeration beyond \(n=11\); new asymptotic
  coefficients; geometric-optimum claims; artifacts, schemas, CLIs, Git
  writes, or upstream changes.

## Verified Facts

- Required startup files, relevant predecessor dossiers, proof/source/tests,
  roadmap, and the initially clean worktree were inspected.
- Three independent mathematical analyses agree on the same symbolic family
  and all inequalities; an independent implementation audit also passes.
- EXACT THEOREM: the generated order is a permutation of \(\{2,\dots,n\}\)
  and satisfies
  \[
  W(\sigma_n^{(2)})=J_n
  \qquad(n=5k+2,\ k\ge2).
  \]
- EXACT THEOREM: the accepted lower obstruction and this order give
  \[
  B_n=W_n=J_n
  \]
  at \(n=12\) and for every \(n\equiv2\pmod5\), \(n\ge17\).
- The proof separately covers permutation, adjacency, positional distances
  two and three, all pairs crossing the displayed cut, and distances at least
  four using \(4J_n-n(n-1)=7k^2+33k+14>0\).
- The generator uses only linear integer/list operations and performs no
  search, solver call, permutation generation, or enumeration.

## Assumptions / Inferences

- The residue-two saturation lower obstruction is accepted project input.
- Finite exact checks are falsification and regression evidence only; the
  all-\(k\) conclusion comes from the symbolic proof.

## Decisions And Rationale

- Use the uniform \(D=d-1\) block family, which includes \(k=2\) without an
  exceptional production witness and attains \(J_n\) on an internal edge.
- Add a label-first all-pairs oracle alongside the existing position-first
  oracle; neither calls production scoring support.
- Keep canonical enumeration, geometric claims, and all asymptotic
  coefficients unchanged.

## Plan And Expected Delta

- Implement the generator and independent tests. COMPLETE.
- Write and independently audit the symbolic proof. COMPLETE.
- Run focused, integrated, full, artifact, and style verification. COMPLETE.
- Synchronize durable project memory. COMPLETE.
- Complete final documentation and diff hygiene. COMPLETE.

## Verification

- **Checks:** independent formula/code audits; compile; Ruff; targeted,
  focused, integrated, and full pytest; checked-artifact verification; TeX
  serialization repair and byte-level check; final documentation/diff audit.
- **Observed result:** independent audits PASS; new tests \(6/6\); focused
  \(41/41\); integrated \(56/56\); full suite \(169/169\); compile and Ruff
  PASS; checked artifacts accept 4 certificates, 76 local brackets, and
  summary values \(3,4,5,6\); strict text hygiene, complete diff inspection,
  and `git diff --check` PASS.
- **Retained correction:** the first proof patch interpreted several inline
  TeX backslashes as escape characters. The mathematical audit found the
  rendering defect; the proof was repaired, after which its section has
  balanced inline delimiters and no lone carriage returns.
- **Limitations:** the full suite used the already required unsandboxed system
  temporary-directory access; hosted CI was not inspected.

## Blockers / Risks

- No current blocker.
- This is a combinatorial surrogate theorem, not a new geometric optimum,
  leading coefficient, or asymptotic coefficient.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** formula, proof, implementation, independent
  scorers, all local verification, durable memory, and final diff audit pass.
- **Files changed:** source, tests, proof, project state/roadmap, and this
  three-file task dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md,
  src/power_ringmin/product_distance.py, and
  tests/test_product_distance.py.
