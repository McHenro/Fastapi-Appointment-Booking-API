from sqlalchemy.orm import Session
from app.models.availability import Availability
from app.schemas.availability import AvailabilityCreate
from datetime import datetime, timedelta

def create_availability(
    db: Session,
    doctor_id: int,
    availability: AvailabilityCreate
):

    new_slot = Availability(
        doctor_id=doctor_id,
        date=availability.date,
        start_time=availability.start_time,
        end_time=availability.end_time
    )

    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)

    return new_slot

def generate_slots(start_time, end_time, slot_duration):

    slots = []

    start = datetime.combine(datetime.today(), start_time)
    end = datetime.combine(datetime.today(), end_time)

    while start < end:

        slot_end = start + timedelta(minutes=slot_duration)

        slots.append(
            {
                "start_time": start.time(),
                "end_time": slot_end.time()
            }
        )

        start = slot_end

    return slots
