from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -------------------------
# BASE
# -------------------------

class ReadingBase(BaseModel):

    temperatura: float
    humedad: float
    Sensor_Id: int

# -------------------------
# CREATE
# -------------------------

class ReadingCreate(ReadingBase):
    pass

# -------------------------
# RESPONSE
# -------------------------

class Reading(ReadingBase):

    Reading_Id: int
    fecha: datetime

    class Config:
        from_attributes = True