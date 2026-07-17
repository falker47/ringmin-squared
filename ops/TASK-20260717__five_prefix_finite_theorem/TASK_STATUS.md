# TASK STATUS - Five-Prefix Finite Floor/Ceiling Theorem

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** derive the exact finite floor/ceiling theorem for the fixed
  rational five-prefix witness of CR28dx--CR28dz3, without changing
  \(\alpha\), \(x_i\), \(\beta_i\), or \(\lambda_i\).
- **Expected output:** minimal uniform finite threshold, literal
  \(\mathcal B_{5,n}\), integer closure \(\mathcal I_{5,n}\), exact
  remainder relative to \(C_{5,\mathrm{rat}}n^3\), uniform comparison,
  authoritative synchronization, and at most one standalone exact diagnostic.

## Scope

- **In scope:** CR28az, CR28dr--CR28dw, CR28dx--CR28dz3, exact rational
  floor/ceiling arithmetic, fixed-weight finite middle-branch membership,
  one dossier-local exact diagnostic, proof notes, and durable memory.
- **Out of scope:** optimization of the fixed \(k=5\) parameters; changes to
  production code, tests, artifacts, schemas, interval backends, serialized
  certificates, enumeration, or enumeration limits.

## Verified Facts

- Startup used a clean `main` worktree at
  `941d0b6f5a7be00f71552bfd3771a841a7c05782`, tracking `origin/main`.
- The exact finite charging input is CR28dw; integrality is CR12h and the
  pointwise global comparison is CR28ap.
- The original CR28dy weights are retained. They are not replaced by the
  finite reoptimized weights of the three-prefix theorem.
- The minimal uniform threshold is \(234\). At \(233\),
  \((r_n,s_{1,n})=(100,100)\), so the first segment is empty.
- Exact rows \(234\) through \(246\) close the finite bridge; direct
  inequalities cover every \(n\ge247\).
- The literal expression and integer closure are
  \[
  \mathcal B_{5,n}
  =P_{r_n,n}+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})G_{n,\lambda_i}(s_{i,n}),
  \qquad
  \mathcal I_{5,n}=\lceil\mathcal B_{5,n}\rceil.
  \]
- Exact stationarity cancels every ceiling error from the quadratic
  coefficient of \(\mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3\), and
  \[
  \mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
  >{13\over30}n^2-{25\over2}n-{109\over6}>0
  \qquad(n\ge234).
  \]
- Hence
  \[
  \Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
  >C_{5,\mathrm{rat}}n^3
  \qquad(n\ge234).
  \]

## Assumptions / Inferences

- The finite middle condition means
  \((n+r_n)/4<s_{i,n}<(n+r_n)/3\). It classifies each rounded cutoff in the
  middle density branch; it does not make the fixed \(\lambda_i\) equal to a
  finite clipped optimum.
- The exact remainder is the remainder of the literal lower expression, not
  the unknown true residual of the block or of \(\Lambda_n\).

## Decisions And Rationale

- Use one finite bridge for \(234\le n\le246\), followed by a symbolic tail
  from \(247\), so minimality is independently understandable.
- Keep the exact remainder in named floor/ceiling errors; use simplex
  stationarity for the exact quadratic cancellation and rational bounds for
  the uniform sign.
- Add exactly one standalone diagnostic using only `fractions.Fraction`.

## Plan And Expected Delta

- [x] Complete STRICT startup and inspect all authoritative inputs.
- [x] Derive the exact uniform domain and prove minimality.
- [x] Derive \(\mathcal B_{5,n}\), \(\mathcal I_{5,n}\), and the global chain.
- [x] Expand and control the exact rounded remainder.
- [x] Add and run the sole standalone diagnostic.
- [x] Synchronize the primary proof and authoritative research/project notes.
- [x] Run focused/full regressions and mathematical audits.
- [x] Complete the final synchronization/scope, encoding, and diff audit.
- [x] Set the task and project status to `READY_FOR_REVIEW`.

## Verification

- **Checks:** standalone diagnostic; Ruff lint/format; focused and full
  pytest; checked-artifact and schema verification; equation-tag and
  Markdown/LaTeX structure; independent threshold and remainder audits.
- **Observed result:** diagnostic PASS; Ruff PASS after mechanical formatting;
  101 focused and 283 full tests PASS; 4 certificates with 76 local brackets
  and 4 schema tests PASS; 343 equation tags are unique and changed-source
  display/aligned environments balance; all three independent audits PASS;
  exact 10-file scope, encodings, whitespace, protected paths, complete diff,
  and `git diff --check` PASS.
- **Limitations:** hosted GitHub Actions were not inspected.

## Blockers / Risks

- No blocker. The fixed-versus-reoptimized-weight distinction is explicit in
  every authoritative theorem statement.

## Next Atomic Action

- User review and, if accepted, manual commit.

## Handoff

- **Last verified result:** exact theorem, diagnostic, regressions, source
  structure, all three independent audits, and final diff checks pass.
- **Files changed:** six authoritative research/project files and this
  four-file dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` and this
  dossier.
- **Suggested manual commit message:**
  `Add finite five-prefix floor-ceiling theorem`.
