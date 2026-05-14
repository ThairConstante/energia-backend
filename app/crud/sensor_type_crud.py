from sqlalchemy.orm import Session

from app.models.sensor_type_model import SensorType

def get_sensor_types(db: Session):

    return db.query(SensorType).all()

def create_sensor_type(
    db: Session,
    sensor_type
):

    new_sensor_type = SensorType(

        Sensor_Names=sensor_type.Sensor_Names
    )

    db.add(new_sensor_type)

    db.commit()

    db.refresh(new_sensor_type)

    return new_sensor_type