from pydantic import BaseModel
from datetime import date, time

class AvailabilityCreate(BaseModel):
    date: date
    start_time: time
    end_time: time


class AvailabilityResponse(BaseModel):
    id: int
    date: date
    start_time: time
    end_time: time

    class Config:
        from_attributes = True