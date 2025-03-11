from enum import StrEnum


PREFIX = "/groups"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
