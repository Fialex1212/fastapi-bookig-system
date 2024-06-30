from sqlalchemy.orm import Session
from app.models.event import Event as DBEvent
from app.schemas.event import EventCreate, EventUpdate

def create_event(db: Session, event: EventCreate):
    db_event = DBEvent(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_event(db: Session, event_id: int):
    return db.query(DBEvent).filter(DBEvent==event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBEvent).offset(skip).limit(limit).all()

def update_event(db: Session, event_update: EventUpdate, event_id: int):
    db_event = db.query(DBEvent).filter(DBEvent==event_id).first()
    if db_event:
        db_event.title = event_update.title
        db_event.time = event_update.time
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = db.query(DBEvent).filter(DBEvent==event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event