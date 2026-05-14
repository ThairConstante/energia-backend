from pydantic import BaseModel

class SensorBase(BaseModel):

    Sensor_Names: str
    Sensortype_Id: int