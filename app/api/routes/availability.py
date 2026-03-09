from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.availability import AvailabilityCreate, AvailabilityResponse
from app.services.availability_service import create_availability
from app.api.deps import get_current_user

from app.core.database import get_db

router = APIRouter(prefix="/availability", tags=["Availability"])

@router.post("/", response_model=AvailabilityResponse)
def create_slot(
    availability: AvailabilityCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_availability(
        db=db,
        doctor_id=current_user.id,
        availability=availability
    )
