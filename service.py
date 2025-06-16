from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_timeslots(db: Session):

    query = db.query(models.Timeslots)

    timeslots_all = query.all()
    timeslots_all = (
        [new_data.to_dict() for new_data in timeslots_all]
        if timeslots_all
        else timeslots_all
    )
    res = {
        "timeslots_all": timeslots_all,
    }
    return res


async def get_timeslots_id(db: Session, id: int):

    query = db.query(models.Timeslots)
    query = query.filter(and_(models.Timeslots.id == id))

    timeslots_one = query.first()

    timeslots_one = (
        (
            timeslots_one.to_dict()
            if hasattr(timeslots_one, "to_dict")
            else vars(timeslots_one)
        )
        if timeslots_one
        else timeslots_one
    )

    res = {
        "timeslots_one": timeslots_one,
    }
    return res


async def post_timeslots(db: Session, raw_data: schemas.PostTimeslots):
    id: int = raw_data.id
    date: datetime.date = raw_data.date
    start_time: str = raw_data.start_time
    end_time: str = raw_data.end_time

    record_to_be_added = {
        "id": id,
        "date": date,
        "end_time": end_time,
        "start_time": start_time,
    }
    new_timeslots = models.Timeslots(**record_to_be_added)
    db.add(new_timeslots)
    db.commit()
    db.refresh(new_timeslots)
    timeslots_inserted_record = new_timeslots.to_dict()

    res = {
        "timeslots_inserted_record": timeslots_inserted_record,
    }
    return res


async def put_timeslots_id(
    db: Session, id: int, date: str, start_time: str, end_time: str
):

    query = db.query(models.Timeslots)
    query = query.filter(and_(models.Timeslots.id == id))
    timeslots_edited_record = query.first()

    if timeslots_edited_record:
        for key, value in {
            "id": id,
            "date": date,
            "end_time": end_time,
            "start_time": start_time,
        }.items():
            setattr(timeslots_edited_record, key, value)

        db.commit()
        db.refresh(timeslots_edited_record)

        timeslots_edited_record = (
            timeslots_edited_record.to_dict()
            if hasattr(timeslots_edited_record, "to_dict")
            else vars(timeslots_edited_record)
        )
    res = {
        "timeslots_edited_record": timeslots_edited_record,
    }
    return res


async def delete_timeslots_id(db: Session, id: int):

    query = db.query(models.Timeslots)
    query = query.filter(and_(models.Timeslots.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        timeslots_deleted = record_to_delete.to_dict()
    else:
        timeslots_deleted = record_to_delete
    res = {
        "timeslots_deleted": timeslots_deleted,
    }
    return res


async def get_providers(db: Session):

    query = db.query(models.Providers)

    providers_all = query.all()
    providers_all = (
        [new_data.to_dict() for new_data in providers_all]
        if providers_all
        else providers_all
    )
    res = {
        "providers_all": providers_all,
    }
    return res


async def get_providers_id(db: Session, id: int):

    query = db.query(models.Providers)
    query = query.filter(and_(models.Providers.id == id))

    providers_one = query.first()

    providers_one = (
        (
            providers_one.to_dict()
            if hasattr(providers_one, "to_dict")
            else vars(providers_one)
        )
        if providers_one
        else providers_one
    )

    res = {
        "providers_one": providers_one,
    }
    return res


async def post_providers(db: Session, raw_data: schemas.PostProviders):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"id": id, "name": name, "contact_details": contact_details}
    new_providers = models.Providers(**record_to_be_added)
    db.add(new_providers)
    db.commit()
    db.refresh(new_providers)
    providers_inserted_record = new_providers.to_dict()

    res = {
        "providers_inserted_record": providers_inserted_record,
    }
    return res


async def put_providers_id(db: Session, id: int, name: str, contact_details: str):

    query = db.query(models.Providers)
    query = query.filter(and_(models.Providers.id == id))
    providers_edited_record = query.first()

    if providers_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_details": contact_details,
        }.items():
            setattr(providers_edited_record, key, value)

        db.commit()
        db.refresh(providers_edited_record)

        providers_edited_record = (
            providers_edited_record.to_dict()
            if hasattr(providers_edited_record, "to_dict")
            else vars(providers_edited_record)
        )
    res = {
        "providers_edited_record": providers_edited_record,
    }
    return res


async def delete_providers_id(db: Session, id: int):

    query = db.query(models.Providers)
    query = query.filter(and_(models.Providers.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        providers_deleted = record_to_delete.to_dict()
    else:
        providers_deleted = record_to_delete
    res = {
        "providers_deleted": providers_deleted,
    }
    return res


async def get_customers(db: Session):

    query = db.query(models.Customers)

    customers_all = query.all()
    customers_all = (
        [new_data.to_dict() for new_data in customers_all]
        if customers_all
        else customers_all
    )
    res = {
        "customers_all": customers_all,
    }
    return res


async def get_customers_id(db: Session, id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))

    customers_one = query.first()

    customers_one = (
        (
            customers_one.to_dict()
            if hasattr(customers_one, "to_dict")
            else vars(customers_one)
        )
        if customers_one
        else customers_one
    )

    res = {
        "customers_one": customers_one,
    }
    return res


async def post_customers(db: Session, raw_data: schemas.PostCustomers):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"id": id, "name": name, "contact_details": contact_details}
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    customers_inserted_record = new_customers.to_dict()

    res = {
        "customers_inserted_record": customers_inserted_record,
    }
    return res


async def put_customers_id(db: Session, id: int, name: str, contact_details: str):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))
    customers_edited_record = query.first()

    if customers_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_details": contact_details,
        }.items():
            setattr(customers_edited_record, key, value)

        db.commit()
        db.refresh(customers_edited_record)

        customers_edited_record = (
            customers_edited_record.to_dict()
            if hasattr(customers_edited_record, "to_dict")
            else vars(customers_edited_record)
        )
    res = {
        "customers_edited_record": customers_edited_record,
    }
    return res


async def delete_customers_id(db: Session, id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        customers_deleted = record_to_delete.to_dict()
    else:
        customers_deleted = record_to_delete
    res = {
        "customers_deleted": customers_deleted,
    }
    return res


async def get_appointments(db: Session):

    query = db.query(models.Appointments)

    appointments_all = query.all()
    appointments_all = (
        [new_data.to_dict() for new_data in appointments_all]
        if appointments_all
        else appointments_all
    )
    res = {
        "appointments_all": appointments_all,
    }
    return res


async def get_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))

    appointments_one = query.first()

    appointments_one = (
        (
            appointments_one.to_dict()
            if hasattr(appointments_one, "to_dict")
            else vars(appointments_one)
        )
        if appointments_one
        else appointments_one
    )

    res = {
        "appointments_one": appointments_one,
    }
    return res


async def post_appointments(db: Session, raw_data: schemas.PostAppointments):
    id: int = raw_data.id
    customer_id: int = raw_data.customer_id
    provider_id: int = raw_data.provider_id
    timeslot_id: int = raw_data.timeslot_id

    record_to_be_added = {
        "id": id,
        "customer_id": customer_id,
        "provider_id": provider_id,
        "timeslot_id": timeslot_id,
    }
    new_appointments = models.Appointments(**record_to_be_added)
    db.add(new_appointments)
    db.commit()
    db.refresh(new_appointments)
    appointments_inserted_record = new_appointments.to_dict()

    res = {
        "appointments_inserted_record": appointments_inserted_record,
    }
    return res


async def put_appointments_id(
    db: Session, id: int, customer_id: int, provider_id: int, timeslot_id: int
):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))
    appointments_edited_record = query.first()

    if appointments_edited_record:
        for key, value in {
            "id": id,
            "customer_id": customer_id,
            "provider_id": provider_id,
            "timeslot_id": timeslot_id,
        }.items():
            setattr(appointments_edited_record, key, value)

        db.commit()
        db.refresh(appointments_edited_record)

        appointments_edited_record = (
            appointments_edited_record.to_dict()
            if hasattr(appointments_edited_record, "to_dict")
            else vars(appointments_edited_record)
        )
    res = {
        "appointments_edited_record": appointments_edited_record,
    }
    return res


async def delete_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointments_deleted = record_to_delete.to_dict()
    else:
        appointments_deleted = record_to_delete
    res = {
        "appointments_deleted": appointments_deleted,
    }
    return res


async def get_calendar_events(db: Session):

    query = db.query(models.CalendarEvents)

    calendar_events_all = query.all()
    calendar_events_all = (
        [new_data.to_dict() for new_data in calendar_events_all]
        if calendar_events_all
        else calendar_events_all
    )
    res = {
        "calendar_events_all": calendar_events_all,
    }
    return res


async def get_calendar_events_id(db: Session, id: int):

    query = db.query(models.CalendarEvents)
    query = query.filter(and_(models.CalendarEvents.id == id))

    calendar_events_one = query.first()

    calendar_events_one = (
        (
            calendar_events_one.to_dict()
            if hasattr(calendar_events_one, "to_dict")
            else vars(calendar_events_one)
        )
        if calendar_events_one
        else calendar_events_one
    )

    res = {
        "calendar_events_one": calendar_events_one,
    }
    return res


async def post_calendar_events(db: Session, raw_data: schemas.PostCalendarEvents):
    id: int = raw_data.id
    appointment_id: int = raw_data.appointment_id
    calendar_id: str = raw_data.calendar_id
    event_id: str = raw_data.event_id

    record_to_be_added = {
        "id": id,
        "event_id": event_id,
        "calendar_id": calendar_id,
        "appointment_id": appointment_id,
    }
    new_calendar_events = models.CalendarEvents(**record_to_be_added)
    db.add(new_calendar_events)
    db.commit()
    db.refresh(new_calendar_events)
    calendar_events_inserted_record = new_calendar_events.to_dict()

    res = {
        "calendar_events_inserted_record": calendar_events_inserted_record,
    }
    return res


async def put_calendar_events_id(
    db: Session, id: int, appointment_id: int, calendar_id: str, event_id: str
):

    query = db.query(models.CalendarEvents)
    query = query.filter(and_(models.CalendarEvents.id == id))
    calendar_events_edited_record = query.first()

    if calendar_events_edited_record:
        for key, value in {
            "id": id,
            "event_id": event_id,
            "calendar_id": calendar_id,
            "appointment_id": appointment_id,
        }.items():
            setattr(calendar_events_edited_record, key, value)

        db.commit()
        db.refresh(calendar_events_edited_record)

        calendar_events_edited_record = (
            calendar_events_edited_record.to_dict()
            if hasattr(calendar_events_edited_record, "to_dict")
            else vars(calendar_events_edited_record)
        )
    res = {
        "calendar_events_edited_record": calendar_events_edited_record,
    }
    return res


async def delete_calendar_events_id(db: Session, id: int):

    query = db.query(models.CalendarEvents)
    query = query.filter(and_(models.CalendarEvents.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        calendar_events_deleted = record_to_delete.to_dict()
    else:
        calendar_events_deleted = record_to_delete
    res = {
        "calendar_events_deleted": calendar_events_deleted,
    }
    return res
