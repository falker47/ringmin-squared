# TASK_LOG - TASK-20260718 / Residue-Two Exact K

Append-only. Add a new entry to correct previous information.

## 2026-07-18 - Strict startup and independent derivation

- **Action:** completed the repository startup protocol; inspected the
  residue-two construction, canonical and residue-one \(K\) proofs, scorer
  semantics, tests, roadmap, and predecessor dossiers; commissioned three
  independent read-only audits.
- **Result:** the worktree was clean and every derivation found the same sole
  candidate \(\{2k+1,\ldots,5k+2\}\), parity formula, shortcut architecture,
  and K825 comparison.
- **Interpretation:** the task can be completed without production or test
  changes, subset enumeration, cyclic-order enumeration, or artifact changes.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-scope`.
- **Next step:** complete the symbolic all-\(k\) proof.

## 2026-07-18 - Exact theorem and shortcut-budget proof

- **Action:** deleted the isolated holes \(\{2,\ldots,2k\}\) while retaining
  the closing label \(2k+1\), proved every hole gain positive, and classified
  compressed paths with two, three, and at least four edges, including hole
  endpoints.
- **Result:** every shortcut inequality is strict; equality in the budget
  forces the sole subset \(\{2k+1,\ldots,5k+2\}\). Direct parity-specific
  block sums give the exact quasipolynomial without a boundary correction.
- **Interpretation:** \(k=2\) has a final doubleton, \(k=3\) has no nonfinal
  odd singleton, and \(k=4\) has no nonfinal even singleton. None changes the
  argmax or formula.
- **Evidence:** `EVIDENCE.md#ev-002---exact-theorem-and-proof`.
- **Next step:** corroborate the theorem with the sole bounded diagnostic.

## 2026-07-18 - Sole bounded diagnostic

- **Action:** added and ran `exact_diagnostic.py`, which independently
  reconstructs both block orders, applies increasing-path max-plus dynamic
  programming, and audits every oriented residue-two shortcut arc for
  \(2\le k\le30\); direct formula and comparison checks continue through
  \(k=1000\).
- **Result:** PASS. Both DPs check 4,623,615 transitions, all 238,670 arcs
  pass, every row has the predicted sole argmax, bounded minimum hole/path
  margins are respectively \(26\) and \(7\), and there is no K825 crossover.
- **Interpretation:** this is a bounded exact computation using only the
  standard library. It enumerates neither subsets nor cyclic orders and does
  not replace the infinite symbolic proof.
- **Evidence:** `EVIDENCE.md#ev-003---sole-bounded-exact-diagnostic`.
- **Next step:** synchronize the exact comparison and only the authorized
  consequences into pertinent authoritative sources.

## 2026-07-18 - Exact comparison and authoritative synchronization

- **Action:** specialized K825 to \(e=8\), \(v=k-1\), including the \(-25\)
  correction at \(k=7\); compared every explicit and symbolic row; propagated
  only label-one elimination and fixed-order sandwich consequences.
- **Result:** all K825 gaps are positive, with no crossover. The two families
  share cubic coefficient \(143/500\), and the gap is
  \(21n^2/100+O(n)\). The primary proof and cross-references are being
  synchronized without production, test, or artifact changes.
- **Interpretation:** the result orders the exact \(\Lambda\) scores after
  insertion but not the exact angular thresholds; it provides no global
  equality, minimizing-order classification, or cubic coefficient
  improvement.
- **Evidence:** `EVIDENCE.md#ev-004---authoritative-synchronization-and-scope`.
- **Next step:** finish synchronization and run complete verification.

## 2026-07-18 - Regressions, audits, and ready for review

- **Action:** reran the sole diagnostic in normal and isolated Python modes;
  ran the full regression suite, checked-artifact verifier, focused schema
  suite, Ruff, `py_compile`, and strict source/equation-tag checks; inspected
  every tracked diff and all four dossier files; ran final Git hygiene checks.
- **Result:** 283 tests pass; four certificates, 76 brackets, and four schema
  tests pass; the diagnostic, isolated execution, Ruff, compilation, ten-path
  source structure, all 489 unique primary tags, all 36 KR2 tags, full diff
  inspection, and `git diff --check` pass. Three independent audits report no
  remaining substantive or editorial finding.
- **Interpretation:** the task is complete and `READY_FOR_REVIEW`. The only
  changed paths are six pertinent authoritative Markdown files and this
  four-file dossier; no production, test, artifact, schema, certificate, or
  cache path changed.
- **Evidence:** `EVIDENCE.md#ev-005---final-repository-verification`.
- **Next step:** user manual review and commit decision.
