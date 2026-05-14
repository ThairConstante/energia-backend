from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.config import get_db

import app.crud.sensor_type_crud as crud
import app.schemas.sensor_type_schemas as schemas

app = APIRouter()

# =========================
# LISTAR
# =========================

@app.get("/list")
def list_sensor_types(
    db: Session = Depends(get_db)
):

    return crud.get_sensor_types(db=db)

# =========================
# CREAR
# =========================

@app.post("/create")
def create_sensor_type(
    sensor_type: schemas.SensorTypeBase,
    db: Session = Depends(get_db)
):

    return crud.create_sensor_type(
        db=db,
        sensor_type=sensor_type
    )