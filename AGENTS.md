# AGENTS.md - Power-Ringmin Operating Contract

## 0. Project Configuration

- **Project name:** `power-ringmin`
- **Project title:** Power-Ringmin: Quadratic Radii
- **Author:** Maurizio Falconi
- **Purpose:** independent mathematical research repository for the quadratic-radii extension of Ringmin.
- **Primary outputs:** definitions, proofs, certified finite results where feasible, numerical experiments, reproducible code, figures, and research notes.
- **Typical work:** mathematical formulation, code implementation, tests, optimization experiments, certificate generation, proof development, and documentation.
- **Default work mode:** `STANDARD`; use `STRICT` for mathematical claims, certification, long experiments, or changes affecting reproducibility.
- **Stack and tools:** Python 3.11+ (`setuptools`, `src` layout); `mpmath` for high-precision and guarded interval arithmetic; optional NumPy/SciPy SLSQP cross-checks; `pytest` and `jsonschema` for verification; JSON artifact schemas, console CLIs, standalone `verify.py`, and a GitHub Actions Python 3.11-3.13 verification matrix.
- **Canonical commands:** only record commands after they have been run in this repository.
- **Document source hierarchy:** the unambiguous role and conflict rules are
  defined in Section 3. `start.md` is a deprecated compatibility pointer, not
  an authoritative source or project-memory file.
- **Protected paths/systems:** the upstream Ringmin repository at `C:\Users\Falker\Desktop\Code\circle\ringmin` is read-only; Git remotes, staging, commits, pushes, merges, rebases, resets, and history edits are not allowed for Codex.
- **Project-specific constraints:** this is an independent repository, not a Ringmin worktree or branch. Do not silently generalize Ringmin results to quadratic radii.

Project-specific rules in this file take precedence over generic defaults.

## 1. Core Role

Codex works as a repository-local collaborator. It may inspect, reason, edit, test, and document inside this repository, within one bounded task per chat.

Codex must:

- use the filesystem as durable project memory;
- treat chat as temporary execution context;
- inspect before modifying;
- make the smallest coherent change that completes the task;
- connect every material change to verification;
- preserve enough state for a later session to resume;
- separate definitions, verified facts, assumptions, heuristics, conjectures, and open questions.

`AGENTS.md` is an operating contract, not a diary or backlog.

## 2. One Task Per Chat

- One fresh Codex chat corresponds to one bounded task.
- The first user prompt defines that task.
- Codex works only on that task.
- Codex continues autonomously through all non-blocked steps required to finish it.
- Codex must not begin the next task in the same chat.
- The next task is always performed in a fresh Codex chat.

## 3. Durable Memory

- The filesystem is the durable project memory.
- Chat is temporary execution context.
- All information required by later sessions must be stored in project files.
- Do not rely on previous chat messages being available.
- Promote only stable, reusable, verified or explicitly classified knowledge to `PROJECT_KNOWLEDGE.md`.
- Keep transient chronology and evidence inside the relevant task dossier.

### Document Source Hierarchy

Each document class has one role. A file must not take over the role assigned
to another class.

1. `AGENTS.md` is the authoritative operational contract. It governs how work
   is performed, but it is not a proof, roadmap, or task-status document.
2. `research/*.md` contains the authoritative detailed mathematical proofs.
   When a compact mathematical summary differs from its linked proof, the
   proof controls the mathematical detail and the summary must be corrected.
3. `PROJECT_KNOWLEDGE.md` contains only stable, reusable results in compact
   form, with links to the detailed proof or durable evidence. It contains no
   task chronology, proof development, current status, or ranked roadmap.
4. `CURRENT_STATUS.md` contains only the current task, its state, blockers,
   and the next task. It must not repeat proofs, diagnostics, or prior-task
   handoffs.
5. `research/NEXT_RESEARCH_STEPS.md` is the sole roadmap and priority source.
   It records completed milestones and pending priorities without duplicating
   proofs or task evidence.
6. `ops/` contains task-local status, append-only chronology, evidence, and
   diagnostic assets. A dossier is authoritative only for its task history and
   evidence; it does not define the current global roadmap.

`start.md` is retained only as a deprecated compatibility stub pointing to
the current sources above. It is not substantive project memory. Do not create
another global summary file. In a cross-file conflict, use the source assigned
to that kind of information and correct the out-of-role duplicate.

## 4. Manual Review And Manual Commits

Codex must never run:

- `git add`;
- `git commit`;
- `git push`;
- merge commands;
- rebase commands;
- reset commands;
- history-rewriting commands;
- remote-creation or remote-modification commands.

Codex may use read-only Git commands such as:

- `git status`;
- `git diff`;
- `git diff --check`;
- `git log`;
- `git show`;
- `git rev-parse`;
- `git remote -v`.

The user reviews all changes and performs commits manually.

Successful modified work ends with status `READY_FOR_REVIEW`, not `DONE` and not `BLOCKED`.

`READY_FOR_REVIEW` means:

- the bounded task has been implemented;
- required verification has completed;
- durable memory has been updated;
- the final diff has been inspected;
- the user must now review and decide whether to commit.

A task is `BLOCKED` only when implementation or verification cannot proceed because of a genuine unresolved dependency, missing resource, missing material decision, or inaccessible information.

The absence of a Git commit is never a blocker.

## 5. Startup Protocol For Every New Task

At the start of every new task, Codex must:

1. locate the repository root;
2. read the applicable `AGENTS.md`;
3. read `PROJECT_KNOWLEDGE.md`;
4. read `CURRENT_STATUS.md`;
5. inspect the relevant proof, roadmap entry, and task dossier;
6. inspect the Git working tree;
7. normally require a clean working tree before beginning a new task;
8. stop and report unrelated uncommitted changes rather than mixing tasks;
9. inspect the actual code, data, and evidence before reasoning from assumptions.

If required startup files are missing during bootstrap, create only the minimum files needed by the bootstrap task.

## 6. Memory Structure

Use this minimum structure unless a task justifies more:

```text
<PROJECT_ROOT>/
|-- AGENTS.md
|-- start.md                         # deprecated compatibility stub
|-- PROJECT_KNOWLEDGE.md
|-- CURRENT_STATUS.md
|-- research/
|   `-- NEXT_RESEARCH_STEPS.md      # roadmap and priorities only
|-- UPSTREAM_RINGMIN.md
|-- AGENTS_GENERIC_TEMPLATE_v2.md
|-- _TEMPLATES/
|   |-- TASK_STATUS_TEMPLATE.md
|   |-- TASK_LOG_TEMPLATE.md
|   `-- EVIDENCE_TEMPLATE.md
`-- ops/
    `-- TASK-YYYYMMDD__short_description/
        |-- TASK_STATUS.md
        |-- TASK_LOG.md
        `-- EVIDENCE.md
```

Rules:

- Level 0 files keep their roles from the document source hierarchy; they do
  not duplicate one another.
- Detailed proofs live under `research/`; its `NEXT_RESEARCH_STEPS.md` file is
  roadmap-only.
- `start.md` remains a short deprecated pointer and contains no project brief,
  theorem, roadmap, or status.
- `ops/` contains operational task dossiers, including bootstrap and repository maintenance tasks.
- Task dossiers contain current task truth, chronology, and evidence.
- Do not create duplicate project briefs, duplicate global status files, or decorative documentation.
- Do not create a global chronological log.

## 7. Task Dossiers

Create a task dossier for `STANDARD` or `STRICT` work, or whenever durable handoff matters.

Recommended naming:

```text
ops/TASK-YYYYMMDD__short_description/
```

Each persistent task uses:

- `TASK_STATUS.md` for current truth;
- `TASK_LOG.md` for append-only chronology;
- `EVIDENCE.md` for independently understandable verification.

Avoid duplicating global knowledge inside task files. Reference project files when possible.

## 8. Mathematical Rigor

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
- important conjectures must be actively tested for counterexamples;
- all-pairs constraints must be checked, not only adjacent pairs;
- numerical precision, parameters, solver, seeds, environment, and code version must be recorded when relevant;
- incomplete proofs must retain explicit gaps;
- contradictory evidence must be preserved and investigated;
- no Ringmin theorem, implementation assumption, or observed structural pattern may be silently generalized to quadratic radii.

## 9. Research Execution Loop

Use this loop for implementation, experiments, and proof work:

```text
UNDERSTAND -> INSPECT -> DEFINE EXPECTED DELTA -> ACT -> VERIFY -> RECORD -> HANDOFF
```

For analytical or mathematical work:

1. state the question precisely;
2. define objects, variables, assumptions, and domain of validity;
3. separate known results from hypotheses;
4. examine smallest and boundary cases;
5. establish a simple baseline before optimizing or generalizing;
6. look for invariants, symmetries, equivalent formulations, and decompositions;
7. generate candidate explanations or conjectures;
8. search actively for counterexamples and failure modes;
9. record negative results when they eliminate a plausible approach;
10. separate formal deduction, computational result, heuristic evidence, empirical pattern, conjecture, proof, and certificate;
11. never present finite numerical evidence as a general proof;
12. separate generator or solver from independent verifier when practical.

## 10. Upstream Ringmin Rules

The upstream Ringmin repository is prior work and a read-only reference.

Allowed during a bounded task only when in scope:

- confirm it is a valid Git repository;
- determine its current commit;
- record its public repository URL and provenance;
- understand at a high level which prior assets may later be reused.

Not allowed:

- create a worktree from Ringmin;
- create a branch in Ringmin;
- modify Ringmin files;
- stage or commit anything in Ringmin;
- push anything to Ringmin;
- copy Ringmin source code without an explicit future import task;
- treat Ringmin results as automatically true for quadratic radii.

Future imports must preserve provenance and relevant license notices.

## 11. Verification Standards

Every material change must map to verification proportional to risk.

Possible verification methods include:

- automated tests;
- static checks;
- build or syntax checks;
- independent verifier;
- before/after comparison;
- source inspection;
- high-precision recomputation;
- manual inspection with explicit criteria.

Evidence must state:

- what was checked;
- how it was checked;
- relevant output or result;
- interpretation;
- limitations.

Failed checks are evidence and must be recorded.

### Canonical Local Verification Commands

- `python -m pytest`
- `python -m pytest tests\test_n3_arb_interval_crosscheck.py`
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
- `python -m pytest tests\test_checked_artifact_schema_validation.py`

## 12. Completion Protocol

At the end of a successfully completed task, Codex must:

1. run all relevant tests and verification;
2. update task memory;
3. update `PROJECT_KNOWLEDGE.md` only with stable reusable knowledge;
4. update `CURRENT_STATUS.md`;
5. inspect `git status`;
6. inspect `git diff`;
7. run `git diff --check`;
8. set the task to `READY_FOR_REVIEW`;
9. stop;
10. report the task objective, files changed, commands run, verification results, evidence classification, residual uncertainty or risks, suggested manual commit message, and one proposed next atomic task.

Do not begin the proposed next task in the same chat.
