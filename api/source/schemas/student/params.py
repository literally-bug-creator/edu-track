from schemas.common.list import ListParams
from pydantic import BaseModel
from fastapi import Path, Depends
from schemas.marks.common import MarkFilters


class Read(BaseModel):
    id: int = Path()


class Update(BaseModel):
    id: int = Path()


class Delete(BaseModel):
    id: int = Path()


class List(ListParams):
    pass


class ListMarks(ListParams):
    id: int = Path()
    filters: MarkFilters = Depends()


class ListDisciplines(ListParams):
    id: int = Path()


class ReadMarksDistribution(BaseModel):
    id: int = Path()
