from datetime import datetime

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
    assert result is not source
