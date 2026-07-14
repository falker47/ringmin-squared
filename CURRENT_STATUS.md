# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** symbolic all-\(n\) lower obstruction for the unresolved
  residue-two product-distance surrogate.
- **Current task:** prove a new saturation obstruction for
  \(n\equiv2\pmod5\), without a matching upper construction or geometric
  claim.
- **Task dossier:**
  `ops/TASK-20260714__residue_two_saturation_obstruction/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Residue-Two Saturation Obstruction

Let

\[
n=5k+2,
\qquad
d=d_n=4k+4,
\qquad
J_n={d(d-2)\over2}.
\]

EXACT THEOREM: for \(k\ge3\),

\[
\boxed{B_n\ge J_n}.
\]

The proof starts from the existing exact lower obstruction

\[
H_n={(d-1)(d-2)\over2}
\]

and excludes every exact threshold \(H_n\le T<J_n\). In that interval,
strict threshold arithmetic gives

\[
b_T=d-1,
\qquad
V_T=\{d-1,\dots,n\},
\qquad
v=k.
\]

The usable lows are exactly \(2,\dots,2k+1\), so their number is
\(2k=2v\) and the terminal-high incidence injection is saturated. After
deleting the terminal highs, the component containing \(x=d-2\) must be
low--\(x\)--low because

\[
x{d\over2}=J_n>T.
\]

The two terminal extensions are at distinct positions \(p(x)-2\) and
\(p(x)+2\) in a cycle of length \(n-1>4\). The distance-two constraint would
force both labels to equal \(d-1\), contradicting that the order is a
permutation.

The exceptional case uses separate exact arithmetic:

\[
H_{12}=56<J_{12}=60,
\qquad
\boxed{B_{12}\ge60}.
\]

Here the saturated lows are \(\{2,3,4,5\}\), the terminal highs are
\(\{11,12\}\), and \(x=10\) cannot neighbor the intermediate block because
\(10\cdot6=60>T\). Both distinct distance-two terminals would have to be
\(11\).

## Consequence For W And Bound Widths

Since \(B_n\le W_n\), the same lower bound transfers immediately. Combining
it with the existing uniform construction gives

\[
J_n\le B_n\le W_n\le T_n={d_n(d_n-1)\over2}.
\]

For \(n=5k+2\), \(k\ge3\), the width between the proved endpoints is

\[
T_n-J_n={d_n\over2}=2k+2={2n+6\over5}.
\]

At \(n=12\),

\[
56=H_{12}<60=J_{12}\le B_{12}\le W_{12}\le T_{12}=66,
\]

so the proved-bound width is \(6\). These widths are not optimality gaps;
neither \(B_n=J_n\), \(W_n=J_n\), nor \(B_n=W_n\) is asserted.

## Exact Support And Verification

- CURRENT LOCAL VERIFIED FACT: three independent read-only audits agree on
  the strict inequalities, floors, cardinalities, residual component, distinct
  terminal positions, separate `n=12` arithmetic, and width consequences.
- CURRENT LOCAL VERIFIED FACT: the four targeted residue-two test items, all
  35 focused product-distance tests, 50 integrated tests, and the full 163-test
  suite pass; the full suite required an unsandboxed rerun for temporary-path
  access.
- RETAINED FAILED CHECK: the first focused run had three test-body harness
  failures when entering the threshold scan because `range` received integral
  `Fraction` endpoints. Preliminary formula assertions ran, but no
  per-threshold assertion ran in those rows; converting the already integral
  doubled endpoints to integer numerators fixed the test harness.
- CURRENT LOCAL VERIFIED FACT: independent tests inspect every half-integer
  threshold in `[H_n,J_n)` for `n=12,17,22`, check the strict boundary
  `T=J_n`, and falsify the symbolic endpoint arithmetic for every
  `2<=k<=1000`.
- RETAINED FAILED CHECK: sandboxed full pytest reported `132 passed, 31
  errors`, all from denied temporary-directory creation. The identical
  unsandboxed suite passed `163/163`.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: the changed test module compiles; Ruff with the sole
  pre-existing `F841` ignored passes. Unmodified Ruff reports only the
  unchanged unused variable at test line 566, confirmed in `HEAD`.
- CURRENT LOCAL VERIFIED FACT: all three final independent audits pass; all 9
  intended paths pass strict UTF-8 and trailing-whitespace checks; the proof
  has 130 unique equation tags and 243 balanced display pairs; complete diff
  inspection and `git diff --check` pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current worktree has not been
  independently verified.

## Residual Limitations

- Exact values of \(B_n\) and \(W_n\) beyond the bounded table remain open
  only in residue class two.
- The new theorem is a lower obstruction only; no matching residue-two order
  was sought in this task.
- Structural classifications of optimal orders remain open in every class.
- The first index, if any, where distances at least three change \(W_n\)
  remains open.
- Canonical cyclic-order enumeration remains bounded to `n=3..11`; the new
  larger-range checks evaluate formulas and threshold data only.
- No geometric claim follows from this task.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.
