# TASK_STATUS - TASK-20260717__p0_terminal_gap_classification / P0 Terminal-Gap Classification

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** characterize the possible terminal-gap locations of the
  distinguished oriented path \(P_0=(d-1,4m+2,d-2)\) under arbitrary
  whole-path reassignments in the symbolic \(n=10m+3\), \(m\ge3\), scaffold.
- **Expected output:** an exact necessary local placement theorem, complete
  cyclic and boundary treatment, an independent gap-index diagnostic, and
  synchronized durable project state.

## Scope

- **In scope:** the fixed terminal/low scaffold, the existing path definitions
  and orientations, the threshold \(T=d(d-1)/2\), and every distance-one and
  distance-two pair determined by placing \(P_0\) in one terminal gap.
- **Out of scope:** selecting, constructing, scoring, or enumerating a second
  complete reassignment family; enumerating path permutations; inferring a
  nonidentity completion; changing production code, tests, public APIs,
  artifacts, schemas, interval backends, certificates, or limits.

## Verified Facts

- If \(P_0\) occupies \(G_j\), the seven-label local word is
  \[
  (E_j,\lambda_j,d-1,4m+2,d-2,\rho_{j^+},E_{j^+}),
  \qquad j^+=j+1\pmod{2m}.
  \]
- Its unique local maxima are
  \[
  M^{\rm loc}_1(j)=T,
  \qquad
  M^{\rm loc}_2(j)=T+{j(d-1)\over2}.
  \]
- The right terminal distance-two score is
  \[
  R_j=
  \begin{cases}
  T+[j(d-2)-2]/2,&0\le j\le2m-2,\\
  T-d/2,&j=2m-1.
  \end{cases}
  \]
  Thus the right side permits \(j=0\) and the closing index, while the left
  side permits only \(j=0\).
- **Excluded:** \(G_1,\ldots,G_{2m-1}\).
- **Locally non-excluded:** only \(G_0\).
- **Existence distinction:** local non-exclusion does not prove that a
  prescribed assignment of the remaining paths has a valid completion. The
  canonical identity assignment is a separate prior witness; no nonidentity
  completion is established here.
- The internal edge \((d-1)(4m+2)=T\) implies that every reassignment with
  \(W^{(\le2)}\le T\) has \(W^{(\le2)}=T\), and every reassignment with
  \(W\le T\) has \(W=T\). Merely placing \(P_0\) in \(G_0\) does not bound
  the truncated score contributed by the remaining paths.
- The minimum row \(m=3\), the nonclosing endpoint \(j=2m-2\), the transition
  indices \(m-1,m,m+1\), and the cyclic closing index \(2m-1\) are explicit.
- The standalone diagnostic passes for \(m=3,4,9,25\) and scans no object
  larger than the gap-index set and its constant-size local word.

## Assumptions / Inferences

- None beyond the retained definitions and domain. The symbolic theorem is
  exact for every \(m\ge3\); the four diagnostic rows are corroboration only.

## Decisions And Rationale

- Introduce a generic gap-to-path bijection only to state the conditional
  theorem; do not choose its values away from the unique location of \(P_0\).
- Separate the two terminal distance-two inequalities so that the cyclic
  closing exception on the right cannot hide the left obstruction.
- Use a standard-library `Fraction` diagnostic that reconstructs no full
  order and cannot select a reassignment from observed scores.

## Plan And Expected Delta

- Complete STRICT startup and inspect the accepted scaffold. COMPLETE.
- Derive and independently audit the exact local theorem. COMPLETE.
- Add and run the gap-index-only exact diagnostic. COMPLETE.
- Synchronize proof note, stable memory, state, roadmap, and dossier. COMPLETE.
- Complete repository verification and diff inspection. COMPLETE.

## Verification

- **Checks completed:** diagnostic, Python compilation, Ruff lint/format,
  focused surrogate regression, complete test suite, schema-selection
  regression, checked-artifact semantic verifier, documentation hygiene,
  protected-scope inspection, independent proof and code audits, complete
  diff inspection, and final `git diff --check`.
- **Observed result:** diagnostic PASS on \(m=3,4,9,25\); Ruff and compilation
  PASS; 49 focused tests, 4 schema tests, and all 283 repository tests PASS;
  4 certificates and 76 local brackets verify; hygiene, scope, audit, and
  final diff checks PASS.
- **Retained failed check:** the first Ruff format check reported that the new
  diagnostic would be reformatted. Ruff formatting was applied, after which
  lint and format checks passed.
- **Retained harness corrections:** an initial PowerShell hygiene command had
  a variable-interpolation parse error, and its corrected successor
  overcounted a LaTeX row-break command as a display opener. A trimmed-line
  display check replaced that faulty heuristic and passed on every changed
  Markdown file. A final direct `ruff` invocation also found no executable on
  this shell's `PATH`; the equivalent `python -m ruff` lint and format checks
  both passed.
- **Limitations:** finite diagnostic rows do not prove the all-\(m\) theorem,
  and no check analyzes the remaining path reassignment.

## Blockers / Risks

- No blocker.
- Residual uncertainty is intentional: the theorem is local and necessary;
  it neither classifies the remaining paths nor proves a nonidentity
  completion.

## Next Atomic Action

- User review of the exact theorem, diagnostic, and synchronized documentation,
  followed by a manual commit decision.

## Handoff

- **Last verified result:** only \(G_0\) is locally non-excluded for \(P_0\);
  every target full reassignment must fix \(P_0\) there.
- **Files changed:** proof note, project brief, stable memory, current status,
  roadmap, and this dedicated STRICT dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md,
  CURRENT_STATUS.md, and this file.
- **Handoff state:** READY_FOR_REVIEW; Codex performed no staging, commit,
  push, merge, rebase, reset, or history edit.
