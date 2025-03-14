from collections import defaultdict
from statistics import mean

from database.repos import DisciplineGroupRepo, MarkRepo, StudentRepo
from fastapi import Depends, HTTPException, status
from schemas.auth.common import User, UserRole
from schemas.discipline.common import Discipline, DisciplineMarksAvg
from schemas.mark.common import Mark, MarksDistribution, MarkType, AvgMarkByDate
from schemas.student import bodies, params, responses
from schemas.student.common import Student


class StudentService:
    def __init__(
        self,
        repo: StudentRepo = Depends(StudentRepo),
        mark_repo: MarkRepo = Depends(MarkRepo),
        disc_group_repo: DisciplineGroupRepo = Depends(DisciplineGroupRepo),
    ) -> None:
        self.repo = repo
        self.mark_repo = mark_repo
        self.disc_group_repo = disc_group_repo

    async def read(
        self,
        pms: params.Read,
        user: User,
    ) -> responses.Read:
        if (user.role == UserRole.STUDENT) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.STUDENT
            )
        ):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = Student.model_validate(model, from_attributes=True)
        return responses.Read(item=scheme)

    async def read_marks_distribution(
        self,
        pms: params.ReadMarksDistribution,
        user: User,
    ) -> responses.ReadMarksDistribution:
        if (user.role == UserRole.STUDENT) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        distribution: dict[MarkType, int] = dict.fromkeys(MarkType, 0)

        if not (student := await self.repo.filter_one(id=pms.id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        items = await self.mark_repo.filter(student_id=student.id)

        for item in items:
            distribution[item.type] += 1

        return responses.ReadMarksDistribution(
            item=MarksDistribution(items=distribution),
        )

    async def update(
        self,
        pms: params.Update,
        body: bodies.Update,
        user: User,
    ) -> responses.Update:
        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.STUDENT
            )
        ):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        upd_model = await self.repo.update(model, **body.model_dump(exclude_none=True))

        if upd_model is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = Student.model_validate(upd_model, from_attributes=True)
        return responses.Update(item=scheme)

    async def delete(
        self,
        pms: params.Delete,
        user: User,
    ) -> None:
        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.STUDENT
            )
        ):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        await self.repo.delete(model)

    async def list(
        self,
        pms: params.List,
        user: User,
    ) -> responses.List:
        items, total = await self.repo.list(params=pms, role=UserRole.STUDENT)
        return responses.List(
            items=[Student.model_validate(obj, from_attributes=True) for obj in items],
            total=total,
        )

    async def list_marks(
        self,
        pms: params.ListMarks,
        user: User,
    ) -> responses.ListMarks:
        if (user.role == UserRole.STUDENT) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (await self.repo.filter_one(id=pms.id)):
            return responses.ListMarks(
                items=[],
                total=0,
            )

        items, total = await self.mark_repo.list(
            params=pms,
            student_id=pms.id,
            **pms.filters.model_dump(exclude_none=True),
        )
        return responses.ListMarks(
            items=[Mark.model_validate(obj, from_attributes=True) for obj in items],
            total=total,
        )

    async def list_disciplines(
        self,
        pms: params.ListDisciplines,
        user: User,
    ) -> responses.ListDisciplines:
        if (user.role == UserRole.STUDENT) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (student := await self.repo.filter_one(id=pms.id)):
            return responses.ListDisciplines(items=[], total=0)

        items, total = await self.disc_group_repo.list(
            params=pms,
            group_id=student.group_id,
        )
        return responses.ListDisciplines(
            items=[
                Discipline.model_validate(obj, from_attributes=True) for obj in items
            ],
            total=total,
        )

    async def list_disciplines_marks_avg(
        self,
        pms: params.ListDisciplinesMarksAvg,
        user: User,
    ) -> responses.ListDisciplinesMarksAvg:
        if (user.role == UserRole.STUDENT) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (student := await self.repo.filter_one(id=pms.id)):
            return responses.ListDisciplinesMarksAvg(items=[], total=0)

        marks, _ = await self.mark_repo.list(
            params=pms,
            student_id=student.id,
        )

        discipline_marks = defaultdict(list)

        for mark in marks:
            discipline_marks[mark.discipline_id].append(mark.type)

        discipline_marks_avg = []
        for discipline_id, grades in discipline_marks.items():
            average_grade = mean(grades)
            discipline_marks_avg.append(
                DisciplineMarksAvg(
                    discipline_id=discipline_id,
                    average_grade=average_grade,
                )
            )

        return responses.ListDisciplinesMarksAvg(
            items=discipline_marks_avg,
            total=len(discipline_marks_avg),
        )

    async def list_marks_avg_by_date(
        self,
        pms: params.ListMarksAvgByDate,
        user: User,
    ) -> responses.ListMarksAvgByDate:
        if (user.role == UserRole.STUDENT) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (student := await self.repo.filter_one(id=pms.id)):
            return responses.ListMarksAvgByDate(items=[], total=0)

        marks = await self.mark_repo.filter_by_date(
            student.id,
            pms.date_from,
            pms.date_to,
        )

        marks_by_date = defaultdict(list)
        for mark in marks:
            marks_by_date[mark.date.date()].append(mark.type.value)

        average_marks = [
            AvgMarkByDate(date=date, value=sum(scores) / len(scores))
            for date, scores in marks_by_date.items()
        ]

        average_marks.sort(key=lambda x: x.date)

        return responses.ListMarksAvgByDate(
            items=average_marks,
            total=len(average_marks),
        )
