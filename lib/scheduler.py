from rocketry import Rocketry
from rocketry.args import Config
from rocketry.conds import minutely
from lib.db_handler import DBHandler
from lib.processes_api_client import ProcessesApiClient
from lib.session import SessionLocal

app = Rocketry()


@app.setup()
def set_config(config=Config()):
    config.silence_task_prerun = True


@app.task(minutely.at("00"))
def get_running_processes_minutely():
    processes = ProcessesApiClient.get_running_processes()
    tmp_db = SessionLocal()
    for process in processes:
        DBHandler.upsert_process(tmp_db, process)
