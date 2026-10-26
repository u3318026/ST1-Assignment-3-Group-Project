from datetime import datetime
from smartcare.data_store import SmartCareDataStore
from smartcare.domain import(AppointmentStatus)
from smartcare.services import(PatientService, PractitionerService, AppointmentService)
import pytest

#Import all necessary files needed for testing ^^^^^^^^^^^^^^^^^^^^


date = datetime(2026, 10, 26, 0) #date and time

#setup for the tests, makes sure that every test has a new testing environemnt
def setup():
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)
    return data_store, patient_service, practitioner_service, appointment_service

#setup for the tests, makes sure that every test has a new testing environemnt with an appointment already booked
def setup_with_appointment():
    data_store, patient_service, practitioner_service, appointment_service = setup()
    patient = patient_service.register_patient("p1", "John Doe")
    practitioner = practitioner_service.register_practitioner("pr1", "Dr. Smith", "General")
    appointment = appointment_service.book_appointment("a1", patient.patient_id, practitioner.practitioner_id, date)
    return data_store, patient_service, practitioner_service, appointment_service, appointment


#Patient Tets
#Testing to make sure that the patient is registered correctly and that the data is stored in the data store
def test_register_patient():
    data_store, patient_service, _, _ = setup()
    patient = patient_service.register_patient("p1", "John Doe")
    assert patient.patient_id == "p1"
    assert patient.name == "John Doe"
    assert data_store.find_patient("p1") == patient

#testing to make sure that the patient is not registered twice and that the original patient is preserved
def test_duplicate_patient():
    data_store, patient_service, _, _ = setup()
    patient_service.register_patient("p1", "John Doe")
    with pytest.raises(ValueError):
        patient_service.register_patient("p1", "Jane Doe")

#tests to make sure that the patient ID isnt blank
def test_blank_patient_ID():
    data_store, patient_service, _, _ = setup()
    with pytest.raises(ValueError):
        patient_service.register_patient("", "John Doe")

#tests to make sure that the patient name is not blank
def test_blank_patient_name():
    data_store, patient_service, _, _ = setup()
    with pytest.raises(ValueError):
        patient_service.register_patient("p1", "")  

#tests to make sure that the patient ID and name findable
def test_find_patient():
    data_store, patient_service, _, _ = setup()
    patient_service.register_patient("p1", "John Doe")
    patient = patient_service.find_patient("p1")
    assert patient.patient_id == "p1"
    assert patient.name == "John Doe"

#tests to make sure that the if there is a unknow patient then we can raise a LookupError
def test_unknown_patient():
    data_store, patient_service, _, _ = setup()
    with pytest.raises(LookupError):
        patient_service.find_patient("unknown")


#practitioner Tets
#tests to make sure that the practitioner is registered correctly and that the data is stored in the data store
def test_registered_practitioner():
    data_store, _, practitioner_service, _ = setup()
    practitioner = practitioner_service.register_practitioner("pr1", "Dr. Smith", "General")
    assert practitioner.practitioner_id == "pr1"
    assert practitioner.name == "Dr. Smith"
    assert practitioner.specialty == "General"
    assert data_store.find_practitioner("pr1") == practitioner

#tests to make sure that the practitioner is not registered twice and that the original practitioner is preserved
def test_duplicate_practitioner():
    data_store, _, practitioner_service, _ = setup()
    practitioner_service.register_practitioner("pr1", "Dr. Smith", "General")
    with pytest.raises(ValueError):
        practitioner_service.register_practitioner("pr1", "Dr. Jones", "Specialty")

#tests to make sure that the practitioner is findable
def test_find_practitioner():
    data_store, _, practitioner_service, _ = setup()
    practitioner_service.register_practitioner("pr1", "Dr. Smith", "General")
    practitioner = practitioner_service.find_practitioner("pr1")
    assert practitioner.practitioner_id == "pr1"
    assert practitioner.name == "Dr. Smith"
    assert practitioner.specialty == "General"

#tests to make sure that the if there is a unknow practitioner then we can raise a LookupError
def test_unknown_practitioner():
    data_store, _, practitioner_service, _ = setup()
    with pytest.raises(LookupError):
        practitioner_service.find_practitioner("unknown")

#appointent tests
#tests to make sure that the appointment is booked correctly and that the data is stored in the data store
def test_book_appointment():
    data_store, _, _, _, appointment = setup_with_appointment()
    assert appointment.status == AppointmentStatus.SCHEDULED
    assert appointment.patient == data_store.find_patient("p1")
    assert appointment.practitioner == data_store.find_practitioner("pr1")

#tests to make sure that the appointment is findable
def test_find_appointment():
    data_store, _, _, appointment_service, appointment = setup_with_appointment()
    found_appointment = appointment_service.find_appointment("a1")
    assert found_appointment == appointment

#tests to make sure that the if there is a unknow appointment then we can raise a LookupError
def test_unkown_appointment():
    data_store, _, _, appointment_service, _ = setup_with_appointment()
    with pytest.raises(LookupError):
        appointment_service.find_appointment("unknown")

#tests to make sure that the appointment cannot be booked without a patient
def test_appointment_without_patient():
    data_store, _, practitioner_service, appointment_service = setup()
    practitioner_service.register_practitioner("pr1", "Dr. Smith", "General")
    with pytest.raises(LookupError):
        appointment_service.book_appointment("a1", "unknown_patient", "pr1", date)

#tests to make sure that the appointment cannot be booked without a practitioner
def test_appointment_without_practitioner():
    data_store, patient_service, _, appointment_service = setup()
    patient_service.register_patient("p1", "John Doe")
    with pytest.raises(LookupError):
        appointment_service.book_appointment("a1", "p1", "unknown_practitioner", date)

#tests to make sure you can cancel the appointment and that the status is changed to cancelled
def test_cancel_appointment():
    data_store, _, _, appointment_service, appointment = setup_with_appointment()
    canceled_appointment = appointment_service.cancel_appointment("a1")
    assert canceled_appointment.status == AppointmentStatus.CANCELLED
    assert data_store.find_appointment("a1").status == AppointmentStatus.CANCELLED

#tests to make sure that the cancelled appointment is stored in the data store
def test_cancelled_appointment_is_stored():
    data_store, _, _, appointment_service, appointment = setup_with_appointment()
    appointment_service.cancel_appointment("a1")
    assert data_store.find_appointment("a1").status == AppointmentStatus.CANCELLED

def test_find_cancelled_appointment():
    data_store, _, _, appointment_service, appointment = setup_with_appointment()
    appointment_service.cancel_appointment("a1")
    found_appointment = appointment_service.find_appointment("a1")
    assert found_appointment.status == AppointmentStatus.CANCELLED

#tests to make sure that the cancelled appointment cannot be cancelled again and raises a ValueError
def test_cancelled_appointment_cant_be_cancelled_again():
    data_store, _, _, appointment_service, appointment = setup_with_appointment()
    appointment_service.cancel_appointment("a1")
    with pytest.raises(ValueError):
        appointment_service.cancel_appointment("a1")


#practitioner and patient conflicts
#tests to make sure that the same practitioner cannot have two appointments at the same time and raises a ValueError
def test_same_practitioner_at_the_same_time_isnt_allowed():
    data_store, _, _, appointment_service, original = setup_with_appointment()
    with pytest.raises(ValueError):
        appointment_service.book_appointment("a2", "p1", "pr1", date)

#tests to make sure that there can be multiple appointments at the same time as long as they are with different practitioners
def test_same_time_different_practitioner_is_allowed():
    data_store, patient_service, practitioner_service, appointment_service = setup()
    patient_service.register_patient("p1", "John Doe")
    practitioner_service.register_practitioner("pr1", "Dr. Smith", "General")
    practitioner_service.register_practitioner("pr2", "Dr. Jones", "Specialty")
    appointment1 = appointment_service.book_appointment("a1", "p1", "pr1", date)
    appointment2 = appointment_service.book_appointment("a2", "p1", "pr2", date)
    assert appointment1.practitioner.practitioner_id == "pr1"
    assert appointment2.practitioner.practitioner_id == "pr2"