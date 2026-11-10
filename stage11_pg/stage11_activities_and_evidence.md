# Stage 11 PG assurance activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG participation is unassessed.

Blank student template. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied file in stage11_pg/ in your EXISTING repository. Preserve project/, earlier records/tests and the protected common Stage 9 SHA. Do not copy staff references or fabricate AI evidence.

Group/tutorial: Group 6 / Wednesday 2.30 pm - 4.30 pm
Assessed PG members and contributions: Md Tahmid Ul Islam Tonmoy — led the Stage 11 assurance review, identified two coverage gaps, reviewed and approved the Copilot test proposal, verified the resulting changes, ran the test suites, and documented the findings and limitations.
Optional UG contributors: None.

## A Handover and human-first scope

Integrated Stage 10 code SHA / protected Stage 9 common SHA: Stage 10 was integrated through [PR #4](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/4) at `fbad1d2e848ad8ba2b6c457a5c0a0929cf699fbc`. Protected Stage 9 common SHA: `ad62e75f16a38e6ba2e7099391edfe526dff2872`.

Recoverable branch / baseline / actual commands, working directory and results: On branch `feature/stage11-assurance` at commit `7fd79787bfb45da9e18c9d1f9e33f04a8b52f025`, I ran `../.venv/bin/python -m pytest -q` from `project/` before making Stage 11 changes. Result: 97 passed in 0.05s.

Domain, store, services, queries, console, entry point, tests and rescheduling inspected: I mapped the application entry point in `project/main.py`, the console actions in `project/smartcare/console.py`, the shared store in `project/smartcare/data_store.py`, and the appointment selection and sorting functions in `project/smartcare/queries.py`. For the focused review, I checked the rescheduling status guard in `project/smartcare/domain.py`, the rescheduling and patient lookup methods in `project/smartcare/services.py`, the console patient lookup and display, and the relevant tests in `project/tests/test_rescheduling.py`, `project/tests/test_services.py`, and `project/tests/test_assurance.py`.

Selected PG feature and common workflow / requirements / code locations: PG feature — appointment rescheduling in `project/smartcare/domain.py` and `project/smartcare/services.py`, with tests in `project/tests/test_rescheduling.py`. Check that a cancelled or completed appointment rejects a request for its original time without changing its time or status. Common workflow — patient lookup by ID through `PatientService.find_patient()` in `project/smartcare/services.py` and `SmartCareDataStore.find_patient()` in `project/smartcare/data_store.py`. The service contract requires `ValueError` for blank or invalid IDs and `LookupError` for valid IDs that are not found. The existing direct service tests cover a known ID and an unknown ID. Proposed assurance check: a whitespace-only ID raises `ValueError`.

Actual available earlier AI, issue, PR and dependency evidence: Stage 10 Copilot-assisted work is recorded in [Issue #3](https://github.com/u3318026/ST1-Assignment-3-Group-Project/issues/3), [implementation PR #4](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/4), and [evidence PR #5](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/5). The dependency declaration and installed pytest metadata were checked in Section H.

Missing evidence / honest limitation: The exact Copilot model and extension version were not recorded. The available Stage 10 records do not establish the AI provenance of every earlier contribution. Stage 11 independent review and the integrated retest are pending.

Assets and trust boundaries: The assets in scope are patient identifiers and names, appointment times and statuses, and the integrity of the repository and its tests. The console passes user input to the service, which validates it and uses the shared store. Copilot inspected repository code and tests; editing was limited to one new test file using synthetic data.

Scope, assumptions, exclusions and initial observations made BEFORE Copilot: The existing tests verify that a scheduled appointment can keep its original time and that cancelled or completed appointments reject a move to a different time. The file does not test whether cancelled or completed appointments also reject a request for their original time. Expected result: `ValueError`, with the stored time and status unchanged.

Confirmed Copilot mode / student entitlement / permissions / approval reference: I used Copilot Chat in VS Code. Ask mode inspected the code and proposed a plan without editing. I approved Agent mode to create only `project/tests/test_assurance.py` and verified the resulting file with Git. Both modes were available in my session; the specific student entitlement and a written course approval reference were not recorded.

Plan-only → human approval → bounded editing check / approved equivalent route: Copilot proposed two test-only changes after checking the existing coverage. I approved both cases, with one adjustment: add them in a new `project/tests/test_assurance.py` file so the original suites remain unchanged and can be rerun separately. The approved scope is one new test file. No production, dependency or existing test changes are authorised.

Overview/revision 2 availability / source: `project/README.md` identifies the requirements baseline as SmartCare A3 2026 revision 2. The root `README 2.md` states that the Assignment 3 Overview and Stage 6–12 handouts were supplied at the beginning. I found these references in the repository but did not locate a separate tracked copy of the Overview.

Assigned PG owner / independent reviewer: Md Tahmid Ul Islam Tonmoy owns the Stage 11 assurance work. Independent reviewer: pending confirmation.

## B Original tutorial activities


### B1 Risk classification

| Scenario | Risk | Why | Control |
|---|---|---|---|
| AI explains a public Python error | Low | The error is public and the AI is only explaining it. The explanation can still be wrong. | Share a minimal example without private data and verify the explanation locally. |
| Student pastes an API key into AI | High | A credential could be exposed and used to access a service. | Never share the key. Use a placeholder. If a real key was shared, revoke or rotate it and report the exposure. |
| Agent proposes unknown package | Medium | The package may be unnecessary, nonexistent, or unsafe to install. | Verify its source, purpose, version and licence before approving it. Prefer an existing dependency when it meets the need. |
| AI-generated code logs patient names | High | Personal data could be retained in logs and seen by people who do not need it. | Remove patient names from logs and check the output using synthetic records. |
| Agent modifies deployment configuration | High | The change could affect availability, access permissions or secret handling. | Require human approval, inspect the diff and verify the change outside production before deployment. |

### B2 Green Amber Red
Choose GREEN / AMBER / RED and justify each.

| Use | Classification | Reason and policy/control |
|---|---|---|
| Ask AI to explain pytest fixture | GREEN | Conceptual help is low risk. Use a generic example and verify the explanation. |
| Generate 100 lines of assessed domain code | AMBER | Proceed only if the assessment permits that use. Limit the scope, understand and test the code, and disclose assistance as required. If the assessment prohibits it, do not proceed. |
| Paste real patient record for debugging | RED | It exposes personal data. Use a synthetic record that reproduces the problem. |
| Use AI to draft test ideas then verify | AMBER | Treat the ideas as proposals. Check them against requirements and existing coverage, then run meaningful tests and record the assistance. |
| Agent autonomously deletes repository files | RED | Unsupervised deletion can destroy work and exceed the task scope. Keep deletion outside the agent's permissions unless a specific, reviewed change is approved. |

### B3 VERIFY patient search
Record one concrete question/evidence item for each letter against the current PatientService/shared-store contract.

| VERIFY element | Question or evidence |
|---|---|
| Validate | Does `PatientService.find_patient()` return the stored patient for a known ID, raise `LookupError` for a valid but unknown ID, and raise `ValueError` for a blank or invalid ID? |
| Examine | Check that `PatientService.find_patient()` validates the input, asks the shared store for the patient, and returns the stored object without creating a replacement. |
| Run meaningful tests | Run the existing known-ID and unknown-ID tests and the Stage 11 whitespace-only ID test. Check that each case gives the expected result or exception. |
| Inspect risks | Check whether invalid IDs are confused with unknown IDs and whether the console displays more patient information than needed. |
| Fit architecture/policy | Keep lookup in the service and shared store. Use synthetic records and avoid new dependencies or unnecessary changes to the console. |
| You remain responsible | Read the code and assertions, run the tests locally, and record what they establish and what they do not cover. |

### B4 TRUST decision
The feature passes tests but adds an unreviewed package and logs full patient records. Should it be accepted?

| TRUST element | Reason/evidence/action |
|---|---|
| Trace | Identify where the package and logging change came from, who proposed them, and whether the change was approved. |
| Review | Inspect the diff to see why the package was added and where full patient records are written. |
| Understand | Establish whether the feature needs the package or the record logging. Check what happens to the logged data and who could access it. |
| Secure | Remove the patient-record logging. Remove the unnecessary package, or verify and approve it separately if it is essential. |
| Test | Rerun the functional tests and use synthetic records to check that patient details are no longer written to logs. |

Decision and reason: Reject the example change as submitted. Passing functional tests does not justify adding an unreviewed dependency or logging full patient records. Reconsider it after removing the unnecessary logging, resolving the dependency concern, and rerunning the relevant checks.

Exit: Why is a technically correct AI-generated feature still potentially unacceptable? It can return the expected result while exposing private data, introducing an unverified dependency, or exceeding the approved scope.

### B5 Sanitised critique only
Identify the hard-coded demo-key placeholder, unnecessary requests import, patient-ID/name logging, fabricated lookup and missing test/provenance evidence. Do not copy or run the old audit target.

| Concern | Observed example evidence | Severity | Correction and recheck |
|---|---|---|---|
| Hard-coded demo-key placeholder | The tutorial example describes a key placeholder embedded in the code. It is not evidence that a real credential was exposed. | Medium | Remove the placeholder and check that no credential is needed for local patient lookup. |
| Unnecessary `requests` import | The example imports `requests`, although the lookup should use the existing shared store. | Medium | Remove the unused import. Check the dependency declarations and rerun the lookup tests. |
| Patient ID and name logging | The example logs patient IDs and names, exposing details that are unnecessary for debugging. | High | Remove those details from logs. Use synthetic data to check that lookup still works without writing identifiers or names to logs. |
| Fabricated patient lookup | The example fabricates a lookup result instead of retrieving the stored patient. | High | Use the existing service and shared store. Verify that a known ID returns the stored object and that unknown and invalid IDs raise the expected exceptions. |
| Missing test and provenance evidence | The example lacks evidence showing where the change came from and which checks were run. | Medium | Record the source, reviewed diff, test commands and observed results. Ask a reviewer to verify the evidence before accepting the change. |

## C Actual risk register


| Risk | Artefact | Likelihood | Impact | Control | Status |
|---|---|---|---|---|---|
| A same-time request bypasses the status check for a cancelled or completed appointment. | `Appointment.reschedule()` and `AppointmentService.reschedule_appointment()`; coverage in `project/tests/test_assurance.py`. | Low after adding regression coverage. | Medium: the service could report success for a request that should be rejected. | Check that both statuses raise `ValueError` and that the stored appointment, time and status remain unchanged. | Both cases passed locally. No defect observed. |
| A whitespace-only patient ID is treated as an unknown ID instead of invalid input. | `PatientService.find_patient()`; coverage in `project/tests/test_assurance.py`. | Low after adding regression coverage. | Low: callers could receive the wrong error and respond incorrectly. | Check that whitespace-only input raises `ValueError`; retain the existing test that expects `LookupError` for a valid but unknown ID. | Both checks passed locally. No defect observed. |

## D Actual findings tests and corrective actions

For each of at least TWO new/materially strengthened tests, explain the earlier coverage gap and the incorrect behaviour its assertions detect. No duplicated unchanged tests. The two assurance tests and their coverage gaps are documented in the Test 1 and Test 2 rows below. Test 1 detects a same-time request bypassing the status guard; Test 2 detects a whitespace-only ID being accepted or treated as an unknown ID.

| Claim / risk / requirement | Location / version | Independent check / test | Observed result / finding or no finding | Action / owner | Recheck / limitation |
|---|---|---|---|---|---|
| Only scheduled appointments may be rescheduled, including requests for the original time. | `project/smartcare/domain.py` and `project/smartcare/services.py`; verified at `4102507`. | Reviewed the status check and ran the new same-time test for cancelled and completed appointments. | Both requests raised `ValueError`. The store retained the same appointment with its original time and status. | Added regression coverage; no production fix needed. Owner: Md Tahmid Ul Islam Tonmoy. | Both cases passed. This check covers the two non-scheduled statuses for same-time requests. |
| Patient lookup must reject invalid IDs with `ValueError` and report valid but unknown IDs with `LookupError`. | `PatientService.find_patient()` in `project/smartcare/services.py`; verified at `4102507`. | Ran the new whitespace-only ID test and retained the existing unknown-ID test. | A whitespace-only ID raised `ValueError`; the existing unknown-ID case still passed. | Added regression coverage; no production fix needed. Owner: Md Tahmid Ul Islam Tonmoy. | The new check covers whitespace-only input at the service layer. |

| Assurance test | Earlier gap | Input/setup | Meaningful assertion | Incorrect result detected | Evidence/result |
|---|---|---|---|---|---|
| Test 1 — Reject same-time rescheduling for non-scheduled appointments | Earlier tests covered same-time requests for scheduled appointments and different-time requests for cancelled or completed appointments, but not the combination. | Store a cancelled or completed appointment and request its original time through `AppointmentService.reschedule_appointment()`. | Expect `ValueError`. Verify the store still holds the same appointment object and that its time and status are unchanged. | Detects a regression where the same-time shortcut bypasses the status check, or a rejected request changes the stored appointment. | `test_non_scheduled_appointment_cannot_be_rescheduled_to_original_time` in `project/tests/test_assurance.py`; both status cases passed. |
| Test 2 — Reject a whitespace-only patient ID | Earlier service tests covered a known ID and an unknown ID, but not a whitespace-only ID. | Call `PatientService.find_patient('   ')`. | Expect `ValueError`. The existing unknown-ID test still expects `LookupError`. | Detects a regression where whitespace-only input is accepted or treated as an unknown ID instead of invalid input. | `test_find_patient_rejects_whitespace_only_id` in `project/tests/test_assurance.py`; passed. |

| Suite | Command / project working directory | Tested code SHA | Actual result | Evidence |
|---|---|---|---|---|
| Assurance focused | From `project/`: `../.venv/bin/python -m pytest -q tests/test_assurance.py` | Pre-commit working tree on `feature/stage11-assurance`; base `7fd79787bfb45da9e18c9d1f9e33f04a8b52f025` plus the uncommitted `test_assurance.py` | 3 passed in 0.01s | Local terminal output |
| Previous PG independently | From `project/`: `../.venv/bin/python -m pytest -q tests/test_rescheduling.py` | Same pre-commit working tree | 16 passed in 0.01s | Local terminal output |
| Common independently | From `project/`: `../.venv/bin/python -m pytest -q --ignore=tests/test_assurance.py --ignore=tests/test_rescheduling.py` | Same pre-commit working tree | 81 passed in 0.03s | Local terminal output |
| Full PG cumulative | From `project/`: `../.venv/bin/python -m pytest -q` | `410250721c41dda0f28c4129a2e7cc177d189141` | 100 passed in 0.08s | Local terminal output immediately after the Stage 11 test commit |
| Integrated retest | Pending integration | Pending | Not yet run | Record after testing the integrated commit |

Confirmed defect / minimal correction / before-after evidence, or justified no-change decision: No production defect was found in the cases tested. Same-time requests for cancelled and completed appointments raised ValueError and left the stored time and status unchanged. A whitespace-only patient ID also raised ValueError. Two test functions were added to cover these gaps; no production code change was needed.
Preserved earlier assertions / inspected test diff: I compared the new `project/tests/test_assurance.py` with the reviewed proposal and confirmed that no existing project files changed. The original Stage 10 suite passed all 16 cases, and the common suite passed all 81 cases independently.

Unresolved failures, action and owner: No test failures remain from the local runs. Md Tahmid Ul Islam Tonmoy will record the integrated retest after Stage 11 is merged.

## E VERIFY assessment


| VERIFY element | Evidence | Finding/action |
|---|---|---|
| Validate against requirements | The rescheduling rule permits changes only for scheduled appointments. The patient lookup contract requires `ValueError` for invalid IDs and `LookupError` for valid IDs that are not found. | Checked that both new tests assert the required behaviour. |
| Examine implementation | `Appointment.reschedule()` checks the status before returning for a same-time request. `PatientService.find_patient()` rejects whitespace-only IDs before calling the store. | The implementation matches the expected behaviour for the cases reviewed. |
| Run meaningful tests | The new assurance suite passed 3 cases. The Stage 10 suite passed 16, and the common suite passed 81. The full suite passed 100 at commit `4102507`. | The new tests cover gaps without replacing earlier assertions. See Section D for commands and results. |
| Inspect risks and assumptions | The same-time shortcut could bypass the status check if reordered. Whitespace-only IDs could be mistaken for valid but unknown IDs. | Added regression checks for both risks. The findings apply to the service calls tested; console behaviour was not tested by these new cases. |
| Fit architecture and policy | The new file uses existing SmartCare services, the shared store, pytest and synthetic records. The Git scope check showed no changes to existing project files. | No production code or dependency changes were needed. |
| You remain responsible | I checked the Copilot proposal against the saved test file and ran the suites locally. | I accepted the test changes based on the code and test output. Independent review and the integrated retest are still pending. |

## F TRUST assessment


| TRUST element | Evidence | Status/action |
|---|---|---|
| Trace | Copilot proposed the tests in Ask mode and created the approved file in Agent mode. The test changes are recorded in commit `410250721c41dda0f28c4129a2e7cc177d189141`. | The proposal, approved scope and resulting change can be traced. See Section G for the Copilot audit. |
| Review | I compared the saved test file with the reviewed proposal and checked Git status. Only the new test file was added under `project/`. | Local scope review complete; independent review is pending. |
| Understand | The rescheduling test checks that a same-time request cannot bypass the status check. The lookup test checks that an invalid ID is rejected as invalid input. | Both tests target specific gaps in earlier coverage. |
| Secure | The tests use synthetic records and the existing local test setup. The change introduces no new dependency or production logging. | No real patient data or credentials were needed for these tests. |
| Test | The assurance suite passed 3 cases, the previous PG suite passed 16, and the common suite passed 81. The full suite passed 100 tests at commit `4102507`. | Local verification complete. The integrated retest is pending. |

## G GitHub Copilot audit

Sanitised material / actual prompt, context, version and response links: In VS Code Copilot Chat, I asked for a plan only to check two gaps: same-time rescheduling for cancelled or completed appointments, and patient lookup with a whitespace-only ID. Copilot inspected the existing tests and service code and proposed two test changes. See the actual prompt and response summary below. The exact Copilot model and extension version were not recorded.

Evidence that human scope and initial observations preceded Copilot: Before the Stage 11 Copilot session, I ran the 97-test baseline, inspected the existing rescheduling and patient lookup tests, and recorded the proposed checks in Section A.

Actual supported route or approved equivalent / access limitations: Ask mode reviewed the repository and proposed the diff without editing. After I approved the two tests and limited the scope to one new file, Agent mode created `project/tests/test_assurance.py`. I checked the saved file and Git status, then ran the tests myself.

Significant earlier AI contributions reviewed / available evidence / missing provenance: Stage 10 Copilot assisted with the rescheduling implementation and its tests. The implementation is traceable through [Issue #3](https://github.com/u3318026/ST1-Assignment-3-Group-Project/issues/3) and [PR #4](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/4). The separate documentation is in [PR #5](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/5). These records cover the documented Stage 10 work; they do not establish the AI provenance of every earlier contribution.

| AI claim | Affected requirement/code/evidence | Observed vs speculative / human verification | Severity / Accept Modify Reject / reason | Outcome / correction or no change | Recheck / limit |
|---|---|---|---|---|---|
| The existing rescheduling tests omit same-time requests for cancelled and completed appointments. | `project/tests/test_rescheduling.py`; status guard in `Appointment.reschedule()`. | Checked the earlier same-time test and the non-scheduled test. The first uses a scheduled appointment; the second requests `NEW_TIME`. | Modify: keep the proposed cases but add them in a separate assurance file to preserve the Stage 10 suite. | Both new cases raised `ValueError` and preserved the stored appointment, time and status. No production change needed. | Both cases passed locally. The new tests cover the service call. |
| The existing patient lookup tests omit a whitespace-only ID. | `project/tests/test_services.py`; `PatientService.find_patient()`. | Checked the known-ID and unknown-ID tests. Neither calls the service with a whitespace-only ID. | Modify: add the proposed case to the separate assurance file and retain the existing lookup tests. | The new case raised `ValueError`; the existing unknown-ID check still passed. No production change needed. | The new service test passed locally. It does not test console output. |

No false/rejected suggestion, if applicable: No incorrect coverage claim was identified in the reviewed Copilot plan. I changed where the tests were added so the existing suites stayed intact.

Actual Copilot Ask prompt:

```text
Review these two proposed SmartCare Stage 11 assurance tests. Give me a plan only. Do not edit files, run tests, or make commits.

1. Rescheduling: Check whether any existing test requests the original time for a cancelled or completed appointment. If this is not covered, propose a test that expects ValueError and verifies that the stored time and status remain unchanged.
2. Patient lookup: Check whether any existing service or console test covers a whitespace-only patient ID. If this is not covered, propose a service test that expects ValueError. Keep the existing unknown-ID LookupError test.

For each case, name the files and tests you inspected, explain whether it is already covered, and identify the smallest test change that would add coverage. Keep the plan limited to tests. Stop after presenting the plan so I can review it before any edits.
```

Copilot response summary: Copilot identified both coverage gaps. It proposed extending the existing rescheduling test to check the original time for cancelled and completed appointments, and adding a whitespace-only ID test beside the existing unknown-ID test. I kept both cases but approved putting them in a separate `project/tests/test_assurance.py` file.

## H Dependency provenance and privacy review


| Dependency/artefact | Source | Purpose | Licence/provenance | Verified? | Decision | Evidence link |
|---|---|---|---|---|---|---|
| pytest 8.3.5 | Declared in `project/requirements-dev.txt`; upstream source listed in the installed package metadata. | Development test runner. | MIT, as reported by the installed package metadata. | Yes — the declared pin, `pytest --version`, and installed metadata all reported 8.3.5. | Retain the existing development dependency. Stage 11 did not add or change dependencies. | [pytest source](https://github.com/pytest-dev/pytest); local version and metadata output. |

Actual runtime imports / test-tool dependencies / versions checked:  I inspected imports in `project/smartcare/` and found only Python standard-library modules (`re`, `datetime`, and `enum`) and local `smartcare` modules. `project/requirements-dev.txt` pins `pytest==8.3.5`. From `project/`, the virtual environment reported Python 3.12.10 and pytest 8.3.5. The Stage 11 change added tests without changing the dependency declaration.

Secret/data/output/input/permission/minimisation checks and evidence: In `project/smartcare/console.py`, `find_patient_action()` asks for a patient ID and prints the matched ID and name. It then calls `show_patient()`, which prints both again. This is existing terminal output; Stage 11 did not change it or add logging. The new tests use synthetic names and IDs and contain no credentials. Agent editing was limited to `project/tests/test_assurance.py`, and I checked the resulting file and Git status. The new whitespace-only ID test checks service validation, not console output.

Requirements/model/code/tests/Stage 10 provenance links: Patient lookup is traceable from `PatientService.find_patient()` in `project/smartcare/services.py` to `project/smartcare/data_store.py` and `project/tests/test_services.py`. Rescheduling is traceable through [Issue #3](https://github.com/u3318026/ST1-Assignment-3-Group-Project/issues/3), [PR #4](https://github.com/u3318026/ST1-Assignment-3-Group-Project/pull/4), `project/smartcare/domain.py`, and `project/tests/test_rescheduling.py`. The Stage 11 checks are in `project/tests/test_assurance.py` at commit `410250721c41dda0f28c4129a2e7cc177d189141`.

Bias/hidden assumptions / name formats / unnecessary fields / accessibility / scheduling policy: The lookup assumes the operator knows the patient ID. The new test checks whitespace-only input; it does not assess name formats or console accessibility. The repeated display of the patient ID and name is a data-minimisation concern if the console is used with real records. The scheduling check is limited to same-time requests for cancelled and completed appointments.

Policy questions or unresolved provenance / responsible contact: No production change was made. If the console is ever used with real records, the project team should confirm whether displaying the patient ID and name twice is necessary and who may view that output. The exact Copilot model and extension version were not recorded; see Section G.

## I Independent review and final audit statement

Human reviewer / PR or diff link / feedback: Pending. Stage 11 test commit available for review: `410250721c41dda0f28c4129a2e7cc177d189141`.

Corrections and recheck / approval before integration: No production correction was needed in the cases tested. Independent review and approval are pending.

Overall decision: Not yet acceptable for integration. Local verification passed; independent review and approval are still required. The integrated version will be retested after merge.

Unresolved risks: The existing patient lookup console displays the patient ID and name twice. This is a data-minimisation concern if real records are used; see Section H.

Evidence supporting decision: The full suite passed 100 tests at `410250721c41dda0f28c4129a2e7cc177d189141`. Separate local runs passed 3 assurance, 16 Stage 10 and 81 common cases. Commands and results are recorded in Section D.

Remediation owner / action / status: Md Tahmid Ul Islam Tonmoy — obtain independent review, address any feedback and record the integrated retest. Pending.

Residual limitations and conditions of acceptance: The new tests verify service behaviour. They do not verify console accessibility or privacy with real patient records.

Accountable reviewer and PG member sign-off: PG owner: Md Tahmid Ul Islam Tonmoy. Independent reviewer and final sign-off: pending.

Integrated PG SHA / protected common SHA: Stage 11 integrated SHA: pending. Protected Stage 9 common SHA: `ad62e75f16a38e6ba2e7099391edfe526dff2872`.

## J Reflections

1. Which risk would have been easy to miss if you only checked whether tests passed? The 97-test baseline passed, but it did not check whether a cancelled or completed appointment could be rescheduled to its original time. If the same-time shortcut were moved before the status check, the service could incorrectly report success. The new test covers both statuses and checks that the stored appointment remains unchanged.

2. Which AI audit finding was false or overstated? If none, state honestly and explain verification. I did not identify a false claim in the Copilot plan I reviewed. I checked the existing tests and confirmed that they did not cover same-time requests for cancelled or completed appointments or a whitespace-only patient ID at the service layer. I changed where the tests were added so the earlier suites remained intact.

3. What evidence supports your final trust decision? I checked the saved test file against the approved scope and confirmed that no existing project files changed. The three new assurance cases, 16 Stage 10 cases and 81 common cases passed in separate runs. The full suite passed 100 tests at commit `4102507`. This supports accepting the local test changes for review. Final acceptance is pending independent review and an integrated retest.

## K Ten formative questions

1. What does least privilege mean? Give a person or tool only the access needed for the task. In Stage 11, I approved edits to one new test file and verified that existing project files were unchanged.

2. What is provenance in AI-assisted software engineering? Provenance is the record of where a contribution came from, how it was produced or changed, and who verified it. A prompt, an AI response, a Git diff and a test result can each provide part of that record.

3. What is data minimisation? Use, share and display only the data needed for the task. The assurance tests used synthetic records because real patient data was unnecessary.

4. What is dependency hallucination? It occurs when AI recommends a package, version or API that does not exist or misrepresents what it does. Check the package source and verify that the dependency is needed before adding it.

5. What is software supply-chain risk? It is the risk that software is affected by a compromised or unsuitable dependency, tool or distribution source. Passing tests alone does not establish that a new dependency is trustworthy.

6. What does the VERIFY framework ask students to do? Validate against requirements, examine the implementation, run meaningful tests, inspect risks and assumptions, check fit with architecture and policy, and remain responsible for the result.

7. What does the TRUST framework ask students to do? Trace the origin of a contribution, review what changed, understand how it works, check security and privacy, and test its behaviour before accepting it.

8. What does an AMBER AI-use classification mean in this course? The use may be allowed with conditions. Check the course rules, limit the scope, verify the output independently and record the assistance as required.

9. Who remains responsible for professionally accepted AI-assisted software? The people who review and accept the software remain accountable for it. An AI tool cannot take responsibility for their decision.

10. What is the Stage 11 engineering rule? Treat AI output as a proposal. Check it against the requirements, inspect the changes and their provenance, test the risks that matter, and record the evidence before accepting it.

## L Completion and Stage 12 handover


- [x] Actual SmartCare scope and human-first observations recorded.
- [x] All tutorial activities and every VERIFY/TRUST element complete.
- [x] At least two meaningful assurance tests with added-value explanations.
- [x] Real findings/no-findings and corrective actions or no-change evidence recorded.
- [x] Earlier assertions preserved; common and PG suites independently checked.
- [x] Copilot claims independently verified and actual decisions recorded honestly.
- [x] Dependency/provenance/privacy review and residual limits complete.
- [ ] Independent human review, integration and retest recorded.
- [x] All three reflections and ten formative questions answered.
- [ ] Accountable PG contribution/sign-off and protected UG pathway retained.

Unresolved issues / owner / handover action: Md Tahmid Ul Islam Tonmoy will request independent review of the Stage 11 changes, address any feedback, and record the integrated commit and retest after merge. The existing console displays the patient ID and name twice; see Section H for the limitation.

Tested code SHA / command / working directory / observed result: `410250721c41dda0f28c4129a2e7cc177d189141` — ran `../.venv/bin/python -m pytest -q` from `project/`. Result: 100 passed in 0.08s.

Final submitted SHA / later evidence-only change explanation: Pending. The tested SHA above identifies the assurance test commit. Record the final submitted SHA after integration and identify any later documentation-only updates.

Stage 12 handover links to same project/tests/assurance conclusion and limitations: [SmartCare project](../project/README.md), [Stage 11 assurance tests](../project/tests/test_assurance.py), and [Stage 10 rescheduling tests](../project/tests/test_rescheduling.py). Section D records the findings and test results; Section H records the privacy and provenance limitations. The tested cases required no production code fix.

Begin Stage 12 after the previous applicable stage is integrated, verified and recorded. Its handout and blank record are already supplied.
