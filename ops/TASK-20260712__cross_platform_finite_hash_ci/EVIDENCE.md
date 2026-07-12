# EVIDENCE - TASK-20260712__cross_platform_finite_hash_ci

## Evidence Classification

- Digest semantics and schema documentation updates are VERIFIED FACTS once implemented and tested.
- Checked finite brackets, candidate sets, and exclusion gaps remain COMPUTER-CERTIFIED RESULTS under the existing repository semantics; this task does not change their mathematical content.

## Commands And Results

### Startup

- `Get-Location`
  - Result: repository root confirmed as `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- `Get-Content -Raw AGENTS.md`
  - Result: operating contract read.
- `Get-Content -Raw start.md`
  - Result: project brief read.
- `Get-Content -Raw PROJECT_KNOWLEDGE.md`
  - Result: durable knowledge read.
- `Get-Content -Raw CURRENT_STATUS.md`
  - Result: current project status read.
- `git status --short`
  - Result: no output; initial working tree clean.

### Inspection

- `rg --files`
  - Result: repository files enumerated.
- `Get-ChildItem -Name ops`
  - Result: task memory inspected.
- `Get-Content -Raw src\power_ringmin\finite_results.py`
  - Result: raw-byte `_sha256_file` source digest found.
- `Get-Content -Raw tests\test_finite_results.py`
  - Result: tests found to compare `content_sha256` against raw `hashlib.sha256(path.read_bytes())`.
- `Get-Content -Raw schemas\README.md`
  - Result: finite-results schema documentation found to describe recomputed source SHA-256 hashes.
- `Get-Content -Raw .github\workflows\verification.yml`
  - Result: workflow found to install only `.[test]`.

### Implementation Verification

- `python -m pytest tests\test_finite_results.py`
  - Result before summary regeneration: failed with `1 failed, 15 passed`.
  - Interpretation: expected stale-summary failure because `examples/finite_results_summary_n3_n6.json` still contained the old platform-dependent hashes.
- `python -m power_ringmin.finite_results --created-at-utc 2026-07-12T00:00:00Z --output examples\finite_results_summary_n3_n6.json`
  - Result: failed with `ModuleNotFoundError: No module named 'power_ringmin'`.
  - Interpretation: direct module execution needed `src/` on `PYTHONPATH` because the package is not installed in this shell.
- `$env:PYTHONPATH='src'; python -m power_ringmin.finite_results --created-at-utc 2026-07-12T00:00:00Z --output examples/finite_results_summary_n3_n6.json`
  - Result: passed and regenerated the checked finite-results summary.
  - Note: Python emitted a `runpy` warning because package import preloaded `power_ringmin.finite_results`; command exit code was `0`.
- `python -m pytest tests\test_finite_results.py`
  - Result: passed with `16 passed in 6.68s`.
- `python -m pytest`
  - Result: final run passed with `109 passed in 29.99s`.
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  - Result: passed with `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- `git diff --check`
  - Result: passed with no output.

## Interpretation

- VERIFIED FACT: `source_content_sha256` hashes source certificate bytes after normalizing CRLF and lone CR to LF, without decoding text or normalizing any other byte.
- VERIFIED FACT: tests cover LF/CRLF/lone-CR digest equivalence, changed-content digest sensitivity, and finite-summary validation when a real source certificate changes only by line endings.
- VERIFIED FACT: the checked finite-results summary was regenerated with normalized `content_sha256` values.
- VERIFIED FACT: the GitHub Actions workflow now installs `.[test,crosscheck]` before running the full test suite.

## Limitations

- Local verification cannot observe hosted GitHub Actions after commit.
- The existing interval-backend trust limitations remain unchanged.
