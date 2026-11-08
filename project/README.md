# SmartCare

Requirements baseline: SmartCare A3 2026 revision 2. The application uses only the Python standard library. The Stage 10 test suite passed locally with Python 3.12.10 and pytest 8.3.5.

## Run SmartCare

Run these commands from the `project/` directory using your project’s Python environment:

```sh
python -m pip install -r requirements-dev.txt
python main.py
python main.py --interactive
python -m pytest -q
```

`python main.py` runs the demo with synthetic records. Use `--interactive` to open the console menu. Use synthetic information only.

## How the project is organised

- `domain.py` defines the entities and guards appointment state changes.
- `data_store.py` holds patients, practitioners and appointments for the current session.
- `services.py` coordinates registration, lookup, booking, cancellation, listing and rescheduling.
- `queries.py` filters and sorts appointment listings.
- `console.py` handles interaction with the user.

IDs are trimmed, non-blank and case-sensitive. The console expects `YYYY-MM-DD HH:MM`. Service booking takes a local `datetime` at minute precision. A store lookup returns `None` if a valid ID is absent; a service lookup raises `LookupError`. Invalid values, duplicates, conflicts and illegal transitions raise `ValueError`.

## Stage 10: Appointment rescheduling

Use `AppointmentService.reschedule_appointment(appointment_id, new_date_time=...)`
to move an existing scheduled appointment to a valid time. The service returns
the same appointment object and preserves its ID, participants and status.

A valid same-time request leaves the appointment unchanged. A move is rejected
if another scheduled appointment for the same practitioner occupies the new
time. After a successful move, the old slot becomes available, and lookup and
sorted practitioner listings reflect the new time.

Rescheduling is available through the service. The console menu is unchanged.

## Limitations

- Data is held in memory for one session and is lost when the program exits.
- Cancellation retains the appointment with status `CANCELLED`. A new booking needs a new appointment ID.
- Conflict checks prevent two scheduled appointments for the same practitioner at the exact same time. They do not check patient clashes or appointment duration.
- Notifications and saving to a file or database are outside scope.