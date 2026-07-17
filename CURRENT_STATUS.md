# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

- **Current phase:** exact local audit of arbitrary whole-path reassignments
  in the product-distance upper construction.
- **Current task:** classify the terminal-gap locations of the distinguished
  path \(P_0\) in the symbolic \(n=10m+3\), \(m\ge3\), branch.
- **Task dossier:**
  ops/TASK-20260717__p0_terminal_gap_classification/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Necessary Placement Result

Write

\[
n=10m+3,
\qquad
d=8m+4,
\qquad
T={d(d-1)\over2},
\qquad
m\ge3.
\]

Keep the terminal/low scaffold, every whole path, and every internal path
orientation fixed, but allow an arbitrary bijection assigning paths to the
\(2m\) terminal gaps. If

\[
P_0=(d-1,4m+2,d-2)
\]

occupies \(G_j\), its seven-label local word is

\[
(E_j,\lambda_j,d-1,4m+2,d-2,\rho_{j^+},E_{j^+}),
\qquad
j^+=j+1\pmod{2m}.
\]

Its exact local maxima are

\[
M^{\rm loc}_1(j)=T,
\qquad
M^{\rm loc}_2(j)=T+{j(d-1)\over2},
\]

with unique maximizing pairs
\(\{d-1,4m+2\}\) and \(\{E_j,d-1\}\). The two terminal
distance-two scores are

\[
L_j=T+{j(d-1)\over2},
\]

and

\[
R_j=
\begin{cases}
T+[j(d-2)-2]/2,&0\le j\le2m-2,\\
T-d/2,&j=2m-1.
\end{cases}
\]

Therefore

\[
L_j\le T\iff j=0,
\qquad
R_j\le T\iff j\in\{0,2m-1\}.
\]

The exact classification is:

- **Excluded:** \(G_1,\ldots,G_{2m-1}\).
- **Locally non-excluded:** only \(G_0\).
- **Necessary global consequence:** every full reassignment with
  \(W^{(\le2)}\le T\), hence every one with \(W\le T\), must fix
  \(P_0\) in \(G_0\).
- **Existence:** not inferred. Placing \(P_0\) in \(G_0\) does not check the
  remaining path assignments. The canonical identity assignment is a
  separate prior witness; no nonidentity completion is constructed or
  asserted.

The cyclic closing word is

\[
(n,2,d-1,4m+2,d-2,4m+1,d).
\]

Its right terminal pair is safe by \(d/2\), but its left pair exceeds
\(T\) by \((2m-1)(d-1)/2\). At \(m=3\), the nonclosing gaps
\(G_1,\ldots,G_4\) each have two strict terminal violations and \(G_5\)
has the closing left violation, so the minimum parameter and every endpoint
are covered.

Because the internal adjacent pair always attains \(T\), any reassignment
with truncated score at most \(T\) has truncated score exactly \(T\); if it
also has full score at most \(T\), then its full score is exactly \(T\).

## Independent Diagnostic

Exactly one new task-local diagnostic uses only the Python standard library
and exact `Fraction` arithmetic. For \(m=3,4,9,25\), it scans only the gap
indices, constructs only the seven-label local word, and checks:

- all displayed distance-one and distance-two inequalities;
- both unique local maxima;
- the separate left and right allowed-index sets;
- the invariant low--terminal--low scaffold pair;
- transition indices, nonclosing endpoint, and literal cyclic closure.

Every row returns the symbolic sets
\(\mathrm{left\_allowed}=\{0\}\),
\(\mathrm{right\_allowed}=\{0,2m-1\}\), and
\(\mathrm{locally\_allowed}=\{0\}\); the printed tuples use the corresponding
numeric closing index in each row. The diagnostic builds no complete order,
assigns no other path, and enumerates no path permutation.

## Protected Scope

- No second complete reassignment was selected, constructed, scored, or
  experimentally probed.
- No path permutation was enumerated.
- No production source, test module, public API, artifact, schema, verifier
  backend, certificate, or limit changed.
- No geometric consequence was added.
- Finite diagnostic rows corroborate but do not prove the all-\(m\) theorem.

## Verification

- Standalone exact local-gap diagnostic: PASS on \(m=3,4,9,25\).
- Python compilation and Ruff lint/format: PASS after one recorded mechanical
  format correction.
- Focused product-distance regression: 49 tests passed.
- Schema-selection regression: 4 tests passed.
- Complete local suite with task-specific temporary directory: 283 tests
  passed.
- Checked-artifact semantic verifier: 4 certificates and 76 local brackets.
- UTF-8 readability, trailing-whitespace, display-math balance, proof-tag
  uniqueness, expected-file scope, and sole-diagnostic checks: PASS.
- Independent read-only diagnostic audit: PASS.
- Independent proof and cross-source audit: PASS after defining the generic
  assignment map explicitly and tightening two statements of notation and
  logical scope.
- Complete status and diff inspection, including final `git diff --check`:
  PASS.

## Files Changed

- research/PRODUCT_DISTANCE_SURROGATE.md: exact necessary placement theorem,
  closure, logical classification, and diagnostic boundary.
- start.md and PROJECT_KNOWLEDGE.md: synchronized stable result and
  limitations.
- research/NEXT_RESEARCH_STEPS.md: completed priority and next atomic task.
- CURRENT_STATUS.md: current repository state.
- ops/TASK-20260717__p0_terminal_gap_classification/: STRICT dossier and
  sole standalone diagnostic.

## Proposed Next Task

In a fresh STRICT task, derive the exact local admissible-gap sets for a
generic remaining path \(P_k\), separating triple and singleton paths, without
choosing a full reassignment or inferring a completion.
