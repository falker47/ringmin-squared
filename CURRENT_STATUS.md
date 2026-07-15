# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact finite classification of cyclic-ratio core
  minimizers at `n=9`.
- **Current task:** classify all core orders with \(K=239\), record every
  maximizing subset with an independent test-only oracle, and count complete
  minimizers through exact label-one elimination/insertion.
- **Task dossier:**
  ops/TASK-20260715__lambda9_core_minimizer_classification/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Finite Exact Classification

- EXACT THEOREM (FINITE SIX-LABEL EQUALITY CASE): if a core order has
  \(K=239\), its induced cycle on
  \(S_6=\{4,5,6,7,8,9\}\) is, up to dihedral symmetry,
  \[
  \Omega=(9,5,8,6,7,4),
  \]
  with \(P_\Omega(S_6)=239\) and \(P_\Omega(S_5)=238\). The proof refines
  the accepted \(S_6/S_5\) lemma: rearrangement equality is impossible in the
  nonexceptional branch, the \(\{8,9\}\) branch is too large, and the
  \(\{7,9\}\) table has one equality row.
- EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION): orient \(\Omega\) as
  displayed. Insert label \(3\) in one of the four gaps not incident to label
  \(4\), then insert label \(2\) in any of the seven resulting gaps. These
  \(4\cdot7=28\) dihedral classes are all and only the core orders with
  \(K=239\). Consequently
  \[
  \Lambda_9=239,
  \qquad
  \#\{\text{dihedral core minimizers}\}=28.
  \]
- EXACT ARGMAX CLASSIFICATION: all 28 classes maximize on \(S_6\).
  Twenty-seven do so uniquely. The canonical class
  `(9,4,7,6,8,3,2,5)` also maximizes on the full core
  \(\{2,3,4,5,6,7,8,9\}\).
- EXACT COMPLETE-CLASS COUNT: (CR12p)--(CR12q) make all eight insertions of
  label \(1\) into each minimizing core score-preserving and exclude \(1\)
  from every maximizing subset. The gap map is injective, so there are
  \[
  28\cdot8=224
  \]
  complete dihedral minimizer classes: 216 with sole argmax \(S_6\) and eight
  with the two argmax subsets of the exceptional core.
- LIMITATION: these are finite exact combinatorial results. They give no exact
  value of \(R_2^*(9)\), exact angular/geometric minimizer classification,
  finite geometric certificate, all-\(n\) formula, or asymptotic claim.

## Independent Finite Verification

- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a test-only oracle
  directly generates all \(7!/2=2{,}520\) dihedral core classes as
  `(9,*tail)` with `order[1] < order[-1]`. It calls no repository
  canonicalizer, public enumerator, or production scorer.
- The oracle literally evaluates all 255 nonempty subsets of every row,
  records every maximizing subset, and performs 642,600 exact integer subset
  evaluations. It recovers minimum 239, exactly the 28 hard-coded canonical
  minimizers, and the \(27+1\) minimizer-argmax pattern. Across all rows,
  2,412 have one argmax and 108 have two.
- The deterministic 84,395-byte full-row serialization has SHA-256
  `557226668a82f6489274571148572076e373d49baefaa61e6d1f5a458bb857a2`.
- The focused cycle-ratio module passes all 28 tests.
- The production enumerator remains unchanged and hard-rejects `n=9`; its
  public complete-order domain is still `3<=n<=8`. The coincident number
  2,520 in the oracle is the `n=9` core space, not an enlarged public
  complete-order domain.

## Changes

- `research/FIXED_ORDER_CYCLE_RATIO.md` contains the equality refinement,
  exact shortcut-gain placement proof, 28-class parametrization, complete
  count 224, argmax classification, and independent-oracle contract.
- `tests/test_fixed_order_cycle_ratio.py` contains the test-local direct core
  generator, literal subset/argmax scorer, parametrization check, hard-coded
  28 representatives, and deterministic full-record checksum.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` record the stable finite result and its
  geometric/public-boundary limitations.
- The new STRICT task dossier records chronology, proof evidence, local
  verification, and hosted-status separation.
- No production source, public limit, backend, verifier, certificate, checked
  artifact, schema, example, CLI, geometric claim, or all-\(n\) claim changed.

## Verification

- CURRENT LOCAL VERIFIED FACT: on local Windows with Python 3.14.3, the
  focused cycle-ratio module passes all 28 tests in 15.10 seconds and the
  complete repository suite passes all 201 tests in 55.99 seconds.
- CURRENT LOCAL VERIFIED FACT: explicit schema validation passes all 4 tests
  in 0.99 seconds. Checked-artifact semantic verification accepts 4
  certificates, 76 local brackets, and the `n=3..6` summary; no artifact or
  certification claim changed.
- CURRENT LOCAL VERIFIED FACT: targeted Ruff and Python compilation pass.
  Independent mathematical, oracle, and documentation audits accept the
  equality proof, 28/224 counts, canonical list, checksum, Python 3.11 syntax,
  evidence classification, and unchanged public/geometry boundaries.
- CURRENT LOCAL VERIFIED FACT: the final changed-file whitespace scan,
  complete diff inspection, `git diff --check`, and worktree-status review
  pass. The worktree contains only the intended tracked changes and new task
  dossier; nothing is staged.
- CURRENT HOSTED STATUS: GitHub Actions on Ubuntu/Python 3.11-3.13 has not
  been run or independently verified for this worktree. The preceding results
  are local and do not establish hosted CI status.

## Residual Limitations

- The 2,520-core oracle is independent finite implementation evidence; the
  equality and shortcut-gain argument is the mathematical classification
  proof.
- The 224 complete count follows from the exact insertion theorem and
  injective eight-gap map; the complete `n=9` space was not publicly
  enumerated.
- Existing interval-backend trust limitations and certified finite geometric
  claims are unchanged.

## Proposed Next Task

In a fresh chat, design a bounded independent interval-backend
cross-verification path for the existing checked artifacts, without generating
a larger finite certificate or changing current certified claims.
