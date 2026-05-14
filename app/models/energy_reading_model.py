from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, ForeignKey, Date, Time, Text
from app.core.config import Base


class Reading(Base):

    __tablename__ = 'energy_reading'

    Reading_Id = Column(Integer, primary_key=True, index=True)

    voltaje = Column(Float, nullable=True)
    corriente = Column(Float, nullable=True )
    potencia = Column( Float, nullable=True  )
    energia = Column( Float, nullable=True )
    Sensor_Id = Column( Integer, ForeignKey("sensor.Sensor_Id"))
    fecha = Column( TIMESTAMP, server_default=func.now() )

    