from typing import Any

from sqlalchemy import func

from database.models import DisciplineGroup

from .base import BaseRepo


class DisciplineGroupRepo(BaseRepo):
    MODEL = DisciplineGroup

    async def count(self, **filters: Any) -> int | Any:
        query = self._get_query(func.count(self.model.discipline_id)).filter_by(
            **filters
        )
        return (await self.execute(query)).scalar_one()
