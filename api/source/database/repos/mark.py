from datetime import datetime
from typing import Any, Iterable

from sqlalchemy import Integer, cast, func, select

from database.models import Discipline, Mark

from .base import BaseRepo


class MarkRepo(BaseRepo):
    MODEL = Mark

    async def filter_by_date(
        self,
        student_id: int,
        date_from: datetime,
        date_to: datetime,
    ) -> Iterable[MODEL] | Any:
        query = self._get_query().filter(
            Mark.student_id == student_id,
            Mark.date >= date_from,
            Mark.date <= date_to,
        )
        return (await self.execute(query)).scalars()

    async def get_marks_per_discipline(self, student_id: int):
        result = await self.session.execute(
            select(
                Discipline.id,
                Discipline.name,
                Mark.type,
            )
            .join(Mark, Discipline.id == Mark.discipline_id)
            .filter(Mark.student_id == student_id)
        )

        return result.fetchall()
