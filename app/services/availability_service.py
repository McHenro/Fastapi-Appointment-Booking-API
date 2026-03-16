from sqlalchemy.orm import Session
from app.models.availability import Availability
from app.schemas.availability import AvailabilityCreate
from datetime import datetime, timedelta

def create_availability(
    db: Session,
    doctor_id: int,
    availability: AvailabilityCreate
):

    slots = generate_slots(
        availability.start_time,
        availability.end_time,
        availability.slot_duration
    )

    new_slot = Availability(
        doctor_id=doctor_id,
        date=availability.date,
        start_time=availability.start_time,
        end_time=availability.end_time,
        slot_duration=availability.slot_duration
    )

    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)

    return {
        'availability': new_slot,
        'slots': slots
    }

def generate_slots(start_time, end_time, slot_duration):

    # Validate inputs
    if slot_duration is None or slot_duration <= 0:
        return []

    slots = []

    start = datetime.combine(datetime.today().date(), start_time)
    end = datetime.combine(datetime.today().date(), end_time)

    if start >= end:
        return []

    # Only create full slots that fit entirely within [start, end]
    while start + timedelta(minutes=slot_duration) <= end:
        slot_end = start + timedelta(minutes=slot_duration)

        slots.append(
            {
                "start_time": start.time(),
                "end_time": slot_end.time()
            }
        )

        start = slot_end

    return slots
