from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, index=True)
    create_at = Column(DateTime, index=True)
    start_time = Column(DateTime, index=True)