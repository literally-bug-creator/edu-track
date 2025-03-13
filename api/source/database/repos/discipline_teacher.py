from .base import BaseRepo
from database.models import DisciplineTeacher
from typing import Any
from sqlalchemy import func


class DisciplineTeacherRepo(BaseRepo):
    MODEL = DisciplineTeacher

    async def count(self, **filters: Any) -> int | Any:
        query = self._get_query(func.count(self.model.discipline_id)).filter_by(
            **filters
        )
        return (await self.execute(query)).scalar_one()
