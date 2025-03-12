from enum import StrEnum


PREFIX = "/students"


class EPath(StrEnum):
    READ = "/{id}"
    READ_MARKS_DISTRIBUTION = "/{id}/marks/distribution"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
    LIST_MARKS = "/{id}/marks"
    LIST_DISCIPLINES = "/{id}/disciplines"
    LIST_DISCIPLINES_MARKS_AVG = "/{id}/disciplines/marksAvg"
