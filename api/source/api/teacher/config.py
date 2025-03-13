from enum import StrEnum


PREFIX = "/teachers"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
    LIST_DISCIPLINES = "/{id}/disciplines"
