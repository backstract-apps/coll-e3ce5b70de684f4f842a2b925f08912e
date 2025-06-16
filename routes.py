from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/timeslots/')
async def get_timeslots(db: Session = Depends(get_db)):
    try:
        return await service.get_timeslots(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/timeslots/id')
async def get_timeslots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_timeslots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/timeslots/')
async def post_timeslots(raw_data: schemas.PostTimeslots, db: Session = Depends(get_db)):
    try:
        return await service.post_timeslots(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/timeslots/id/')
async def put_timeslots_id(id: int, date: str, start_time: Annotated[str, Query(max_length=100)], end_time: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_timeslots_id(db, id, date, start_time, end_time)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/timeslots/id')
async def delete_timeslots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_timeslots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/providers/')
async def get_providers(db: Session = Depends(get_db)):
    try:
        return await service.get_providers(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/providers/id')
async def get_providers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_providers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/providers/')
async def post_providers(raw_data: schemas.PostProviders, db: Session = Depends(get_db)):
    try:
        return await service.post_providers(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/providers/id/')
async def put_providers_id(id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_providers_id(db, id, name, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/providers/id')
async def delete_providers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_providers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/')
async def get_customers(db: Session = Depends(get_db)):
    try:
        return await service.get_customers(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/id')
async def get_customers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_customers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/customers/')
async def post_customers(raw_data: schemas.PostCustomers, db: Session = Depends(get_db)):
    try:
        return await service.post_customers(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/customers/id/')
async def put_customers_id(id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_customers_id(db, id, name, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/customers/id')
async def delete_customers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_customers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/')
async def get_appointments(db: Session = Depends(get_db)):
    try:
        return await service.get_appointments(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/id')
async def get_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointments/')
async def post_appointments(raw_data: schemas.PostAppointments, db: Session = Depends(get_db)):
    try:
        return await service.post_appointments(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointments/id/')
async def put_appointments_id(id: int, customer_id: int, provider_id: int, timeslot_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_appointments_id(db, id, customer_id, provider_id, timeslot_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointments/id')
async def delete_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/calendar_events/')
async def get_calendar_events(db: Session = Depends(get_db)):
    try:
        return await service.get_calendar_events(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/calendar_events/id')
async def get_calendar_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_calendar_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/calendar_events/')
async def post_calendar_events(raw_data: schemas.PostCalendarEvents, db: Session = Depends(get_db)):
    try:
        return await service.post_calendar_events(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/calendar_events/id/')
async def put_calendar_events_id(id: int, appointment_id: int, calendar_id: Annotated[str, Query(max_length=100)], event_id: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_calendar_events_id(db, id, appointment_id, calendar_id, event_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/calendar_events/id')
async def delete_calendar_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_calendar_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

