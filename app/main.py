from fastapi import FastAPI
from app.core.database import engine, Base
from app.models.users import User

app = FastAPI(title="Appointment Booking API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}