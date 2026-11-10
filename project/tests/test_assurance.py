from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


ORIGINAL_TIME = datetime(2026, 10, 1, 9)


@pytest.fixture
def setup():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)
    patient = patients.register_patient('P1', 'Alex Example')
    practitioner = practitioners.register_practitioner(
        'D1',
        'Taylor Example',
        'General practice',
    )
    return store, patients, appointments, patient, practitioner


@pytest.mark.parametrize(
    'status',
    [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED],
)
def test_non_scheduled_appointment_cannot_be_rescheduled_to_original_time(
    setup,
    status,
):
    store, _, appointments, patient, practitioner = setup
    appointment = Appointment(
        'A1',
        patient,
        practitioner,
        ORIGINAL_TIME,
        status,
    )
    store.add_appointment(appointment)

    with pytest.raises(ValueError):
        appointments.reschedule_appointment(
            'A1',
            new_date_time=ORIGINAL_TIME,
        )

    assert store.find_appointment('A1') is appointment
    assert appointment.date_time == ORIGINAL_TIME
    assert appointment.status is status


def test_find_patient_rejects_whitespace_only_id(setup):
    _, patients, _, _, _ = setup

    with pytest.raises(ValueError):
        patients.find_patient('   ')
