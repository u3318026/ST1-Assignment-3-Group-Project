from datetime import datetime, timezone

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


OLD_TIME = datetime(2026, 10, 1, 9)
NEW_TIME = datetime(2026, 10, 1, 10)
RESCHEDULED_TIME = datetime(2026, 10, 1, 12)


@pytest.fixture
def setup():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)
    patient = patients.register_patient('P1', 'Alex Example')
    other_patient = patients.register_patient('P2', 'Sam Example')
    practitioner = practitioners.register_practitioner(
        'D1',
        'Taylor Example',
        'General practice',
    )
    other_practitioner = practitioners.register_practitioner(
        'D2',
        'Jordan Example',
        'Cardiology',
    )
    return (
        store,
        appointments,
        patient,
        other_patient,
        practitioner,
        other_practitioner,
    )


def test_reschedule_preserves_appointment_and_participant_identity(setup):
    store, appointments, patient, _, practitioner, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)

    result = appointments.reschedule_appointment(
        'A1',
        new_date_time=NEW_TIME,
    )

    assert result is booked
    assert result.appointment_id == 'A1'
    assert result.patient is patient
    assert result.practitioner is practitioner
    assert result.status is AppointmentStatus.SCHEDULED
    assert result.date_time == NEW_TIME
    assert store.find_appointment('A1') is booked


def test_same_time_reschedule_succeeds_without_changing_state(setup):
    store, appointments, _, _, _, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    before = (
        booked.appointment_id,
        booked.patient,
        booked.practitioner,
        booked.status,
        booked.date_time,
        store.list_appointments(),
    )

    result = appointments.reschedule_appointment(
        'A1',
        new_date_time=OLD_TIME,
    )

    assert result is booked
    assert (
        booked.appointment_id,
        booked.patient,
        booked.practitioner,
        booked.status,
        booked.date_time,
        store.list_appointments(),
    ) == before


def test_reschedule_excludes_target_and_different_practitioner_conflicts(
    setup,
):
    store, appointments, _, _, _, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    appointments.book_appointment('A2', 'P2', 'D2', NEW_TIME)

    assert appointments.reschedule_appointment(
        'A1',
        new_date_time=NEW_TIME,
    ) is booked
    assert booked.date_time == NEW_TIME
    assert store.find_appointment('A1') is booked


def test_conflicting_reschedule_is_rejected_without_changing_records(setup):
    store, appointments, _, _, _, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    conflicting = appointments.book_appointment('A2', 'P2', 'D1', NEW_TIME)
    before = store.list_appointments()
    booked_before = (
        booked.appointment_id,
        booked.patient,
        booked.practitioner,
        booked.status,
        booked.date_time,
    )

    with pytest.raises(ValueError):
        appointments.reschedule_appointment(
            'A1',
            new_date_time=NEW_TIME,
        )

    assert store.list_appointments() == before
    assert store.find_appointment('A1') is booked
    assert store.find_appointment('A2') is conflicting
    assert (
        booked.appointment_id,
        booked.patient,
        booked.practitioner,
        booked.status,
        booked.date_time,
    ) == booked_before


def test_invalid_time_is_rejected_before_conflict_check(setup, monkeypatch):
    _, appointments, _, _, _, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    conflict_check_called = False

    def conflict_check(*args, **kwargs):
        nonlocal conflict_check_called
        conflict_check_called = True
        return False

    monkeypatch.setattr(
        appointments.data_store,
        'has_practitioner_conflict',
        conflict_check,
    )

    with pytest.raises(ValueError):
        appointments.reschedule_appointment(
            'A1',
            new_date_time=datetime(2026, 10, 1, 10, 0, 30),
        )

    assert not conflict_check_called
    assert booked.date_time == OLD_TIME


@pytest.mark.parametrize(
    'bad_time',
    [
        None,
        '2026-10-01 10:00',
        datetime(2026, 10, 1, 10, tzinfo=timezone.utc),
        datetime(2026, 10, 1, 10, 0, 0, 1),
    ],
)
def test_domain_rejects_invalid_times_without_changing_appointment(
    setup,
    bad_time,
):
    _, appointments, _, _, _, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    before = (booked.date_time, booked.status)

    with pytest.raises(ValueError):
        booked.reschedule(new_date_time=bad_time)

    assert (booked.date_time, booked.status) == before


@pytest.mark.parametrize(
    'status',
    [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED],
)
def test_non_scheduled_appointment_cannot_be_rescheduled(setup, status):
    store, appointments, patient, _, practitioner, _ = setup
    from smartcare.domain import Appointment

    appointment = Appointment('A1', patient, practitioner, OLD_TIME, status)
    store.add_appointment(appointment)
    before = store.list_appointments()

    with pytest.raises(ValueError):
        appointments.reschedule_appointment(
            'A1',
            new_date_time=NEW_TIME,
        )

    assert store.list_appointments() == before
    assert appointment.date_time == OLD_TIME
    assert appointment.status is status


@pytest.mark.parametrize('bad_id', ['', '   ', None])
def test_invalid_appointment_id_is_rejected_without_changing_records(
    setup,
    bad_id,
):
    store, appointments, _, _, _, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    before = store.list_appointments()

    with pytest.raises(ValueError):
        appointments.reschedule_appointment(
            bad_id,
            new_date_time=NEW_TIME,
        )

    assert store.list_appointments() == before
    assert store.find_appointment('A1') is booked
    assert booked.date_time == OLD_TIME


def test_unknown_appointment_id_raises_lookup_error_without_changes(setup):
    store, appointments, _, _, _, _ = setup
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    before = store.list_appointments()

    with pytest.raises(LookupError):
        appointments.reschedule_appointment(
            'MISSING',
            new_date_time=NEW_TIME,
        )

    assert store.list_appointments() == before
    assert store.find_appointment('A1') is booked
    assert booked.date_time == OLD_TIME


def test_rescheduled_time_is_visible_sorted_and_old_slot_is_reusable(setup):
    store, appointments, _, _, _, _ = setup
    earlier = appointments.book_appointment(
        'A0',
        'P1',
        'D1',
        datetime(2026, 10, 1, 8),
    )
    booked = appointments.book_appointment('A1', 'P1', 'D1', OLD_TIME)
    later = appointments.book_appointment(
        'A3',
        'P2',
        'D1',
        datetime(2026, 10, 1, 11),
    )
    assert [item.appointment_id for item in
            appointments.list_practitioner_appointments('D1')] == [
                'A0', 'A1', 'A3',
            ]

    appointments.reschedule_appointment(
        'A1',
        new_date_time=RESCHEDULED_TIME,
    )

    found = appointments.find_appointment('A1')
    assert found is booked
    assert found.date_time == RESCHEDULED_TIME
    assert [item.appointment_id for item in
            appointments.list_practitioner_appointments('D1')] == [
                'A0', 'A3', 'A1',
            ]
    reused = appointments.book_appointment('A4', 'P2', 'D1', OLD_TIME)
    assert reused.date_time == OLD_TIME
    assert store.find_appointment('A1') is booked
    assert store.find_appointment('A4') is reused
    assert earlier.date_time < later.date_time < booked.date_time
