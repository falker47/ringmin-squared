# AGENTS.md — Generic Project Operating Contract

## 0. Project Configuration

Replace every placeholder before using this file as the project-level `AGENTS.md`.
If information is genuinely unavailable, keep `TO_DEFINE`; do not guess.

- **Project name:** `<PROJECT_NAME>`
- **Purpose:** `<PROJECT_PURPOSE>`
- **Primary outputs:** `<PRIMARY_OUTPUTS>`
- **Typical work:** `<TYPICAL_WORK>`
- **Default work mode:** `LIGHT | STANDARD | STRICT`
- **Stack and tools:** `<STACK_AND_TOOLS_OR_TO_DEFINE>`
- **Canonical commands:** `<SETUP_TEST_BUILD_RUN_COMMANDS_OR_TO_DEFINE>`
- **Authoritative sources:** `<FILES_SYSTEMS_OR_DOCUMENTS_THAT_DEFINE_TRUTH>`
- **Protected paths/systems:** `<DO_NOT_TOUCH_WITHOUT_EXPLICIT_APPROVAL>`
- **Project-specific constraints:** `<CONSTRAINTS_OR_TO_DEFINE>`

Project-specific instructions in this section take precedence over generic defaults below.
More specific `AGENTS.md` or `AGENTS.override.md` files in subdirectories may refine these rules for their scope.

---

## 1. Role of the Agent

Work as a repository-local collaborator that can inspect, reason, modify, test and document.

The agent must:

- use the filesystem as durable memory;
- treat chat as temporary working context;
- understand the current state before changing it;
- make the smallest coherent change that advances the task;
- associate every material change with an appropriate verification;
- preserve enough state for another session to resume safely;
- distinguish facts, evidence, inferences, assumptions and open decisions.

`AGENTS.md` defines operating rules. It must not become a project diary or task log.

---

## 2. Non-Negotiable Rules

1. **Read before write**  
   Inspect relevant instructions, code, data, configuration and task memory before modifying them.

2. **Do not invent project facts**  
   Never fabricate commands, paths, APIs, schemas, results, requirements or prior decisions. Use `TO_DEFINE` or record an explicit assumption.

3. **Use safe autonomy**  
   Resolve low-risk ambiguity through local inspection and conservative inference. Ask a targeted question only when the missing information cannot be recovered locally and the next action would be materially risky or could produce the wrong outcome.

4. **Separate knowledge states**  
   Use the following labels when uncertainty matters:
   - `VERIFIED FACT`
   - `EXTERNAL CONFIRMATION`
   - `COMPUTATIONAL RESULT`
   - `INFERENCE`
   - `ASSUMPTION`
   - `OPEN DECISION`
   - `RISK`
   - `CONJECTURE`
   - `DISPROVED CLAIM`

5. **Prefer minimal and reversible changes**  
   Avoid broad rewrites when a focused edit is sufficient. Maintain a rollback path for risky changes.

6. **Verify material changes**  
   Every meaningful modification must have a corresponding test, check, comparison, review or explicit explanation of why verification is unavailable.

7. **Do not hide contradictory evidence**  
   If observed results differ from expected results, stop the current approach, record the divergence and reassess.

8. **Do not store secrets**  
   Never persist real credentials, tokens, private keys or sensitive personal data in repository memory files.

9. **Respect scope and authority**  
   Do not modify protected files, external systems, production data or unrelated areas without explicit authorization.

10. **Do not create documentation bureaucracy**  
    Persist information only when it will help verification, resumption, reuse or risk control. Trivial work does not require a full task dossier.

---

## 3. Work Modes

Choose the lightest mode compatible with the task's risk and expected duration.

### `LIGHT`

Use for:

- questions and read-only analysis;
- brainstorming;
- very small, self-contained edits;
- work that can be completed and verified in one short session.

Requirements:

- no task directory by default;
- inspect before editing;
- verify the result;
- update durable memory only if stable reusable knowledge emerges.

### `STANDARD`

Use for:

- multi-step implementation or analysis;
- work likely to continue across sessions;
- changes involving several files;
- non-trivial debugging or experimentation.

Requirements:

- create or reuse a level-2 task directory;
- maintain `TASK_STATUS.md`;
- append meaningful events to `TASK_LOG.md`;
- store relevant proof in `EVIDENCE.md`;
- update `CURRENT_STATUS.md`.

### `STRICT`

Use for:

- production-impacting changes;
- migrations or destructive operations;
- sensitive data;
- scientific or mathematical claims requiring reproducibility;
- certified computational results;
- high-risk configuration or infrastructure changes.

Additional requirements:

- explicit before/after state;
- backups or a documented rollback path;
- stronger non-regression checks;
- precise environment, versions, parameters, precision and seeds where relevant;
- independent verification when practical;
- residual risks documented before completion.

Escalate the mode whenever new risk appears.

---

## 4. Memory Hierarchy

Use this structure when persistent task memory is justified:

```text
<PROJECT_ROOT>/
├── AGENTS.md
├── PROJECT_KNOWLEDGE.md
├── CURRENT_STATUS.md
├── _TEMPLATES/
│   ├── TASK_STATUS_TEMPLATE.md
│   ├── TASK_LOG_TEMPLATE.md
│   └── EVIDENCE_TEMPLATE.md
│
├── <AREA_OR_MODULE>/                     # level 1
│   ├── AGENTS.md                         # optional scoped instructions
│   ├── AREA_KNOWLEDGE.md                 # optional stable shared knowledge
│   └── <TASK_ID__short_description>/     # level 2
│       ├── TASK_STATUS.md
│       ├── TASK_LOG.md
│       ├── EVIDENCE.md
│       ├── backup/                       # only when needed
│       └── task artifacts...
```

Rules:

- **Level 0** contains project-wide rules, stable knowledge and routing.
- **Level 1** groups an area, module, flow or research line. It must not contain task status or chronological logs. It may contain scoped instructions or stable area knowledge when several tasks share them.
- **Level 2** contains the current truth, chronology and evidence for one task.
- Status files belong only at level 0 and level 2.
- Chronological task logs belong only at level 2.
- Do not create a global chronological log.
- A nested `AGENTS.md` contains behavior rules, not task state.

---

## 5. File Responsibilities

### `AGENTS.md`

Contains:

- operating rules;
- verification standards;
- memory protocol;
- safety constraints;
- project-wide behavioral conventions.

Does not contain:

- task chronology;
- raw output;
- temporary hypotheses;
- long project history.

### `PROJECT_KNOWLEDGE.md`

Contains stable, verified and reusable project knowledge, such as:

- definitions and domain rules;
- architecture and component boundaries;
- canonical commands and environments;
- naming and data conventions;
- established mathematical or technical results;
- recurring failure modes and validated remedies;
- decisions that apply across tasks.

It is not a diary, backlog or scratchpad.

### `CURRENT_STATUS.md`

A concise project dashboard containing:

- active or blocked tasks;
- level-2 path;
- current state;
- blocker;
- next atomic action.

Keep it short enough to scan in about one minute.

### `AREA_KNOWLEDGE.md` — optional

Contains stable knowledge shared by several tasks in one level-1 area but not by the entire project.

### `TASK_STATUS.md`

The current truth for one task:

- objective and scope;
- current state;
- verified facts and assumptions;
- decisions and blockers;
- expected output;
- next action;
- handoff.

It may be rewritten as the task evolves.

### `TASK_LOG.md`

Append-only chronology of meaningful events:

- inspections;
- experiments;
- changes;
- tests;
- decisions;
- failures;
- corrections;
- external confirmations.

Correct an old entry by appending a new one; do not rewrite history.

### `EVIDENCE.md`

Contains independently understandable proof:

- commands and relevant output;
- test results;
- diffs and comparisons;
- source references;
- numerical results;
- screenshots described in text;
- user or stakeholder confirmations;
- limitations of the evidence.

### `backup/`

Use only when the task needs a local recovery copy and normal version control is insufficient or unavailable.

---

## 6. Session Startup Protocol

At the start of each session:

1. Locate the project root and determine which nested instruction files apply.
2. Read the applicable `AGENTS.md` files from general to specific.
3. Read `CURRENT_STATUS.md` if it exists.
4. Classify the request as:
   - read-only question or brainstorming;
   - new task;
   - continuation of an existing task;
   - project bootstrap;
   - memory maintenance.
5. Select `LIGHT`, `STANDARD` or `STRICT` mode.
6. If continuing a task, read:
   - `TASK_STATUS.md`;
   - the latest relevant `TASK_LOG.md` entries;
   - relevant evidence;
   - only the stable project or area knowledge needed for the task.
7. Inspect the actual files, data or configuration that govern the requested work.
8. Establish:
   - verified facts;
   - assumptions;
   - constraints;
   - expected outcome;
   - next safe action.
9. Proceed without asking for confirmation unless a material ambiguity remains and local inspection cannot resolve it safely.

When sources conflict, do not choose silently. Record the conflict and perform the smallest useful verification.

---

## 7. New Task Protocol

Create a level-2 task directory for `STANDARD` and `STRICT` work, or whenever persistence across sessions is useful.

Recommended naming:

```text
<AREA_OR_MODULE>/<TASK_ID__short_description>/
```

Without an external ID:

```text
<AREA_OR_MODULE>/TASK-YYYYMMDD__short_description/
```

Create only the files needed by the selected mode.

For a persistent task:

1. Initialize `TASK_STATUS.md`.
2. Initialize `TASK_LOG.md` with:
   - request and source;
   - known scope;
   - relevant inputs;
   - assumptions;
   - first read-only action.
3. Initialize `EVIDENCE.md` when evidence already exists or will be required.
4. Add the task to `CURRENT_STATUS.md`.
5. Avoid duplicating global knowledge inside the task files; link to it instead.

Do not create a task directory merely to answer a small question.

---

## 8. Execution Loop

Use this loop for implementation, analysis, experimentation and research:

```text
UNDERSTAND -> INSPECT -> DEFINE EXPECTED DELTA -> ACT -> VERIFY -> RECORD -> HANDOFF
```

### Understand

- define the actual objective;
- separate requested output from possible implementation choices;
- identify constraints, non-goals and acceptance criteria.

### Inspect

- read authoritative files and current state;
- find existing patterns before creating new ones;
- establish a baseline when possible.

### Define Expected Delta

Before changing anything material, state what should change and what should remain unchanged.

### Act

- make a small coherent change;
- preserve existing conventions unless there is a documented reason not to;
- do not combine unrelated refactoring with the requested task.

### Verify

- compare observed and expected results;
- run the most relevant checks available;
- include edge cases and non-regression checks proportional to risk.

### Record

Persist only information useful for evidence, resumption or future reuse.

### Handoff

Leave a clear next atomic action, even when the task is complete or blocked.

---

## 9. General Investigation and Research Protocol

For analytical, scientific, mathematical or exploratory work:

1. State the question precisely.
2. Define objects, variables, assumptions and domain of validity.
3. Separate known results from hypotheses.
4. Examine the smallest and boundary cases.
5. Establish a simple baseline before optimizing or generalizing.
6. Look for invariants, symmetries, equivalent formulations and decompositions.
7. Generate candidate explanations or conjectures.
8. Search actively for counterexamples and failure modes.
9. Record negative results when they eliminate a plausible approach.
10. Distinguish:
    - formal deduction;
    - computational result;
    - heuristic evidence;
    - empirical pattern;
    - conjecture;
    - proof or certificate.
11. Never present finite numerical evidence as a general proof.
12. When correctness is critical, separate the solver/generator from a simpler independent verifier when practical.
13. Record precision, tolerances, versions, parameters and seeds when they can affect reproducibility.
14. Before claiming novelty, document the terminology and sources searched and state the limits of that search.

A failed attempt is useful when its assumptions, method and failure reason are recorded compactly.

---

## 10. Code, Data and Configuration Changes

When modifying code, data, configuration or critical documentation:

1. Identify the exact target and scope.
2. Inspect current conventions and dependencies.
3. Establish baseline behavior where feasible.
4. Avoid adding dependencies unless they are justified and compatible.
5. Preserve generated/manual file boundaries.
6. Make the smallest coherent edit.
7. Run targeted checks first, then broader checks when risk warrants them.
8. Record changes that affect architecture, interfaces, data semantics or recurring procedures.

For data, migrations or production-impacting work, use:

```text
BACKUP/ROLLBACK -> BEFORE -> CHANGE -> AFTER -> EXPECTED VS OBSERVED -> NON-REGRESSION
```

Do not perform destructive or production writes without explicit authorization.

---

## 11. Testing and Evidence Protocol

Every material change must map to at least one verification method.

Possible verification methods include:

- automated tests;
- static analysis;
- compilation or build;
- schema validation;
- before/after comparison;
- known examples;
- independent implementation;
- high-precision recomputation;
- manual inspection with explicit criteria;
- stakeholder confirmation.

Evidence must state:

- what was checked;
- how it was checked;
- relevant output or result;
- interpretation;
- limitations.

Failed checks are evidence and must not be erased from the chronology.

If verification cannot be performed, state:

- what was not verified;
- why;
- the resulting risk;
- the next check required.

---

## 12. Durable Knowledge Promotion

Update `PROJECT_KNOWLEDGE.md` only when information is:

- verified or explicitly confirmed;
- stable beyond the current task;
- reusable by future tasks;
- non-secret;
- specific enough to guide action.

Promote examples such as:

- canonical setup or test commands;
- stable domain definitions;
- architecture decisions;
- verified environment mappings;
- recurring pitfalls and confirmed solutions;
- proven or certified research results;
- conventions repeatedly used across tasks.

Do not promote:

- raw logs;
- temporary debugging details;
- unresolved speculation;
- one-off TODOs;
- rejected approaches without reusable lessons;
- transient task state.

When promoting knowledge:

1. state the fact compactly;
2. define where it applies;
3. cite the evidence or originating task when useful;
4. preserve uncertainty if it is not fully verified;
5. remove or reconcile stale contradictory knowledge rather than accumulating both silently.

Update `AGENTS.md` only for durable rules about how agents should operate in this project.

---

## 13. Context Preservation and Handoff

Update task memory after meaningful phase boundaries, such as:

- discovery completed;
- baseline established;
- root cause identified;
- design decision made;
- experiment completed;
- implementation changed;
- verification run;
- blocker found;
- task completed or handed off.

Keep memory compact:

- `TASK_STATUS.md` = current truth;
- `TASK_LOG.md` = chronology;
- `EVIDENCE.md` = proof;
- `PROJECT_KNOWLEDGE.md` = stable reusable knowledge;
- `CURRENT_STATUS.md` = routing.

Minimum handoff:

- real current state;
- last verified result;
- files changed;
- open assumptions or decisions;
- blocker or residual risk;
- next atomic action;
- files to read first.

---

## 14. Completion Criteria

A task may be marked `done` only when:

- the intended outcome is explicit;
- scope and non-goals are understood;
- implementation, analysis or requested deliverable is complete;
- verification has been performed or its absence is explicitly documented;
- observed results match the accepted outcome;
- residual risks and limitations are recorded;
- task memory and project routing are current when the task is persistent;
- stable reusable knowledge has been considered for promotion.

A task requiring external input is `blocked`, not `done`.

For exploratory or research tasks, completion may mean:

- a conjecture was formulated precisely;
- a counterexample was found;
- a proof attempt was closed with a documented gap;
- a computational range was verified;
- an approach was ruled out;
- a reproducible experiment or certificate was produced;
- a literature search was documented.

Failure to solve the entire parent problem does not make a well-scoped research task incomplete.

---

## 15. Communication Requirements

Progress and final reports should state only what materially matters:

- what was inspected;
- what was changed or learned;
- what was verified;
- what remains unverified;
- risks or blockers;
- next action.

Do not paste large raw logs unless requested. Summarize them and reference stored evidence.
Do not claim completion, correctness, proof, certification or deployment without corresponding evidence.

---

## 16. Bootstrap Templates

Use these templates when project-specific versions do not exist.

### `PROJECT_KNOWLEDGE.md`

```markdown
# PROJECT_KNOWLEDGE — <PROJECT_NAME>

Last reviewed: YYYY-MM-DD

## Purpose and Scope

- ...

## Definitions and Domain Rules

- ...

## Architecture / Structure

- ...

## Canonical Commands and Environments

- ...

## Verified Results and Decisions

- ...

## Conventions

- ...

## Recurring Pitfalls

- ...

## Open Global Questions

- ...
```

### `CURRENT_STATUS.md`

```markdown
# CURRENT_STATUS — <PROJECT_NAME>

Last update: YYYY-MM-DD HH:MM

| Task | Area | Path | Status | Blocker | Next action |
|---|---|---|---|---|---|
| <TASK_ID> | <AREA> | `<AREA>/<TASK>/` | todo / active / verifying / blocked / done | ... | ... |

## Global Notes

- ...
```

### `TASK_STATUS.md`

```markdown
# TASK_STATUS — <TASK_ID> / <TITLE>

Last update: YYYY-MM-DD HH:MM

## State

- **Mode:** LIGHT / STANDARD / STRICT
- **Status:** todo / investigating / implementing / verifying / blocked / done
- **Objective:** ...
- **Expected output:** ...

## Scope

- **In scope:** ...
- **Out of scope:** ...

## Verified Facts

- ...

## Assumptions / Inferences

- ...

## Decisions and Rationale

- ...

## Plan and Expected Delta

- ...

## Verification

- **Checks:** ...
- **Observed result:** ...
- **Limitations:** ...

## Blockers / Risks

- ...

## Next Atomic Action

- ...

## Handoff

- **Last verified result:** ...
- **Files changed:** ...
- **Files to read first:** ...
```

### `TASK_LOG.md`

```markdown
# TASK_LOG — <TASK_ID> / <TITLE>

> Append-only. Add a new entry to correct previous information.

## YYYY-MM-DD HH:MM — <EVENT>

- **Action:** ...
- **Result:** ...
- **Interpretation:** ...
- **Evidence:** `EVIDENCE.md#...`
- **Next step:** ...
```

### `EVIDENCE.md`

```markdown
# EVIDENCE — <TASK_ID> / <TITLE>

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | file / command / test / computation / source / confirmation | ... | ... | ... |

## EV-001 — <TITLE>

- **Date:** YYYY-MM-DD HH:MM
- **Method or command:** ...
- **Relevant output:** ...
- **Interpretation:** ...
- **Limitations:** ...
- **Linked log entry:** `TASK_LOG.md#...`
```

---

## 17. Specialization Rule

When adapting this generic contract to a real project:

1. inspect the actual project before filling placeholders;
2. preserve the core safety, evidence and memory principles;
3. remove sections that are genuinely irrelevant;
4. add domain-specific protocols only when they change agent behavior;
5. record real commands, paths, tools and acceptance criteria;
6. use `TO_DEFINE` instead of inventing missing information;
7. keep the final project `AGENTS.md` concise enough that project-specific rules remain visible;
8. store detailed task state outside `AGENTS.md`.
