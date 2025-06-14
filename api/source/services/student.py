from collections import defaultdict

from database.repos import DisciplineGroupRepo, MarkRepo, StudentRepo
from fastapi import Depends, HTTPException, status
from schemas.auth.common import User, UserRole
from schemas.discipline.common import Discipline, DisciplineMarksAvg
from schemas.mark.common import AvgMarkByDate, ExtendedMark, MarksDistribution, MarkType
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

        extended_marks = []
        marks = await self.mark_repo.get_student_extended_marks(pms, pms.id)
        for mark, discipline_name in marks:
            extended_marks.append(
                ExtendedMark(
                    discipline_id=mark.discipline_id,
                    student_id=mark.student_id,
                    work_type=mark.work_type,
                    type=mark.type,
                    date=mark.date,
                    discipline_name=discipline_name,
                )
            )
        return responses.ListMarks(
            items=extended_marks,
            total=len(extended_marks),
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

        items = await self.repo.get_disciplines(student.id)
        return responses.ListDisciplines(
            items=[
                Discipline.model_validate(obj, from_attributes=True) for obj in items
            ],
            total=len(items),
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

        marks = await self.mark_repo.get_marks_per_discipline(student.id)

        disciplines_marks = defaultdict(list)
        disciplines_names = {}

        for discipline_id, discipline_name, mark in marks:
            disciplines_marks[discipline_id].append(mark)
            disciplines_names[discipline_id] = discipline_name

        average_marks = []
        for discipline_id, marks_list in disciplines_marks.items():
            avg_mark = sum(marks_list) / len(marks_list)
            average_marks.append(
                DisciplineMarksAvg(
                    discipline_id=discipline_id,
                    discipline_name=discipline_name,
                    avg_mark=avg_mark,
                )
            )

        return responses.ListDisciplinesMarksAvg(
            items=average_marks,
            total=len(average_marks),
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

        date_marks = defaultdict(list)
        for mark in marks:
            date_marks[mark[0].date.date()].append(mark[0].type.value)

        average_marks_per_date = []
        for mark_date, marks_list in date_marks.items():
            avg_mark = sum(marks_list) / len(marks_list)
            average_marks_per_date.append(AvgMarkByDate(date=mark_date, value=avg_mark))

        return responses.ListMarksAvgByDate(
            items=average_marks_per_date,
            total=len(average_marks_per_date),
        )
