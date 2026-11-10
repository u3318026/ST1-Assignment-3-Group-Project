# Stage 10 PG agentic rescheduling activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG help is voluntary and unassessed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage10_pg/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Protect the common Stage 9 SHA and UG Stage 12 pathway.

This is a blank student record. Use actual accessible links and concise evidence; do not invent an agent session, test result or approval. Retain this record's headings when linking equivalent issue/PR evidence.

Group/tutorial: Group 6 / Wednesday 2.30 pm - 4.30 pm

Assessed PG members and roles: Md Tahmid Ul Islam Tonmoy — responsible for Stage 10 rescheduling, Stage 11 assurance and Stage 12 release preparation.

Optional UG contributors: [response or none]

## A Access baseline and recovery

- Confirmed GitHub Copilot feature/mode, version/environment and teaching-team approval reference: GitHub Copilot Chat in VS Code on macOS. I used Ask for planning and Agent for implementation. My tutor advised that GPT use was permitted. No separate written confirmation of the specific Copilot modes is recorded.
- Actual account access and tool permissions check: Ask mode read and searched the workspace and returned a plan without editing files or running commands. A separate Agent session applied the approved edits. No agent terminal commands, commits, pushes or merges were reported.
- Live route or convenor-confirmed equivalent staged interaction: Live GitHub Copilot Chat: Ask for the plan, my scope approval in Section D, then Agent for the approved edits. I inspected the changes and ran the tests myself.
- Access limitation and tutor resolution if applicable: The first implementation request ran in a read-only session and made no edits. I switched to an Agent session and submitted the same approved scope. No tutor intervention was needed for this access issue.

- Protected Stage 9 common SHA / recoverable reference: ad62e75f16a38e6ba2e7099391edfe526dff2872

- Common baseline command / project working directory / actual result: From project/, ran ../.venv/bin/python -m pytest -q with Python 3.12.10 and pytest 8.3.5. Result: 81 passed in 0.07s.

- Clean branch and preparer / recovery baseline: I created feature/stage10-rescheduling from the clean Stage 9 commit above.

- Evidence-only later SHA if different / explanation: Pending commit on docs/stage10-evidence. The tested integration SHA is fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc; the separate evidence update does not change the tested code.

## B Tutorial activities

### B1 Rewrite the vague task

“Improve SmartCare appointment scheduling.” Write your bounded goal, requirements, exclusions, constraints, acceptance criteria and Definition of Done:

Bounded task
- Goal: Add rescheduling so an existing scheduled appointment can move to a new time during the current session.

- Requirements: Implement RES-01–`RES-06`, using RES-05-R2 for session visibility. Keep the same appointment object, ID, patient and practitioner. Change only its time.

- Exclusions: No database changes, persistence between sessions, notifications, calendar packages or unrelated changes to booking and cancellation.

- Architecture: Appointment validates and applies the time change. AppointmentService finds the appointment and uses the existing data store’s conflict check, excluding the appointment being moved.

- Acceptance criteria: A move to a free time succeeds, frees the old slot and appears in lookup and the sorted list. A valid same-time request succeeds without changing anything. Invalid IDs or times, scheduling conflicts, and attempts to move cancelled or completed appointments are rejected without changing stored records.

- Definition of done: The focused rescheduling tests, existing common tests and full suite pass. The code and test changes are reviewed separately, and the actual results and decisions are recorded.

Predicted changed files and human test intentions:

I expect changes in project/smartcare/domain.py and project/smartcare/services.py, with new tests in project/tests/test_rescheduling.py. I would test a successful move that preserves identity and frees the old slot, a valid same-time request, rejected requests that leave records unchanged, and lookup and listing that show the new time in the same session.

### B2 Judge every proposed plan step

| Proposed step | Accept / Modify / Reject | Requirement evidence and reason |
|---|---|---|

| Redesign database schema | Reject | `RES-05-R2` only requires the updated time to be visible during the current session. The existing in-memory store is enough. |

| Add notifications | Reject | The rescheduling requirements do not ask for emails, messages or reminders. |

| Introduce calendar library | Reject | SmartCare already validates times using Python’s `datetime`. No new dependency is needed. |

| Modify Patient | Reject | Rescheduling must keep the same patient object. Only the appointment time changes. |

| Add rescheduling | Modify | Keep the feature, but specify the scope: add the time change to `Appointment`, coordinate lookup and conflict checks in `AppointmentService`, reuse the store’s conflict helper, and add focused tests. |

| Rewrite all tests | Reject | Retain the existing 81 baseline tests. Add rescheduling tests alongside them and rerun the full suite. |

### B3 Six proposed changes

| File or action | Expected? | Review concern and evidence needed |
|---|---|---|

| Appointment in project/smartcare/domain.py | Yes | Check that only scheduled appointments can move and that only the time changes. Look for tests showing that invalid times and attempts to move cancelled or completed appointments leave the object unchanged. |

| project/smartcare/services.py | Yes | Check that the service finds the stored appointment and reuses the conflict helper, excluding the appointment being moved. Look for tests showing that another appointment for the same practitioner blocks the move, a valid same-time request succeeds, and the service returns the original object. |

| Proposed sqlite_repository.py or schema change | No | `RES-05-R2` requires visibility during the current session. Check the diff for new storage files or schema changes; neither is needed. |

| Patient fields in project/smartcare/domain.py | No | The domain file can change, but the `Patient` class does not need to. Check that its fields are unchanged and that rescheduling preserves the original patient object. |

| requirements-dev.txt adds a calendar package | No | The existing datetime validator is enough. Check that the dependency list and imports contain no new calendar package. |

| Existing appointment assertions are weakened | No | A passing suite is less useful if its checks were weakened. Compare the test diff with the Stage 9 baseline and confirm that the original assertions are retained and new rescheduling tests are added separately. |

### B4 Approval gate

Agent says “All tests pass.” Give at least SIX distinct checks before approval.

1. Check the scope of the changes. Compare the actual Git diff with the approved plan. Look for unrelated edits to booking, cancellation, the console or dependencies.
2. Check what a successful move changes. Verify that the time changes while the appointment object, ID, patient, practitioner and status stay the same.
3. Check the conflict rules. Confirm that the appointment doesn’t conflict with itself, a valid same-time request succeeds, and another scheduled appointment for the same practitioner at the requested time blocks the move.
4. Check what happens when a move is rejected. Verify that invalid inputs and attempts to move cancelled or completed appointments leave the appointment and stored records unchanged.
5. Check what users see after the move. Confirm that lookup and the sorted list show the new time in the same session, and that the old slot can be booked again.
6. Check the tests themselves. Compare the existing tests with the Stage 9 baseline to make sure no assertions were weakened. Run the focused rescheduling tests, the common tests separately and the full suite yourself. Record the actual results before deciding whether to approve.

### B5 Exit question

Why does increasing AI autonomy increase rather than decrease the importance of software engineering discipline?

An agent that can edit several files and run commands can make a useful change quickly, but it can also change unrelated behaviour or weaken tests. In SmartCare, a rescheduling change might appear to work while breaking cancellation history or modifying the shared data store unnecessarily. Clear requirements, a separate branch, a plan approved before edits, and independent tests help catch those problems. Reviewing the actual changes matters because a passing test count alone does not show what was tested or whether the change stayed within scope. The person approving the change remains responsible for it.

## C Human task specification before AI

- Goal: Allow an existing scheduled appointment to move to a valid new time during the current SmartCare session.

- Requirements RES-01–06 with RES-05-R2: Implement RES-01–RES-06, using RES-05-R2 for session visibility. The service must return the same appointment object. Preserve its ID, patient, practitioner and status; change only its time. A successful move frees the old slot and appears at the correct position in the sorted practitioner list.

- Out of scope: Database or persistence changes, notifications, new dependencies, new console commands, and unrelated changes to patient registration, booking or cancellation.

- Architecture constraints: Add Appointment.reschedule() to validate the new time and guard the state change. Add AppointmentService.reschedule_appointment() to find the stored appointment and reuse the data store’s existing conflict check. Exclude the target appointment by its stored ID. Keep the existing store, query functions and console unchanged.

- Acceptance criteria: A scheduled appointment can move to a free time. A valid same-time request succeeds without changing state. Another scheduled appointment for the same practitioner at the requested time blocks the move; an appointment for a different practitioner does not. A valid unknown ID raises LookupError. Invalid IDs, invalid times, conflicts and attempts to move cancelled or completed appointments raise ValueError. Rejected requests leave the appointment and stored records unchanged.

- Definition of Done: The rescheduling tests, common tests run separately and full suite all pass. Existing test assertions are retained. The production and test diffs are reviewed separately. Record the actual test results and AI-assisted decisions, and obtain independent review before integration.

- Issue / PG owner: https://github.com/u3318026/ST1-Assignment-3-Group-Project/issues/3

- Human expected positive, negative and boundary tests:

Positive: Move a scheduled appointment to a free time. Check that the returned object is the original, its ID and participants are unchanged, lookup and sorted listing show the new time, and the old slot can be booked again.

Negative: Test a valid unknown ID, invalid IDs, invalid datetime values, another scheduled appointment for the same practitioner, and cancelled and completed targets. Check the expected exception and confirm that appointment fields and stored records remain unchanged after each rejection.

Boundary: Request the same time for a scheduled appointment and check that it returns the original object without changing state. Move to a time booked by a different practitioner and check that the move succeeds. Test invalid time inputs separately, including timezone-aware datetimes and times with nonzero seconds or microseconds.

- Allowed files: project/smartcare/domain.py, project/smartcare/services.py and a new project/tests/test_rescheduling.py. Update project/README.md and the Stage 10 evidence record for documentation.

- Forbidden/unnecessary files and changes: Editing the store, queries, console or dependencies; weakening existing tests; adding persistence; or rewriting unrelated code.

- Baseline/recovery link: Branch feature/stage10-rescheduling, created from Stage 9 commit ad62e75f16a38e6ba2e7099391edfe526dff2872. The local baseline returned 81 passing tests.

- Evidence that human analysis preceded agent use: Before starting the Stage 10 agent session, I verified the Stage 9 baseline and completed the Section B exercises on scope, proposed changes and approval checks. I ran ../.venv/bin/python -m pytest -q from project/, which returned 81 passed in 0.07s. I confirmed that main was clean at commit ad62e75f16a38e6ba2e7099391edfe526dff2872 and created feature/stage10-rescheduling from that commit. My terminal output and Sections A and B document this preparation.

## D Agent plan and approval

Actual plan-only prompt/context and response or confirmed equivalent artefacts:

- Tool and mode: GitHub Copilot Chat in VS Code, Ask mode.

- Task: GitHub Issue #3 — Add appointment rescheduling to SmartCare.

- Context provided: `stage10_pg/stage10_activities_and_evidence.md`, including Section C.

- Prompt sent:

Prepare a plan only for Stage 10, Issue #3: Add appointment
rescheduling to SmartCare. Use Section C of stage10_pg/stage10_activities_and_evidence.md as the task specification. Inspect the existing domain, service, data store and tests to check how the feature fits. For each planned change, list the requirement it addresses, the exact file, why the change is needed and how to test it. Include separate runs for the focused, common and full test suites. Preserve the existing common tests and identify any
questions or changes outside the approved scope. Do not edit files or run terminal commands. Stop after presenting the plan and wait for my review and approval.

- Copilot response:

I’ll read Section C and map the existing appointment domain, service, store, and test coverage before outlining the plan.

Read , lines 1 to 248
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/stage10_pg/stage10_activities_and_evidence.md",
  "view_range": [
    1,
    248
  ]
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3"
}

Read , lines 95 to 248
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/stage10_pg/stage10_activities_and_evidence.md",
  "view_range": [
    95,
    248
  ]
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/smartcare"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests"
}

Section C explicitly limits implementation to the domain and service layers, with a new focused test file; the store and console must stay untouched. I’m checking current APIs and test conventions to make the plan concrete.

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/smartcare/domain.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/smartcare/services.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/smartcare/data_store.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/smartcare/queries.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_domain.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_services.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_regressions.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/README.md"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/requirements-dev.txt"
}

Read , lines 1 to 260
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_services.py",
  "view_range": [
    1,
    260
  ]
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_workflows.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_queries.py"
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_starter.py"
}

Read , lines 1 to 240
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_regressions.py",
  "view_range": [
    1,
    240
  ]
}

Search for `RES-0|RES-05|reschedul|common|81 passed|test_rescheduling`

Read , lines 155 to 230
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests/test_services.py",
  "view_range": [
    155,
    230
  ]
}

Read , lines 218 to 248
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/stage10_pg/stage10_activities_and_evidence.md",
  "view_range": [
    218,
    248
  ]
}

Read , lines 1 to 90
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/smartcare/console.py",
  "view_range": [
    1,
    90
  ]
}

Read
Completed with input: {
  "path": "/Users/tahmid/Documents/st1-assignment-3/project/tests"
}

## Proposed plan — Stage 10, Issue #3: Add appointment rescheduling

This follows Section C of the `Stage 10 activity and evidence record`. **No files were edited and no commands were run.**

| Planned change | Requirement addressed | Exact file | Why it is needed | How to test |
|---|---|---|---|---|
| Add `Appointment.reschedule()` to validate the proposed datetime, reject non-scheduled appointments, and change only the appointment time. | RES-01, RES-02, RES-06; invalid-time and unchanged-on-rejection criteria | `domain.py` | The domain owns appointment state and already centralizes datetime validation and guarded state transitions. Keeping the change here preserves the same appointment object, ID, participants, and status. | Focused tests should cover a valid move, identity and unchanged fields, invalid datetime inputs (including timezone-aware, seconds, and microseconds), and cancelled/completed appointments. Assert failed calls leave the object unchanged. |
| Add `AppointmentService.reschedule_appointment()` to find the stored appointment, check conflicts with the existing store helper while excluding the target’s stored ID, then delegate the change to the domain. Return the original appointment. | RES-02, RES-03, RES-04, RES-05-R2; same-time, different-practitioner, and rejection criteria | `services.py` | The service coordinates lookup and store-level conflict rules. Excluding the target avoids a self-conflict on same-time requests; using the existing store keeps conflict logic consistent with booking. | Focused service tests should cover a free-time move, same-time no-op, same-practitioner conflict, different-practitioner allowance, valid unknown ID (`LookupError`), invalid IDs (`ValueError`), and unchanged store records after rejection. Check lookup and sorted listing show the new time, and that the old slot can be booked again. |
| Add rescheduling-specific domain and service tests without changing existing tests. | All RES-01–06 / RES-05-R2 acceptance scenarios | `new test_rescheduling.py` | A separate test module provides a focused run and preserves the existing common tests and their assertions. Include positive, negative, boundary, and failed-state snapshot checks. | Run the focused suite below; review its assertions separately from production changes. |
| Update the README’s feature/limitations description to reflect session-only rescheduling and retain the existing no-persistence limitation. | RES-05-R2 and approved documentation scope | `README.md` | It currently says rescheduling is not included; that would be inaccurate after the feature is added. | Review the README diff for accuracy and scope; no separate automated test is needed. |
| Record the approved plan, actual reviewed changes, and actual test outcomes in the Stage 10 evidence record after implementation and verification. Do not pre-fill results. | Section C Definition of Done and evidence requirements | `stage10_activities_and_evidence.md` | The record requires separate production/test review and actual focused, common, and full-suite results. Results must reflect runs that actually occurred. | Check the updated record against the reviewed diff and real test output; do not record planned or assumed results as actual. |

### Planned test runs

Run each separately from `project/`, after implementation:

```sh
# Focused rescheduling tests
../.venv/bin/python -m pytest -q tests/test_rescheduling.py
```

```sh
# Existing common tests only; preserve these files and assertions
../.venv/bin/python -m pytest -q \
  tests/test_domain.py tests/test_queries.py tests/test_regressions.py \
  tests/test_services.py tests/test_starter.py tests/test_workflows.py
```

```sh
# Full cumulative suite, including the new rescheduling tests
../.venv/bin/python -m pytest -q
```

The record reports 81 passing tests at the protected Stage 9 baseline. These are **planned runs**, not results from this review.

### Scope boundaries and review points

Keep the data store, query functions, console, dependencies, patient fields, booking, and cancellation behavior unchanged. Do not add persistence, notifications, new console commands, or unrelated cleanup. Do not weaken or rewrite existing tests; compare their diff with the Stage 9 baseline.

Section C permits the README and evidence-record updates listed above, in addition to the three implementation/test files. No further scope question appears to block this plan. I’ll wait for your review and approval before any edits or test runs.


- Observed Copilot actions: Copilot read the Stage 10 evidence file,
inspected the domain, service, store, queries and tests, and searched the
project for rescheduling requirements. It proposed a plan and reported
that no files were edited and no terminal commands were run.

| Plan step / action | Requirement link | Reason | Expected files | Accept / Modify / Reject | Conditions / evidence |

| Add the appointment method | `RES-01`, `RES-02`, `RES-06` | Keep the rules for changing an appointment inside `Appointment`. | `project/smartcare/domain.py` | Accept | Validate the time and require `SCHEDULED` status before changing anything. A valid same-time request leaves state unchanged. |

| Add the service method | `RES-02`–`RES-04`, `RES-05-R2` | Coordinate lookup and conflict checks using the existing store. | `project/smartcare/services.py` | Accept with condition | Validate the time before the conflict check. Exclude the target by its stored ID and return the original object. |

| Add focused tests | `RES-01`–`RES-06`, including `RES-05-R2` | Verify successful moves, rejected moves and session visibility. | `project/tests/test_rescheduling.py` | Accept | Assert that rejected requests leave records unchanged. Keep the existing tests intact. |

| Update the README | `RES-05-R2` | Explain what rescheduling supports. | `project/README.md` | Accept | Describe rescheduling as available during the current session only. |

| Record the evidence | Section C definition of done | Keep the approval, review and results traceable. | `stage10_pg/stage10_activities_and_evidence.md` | Modify | Record approval before edits. Record diff reviews and actual test results afterwards. |

Approved bounded scope / forbidden changes / verification plan: On feature/stage10-rescheduling, Copilot may add Appointment.reschedule() in project/smartcare/domain.py, add AppointmentService.reschedule_appointment() in project/smartcare/services.py, and create project/tests/test_rescheduling.py. Validate the new time before checking for conflicts and exclude the appointment being moved by its stored ID. Do not change the store, queries, console, dependencies, existing tests or unrelated behaviour. README and evidence updates will be handled separately. After implementation, I will review the production and test diffs separately, then run the focused rescheduling tests, the existing common tests and the full suite from project/.

Human plan approver and approval before edits: I, Md Tahmid Ul Islam Tonmoy, reviewed the Copilot Ask mode plan for Issue #3, recorded above in Section D. I approved the plan before any implementation edits, subject to the approved file scope and verification plan. My approval requires validating the new appointment time before checking for conflicts, excluding the appointment being moved by its stored ID, and keeping all existing tests unchanged.

Tool permissions and any expanded-scope requests / decision: Copilot’s planning response shows file reads and searches. It reported no file edits or terminal commands.” For Human plan approver, enter your name and actual approval only once you’ve reviewed the plan and agreed to the conditions.

## E Production diff review

Actual proposal / branch diff / version reviewed: [Issue #3](https://github.com/u3318026/ST1-Assignment-3-Group-Project/issues/3). I reviewed the revised local diff on `feature/stage10-rescheduling` against Stage 9 commit `ad62e75f16a38e6ba2e7099391edfe526dff2872`. The reviewed changes were uncommitted.

| File | Change purpose and reason | Requirement / test link | Expected? | Architecture OK? | Decision | Notes / correction |
|---|---|---|---|---|---|---|

| `project/smartcare/domain.py` | Add `Appointment.reschedule()` so a scheduled appointment can change time without replacing the object. | `RES-01`, `RES-02`, `RES-06`; see the identity, invalid-time and same-time tests in Section F. | Yes | Yes. The domain object owns validation and the state change. | Accepted after correction | I confirmed the parameter is `new_date_time`. The method validates the time and checks `SCHEDULED` status before returning early for a same-time request. Only a different valid time is assigned. |

| `project/smartcare/services.py` | Add `AppointmentService.reschedule_appointment()` to coordinate lookup, conflict checking and the move. | `RES-02`–`RES-04`, `RES-05-R2`; see the lookup, conflict and listing tests in Section F. | Yes | Yes. The service reuses the store's conflict helper and delegates the time change to the appointment. | Accepted after correction | I confirmed the parameter is `new_date_time`. The service validates the time before checking for conflicts, excludes the target by its stored ID and returns the original appointment. |

Every changed file inspected, including new/untracked files: I reviewed the revised production diff using `git --no-pager diff HEAD -- project/smartcare/domain.py project/smartcare/services.py`. I read the revised untracked `project/tests/test_rescheduling.py` separately for Section F. The remaining modified file was this evidence record, which contains my documentation edits.

Unexpected changes, scope creep, secrets/dependencies/configuration, unrelated cleanup: `git status` listed only the two approved production files, the new test file and this evidence record. The reviewed production diff showed no secrets, dependency or configuration changes, or unrelated cleanup. The store, queries and console were unchanged.

## F Separate test review

| Test | Criterion | Actual assertion | Assertion meaningful / adequate? | Agent changed expected behaviour? | Human or agent authorship | Decision and reason |
|---|---|---|---|---|---|---|

| Successful move and identity | `RES-01`, `RES-02` | The service returns the stored object, with the same ID, patient, practitioner and status, and the requested new time. The call uses `new_date_time=`. | Yes | No | Copilot-generated; human-reviewed | Accept. The identity checks would detect replacement of the appointment or its participants. |

| Same-time request and conflict rules | `RES-04`, `RES-06` | The same-time request returns the original object and preserves state. A booking for a different practitioner does not block the move; a booking for the same practitioner does, without changing the target. | Yes | No | Copilot-generated; human-reviewed | Accept. The tests distinguish a self-conflict, a permitted move and a genuine conflict. |

| Invalid IDs, times and states | `RES-03`, `RES-06`; datetime validation | An unknown valid ID raises `LookupError`. Invalid IDs, invalid times and cancelled or completed targets raise `ValueError`. The tests check unchanged state after rejection. The invalid-time service test also checks that the conflict helper was not called. | Yes | No | Copilot-generated; human-reviewed | Accept. The tests check the error, the relevant state after failure and the required order of validation. |

| Lookup, sorted listing and old-slot reuse | `RES-05-R2`; successful old-slot reuse | Before the move the list is `A0, A1, A3`. After moving `A1` to 12:00, lookup returns the same object with the new time, the list is `A0, A3, A1`, and a new booking succeeds at the old time. | Yes, after correction | No. The assertion was strengthened to detect incorrect ordering. | Copilot-generated; strengthened after human review | Accepted after correction. The initial test kept the same order before and after the move. I requested a move past `A3` and confirmed the revised assertions in the file. |

Comparison with original common tests / any proposed weakening: `git --no-pager diff HEAD -- project/tests` returned no output. The existing tracked tests and their assertions were unchanged; the Stage 10 cases were added in the new `project/tests/test_rescheduling.py` file.

Independent human checks and corrections: I reviewed the revised assertions separately from the production code and ran the focused, common and full suites myself. Results: 16 focused, 81 common and 97 full tests passed. See Section G for the commands and timings.

## G Actual verification

| Requirement / acceptance scenario | Test or demonstration | Meaningful expected result | Actual result | Evidence / version |
|---|---|---|---|---|

| RES-01 / AC-RES-01 successful move | Successful move and identity test | A scheduled appointment moves to a free time. | Passed: the appointment time changed to the requested time. | `project/tests/test_rescheduling.py`; local Stage 10 run |

| RES-02 same object and participant identities | Successful move and identity test | The original appointment is returned with the same ID, patient, practitioner and status. | Passed: the returned and stored objects were the original appointment, with those fields preserved. | Same focused run |

| RES-03 / AC-RES-02 unknown and invalid IDs | Unknown-ID and invalid-ID tests | An unknown valid ID raises `LookupError`; an invalid ID raises `ValueError`. | Passed: both errors were distinguished and the checked stored state remained unchanged. | Same focused run |

| RES-04 / AC-RES-03 conflicting practitioner | Conflicting reschedule test | Another scheduled appointment for the same practitioner at the requested time blocks the move. | Passed: the service raised `ValueError` and preserved the target's original state. | Same focused run |

| AC-RES-04 different practitioner allowed | Different-practitioner test | A booking at the new time for a different practitioner does not block the move. | Passed: the target moved successfully. | Same focused run |

| RES-06 / AC-RES-05 cancelled and completed | Non-scheduled appointment test | Both cancelled and completed appointments are rejected without a time or status change. | Passed for both statuses. | Same focused run |

| RES-05-R2 / AC-RES-06-R2 lookup and listing order | Lookup, sorting and old-slot reuse test | Lookup shows the new time and the list is reordered during the same session. | Passed: lookup showed 12:00 and the list changed from `A0, A1, A3` to `A0, A3, A1`. | Same focused run |

| Self-exclusion and same-time no-op | Same-time request test | The appointment does not conflict with itself; the request returns the same object and preserves state. | Passed: the same-time request succeeded and the before-and-after state comparison matched. | Same focused run |

| Invalid datetime and failed-state snapshots | Domain invalid-time tests and service validation-order test | Invalid time values raise `ValueError` without mutation. The service validates time before checking conflicts. | Passed: invalid values were rejected; the service test confirmed that the conflict helper was not called for the invalid time. | Same focused run |

| Successful old-slot reuse | Lookup, sorting and old-slot reuse test | A new booking can use the original slot after the appointment moves. | Passed: a new appointment was stored at the original time. | Same focused run |

| Suite | Command / working directory | Code SHA | Actual count and result | Evidence |
|---|---|---|---|---|
| Focused PG | From `project/`: `../.venv/bin/python -m pytest -q tests/test_rescheduling.py` | Uncommitted Stage 10 changes on `feature/stage10-rescheduling` | 16 passed in 0.03s | Local terminal output |
| Common independently | From `project/`: `../.venv/bin/python -m pytest -q --ignore=tests/test_rescheduling.py` | Same uncommitted Stage 10 changes | 81 passed in 0.04s | Local terminal output |
| Full cumulative | From `project/`: `../.venv/bin/python -m pytest -q` | Same uncommitted Stage 10 changes | 97 passed in 0.04s | Local terminal output |
| Integrated retest | From `smartcare-stage10-retest/project/`: `../../st1-assignment-3/.venv/bin/python -m pytest -q` | `fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc` | 97 passed in 0.12s | Local terminal output; [PR #4](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/4) |



Failures / diagnosis / corrections and reruns / unresolved concerns: The review identified two production corrections and a weak list-order assertion, documented in Sections E and F. I inspected the revised files. The focused, common and full local suites all passed after the corrections. The integrated retest is pending until the changes are merged.

## H Decisions corrections and independent review

| Significant agent action | Human review and evidence | Accept / Modify / Reject and reason | Manual correction or recovery | Recheck evidence |
|---|---|---|---|---|
| Copilot added the domain and service rescheduling methods. | I inspected the production diff and checked both methods against the handout and approved scope. | Modify, then accept. The parameter names needed to match the handout, and a valid same-time request needed to return without reassigning the time. | I requested both corrections; Copilot applied them. | The revised diff showed `new_date_time` in both methods and the early return after validation and the scheduled-status check. |
| Copilot added the focused rescheduling tests. | I reviewed the tests separately and found that the original listing test expected the same order before and after the move. | Modify, then accept. The test needed to detect an actual change in order. | I asked Copilot to move `A1` past `A3` in the test and assert the new order while keeping the old-slot reuse check. | The revised test checks `A0, A1, A3` before the move and `A0, A3, A1` afterwards. See Section G for the passing test runs. |

Final proposal decision: Accepted after modification

Evidence supporting decision: I inspected the revised production diff and the new test file. Both methods now use new_date_time, a valid same-time request returns without changing the stored time, and the revised listing test checks that rescheduling actually changes the order. The focused, common and full local test suites passed.

If rejected, how the required feature was subsequently completed and verified: [response or not applicable]
Saved proposal and targeted recovery details if needed: [response or not applicable]
Human explanation of every changed method and limitations: Appointment.reschedule() validates the new time and allows only scheduled appointments to move. A valid same-time request returns without changing the stored time. AppointmentService.reschedule_appointment() finds the stored appointment, validates the time before checking for practitioner conflicts, excludes the appointment’s own ID from that check, and delegates the change to the domain method. The same appointment object is returned. Rescheduling is available through the service during the current session only; the console and persistence behaviour are unchanged.

Another PG / willing UG / tutor reviewer, actual PR/diff review and feedback: [PR #4 — Stage 10 rescheduling](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/4). Collaborator `BlackJack2180` commented, “All the tests ran.” `u3318026` then merged the PR into `main` at commit `fbad1d2`. No formal approval is visible in the PR timeline.

Corrections, recheck and actual approval before integration: I requested three corrections: use new_date_time in both method signatures, make a same-time request an explicit no-op, and strengthen the listing test so it detects a change in order. I inspected the revised production and test files and accepted the proposal after modification. The local runs passed with 16 focused, 81 common and 97 full tests. On PR #4, collaborator BlackJack2180 commented, “All the tests ran.” u3318026 then merged the PR. No formal reviewer approval is visible in the timeline. The integrated retest passed all 97 tests at fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc.
Integrated PG SHA / common protected SHA: fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc
Each assessed PG member's implementation, supervision and test contribution: [response and links]
Optional UG help, acknowledged separately: [response or none]

## I Four reflections

1. Which agent change had the greatest blast radius? The service method, AppointmentService.reschedule_appointment(), had the widest potential impact. It coordinates appointment lookup, time validation and practitioner conflict checking. A mistake there could allow overlapping bookings, block a valid move or change an appointment before rejecting the request.
2. Did the plan predict it? Yes. The plan identified the service as the place to reuse the existing conflict check and exclude the appointment being moved. During review, I also checked that the new time was validated before checking for conflicts and that the method returned the original appointment.
3. What did you reject or manually correct? I did not manually edit the code or reject the whole proposal. During review, I asked Copilot to make three corrections: rename the time parameter to new_date_time in both methods to match the handout, make a valid same-time request return without reassigning the stored time, and strengthen the listing test so the rescheduled appointment actually changes position. Copilot applied the edits. I inspected the revised files and accepted the changes after the focused, common and full test suites passed.
4. What evidence justified final approval? I accepted the changes after inspecting the revised production and test files. The revised test showed that moving A1 changed its position in the list and allowed the old slot to be booked again. The 16 focused tests, 81 common tests and 97 full-suite tests passed locally. After PR #4 was merged, the full suite passed again at the merge commit. These results support my technical decision; the PR timeline does not show a formal reviewer approval.

## J Ten formative questions

1. What is the difference between an AI assistant and an engineering agent? An AI assistant gives advice or drafts for me to apply. An engineering agent can use tools to inspect the repository, edit files or run commands within the permissions I give it.
2. What is the simplified agent loop used in Stage 10? Define the task and its limits, ask for a plan, review and approve the plan, allow the agreed edits, then inspect the diff and run the tests. If anything is wrong, request a correction and verify it before accepting the change.
3. Why should an agent plan be reviewed before repository edits begin? Reviewing the plan lets me catch misunderstandings before they become code changes. For Stage 10, I checked that the plan reused the existing conflict check and left the store, queries and console alone.
4. What is meant by the blast radius of a software change? It is the range of files, features and users that a change could affect. The rescheduling service had the widest potential impact because a mistake in its conflict check could affect which appointments are allowed.
5. Why is diff review essential for agentic changes? The diff shows what the agent actually changed. I can compare it with the approved plan and spot unrelated edits, missing validation or weakened tests even if the suite passes.
6. What is a human approval gate? It is a point where the agent must stop until a person reviews the work and decides whether it can proceed. In Stage 10, I approved the plan before allowing edits and reviewed the resulting changes before accepting them.
7. What is test accommodation and why is it dangerous? Test accommodation means changing a test to accept the implementation’s behaviour without checking whether that behaviour meets the requirement. It can make a faulty change look correct. I asked for the listing test to require a real change in order, so it would catch a failure to reorder the appointment.
8. What is rollback in the context of agentic software engineering? Rollback means restoring a known good version if an agent’s changes are unsuitable. A separate branch and a recorded baseline make it possible to discard or revert the unwanted changes while preserving other work.
9. Who remains accountable for accepted agentic changes? The human who accepts the changes remains accountable. The agent can propose and implement a change, but I must understand it, verify it and explain why it meets the requirements.
10. What is the Stage 10 engineering rule? Give the agent a clear, limited task. Approve the plan before edits, check the code and tests separately, and accept the change only when the evidence supports it.


## K Completion and Stage 11 handover

- [ ] Common Stage 9 checkpoint protected; UG pathway unaffected.
- [ ] RES-01–06 and RES-05-R2 implemented in the same project.
- [ ] Domain/service boundaries, current exceptions and coding standard preserved.
- [ ] Positive/negative/boundary cases and failed-state checks verified.
- [ ] Common tests remain valid and independently passing; full suite passes.
- [ ] Plan reviewed before bounded actions; every file and test diff inspected.
- [ ] Actual agent route, decisions, corrections and rechecks recorded honestly.
- [ ] No unrelated features, persistence, dependencies or staff solutions introduced.
- [ ] Another-member or tutor review and integrated retest complete.
- [ ] Tutorial, four reflections, ten formative responses and PG contributions complete.
- [ ] Each PG member can explain their code and supervision.
- [ ] README PG note, actual integrated SHA and limitations recorded.

Unresolved issues / owner / action: No implementation or test failures remain from the Stage 10 integrated retest. The PR records a collaborator’s test comment and the merge, but no formal approval is visible. Owner: Md Tahmid Ul Islam Tonmoy. If separate review evidence is required, obtain and link the reviewer’s actual feedback in Section H.
Stage 11 handover references to extension, tests, dependencies and actual AI/review evidence: Stage 11 starts from the integrated Stage 10 work in PR #4. Rescheduling is implemented in project/smartcare/domain.py and project/smartcare/services.py, with focused tests in project/tests/test_rescheduling.py and usage documented in project/README.md. No dependency changes were introduced. Section D records the Copilot plan and scope approval, Sections E–F record the code and test reviews, Section G records the test runs, and Section H records the review and integration evidence.
Submitted SHA / explanation if later than tested code: Integrated code tested: fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc — 97 passed in 0.12s. Submitted evidence SHA is pending. The evidence update is being prepared separately on docs/stage10-evidence.
Stage 11 materials are supplied from the beginning. Begin Stage 11 only after Stage 10 has been integrated, verified and recorded. UG follows the protected common code from Stage 9 to Stage 12.
