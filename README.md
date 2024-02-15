# echse_backend
 
Ein Fullstack-Projekt zum Tracken der Zeit diverser Windows-Programme (.exe).

- Frontend: Flutter (Dart)
- Backend: FastAPI (Python)

Das Backend fragt jede Minute über die win32-API die aktuell laufenden Prozessdaten ab und speichert diese in einer SQLite-Datenbank.

Das Frontend kann über die REST-Schnittstelle Programme sortiert nach laufender Dauer abfragen und anzeigen.
