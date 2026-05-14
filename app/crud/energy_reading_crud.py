from sqlalchemy.orm import Session
from app.models.energy_reading_model import Reading

from app.schemas.energy_reading_schemas import ReadingCreate

# -------------------------
# GET ALL
# -------------------------

def get_readings(db: Session):

    return db.query(Reading).all()

# -------------------------
# GET LAST
# -------------------------

def get_last_reading(db: Session):

    return db.query(Reading)\
        .order_by(Reading.Reading_Id.desc())\
        .first()

# -------------------------
# CREATE
# -------------------------

def create_reading(
    db: Session,
    reading: ReadingCreate
):

    new_reading = Reading(

        voltaje=reading.voltaje,
        corriente=reading.corriente,
        potencia=reading.potencia,
        energia=reading.energia,
        Sensor_Id=reading.Sensor_Id
    )

    db.add(new_reading)

    db.commit()

    db.refresh(new_reading)

    return new_reading