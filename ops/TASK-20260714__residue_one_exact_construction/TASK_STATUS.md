# TASK_STATUS - TASK-20260714__residue_one_exact_construction / Residue-One Exact Construction

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine whether every `n=5k+1`, `k>=2`, has an explicit
  cyclic core order with product-distance score at most
  `H_n=(4k+2)^2/2`, without canonical enumeration beyond `n=11`.
- **Expected output:** a search-free generator, a separate exact proof by
  positional-distance class and closing arcs, independent targeted tests,
  and only the necessary proof, roadmap, and durable-memory updates.

## Scope

- **In scope:** the residue class `n == 1 (mod 5)`; exact bounded search for
  candidate falsification and pattern identification; source, tests, proof,
  roadmap, and durable task/project memory.
- **Out of scope:** residue class two; canonical factorial enumeration above
  `n=11`; geometric-optimum claims; artifacts, schemas, CLIs, Git writes, or
  changes to upstream Ringmin.

## Verified Facts

- The startup worktree was clean and all required project state was read.
- Two independent derivations found the same uniform path construction for
  every `k>=2`; an independent exact diagnostic checked its local constraints
  through `k=5000`.
- The naive `e=2` specialization of the older block family is false:
  `(D-1)(2k+2)=H_n+2k`, where `D=4k+2`.
- EXACT THEOREM: the implemented search-free order satisfies
  \(W(\sigma_n^{(1)})=H_n=(4k+2)^2/2\) for every `k>=2`.
- EXACT THEOREM: the lower/upper squeeze gives
  \(B_n=W_n=H_n\) for every \(n\equiv1\pmod5\), \(n\ge11\).
- The residue roadmap now leaves only class two unresolved beyond the bounded
  table.

## Assumptions / Inferences

- None. Finite diagnostics are treated as falsification and regression
  evidence only; the all-`k` claim is established by the separate symbolic
  proof.

## Decisions And Rationale

- Add a separate residue-one generator and retain the older uniform
  eight-twenty-fifths generator unchanged.
- Reuse the exact closed formula for `H_n`; no duplicate threshold API is
  needed.

## Plan And Expected Delta

- Implement the generator and independent tests. COMPLETE.
- Write and audit the symbolic proof. COMPLETE.
- Correct only necessary global memory and the residue-class roadmap. COMPLETE.
- Run focused, integrated, full, artifact, and final diff verification.
  COMPLETE.

## Verification

- **Checks:** compile, Ruff, focused/integrated/full pytest, checked-artifact
  verification, independent exact oracles, mathematical/implementation/
  documentation audits, strict UTF-8, whitespace, proof delimiters, complete
  diff, and `git diff --check`.
- **Observed result:** compile and Ruff PASS; focused `31/31`; integrated
  `46/46`; full suite `159/159` outside the sandbox; checked artifacts
  accepted; exact oracles and independent audits PASS; all 10 changed paths
  pass strict UTF-8 and trailing-whitespace checks; the proof has 118 unique
  equation tags and 215 balanced display pairs; complete diff inspection and
  `git diff --check` PASS.
- **Limitations:** the sandboxed full suite retained 31 temporary-path setup
  errors and then passed unchanged outside the sandbox; no hosted CI result is
  available for the worktree.

## Blockers / Risks

- No current blocker.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact generator/proof/tests, full local suite,
  checked artifacts, independent audits, durable memory, and final diff
  hygiene all pass.
- **Files changed:** `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `start.md`,
  `research/NEXT_RESEARCH_STEPS.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`,
  `tests/test_product_distance.py`, and this three-file task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`, and `tests/test_product_distance.py`.
