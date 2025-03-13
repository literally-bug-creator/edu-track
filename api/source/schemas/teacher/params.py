from fastapi import Path
from pydantic import BaseModel
from schemas.common.list import ListParams


class Read(BaseModel):
    id: int = Path()


class Update(BaseModel):
    id: int = Path()


class Delete(BaseModel):
    id: int = Path()


class List(ListParams):
    pass
