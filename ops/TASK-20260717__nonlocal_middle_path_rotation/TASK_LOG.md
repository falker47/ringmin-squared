# TASK_LOG - TASK-20260717__nonlocal_middle_path_rotation / Nonlocal Middle-Path Rotation

Append-only. Add a new entry to correct previous information.

## 2026-07-17 - Startup And A-Priori Family Selection

- **Action:** Read the required project state and the accepted symbolic
  eight-twenty-fifths construction, confirmed a clean Git worktree, and fixed
  one transformation before running any new direct-scoring experiment.
- **Result:** The sole task family is `G_j <- P_(j+1 mod 2*m)` for
  `n=10*m+3`, `m>=3`, with terminal/low labels and all internal path
  orientations unchanged. Thus every middle path rotates one gap toward the
  lower gap index and `P_0` moves to the canonical closing gap.
- **Interpretation:** This is a deterministic nonlocal reassignment with no
  searched parameter. No other path permutation will be probed or analyzed in
  this task.
- **Evidence:** `EVIDENCE.md#ev-001---startup-and-a-priori-family-selection`
- **Next step:** derive the exact all-distance score symbolically.

## 2026-07-17 - Exact Proof And Independent Corroboration

- **Action:** Proved the permutation property and exact maxima at distances
  one, two, three, at least four, and across the canonical cut; identified
  every class maximizer and the sole full-score saturator; added and ran one
  standalone standard-library all-pairs diagnostic on the fixed rows
  \(m=3,4,9,25\); obtained three independent read-only audits and corrected
  the stated range of one monotonicity difference.
- **Result:** For every \(m\ge3\),
  \(W(\widehat\sigma_m)=n(d-1)/2\), uniquely saturated by
  \(\{n,d-1\}\) at distance two. The word \(n,2,d-1\) forced by the wrap of
  \(P_0\) is the exact obstruction, and the normalized coefficient is
  \(2/5>8/25\). The diagnostic passes every asserted formula and unique
  maximizer on all four fixed rows.
- **Interpretation:** This is an exact family-specific obstruction backed by
  bounded independent corroboration. It is not a geometric lower bound and
  does not classify another reassignment.
- **Evidence:**
  EVIDENCE.md#ev-002---exact-proof-and-independent-all-pairs-corroboration
- **Next step:** synchronize durable memory and run complete verification.

## 2026-07-17 - Final Verification And Handoff

- **Action:** Synchronized the authoritative proof note, startup summary,
  stable knowledge, current status, roadmap, and STRICT dossier; ran the
  task-local diagnostic and static checks, focused and complete regressions,
  artifact/schema verification, structural and protected-scope checks, and
  complete diff inspection.
- **Result:** The diagnostic passes on \(m=3,4,9,25\); Ruff and compilation
  pass; 49 focused tests and all 283 repository tests pass; 4 certificates
  and 76 local brackets verify; 4 schema tests pass; the nine changed/new
  files are strict UTF-8 with no trailing whitespace or unbalanced display
  math; all 42 proof labels occur; exactly one task diagnostic exists; no
  protected production, API, schema, test, artifact, or limit path changed;
  and `git diff --check` passes. A retained first full-suite attempt had 31
  sandbox temporary-directory setup errors, resolved by the successful
  unrestricted rerun.
- **Interpretation:** The bounded task is complete and READY_FOR_REVIEW. The
  exact all-\(m\) theorem is separated from its four-row finite corroboration.
- **Evidence:**
  EVIDENCE.md#ev-003---final-repository-verification-and-synchronized-handoff
- **Next step:** user review and manual commit decision.
