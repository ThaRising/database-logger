from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Time

Base = declarative_base()


class Record(Base):
    __tablename__ = "record"
    id = Column(Integer, primary_key=True)
    timestamp = Column(Time)
    source = Column(String)
    sport = Column(String)
    destination = Column(String)
    dport = Column(String)
