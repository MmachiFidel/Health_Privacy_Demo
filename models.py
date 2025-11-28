from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class PatientEvent(Base):
    __tablename__ = 'patient_events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pseudonym = Column(String(64), index=True, nullable=False)
    event_time = Column(DateTime, default=datetime.datetime.utcnow)
    event_type = Column(String(64))
    details = Column(String(512))
