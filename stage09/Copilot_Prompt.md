Act as a query and console integration reviewer for SmartCare.Review the supplied code and tests for:1. explicit inputs, purity and source non-mutation;2. domain, service, data-store and console responsibilities;3. validation and recovery without partial state changes;4. correct object identity, enum filtering and ordering;5. retained history and integrity risks;6. missing query, workflow and console tests.Do not redesign the domain or add storage/frameworks.Do not invent fields or requirements or delete cancelled history.Separate observed evidence from optional improvements.Rank findings as Critical, Important or Optional.For each finding, identify the code/test evidence to check.Context (project rules):- Session-only, in-memory data. No database or files.- select_appointments must be pure: explicit inputs, returns a NEW list sorted by (date_time, appointment_id) using the named key appointment_sort_key, status None means every status, and it must not change the source list or objects.- list_practitioner_appointments: unknown practitioner gives LookupError, blank ID gives ValueError, a status that is not an AppointmentStatus gives ValueError, a known practitioner with no matches gives an empty list.- Cancelling keeps the appointment (status CANCELLED). It must still be found and listed.- A practitioner can't have two SCHEDULED appointments at the same time; different practitioners can.- The console converts typed status text to the enum and catches ValueError and LookupError only.Code (queries.py):"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    """Return the date/time and appointment ID ordering key without side
    effects.
    """
    return appointment.date_time, appointment.appointment_id


def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:
    """Return a new list for this practitioner, optionally filtered by
    status.

    Order by date/time then appointment ID using appointment_sort_key.
    Do not mutate the source list/objects or perform input/output.
    """
    selected = []
    for appointment in appointments:
        if appointment.practitioner.practitioner_id != practitioner_id:
            continue
        if status is not None and appointment.status is not status:
            continue
        selected.append(appointment)
    return sorted(selected, key=appointment_sort_key)Code (services.py):"""Simple workflows using a shared SmartCareDataStore object."""


from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.queries import select_appointments
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)


class PatientService:
    """Coordinate patient registration and lookup through the shared store."""

    def __init__(self, data_store: SmartCareDataStore) -> None:
        """Use the shared store to coordinate patient operations."""
        self.data_store = data_store

    def register_patient(self, patient_id: str, name: str) -> Patient:
        """Validate and register a patient, returning the stored object.

        Raise ValueError for invalid fields or an existing patient ID.
        """
        patient = Patient(patient_id, name)
        self.data_store.add_patient(patient)
        return patient

    def find_patient(self, patient_id: str) -> Patient:
        """Stage 6 TODO: return the stored patient for a valid patient ID.

        Completion must raise LookupError for absence and ValueError for
        a blank/invalid ID. It must not create a replacement patient.
        The starter deliberately raises NotImplementedError.
        """
        if not isinstance(patient_id, str) or not patient_id.strip():
            raise ValueError("Patient ID cannot be blank")
        patient = self.data_store.find_patient(patient_id)
        if patient is None:
            raise LookupError("Patient doesnt exist")
        return patient


class PractitionerService:
    """Coordinate practitioner registration and lookup through the shared
    store.
    """

    def __init__(self, data_store: SmartCareDataStore) -> None:
        """Use the shared store to coordinate practitioner operations."""
        self.data_store = data_store

    def register_practitioner(
        self,
        practitioner_id: str,
        name: str,
        specialty: str,
    ) -> Practitioner:
        """Validate and register a practitioner, returning the stored
        object.

        Raise ValueError for invalid fields or an existing practitioner
        ID.
        """
        practitioner = Practitioner(practitioner_id, name, specialty)
        self.data_store.add_practitioner(practitioner)
        return practitioner

    def find_practitioner(self, practitioner_id: str) -> Practitioner:
        """Stage 6 TODO: return the stored practitioner for a valid ID.

        Completion must raise LookupError for absence and ValueError for
        a blank/invalid ID. It must not create a replacement
        practitioner. The starter deliberately raises
        NotImplementedError.
        """
        if not isinstance(practitioner_id, str) or not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be blank")
        practitioner = self.data_store.find_practitioner(practitioner_id)
        if practitioner is None:
            raise LookupError("Practitioner doesnt exist")
        return practitioner

class AppointmentService:
    """Coordinate booking, lookup and cancellation using the shared store."""

    def __init__(self, data_store: SmartCareDataStore) -> None:
        """Use the shared store to coordinate appointment operations."""
        self.data_store = data_store

    def book_appointment(
        self,
        appointment_id: str,
        patient_id: str,
        practitioner_id: str,
        date_time: datetime,
    ) -> Appointment:
        """Book registered participant IDs and return the stored
        appointment.

        Raise LookupError for absent participants. Raise ValueError for
        invalid values, duplicate appointment IDs or a practitioner
        conflict.
        """
        patient = self.data_store.find_patient(patient_id)
        practitioner = self.data_store.find_practitioner(practitioner_id)
        if patient is None:
            raise LookupError('Patient not found')
        if practitioner is None:
            raise LookupError('Practitioner not found')
        appointment = Appointment(
            appointment_id,
            patient,
            practitioner,
            date_time,
        )
        if self.data_store.find_appointment(
            appointment.appointment_id,
        ) is not None:
            raise ValueError('Appointment ID already exists')
        if self.data_store.has_practitioner_conflict(
            practitioner.practitioner_id,
            date_time,
        ):
            raise ValueError(
                'Practitioner already has a SCHEDULED appointment at this time',
            )
        self.data_store.add_appointment(appointment)
        return appointment

    def find_appointment(self, appointment_id: str) -> Appointment:
        """Return the stored appointment; raise LookupError when absent.

        Reject a blank or invalid ID with ValueError; do not create
        records.
        """
        appointment = self.data_store.find_appointment(appointment_id)
        if appointment is None:
            raise LookupError('Appointment not found')
        return appointment

    def cancel_appointment(self, appointment_id: str) -> Appointment:
        """Stage 6: cancel through the domain method and retain the
        appointment.

        Return the cancelled object. Unknown IDs raise LookupError;
        invalid transitions raise ValueError and leave state unchanged.
        """
        if not isinstance(appointment_id, str) or not appointment_id.strip():
            raise ValueError("Appointment ID Invalid")

        if self.data_store.find_appointment(appointment_id) is None:
            raise LookupError("Unknown appointment ID")

        appointment = self.find_appointment(appointment_id)
        appointment.cancel()
        return appointment

    def list_practitioner_appointments(self, practitioner_id: str, status: AppointmentStatus | None = None) -> list[Appointment]:
        practitioner = self.data_store.find_practitioner(practitioner_id)
        if practitioner is None:
            raise LookupError('Practitioner not found!')
        if status is not None and not isinstance(status, AppointmentStatus):
            raise ValueError('Status must be an AppointmentStatus or None.')
        return select_appointments(self.data_store.list_appointments(), practitioner.practitioner_id, status)Tests (test_queries.py and test_workflows.py):from datetime import datetime

from smartcare.domain import(Appointment, AppointmentStatus, Patient, Practitioner)
from smartcare.queries import appointment_sort_key, select_appointments

PATIENT = Patient("P1", "Harry")
D1 = Practitioner("D1", "House", "MDing")
D2 = Practitioner("D2", "Martin", "Time Travel")
NINE = datetime(1955, 10, 9, 0, 0)
TEN = datetime(1985, 6, 5, 5, 0)

def make(appointment_id, practitioner, when, status=AppointmentStatus.SCHEDULED):
    return Appointment(appointment_id, PATIENT, practitioner, when, status)

def test_sort_key_is_date_time_then_id():
    appointment = make('A1', D1, NINE)
    assert appointment_sort_key(appointment) == (NINE, 'A1')

def test_only_requested_practitioner_is_returned():
    a1 = make('A1', D1, NINE)
    a2 = make('A2', D2, NINE)
    assert select_appointments([a1, a2], 'D1') == [a1]

def test_default_includes_every_status():
    scheduled = make('A1', D1, NINE)
    cancelled = make('A2', D1, TEN, AppointmentStatus.CANCELLED)
    completed = make('A3', D1, TEN, AppointmentStatus.COMPLETED)
    result = select_appointments([scheduled, cancelled, completed], 'D1')
    assert len(result) == 3

def test_each_status_filter_returns_only_that_status():
    scheduled = make('A1', D1, NINE)
    cancelled = make('A2', D1, TEN, AppointmentStatus.CANCELLED)
    completed = make('A3', D1, TEN, AppointmentStatus.COMPLETED)
    source = [scheduled, cancelled, completed]
    assert select_appointments(
        source, 'D1', AppointmentStatus.SCHEDULED) == [scheduled]
    assert select_appointments(
        source, 'D1', AppointmentStatus.CANCELLED) == [cancelled]
    assert select_appointments(
        source, 'D1', AppointmentStatus.COMPLETED) == [completed]

def test_no_match_gives_empty_list():
    a1 = make('A1', D1, NINE)
    assert select_appointments([a1], 'D1', AppointmentStatus.CANCELLED) == []

def test_sorted_by_time_then_id_for_equal_times():
    late = make('A9', D1, TEN)
    second = make('A2', D1, NINE, AppointmentStatus.CANCELLED)
    first = make('A1', D1, NINE)
    result = select_appointments([late, second, first], 'D1')
    assert [a.appointment_id for a in result] == ['A1', 'A2', 'A9']

def test_source_list_and_objects_are_unchanged():
    source = [make('A2', D1, TEN), make('A1', D1, NINE)]
    order_before = [a.appointment_id for a in source]
    fields_before = [(a.appointment_id, a.date_time, a.status)
                     for a in source]
    select_appointments(source, 'D1')
    assert [a.appointment_id for a in source] == order_before
    assert [(a.appointment_id, a.date_time, a.status)
            for a in source] == fields_before

def test_result_is_a_new_list_with_the_same_objects():
    a1 = make('A1', D1, NINE)
    source = [a1]
    result = select_appointments(source, 'D1')
    assert result is not source
    assert result[0] is a1

def test_empty_input_gives_a_new_empty_list():
    source = []
    result = select_appointments(source, 'D1')
    assert result == []
    assert result is not source

def test_repeated_calls_give_the_same_result():
    source = [make('A2', D1, TEN), make('A1', D1, NINE)]
    first = select_appointments(source, 'D1')
    second = select_appointments(source, 'D1')
    assert first == second

def test_result_order_matches_the_named_key():
    source = [make('A2', D1, TEN), make('A1', D1, NINE)]
    assert select_appointments(source, 'D1') == sorted(
        source, key=appointment_sort_key)

def test_already_sorted_input_gives_a_new_list():
    a1 = make('A1', D1, NINE)
    a2 = make('A2', D1, TEN)
    source = [a1, a2]
    result = select_appointments(source, 'D1')
    assert result == [a1, a2]
    assert result is not sourcefrom datetime import datetime

import pytest
import builtins

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (AppointmentService, PatientService, PractitionerService)
from smartcare.console import run_menu

WHEN = datetime(1955, 10, 9, 0, 0)

@pytest.fixture
def setup():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)
    patients.register_patient('P1', 'Harry')
    patients.register_patient('P2', 'Barry')
    practitioners.register_practitioner('D1', 'House', 'MDing')
    practitioners.register_practitioner('D2', 'Martin', 'Time Travel')
    return store, appointments

def test_known_practitioner_with_no_appointments_gives_empty_list(setup):
    store, appointments = setup
    result = appointments.list_practitioner_appointments('D1')
    assert result == []


def test_unknown_practitioner_raises_lookup_error(setup):
    store, appointments = setup
    with pytest.raises(LookupError):
        appointments.list_practitioner_appointments('NOPE')


def test_blank_practitioner_id_raises_value_error(setup):
    store, appointments = setup
    with pytest.raises(ValueError):
        appointments.list_practitioner_appointments('   ')


def test_text_status_raises_value_error_not_empty_list(setup):
    store, appointments = setup
    appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    with pytest.raises(ValueError):
        appointments.list_practitioner_appointments('D1', 'scheduled')


def test_id_with_spaces_still_finds_appointments(setup):
    store, appointments = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    assert appointments.list_practitioner_appointments(' D1 ') == [booked]


def test_listing_returns_a_new_list_with_the_same_objects(setup):
    store, appointments = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    result = appointments.list_practitioner_appointments('D1')
    assert result is not store.list_appointments()
    assert result[0] is booked


def test_cancelled_appointment_is_kept_found_and_listed(setup):
    store, appointments = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    appointments.cancel_appointment('A1')
    assert store.find_appointment('A1') is booked
    assert appointments.find_appointment('A1') is booked
    assert booked.status is AppointmentStatus.CANCELLED
    assert appointments.list_practitioner_appointments('D1') == [booked]
    assert appointments.list_practitioner_appointments(
        'D1', AppointmentStatus.CANCELLED) == [booked]
    assert appointments.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED) == []


def test_repeated_cancel_is_rejected_and_nothing_changes(setup):
    store, appointments = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    appointments.cancel_appointment('A1')
    with pytest.raises(ValueError):
        appointments.cancel_appointment('A1')
    assert booked.status is AppointmentStatus.CANCELLED
    assert store.list_appointments() == [booked]


def test_same_practitioner_conflict_is_rejected_and_nothing_changes(setup):
    store, appointments = setup
    first = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    with pytest.raises(ValueError):
        appointments.book_appointment('A2', 'P2', 'D1', WHEN)
    assert store.list_appointments() == [first]
    assert store.find_appointment('A2') is None


def test_different_practitioner_at_same_time_is_allowed(setup):
    store, appointments = setup
    first = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    second = appointments.book_appointment('A2', 'P1', 'D2', WHEN)
    assert store.list_appointments() == [first, second]


def test_duplicate_appointment_id_is_rejected_and_nothing_changes(setup):
    store, appointments = setup
    first = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    with pytest.raises(ValueError):
        appointments.book_appointment('A1', 'P2', 'D2', WHEN)
    assert store.list_appointments() == [first]
    assert store.find_appointment('A1') is first


def test_unknown_patient_or_practitioner_is_rejected_and_nothing_changes(setup):
    store, appointments = setup
    with pytest.raises(LookupError):
        appointments.book_appointment('A1', 'NOPE', 'D1', WHEN)
    with pytest.raises(LookupError):
        appointments.book_appointment('A1', 'P1', 'NOPE', WHEN)
    assert store.list_appointments() == []


def test_failed_booking_does_not_reserve_the_id(setup):
    store, appointments = setup
    bad_time = datetime(1955, 10, 9, 0, 0, 30)
    with pytest.raises(ValueError):
        appointments.book_appointment('A1', 'P1', 'D1', bad_time)
    assert store.find_appointment('A1') is None
    good = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    assert store.find_appointment('A1') is good

def test_freed_slot_can_be_booked_again_and_history_stays(setup):
    store, appointments = setup
    first = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    appointments.cancel_appointment('A1')
    third = appointments.book_appointment('A3', 'P1', 'D1', WHEN)
    assert appointments.list_practitioner_appointments('D1') == [first, third]
    assert appointments.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED) == [third]

def run_menu_with(monkeypatch, capsys, lines):
    answers = iter(lines)
    monkeypatch.setattr(builtins, 'input', lambda prompt='': next(answers))
    run_menu()
    return capsys.readouterr().out


def test_menu_full_workflow(monkeypatch, capsys):
    out = run_menu_with(monkeypatch, capsys, [
        '1', 'P1', 'Alex Example',
        '3', 'D1', 'Taylor Example', 'General practice',
        '3', 'D2', 'Jordan Example', 'Cardiology',
        '5', 'A1', 'P1', 'D1', '2026-10-01 09:00',
        '5', 'A-CONFLICT', 'P1', 'D1', '2026-10-01 09:00',
        '5', 'A2', 'P1', 'D2', '2026-10-01 09:00',
        '6', 'A1',
        '7', 'A1',
        '8', 'D1', '',
        '8', 'D1', 'scheduled',
        '5', 'A3', 'P1', 'D1', '2026-10-01 09:00',
        '0',
    ])
    assert ('Error: Practitioner already has a SCHEDULED appointment '
            'at this time') in out
    assert 'Appointment cancelled successfully.' in out
    assert 'Status         : Cancelled' in out
    assert 'No appointments found.' in out
    assert out.count('Appointment booked successfully.') == 3
    assert 'Goodbye. Session data discarded.' in out


def test_menu_recovers_from_bad_input(monkeypatch, capsys):
    out = run_menu_with(monkeypatch, capsys, [
        '1', 'P1', 'Alex Example',
        '3', 'D1', 'Taylor Example', 'General practice',
        '99',
        '5', 'BAD', 'P1', 'D1', 'not a date',
        '5', 'BAD', 'P1', 'D1', '2026-10-01 09:00',
        '8', 'D1', 'pending',
        '2', 'P1',
        '0',
    ])
    assert 'Unknown choice. Choose a number from 0 to 8.' in out
    assert 'Error: Use date/time format YYYY-MM-DD HH:MM' in out
    assert out.count('Appointment booked successfully.') == 1
    assert 'Error: Status must be scheduled, cancelled or completed' in out
    assert 'Patient found. P1: Alex Example' in outTest result: ..............................................................................                                                                                                                                              [100%]
78 passed in 0.06s