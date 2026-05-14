from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.models.temperature_reading_model import Base

import app.crud.temperature_reading_crud as crud
import app.schemas.temperature_reading_schemas as schemas

app = APIRouter()

# =========================
# LISTAR LECTURAS , dependencies=[Depends(decode_token)]
# =========================

@app.get("/list")
def list_readings(db: Session = Depends(get_db)):

    readings = crud.get_readings(db=db)

    return readings

# =========================
# OBTENER ULTIMA LECTURA
# =========================

@app.get("/last", dependencies=[Depends(decode_token)])
def last_reading(db: Session = Depends(get_db)):

    reading = crud.get_last_reading(db=db)

    if reading is None:
        raise HTTPException(
            status_code=404,
            detail="No hay lecturas"
        )

    return reading

# =========================
# CREAR LECTURA (ESP32)
# =========================

@app.post("/create")
def create_reading(
    reading: schemas.ReadingBase,
    db: Session = Depends(get_db)
):

    new_reading = crud.create_reading(
        db=db,
        reading=reading
    )

    return {
        "message": "Lectura registrada",
        "data": new_reading
    }

