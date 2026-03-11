from pydantic import BaseModel
from datetime import date, time

class AppointmentCreate(BaseModel):

    doctor_id: int
    date: date
    start_time: time
    end_time: time


class AppointmentResponse(BaseModel):

    id: int
    doctor_id: int
    patient_id: int
    date: date
    start_time: time
    end_time: time

    class Config:
        from_attributes = True