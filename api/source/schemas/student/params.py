from datetime import date

from fastapi import Depends, Path
from pydantic import BaseModel
from schemas.common.list import ListParams
from schemas.mark.common import MarkFilters


class Read(BaseModel):
    id: int = Path()


class ReadMarksDistribution(BaseModel):
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


class ListDisciplinesMarksAvg(ListParams):
    id: int = Path()


class ListMarksAvgByDate(BaseModel):
    id: int = Path()
    date_from: date | None
    date_to: date | None
