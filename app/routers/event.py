from fastapi import APIRouter, HTTPException, Depends
from app.schemas.event import Event, EventCreate, EventUpdate
from app.crud.event import create_event, get_event, get_events, update_event, delete_event
from sqlalchemy.orm import Session
from app.dependency import get_db
from typing import Annotated

router = APIRouter()

@router.post("/event", response_model=Event)
def create_event_endpoint(
    event: EventCreate,
    db: Session = Depends(get_db)
    ):
    return create_event(db=db, event=event)

@router.get("/event/{event_id}", response_model=Event)
def get_event_endpoint(
    event_id: int,
    db: Session = Depends(get_db)
):
    return get_event(db=db, event_id=event_id)

@router.get("/events", response_model=list[Event])
def get_events_endpoint(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_events(db=db, skip=skip, limit=limit)

@router.put("/event/{event_id}", response_model=Event)
def update_event_endpoint(
    event_id: int,
    event_update: EventUpdate,
    db: Session = Depends(get_db)
):
    return update_event(db=db, event_id=event_id, event_update=event_update)

@router.delete("/event/{event_id}", response_model=Event)
def delete_event_endpoint(
    event_id: int,
    db: Session = Depends(get_db)
):
    return delete_event(db=db, event_id=event_id)