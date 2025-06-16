from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Timeslots(BaseModel):
    id: Any
    date: datetime.date
    start_time: Any
    end_time: Any


class ReadTimeslots(BaseModel):
    id: Any
    date: datetime.date
    start_time: Any
    end_time: Any
    class Config:
        from_attributes = True


class Providers(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadProviders(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class Customers(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadCustomers(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    id: Any
    customer_id: int
    provider_id: int
    timeslot_id: int


class ReadAppointments(BaseModel):
    id: Any
    customer_id: int
    provider_id: int
    timeslot_id: int
    class Config:
        from_attributes = True


class CalendarEvents(BaseModel):
    id: Any
    appointment_id: int
    calendar_id: str
    event_id: str


class ReadCalendarEvents(BaseModel):
    id: Any
    appointment_id: int
    calendar_id: str
    event_id: str
    class Config:
        from_attributes = True




class PostTimeslots(BaseModel):
    id: int = Field(...)
    date: Any = Field(...)
    start_time: str = Field(..., max_length=100)
    end_time: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostProviders(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostCustomers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostAppointments(BaseModel):
    id: int = Field(...)
    customer_id: int = Field(...)
    provider_id: int = Field(...)
    timeslot_id: int = Field(...)

    class Config:
        from_attributes = True



class PostCalendarEvents(BaseModel):
    id: int = Field(...)
    appointment_id: int = Field(...)
    calendar_id: str = Field(..., max_length=100)
    event_id: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

