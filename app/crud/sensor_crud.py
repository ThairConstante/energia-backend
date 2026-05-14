from sqlalchemy.orm import Session

from app.models.sensor_model import Sensor

def get_sensors(db: Session):

    return db.query(Sensor).all()

def create_sensor(
    db: Session,
    sensor
):

    new_sensor = Sensor(

        Sensor_Names=sensor.Sensor_Names,
        Sensortype_Id=sensor.Sensortype_Id
    )

    db.add(new_sensor)

    db.commit()

    db.refresh(new_sensor)

    return new_sensor