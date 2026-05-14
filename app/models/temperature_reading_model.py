from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, ForeignKey, Date, Time, Text
from app.core.config import Base


class Reading(Base):

    __tablename__ = 'temperature_reading'

    Temperature_Id = Column(Integer, primary_key=True, index=True)

    temperatura = Column(Float, nullable=True)
    humedad = Column(Float, nullable=True )
    Sensor_Id = Column( Integer, ForeignKey("sensor.Sensor_Id"))
    fecha = Column( TIMESTAMP, server_default=func.now() )