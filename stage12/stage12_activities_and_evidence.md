# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Group 6 / Wednesday 2.30 pm - 4.30 pm
Members and UG/PG applicability: Tamas Szucs (UG), Ryan Grieves (UG) and Md Tahmid Ul Islam Tonmoy (PG).



## A Release scope and starting SHA

Release label/version and requirements baseline: SmartCare Stage 12 release candidate. Requirements baseline: SmartCare A3 2026 revision 2. Final release version: pending.

Common starting SHA / branch / applicable members: The protected Stage 9 checkpoint is `ad62e75f16a38e6ba2e7099391edfe526dff2872`. Use this exact commit for the UG/common release scope.

PG starting SHA / branch / applicable members: `0372fd825e5de483f2f735b01f8144b1e232a42a`. The `release/stage12` branch was created from `origin/main` at this commit. This is the starting point for the PG extended scope.

Working-state review and approved integration: The working tree was clean when `release/stage12` was created from `origin/main`. Stage 10 rescheduling was integrated at `fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc`, and Stage 11 assurance was integrated at `94c7f244cf3dd1e995287966516bbb5bc2e7b792`. The review and retest records were updated on `main` in `19f1a4c` for Stage 10 and `0372fd825e5de483f2f735b01f8144b1e232a42a` for Stage 11.

Protected common candidate and PG differences: The common candidate is the protected Stage 9 checkpoint. The PG candidate includes the common workflows plus Stage 10 appointment rescheduling and Stage 11 assurance tests and evidence.

Feature freeze / owner / verifier: No new features are planned for Stage 12. Release preparation owner: Md Tahmid Ul Islam Tonmoy. Release verifier: pending confirmation.


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify:

**Decision: Release with conditions.** Passing tests supports the behaviour covered by the suite, but the release is not ready yet. Complete the README setup instructions and verify them from a fresh copy, review the dependency and record the decision, and document the known limitation. Release only after all three conditions are met.

Tutorial activity 2 and actual readiness matrix:

- Protected common starting SHA: `ad62e75f16a38e6ba2e7099391edfe526dff2872`.
- PG starting SHA: `0372fd825e5de483f2f735b01f8144b1e232a42a`.
- The links below point to repository files. Sections C and D record the tested SHAs and observed results.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works — common, FR-06–08 | The service tests and Stage 09 evidence provide prior coverage for cancellation and lookup. | [Service tests](../project/tests/test_services.py); [Stage 09 evidence](../stage09/stage09_activities_and_evidence.md). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Demonstrate that a cancelled appointment remains findable with status `CANCELLED`. |
| Architecture responsibilities are appropriate — common and PG | The console handles input and output, services coordinate workflows, the domain enforces appointment rules, the store holds session data, and queries select and order appointments. | [Project README](../project/README.md); [SmartCare modules](../project/smartcare). | Stage 12 verifier pending. | Responsibilities identified; release review pending. | Confirm these boundaries in the release candidate and check that PG rescheduling stays in the domain and service layers. |
| Rescheduling is safe — PG only, RES-01–06 including RES-05-R2 | Stage 10 recorded 16 focused cases covering identity preservation, conflict rejection without mutation, listing order and reuse of the old slot. | [Rescheduling tests](../project/tests/test_rescheduling.py); [Stage 10 evidence](../stage10_pg/stage10_activities_and_evidence.md); integrated SHA `fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc`. | Stage 10 review documented; Stage 12 verifier pending. | Prior evidence available; release verification pending. | Rerun the focused rescheduling suite on the PG release candidate. |
| AI use is responsible — common recheck / PG assurance | Stage 09 records the Copilot prompt and output. Stage 11 records the human review, assurance tests, and privacy and provenance limitations. | [Stage 09 prompt](../stage09/Copilot_Prompt.md); [Stage 09 output](../stage09/Copilot_Output.md); [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md); integrated SHA `94c7f244cf3dd1e995287966516bbb5bc2e7b792`. | Stage 11 review documented; Stage 12 verifier pending. | Prior evidence available; release recheck pending. | Confirm the release preserves the AI evidence and documents the remaining limitations. |
| System is maintainable — common and PG | The revised README commands worked in a fresh post-merge worktree: dependencies installed, both launch modes worked and 100 tests passed. | [Project README](../project/README.md); Section F. | Md Tahmid Ul Islam Tonmoy | Local setup verified. | Independent reproduction by another verifier has not been confirmed. |
| FR-01–03 registration, lookup and validation — common | Domain and service tests provide prior evidence for registration, lookup and validation. | [Domain tests](../project/tests/test_domain.py); [Service tests](../project/tests/test_services.py). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Rerun the common suite and demonstrate registration, lookup and invalid input handling with synthetic records. |
| FR-04–05 booking and conflict rules — common | Service and workflow tests provide prior evidence for booking and conflict handling. | [Service tests](../project/tests/test_services.py); [Workflow tests](../project/tests/test_workflows.py). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Verify that a same-time booking for the same practitioner is rejected and a same-time booking for a different practitioner is allowed. |
| FR-06–08 cancellation, history and lookup — common | The service tests and Stage 09 evidence cover the cancellation and lookup workflows. | [Service tests](../project/tests/test_services.py); [Stage 09 evidence](../stage09/stage09_activities_and_evidence.md). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Verify that cancellation retains the appointment, lookup still finds it, and a second cancellation is rejected. |
| FR-09 and QRY/FP listing, filtering, ordering and purity — common | The query tests and Stage 09 evidence provide prior coverage for appointment listings. | [Query tests](../project/tests/test_queries.py); [Query implementation](../project/smartcare/queries.py); [Stage 09 evidence](../stage09/stage09_activities_and_evidence.md). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Rerun the query tests and verify that filtering and ordering leave the stored appointments unchanged. |
| UI full console sequence and error recovery — common | The console demo verified registration, lookup, booking conflicts, cancellation, filtering and error recovery. The post-merge check also verified that the menu opened and exited normally. | [Workflow tests](../project/tests/test_workflows.py); Sections D and F. | Md Tahmid Ul Islam Tonmoy | Detailed demo and post-merge launch check completed. | Formal accessibility was not assessed. |
| Session-only scope / FR-10 retired — common and PG | Appointment data is held in the in-memory store for the current session. FR-10 persistence is outside the release scope. | [Data store](../project/smartcare/data_store.py); [Project README](../project/README.md). | Stage 12 verifier pending. | Scope identified; release check pending. | Verify that records are available in the current session and that the README clearly states they are not retained after exit. |
| PG RES and assurance integration — PG only | The post-merge PG suite passed 100 tests in 0.09s, including the rescheduling and assurance tests. | Section C; tested SHA `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224`. | Md Tahmid Ul Islam Tonmoy | Post-merge regression passed. | Compare the submission commit with the tested SHA before packaging. |
## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | macOS; Python 3.12.10; pytest 8.3.5 | From `smartcare-stage12-common/project/`: `../../st1-assignment-3/.venv/bin/python -m pytest -q` | `ad62e75f16a38e6ba2e7099391edfe526dff2872` | 81 passed in 0.07s | Stage 12 local terminal output; protected common commit |
| Complete PG | macOS; Python 3.12.10; pytest 8.3.5 | From `smartcare-stage12-pg/project/`: `../../st1-assignment-3/.venv/bin/python -m pytest -q` | `0372fd825e5de483f2f735b01f8144b1e232a42a` | 100 passed in 0.10s | Stage 12 local terminal output; PG starting commit |
| Affected focused checks after correction | Not applicable at this point | No correction was needed after these runs. | — | Not run | — |
| Full integrated recheck | macOS; Python 3.12.10; pytest 8.3.5 | From `smartcare-stage12-main-check/project/`: `.venv/bin/python -m pytest -q` | `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224` | 100 passed in 0.09s | Local terminal output from a fresh detached worktree after PR #7 merged |

Pre-integration candidate recheck: At `ed5000f91e80f9ff328e23873eb2a3a97d88b5cb`, I ran `.venv/bin/python -m pytest -q` from `smartcare-stage12-candidate/project/`. Result: 100 passed in 0.16s.

Prior assertions preserved / reviewed test diff: Stage 11 recorded that its assurance tests were added in a separate file without replacing earlier assertions. Both Stage 12 suites passed on the commits listed above. See the [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md).

Remaining failure / limitation: No failures were observed in either regression run. The documented console limitation still applies: patient lookup displays the patient ID and name twice. The console demonstration is complete and recorded in Section D


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | Synthetic patient `P001` and practitioners `PR001` and `PR002`. | Clinic staff need to book, find, cancel and list appointments. Patients and practitioners need accurate appointment details and status. | The demo exercised the scheduling workflow using synthetic records only. | Local Stage 12 console output. |
| Register and find Patient and two Practitioners | Register and find Alex Demo (`P001`), Morgan Demo (`PR001`) and Taylor Demo (`PR002`). | Registered records can be retrieved by ID (FR-01–03). | All three records were registered and found across the demo runs. Patient lookup displayed the ID and name twice. | Local Stage 12 console output. |
| Valid booking | Book `A001` for `P001` with `PR001` at `2001-03-01 10:00`. | A valid booking creates a scheduled appointment (FR-04). | `A001` was booked and displayed as `Scheduled`. | Local Stage 12 console output. |
| Same practitioner exact-time conflict rejected | Try to book `A002` for `PR001` at the same time as `A001`. | Reject an exact-time conflict for the same practitioner (FR-05). | `A002` was rejected because `PR001` already had a scheduled appointment at that time. | Local Stage 12 console output. |
| Different practitioner same time allowed | Book `A003` for `P001` with `PR002` at the same time. | A booking for another practitioner is allowed (FR-05). | `A003` was booked and displayed as `Scheduled`. | Local Stage 12 console output. |
| Cancel SCHEDULED and retain/find CANCELLED object | Cancel `A001`, then find it by ID. | Cancellation changes the status and preserves the appointment for lookup (FR-06–08). | Cancellation succeeded; lookup still found `A001` as `Cancelled` with the original details. | Local Stage 12 console output. |
| Invalid/repeated cancellation rejected | Try to cancel `A001` again. | Only scheduled appointments can be cancelled (FR-06–08). | The second cancellation was rejected and the menu returned. | Local Stage 12 console output. |
| Default all-status listing | List `PR001` with a blank filter after adding `A004` at `09:00`. | A blank filter lists all statuses in appointment-time order (FR-09). | The list showed `A004` at `09:00` as `Scheduled`, followed by `A001` at `10:00` as `Cancelled`. | Local Stage 12 console output. |
| Explicit filtering / empty vs unknown / deterministic order | List `PR001` with `cancelled` and `completed`; list `PR999` with no filter. | Apply the requested status, distinguish no matches from an unknown practitioner, and keep the default list ordered (FR-09). | `cancelled` returned only `A001`; `completed` returned no matches; `PR999` returned a practitioner error. The default list showed the earlier appointment first even though it was booked later. | Local Stage 12 console output. |
| Invalid date/status/menu/lookup recovery and continued operation | Try `10.00` in the time field, the filter `invalid`, menu choice `9`, and an unknown practitioner ID. | Reject invalid inputs and allow the user to continue. | The console displayed errors and returned to the menu. It accepted the corrected time `10:00`, and lookup still found `A001` as `Cancelled` after the later errors. | Local Stage 12 console output. |
| Session-only limitation and normal exit | Select option `0`. | Exit normally and report that session data is discarded; persistence is out of scope. | The console printed “Goodbye. Session data discarded.” and returned to the shell. | Local Stage 12 console output; [Project README](../project/README.md). |
| One meaningful requirement-linked pytest test explained | `test_rescheduled_time_is_visible_sorted_and_old_slot_is_reusable` | A successful reschedule must update lookup and listing order in the same session and free the old slot (RES-05-R2). | The test moves an appointment past another booking, checks the changed listing order, and books the old slot again. It would catch an implementation that changed the time without updating how the service lists appointments. The Stage 12 PG suite passed all 100 cases. | [Rescheduling tests](../project/tests/test_rescheduling.py); Section C. |
| Architecture and one actual AI decision / known limitation | Console demonstration plus Stage 11 assurance review. | Keep rescheduling in the domain and service layers and preserve earlier tests. | Stage 11 placed the AI-assisted assurance checks in a separate test file and preserved the earlier tests. The duplicate patient ID/name display remains a documented console limitation. | [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md); [Assurance tests](../project/tests/test_assurance.py). |
| PG reschedule identity/participants/time and no-op | Service tests for a valid move and a request for the original time. | Preserve appointment and participant identity; a valid same-time request leaves state unchanged. | These cases passed in the Stage 12 PG suite. | [Rescheduling tests](../project/tests/test_rescheduling.py); Section C. |
| PG conflict/invalid status/failure non-mutation | Service tests for practitioner conflicts and requests involving cancelled or completed appointments. | Reject invalid rescheduling requests without changing the appointment. | These cases passed, including same-time requests for cancelled and completed appointments. | [Rescheduling tests](../project/tests/test_rescheduling.py); [Assurance tests](../project/tests/test_assurance.py); Section C. |
| PG old slot / current lookup/list ordering / assurance risks | Service tests for old-slot reuse, updated lookup and ordering, and whitespace-only patient IDs. | Make the new time visible in the current session, free the old slot, and reject invalid patient IDs. | These cases passed in the Stage 12 PG suite. | [Rescheduling tests](../project/tests/test_rescheduling.py); [Assurance tests](../project/tests/test_assurance.py); Section C. |

Stable demo owner / fresh process / command: Md Tahmid Ul Islam Tonmoy. Ran the console in fresh processes from `smartcare-stage12-pg/project/` at `0372fd825e5de483f2f735b01f8144b1e232a42a` using `../../st1-assignment-3/.venv/bin/python main.py --interactive`. Only synthetic records were used.

PG demonstrations through service/tests or not applicable: PG rescheduling was verified through service and domain tests in `test_rescheduling.py` and `test_assurance.py`, not through the interactive menu. The full PG suite passed 100 tests in 0.10s at the same SHA.


## E Final code quality and AI review

Code reviewed at PG starting SHA `0372fd825e5de483f2f735b01f8144b1e232a42a`, compared with the protected common SHA `ad62e75f16a38e6ba2e7099391edfe526dff2872`.

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [Domain](../project/smartcare/domain.py), [services](../project/smartcare/services.py), [store](../project/smartcare/data_store.py), [queries](../project/smartcare/queries.py), and [query tests](../project/tests/test_queries.py). | `Appointment` owns status and time changes. `AppointmentService` coordinates lookup and conflict checking. The common query module remains separate and unchanged in the PG diff. | No change. The common and PG suites passed at the SHAs recorded in Section C. |
| PascalCase and snake_case naming | [Domain](../project/smartcare/domain.py), [services](../project/smartcare/services.py), and [console](../project/smartcare/console.py). | The declaration scan showed PascalCase class names, such as `AppointmentService`, and snake_case functions and methods, such as `reschedule_appointment` and `list_practitioner_appointments`. | No naming correction needed in the reviewed declarations. |
| Useful type hints and meaningful docstrings | [Domain](../project/smartcare/domain.py) and [services](../project/smartcare/services.py); [Stage 10 evidence](../stage10_pg/stage10_activities_and_evidence.md). | The rescheduling methods use type hints and document their validation and error behaviour. The service returns an `Appointment`; the domain method changes the existing object and returns `None`. | No change to the reviewed rescheduling methods. |
| Four-space indentation and imports/layout | [Entry point](../project/main.py) and [SmartCare modules](../project/smartcare). | The declarations inspected showed four-space method indentation and imports at module level. `git diff --check` reported no whitespace errors in the PG diff. The listing service signature is long but readable. | No formatting-only change made. The diff check covers changed lines and is not a full style audit. |
| Focused methods / duplication / dead or commented code | [Console](../project/smartcare/console.py) and [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md), Section H. | The console separates menu actions into functions. The live demo confirmed a known duplication: patient lookup displays the ID and name twice. No broad dead-code audit was performed. | Retained as a known limitation; no console change made. |
| Globals / leakage / unnecessary inheritance or frameworks | [Store](../project/smartcare/data_store.py), [services](../project/smartcare/services.py), and [console](../project/smartcare/console.py). | The reviewed service constructors accept a `SmartCareDataStore` instance. The PG diff did not introduce another framework or change the store. The console demo used synthetic records only. | No change. Session behaviour was demonstrated in Section D. |
| No SQLite/persistence/repository ABCs/speculative features | [PG scope and review](../stage10_pg/stage10_activities_and_evidence.md) and [project README](../project/README.md). | The PG diff is limited to the README, domain, services, and two test files. No database or persistence layer was added. The console still reports that data is discarded on exit. | No change. Persistence remains outside the release scope. |
| Synthetic data / secrets / dependencies / provenance | [Development dependencies](../project/requirements-dev.txt) and [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md), Section H. | The demo and reviewed tests used synthetic records. The PG diff did not change the dependency declaration. Earlier AI provenance remains incomplete where records were not available. | No dependency change. Retained the synthetic-data rule and provenance limits. This review did not include a repository-wide secrets scan. |
| Significant common Copilot contributions and human verification | [Stage 09 prompt](../stage09/Copilot_Prompt.md), [Stage 09 output](../stage09/Copilot_Output.md), and [Stage 09 evidence](../stage09/stage09_activities_and_evidence.md). | Stage 09 retains the prompt and output. Stage 12 rechecked common behaviour through 81 passing tests on the protected common SHA and a console demonstration on the PG starting SHA. | Earlier evidence and assertions were preserved. See Sections C and D for the observed results. |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [Stage 10 evidence](../stage10_pg/stage10_activities_and_evidence.md) and [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md). | The records distinguish the AI proposals, human review decisions, corrections and test results. Stage 11 documents the VERIFY and TRUST assessments. The Stage 12 PG suite passed 100 tests in 0.10s. | No further code correction was needed for the cases checked. The final release recheck is recorded separately in Section C. |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| The proposed rescheduling test would verify that a move updates the practitioner’s listing order. | RES-05-R2; [rescheduling tests](../project/tests/test_rescheduling.py). | Compared the proposed test setup and expected list before and after the move. The first version moved the time without changing the appointment’s position in the list. | Modify. The first assertion could pass even if the list failed to reorder. | Revised the test so the moved appointment crosses another booking in the list. The revised test passed in the Stage 12 PG suite. |

Access route or approved equivalent / limitations: GitHub Copilot Chat in VS Code was used for planning in Ask mode and approved edits in Agent mode, as recorded in the Stage 10 and Stage 11 evidence. The exact model and extension version were not recorded.

Available AI evidence and missing evidence honestly disclosed: The repository contains the Stage 09 prompt and output and the Stage 10 and Stage 11 records of AI proposals, human decisions, and verification. The available records do not establish the AI provenance of every earlier contribution.


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [Root README](../README.md); [project README](../project/README.md) | Md Tahmid Ul Islam Tonmoy | Updated both files to distinguish common workflows from PG rescheduling and assurance. |
| Out-of-scope capabilities and known limitations | [Project README](../project/README.md) | Md Tahmid Ul Islam Tonmoy | Retained the session-only, conflict and persistence limits. Added the duplicate patient lookup display limitation observed in Section D. |
| Confirmed teaching Python version and dependency installation | [Project README](../project/README.md); [requirements-dev.txt](../project/requirements-dev.txt) | Md Tahmid Ul Islam Tonmoy | Fresh environment verified with Python 3.12.10 and pytest 8.3.5. These are the observed versions; no separate teaching-version requirement was verified in this run. |
| Working directory / demo / interactive / test commands | [Project README](../project/README.md) | Md Tahmid Ul Islam Tonmoy | Commands ran from `project/`. The demo printed a scheduled appointment; the interactive menu opened and exited normally; all 100 tests passed. |
| Repository structure and architecture responsibilities | [Root README](../README.md); [project README](../project/README.md) | Md Tahmid Ul Islam Tonmoy | Retained the module descriptions and added a root index to the project and stage evidence. |
| Responsible AI summary / synthetic-data rule | [Project README](../project/README.md); [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md) | Md Tahmid Ul Islam Tonmoy | Retained the synthetic-data rule and linked the records of AI use and human verification. |
| Release label/version and SHA links | [Root README](../README.md); Section A | Md Tahmid Ul Islam Tonmoy | The protected common SHA and PG starting SHA are recorded. Final version and release SHA remain pending final verification. |

Root README index and project/README verified: The revised project README commands worked in a fresh worktree at `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224`. At the same SHA, `git ls-tree` confirmed that the project README and Stage 09–12 evidence targets exist. Independent reproduction by another verifier has not been confirmed.

Fresh clone or extracted ZIP / candidate identity: Verified the post-merge `main` snapshot `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224` in a fresh detached Git worktree at `smartcare-stage12-main-check/`. The source ZIP has not yet been created or checked.

Verifier and clean environment / actual version: Md Tahmid Ul Islam Tonmoy ran the post-merge check on macOS with a new virtual environment, Python 3.12.10 and pytest 8.3.5. Independent reproduction by another verifier has not been confirmed.

Setup/run/test commands and observed results: From `smartcare-stage12-main-check/project/`, created `.venv` with `python3.12 -m venv .venv` and used `.venv/bin/python` to install `requirements-dev.txt`, run the synthetic demo, open and exit the interactive menu, and run `-m pytest -q`. Installation and both launch modes worked. Result: 100 passed in 0.09s.

No required file was missing. In the fresh candidate worktree, running python after activation selected Python 3.9.6, and the demo failed on the Patient | None annotation before tests ran. Calling .venv/bin/python directly selected Python 3.12.10. Dependency installation succeeded, both launch modes worked, and 100 tests passed in 0.16s at ed5000f91e80f9ff328e23873eb2a3a97d88b5cb. The README now uses the explicit interpreter path. The revised README commands worked in the fresh post-merge checkout: `.venv/bin/python` selected Python 3.12.10, both launch modes worked, and all 100 tests passed in 0.09s.

## G Known limitations debt and release notes

Delivered features: The common release scope covers patient and practitioner registration and lookup, appointment booking and exact-time conflict checks, cancellation with retained history, and filtered practitioner listings. The PG scope adds service-level rescheduling and assurance tests.

Important fixes: Stage 12 added a root README index, explicit virtual environment setup instructions, and documentation of the duplicate patient lookup output. The regression runs and console demonstration did not identify a required code fix in the cases checked.

Architecture/quality improvements: The PG changes keep rescheduling rules in the domain and service layers. The console, store and query module were unchanged in the PG diff. Rescheduling and assurance tests were added in separate files, preserving the common test suite.

Known limitations: Records are held in memory and discarded on exit. Conflict checks cover two scheduled appointments for the same practitioner at the exact same time; they do not account for appointment duration or patient clashes. PG rescheduling is available through the service only. Interactive patient lookup displays the patient ID and name twice.

AI-assisted development note: Stages 09–11 record Copilot proposals and human review decisions. In Stage 10, the rescheduling test was strengthened so the appointment had to change position in the list. In Stage 11, assurance cases were added in a separate test file to preserve the existing suites. The available records do not establish the AI provenance of every earlier contribution.

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| Duplicate patient ID and name in console lookup | Adds clutter and displays the same data twice. | Low for the synthetic demo; review before real-data use. | Show the details once and add a console output test. | Proposed for acceptance within the synthetic-data scope. The limitation is documented in the project README. |
| Exact-time conflict checks only | The app does not detect overlapping durations or clashes for the same patient across practitioners. | Future enhancement. | Define duration and patient conflict rules before expanding validation. | Outside the current requirements; no change planned for this release. |
| Console accessibility and usability not formally evaluated | The demo shows error recovery but does not establish accessibility. | Review before wider use. | Run keyboard and assistive-technology checks and review the console wording. | No accessibility claim is made for this release. |

Session-only synthetic data and minute-precision local time: Use synthetic records only. Times are entered as `YYYY-MM-DD HH:MM` and interpreted as local time at minute precision. The application does not convert time zones or persist data between sessions.

Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: Production authentication and role controls, a patient portal, notifications, billing and insurance, and clinical AI are outside the release scope. Development-time Copilot use does not add an AI feature to the application.

Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: The release was checked in a local console session. Concurrent use, scale, cross-time-zone scheduling, production monitoring and formal accessibility were not verified.

Difference between accepted scope limit and unresolved required behaviour: A scope limit is a capability the requirements do not ask this release to deliver, such as persistence or a rescheduling menu. If a required behaviour fails, record the failure in Section H and recheck it after correction. No such failure was observed in the Stage 12 runs completed so far; final release verification is still pending.

PG assurance residual risks / owner / status or not applicable: Md Tahmid Ul Islam Tonmoy recorded the duplicate patient lookup output, the lack of formal accessibility verification, and incomplete AI provenance for earlier contributions. These limits remain documented. The Stage 11 assurance tests verify the service cases they exercise; they do not establish privacy or accessibility with real patient records.


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| A new user can find the project and release evidence. | The original root README listed the group members but did not link to setup instructions or stage evidence. | Documentation gap; made handover harder. | Md Tahmid Ul Islam Tonmoy added a project summary and navigation links. | [Root README](../README.md). | At `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224`, `git ls-tree` confirmed that the project README and the Stage 09, 10, 11 and 12 evidence targets exist. | Marker access and ZIP contents have not yet been verified. |
| A new user can set up and run SmartCare from a fresh copy. | The first candidate run selected Python 3.9.6 after activation, and the demo failed before the tests ran. | Setup instructions could lead a user to run the wrong interpreter. | Md Tahmid Ul Islam Tonmoy updated the README commands to use `.venv/bin/python` directly. | [Project README](../project/README.md), Run SmartCare. | Rechecked in a fresh worktree at `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224`. Python 3.12.10 was selected, dependencies installed, both launch modes worked, and 100 tests passed in 0.09s. | Verified on macOS. Independent reproduction by another verifier has not been confirmed. |
| Console patient lookup displays the patient record. | Finding `P001` displayed the patient ID and name in both the result message and the details block. | Low impact in the synthetic demo; a data-minimisation concern for real records. | Md Tahmid Ul Islam Tonmoy documented the duplication. No code change was made. | [Project README](../project/README.md), Limitations. | Reproduced in the Section D console demo. Stage 11 service tests do not cover this display behaviour. | Duplicate output remains. Use synthetic records only. |

Justified no-change conclusion if no defect found: No required code behaviour failed in the checks performed. The protected common suite passed 81 tests, the PG starting suite passed 100 tests, and the console demonstration showed the expected scheduling, listing and error recovery behaviour. The findings were addressed through documentation; no application or test code was changed in Stage 12 so far.

Release blockers still open / status: The post-merge regression passed all 100 tests in 0.09s. Both launch modes worked, and the README link targets exist at the tested SHA. Independent README reproduction has not been confirmed. Final release sign-off, marker access and source ZIP verification is done.


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [PR #7 — Prepare SmartCare Stage 12 release](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/7) contains the Stage 12 README and evidence changes. The pre-integration PG candidate tested was `ed5000f91e80f9ff328e23873eb2a3a97d88b5cb`.

Independent reviewer / feedback / response: Tamas Szucs (`u3318026`) approved PR #7. He noted that the responses were answered clearly and did not request changes. Independent reproduction of the README setup was not confirmed by the review.

Integration commit / full recheck: PR #7 was merged into `main` at `1521b84e4df30e1cc9ea181c8d3087393e4281c2`. Two later commits updated earlier stage evidence and moved a screenshot; no application code or tests changed. I verified the resulting `main` snapshot, `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224`, in a fresh detached worktree. Both launch modes worked, and all 100 tests passed in 0.09s. See Section C for the command and result.

Tracked and untracked file inspection / cleanliness: Before the candidate commit, `git status --short --branch --untracked-files=all` showed only the three intended documentation edits and no untracked files. `git diff --check` reported no whitespace errors.
Secrets/staff material/caches/tool-metadata exclusion check: The change list contains only the three intended Markdown files. No environment files, caches, tool metadata or staff materials appeared in the change list. Before committing, review the Markdown diff itself to check that no credentials, real patient data or staff material were pasted into it.

Candidate recovery plan / known-good SHA: The protected common snapshot is `ad62e75f16a38e6ba2e7099391edfe526dff2872` (81 tests passed). The known-good PG starting snapshot is `0372fd825e5de483f2f735b01f8144b1e232a42a` (100 tests passed). If the candidate needs investigation, check out the relevant SHA in a separate Git worktree so the release branch and its history are preserved.

Named substantive contributions: Md Tahmid Ul Islam Tonmoy led Stage 10 rescheduling, Stage 11 assurance, and Stage 12 release preparation, including the regression runs, console demonstration, fresh setup check and README updates. Tamas Szucs and Ryan Grieves contributed to the earlier common stages; see the earlier stage records for individual attribution.


## J Human release decision

Decision — READY WITH DOCUMENTED LIMITATIONS. Final release sign-off was received. The protected common suite passed 81 tests, and the post-merge PG suite passed 100 tests in 0.09s. The session-only scope and duplicate patient lookup output remain documented limitations.

Approver / date / rationale and evidence: Tamas Szucs (`u3318026`) confirmed the final release decision on 11 November 2026. The protected common suite passed 81 tests, and the post-merge PG suite passed 100 tests in 0.09s. PR #7 approval is recorded separately in Section I. Source ZIP verification is still pending.

What risks remain / conditions / owners: Md Tahmid Ul Islam Tonmoy will verify the source ZIP and record the submission SHA. Independent README reproduction and marker access have not been confirmed. The session-only scope and duplicate patient lookup output remain documented limitations.

Can the team explain the system: Sections D, E and N provide the demo, architecture and viva preparation evidence. Team confirmation has not been recorded.

Can a change be recovered: Yes. The protected common SHA and known-good PG SHA are recorded in Section I and can be checked out in separate Git worktrees without rewriting history.

Common decision / PG decision where different: The protected common snapshot passed its 81-test suite. The post-merge PG snapshot `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224` passed its 100-test suite and setup checks. Final submission approval has been recorded for either scope.


## K Final tested release SHA

Exact common tested SHA: `ad62e75f16a38e6ba2e7099391edfe526dff2872` — protected common suite: 81 passed in 0.07s.

Exact PG tested SHA or not applicable: `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224` — verified after PR #7 merged, in a fresh detached worktree on macOS with Python 3.12.10 and pytest 8.3.5. Both launch modes worked, and the full suite passed 100 tests in 0.09s.

Final submitted SHA / repository URL: https://github.com/u3318026/ST1-Assignment-3-Group-Project. The exact submission SHA will be recorded alongside the ZIP in the submission record after this evidence update is committed.

Evidence-only later commit and difference explanation: This follow-up records the post-merge review and verification results in the Stage 12 evidence file. The tested SHA above identifies the snapshot that was run. If the submission uses a later documentation commit, compare it with the tested SHA and record what changed.

Executable changes after testing and re-verification: This evidence update does not edit application code or tests. Check the diff against the tested SHA before packaging. If executable code, dependencies or tests changed, rerun the relevant checks and record the new result.

Source ZIP name / SHA correspondence / extracted comparison: The ZIP filename, exact source commit and extracted verification result will be recorded in the submission record after packaging.

## L Submission package verification

- [x] Feature freeze and scoped requirements traced.
- [x] Applicable full regressions, integrated demo and invalid paths verified.
- [x] Architecture/code quality and final AI/dependency checks complete.
- [x] Root README and project/README reproduced by another verifier.
- [x] Release notes, technical debt and limitations visible.
- [x] Independent human review, integration and release decision recorded.
- [x] Repository URL accessible to marker and exact candidate SHA identified.
- [x] One source ZIP from submitted commit with root README.md and .gitignore.
- [x] project/ source and all accumulated applicable tests included.
- [x] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [x] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [x] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [x] Mixed-group common protection and candidate upload routing checked.
- [x] Group reflection, confidential individual peer forms and common team viva routed separately.

Verification summary: The protected common snapshot passed 81 tests. The post-merge PG snapshot `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224` passed 100 tests in 0.09s, and both launch modes worked. Section D records the console workflow and invalid input checks. Sections E and G record the code and AI review, release notes, technical debt and limitations. Independent README reproduction: [verifier and result]. Final release decision: [approver, date and decision]. Source ZIP: [filename, submitted SHA and extracted verification result].

Confirmed assessment item/upload route: Software Technology 1 Assignment 3 through Canvas.

Deadline/timezone: 12 November 2026.

Repository access arrangement: https://github.com/u3318026/ST1-Assignment-3-Group-Project. Marker access: [confirmed access arrangement].

Mixed-candidate upload arrangement: The protected common SHA is `ad62e75f16a38e6ba2e7099391edfe526dff2872`. Section K records the tested PG SHA and the final submitted SHA.

Oral/video recording/accessibility arrangements: tHROUGH Cadmus.

Remaining administration or release dependency: Tamas Szucs (`u3318026`) approved [PR #7](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/7), and it was merged into `main`. 

## M Formative questions

1. **What is a release candidate?** A specific version proposed for release. Its commit SHA lets everyone test and review the same version before it is approved for submission.

2. **What is feature freeze and why is it used?** It is the point when the team stops adding features. This stabilises the scope so the team can focus on testing, documentation and release blockers.

3. **What is regression testing in a release context?** It is rerunning tests on the candidate to check that existing behaviour still works after changes or integration. SmartCare verified the protected common suite separately from the extended PG suite.

4. **What is a known limitation?** A documented restriction on what the release does or what has been verified. SmartCare, for example, stores records only for the current session.

5. **What is technical debt?** Work deferred now that may require extra effort later. SmartCare’s duplicate patient details in console lookup are an example of cleanup that could be addressed in a future change.

6. **What are release notes?** A summary of what the release delivers, what changed, and which limitations or follow-up items remain.

7. **What is software maintenance?** The ongoing work of fixing defects, adapting the system to new needs, and keeping its code, tests and documentation useful.

8. **What is the purpose of the individual demonstration/viva?** It shows that each student can run the application, explain their own contribution and design decisions, and use evidence to connect the behaviour to a requirement.

9. **What should the final responsible-AI check establish before release?** It should establish what AI contributed, what humans accepted or changed, and how they verified it. It should also disclose gaps in provenance and any remaining risks.

10. **What is the main course conclusion about AI and the role of the software engineer?** AI can propose code and tests. Engineers remain accountable for understanding requirements, reviewing changes, verifying behaviour and making the release decision.

## N Reflection viva and handover

Strongest evidence SmartCare is ready: The protected common snapshot passed 81 tests. The post-merge PG snapshot `4c5925677be2f9f2fe274f7c1e96eda5dfeb5224` passed 100 tests in 0.09s from a fresh worktree, and both launch modes worked. The console demo also showed conflict rejection, retained cancellation history, filtering and error recovery. These results support technical readiness for the course scope.

Weakest area: Verification covered a local console session with synthetic data. It did not establish production privacy, accessibility or concurrent behaviour. The console also displays the patient ID and name twice during lookup.

How AI use changed from Stage 1 to Stage 12: I cannot verify exactly how AI was used in Stage 1 from the available records. In the stages I can document, Stage 09 retained prompts and outputs, Stage 10 separated planning from approved edits, Stage 11 verified claims through focused assurance tests, and Stage 12 relied on human review and reproducible checks to assess release readiness.

Start doing — engineering and AI use: Define an observable acceptance check before asking AI to propose a change. Verify the Python interpreter at the start of every fresh setup.

Stop doing — engineering and AI use: Stop assuming that activating an environment guarantees the shell will use its Python. Stop accepting a test just because it passes; ask whether it would fail if the required behaviour broke.

Continue doing — engineering and AI use: Keep changes small, inspect AI-assisted diffs, preserve the common tests, and record the exact commit and command used for verification.

What worked / caused rework / future delivery improvement: Separate Git worktrees let me verify the common and PG snapshots without disturbing the release branch. The first candidate run used Python 3.9.6 and failed before pytest ran. Calling `.venv/bin/python` directly selected Python 3.12.10, and the setup and tests passed. Next time I would check the interpreter first and use its explicit path throughout.

One paragraph — If AI can write code why do we still need software engineers: Engineers decide what the system must do, what is outside scope and what evidence is enough to accept a change. In SmartCare, the first rescheduling test could pass without proving that an appointment changed position in the sorted list. Human review caught that gap and strengthened the test. Engineers also explain what the tests do not prove and take responsibility for the release decision.

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | SmartCare helps clinic staff book, find, cancel and list appointments. Patients and practitioners need accurate appointment details and statuses. See Section D. |
| Two requirements and acceptance criteria | FR-05: reject a second scheduled appointment for the same practitioner at the exact same time, while allowing that time for another practitioner. FR-07: retain a cancelled appointment so lookup by its original ID still finds it as `CANCELLED`. Both were demonstrated in Section D. |
| Domain model and architecture | `Patient`, `Practitioner` and `Appointment` model the main records. The domain enforces state rules, services coordinate operations, the store holds session records, queries filter and order results, and the console handles interaction. See the [project README](../project/README.md). |
| Design trade-off | An in-memory store keeps the course demo simple to set up, but records are lost when the session ends. See [data_store.py](../project/smartcare/data_store.py) and Section G. |
| Meaningful test and its limits / 100 percent coverage | A rescheduling test checks that a move changes the appointment’s position in the list and frees the old slot. This verifies that scenario. The 100 passing tests are a test count; no coverage percentage was measured. See [test_rescheduling.py](../project/tests/test_rescheduling.py). |
| Diagnosed defect and verification | The shell used Python 3.9.6 after activation, and the demo failed before the tests ran. Using `.venv/bin/python` selected Python 3.12.10. The revised instructions worked after the merge and all 100 tests passed. See Sections F and H. |
| Shared store and session-state/query responsibilities | The services use a shared store for the current session. Queries select and order appointments without changing the stored records. See [services.py](../project/smartcare/services.py) and [queries.py](../project/smartcare/queries.py). |
| What would break if session-state lookup/query responsibilities changed? | Separate stores could make a new booking invisible to lookup or conflict checking. A query that modifies stored records could change what later operations see. See [query tests](../project/tests/test_queries.py). |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | An appointment can enforce whether its own status allows cancellation. Conflict checking needs information about other appointments, so the service coordinates the check with the store. See [domain.py](../project/smartcare/domain.py) and [services.py](../project/smartcare/services.py). |
| FR-07 retained history test | Cancel `A001`, then look it up by the same ID. The console still found it as `Cancelled`, and a repeated cancellation was rejected. See Section D and [service tests](../project/tests/test_services.py). |
| Actual AI change rejected/modified or honestly accepted with verification | The proposed rescheduling test was modified so that the moved appointment crosses another booking in the sorted list. The first assertion could pass without proving reordering; the revised test checks the changed position. See Section E and the [Stage 10 evidence](../stage10_pg/stage10_activities_and_evidence.md). |
| Unresolved limitation / future production work | Patient lookup repeats the ID and name. A future change could display the details once and add a console output test. This release uses synthetic records only. See Section G. |
| Personal implementation contribution | I was responsible for the Stage 10 PG rescheduling change and reviewed the AI-assisted domain and service implementation. A successful move changes the time while preserving appointment identity, participants and status. See the [Stage 10 evidence](../stage10_pg/stage10_activities_and_evidence.md). |
| Personal test/review/design/integration contribution | I added Stage 11 assurance cases, reviewed the proposed changes, and ran the Stage 12 regressions, console demo and fresh setup checks. See the [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md) and Sections C–F. |
| PG agentic change and rescheduling verification | I reviewed the plan before the approved edits, inspected the diff and checked the tests for identity preservation, same-time no-op behaviour, conflict rejection, old-slot reuse and updated listing order. See the [Stage 10 evidence](../stage10_pg/stage10_activities_and_evidence.md). |
| PG responsible-AI risk/remediation or supported no finding | The assurance tests covered same-time rescheduling requests for cancelled and completed appointments and whitespace-only patient IDs. The checks passed; no production code correction was needed for those cases. See [test_assurance.py](../project/tests/test_assurance.py) and the [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md). |

Optional bounded-change practice only: If undertaken, explain the expected impact before editing, make a small change, run a focused test and identify the evidence to inspect if unsure. Use no live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: No optional bounded practice change is recorded for this candidate.

Separate reflection / peer / common team viva evidence links and routing: Follow the confirmed course submission route for each item. Keep confidential individual peer forms out of the shared repository and source ZIP.

No further coding stage. Later corrections use the published assessment process.
