# TASK_STATUS - TASK-20260721 / Canonical Odd-v E5 Exact K

Last update: 2026-07-21

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove support and evaluate the induced-subset objective
  \(K\) for the one prescribed canonical odd-\(v\), \(e=5\) map on
  \(n=10m+9\), \(m\ge1\), including every maximizing subset, the genuine
  minimum row, strict K825 comparison, coefficient, and only valid
  fixed-order/global consequences.
- **Expected output:** one exact proof section, synchronized durable memory,
  roadmap and status, this task dossier, and one independent bounded
  standard-library max-plus/all-arcs diagnostic.

## Scope

- **In scope:** only the map fixed in (KRPGE5ODD-1) on the already proved
  PGE5ODD scaffold; its support, literal cyclic core, induced \(K\), complete
  induced-subset argmax, K825 comparison, label-one elimination, fixed-order
  angular enclosure, and one-sided subsequential global upper consequences.
- **Out of scope:** changing or optimizing the map; searching assignments,
  subsets, matchings, permanents, or alternative order families; production,
  public-test, schema, artifact, workflow, or upstream changes; global
  minimizing-order, global lower-bound, all-\(n\) limsup, convergence, or
  exact geometric-optimality claims.

## Verified Facts

- Startup found clean `main` at the accepted PGE5ODD support baseline and no
  unrelated working-tree changes.
- The four image blocks of (KRPGE5ODD-1) partition every path index, every
  assigned incidence lies in (PGE5ODD-21), and therefore the map is supported
  with \(W=W_n\).
- The complete induced-subset argmax is uniquely \(\{8,\ldots,19\}\) at
  \(m=1\), and uniquely \(\{4m+3,\ldots,10m+9\}\) for \(m\ge2\).
- At \(m=1\), the stable tail containing \(7\) has score \(2164\), but
  deleting \(7\) gains \(11\), giving the exact optimum \(2175\).
- For \(m\ge2\), the requested polynomial is exact. Canonical K825 is
  strictly larger on every row, with gap \(11\) at \(m=1\), and the fixed
  family has coefficient \(857/3000\).
- The sole diagnostic passes at its declared bounds and checks the three
  sharp shortcut regimes \(m=1\), \(m=2\), and \(m\ge3\).

## Assumptions / Inferences

- No numerical approximation of \(\pi\) is used. Angular and geometric
  statements invoke only the already proved exact CR12p, CR22, CR27, and
  CR28a implications.
- Finite diagnostic coverage corroborates but does not prove the all-domain
  theorem; all-\(m\) validity comes from the symbolic proof.

## Decisions And Rationale

- Treat \(m=1\) as a genuine structural branch instead of extending the
  stable-backbone polynomial incorrectly.
- Audit every deletion class and every compressed shortcut class before
  using the isolated-hole lemma; include the true cyclic closing word.
- Use one dossier-local script only, with candidate-free max-plus aggregation
  and a separate traversal of every proper oriented arc on bounded rows.
- Record only \(\Lambda=K\) for completions of this core, their fixed-order
  enclosure, and the one-sided global upper consequences allowed by the
  general theorems.

## Plan And Expected Delta

- Completed the exact proof, stable summaries, and one independent bounded
  diagnostic without changing production, tests, schemas, or artifacts.
- Completed task-local static checks, repository verification,
  source/tag/link/scope audits, three independent read-only reviews, and final
  Git diff hygiene.

## Verification

- **Checks completed:** standalone diagnostic at full declared bounds; Ruff
  check and format check; 40-tag/display/environment/control-character source
  audit; full and focused pytest; checked-artifact verifier; cross-file link,
  scope, and final Git diff/whitespace audits; three independent read-only
  reviews.
- **Observed result:** diagnostic PASS through 39,970,045 max-plus
  transitions, 1,016,930 proper oriented arcs, 1,891 hole gains, 1,010,149
  nontrivial shortcuts, and 1,000 support/formula rows; Ruff PASS; 283 full
  tests, 4 schema tests, and 3 Arb cross-check tests pass; four certificates,
  76 local brackets, and summary rows \(n=3,4,5,6\) verify; all source,
  scope, link, and diff checks pass.
- **Limitations:** bounded computation does not replace the symbolic proof or
  independently validate the real-arithmetic angular theorems. Verification
  is local on Python 3.14.3, not hosted CI.

## Blockers / Risks

- No current blocker. Main rigor risks are the \(m=1\) optimizer change, the
  true closing column, empty singleton range, absent doubleton, K825 boundary
  correction, and avoiding transfer of the fixed-order lower enclosure to
  the global optimum.

## Next Atomic Action

- User review and manual commit decision. Do not begin the next research task
  in this chat.

## Handoff

- **Last verified result:** exact all-domain theorem, strict K825 comparison,
  bounded diagnostic, full repository verification, and clean final diff.
- **Files changed:** fixed-order proof, compact durable memory, roadmap,
  current status, and this four-file dossier only.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, and this file.
