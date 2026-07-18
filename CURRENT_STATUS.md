# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** classify the complete continuous finite-prefix template
  family, including every clipped regime, for arbitrary finite \(k\).
- **Repository state at startup:** clean `main` worktree at commit
  `807d79eca25249b404ce9b3374472e19c67e5adf`, tracking `origin/main`.
- **Implementation state:** the exact full-family theorem, compact Bellman
  envelope, global all-middle proof, authoritative synchronization, sole
  dossier-local exact diagnostic, regressions, independent audits, and final
  source/diff verification are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Determine whether

\[
C_{\mathrm{AF}}={434+4\sqrt2\over1587}
\]

is the supremum of the complete continuous template family with any finite
number of prefixes, rather than only of the all-middle restriction. The task
allows one small independent exact diagnostic and pertinent authoritative
documentation only. Finite rounding, production source, artifacts, schemas,
backends, test modules, certificates, and enumeration limits remain outside
scope.

## Exact Compact Clipped Envelope

For fixed finite \(k\), put \(\beta_0=\alpha\), \(s=1+\alpha\), and let
\(\Phi_s\) be the exact coordinatewise clipped floor. Since its optimizing
weight is nondecreasing in the cutoff, coordinatewise clipping respects the
ordered-weight constraints. Thus

\[
\mathscr H_k(\alpha)
=p(\alpha)+
\max_{0\le\beta_k\le\cdots\le\beta_1\le\alpha}
\sum_{i=1}^k(\beta_{i-1}-\beta_i)\Phi_s(\beta_i).
\]

With \(t=\alpha/(1+\alpha)\) and the normalized increasing clipped floor
\(\phi\), this becomes the compact Bellman envelope

\[
\boxed{
\mathscr H_k(\alpha)=p(\alpha)+(1+\alpha)^3V_k(t),
\qquad
V_m(t)=\max_{0\le x\le t}
\bigl((t-x)\phi(x)+V_{m-1}(x)\bigr),
\quad V_0=0.
}
\]

It covers exactly \((k+1)(k+2)/2\) ordered regimes \(H^hM^m0^z\).

## Exact Global Classification

Every finite Bellman chain is a lower Darboux sum for \(\phi\). The values
increase monotonically and uniformly to its integral, giving

\[
\mathscr H_{\rm fin}(\alpha)
=\sup_{k<\infty}\mathscr H_k(\alpha)
=
\begin{cases}
p(\alpha),&0\le\alpha\le1/3,\\[1mm]
(23\alpha^3-39\alpha^2+21\alpha+3)/24,
 &1/3\le\alpha\le1/2,\\[1mm]
(5\alpha^3-21\alpha^2+15\alpha+17)/72,
 &1/2\le\alpha\le1.
\end{cases}
\]

The regions \([0,1/3]\) and \([1/2,1]\) are strictly below the feasible
one-prefix all-middle optimum. Hence every finite-\(k\) global maximizer lies
in \(1/3<\alpha<1/2\), where high clipping is impossible and

\[
\mathscr H_k(\alpha)
=p(\alpha)+{M_k\over8}(3\alpha-1)^3.
\]

Strict concavity and the normalized-simplex equality classification give the
unique density

\[
\alpha_{k,*}
={27M_k+4-2\sqrt{2(4-9M_k)}\over81M_k-4}
\]

and one strict all-middle tuple (CR28dw25). No high-clipped counterexample
regime exists for any finite \(k\).

## Family Supremum And Charging Relation

The exact fixed-template maxima satisfy

\[
C_{k,*}\nearrow
{434+4\sqrt2\over1587}=C_{\mathrm{AF}},
\qquad
\alpha_{k,*}\longrightarrow{13-2\sqrt2\over23}.
\]

Therefore

\[
\boxed{
\sup_{\substack{k<\infty\\
 (\alpha,\boldsymbol\beta,\boldsymbol\lambda)\in\mathcal D_k}}
C_k(\alpha,\boldsymbol\beta,\boldsymbol\lambda)
=C_{\mathrm{AF}}.
}
\]

The supremum is not attained at finite \(k\). Applying the already-proved
charging theorem separately to the unique optimizer at each fixed \(k\)
recovers the existing bounds

\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{\mathrm{AF}},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{C_{\mathrm{AF}}\over\pi}.
\]

No \(k=k(n)\), common threshold, finite rounding, or interchange of limits is
used. The formal polynomial endpoint \(E_\infty(1)=1/3\) is not a clipped
finite-prefix coefficient.

## Verification

- The new standard-library exact diagnostic passes the clipped formulas,
  rational-grid integral and Bellman checks, twelve exact normalized-simplex
  rows, critical brackets, exact surd comparisons, and the adversarial check
  \(M_7>C_{\mathrm{AF}}\).
- Ruff check and final format check pass for the sole new diagnostic; the
  initial format check correctly requested one mechanical reformat.
- The historical normalized-simplex diagnostic passes 203,489 exact grid
  states, the arbitrary-charging oracle passes 332,640 histories, and the
  global-five diagnostic passes all 21 regimes.
- The full suite passes 283 tests. The checked-artifact verifier passes four
  certificates and 76 local brackets; the schema suite passes four tests.
- Strict UTF-8/LF/final-newline/trailing-whitespace and balanced
  display/fence/environment checks pass for all 10 intended paths; all 395
  primary equation tags are unique.
- Three independent read-only audits confirm the proof, source consistency,
  diagnostic independence, and protected-path scope after four local wording
  and endpoint qualifications were corrected.
- Final `git status`, complete diff inspection, and `git diff --check` pass;
  only the six pertinent authoritative Markdown files and the new four-file
  task dossier are changed.

## Evidence Classification And Limitations

- The compact envelope, all-middle classification, exact maximizers, and
  family supremum are **exact method-specific theorems**.
- The dossier-local script is a **verified bounded exact computation** that
  corroborates but does not replace the all-real proof.
- The result is optimality inside this continuous template family. It is not
  a matching upper bound for the original geometric problem, convergence, an
  exact leading constant, an exact residual, or a finite rounded theorem.
- No production, test, artifact, schema, backend, certificate, or enumeration
  claim changes.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/ALL_N_LOWER_BOUND.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260718__global_finite_prefix_envelope/

## Proposed Next Task

In a fresh STRICT task, derive an exact symbolic count of
relation-compatible, equivalently full-optimal, scaffold bijections from the
nested Ferrers thresholds, without enumerating path permutations.
