from sqlalchemy.orm import Session

from app.models.relay_model import Relay

from app.schemas.relay_schemas import (
    RelayCreate,
    RelayUpdate
)

# =========================
# LISTAR
# =========================

def get_relays(db: Session):

    return db.query(Relay).all()


# =========================
# OBTENER UNO
# =========================

def get_relay(
    db: Session,
    relay_id: int
):

    return db.query(Relay).filter(
        Relay.Relay_Id == relay_id
    ).first()


# =========================
# CREAR
# =========================

def create_relay(
    db: Session,
    relay: RelayCreate
):

    db_relay = Relay(

        Relay_Name = relay.Relay_Name,

        status = relay.status
    )

    db.add(db_relay)

    db.commit()

    db.refresh(db_relay)

    return db_relay


# =========================
# ACTUALIZAR
# =========================

def update_relay(
    db: Session,
    relay_id: int,
    relay: RelayUpdate
):

    db_relay = db.query(Relay).filter(
        Relay.Relay_Id == relay_id
    ).first()

    if not db_relay:
        return None

    if relay.Relay_Name is not None:
        db_relay.Relay_Name = relay.Relay_Name

    if relay.status is not None:
        db_relay.status = relay.status

    db.commit()

    db.refresh(db_relay)

    return db_relay


# =========================
# ELIMINAR
# =========================

def delete_relay(
    db: Session,
    relay_id: int
):

    db_relay = db.query(Relay).filter(
        Relay.Relay_Id == relay_id
    ).first()

    if not db_relay:
        return None

    db.delete(db_relay)

    db.commit()

    return db_relay