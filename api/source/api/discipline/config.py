from enum import StrEnum


PREFIX = "/disciplines"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""

    CREATE_GROUP = "/{id}/{group_id}"
    READ_GROUP = "/{id}/{group_id}"
    DELETE_GROUP = "/{id}/{group_id}"

    CREATE_TEACHER = "/{id}/{group_id}"
    READ_TEACHER = "/{id}/{group_id}"
    DELETE_TEACHER = "/{id}/{group_id}"
