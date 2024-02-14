from sqlalchemy import Integer, Column, String
from session import Base, engine


class Process(Base):
    __tablename__ = 'Process'

    name = Column(String, primary_key=True, index=True)
    icon = Column(String, nullable=False)
    duration = Column(Integer, default=0)


Base.metadata.create_all(bind=engine)
