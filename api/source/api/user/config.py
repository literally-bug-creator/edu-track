from enum import StrEnum


PREFIX = "/users"


class EPath(StrEnum):
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
