# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** reduced finite evaluation of the cyclic-ratio objective
  at `n=9`.
- **Current task:** prove \(\Lambda_9=239\) from the accepted core reduction,
  without enlarging the public enumerator.
- **Task dossier:**
  ops/TASK-20260715__lambda9_exact_finite_value/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Finite Exact Result

- EXACT THEOREM (FINITE SIX-LABEL LEMMA): for every cyclic order \(\omega\)
  on \(S_6=\{4,\ldots,9\}\), with \(S_5=\{5,\ldots,9\}\),
  \[
  \max\{P_\omega(S_6),P_\omega(S_5)\}\ge239.
  \]
  The proof uses the exact rearrangement bound
  \(P_\omega(S_5)\ge235\), the effect
  of inserting label `4`, and twelve explicit sums for the only two
  exceptional neighbor pairs.
- VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT): for every core order
  \(\tau\) of \(\{2,\ldots,9\}\), the lemma gives \(K(\tau)\ge239\). The
  exact witness
  \[
  \tau_*=(9,2,3,5,8,6,7,4)
  \]
  has \(K(\tau_*)=239\). The accepted reduction therefore gives
  \[
  \Lambda_9=239.
  \]
- The unique maximizing subset for the displayed witness is
  \(S_6=\{4,5,6,7,8,9\}\), induced as `(9,5,8,6,7,4)` with cyclic sum
  `239`.
- LIMITATION: this is a finite exact combinatorial value. It gives no exact
  value of \(R_2^*(9)\), geometric conclusion, all-`n` formula, asymptotic
  claim, or classification of all minimizing core orders.

## Independent Finite Verification

- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a test-only oracle
  generated all 60 dihedral cyclic classes on \(S_6\) directly, without a
  repository canonicalizer, public enumerator, or production scorer, and
  found
  \[
  \min_\omega\max\{P_\omega(S_6),P_\omega(S_5)\}=239.
  \]
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a separate literal
  audit scored all 255 nonempty subsets of \(\tau_*\), recovered
  \(K(\tau_*)=239\), and found only \(S_6\) at the maximum.
- The focused cycle-ratio module passes all 27 tests.
- The production enumerator remains unchanged and hard-rejects `n=9`; its
  public domain is still `3<=n<=8`.

## Changes

- `research/FIXED_ORDER_CYCLE_RATIO.md` contains the finite lower lemma,
  exact shortcut-gain witness certificate, maximizing-subset record, and
  independent-oracle boundary.
- `tests/test_fixed_order_cycle_ratio.py` contains only test-local direct
  generators and literal integer scorers for the 60-class and 255-subset
  checks.
- The roadmap, current status, and this task dossier are synchronized.
- No production source, public limit, backend, verifier, certificate,
  checked artifact, schema, example, CLI, geometric claim, or all-`n` claim
  changed.

## Verification

- CURRENT LOCAL VERIFIED FACT: the focused cycle-ratio module passes all 27
  tests and the complete repository suite passes all 200 tests on local
  Python 3.14.3.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary; no artifact or
  certification claim changed.
- CURRENT LOCAL VERIFIED FACT: targeted Ruff, Python compilation, independent
  mathematical/test/documentation audits, final diff inspection, and
  whitespace hygiene pass.
- CURRENT HOSTED STATUS: GitHub Actions on Python 3.11-3.13 has not been run
  for this worktree.

## Residual Limitations

- The proof identifies one minimizing core order but does not classify every
  minimizing core order at `n=9`.
- The 60-class oracle is independent finite implementation evidence; the
  displayed finite lemma is the mathematical lower-bound proof.
- Existing interval-backend trust limitations and certified finite geometric
  claims are unchanged.

## Proposed Next Task

In a fresh chat, design a bounded independent interval-backend
cross-verification path for the existing checked artifacts, without generating
a larger finite certificate or changing current certified claims.
