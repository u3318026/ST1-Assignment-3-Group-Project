from datetime import datetime

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
    assert 'Patient found. P1: Alex Example' in out
