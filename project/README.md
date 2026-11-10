# SmartCare

Requirements baseline: SmartCare A3 2026 revision 2. The application uses only the Python standard library at runtime.

The common scope includes patient and practitioner registration and lookup, booking and conflict checks, cancellation with history, and filtered appointment listings. The PG scope adds service-level appointment rescheduling and assurance tests. Rescheduling is not exposed in the console menu.

## Run SmartCare

The Stage 12 PG starting snapshot was verified on macOS using Python 3.12.10 and pytest 8.3.5. From the repository root, run:

```sh
cd project
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python main.py
python main.py --interactive
python -m pytest -q
```

`python main.py` runs a synthetic demo. Use `--interactive` to open the menu and select `0` to exit. Pytest is a development dependency. Use synthetic information only.

AI-assisted proposals, human review decisions and verification results are documented in the [Stage 09 common evidence](../stage09/stage09_activities_and_evidence.md), [Stage 10 rescheduling evidence](../stage10_pg/stage10_activities_and_evidence.md), and [Stage 11 assurance evidence](../stage11_pg/stage11_activities_and_evidence.md).

## How the project is organised

- `domain.py` defines the entities and guards appointment state changes.
- `data_store.py` holds patients, practitioners and appointments for the current session.
- `services.py` coordinates registration, lookup, booking, cancellation, listing and rescheduling.
- `queries.py` filters and sorts appointment listings.
- `console.py` handles interaction with the user.

IDs are trimmed, non-blank and case-sensitive. The console expects `YYYY-MM-DD HH:MM`. The booking service accepts a local `datetime` at minute precision. Store lookup returns `None` if a valid ID is absent; service lookup raises `LookupError`. Invalid values, duplicates, conflicts and illegal transitions raise `ValueError`.

## Stage 10: Appointment rescheduling

Use `AppointmentService.reschedule_appointment(appointment_id, new_date_time=...)` to move an existing scheduled appointment. The service returns the same appointment object and preserves its ID, participants and status.

A valid same-time request leaves the appointment unchanged. A move is rejected if another scheduled appointment for the same practitioner occupies the new time. After a successful move, the old slot becomes available, and lookup and sorted practitioner listings show the new time.

Rescheduling is available through the service. The console menu is unchanged.

## Limitations

- Data is held in memory for one session and is lost when the program exits.
- Cancellation retains the appointment with status `CANCELLED`. A new booking needs a new appointment ID.
- Conflict checks prevent two scheduled appointments for the same practitioner at the exact same time. They do not check patient clashes or appointment duration.
- Notifications and saving to a file or database are outside scope.
- Interactive patient lookup displays the patient ID and name twice. Use synthetic records only.