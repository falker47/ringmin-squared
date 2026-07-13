# TASK_STATUS - TASK-20260713__align_contract_state_provenance / Align Contract And State Provenance

Last update: 2026-07-13

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** align the repository operating-contract configuration, GitHub Actions status provenance, and next-task roadmap before the next research task.
- **Expected output:** a factual `AGENTS.md` stack summary; provenance-safe CI wording in the four requested state/roadmap files; the product-distance surrogate formalization and analysis as the recommended next task; STN documentation retained as later certification debt; task evidence and final document hygiene checks.

## Scope

- **In scope:** `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, and this task dossier.
- **Out of scope:** source code, tests, mathematical proofs, checked artifacts, certificates, surrogate analysis, Git staging/commits/pushes, and upstream Ringmin changes.

## Verified Facts

- Required startup files and the current roadmap were read.
- Initial `git status --short --branch` returned `## main...origin/main` with no changed paths.
- Initial `HEAD` is `ab2cc30` (`Prove improved zigzag core cubic upper bound`).
- The repository contains a Python `src` package, tests, JSON schemas and checked artifacts, command-line tools, and a GitHub Actions workflow.
- The CI-related task dossiers record local verification and explicitly state that hosted GitHub Actions was not observed locally.
- The later roadmap dossier records only user-reported green hosted context; it does not provide a hosted run URL, run identifier, or independently verified commit association.
- Three independent final reviews found the stack description factual, the CI provenance distinctions correct, the roadmap ordering correct, and no surrogate analysis introduced.

## Assumptions / Inferences

- No hosted success should be attributed to a commit without recorded evidence that identifies and verifies that hosted run.
- Because this task does not query GitHub, current hosted status must remain explicitly unverified.

## Decisions And Rationale

- Use `STANDARD` mode because the task changes operating metadata and durable research planning but no mathematical or certification result.
- Preserve every operational, Git-safety, and manual-review rule in `AGENTS.md`; change only the obsolete stack/configuration bullet.
- Describe the surrogate only as the next task objective and acceptance boundary; do not define or analyze it in this task.

## Plan And Expected Delta

- Complete stack, CI-provenance, and roadmap audits. COMPLETE.
- Apply the minimum documentation-only patch to the five requested files. COMPLETE.
- Run targeted content, Markdown/path, and whitespace checks. COMPLETE.
- Inspect Git status and the complete final diff, record evidence, and set `READY_FOR_REVIEW`. COMPLETE.

## Verification

- **Checks:** required-wording assertions; obsolete-wording absence; referenced-path existence; UTF-8 reads; trailing-whitespace scan; `git diff --check`; independent stack, CI-provenance, and roadmap reviews; Git status and complete diff inspection.
- **Observed result:** required wording and obsolete-wording checks passed; 6 referenced paths exist; 8 changed documents read as UTF-8 without replacement characters; trailing-whitespace scan found no matches; `git diff --check` produced no output; all three independent reviews passed; `AGENTS.md` changes exactly one line; final scope contains only the five requested documents and this dossier.
- **Limitations:** hosted GitHub Actions will not be queried; no code/test/proof/artifact behavior will be revalidated because those files are out of scope and unchanged.

## Blockers / Risks

- No current blocker.
- Residual limitation: current hosted GitHub Actions status remains unverified, and no hosted result is attributed to a specific commit.

## Next Atomic Action

- User reviews the documentation-only diff and decides whether to commit manually.

## Handoff

- **Last verified result:** all targeted document, path, UTF-8, whitespace, scope, and diff checks passed; independent reviews passed.
- **Files changed:** `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, and this task dossier.
- **Files to read first:** `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, and this dossier.
