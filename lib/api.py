from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db_handler import DBHandler
from session import yield_db

app = FastAPI()


@app.get('/data')
async def get_data(db: Session = Depends(yield_db)):
    return {
        "data": DBHandler.get_processes(db),
    }
