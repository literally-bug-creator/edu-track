from datetime import datetime
from typing import Any, Iterable

from sqlalchemy import func, select

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

    async def get_average_marks_per_discipline(self, student_id: int):
        result = await self.session.execute(
            select(
                Discipline.id,
                Discipline.name,
                func.avg(Mark.type).label("avg_mark"),
            )
            .join(Mark, Discipline.id == Mark.discipline_id)
            .filter(Mark.student_id == student_id)
            .group_by(Discipline.id, Discipline.name)
        )

        average_marks = [
            {"discipline_id": row[0], "discipline_name": row[1], "avg_mark": row[2]}
            for row in result.fetchall()
        ]

        return average_marks
