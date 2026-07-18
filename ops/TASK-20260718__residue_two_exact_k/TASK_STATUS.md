# TASK_STATUS - TASK-20260718 / Residue-Two Exact K

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine exactly the induced-subset objective \(K\) on the
  cyclic core order returned by `residue_two_product_distance_order(n)` for
  every \(n=5k+2\), \(k\ge2\), classify every maximizing subset, and compare
  the result exactly and asymptotically with the canonical formula (K825-4).
- **Expected output:** an all-\(k\) shortcut-budget proof from the block word,
  an exact parity quasipolynomial, a complete boundary/equality audit, one
  bounded independent standard-library diagnostic, and only the logically
  permitted consequences for \(\Lambda\) and \(R_2^*\).

## Scope

- **In scope:** residue two only; the existing search-free block order;
  shortcut gains and compressed-path margins; all maximizing subsets; parity
  and smallest-\(k\) cases; exact pointwise and asymptotic comparison with the
  canonical eight-twenty-fifths order.
- **Out of scope:** permutation or subset enumeration; production or test
  changes; artifacts, schemas, backends, certificates, or enumeration limits;
  global minimizing-order, exact angular ordering, or exact geometric-optimum
  claims.

## Startup Facts

- The startup worktree was clean on `main` at
  `6edc37325200dec1826173b2506dd0893219b28b`.
- The operating contract, project brief, stable knowledge, current status,
  prior residue-two construction dossier, canonical and residue-one \(K\)
  dossiers, and relevant proof/source/test sections were inspected before
  modification.
- Three independent read-only audits agree on the unique candidate, exact
  formulas, shortcut proof, K825 comparison, and permitted consequences.

## Current Result

- The unique maximizer for every \(k\ge2\) is
  \(S_k=\{2k+1,\ldots,5k+2\}\); neither parity nor the boundary rows
  \(k=2,3,4\) produce a tie or score correction.
- With \(\varepsilon=k\bmod2\),
  \[
  K(\tau_n^{(2)})
  ={286k^3+459k^2+198k+16
   +\varepsilon(-10k^2+40k+27)\over8}.
  \]
- The score is strictly below K825 for every \(k\ge2\), with no crossover.
  Both cubic coefficients are \(143/500\), while
  \(K_{825}-K(\tau_n^{(2)})=21n^2/100+O(n)\).
- The proof deletes exactly the holes \(\{2,\ldots,2k\}\), proves every
  deletion gain and every non-atomic compressed-path margin strictly
  positive, and sums the even and odd block words directly.

## Plan

- Record and independently audit the exact theorem and all-\(k\) proof. DONE.
- Add and run the sole bounded diagnostic. DONE.
- Synchronize only pertinent authoritative sources. DONE.
- Run final repository verification and diff review. DONE.

## Blockers / Risks

- No blocker. The main rigor risks are \(t=\lceil k/2\rceil\), retaining the
  closing label \(2k+1\), arcs with hole endpoints, the empty or terminal
  path ranges at \(k=2,3,4\), the K825 correction \(-25\) at \(k=7\), and
  avoiding geometric or global consequences not licensed by the sandwich.

## Verification Summary

- The sole mathematical diagnostic passes all 29 bounded certificate rows
  and formula/comparison checks through \(k=1000\). Each max-plus DP checks
  4,623,615 transitions, all 238,670 oriented shortcut arcs pass, every row
  has one maximizer, and bounded minimum hole and path margins are
  respectively \(26\) and \(7\).
- Ruff lint/format and `py_compile` pass for the sole diagnostic.
- The full repository suite passes 283 tests; checked-artifact verification
  accepts four certificates and 76 brackets; the focused schema suite passes
  four tests.
- Three independent read-only audits pass after one logical wording fix and
  three editorial clarifications. Strict source structure passes on all ten
  intended paths with 489 unique primary tags and KR2-1 through KR2-36.
- Final Git scope is exactly six tracked Markdown files plus this four-file
  dossier. Complete diff inspection and `git diff --check` pass; production,
  tests, artifacts, schemas, certificates, and caches are unchanged.

## Next Atomic Action

- User manual review and commit decision. Do not begin the proposed Ferrers-
  count task in this chat.
