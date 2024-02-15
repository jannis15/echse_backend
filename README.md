# echse_backend
 
Ein Fullstack-Projekt zum Tracken der Zeit diverser Windows-Programme (.exe).

- Frontend: Flutter (Dart)
- Backend: FastAPI (Python)

Das Backend fragt jede Minute über die win32-API die aktuell laufenden Prozessdaten ab und speichert diese in einer SQLite-Datenbank.

Das Frontend kann über die REST-Schnittstelle Programme sortiert nach laufender Dauer abfragen und anzeigen.

![demo](https://github.com/jannis15/echse_backend/assets/78983365/87706732-399c-40bd-a590-21e8fe08c7d9)
