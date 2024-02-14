from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from lib.models import Process
from abc import ABC

from lib.schemas import ProcessSchema


class DBHandler(ABC):
    @staticmethod
    def get_processes(db: Session) -> List[ProcessSchema]:
        try:
            processes = db.query(Process).all()
            return [ProcessSchema(name=process.name, icon=process.icon, duration=process.duration) for process in
                    processes]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def upsert_process(db: Session, schema: ProcessSchema) -> bool:
        existing_process = db.query(Process).filter_by(name=schema.name).first()
        if existing_process:
            existing_process.icon = schema.icon
            existing_process.duration += 1
        else:
            new_process = Process(name=schema.name, icon=schema.icon, duration=schema.duration)
            db.add(new_process)
        try:
            db.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
