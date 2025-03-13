from datetime import datetime
from typing import Any, Iterable

from database.models import Mark

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
