import pytest
from smartcare.domain import Patient, Practitioner, Appointment
from datetime import datetime



#patient tests
def test_patient():
    patient = Patient(id="p1", name="John Doe")
    assert patient.id == "p1"
    assert patient.name == "John Doe"

def test_blank_patient_name():
    with pytest.raises(ValueError):
        Patient(id="p1", name="")

def test_blank_patient_ID():
    with pytest.raises(ValueError):
        Patient(id="", name="Jane Doe")

def test_empty_space_patient_name():
    with pytest.raises(ValueError):
        Patient(id="p1", name="   ")

def test_empty_space_patient_ID():
    with pytest.raises(ValueError):
        Patient(id="   ", name="Jane Doe")



# Practitioner tests
def test_practitioner():
    practitioner = Practitioner(id="pr1", name="Dr. Smith")
    assert practitioner.id == "pr1"
    assert practitioner.name == "Dr. Smith" 

def test_blank_practitioner_name():
    with pytest.raises(ValueError):
        Practitioner(id="pr1", name="")

def test_blank_practitioner_ID():
    with pytest.raises(ValueError):
        Practitioner(id="", name="Dr. Jones")

def test__empty_space_practitioner_name():
    with pytest.raises(ValueError):
        Practitioner(id="pr1", name="   ")

def test__empty_space_practitioner_ID():
    with pytest.raises(ValueError):
        Practitioner(id="   ", name="Dr. Jones")


#appointment tests
def appointment():
    patient = Patient(id="p1", name="John Doe")
    practitioner = Practitioner(id="pr1", name="Dr. Smith")
    appointment = Appointment(
        id="a1",
        patient=patient,
        practitioner=practitioner,
        date_time=datetime.now(),
    )
    assert appointment.id == "a1"
    assert appointment.patient == patient
    assert appointment.practitioner == practitioner

def test_new_appointment_scheduled():
    patient = Patient(id="p1", name="John Doe")
    practitioner = Practitioner(id="pr1", name="Dr. Smith")
    appointment = Appointment(
        id="a1",
        patient=patient,
        practitioner=practitioner,
        date_time=datetime.now(),
    )
    assert appointment.status == "scheduled"

def test_cancel_appointment():
    patient = Patient(id="p1", name="John Doe")
    practitioner = Practitioner(id="pr1", name="Dr. Smith")
    appointment = Appointment(
        id="a1",
        patient=patient,
        practitioner=practitioner,
        date_time=datetime.now(),
    )
    appointment.cancel()
    assert appointment.status == "cancelled"

def test_repeated_cancellation_request():
    patient = Patient(id="p1", name="John Doe")
    practitioner = Practitioner(id="pr1", name="Dr. Smith")
    appointment = Appointment(
        id="a1",
        patient=patient,
        practitioner=practitioner,
        date_time=datetime.now(),
    )
    appointment.cancel()
    with pytest.raises(ValueError):
        appointment.cancel()


def test_completed_appointment():
    patient = Patient(id="p1", name="John Doe")
    practitioner = Practitioner(id="pr1", name="Dr. Smith")
    appointment = Appointment(
        id="a1",
        patient=patient,
        practitioner=practitioner,
        date_time=datetime.now(),
    )
    appointment.complete()
    assert appointment.status == "completed"