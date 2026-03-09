from sqlalchemy.orm import Session
from app.models.availability import Availability
from app.schemas.availability import AvailabilityCreate

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