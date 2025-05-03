from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session, select, update, delete

from api.db.session import get_session
from .models import EventModel
from .schemas import EventRead, EventCreate, EventUpdate, EventListSchema

router = APIRouter()


@router.get('/', response_model=EventListSchema)
async def read_events(session: Session = Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id)
    res = session.exec(query).all()
    return {'items': res}


@router.get('/{event_id}', response_model=EventRead)
async def get_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f'Event with id {event_id} is not found')

    return obj


@router.post('/', response_model=EventCreate)
async def create_event(payload: EventCreate, session: Session = Depends(get_session)):
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)  # to get newly created obj with id
    return obj


@router.put('/{event_id}', response_model=EventRead)
async def update_event(event_id: int, payload: EventUpdate, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f'Event with id {event_id} is not found')

    data = payload.model_dump()
    for k, v in data.items():
        setattr(obj, k, v)

    session.add(obj)
    session.commit()
    session.refresh(obj)  # to get newly created obj with id
    return obj


@router.delete('/{event_id}', response_model=dict)
async def update_event(event_id: int, session: Session = Depends(get_session)):
    query = delete(EventModel).where(EventModel.id == event_id)
    res = session.exec(query)
    return {'message': f'Deleted {res.rowcount} event with id {event_id}'}
