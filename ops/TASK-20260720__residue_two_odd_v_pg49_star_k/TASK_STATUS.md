# TASK_STATUS - TASK-20260720 / Residue-Two Odd-v PG49-Star K

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** evaluate exactly the induced-subset objective \(K\) for the
  unchanged core order fixed by (PGE2ODD-6) on
  \(n=10m+7\), \(m\ge1\).
- **Expected output:** the literal cyclic order, every maximizing subset, an
  exact all-domain formula and every residue branch, a complete cancellation-
  gain and compressed-shortcut proof, explicit \(m=1,2,3\), empty ranges,
  singleton block, absent doubleton, cyclic closure, exact same-row
  comparisons with the known residue-two order and K825, and one independent
  bounded standard-library max-plus/all-arcs diagnostic.

## Scope

- **In scope:** only the fixed map (PGE2ODD-6); the exact induced-subset
  objective on that one core; all literal boundary and closure cases; the two
  named combinatorial comparators on the same subsequence.
- **Out of scope:** construction changes; candidate, subset, matching,
  permutation, path-assignment, or alternative-order search; production or
  test changes; angular or geometric conclusions; global minimizing-order or
  global-optimality claims.

## Verified Facts

- Startup found a clean `main` worktree after reading the repository contract,
  project brief, durable knowledge, current status, prior PGE2ODD dossier, and
  the relevant K825, residue-two, and fixed-core proof precedents.
- The candidate remains exactly (PGE2ODD-6). No path assignment or orientation
  has been changed.
- For every \(m\ge1\), the unique maximizing subset is
  \(B_m=\{4m+3,\ldots,10m+7\}\), with exact score (KPGE2ODD-4).
- All five \(m\bmod5\) branches are regular. There is no residual score or
  argmax correction; \(m=1,2,3\) are the first rows of three regular branches.
- All seven cancellation-gain classes and every compressed shortcut are
  strict. Exact subtraction makes both named comparator scores strictly larger
  on every row.
- The sole diagnostic constructs only (PGE2ODD-6), passes at its declared
  bounds, and imports only the standard library.

## Decisions And Rationale

- Reconstruct the cyclic word directly from (PGE2ODD-1)--(PGE2ODD-6),
  including the retained closing label \(4m+3\).
- Apply the isolated-hole identity (K825-6)--(K825-9) only after auditing all
  seven deletion positions and every compressed-arc length.
- Add exactly one dossier-local script using max-plus aggregation rather than
  subset enumeration and an independent all-arcs cancellation identity.

## Verification

- **Completed:** exact symbolic derivation; four focused independent audits;
  standalone diagnostic; Ruff check and format check; scoped 43-tag source
  audit; full and focused repository tests; checked-artifact verification;
  complete tracked/untracked scope inspection; final whitespace hygiene.
- **Observed result:** the diagnostic passes with its declared counts; the
  source audit reports 43 sequential unique tags and 48 balanced display
  pairs; full pytest reports 283 passed; the focused schema suite reports
  4 passed; and the verifier confirms four certificates, 76 local brackets,
  and \(n=3,4,5,6\).
- **Limitation:** bounded computation corroborates but does not replace the
  exact all-domain proof.

## Blockers / Risks

- No current blocker. The main rigor risks are the true cyclic cut, the
  shifted-triple interval empty exactly at \(m=1,2,3\), the always nonempty
  singleton block, the genuinely absent doubleton, and distinguishing both
  comparator orders from the fixed PGE2ODD core.

## Next Atomic Action

- User review and manual commit decision. Do not begin the proposed next
  research task in this chat.

## Handoff

- **Last verified result:** exact all-\(m\) theorem, strict two-comparator
  result, and passing bounded diagnostic plus repository verification.
- **Files changed:** fixed-order proof, pertinent authoritative summaries,
  current status, and this four-file task dossier; production and tests are
  untouched.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, and this file.
