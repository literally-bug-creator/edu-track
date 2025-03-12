from enum import StrEnum


PREFIX = "/students"


class EPath(StrEnum):
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
    LIST_MARKS = "/{id}/marks"
