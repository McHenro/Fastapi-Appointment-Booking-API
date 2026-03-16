from pydantic import BaseModel
from datetime import date, time
from typing import List

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


class Slot(BaseModel):
    start_time: time
    end_time: time


class AvailabilityWithSlotsResponse(BaseModel):
    availability: AvailabilityResponse
    slots: List[Slot]