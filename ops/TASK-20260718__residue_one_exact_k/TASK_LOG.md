# TASK_LOG - TASK-20260718 / Residue-One Exact K

Append-only. Add a new entry to correct previous information.

## 2026-07-18 - Strict startup and independent derivation

- **Action:** completed the repository startup protocol; read the prior
  residue-one construction and canonical K dossiers plus the relevant block,
  scorer, proof, and roadmap sources; commissioned three independent
  read-only derivations.
- **Result:** the worktree is clean and all derivations agree that the unique
  maximizer is the tail from (2k+1), with an exact parity
  quasipolynomial and a strict all-row improvement over K825.
- **Interpretation:** the bounded task can be completed without production or
  test changes, subset enumeration, permutation enumeration, or residue-two.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-scope`.
- **Next step:** write and audit the all-(k) shortcut-budget proof.

## 2026-07-18 - Exact theorem and shortcut-budget proof

- **Action:** decomposed the block word into the retained backbone
  \((L,E_0,P_0,\ldots,E_{k-1},P_{k-1})\), proved every isolated-hole gain
  positive, and proved a strict shortcut margin for every compressed path
  with at least two edges.
- **Result:** for all \(k\ge2\), the sole maximizer is
  \(\{2k+1,\ldots,5k+1\}\), and direct block summation gives the exact
  period-two quasipolynomial recorded in the theorem.
- **Interpretation:** equality in the shortcut budget forces every hole out
  and every backbone label in; the proof classifies all maximizers without
  bounded enumeration. The rows \(k=2,3\), the odd connector at \(n/2\), and
  both parity branches were checked explicitly.
- **Evidence:** `EVIDENCE.md#ev-002---exact-theorem-and-proof`.
- **Next step:** corroborate the theorem with one independent bounded
  standard-library diagnostic.

## 2026-07-18 - Sole bounded diagnostic

- **Action:** added and ran `exact_diagnostic.py`, which independently
  reconstructs the two block orders, applies increasing-path max-plus dynamic
  programming, and audits every oriented residue-one shortcut arc for
  \(2\le k\le30\); formula-only checks continue through \(k=1000\).
- **Result:** PASS. Each DP family checks 4,504,280 transitions, all 234,030
  oriented shortcut arcs pass, every residue-one row has exactly one
  maximizer, minimum bounded hole/path margins are 14/15, and there is no
  K825 crossover.
- **Interpretation:** this is an independent bounded exact computation, not
  an infinite proof. It imports only the Python standard library and
  enumerates neither subsets nor permutations.
- **Evidence:** `EVIDENCE.md#ev-003---sole-bounded-exact-diagnostic`.
- **Next step:** synchronize only the pertinent authoritative research and
  project-memory sources.

## 2026-07-18 - Exact comparison and authoritative synchronization

- **Action:** specialized the canonical K825 formula to \(n=5k+1\), compared
  all explicit and symbolic rows, derived the permitted fixed-order and
  subsequence consequences, and synchronized the theorem into the pertinent
  authoritative sources.
- **Result:** the residue-one score is strictly smaller for every \(k\ge2\),
  with cubic improvement \(1/3000\) and no crossover. Only label-one
  elimination, the fixed-order sandwich, and one-sided global/subsequence
  bounds were propagated.
- **Interpretation:** no residue-two mathematics, exact global optimum,
  global lower bound from this construction, or exact ordering of angular
  thresholds was inferred.
- **Evidence:** `EVIDENCE.md#ev-004---authoritative-synchronization-and-scope`.
- **Next step:** complete repository verification and final diff review.

## 2026-07-18 - Regressions, audits, and ready for review

- **Action:** reran the sole diagnostic; ran the full regression suite,
  checked-artifact verifier, focused schema suite, Ruff, `py_compile`, and
  strict Markdown/equation-tag checks; inspected every tracked diff and all
  four untracked dossier files; ran final Git hygiene checks.
- **Result:** 283 tests pass; four certificates, 76 brackets, and four schema
  tests pass; diagnostic, Ruff, compilation, nine-path source structure, all
  453 unique primary tags, all 32 KR1 tags, full diff inspection, and
  `git diff --check` pass. Three independent audits report no substantive
  finding.
- **Interpretation:** the task is complete and `READY_FOR_REVIEW`. The only
  changed paths are six pertinent authoritative Markdown files and this
  four-file dossier; no production, test, artifact, schema, or residue-two
  implementation was changed.
- **Evidence:** `EVIDENCE.md#ev-005---final-repository-verification`.
- **Next step:** user manual review and commit decision.
