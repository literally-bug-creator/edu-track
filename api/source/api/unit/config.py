from enum import StrEnum


PREFIX = "/units"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
