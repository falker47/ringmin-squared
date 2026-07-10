# UPSTREAM_RINGMIN

Inspection date: 2026-07-10

## Identity

- Public repository URL: `https://github.com/falker47/ringmin.git`
- Local path: `C:\Users\Falker\Desktop\Code\circle\ringmin`
- Current inspected commit: `cc0327400819fe06b230d967cdcbafffe1648317`
- License observed during high-level inspection: MIT, via upstream `LICENSE`.

## Role

Ringmin is prior work by Maurizio Falconi for the original peripheral radii problem

\[
1,2,\dots,n.
\]

It is a read-only upstream reference for Power-Ringmin.

## High-Level Assets Observed

Read-only inspection observed the following upstream asset classes:

- `src/ringmin/`: solver library and CLI;
- `tests/`: pytest coverage;
- `scripts/`: reproducibility and artifact-generation scripts;
- `verify.py`: standalone verifier;
- `results/`: certified optima, frontier certificates, calibration data, and logs;
- `figures/`: generated figures;
- `paper_assets/`: paper source, PDF, figures, tables, and appendix snippets;
- `README.md`, `REPORT.md`, `CITATION.cff`, `LICENSE`, and related project documents.

These observations are for provenance and future planning only. No source code was copied during bootstrap.

## Import Audit - 2026-07-10

Task dossier: `ops/TASK-20260710__upstream_import_audit/`.

Audit basis: read-only inspection of upstream commit `cc0327400819fe06b230d967cdcbafffe1648317`, including Git identity/status, tracked file map, package source, tests, key scripts, result schemas, README/report material, and paper source. No upstream file was modified and no Ringmin source code was copied into Power-Ringmin during this audit.

### Minimum Coherent Import Set

The recommended minimum coherent import is a foundation import, not a wholesale repository copy.

Code to import/adapt first:

- `src/ringmin/geometry.py`: reusable geometric primitives: radius validation, `theta(R,a,b)`, cyclic pairs, and cycle-equivalence checks. This file is already radius-value based.
- `src/ringmin/evaluator.py`: fixed-order evaluator using all-pairs STN feasibility, bisection for `R_full`, recovered witness positions, Cartesian verification, essential tight pairs, and floating-circle detection. This is the core computational asset, but its `R` brackets and tolerances must be reviewed for quadratic radii.
- `src/ringmin/highprec.py`: mpmath STN verifier for fixed orders. Import as the independent high-precision counterpart to the float64 evaluator, with scale-aware bracketing.
- `src/ringmin/patterns.py`: generic sorted-value pattern and Supnick-tour helpers. Import the order constructors as experimental candidates, not as automatic proof of quadratic optimality.
- `src/ringmin/crosscheck.py`: import the fixed-order SLSQP cross-check as an independent numerical validator. The unconstrained global helper is hard-coded to `range(1,n+1)` and should be parameterized before use.
- `src/ringmin/search.py`: import selectively as a certification/search scaffold. It already has `*_values` entry points for arbitrary distinct radius values, but default wrappers, random search, result naming, and the `lb3` lower bound assume original radii and removals `{1}` and `{1,2}`.
- `src/ringmin/artifacts.py`: import after defining a Power-Ringmin artifact schema with explicit `problem`, `radius_sequence`, and provenance fields.
- `src/ringmin/cli.py` and `src/ringmin/plots.py`: optional initial import. They are useful for ergonomics and figures, but should come after the core package API is named and tested.

Tests to import/adapt:

- `tests/conftest.py`: path setup only; adapt if the package name changes.
- From `tests/test_m0.py`: keep theta symmetry/monotonicity tests, rotation/reflection invariance, `R_full >= R_chain`, Supnick helper equivalence, and cycle-equivalence tests; rewrite numeric cases for quadratic radii or label original-radii cases as upstream reference regressions.
- From `tests/test_m1.py`: keep fixed-order SLSQP cross-validation, rewritten for quadratic radius orders. The unconstrained-global test needs a radius-sequence-aware API before import.
- Add new quadratic smoke tests immediately with radii `(1,4,9)`, small fixed orders, and `certified_search_values(tuple(k*k for k in range(1,n+1)))` for small `n`.

Mathematical assets to import/adapt:

- DEFINITION: exact angular separation formula and all-pairs non-overlap formulation.
- DEFINITION: fixed-order chain radius and full radius.
- VERIFIED-FROM-UPSTREAM-SOURCE CLAIM TO REVIEW LOCALLY: fixed-order feasibility can be represented as a circular system of difference constraints / STN and checked by shortest paths.
- VERIFIED-FROM-UPSTREAM-SOURCE CLAIM TO REVIEW LOCALLY: the matrix `theta_R(r_i,r_j)` is symmetric anti-Monge for arbitrary distinct positive radii, giving a Supnick chain-order theorem for the adjacent-chain relaxation. This is promising for quadratic radii, but must be imported as a proof asset and reviewed in this repository before being used as a Power-Ringmin theorem.
- DEFINITION: floating circle via strict slack / no essential pairwise constraint.
- DEFINITION: Descartes pocket formula and its angular feasibility interpretation.
- CERTIFICATION PATTERN: separate generator/search from independent high-precision verifier, record all-pairs checks, witness positions, frontier/pruning metadata, numerical guards, precision, and source provenance.
- Bibliography/provenance entries from `paper_assets/ringmin_paper.tex` for Supnick, the Monge/Supnick survey, Descartes-circle background, and the original problem context.

Reference/provenance assets to import:

- `LICENSE`: required if any substantial Ringmin code or documentation is copied.
- `CITATION.cff`: useful provenance reference; adapt or supplement for Power-Ringmin rather than reusing unchanged as the project citation.
- `pyproject.toml` and `requirements.txt`: use as environment/dependency starting points only. Rename the package and decide fresh versioning before import.
- A short `references/ringmin/` provenance note can cite the upstream commit and public URL. Original Ringmin certified results may be listed there as prior-work evidence, but not as Power-Ringmin quadratic-radii evidence.

### Assets To Exclude From The Minimum Import

- Upstream `.git`, `.agents`, `.pytest_cache`, `__pycache__`, `*.egg-info`, and generated bytecode/cache state.
- `results/checkpoints/*.pkl` and long progress logs: regeneration state, bulky, and not needed for a clean Power-Ringmin import.
- Generated PDFs, arXiv source zips, submission/endorsement documents, and most figure outputs: useful as reference, not needed for the computational foundation.
- Original `results/n03` through `results/n14`, frontier certificates, heuristic artifacts, and CSV summaries as active data. They concern radii `1,2,\dots,n`; if imported at all, place them under a clearly labeled upstream-reference area.
- Analysis scripts tightly coupled to the original paper narrative (`audit_m2.py`, `audit_n8_pocket.py`, `m2_summary.py`, `pocket_definition_audit.py`, `confidence_boost.py`, `refresh_heuristic_artifacts.py`, `export_paper_assets.py`, `build_report.py`) unless a later task explicitly ports that analysis for quadratic radii.

### Required Adaptations Before Trusting Imported Code For Quadratic Radii

- Rename the package/API from `ringmin` to the Power-Ringmin package name selected for this repository.
- Make radius sequences first-class. Prefer functions that accept `values`/`radii` explicitly; wrappers for `r_k=k^2` should be thin and obvious.
- Replace `R` upper brackets such as `4*n*n` with scale-aware brackets that work when `max(r_i)=n^2` and expected `R` is order `n^3`.
- Rework lower bounds in search and verifier. The upstream `lb3` bound removes radii `{1}` and `{1,2}`; for quadratic radii the intended removable prefixes are `{1^2}` and `{1^2,2^2}` or a more general candidate-floating set. Treat this as a new mathematical/computational design decision, not a mechanical copy.
- Update artifact schemas so every result records the radius sequence, exact radii, command, precision, tolerances, search bound version, provenance commit, and whether the result is certified, numerical, heuristic, or conjectural.
- Keep all-pairs validation mandatory; no adjacent-only result should be labeled feasible.
- Adapt `verify.py` to load Power-Ringmin artifacts and recompute with high precision without importing the generator package.
- Rebuild tests around quadratic radii before accepting any imported search/certificate result.

### Import Priority

1. Core package foundation: `geometry.py`, `evaluator.py`, `highprec.py`, selected `patterns.py`, and adapted tests.
2. Independent validation: fixed-order `crosscheck.py`, standalone verifier scaffold, and high-precision tests.
3. Certified-search pipeline: adapted `search.py`, `artifacts.py`, sweep/high-precision/frontier scripts, and small quadratic certificates.
4. Reporting/figures/paper assets only after the computational and mathematical foundation is established.

## Foundation Import - 2026-07-10

Task dossier: `ops/TASK-20260710__foundation_import/`.

Imported/adapted into Power-Ringmin:

- `pyproject.toml` and `requirements.txt` as new Power-Ringmin package metadata, not a direct upstream metadata copy.
- `LICENSE`, preserving the MIT notice for substantial adapted Ringmin code.
- `src/power_ringmin/geometry.py`, adapted from upstream `src/ringmin/geometry.py`.
- `src/power_ringmin/evaluator.py`, adapted from upstream `src/ringmin/evaluator.py` with scale-aware bracketing for quadratic radii.
- `src/power_ringmin/highprec.py`, adapted from upstream `src/ringmin/highprec.py` with scale-aware high-precision bracketing.
- `src/power_ringmin/patterns.py`, adapted selectively from upstream `src/ringmin/patterns.py`; evaluator-dependent exhaustive insertion was not imported.
- `tests/test_quadratic_foundation.py`, adapted from upstream fixed-order/property tests but rewritten for quadratic-radii smoke coverage.

Explicitly not imported in this task:

- upstream `search.py`, `crosscheck.py`, `artifacts.py`, CLI, plots, scripts, result artifacts, figures, paper assets, and original Ringmin certified results.

Verification:

- `python -m pytest` passed 5 tests on 2026-07-10.

Interpretation:

- The imported foundation provides tested fixed-order computational tools for finite quadratic-radii smoke cases.
- This import establishes no quadratic-radii theorem and no certified quadratic optimum.

## Read-Only Rules

Power-Ringmin must not:

- create a worktree from Ringmin;
- create a branch in Ringmin;
- modify Ringmin files;
- stage or commit anything in Ringmin;
- push anything to Ringmin;
- copy Ringmin source code except during a future explicit import task.

Future imports must preserve provenance and relevant license notices.

## Mathematical Caution

Ringmin results concern peripheral radii \(1,2,\dots,n\). They do not automatically transfer to quadratic radii \(1^2,2^2,\dots,n^2\).

No Ringmin theorem, implementation assumption, or observed structural pattern may be silently generalized to Power-Ringmin.

## Inspection Notes

- Git top-level check succeeded using a per-command `safe.directory` override because the sandbox user differs from the repository owner.
- Upstream `git status --short` returned no status entries during bootstrap inspection.
- Bootstrap inspection was read-only and high-level.
- The 2026-07-10 import audit was also read-only and inspected source, tests, scripts, result schemas, and paper assets for import planning.
