# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** fixed-block method analysis for lower bounds on the exact
  cyclic-ratio objective.
- **Current task:** exact obstruction from three consecutive nested tails,
  including compatible double edge splits and uniform error.
- **Task dossier:**
  ops/TASK-20260715__three_nested_tail_obstruction/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- research/FIXED_ORDER_CYCLE_RATIO.md defines
  \[
  \gamma^*_{m,n}
  =
  \min_\sigma
  \max\{P_\sigma(S_m),P_\sigma(S_{m+1}),P_\sigma(S_{m+2})\}
  \]
  for \(n\ge5\), \(1\le m\le n-4\).
- Deleting \(m\), then \(m+1\), gives a bijection to a simple base cycle
  \(C\) on \(S_{m+2}\), a first split edge \(e\), and a compatible second
  split edge \(f\). With exact corrections \(A,B\),
  \[
  \gamma^*_{m,n}
  =
  \min_{C,e,f}\left[P(C)+\max(0,A,A+B)\right].
  \]
- The second split is exhaustively nested, distinct-incident, or
  distinct-disjoint. Every base, intermediate, and final signature must be a
  connected loopless degree-two spanning cycle with no repeated edge and
  must satisfy the literal split identities.
- Nested splits can tie but are weakly dominated in the minimum, yielding an
  equivalent reduction to two distinct base edges.
- tests/test_fixed_order_cycle_ratio.py adds exact bounded test-local checks
  only. No production source, API, scorer, canonicalizer, or enumeration
  boundary changed.

## Exact Method Result

- EXACT THEOREM: if
  \[
  P^*_{m+2,n}
  =
  \min_{C\text{ simple on }S_{m+2}}P(C),
  \]
  then uniformly
  \[
  0\le\gamma^*_{m,n}-P^*_{m+2,n}<2n^2.
  \]
- EXACT THEOREM: the established pairing floor satisfies the simultaneous
  uniform squeeze
  \[
  P_{m+2,n}\le\gamma^*_{m,n}<P_{m+2,n}+2n^2.
  \]
- EXACT METHOD-SPECIFIC LIMITATION: with
  \[
  \Gamma_n^{(3)}
  =
  \max_{1\le m\le n-4}\gamma^*_{m,n},
  \]
  one has
  \[
  \Gamma_n^{(3)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
  Thus one optimized block of three tails preserves the old cubic
  coefficient. This is not an asymptotic evaluation, upper bound, or
  convergence claim for \(\Lambda_n\), and it gives no exact asymptotic claim
  for \(R_2^*(n)\).
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): at \((m,n)=(2,7)\), 60
  compatible double splits give all 60 outer dihedral cycles, with 24
  nested, 24 distinct-incident, and 12 distinct-disjoint interactions.
  Four bounded rows recover
  \((P_{m+2,n},P^*_{m+2,n},\gamma^*_{m,n})\) exactly.

## Verification

- Focused new-test selection: 3 passed, 37 deselected.
- Complete cyclic-ratio module: 40 passed.
- Induced-subset lower-bound module: 7 passed.
- Complete local suite: 216 passed.
- Checked-artifact verifier: all 4 certificates and 76 local brackets
  verified; schema suite: 4 passed.
- Ruff, independent proof/test/scope audits, Git diff hygiene, and the
  no-src-diff production-boundary check pass.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- research/FIXED_ORDER_CYCLE_RATIO.md adds the authoritative theorem and
  proof.
- tests/test_fixed_order_cycle_ratio.py adds independent exact bounded checks.
- start.md, PROJECT_KNOWLEDGE.md, and
  research/NEXT_RESEARCH_STEPS.md synchronize stable knowledge and the
  research boundary.
- CURRENT_STATUS.md and the STRICT task dossier record durable handoff.

## Residual Limitations

- The theorem concerns exactly one optimized block of three consecutive
  tails; it does not treat a block length growing with \(n\).
- Finite tests verify exact arithmetic, compatibility, and bounded coverage
  only; they are not the all-\(n\) proof.
- No exact leading constant or convergence theorem for \(\Lambda_n/n^3\) or
  \(R_2^*(n)/n^3\) is claimed.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh chat, generalize the compatible-prefix construction from three
tails to a fixed symbolic block of \(r\ge4\) tails and identify the first
growth scale of \(r=r(n)\) not excluded by the resulting error bound, without
changing production enumeration.
