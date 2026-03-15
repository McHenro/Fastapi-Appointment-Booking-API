from pydantic import BaseModel
from datetime import date, time

class AvailabilityCreate(BaseModel):
    date: date
    start_time: time
    end_time: time
    slot_duration: int


class AvailabilityResponse(BaseModel):
    id: int
    date: date
    start_time: time
    end_time: time
    slot_duration: int

    class Config:
        from_attributes = True