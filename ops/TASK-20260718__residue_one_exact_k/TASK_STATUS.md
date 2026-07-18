# TASK_STATUS - TASK-20260718 / Residue-One Exact K

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine exactly the induced-subset objective \(K\) on the
  cyclic core order returned by `residue_one_product_distance_order(n)` for
  every \(n=5k+1\), \(k\ge2\), classify every maximizing subset, and compare
  the result exactly with the canonical formula (K825-4).
- **Expected output:** an all-\(k\) shortcut-budget proof from the block word,
  an exact parity quasipolynomial, a complete boundary/equality audit, one
  bounded independent standard-library diagnostic, and only the logically
  permitted consequences for \(\Lambda\) and \(R_2^*\).

## Scope

- **In scope:** residue one only; the existing search-free block order;
  shortcut gains and compressed-path margins; all maximizing subsets; parity
  and smallest-\(k\) cases; exact pointwise and asymptotic comparison with the
  canonical eight-twenty-fifths order.
- **Out of scope:** residue two; permutation or subset enumeration; production
  or test changes; artifacts, schemas, backends, certificates, or enumeration
  limits; global minimizing-order or exact geometric-optimum claims.

## Startup Facts

- The startup worktree was clean on `main` at
  `aca4a7b3544fa015b21774be2413296321f47ed3`.
- The required operating contract, project brief, stable knowledge, current
  status, prior residue-one construction dossier, canonical K dossier, and
  relevant proof/source/test sections were read before modification.
- Three independent read-only derivations agree on the candidate, exact
  formula, shortcut proof architecture, K825 comparison, and permitted
  consequences.

## Current Result

- The unique maximizer for every \(k\ge2\) is
  \(S_k=\{2k+1,\ldots,5k+1\}\); parity and the boundary rows \(k=2,3\)
  produce no tie or exceptional argmax.
- With \(\varepsilon=k\bmod2\), the exact value is
  \[
  K(\tau_n^{(1)})=
  {857k^3+891k^2+214k
   +\varepsilon(27k^2-51k-18)\over24}.
  \]
  This is a period-two quasipolynomial in \(k\), hence period ten in \(n\),
  with cubic coefficient \(857/3000\).
- The exact comparison is strictly better than K825 on every row \(k\ge2\);
  no crossover occurs, and the asymptotic gap is
  \(n^3/3000+O(n^2)\).
- The all-\(k\) proof uses positive isolated-hole gains and strict compressed
  shortcut margins. Three independent read-only audits found no mathematical,
  computational, or scope defect after two editorial clarifications.

## Plan

- Record and independently audit the exact theorem and all-\(k\) proof. DONE.
- Add, run, and independently audit the sole bounded diagnostic. DONE.
- Synchronize only pertinent authoritative sources. DONE.
- Run final repository verification and diff review. DONE.

## Blockers / Risks

- No blocker. The main rigor risks are the retained closing label (2k+1),
  the empty small-(k) path ranges, the exact (k=6) K825 boundary
  correction, and avoiding globalization of a residue-one-only upper bound.

## Verification Summary

- The sole mathematical diagnostic passes all 29 bounded certificate rows
  and the formula/comparison tail through \(k=1000\).
- The full repository suite passes 283 tests; checked artifacts and the four
  focused schema tests pass.
- Ruff, `py_compile`, strict Markdown/source structure, all 453 primary
  equation tags, all 32 KR1 tags, complete diff inspection, and
  `git diff --check` pass.
- Final Git scope is exactly six pertinent tracked Markdown files plus the
  four-file dossier. No production or test path changed.

## Next Atomic Action

- User manual review and commit decision. Do not begin the proposed
  residue-two task in this chat.
