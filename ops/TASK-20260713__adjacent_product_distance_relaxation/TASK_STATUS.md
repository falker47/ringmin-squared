# TASK_STATUS - TASK-20260713__adjacent_product_distance_relaxation / Adjacent Product-Distance Relaxation

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** characterize the adjacent product-distance relaxation exactly and determine when non-adjacent positional constraints become essential.
- **Expected output:** all-n adjacent theorem, explicit interleave construction, exact distance-one/distance-two comparison for n=3..11, focused tests, and aligned research memory.

## Scope

- **In scope:** exact proof for A_n; comparison with the tail obstruction; exact truncated scoring and bounded enumeration for n=3..11; source, tests, research note, roadmap, and durable memory.
- **Out of scope:** cyclic-order enumeration beyond n=11; certificates, artifacts, schemas, or CLIs; geometric-optimum claims; commits, staging, pushes, and upstream changes.

## Verified Facts

- Required startup memory and the preceding product-distance dossier were read; the initial Git tree was clean.
- The target formula for A_n is true. A high/low internal-edge count gives the lower bound, and the existing interleave cycle gives the upper bound.
- The adjacent objective sequence for n=3..11 is (6,12,15,20,24,30,35,42,48).
- Exact distance-two objectives equal the existing full W_n values throughout n=3..11. The first adjacent/full gap is 35 < 36 at n=9.
- A_n/n^2 tends to 1/4, while L_n/n^2 tends to 2(sqrt(2)-1)/3.
- Exact tail-formula evaluation gives L_n <= A_n through n=32. The explicit tail m=ceil(2n/5), proved by residue classes modulo 10, gives L_n > A_n for every n>=33.

## Assumptions / Inferences

- Exact finite truncated enumeration is not an all-n characterization of W_n.
- No claim is made about strictness of W_n>A_n for n=12..32.
- No claim is made about when distances at least three first become essential beyond the bounded table.

## Decisions And Rationale

- Add a small exact truncated-enumeration API using the existing canonical space, integer cutoff, hard n<=11 boundary, and work ceiling.
- Reuse patterns.interleave rather than add a duplicate order constructor.
- Record the tail threshold 33 with a symbolic all-n proof from that point onward, while classifying the n=4..32 comparison as finite exact computation.

## Plan And Expected Delta

- Inspect memory, code, and previous evidence. COMPLETE.
- Prove and independently check the adjacent formula and tail comparison. COMPLETE.
- Implement truncated exact scoring/enumeration and focused tests. COMPLETE.
- Update research note, roadmap, project memory, and status. COMPLETE.
- Run full verification and final diff inspection. COMPLETE.

## Verification

- **Checks:** independent exact table probe; residue-polynomial identities;
  Python AST parsing; focused and full pytest; checked-artifact semantic
  verification; exact path, strict UTF-8, trailing-whitespace, equation-tag,
  status, complete diff, and `git diff --check` inspection.
- **Observed result:** truncated values, counts, and representatives reproduced;
  80 residue identities matched; Python AST parsed 2 files; focused tests
  passed 22/22; full pytest passed 140/140; checked artifacts accepted 4
  certificates and 76 local brackets; all 11 intended paths passed hygiene,
  and `git diff --check` produced no output.
- **Limitations:** local runtime is Python 3.14.3; finite enumeration proves no
  all-n statement about W_n, and current hosted CI status is unverified.

## Blockers / Risks

- No blocker.
- Main risks are overclaiming the unresolved n=12..32 interval, confusing finite computation with an all-n proof, or silently extending cyclic-order enumeration; current code and prose preserve these boundaries.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused/full tests, checked-artifact verification,
  independent exact probes, and final scope/UTF-8/whitespace/diff hygiene pass.
- **Files changed:** product-distance and pattern source, focused tests,
  research note, roadmap, project brief/knowledge/status, and this dossier.
- **Files to read first:** research/PRODUCT_DISTANCE_SURROGATE.md, src/power_ringmin/product_distance.py, tests/test_product_distance.py, and EVIDENCE.md.
