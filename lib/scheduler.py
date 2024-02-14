from rocketry import Rocketry
from lib.db_handler import DBHandler
from lib.processes_api_client import ProcessesApiClient
from lib.session import SessionLocal

app = Rocketry()


@app.task('minutely')
def get_running_processes_minutely():
    processes = ProcessesApiClient.get_running_processes()
    tmp_db = SessionLocal()
    for process in processes:
        DBHandler.upsert_process(tmp_db, process)
