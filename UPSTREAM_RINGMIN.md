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
- The upstream repository was inspected only read-only for provenance and high-level asset awareness.

