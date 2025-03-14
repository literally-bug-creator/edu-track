from datetime import datetime
from typing import Any, Iterable

from sqlalchemy import select

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
        result = await self.session.execute(
            select(Mark)
            .filter(Mark.student_id == student_id)
            .filter(Mark.date >= date_from)
            .filter(Mark.date <= date_to)
        )

        return result.fetchall()

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

    async def get_student_extended_marks(self, student_id: int):
        results = (
            self.session.query(Mark, Discipline.name.label("discipline_name"))
            .join(Discipline, Discipline.id == Mark.discipline_id)
            .filter(Mark.student_id == student_id)
            .all()
        )

        return results
