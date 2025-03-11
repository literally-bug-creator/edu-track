from sqlalchemy import and_, or_
from typing import Optional
from datetime import date
from .database.repos.base import BaseRepo
from .database.models.mark import Mark
from FastAPI import Depends
from .utils.enums import WorkType, CourseNumber, SemesterNumber


class StatsService:
    def __init__(
        self,
        mark_repo: BaseRepo,  
        discipline_repo: BaseRepo,
        user: "User" = Depends(get_user)
    ):
        self.mark_repo = mark_repo
        self.discipline_repo = discipline_repo
        self.user 

    async def _get_discipline_filters(
        self,
        course: Optional[int],
        semester: Optional[int]
    ) -> list[int]:
        where = []
        if course is not None:
            where.append(self.discipline_repo.model.course == course)
        if semester is not None:
            where.append(self.discipline_repo.model.semester == semester)
        
        if not where:
            return []
            
        disciplines = await self.discipline_repo.filter(*where)
        return [d.id for d in disciplines]

    async def get_average(
        self,
        student_id: int,
        discipline_id: int | None = None,
        course: CourseNumber | None = None,
        semester: SemesterNumber | None = None,
        period_start: date | None = None,
        period_end: date | None = None
    ) -> float:
        mark_where = [self.mark_repo.model.student_id == student_id]
        
        if discipline_id:
            mark_where.append(self.mark_repo.model.discipline_id == discipline_id)
        else:
            discipline_ids = await self._get_discipline_filters(course, semester)
            if discipline_ids:
                mark_where.append(self.mark_repo.model.discipline_id.in_(discipline_ids))

        if period_start and period_end:
            mark_where.append(self.mark_repo.model.date.between(period_start, period_end))
            
        marks = await self.mark_repo.filter(*mark_where)
        if not marks:
            return 0.0
            
        return sum(m.value for m in marks) / len(marks)

    async def get_marks(
        self,
        student_id: int,
        discipline_id: int | None = None,
        course: CourseNumber | None = None,
        semester: SemesterNumber | None = None,
        work_type: WorkType | None = None,
        period_start: date | None = None,
        period_end: date | None = None
    ) -> list[Mark]:
        discipline_ids = []
        if course or semester:
            discipline_ids = await self._get_discipline_filters(course, semester)
        
        mark_where = [self.mark_repo.model.student_id == student_id]
        
        if discipline_id:
            mark_where.append(self.mark_repo.model.discipline_id == discipline_id)
        elif discipline_ids:
            mark_where.append(self.mark_repo.model.discipline_id.in_(discipline_ids))
            
        if work_type is not None:
            mark_where.append(self.mark_repo.model.work_type == work_type)
            
        if period_start and period_end:
            mark_where.append(self.mark_repo.model.date.between(period_start, period_end))
            
        return await self.mark_repo.filter(*mark_where)