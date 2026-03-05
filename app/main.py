from fastapi import FastAPI
from app.core.database import engine, Base
from app.models.users import User
from app.api.routes import auth


app = FastAPI(title="Appointment Booking API")

Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {"message": "API is running"}
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
