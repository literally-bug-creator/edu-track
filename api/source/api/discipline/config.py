from enum import StrEnum


PREFIX = "/disciplines"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
