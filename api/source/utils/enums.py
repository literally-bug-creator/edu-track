from enum import IntEnum


class CourseNumber(IntEnum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5


class SemesterNumber(IntEnum):
    FIRST = 1
    SECOND = 2


class WorkType(IntEnum):
    HOMEWORK = 0
    PRACTICAL_WORK = 1
    LABORATORY_WORK = 2
    VERIFICATION_WORK = 3
    COURSE_WORK = 4


class MarkType(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
