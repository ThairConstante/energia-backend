from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.config import get_db

import app.crud.sensor_crud as crud
import app.schemas.sensor_schemas as schemas

app = APIRouter()

# =========================
# LISTAR
# =========================

@app.get("/list")
def list_sensors(
    db: Session = Depends(get_db)
):

    return crud.get_sensors(db=db)

# =========================
# CREAR
# =========================

@app.post("/create")
def create_sensor(
    sensor: schemas.SensorBase,
    db: Session = Depends(get_db)
):

    return crud.create_sensor(
        db=db,
        sensor=sensor
    )