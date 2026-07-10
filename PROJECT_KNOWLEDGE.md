# PROJECT_KNOWLEDGE - power-ringmin

Last reviewed: 2026-07-10

## Project Identity

- VERIFIED FACT: working repository name is `power-ringmin`.
- VERIFIED FACT: project title is Power-Ringmin: Quadratic Radii.
- VERIFIED FACT: author is Maurizio Falconi.
- VERIFIED FACT: repository status is an independent research project, not a Ringmin worktree or branch.
- VERIFIED FACT: the authoritative project brief is `start.md`.

## Mathematical Definitions

- DEFINITION: peripheral radii are \(r_k=k^2\), for \(k=1,\dots,n\).
- DEFINITION: \(R_2^*(n)\) is the minimum feasible central radius for externally tangent peripheral circles with pairwise disjoint interiors.
- DEFINITION: for peripheral radii \(r_i,r_j\) and central radius \(R\),
  \[
  \theta_R(r_i,r_j)
  =
  2\arcsin
  \sqrt{
  \frac{r_i r_j}
  {(R+r_i)(R+r_j)}
  }.
  \]
- DEFINITION: for quadratic radii,
  \[
  \theta_R(i^2,j^2)
  =
  2\arcsin
  \left(
  \frac{ij}
  {\sqrt{(R+i^2)(R+j^2)}}
  \right).
  \]
- CONJECTURE: the principal research target is
  \[
  R_2^*(n)=\frac{n^3}{6\pi}(1+o(1)).
  \]
- UNRESOLVED CLAIM: a possible stronger target is
  \[
  R_2^*(n)=\frac{n^3}{6\pi}+O(n^2).
  \]
- HEURISTIC: in the expected regime \(R\asymp n^3\), \(\theta_R(i^2,j^2)\approx 2ij/R\).
- HEURISTIC: a Supnick-type or alternating chain may suggest a leading adjacent weight of order \(\sum ij\sim n^3/6\).

## Evidence Classification Rules

Every material mathematical or computational claim must be classified where relevant as one of:

- definition;
- verified fact;
- exact theorem;
- computer-certified result;
- numerical observation;
- empirical pattern;
- heuristic;
- conjecture;
- unresolved claim;
- disproved claim.

Rules:

- finite computation is not proof for all `n`;
- a conjecture must not be used as an established lemma;
- conditional arguments must be labeled conditional;
- all-pairs constraints must be checked, not only adjacent pairs;
- numerical precision, parameters, solver, seeds, environment, and code version must be recorded when relevant;
- contradictory evidence must be preserved and investigated.

## Upstream Reference

- VERIFIED FACT: upstream Ringmin local path is `C:\Users\Falker\Desktop\Code\circle\ringmin`.
- VERIFIED FACT: upstream public repository URL is `https://github.com/falker47/ringmin.git`.
- VERIFIED FACT: upstream inspected commit is `cc0327400819fe06b230d967cdcbafffe1648317`.
- VERIFIED FACT: upstream Ringmin studies the original radii \(1,2,\dots,n\), not the quadratic radii problem.
- VERIFIED FACT: upstream Ringmin includes source code, tests, scripts, result artifacts, figures, paper assets, a standalone verifier, and an MIT license file.
- RULE: Ringmin is prior work and a read-only upstream reference.
- RULE: future imports from Ringmin must preserve provenance and relevant license notices.
- RULE: Ringmin mathematical results and observed structural patterns do not automatically transfer to quadratic radii.

See `UPSTREAM_RINGMIN.md` for provenance details.

## Verified Environment Facts

- VERIFIED FACT: repository root during bootstrap is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- VERIFIED FACT: before bootstrap, the only project file in the new repository folder was `AGENTS_GENERIC_TEMPLATE_v2.md`.
- VERIFIED FACT: Git was initialized directly in this folder on branch `main`.
- VERIFIED FACT: no Git remote is configured for this repository as of bootstrap.
- VERIFIED FACT: no Ringmin source code has been imported into this repository.

## Canonical Commands

No build, test, package, or experiment command exists yet for Power-Ringmin because no implementation has been created.

Read-only repository inspection commands used during bootstrap:

- `git status`;
- `git diff`;
- `git diff --check`;
- `git rev-parse --show-toplevel`;
- `git rev-parse --git-common-dir`;
- `git branch --show-current`;
- `git remote -v`.

## Current Established Results

- VERIFIED FACT: no quadratic-radii numerical result has yet been established in this repository.
- VERIFIED FACT: no quadratic-radii theorem has yet been established in this repository.
- VERIFIED FACT: no quadratic-radii implementation, test suite, certificate, or experiment artifact has yet been created in this repository.

