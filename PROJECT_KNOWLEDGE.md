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
- VERIFIED FACT: the 2026-07-10 import audit found that upstream `geometry.py`, `evaluator.py`, `highprec.py`, and parts of `patterns.py` are primarily radius-value based and are the safest code foundation to import/adapt first.
- VERIFIED FACT: the 2026-07-10 import audit found original-radii assumptions in upstream search wrappers, lower-bound components, verifier/result paths, unconstrained SLSQP helper, scripts, result artifacts, and paper/report assets.
- RECOMMENDATION: import the Ringmin geometric/STN foundation before importing the certified-search pipeline; keep original Ringmin results as reference-only unless a later task explicitly creates a provenance-labeled reference area.

See `UPSTREAM_RINGMIN.md` for provenance details.

## Computational Foundation

- VERIFIED FACT: the Python package import name is `power_ringmin`.
- VERIFIED FACT: the initial package metadata is in `pyproject.toml`; package source is under `src/power_ringmin/`; tests are under `tests/`.
- VERIFIED FACT: substantial imported/adapted code is licensed under MIT and records upstream Ringmin commit `cc0327400819fe06b230d967cdcbafffe1648317` in module docstrings.
- VERIFIED FACT: `src/power_ringmin/geometry.py` provides positive-radius validation, `quadratic_radii(n)`, `theta(R,a,b)`, cyclic adjacent pairs, and cycle-equivalence helpers.
- VERIFIED FACT: `src/power_ringmin/evaluator.py` provides a float64 fixed-order evaluator using all-pairs STN feasibility, scale-aware radius bracketing, recovered positions, Cartesian validation, essential tight-pair detection, and floating-radius detection.
- VERIFIED FACT: `src/power_ringmin/highprec.py` provides an independent mpmath fixed-order feasibility verifier, high-precision full-radius bisection, position recovery, and pair slack checks.
- VERIFIED FACT: `src/power_ringmin/patterns.py` provides selected generic order constructors: sequential, zigzag, interleave, Supnick maximum-tour form, Supnick minimum-tour form, and JSON order loading.
- VERIFIED FACT: `src/power_ringmin/crosscheck.py` provides a radius-sequence-aware fixed-order SLSQP cross-check using all-pairs Cartesian non-overlap constraints and explicit fixed-order angle variables.
- VERIFIED FACT: the upstream unconstrained global SLSQP helper was not imported because it hardcodes the original radii `1,\dots,n` and belongs with a later radius-sequence-aware search design.
- VERIFIED FACT: root `verify.py` is a standalone high-precision fixed-order verifier scaffold that imports only the Python standard library and `mpmath`; it accepts explicit order/radius inputs or minimal JSON payloads and can check optional witness positions and local radius brackets.
- VERIFIED FACT: as of the fixed-order crosscheck import, the certified-search pipeline, frontier verifier, result artifact schema, package CLI, plots, and original Ringmin result artifacts have not been imported.
- VERIFIED FACT: `pyproject.toml` defines optional `crosscheck` dependencies for NumPy/SciPy; `requirements.txt` includes NumPy/SciPy for the local development/test environment.
- VERIFIED FACT: `python -m pytest` passed 5 adapted quadratic smoke tests on 2026-07-10.
- VERIFIED FACT: `python -m pytest` passed 8 tests after the fixed-order crosscheck import on 2026-07-10.
- INTERPRETATION: passing finite smoke tests verifies the imported implementation behavior on tested cases only; it is not a theorem about all quadratic-radii instances.

## Verified Environment Facts

- VERIFIED FACT: repository root during bootstrap is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- VERIFIED FACT: before bootstrap, the only project file in the new repository folder was `AGENTS_GENERIC_TEMPLATE_v2.md`.
- VERIFIED FACT: Git was initialized directly in this folder on branch `main`.
- VERIFIED FACT: no Git remote is configured for this repository as of bootstrap.
- VERIFIED FACT: Python reported version `3.14.3` during the 2026-07-10 foundation import.
- VERIFIED FACT: mpmath reported version `1.3.0` during the 2026-07-10 foundation import.
- VERIFIED FACT: during the 2026-07-10 fixed-order crosscheck import, NumPy reported version `2.4.3`, SciPy reported version `1.17.1`, and mpmath reported version `1.3.0`.

## Canonical Commands

- `python -m pytest`

Read-only repository inspection commands used during bootstrap:

- `git status`;
- `git diff`;
- `git diff --check`;
- `git rev-parse --show-toplevel`;
- `git rev-parse --git-common-dir`;
- `git branch --show-current`;
- `git remote -v`.

## Current Established Results

- VERIFIED FACT: the foundation smoke tests include finite quadratic-radii computations for fixed orders, including `(1,4,9)` and sampled orders from `quadratic_radii(6)` and `quadratic_radii(7)`.
- VERIFIED FACT: the fixed-order crosscheck tests include a finite numerical comparison where SLSQP matches the STN fixed-order radius for the quadratic order `(16,1,9,4)` within the test tolerance.
- VERIFIED FACT: the standalone verifier accepted the high-precision fixed-order radius for `(1,4,9)` and rejected a radius smaller by `1e-8` during the 2026-07-10 verification.
- VERIFIED FACT: no certified quadratic-radii optimum has yet been established in this repository.
- VERIFIED FACT: no quadratic-radii theorem has yet been established in this repository.
- VERIFIED FACT: no quadratic-radii certificate or experiment artifact has yet been created in this repository.
