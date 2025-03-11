from enum import StrEnum


PREFIX = "/tracks"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
