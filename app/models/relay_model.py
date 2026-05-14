from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from app.core.config import Base

class Relay(Base):

    __tablename__ = "relay"

    Relay_Id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    Relay_Name = Column(
        String(50),
        nullable=False
    )

    status = Column(
        Boolean,
        default=False
    )