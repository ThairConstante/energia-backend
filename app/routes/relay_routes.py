from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.auth_token import decode_token

from app.core.config import get_db

import app.crud.relay_crud as crud

import app.schemas.relay_schemas as schemas

app = APIRouter()

# =========================
# LISTAR
# =========================

@app.get(
    "/list",
    
)
def list_relays(
    db: Session = Depends(get_db)
):

    return crud.get_relays(db=db)


# =========================
# OBTENER UNO
# =========================

@app.get(
    "/{relay_id}",
    dependencies=[Depends(decode_token)]
)
def get_relay(
    relay_id: int,
    db: Session = Depends(get_db)
):

    relay = crud.get_relay(
        db=db,
        relay_id=relay_id
    )

    if not relay:

        raise HTTPException(
            status_code=404,
            detail="Relay no encontrado"
        )

    return relay


# =========================
# CREAR
# =========================

@app.post(
    "/create",

    
)
def create_relay(
    relay: schemas.RelayCreate,
    db: Session = Depends(get_db)
):

    return crud.create_relay(
        db=db,
        relay=relay
    )


# =========================
# ACTUALIZAR
# =========================

@app.put(
    "/update/{relay_id}"
)
def update_relay(
    relay_id: int,
    relay: schemas.RelayUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_relay(

        db=db,

        relay_id=relay_id,

        relay=relay
    )

    if not updated:

        raise HTTPException(
            status_code=404,
            detail="Relay no encontrado"
        )

    return updated

