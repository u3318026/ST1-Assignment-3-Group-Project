# Stage 7 Testing and Verification Record

Group/tutorial: Group 6 wednesday 2:30-4:30pm  Members/cohorts: Tamas Szucs, Ryan Grieves, Md Tahmid Ul Islam Tonmoy
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | test_register_patient checks if the patient is registered and stored | test_duplicate_patients checks for patients with duplicate ids | the patient ID and name match the stored data. |
| FR-05 Prevent practitioner conflict | test_book_appointment, checks successful booking | test_same_practitioner_at_the_same_time_isnt_allowed, checks for bookings with the same doctor at the same time | bookings at the same time will cause a valueerror for the second booking and keep the first one |
| FR-06 Cancel appointment | test_cancel_appointment checks cancellations | test_cancelled_appointment_cant_be_cancelled_again checks for repeated cancellations | first cancellation cancels it, causes value error on second attempt |
| FR-07 Retain cancelled history | test_cancelled_appointment_is_stored checks the cancelled appointment is stored | test_find_cancelled_appointment checks for cancelled appointments and makes sure you can still find them | appointment remains stored and findable if it is cancelled |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: Weak/unclear  Why: it always passes the assertion

`assert appointment is not None`
Judgement: Weak/unclear  Why: only tells us that an objct is there, doesnt tell us if the info is correct.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Strong for stated behaviour  Why: checks for the specific status that is required

`assert len(results) > 0`
Judgement: Weak/unclear  Why: proves atleast one result is there but not that the result is correct

`assert data_store.find_appointment('A1') is appointment`
Judgement: Strong for stated behaviour Why: checks that the data store is returning the same object

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: most would raise a value error and the rest would just reject it entirely. This is based off the testing and excepetions created in the starter code.

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | Assert appointment is not none | Book an appointment and check all of its variables |
| 2 | Assert appointment is not none | Find an appointment ID and check whether the corresponding patient and practitioner details are correct |
| 3 | Assert true | cancel the shedued appointment  and assert its status to cancelled |
| 4 | Assume sms notification exists | test the cancellation and retained history without thinking notification will work |
| 5 | Assume sms notification exists | verify that a repeated cancellation is rejected and the appointment remains cancelled |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
It can coexist because it is checking the code exectued and not the tests checked the correct behaviour. Could complete the entire executable but with weak assertions nothing will happen.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| Makes sure a patient exists | Patient Exists | test_patient() | test_domain.py | test for patient | Pass | Supplied | Positive |
| dont accept blank patient names | Patient name isnt blank | test_blank_patient_name() | test_domain.py | reject patients with a blank patient name | Pass | Supplied | Negative |
| dont accept blank patient IDs | Patient ID isnt blank | test_blank_patient_id() | test_domain.py | reject patients with a blank patient ID | Pass | Supplied | Negative |
| dont accept empty space patient names | Patient name isnt a empty space | test_empty_space_patient_name() | test_domain.py | reject patients with a empty space patient name | Pass | Supplied | Negative |
| dont accept empty space patient IDs | Patient ID isnt a empty space | test_empty_space_patient_ID() | test_domain.py | reject patients with a empty space patient id | Pass | Supplied | Negative |

| Makes sure a practitioner exists | Practitioner Exists | test_practitioner() | test_domain.py | test for practitioner | Pass | Supplied | Positive |
| dont accept blank practitioner names | Practitioner name isnt blank | test_blank_practitioner_name() | test_domain.py | reject practitioner with a blank patient name | Pass | Supplied | Negative |
| dont accept blank practitioner IDs | Practitioner ID isnt blank | test_blank_practitioner_id() | test_domain.py | reject practitioners with a blank patient ID | Pass | Supplied | Negative |
| dont accept empty space practitioner names | Practitioner name isnt a empty space | test_empty_space_practitioner_name() | test_domain.py | reject practitioners with a empty space patient name | Pass | Supplied | Negative |
| dont accept empty space practitioner IDs | Practitioner ID isnt a empty space | test_empty_space_practitioner_ID() | test_domain.py | reject practitioners with a empty space patient id | Pass | Supplied | Negative |
| dont accept empty space practitioner specialities  | Patient Exists | test_blank_pracitioner_Speciality() | test_domain.py | reject practitioners with a blank speicality | Pass | Supplied | Negative |
| dont accept blank practitioner Specialities  | Patient name isnt blank | test_empty_space_practitioner_Speciality() | test_domain.py | reject practitioners with a empty space speicality | Pass | Supplied | Negative |

| Makes sure a appointment exists | Appointment Exists | test_appointment() | test_domain.py | test for apointment | Pass | Supplied | Positive |
| make sure new appointment status is changed to scheduled | change status to scheduled | test_new_appointment_scheduled() | test_domain.py | changes appointment status to sheduled | Pass | Supplied | Positive |
| cancelling appointments | changed status from scheduled to cancelled | test_cancel_appointment() | test_domain.py | changes status of appointment | Pass | Supplied | Positive |
| cant double cancel a appointment | trying to cancel a cancelled appointment fails | test_repeated_cancellation_request() | test_domain.py | reject cancellations when appointment is already cancelled | Pass | Supplied | Negative |


| make sure that even though appointment is canelled, it is still stored | store cancelled appointment | test_cancelled_appointment_is_stored() | test_services.py | store cancelled appointments data | Pass | Supplied | Positive |
| dont accept bookings with same practitioner at the same time | double booking | test_same_practitioner_at_the_same_time_isnt_allowed() | test_services.py | reject appointments with same practitioners at the same time | Pass | Supplied | Negative |
| Allow appointmnets at same time with differnet practitioners | same time different pracitioner | test_same_time_different_practitioner_is_allowed() | test_services.py | allow people to book at same time so long as they are booking different practitioners | Pass | Supplied | Positive |
| dont accept appointments without patients | appointment without a patient | test_appointment_without_patient() | test_services.py | reject appointments without patients | Pass | Supplied | Negative |
| Find cancelled appointments | stored cancelled appointments can be found | test_find_cancelled_appointment() | test_services.py | find a cancelled appointment in data store | Pass | Supplied | Positive |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| test_patient() | test if patient is real | Positive | Passes if all areas are filled | intended to test existance | Pass | N/A |
| test_blank_patient_name() | test to make sure patient name is not empty | Negative | passes if noy empty patient name | intended to test for a name | Pass | N/A |
| test_blank_patient_id() | test to make sure patient id isnt empty | Negative | passes if not blank patient id | intended to test for id | Pass | N/A |
| test_empty_space_patient_name() | test to make sure patient name isnt a blank space | Negative | passes if not empty name space for patient | intended to test for a name | Pass | N/A |
| test_empty_space_patient_ID() | test to make sure patient name isnt a blank space | Negative | passes if not empty id space for patient | intended to test for a id | Pass | N/A |

| test_practitioner() | test if practitioner is real | Positive | Passes if all areas are filled | intended to test existance | Pass | N/A |
| test_blank_practitioner_name() | test to make sure practitioner name is not empty | Negative | passes if noy empty practitioner name | intended to test for a name | Pass | N/A |
| test_blank_pracitioner_ID() | test to make sure pratitioner id isnt empty | Negative | passes if not blank practitioner id | intended to test for id | Pass | N/A |
| test_empty_space_practitioner_name() | test to make sure pracitioner name isnt a blank space | Negative | passes if not empty name space for pracitioner | intended to test for a name | Pass | N/A |
| test_empty_space_practitioner_ID() | test to make sure practitioner name isnt a blank space | Negative | passes if not empty id space for practitioner | intended to test for a id | Pass | N/A |
| test_empty_space_practitioner_Speciality() | test to make sure practitioner speciality isnt a blank space | Negative | passes if not empty speciality space for practitioner | intended to test for a speciality | Pass | N/A |
| test_blank_pracitioner_Speciality() | test to make sure pratitioner speciality isnt empty | Negative | passes if not blank practitioner speciality | intended to test for speciality | Pass | N/A |

| test_appointment() | test if appointment is real | Positive | Passes if all areas are filled | intended to test existance | Pass | N/A |
| test_new_appointment_scheduled() | test to make sure appointment is scheduled properly | Negative | passes if all areas for a appointment are filled | intended to test for a sheduled appointments | Pass | N/A |
| test_cancel_appointment() | test to make sure you can cancel appointments| Positive | passes if appointment is cancelled and stored | intended to allow people to cancel appointments| Pass | N/A |
| test_repeated_cancellation_request() | test to make sure you cant cancel a cancelled appointment | Negative | passes if you rasie a value error on already cancelled appointments | intended to not allow cancelled appointments to be cancelled again | Pass | N/A |
| test_cancelled_appointment_is_stored() | test to make sure completed appointments are stored | Negative | passes if appointment is stored | intended to test for completed appointments| Pass | N/A |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| test_patient() | setup | create a patient | patient id name, oractitioner details, appointment details | proves patient can exist |
| test_blank_patient_name() | N/A | p1, "" | raise value error | proves patient cant exist without a specific string or integer |
| test_cancel_appointment() | AppointmentStatus.Scheduled | cancel the apointment | Appointment Status changed to cancel | proves appointments can be cancelled |
| test_appointment_without_patient() | Practitioner booked but patient not | book appointment with unknown patient | raise value error | makes sure you cant book without a patient |
| test_repeated_cancellation_request() | Cancelled appointment | cancel again | raise value error | makes sure you cant cancel twice |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| test_patient() | tests for exisiting patient | Test_domain.py | Pass |
| test_blank_patient_name() | tests for blank patient name | Test_domain.py | Pass |
| test_blank_patient_id() | tests for blank patient id | Test_domain.py | Pass |
| test_empty_space_patient_name() | tests for empty space patient name| Test_domain.py | Pass |
| test_empty_space_patient_ID() | tests for empty space patient id | Test_domain.py | Pass |

| test_practitioner() | tests for exisiting practitioner | Test_domain.py | Pass |
| test_blank_practitioner_name() | tests for blank practitioner name | Test_domain.py | Pass |
| test_blank_practitioner_id() | tests for blank practitioner id | Test_domain.py | Pass |
| test_empty_space_practitioner_name() | tests for empty space practitioner name| Test_domain.py | Pass |
| test_empty_space_practitioner_ID() | tests for empty space practitioner id | Test_domain.py | Pass |
| test_blank_practitioner_Speciality() | tests for blank practitioner speiciality| Test_domain.py | Pass |
| test_empty_space_practitioner_Speciality() | tests for empty space practitioner speciality | Test_domain.py | Pass |

| test_appointment() | tests for appointment | Test_domain.py | Pass |
| test_new_appointment_scheduled() | tests for new appointment | Test_domain.py | Pass |
| test_cancel_appointment() | tests for changing scheduled status to cancelled | Test_domain.py | Pass |
| test_repeated_cancellation_request() | tests for cancelled appointmnets cant be cancelled again | Test_domain.py | Pass |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| test_same_practitioner_at_the_same_time_isnt_allowed() | tests to make sure no 2 appointments are booked at the same time with the same practitioner | reject appointments at the same time with the same practitioner | Test_services.py | Pass |
| test_cancelled_appointment_is_stored() | tests for cancelled appointment is storing | Test_services.py | Pass |
| test_same_time_different_practitioner_is_allowed() | tests to allow same time different practitioner appointments | Pass appointments at same time different practitioner | Test_services.py | Pass |
| test_appointment_without_patient() | tests to find appointments linked to unknow patients | reject appointments with unknown patients | Test_services.py | Pass |
| test_find_cancelled_appointment() | tests to find appointments that have been canelled since they must be stored | return with the info on the cancelled appointment | Test_services.py | Pass |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| Patient | blank or empty space | raise value error | Test_patient(), test_blank_patient_name(). test_blank_patient_id(), test_empty_space_patient_name(), test_empty_space_patient_ID() |
| Practitioner | blank or empty space | raise value error | test_practitioner(), test_blank_practitioner_name(), test_blank_practitioner_id(), test_empty_space_practitioner_name(), test_empty_space_practitioner_ID(), test_blank_practitioner_Speciality(),  test_empty_space_practitioner_Speciality() |
| Appointment | blank or empty space | raise value error | test_unkown_appointment(), test_appointment_without_patient(), test_appointment_without_practitioner() |
| Practitioner conflicts | same practitioner same time | raise value error | test_same_practitioner_at_the_same_time_isnt_allowed() |
| timing isues | same time different practitioner | N/A | test_same_time_different_practitioner_is_allowed() |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: FR-06
Acceptance criterion: Cancelling a sheduled appointment will make the appointment status Cancelled
Behaviour to test: Cancelled appointments change to cancelled status
Human-first test idea/categories: Positive/negative
Prompt and purpose: Pretend you are a healthcare clinic, prove that when i am cancelling my appointment, the status of the appointment is correctly changed to CANCELLED.

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: Test a candidate and then Assert True
- What it claims to verify: that the cancellation works
- Requirement trace: FR-06
- Assertion quality: weak, Assert true
- Human critique: Passes regardless, needs to be more specific
- Decision: Modify
- Reason: Replace the assertion to appointment.status == AppointmentStatus.CANCELLED()
- Final test reference if accepted/modified: changed inside of test_services.py
- Actual verification result: Completed, Pass

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? the cancelling appointment, it lloked convincing but was weak since there was nothing exact it was testing for and it was too generic.
Why was it weak? Too generic
How did you strengthen it? Give it a more exact thing to test
Accepted / modified / rejected test decisions and evidence: Accepted, test_services.py

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| python -m pytest from project/ | project/ | c9e1736e29b845c6308a0b057f0c2af95fdd9d40 | Passed 45 | Failed 0 | O fails | N/A | see photo All tests passed.png |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? doesnt test the behavious of uncommon inputs like date and time.
Coverage if used: not used
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? Time boundaries and time status carry the coverage percentage because they are the ones establshing whether or not the appointment can happen
Optional fixtures/parametrisation used and why, if any: N/A

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| Stage 7 | Main | N/A | Tamas Szucs | N/A | All tests pass |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| Tamas Szucs | All of stage 7 | Commit history |

## N Formative Questions

1. What question does verification answer?
The question that is being answered when we are doing verification is are we making this correctly?

2. What question does validation answer?
The question that is being answered when we are validating is are we making the right thing? Is it what is needed?

3. What is a unit test?
A unit test is a test that checks for only one thing on any behaviour

4. What is a pytest fixture?
The pytest fixture is function that prepares test data, allowing it to be used in multiple test areas.

5. What is parametrisation in pytest?
Allows you to run the same test over again with different inputs

6. What is regression testing?
Re-running the tests to make sure that the code you added then didnt change any behaviours that were working before

7. What does code coverage tell us, and what does it not prove?
Tells us what was ran through the test, doesnt tell us if the assertion tests were correct.

8. What makes an assertion weak?
An assertion is weak if the what we are asserting is too generic.

9. What is the appropriate role of GitHub Copilot as a test assistant?
It is only appropriate to use github copilot as a test assistant when you are using it for reviewing your tests and giving possible suggestions

10. What is the Stage 7 engineering rule?
The engineering rule for stage 7 is to make sure your assertions are strong and tests must be traceable.

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: all 45 tests pass
Unresolved defects and effect on baseline: None
Clean working tree and integration evidence: Completed
Stage 8 handover status: Completed
All tutorial/formative responses and traceability/Copilot decisions complete: Completed
