from pydantic import BaseModel
from typing import Optional

# =========================
# BASE
# =========================

class RelayBase(BaseModel):

    Relay_Name: str

    status: bool


# =========================
# CREATE
# =========================

class RelayCreate(RelayBase):
    pass


# =========================
# UPDATE
# =========================

class RelayUpdate(BaseModel):

    Relay_Name: Optional[str] = None

    status: Optional[bool] = None