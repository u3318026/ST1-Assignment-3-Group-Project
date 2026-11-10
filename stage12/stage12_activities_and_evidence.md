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
| System is maintainable — common and PG | A fresh checkout of the PG starting commit ran both launch modes and passed 100 tests in a new virtual environment. | [Project README](../project/README.md); [development dependencies](../project/requirements-dev.txt); Section F. | Md Tahmid Ul Islam Tonmoy verified the setup; independent review pending. | Starting setup verified; updated README instructions still need a final recheck. | Follow the revised README from a fresh checkout of the final candidate. |
| FR-01–03 registration, lookup and validation — common | Domain and service tests provide prior evidence for registration, lookup and validation. | [Domain tests](../project/tests/test_domain.py); [Service tests](../project/tests/test_services.py). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Rerun the common suite and demonstrate registration, lookup and invalid input handling with synthetic records. |
| FR-04–05 booking and conflict rules — common | Service and workflow tests provide prior evidence for booking and conflict handling. | [Service tests](../project/tests/test_services.py); [Workflow tests](../project/tests/test_workflows.py). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Verify that a same-time booking for the same practitioner is rejected and a same-time booking for a different practitioner is allowed. |
| FR-06–08 cancellation, history and lookup — common | The service tests and Stage 09 evidence cover the cancellation and lookup workflows. | [Service tests](../project/tests/test_services.py); [Stage 09 evidence](../stage09/stage09_activities_and_evidence.md). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Verify that cancellation retains the appointment, lookup still finds it, and a second cancellation is rejected. |
| FR-09 and QRY/FP listing, filtering, ordering and purity — common | The query tests and Stage 09 evidence provide prior coverage for appointment listings. | [Query tests](../project/tests/test_queries.py); [Query implementation](../project/smartcare/queries.py); [Stage 09 evidence](../stage09/stage09_activities_and_evidence.md). | Stage 12 verifier pending. | Prior evidence available; release verification pending. | Rerun the query tests and verify that filtering and ordering leave the stored appointments unchanged. |
| UI full console sequence and error recovery — common | The Stage 12 demo verified registration, lookup, booking conflicts, cancellation, filtering, and recovery from invalid input using synthetic records. | [Workflow tests](../project/tests/test_workflows.py); Section D. | Md Tahmid Ul Islam Tonmoy ran the demo; independent review pending. | Demo complete on the PG starting commit using the common console workflows. | Confirm the console still launches from the final candidate. |
| Session-only scope / FR-10 retired — common and PG | Appointment data is held in the in-memory store for the current session. FR-10 persistence is outside the release scope. | [Data store](../project/smartcare/data_store.py); [Project README](../project/README.md). | Stage 12 verifier pending. | Scope identified; release check pending. | Verify that records are available in the current session and that the README clearly states they are not retained after exit. |
| PG RES and assurance integration — PG only | The full suite passed 100 tests in 0.10s on the PG starting commit and 100 tests in 0.16s in a fresh environment at the same commit. | [Assurance tests](../project/tests/test_assurance.py); [rescheduling tests](../project/tests/test_rescheduling.py); Sections C and F. Tested SHA: `0372fd825e5de483f2f735b01f8144b1e232a42a`. | Md Tahmid Ul Islam Tonmoy ran the tests; independent review pending. | Stage 12 starting regression passed; final candidate recheck pending. | Run the full PG suite on the final candidate and record its SHA and result in Section C. |
## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | macOS; Python 3.12.10; pytest 8.3.5 | From `smartcare-stage12-common/project/`: `../../st1-assignment-3/.venv/bin/python -m pytest -q` | `ad62e75f16a38e6ba2e7099391edfe526dff2872` | 81 passed in 0.07s | Stage 12 local terminal output; protected common commit |
| Complete PG | macOS; Python 3.12.10; pytest 8.3.5 | From `smartcare-stage12-pg/project/`: `../../st1-assignment-3/.venv/bin/python -m pytest -q` | `0372fd825e5de483f2f735b01f8144b1e232a42a` | 100 passed in 0.10s | Stage 12 local terminal output; PG starting commit |
| Affected focused checks after correction | Not applicable at this point | No correction was needed after these runs. | — | Not run | — |
| Full integrated recheck | Pending | Rerun the full suite from a fresh copy of the final release candidate. | Pending final release SHA | Not yet run | Record the result after the final recheck. |

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

Root README index and project/README verified: The original root README listed the group but had no project or evidence index. The project README included run commands but did not show how to create a virtual environment. Both files were updated on the Stage 12 branch. Verification of the final versions remains pending.

Fresh clone or extracted ZIP / candidate identity: Created a fresh detached Git worktree at PG starting SHA `0372fd825e5de483f2f735b01f8144b1e232a42a`. This was a fresh checkout of the starting snapshot; the final release package has not yet been verified.

Verifier and clean environment / actual version: Md Tahmid Ul Islam Tonmoy. macOS, a newly created virtual environment, Python 3.12.10 and pytest 8.3.5.

Setup/run/test commands and observed results: From `smartcare-stage12-fresh/project/`, created a virtual environment with `python3.12 -m venv` and used its Python to run `-m pip install -r requirements-dev.txt`, `main.py`, `main.py --interactive`, and `-m pytest -q`. Installation succeeded, the synthetic demo ran, and the interactive console opened and exited normally using option `0`. Result: 100 passed in 0.16s.

Missing local file or setup gap / remedy and recheck: No required local file was missing during the run. Added explicit virtual environment setup instructions to the project README and navigation links to the root README. Recheck the updated instructions against the final release candidate.

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
| A new user can find the project and release evidence. | The original root README listed the group members but did not link to setup instructions or stage evidence. | Documentation gap; makes handover harder. | Md Tahmid Ul Islam Tonmoy added a project summary and navigation links. | [Root README](../README.md), updated on `release/stage12`. | Final checkout: verify that the links open the intended files. Pending. | Final release SHA is not yet recorded. |
| A new user can set up and run SmartCare from a fresh copy. | The original project README listed run commands but assumed a Python environment was already configured. A fresh worktree and new environment successfully ran both launch modes and passed 100 tests. | Documentation gap; a new user could miss the environment setup step. | Md Tahmid Ul Islam Tonmoy added virtual environment setup, verified environment versions and scope notes. | [Project README](../project/README.md), updated on `release/stage12`. | Starting snapshot: 100 passed in 0.16s. Recheck the revised README commands from the final checkout. Pending. | The observed environment was macOS with Python 3.12.10 and pytest 8.3.5. |
| Console patient lookup displays the patient record. | Finding `P001` displayed the patient ID and name in both the result message and the details block. | Low impact in the synthetic demo; a data-minimisation concern for real records. | Md Tahmid Ul Islam Tonmoy documented the duplication. No code change was made. | [Project README](../project/README.md), Limitations. | Reproduced in the Section D console demo. Stage 11 service tests do not cover this display behaviour. | Duplicate output remains. Use synthetic records only. |

Justified no-change conclusion if no defect found: No required code behaviour failed in the checks performed. The protected common suite passed 81 tests, the PG starting suite passed 100 tests, and the console demonstration showed the expected scheduling, listing and error recovery behaviour. The findings were addressed through documentation; no application or test code was changed in Stage 12 so far.

Release blockers still open / status: No failing required behaviour was observed in the checks completed so far. Final checkout verification, the integrated regression recheck, and release sign-off remain open. Do not record the release as ready until those checks are complete.


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: The Stage 12 documentation diff was checked on `release/stage12` against its starting commit, `0372fd825e5de483f2f735b01f8144b1e232a42a`. The diff contains changes to the [root README](../README.md), [project README](../project/README.md), and this Stage 12 evidence file. A final candidate commit has not yet been recorded.

Independent reviewer / feedback / response: Stage 12 independent review is pending. The Stage 10 and Stage 11 reviews are documented in their respective evidence files.

Integration commit / full recheck: Stage 12 changes have not been integrated. The starting snapshots passed 81 common tests and 100 PG tests. The final integrated recheck and its exact SHA are pending.

Tracked and untracked file inspection / cleanliness: `git status --short --branch --untracked-files=all` showed only the three expected tracked documentation edits and no untracked files. `git diff --stat` confirmed the scope, and `git diff --check` reported no whitespace errors. The working tree has uncommitted documentation edits.

Secrets/staff material/caches/tool-metadata exclusion check: The change list contains only the three intended Markdown files. No environment files, caches, tool metadata or staff materials appeared in the change list. Before committing, review the Markdown diff itself to check that no credentials, real patient data or staff material were pasted into it.

Candidate recovery plan / known-good SHA: The protected common snapshot is `ad62e75f16a38e6ba2e7099391edfe526dff2872` (81 tests passed). The known-good PG starting snapshot is `0372fd825e5de483f2f735b01f8144b1e232a42a` (100 tests passed). If the candidate needs investigation, check out the relevant SHA in a separate Git worktree so the release branch and its history are preserved.

Named substantive contributions: Md Tahmid Ul Islam Tonmoy led Stage 10 rescheduling, Stage 11 assurance, and Stage 12 release preparation, including the regression runs, console demonstration, fresh setup check and README updates. Tamas Szucs and Ryan Grieves contributed to the earlier common stages; see the earlier stage records for individual attribution.


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: NOT YET READY. The starting snapshots passed verification, but the final release candidate has not been committed, rechecked or signed off.

Approver / date / rationale and evidence: Final approval and date are pending. The protected common snapshot passed 81 tests. The PG starting snapshot passed 100 tests, and a fresh setup of that snapshot also passed 100 tests. The console demonstration is recorded in Section D.

What risks remain / conditions / owners: Md Tahmid Ul Islam Tonmoy will prepare the candidate and verify the revised README instructions and full suite from a fresh checkout of the candidate commit. Independent review and release sign-off are pending. The duplicate patient lookup display and session-only scope remain documented limitations.

Can the team explain the system: The walkthrough is documented in Sections D and E. It covers the console, service and domain responsibilities, the in-memory store, and how the tests verify common and PG behaviour. Team confirmation is pending.

Can a change be recovered: Yes. The protected common and known-good PG starting SHAs are recorded in Section I and can be checked out in separate Git worktrees without rewriting branch history.

Common decision / PG decision where different: The protected common snapshot passed its regression suite. The PG starting snapshot passed its extended suite and fresh setup checks. Neither is recorded as the final release until the applicable candidate and sign-off are recorded.


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [response]

2. What is feature freeze and why is it used? [response]

3. What is regression testing in a release context? [response]

4. What is a known limitation? [response]

5. What is technical debt? [response]

6. What are release notes? [response]

7. What is software maintenance? [response]

8. What is the purpose of the individual demonstration/viva? [response]

9. What should the final responsible-AI check establish before release? [response]

10. What is the main course conclusion about AI and the role of the software engineer? [response]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
