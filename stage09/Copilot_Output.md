SmartCare Review

Scope reviewed against the stated SmartCare rules only. Findings are separated into Observed Evidence (rule compliance issues or gaps evidenced by the supplied code/tests) and Optional Improvements (non-required quality improvements).

Summary

The query implementation (select_appointments) appears compliant with the stated Stage 9 requirements and is well covered by tests.

The primary concern is in list_practitioner_appointments, where the implementation does not appear to satisfy the documented contract for blank practitioner IDs and whitespace handling. Existing tests suggest a mismatch between the service implementation and the intended specification.

No Critical defects were identified from the supplied code alone, but several Important contract and test-coverage gaps exist.

Observed Evidence
Important: list_practitioner_appointments does not implement the documented blank-ID contract
Rule

blank ID gives ValueError

Implementation
def list_practitioner_appointments(
    self,
    practitioner_id: str,
    status: AppointmentStatus | None = None
) -> listpractitioner = self.data_store.find_practitioner(practitioner_id)
    if practitioner is None:
        raise LookupError('Practitioner not found!')


There is no explicit validation of:

not isinstance(practitioner_id, str)
not practitioner_id.strip()


Unlike the other service lookup methods.

Risk

A blank ID may be delegated directly to the datastore and produce:

LookupError


instead of the required:

ValueError


depending on datastore behaviour.

Evidence to Check

Verify actual runtime behaviour of:

appointments.list_practitioner_appointments("")
appointments.list_practitioner_appointments("   ")
appointments.list_practitioner_appointments(None)


and confirm exceptions match the project contract.

Related Test Evidence

The suite contains:

test_blank_practitioner_id_raises_value_error


but the implementation shown does not obviously satisfy it.

This suggests either:

datastore is performing validation, or
code shown is not the exact code tested.

Either way, responsibility appears misplaced (see next finding).

Important: Service responsibility is partially delegated to datastore
Rule Category

Domain / Service / Data-store responsibility separation

Observation

The service contract requires:

blank ID -> ValueError
unknown practitioner -> LookupError


but the service currently determines both outcomes indirectly via:

self.data_store.find_practitioner(practitioner_id)


before validating the input.

The service layer should be the location enforcing workflow contracts.

Risk

If datastore behaviour changes, service exception behaviour changes.

Evidence to Check

Inspect:

SmartCareDataStore.find_practitioner()


and determine whether service behaviour relies on datastore validation.

Important: Whitespace practitioner IDs appear inconsistent with the stated contract
Rule

The requirements only state:

blank ID -> ValueError
unknown practitioner -> LookupError

Test Evidence
assert appointments.list_practitioner_appointments(' D1 ') == [booked]

Observation

The test requires automatic trimming:

' D1 '


to resolve to

'D1'


but the service implementation shown performs no trimming.

Risk

Either:

hidden datastore normalization exists, or
the test and implementation shown do not correspond.

More importantly, whitespace-normalization is being treated as a requirement although it is not present in the supplied project rules.

Evidence to Check

Verify whether practitioner IDs are intended to be:

exact identifiers, or
normalized identifiers.

Review datastore lookup implementation.

Important: Missing validation test for non-enum status with None distinction
Rule
status None means every status
status not AppointmentStatus -> ValueError

Existing Coverage

Covered for:

"scheduled"


Covered for:

None

Missing Evidence

No tests shown for:

123
object()
[]

Risk

A loose implementation could accidentally accept non-enum values.

Evidence to Check

Add tests verifying:

with pytest.raises(ValueError):
    appointments.list_practitioner_appointments("D1", 123)


and similar invalid values.

Important: Missing explicit test that cancelled appointments participate in ordering
Rule
Cancelled appointments must still be found and listed.

Existing Coverage

Cancellation retention is tested.

Sorting is tested.

However no test combines:

cancelled appointments,
scheduled appointments,
same practitioner,
ordering requirements.
Risk

Future code could accidentally special-case cancelled appointments during query selection.

Evidence to Check

Create appointments with mixed statuses and verify:

select_appointments(...)


orders solely by:

(date_time, appointment_id)


regardless of status.

Important: Missing object identity verification for filtered multi-item results
Rule

Query must not mutate or replace objects.

Existing Coverage

Covered for:

result[0] is a1

Gap

Only tested with a single returned object.

Risk

A future implementation could inadvertently clone objects during filtering.

Evidence to Check

Add test:

a1
a2


returned together and verify:

result[0] is a1
result[1] is a2


after sorting/filtering.

Important: Console integration contract not fully exercised
Rule
Console converts typed status text to the enum.
Console catches ValueError and LookupError only.

Existing Coverage

Covered:

scheduled
pending


indirectly.

Missing Evidence

No test explicitly proves conversion to:

AppointmentStatus.SCHEDULED
AppointmentStatus.CANCELLED
AppointmentStatus.COMPLETED


before calling the service.

Risk

Console could pass strings to the service while still accidentally satisfying portions of the workflow tests.

Evidence to Check

Add console tests for:

cancelled
completed


and verify successful listings.

Optional Improvements

These are not rule violations from the supplied requirements.

Optional: Add purity regression tests around identity and source integrity

Current coverage is good.

Additional checks could verify:

id(source[i])


before and after query execution.

Reason: strengthens protection against future refactoring.

Optional: Add explicit query contract tests for practitioner mismatch + status mismatch

Examples:

wrong practitioner + matching status
correct practitioner + wrong status


Current behaviour is implied but not exhaustively tested.

Optional: Add explicit stable-history workflow test with multiple cancellations

The current retention rule is covered for a single appointment.

A stronger regression test could verify:

A1 CANCELLED
A2 CANCELLED
A3 SCHEDULED


all remain discoverable through appropriate queries.

This protects against future deletion-style cancellation implementations.

Assessment by Category
Area	AssessmentExplicit inputs	Mostly compliant
Query purity	Compliant and well tested
Source non-mutation	Compliant and well tested
Service responsibilities	Some responsibility leakage to datastore
Validation	Gap around practitioner ID validation responsibility
Recovery/no partial state changes	Well tested
Object identity	Mostly covered; more multi-item identity tests desirable
Enum filtering	Compliant; additional invalid-value tests desirable
Ordering	Compliant and well tested
Retained history	Compliant; cancellation retention verified
Console integration	Partially covered; enum-conversion coverage incomplete
Ranking
Critical

None identified from supplied evidence.

Important
list_practitioner_appointments lacks explicit practitioner-ID validation.
Service contract appears dependent on datastore behaviour.
Whitespace-ID behaviour is inconsistent with the supplied contract.
Missing invalid-status coverage beyond text values.
Missing ordering tests involving cancelled appointments.
Missing multi-object identity verification.
Missing explicit console enum-conversion tests.
Optional
Additional purity/identity regression tests.
Additional practitioner/status combination query tests.
Stronger retained-history regression tests involving multiple cancellations.