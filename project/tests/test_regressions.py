from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (AppointmentService, PatientService, PractitionerService)

WHEN = datetime(2026, 10, 1, 9, 0)

@pytest.fixture #reuseable thingy
def services():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)
    patients.register_patient('P1', 'Alex Example')
    patients.register_patient('P2', 'Sam Example')
    practitioners.register_practitioner('D1', 'Taylor Example', 'General practice')
    practitioners.register_practitioner('D2', 'Jordan Example', 'Cardiology')
    return store, appointments


def test_f8_01_same_practitioner_same_time_is_rejected(services):
    store, appointments = services
    first = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    before = store.list_appointments()
    with pytest.raises(ValueError):
        appointments.book_appointment('A2', 'P2', 'D1', WHEN)
    assert store.list_appointments() == before
    assert store.find_appointment('A2') is None
    assert store.find_appointment('A1') is first


def test_f8_01_different_practitioner_same_time_is_allowed(services):
    store, appointments = services
    appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    second = appointments.book_appointment('A2', 'P1', 'D2', WHEN)
    assert second.practitioner.practitioner_id == 'D2'
    assert store.find_appointment('A2') is second


def test_f8_02_cancelled_appointment_is_still_found(services):
    store, appointments = services
    booked = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    cancelled = appointments.cancel_appointment('A1')
    assert cancelled is booked
    assert cancelled.status is AppointmentStatus.CANCELLED
    assert store.find_appointment('A1') is booked
    assert appointments.find_appointment('A1') is booked
    assert booked in store.list_appointments()


def test_f8_02_repeated_cancellation_is_rejected_without_change(services):
    store, appointments = services
    booked = appointments.book_appointment('A1', 'P1', 'D1', WHEN)
    appointments.cancel_appointment('A1')
    with pytest.raises(ValueError):
        appointments.cancel_appointment('A1')
    assert booked.status is AppointmentStatus.CANCELLED
    assert store.find_appointment('A1') is booked