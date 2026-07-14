# EVIDENCE - TASK-20260714__residue_one_exact_construction / Residue-One Exact Construction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / exact computation | Startup, candidate falsification, and uniform construction | project memory, predecessor proof/source/tests, bounded exact probes | PASS |
| EV-002 | source / proof / test | Exact construction, symbolic proof, and targeted tests | product-distance source/tests/proof note | PASS |
| EV-003 | independent exact computation / review | Formula, implementation, proof, and documentation audits | independent oracles and read-only reviews | PASS after findings applied |
| EV-004 | command / test | Automated verification | compile, Ruff, pytest, checked-artifact verifier | PASS after environment rerun |
| EV-005 | documentation / hygiene | Durable memory and final diff audit | ten changed paths | PASS |

## EV-001 - Startup, Falsification, And Uniform Candidate

- **Date:** 2026-07-14
- **Method or command:** Inspected all required startup and relevant task
  state; used exact bounded positional-constraint reasoning only to falsify
  candidate forms and identify a uniform path pattern; independently checked
  permutation and distance-one, -two, and -three inequalities through
  `k=5000`. A Boolean position-label CSP used Z3 `4.16.0` under Python
  `3.14.3` on the bounded values `n=11,16,21,26,31`; no random seed was
  configured. The canonical factorial enumerator was not run above `n=11`.
- **Relevant output:** With `D=4k+2`, the naive old-family triple begins with
  an invalid edge because `(D-1)(2k+2)-D^2/2=2k`. Isolating `D-1` and shifting
  the triple endpoints yields a single uniform family for every `k>=2`.
- **Failed probe retained:** A preliminary nonlinear-integer Z3 probe over
  `k=2..8` produced no result within roughly 30 seconds and was terminated.
  This is a solver-formulation/runtime failure, not infeasibility evidence.
- **Interpretation:** Exact finite evidence identified and aggressively tested
  the candidate; the separate symbolic proof below establishes the all-`k`
  theorem.
- **Limitations:** Finite checks are not an all-`n` proof and do not establish
  optimality by themselves.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---startup-falsification-and-uniform-candidate`

## EV-002 - Exact Construction, Proof, And Tests

- **Date:** 2026-07-14
- **Method or command:** Added
  `residue_one_product_distance_order(n)` to
  `src/power_ringmin/product_distance.py`; added independent exact local,
  closing, broad integer, full all-pairs, and strict-domain tests to
  `tests/test_product_distance.py`; recorded R1C1--R1C24 and the updated
  squeeze RC5--RC6 in `research/PRODUCT_DISTANCE_SURROGATE.md`.
- **Relevant output:** The generator is linear-time integer arithmetic and
  contains no search. It covers both parities with no exceptional witness.
  The proof establishes permutation coverage, adjacent score exactly `h`,
  distance-two score exactly `h-1/2`, the distance-three bound, every
  closing pair, and automatic distances at least four.
- **Interpretation:** EXACT THEOREM:
  \(W(\sigma_n^{(1)})=H_n=(d_n-1)^2/2\), so
  \(B_n=W_n=H_n\) for every \(n\equiv1\pmod5\), \(n\ge11\).
- **Limitations:** This is an exact combinatorial surrogate theorem, not a
  geometric optimum or structural classification of all minimizing orders.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---exact-generator-proof-and-targeted-tests`

## EV-003 - Independent Exact Checks And Audits

- **Date:** 2026-07-14
- **Method or command:** Used independent integer oracles to reconstruct the
  formula and score its cyclic distance classes; commissioned separate
  read-only mathematical, implementation, and documentation audits.
- **Relevant output:** One oracle checked every `2<=k<=5000`. A final
  implementation oracle matched the generated tuple for every `2<=k<=2000`,
  plus `k=9999,10000,10001`; selected full all-pairs scores equal `h`.
  The implementation audit found no code/test issue. The proof audit identified
  only boundary wording at `k=2`; the documentation audit identified one
  missing `n>=9` roadmap domain. Both findings were applied, and the final
  audits report PASS.
- **Interpretation:** Independent exact computation, source inspection, and
  the symbolic proof agree. The class-one theorem does not rest on finite
  extrapolation.
- **Limitations:** The independent diagnostics are finite regression evidence;
  R1C1--R1C24 remain the all-`n` proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---independent-audits-and-full-verification`

## EV-004 - Automated Verification

- **Date:** 2026-07-14
- **Method or command:** Ran `py_compile`; Ruff; focused product-distance
  pytest; integrated product-distance/zigzag/induced-subset/insertion pytest;
  the complete pytest suite; and
  `python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** Compile and Ruff PASS; focused `31/31`; integrated
  `46/46`; complete suite `159/159` outside the sandbox. The semantic
  verifier reports `certificates=4 local_brackets=76` and summary values
  `3,4,5,6`.
- **Failed check retained:** The first sandboxed complete-suite run produced
  31 setup errors because pytest could not access
  `C:\Users\Falker\AppData\Local\Temp\pytest-of-Falker`. The unchanged
  suite passed outside the sandbox. No test body for the changed
  product-distance code failed.
- **Interpretation:** All executable and artifact checks pass; the retained
  errors isolate the known sandbox temporary-directory restriction.
- **Limitations:** Hosted GitHub Actions for the current worktree was not
  inspected.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---independent-audits-and-full-verification`

## EV-005 - Durable Memory And Final Diff Audit

- **Date:** 2026-07-14
- **Method or command:** Aligned `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, the proof note, residue roadmap, and this dossier;
  inspected the complete diff; checked strict UTF-8, trailing whitespace,
  equation-tag uniqueness, display-math balance, exact changed-path scope,
  and `git diff --check`.
- **Relevant output:** Exactly 10 intended paths are changed. All decode as
  strict UTF-8 and contain no trailing whitespace. The proof note has 118
  unique equation tags and 215 balanced opening/closing display pairs.
  Complete diff inspection and `git diff --check` pass.
- **Interpretation:** Durable memory consistently records the exact theorem,
  its evidence basis, and the sole remaining residue class. The task is ready
  for user review.
- **Limitations:** The worktree is intentionally unstaged and uncommitted;
  hosted CI remains unchecked.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---durable-memory-and-final-handoff`
