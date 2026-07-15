# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact finite structural classification beyond the public
  cyclic-ratio enumeration boundary.
- **Current task:** classify label `2` in the eleven surviving partial
  `n=10` cycles, then derive the complete count through label `1`.
- **Task dossier:**
  `ops/TASK-20260715__lambda10_label2_core_classification/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review of the proof, oracle, durable
  memory, and final diff, followed by a manual commit if accepted.
- **Awaiting user review:** yes.

## Implemented Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md` now proves the exact label-two
  insertion classification over all eleven accepted partial cycles.
- The proof uses
  \(\Delta_2(a,b)=2(a+b)-ab=4-(a-2)(b-2)\), the previously recorded
  partial argmaxes, and constrained shortcut-gain pruning certificates.
- It resolves all dihedral equivalences before counting and derives the
  complete-class count only after the core classification is proved.
- `tests/test_fixed_order_cycle_ratio.py` adds a literal independent oracle
  over all 88 core orders and all 511 nonempty subsets of each, plus
  test-local dihedral keys for the core and complete counts.
- No production source, scorer, API, enumerator, or canonicalizer changed.
  The public complete-order domain remains `n<=8`.

## Exact Finite Result

- EXACT THEOREM: the 88 label-two insertions are 88 distinct dihedral core
  classes. Exactly 87 have \(K=323\).
- The sole exception is `(10,3,2,4,7,8,6,9,5)`, obtained by inserting label
  `2` in the `{3,4}` gap of `(10,3,4,7,8,6,9,5)`; it has `K=325` and sole
  argmax \(\{2,\ldots,10\}\).
- Among the 87 core minimizers, seven have exactly the two argmaxes
  \(\{5,\ldots,10\}\) and \(\{3,\ldots,10\}\), 40 have sole argmax
  \(\{5,\ldots,10\}\), and 40 have sole argmax
  \(\{4,\ldots,10\}\).
- Exact label-one elimination/insertion gives exactly
  \(87\cdot9=783\) complete dihedral minimizer classes: 63 retain the two
  argmaxes, 360 have sole argmax \(\{5,\ldots,10\}\), and 360 have sole
  argmax \(\{4,\ldots,10\}\).
- VERIFIED FACT: the independent oracle performs 44,968 literal subset
  evaluations and recovers every score, argmax, and dihedral count.

## Verification

- Focused oracle check: `1 passed, 33 deselected`.
- Full cyclic-ratio module: `34 passed`.
- Complete suite: `210 passed`. The first sandboxed attempt produced only
  permission/provenance setup failures; the required unrestricted rerun
  passed completely.
- Checked-artifact schema regression: `4 passed`; semantic verifier:
  `4` certificates and `76` local brackets verified.
- Ruff and `compileall` passed. Three independent STRICT audits found no
  residual mathematical, test-independence, documentation, or scope issue.
- Final Git hygiene passed: clean whitespace, no staged paths, no production
  diff, and no retained task-specific temporary directory.
- CURRENT HOSTED STATUS: GitHub Actions on Ubuntu/Python 3.11--3.13 has not
  been run or independently verified for this worktree.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` adds the label-two proof, exact
  argmax classification, dihedral completeness, and core/complete counts.
- `tests/test_fixed_order_cycle_ratio.py` adds the independent 88-by-511
  oracle and test-local orbit checks.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize the exact result, evidence
  role, limitations, and next research boundary.
- `CURRENT_STATUS.md` and the STRICT task dossier record durable handoff.

## Residual Limitations

- The classification is finite and combinatorial. It gives no exact value or
  geometric minimizer classification for \(R_2^*(10)\), no all-`n` formula,
  and no asymptotic claim.
- The score-325 exception is unique among the 88 candidates forced by the
  accepted equality chain, not among all nonminimizing core orders.
- Hosted GitHub Actions for this worktree has not been inspected.

## Proposed Next Task

In a fresh chat, extend the independent test-only Arb endpoint-sign
cross-check from the checked `n=3` certificate to the existing checked `n=4`
certificate, without changing production verification or certification
claims.
