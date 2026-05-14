from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text
from app.core.config import Base


class Sensor(Base):

    __tablename__ = 'sensor'

    Sensor_Id = Column(Integer, primary_key=True, index=True)
    Sensor_Names = Column(String(20), nullable=False)
   

    Sensortype_Id = Column(Integer, ForeignKey("sensor_type.Sensortype_Id"))
