from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, ForeignKey, Date, Time, Text
from app.core.config import Base

class SensorType(Base):

    __tablename__ = 'sensor_type'

    Sensortype_Id = Column(Integer, primary_key=True, index=True)
    Sensor_Names = Column(String(50), nullable=False)
