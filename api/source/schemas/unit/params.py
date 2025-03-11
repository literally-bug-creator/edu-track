from schemas.common.list import ListParams
from pydantic import BaseModel
from fastapi import Path


class Read(BaseModel):
    id: int = Path()


class Update(BaseModel):
    id: int = Path()


class Delete(BaseModel):
    id: int = Path()


class List(ListParams):
    pass
