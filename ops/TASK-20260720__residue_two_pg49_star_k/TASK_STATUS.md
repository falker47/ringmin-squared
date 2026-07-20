# TASK_STATUS - TASK-20260720 / Residue-Two PG49-Star K

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** evaluate exactly the induced-subset objective \(K\) for the
  unchanged core order fixed by (PGE2-1)--(PGE2-6) on
  \(n=10m+2\), \(m\ge1\).
- **Expected output:** the literal cyclic order, every maximizing subset, an
  exact all-row formula with residual branches, a complete deletion-gain and
  compressed-shortcut proof, exact same-row comparisons with the known
  residue-two order and K825, and one independent bounded standard-library
  max-plus/all-arcs diagnostic.

## Scope

- **In scope:** only the fixed map (PGE2-6); doubleton, singleton block,
  cyclic closure, empty intervals, and \(m=1,2\); exact comparison with the
  two named combinatorial orders on the same subsequence.
- **Out of scope:** candidate changes or searches; subset, matching,
  permutation, path-assignment, or alternative-order enumeration; production
  or test changes; angular, geometric, global-minimizer, or global-optimality
  conclusions.

## Verified Facts

- Startup found a clean `main` worktree after reading the repository contract,
  project brief, durable knowledge, current status, prior PGE2 dossier, and
  the relevant K825, residue-two, and odd-parity proof precedents.
- The candidate remains exactly (PGE2-6). No path assignment or orientation
  has been changed.
- The literal cyclic word and compressed backbone are (KPGE2-1) and
  (KPGE2-5), including the true closing segment through
  \((A_q,c_q,B_q,4m+1,D)\).
- For every \(m\ge1\), the unique maximizer is
  \(B_m=\{4m+1,\ldots,10m+2\}\), and its exact all-row score is (KPGE2-4).
  The only residual is \(m=1\) in the five-branch expansion, not in the
  all-row formula or argmax.
- All nine deletion-gain classes and every compressed shortcut are strict.
  The boundary transitions at \(m=1,2,3\), every empty range, the doubleton,
  singleton block, and cyclic closure are explicit.
- Exact subtraction proves the fixed PGE2 core is strictly lower than both
  the known residue-two order and K825 on every row of \(n=10m+2\).

## Decisions And Rationale

- Reconstruct the cyclic word directly from (PGE2-1)--(PGE2-6), including
  the literal retained closing label \(4m+1\).
- Apply the isolated-hole identity (K825-6)--(K825-9) only after auditing all
  nine deletion-gain classes and every compressed-arc length.
- Add exactly one dossier-local script that imports only the standard library,
  constructs no alternative order, and uses max-plus rather than subset
  enumeration.

## Plan And Expected Delta

- Prove the exact backbone and complete argmax classification.
- Sum the literal backbone, derive the residual branches, and compare exactly
  with the established residue-two and K825 orders.
- Add and run the sole independent diagnostic.
- Synchronize the proof note, authoritative summaries, roadmap, and dossier;
  then run proportional repository verification and finish
  `READY_FOR_REVIEW`.

## Verification

- **Checks:** symbolic proof, diagnostic, source audit, full repository
  tests, checked-artifact verification, independent mathematical and script
  reviews, and final diff hygiene.
- **Observed result:** the exact theorem, sole diagnostic, Ruff, 283-test
  suite, four-test schema suite, checked-artifact verifier, source structure,
  three focused independent audits, final synchronization audit, complete
  diff inspection, and `git diff --check` pass.
- **Limitations:** bounded computation will corroborate, not replace, the
  exact all-domain proof.

## Blockers / Risks

- No current blocker. Main rigor risks are the genuine cyclic cut, the
  exceptional threshold \(q=0\) at \(m=1\), empty shifted/singleton ranges,
  and distinguishing the two comparator orders from the fixed PGE2 order.

## Next Atomic Action

- User review and manual commit decision. Do not begin the proposed next
  research task in this chat.

## Handoff

- **Last verified result:** exact all-\(m\) theorem, strict two-comparator
  result, and passing bounded diagnostic plus repository verification.
- **Files changed:** fixed-order proof, pertinent authoritative summaries,
  current status, and this task dossier; production and tests are untouched.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, and this file.
