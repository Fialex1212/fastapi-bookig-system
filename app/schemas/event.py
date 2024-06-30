from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    create_at: datetime
    start_time: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        from_attributes = True