import pytest
from smartcare.domain import Patient, Practitioner, Appointment, AppointmentStatus
from datetime import datetime

#imports everything needed for the tests

date = datetime(2026, 10, 26, 0) #date and time

#creates a patient object with default values for testing
def make_patient(id: str = "p1", name: str = "John Doe") -> Patient:
    return Patient(id, name)

#creates a practitioner object with default values for testing
def make_practitioner(id: str = "pr1", name: str = "Dr. Smith", specialty: str = "General") -> Practitioner:
    return Practitioner(id, name, specialty)

#creates an appointment object with default values for testing
def make_appointment(status: str, AppointmentStatus = AppointmentStatus.SCHEDULED,) -> Appointment:
    return Appointment('a1', make_patient(), make_practitioner(), date, status)


#patient tests
#testing to make sure that the patient is created correctly and stored under patient
def test_patient():
    patient = make_patient(id="p1", name="John Doe")
    assert patient.patient_id == "p1"
    assert patient.name == "John Doe"

#testing to make sure that the patient name is not blank
def test_blank_patient_name():
    with pytest.raises(ValueError):
        Patient("p1", "")

#testing to make sure that the patient ID is not blank
def test_blank_patient_ID():
    with pytest.raises(ValueError):
        Patient("", "John Doe")

#testing to make sure that the patient name is not empty space
def test_empty_space_patient_name():
    with pytest.raises(ValueError):
        Patient("p1", "   ")

#testing to make sure that the patient ID is not empty space
def test_empty_space_patient_ID():
    with pytest.raises(ValueError):
        Patient("   ", "John Doe")



# Practitioner tests
#testing to make sure that the practitioner is created correctly and stored under practitioner
def test_practitioner():
    practitioner = make_practitioner(id="pr1", name="Dr. Smith", specialty="General")
    assert practitioner.practitioner_id == "pr1"
    assert practitioner.name == "Dr. Smith"
    assert practitioner.specialty == "General"

#testing to make sure that the practitioner name is not blank
def test_blank_practitioner_name():
    with pytest.raises(ValueError):
        Practitioner("pr1", "", "General")

#testing to make sure that the practitioner ID is not blank
def test_blank_practitioner_ID():
    with pytest.raises(ValueError):
        Practitioner("", "Dr. Jones", "General")

#testing to make sure that the practitioner specialty is not blank
def test_blank_Specialtiy():
    with pytest.raises(ValueError):
        Practitioner("pr1", "Dr. Jones", "")

#testing to make sure that the practitioner name is not empty space
def test__empty_space_practitioner_name():
    with pytest.raises(ValueError):
        Practitioner("pr1", "   ", "General")

#testing to make sure that the practitioner ID is not empty space
def test__empty_space_practitioner_ID():
    with pytest.raises(ValueError):
        Practitioner("   ", "Dr. Jones", "General")

#testing to make sure that the practitioner specialty is not empty space
def test__empty_space_Speciality():
    with pytest.raises(ValueError):
        Practitioner("pr1", "Dr. Jones", "   ")


#appointment tests
#testing to make sure that the appointment is created correctly and stored under appointment
def test_appointment():
    appointment = make_appointment(status=AppointmentStatus.SCHEDULED)
    assert appointment.appointment_id == "a1"
    assert appointment.patient.patient_id == "p1"
    assert appointment.practitioner.practitioner_id == "pr1"

#testing to make sure that the appointment status is SCHEDULED
def test_new_appointment_scheduled():
    assert make_appointment(status=AppointmentStatus.SCHEDULED).status == AppointmentStatus.SCHEDULED

#testing to make sure that the appointment status is CANCELLED
def test_cancel_appointment():
    appointment = make_appointment(status=AppointmentStatus.SCHEDULED)
    appointment.cancel()
    assert appointment.status == AppointmentStatus.CANCELLED

#testing to make sure that the appointment status is not changed when trying to cancel a completed appointment
def test_repeated_cancellation_request():
    appointment = make_appointment(status=AppointmentStatus.SCHEDULED)
    appointment.cancel()
    with pytest.raises(ValueError):
        appointment.cancel()

#testing to make sure that the appointment status is COMPLETED
def test_completed_appointment():
    appointment = make_appointment(status=AppointmentStatus.COMPLETED)
    assert appointment.status == AppointmentStatus.COMPLETED