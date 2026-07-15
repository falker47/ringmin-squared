# TASK_STATUS - TASK-20260715__lambda10_label2_core_classification / Lambda_10 Label-Two And Core Classification

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** classify label `2` in all 88 gaps of the eleven surviving
  partial `n=10` cycles, resolve every argmax and dihedral equivalence, and
  only then derive the complete-class count by inserting label `1`.
- **Expected output:** an exact variation-and-shortcut proof; a separate
  independent 88-by-511 test-only oracle; synchronized authoritative memory;
  no production or public-boundary change.

## Scope

- **In scope:** the eleven accepted cycles on labels `3..10`; all eight
  label-two gaps in each; exact scores and argmax subsets; dihedral core and
  complete class counts; proof, focused tests, authoritative summaries, and
  this dossier.
- **Out of scope:** exact geometry or `R_2^*(10)`; all-`n` formulas or
  asymptotics; production scorer, enumerator, canonicalizer, API, or public
  limit changes; interval backends, artifacts, schemas, examples, or Git
  writes.

## Verified Facts

- Startup completed on a clean worktree.
- The eleven partial parents give 88 distinct dihedral core candidates.
- Exactly 87 candidates have `K=323`; the sole exception is
  `(10,3,2,4,7,8,6,9,5)`, with `K=325`.
- Every core argmax is classified; exact label-one insertion gives 783
  complete dihedral minimizer classes only after the core proof.
- The independent test-only oracle evaluates all 44,968 core subsets and
  calls no production scorer, enumerator, or canonicalizer.

## Assumptions / Inferences

- The result is a finite exact combinatorial classification, not a geometric
  optimum or all-`n` theorem.
- The exhaustive test oracle audits the proof and is not its source.

## Decisions And Rationale

- Reuse the recorded label-three shortcut certificates to compute exact
  maxima constrained to retain label `3`.
- Separate the one exceptional partial parent before counting any classes.
- Resolve dihedral equivalence by deletion and trivial labelled stabilizers.
- Keep all new finite enumeration test-local and leave `src/` unchanged.

## Plan And Expected Delta

- Prove the 88-case score and argmax classification. COMPLETED.
- Prove core completeness and dihedral distinctness, then derive the
  label-one count. COMPLETED.
- Add the independent 88-by-511 oracle. COMPLETED.
- Synchronize durable memory and run complete verification. COMPLETED.

## Verification

- **Checks:** focused/module/full pytest, checked-artifact semantic and schema
  regressions, Ruff, compilation, independent audits, and final diff/scope
  hygiene.
- **Observed result:** focused oracle `1 passed, 33 deselected`; complete
  cyclic-ratio module `34 passed`; complete suite `210 passed`; schema
  regression `4 passed`; semantic verifier accepted `4` certificates and
  `76` local brackets; Ruff, compilation, three independent audits, and final
  diff/scope hygiene all passed. The failed first full-suite attempt is
  preserved in `EVIDENCE.md` as a sandbox permission/provenance event; the
  required unrestricted rerun passed.
- **Limitations:** hosted GitHub Actions has not been run or independently
  inspected for this worktree.

## Blockers / Risks

- No current blocker.
- The score-325 exception is unique only among the 88 candidates forced by
  the earlier equality classifications.

## Next Atomic Action

- User reviews the final diff and performs a manual commit if accepted.

## Handoff

- **Last verified result:** structural proof, exhaustive test-only oracle,
  complete suite, artifact regressions, and independent audits agree on the
  87/1 classification, every argmax, and the 88/783 dihedral counts.
- **Files changed:** proof note, focused test module, authoritative memory,
  current status, roadmap, and this task dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `tests/test_fixed_order_cycle_ratio.py`, and this file.
- **Review state:** implementation and verification are complete; no files
  are staged or committed by Codex.
