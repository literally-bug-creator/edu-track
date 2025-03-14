from sqlalchemy import select

from database.models import Discipline, DisciplineGroup, User

from .base import BaseRepo


class StudentRepo(BaseRepo):
    MODEL = User

    async def get_disciplines(self, student_id: int):
        result = await self.session.execute(
            select(Discipline)
            .join(DisciplineGroup, DisciplineGroup.discipline_id == Discipline.id)
            .join(User, User.group_id == DisciplineGroup.group_id)
            .filter(User.id == student_id)
        )

        return result.scalars().all()
