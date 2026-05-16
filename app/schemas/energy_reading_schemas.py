from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -------------------------
# BASE
# -------------------------

class ReadingBase(BaseModel):

    voltaje: float
    corriente: float
    potencia: float
    energia: float
    Sensor_Id: int
    fecha: datetime

# -------------------------
# CREATE
# -------------------------

class ReadingCreate(ReadingBase):
    fecha: datetime

# -------------------------
# RESPONSE
# -------------------------

class Reading(ReadingBase):

    Reading_Id: int
    fecha: datetime

    class Config:
        from_attributes = True
