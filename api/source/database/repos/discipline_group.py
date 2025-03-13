from typing import Any

from sqlalchemy import func, select

from database.models import DisciplineGroup, Group

from .base import BaseRepo


class DisciplineGroupRepo(BaseRepo):
    MODEL = DisciplineGroup

    async def count(self, **filters: Any) -> int | Any:
        query = self._get_query(func.count(self.model.discipline_id)).filter_by(
            **filters
        )
        return (await self.execute(query)).scalar_one()
    
    async def list_groups(self, discipline_id):
        query = select(Group).join(DisciplineGroup).filter(DisciplineGroup.discipline_id == discipline_id)
        items = (await self.execute(query)).scalars()
        return items, len(items)

