"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (Appointment, AppointmentStatus, Patient, Practitioner)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')

    """Stage 9: implement the register/find/book/cancel/list/exit menu.

    Call services, recover from expected input errors, and keep this
    session's data until exit. main.py reports the incomplete menu
    without crashing.
    """
MENU = """
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------"""

STATUS_PROMPT = 'Status filter [scheduled/cancelled/completed, blank = all]: '

def parse_status(text: str) -> AppointmentStatus | None:
    """Turn typed text into a status. Blank means all statuses (None)."""
    text = text.strip().lower()
    if text == '':
        return None
    try:
        return AppointmentStatus(text)
    except ValueError:
        raise ValueError(
            'Status must be scheduled, cancelled or completed',
        ) from None

def show_patient(patient: Patient) -> None:
    """Print a patient's details."""
    print(f'Patient ID : {patient.patient_id}')
    print(f'Name       : {patient.name}')

def show_practitioner(practitioner: Practitioner) -> None:
    """Print a practitioner's details."""
    print(f'Practitioner ID : {practitioner.practitioner_id}')
    print(f'Name            : {practitioner.name}')
    print(f'Specialty       : {practitioner.specialty}')

def show_appointment(appointment: Appointment) -> None:
    """Print an appointment's details."""
    patient = appointment.patient
    practitioner = appointment.practitioner
    print(f'Appointment ID : {appointment.appointment_id}')
    print(f'Patient        : {patient.name} ({patient.patient_id})')
    print(
        f'Practitioner   : {practitioner.name} '
        f'({practitioner.practitioner_id})',
    )
    print(f'Specialty      : {practitioner.specialty}')
    print(f'Date/time      : {appointment.date_time:%Y-%m-%d %H:%M}')
    print(f'Status         : {appointment.status.value.capitalize()}')
    print(f'Reference      : {format_appointment(appointment)}')

def register_patient_action(patients: PatientService) -> None:
    """Ask for patient details and register the patient."""
    patient_id = input('Patient ID: ')
    name = input('Patient name: ')
    patient = patients.register_patient(patient_id, name)
    print('Patient registered successfully.')
    show_patient(patient)

def find_patient_action(patients: PatientService) -> None:
    """Ask for a patient ID and show that patient."""
    patient = patients.find_patient(input('Patient ID: '))
    print(f'Patient found. {patient.patient_id}: {patient.name}')
    show_patient(patient)

def register_practitioner_action(practitioners: PractitionerService) -> None:
    """Ask for practitioner details and register the practitioner."""
    practitioner_id = input('Practitioner ID: ')
    name = input('Practitioner name: ')
    specialty = input('Specialty: ')
    practitioner = practitioners.register_practitioner(practitioner_id, name, specialty)
    print('Practitioner registered successfully.')
    show_practitioner(practitioner)

def find_practitioner_action(practitioners: PractitionerService) -> None:
    """Ask for a practitioner ID and show that practitioner."""
    practitioner = practitioners.find_practitioner(
        input('Practitioner ID: '),
    )
    print(
        f'Practitioner found. {practitioner.practitioner_id}: '
        f'{practitioner.name}, {practitioner.specialty}',
    )
    show_practitioner(practitioner)

def book_action(appointments: AppointmentService) -> None:
    """Ask for booking details and book the appointment."""
    appointment_id = input('Appointment ID: ')
    patient_id = input('Patient ID: ')
    practitioner_id = input('Practitioner ID: ')
    date_time = parse_date_time(
        input('Date/time [YYYY-MM-DD HH:MM]: ').strip(),
    )
    appointment = appointments.book_appointment(appointment_id, patient_id, practitioner_id, date_time)
    print('Appointment booked successfully.')
    show_appointment(appointment)

def cancel_action(appointments: AppointmentService) -> None:
    """Ask for an appointment ID and cancel that appointment."""
    appointment = appointments.cancel_appointment(input('Appointment ID: '))
    print('Appointment cancelled successfully.')
    show_appointment(appointment)

def find_appointment_action(appointments: AppointmentService) -> None:
    """Ask for an appointment ID and show that appointment."""
    appointment = appointments.find_appointment(input('Appointment ID: '))
    print('Appointment found.')
    show_appointment(appointment)

def list_action(practitioners: PractitionerService, appointments: AppointmentService) -> None:
    """Ask for a practitioner and a status then list the appointments."""
    practitioner_id = input('Practitioner ID: ')
    status = parse_status(input(STATUS_PROMPT))
    practitioner = practitioners.find_practitioner(practitioner_id)
    found = appointments.list_practitioner_appointments(practitioner.practitioner_id, status)
    label = 'All statuses' if status is None else status.value.capitalize()
    print(
        f'Appointments for {practitioner.name} '
        f'({practitioner.practitioner_id})',
    )
    print(f'Filter: {label}')
    print('-' * 60)
    if not found:
        print('No appointments found.')
        return
    for number, appointment in enumerate(found, start=1):
        print(f'{number}. {appointment.appointment_id}')
        print(
            f'   Patient   : {appointment.patient.name} '
            f'({appointment.patient.patient_id})',
        )
        print(f'   Date/time : {appointment.date_time:%Y-%m-%d %H:%M}')
        print(f'   Status    : {appointment.status.value.capitalize()}')
        print(f'   Reference : {format_appointment(appointment)}')
    print('-' * 60)
    print(f'{len(found)} appointment(s) found.')

def run_menu() -> None:
    """Run the repeated text menu. Data lasts only for this session."""
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    print('=' * 60)
    print('SMARTCARE')
    print('Interactive Console')
    print('=' * 60)
    print('Session data is temporary and will be discarded when you exit.')
    while True:
        print(MENU)
        try:
            choice = input('Select an option: ').strip()
        except EOFError:
            choice = '0'
        if choice == '0':
            print('Goodbye. Session data discarded.')
            return
        try:
            if choice == '1':
                register_patient_action(patients)
            elif choice == '2':
                find_patient_action(patients)
            elif choice == '3':
                register_practitioner_action(practitioners)
            elif choice == '4':
                find_practitioner_action(practitioners)
            elif choice == '5':
                book_action(appointments)
            elif choice == '6':
                cancel_action(appointments)
            elif choice == '7':
                find_appointment_action(appointments)
            elif choice == '8':
                list_action(practitioners, appointments)
            else:
                print('Unknown choice. Choose a number from 0 to 8.')
        except (ValueError, LookupError) as error:
            print(f'Error: {error}')
