from pydantic import BaseModel


class ProcessSchema(BaseModel):
    name: str
    icon: str
    duration: int
