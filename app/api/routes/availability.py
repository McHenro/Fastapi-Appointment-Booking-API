from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.availability import AvailabilityCreate, AvailabilityWithSlotsResponse
from app.services.availability_service import create_availability
from app.api.deps import get_current_user

router = APIRouter(prefix="/availability", tags=["Availability"])

@router.post("/", response_model=AvailabilityWithSlotsResponse)
def create_slot(
    availability: AvailabilityCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = create_availability(
        db=db,
        doctor_id=current_user.id,
        availability=availability
    )
    return result
