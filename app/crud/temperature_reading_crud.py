from sqlalchemy.orm import Session
from app.models.temperature_reading_model import Reading

from app.schemas.temperature_reading_schemas import ReadingCreate

# -------------------------
# GET ALL
# -------------------------

def get_readings(db: Session):

    return db.query(Reading)\
        .order_by(Reading.fecha.desc())\
        .all()

# -------------------------
# GET LAST
# -------------------------

def get_last_reading(db: Session):

    return db.query(Reading)\
        .order_by(Reading.Temperature_Id.desc())\
        .first()

# -------------------------
# CREATE
# -------------------------

def create_reading(
    db: Session,
    reading: ReadingCreate
):

    new_reading = Reading(

        temperatura=reading.temperatura,
        humedad=reading.humedad,
        Sensor_Id=reading.Sensor_Id
    )

    db.add(new_reading)

    db.commit()

    db.refresh(new_reading)

    return new_reading