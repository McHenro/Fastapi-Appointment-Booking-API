from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.appointment import Appointment
from app.models.availability import Availability
from app.schemas.appointment import AppointmentCreate


def book_appointment(
    db: Session,
    patient_id: int,
    appointment: AppointmentCreate
):
    # Check Doctor Availability
    availability = db.query(Availability).filter(
        Availability.doctor_id == appointment.doctor_id,
        Availability.date == appointment.date
    ).first()

    if not availability:
        raise HTTPException(
            status_code=400,
            detail="Doctor not available on this date"
        )

    # Validate Time Range (Ensure appointment fits inside availability.)
    if appointment.start_time < availability.start_time or appointment.end_time > availability.end_time:
        raise HTTPException(
            status_code=400,
            detail="Appointment outside doctor availability"
        )

    # Prevent Double Booking (Prevent Double Booking)
    existing = db.query(Appointment).filter(
        Appointment.doctor_id == appointment.doctor_id,
        Appointment.date == appointment.date,
        Appointment.start_time < appointment.end_time,
        Appointment.end_time > appointment.start_time
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Time slot already booked"
        )

    # Create Appointment
    new_appointment = Appointment(
        doctor_id=appointment.doctor_id,
        patient_id=patient_id,
        date=appointment.date,
        start_time=appointment.start_time,
        end_time=appointment.end_time
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


