# TASK_STATUS - TASK-20260718 / Preclosing PG46 Exact K

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine exactly the induced-subset objective \(K\) for the
  PG46 shift placing \(P_m\) in \(G_{2m-2}\) on \(n=10m+3\), \(m\ge3\),
  and classify every maximizing subset.
- **Expected output:** an all-\(m\) symbolic theorem, exact pointwise and
  asymptotic comparisons with closing PG46 and K825, one bounded independent
  diagnostic, and synchronized authoritative memory without geometric or
  global-optimality inferences.

## Scope

- **In scope:** the prescribed PG46 bijection, its explicit core order,
  induced-cycle subset optimization, isolated-hole and complete shortcut
  proof, cyclic closure, exact block sum, minimum row, all boundary ranges,
  and comparison with the two fixed-order families.
- **Out of scope:** other PG46 bijections, permutation or matching search,
  production code, tests, artifacts, schemas, certificates, geometric
  realizability, angular-threshold ordering, and global minimization.

## Verified Facts

- Startup found a clean main worktree at commit
  113d6f9173213c9ff2363328cec823fb32b2377a, tracking origin/main.
- PG46 specialized to \((m,2m-2)\) gives
  \[
  \alpha_m^{\rm pre}(j)=
  \begin{cases}
  j,&j<m,\\
  j+1,&m\le j<2m-2,\\
  m,&j=2m-2,\\
  2m-1,&j=2m-1.
  \end{cases}
  \]
- The unique maximizing subset is
  \(S_m=\{4m+1,\ldots,10m+3\}\), and
  \[
  K={572m^3+631m^2+235m+22\over2}.
  \]
- The exact minimum hole and shortcut margins are \(28m+12\) and
  \(12m+4\). The changed cyclic three-edge role is explicitly positive.
- Exact comparisons are \(K-K_{\rm cl}=6m\) and
  \(K-K_{825}=m^2-4\); the preclosing order is strictly worse than both for
  every \(m\ge3\), with cubic coefficient \(143/500\).

## Assumptions / Inferences

- None beyond \(m\ge3\) and the previously proved PG46 scaffold definitions,
  relation compatibility, and full \(W\)-optimality.
- Bounded computation is corroborative and is not used as the infinite proof.

## Decisions And Rationale

- Reuse only the general isolated-hole shortcut-budget lemma, not the closing
  witness's terminal inequalities. Seven hole classes and the altered cyclic
  pair \((x_{2m-1},4m+1)\) are audited directly.
- Use one standalone standard-library diagnostic based on increasing-path
  max-plus DP and oriented shortcut arcs, with no production import.
- Record only exact fixed-order \(K\) consequences; infer no angular,
  geometric, or global ordering.

## Plan And Expected Delta

- Reconstruct the exact order and candidate tail. COMPLETE.
- Prove hole positivity, shortcut completeness, cyclic closure, uniqueness,
  block sum, and every boundary. COMPLETE.
- Run the independent diagnostic and exact comparisons. COMPLETE.
- Synchronize authoritative notes and the STRICT dossier. COMPLETE.
- Run regressions, inspect the full diff, and obtain independent audits.
  COMPLETE.
- No production, test, artifact, schema, certificate, or upstream file
  changed.

## Verification

- **Checks:** standalone diagnostic; in-memory compile; Ruff lint/format;
  complete 283-test suite; four schema tests; checked-artifact verification;
  source/tag/LaTeX structure; changed-path and whitespace inspection;
  git diff --check; three independent read-only audits.
- **Observed result:** all final checks pass. The diagnostic covers 28 DP and
  shortcut rows, 36,989,498 DP transitions, 958,916 oriented shortcut arcs,
  and 998 direct formula rows. Pytest reports 283 passed; four schema tests
  pass; four certificates and 76 local brackets verify.
- **Limitations:** no hosted CI, geometry, angular threshold computation, or
  global-order search is in scope.

## Blockers / Risks

- No blocker or known residual defect. User review and commit remain manual.
- Residual risk is ordinary human review of a symbolic proof; the bounded DP
  corroborates but cannot replace the all-\(m\) argument.

## Next Atomic Action

- User manual review and commit decision.

## Handoff

- **Last verified result:** exact order, sole maximizing tail, cubic formula,
  every hole/shortcut/closure boundary, comparisons, diagnostic, regressions,
  source structure, and independent reviews pass.
- **Files changed:** six authoritative Markdown sources and this four-file
  dossier; no production, test, artifact, schema, or certificate path.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md, then this
  dossier's EVIDENCE.md.
