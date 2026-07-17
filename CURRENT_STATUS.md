# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

- **Current phase:** exact symbolic audit of deterministic nonlocal
  middle-path reassignments in the product-distance upper construction.
- **Current task:** classify the fixed one-gap rotation in the symbolic
  \(n=10m+3\), \(m\ge3\), branch.
- **Task dossier:**
  ops/TASK-20260717__nonlocal_middle_path_rotation/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Nonlocal-Rotation Result

Write

\[
n=10m+3,\qquad d=8m+4,\qquad T={d(d-1)\over2},\qquad m\ge3.
\]

Before direct scoring, the sole family was fixed by assigning the complete
oriented middle path \(P_{j+1\bmod 2m}\) to the terminal gap \(G_j\), while
leaving the terminal/low scaffold and every internal path orientation
unchanged. Equivalently, \(P_k\) moves to \(G_{k-1\bmod 2m}\), and \(P_0\)
moves to the canonical closing gap \(G_{2m-1}\).

For every \(m\ge3\), the resulting cyclic order is a permutation. Its exact
distance-class maxima, with unique unordered class maximizers, are

\[
\begin{array}{c|c|c}
q& M_q&\text{unique maximizer}\\ \hline
1&T&\{d-1,4m+2\}\\
2&n(d-1)/2&\{n,d-1\}\\
3&(5m+2)(9m+4)/3&\{5m+2,9m+4\}\\
\ge4&n(n-1)/4&\{n-1,n\}.
\end{array}
\]

Across the canonical cut, the exact maxima are

\[
\begin{aligned}
C_1&=(4m+1)d,&
C_2&={d(d-2)\over2},&
C_3&={d^2\over6},\\
C_4&={d(d-1)\over4},&
C_5&={d^2-4\over10},&
C_6&={dn\over6},
\end{aligned}
\]

and \(C_{\ge4}=T/2\). Every cut-class maximizer is identified in the proof
note.

Consequently,

\[
\boxed{
W(\widehat\sigma_m)
={n(d-1)\over2}
={(10m+3)(8m+3)\over2}
}
\]

is uniquely saturated by \(\{n,d-1\}\) at cyclic distance two. The fixed
rotation forces the local word \(n,2,d-1\) when \(P_0\) wraps into the closing
gap. This is the precise symbolic obstruction: the normalized coefficient is

\[
\lim_{m\to\infty}{W(\widehat\sigma_m)\over n^2}={2\over5}>{8\over25}.
\]

Thus this reassignment does not improve the eight-twenty-fifths construction.

## Independent Diagnostic

Exactly one new task-local diagnostic uses only the Python standard library
and an independent label-position all-pairs scorer. It checks the permutation,
all four distance classes, the canonical-cut classes, every asserted unique
maximizer, the full score, and the sole full saturator on the fixed exact rows
\(m=3,4,9,25\). All rows pass.

## Protected Scope

- No alternative middle-path reassignment was tested or analyzed.
- No cyclic-order enumeration was added or enlarged.
- No production source, public API, artifact, schema, verifier backend,
  certificate, or limit changed.
- No geometric consequence was claimed beyond restating the already proved
  regular-direction upper bound.
- The finite diagnostic is corroboration, not the proof for all \(m\).

## Verification

- Standalone exact all-pairs diagnostic: PASS on \(m=3,4,9,25\).
- Python compilation and Ruff lint/format: PASS.
- Focused product-distance regression: 49 tests passed.
- Complete local suite outside the restricted sandbox: 283 tests passed.
- The retained sandbox attempt had 31 setup errors caused solely by denied
  pytest temporary-directory access; no test body failed in that attempt.
- Checked-artifact semantic verifier: 4 certificates and 76 local brackets.
- Schema-selection regression: 4 tests passed.
- UTF-8, trailing-whitespace, display-math, proof-tag, cross-source
  consistency, protected-scope, sole-diagnostic, complete-diff, and
  git-diff checks: PASS.
- Three independent read-only audits covered the symbolic proof, diagnostic,
  and cross-source consistency. Their actionable range/format findings were
  corrected and rechecked.

## Files Changed

- research/PRODUCT_DISTANCE_SURROGATE.md: complete exact theorem and
  obstruction proof.
- start.md and PROJECT_KNOWLEDGE.md: synchronized stable result and
  limitations.
- research/NEXT_RESEARCH_STEPS.md: completed priority and next atomic task.
- CURRENT_STATUS.md: final repository state.
- ops/TASK-20260717__nonlocal_middle_path_rotation/: STRICT dossier and the
  sole standalone diagnostic.

## Proposed Next Task

In a fresh STRICT task, characterize the admissible terminal-gap positions of
\(P_0\) under arbitrary whole-path reassignments that preserve the scaffold,
internal orientations, and target \(W\le T\), without selecting or testing a
second family.
