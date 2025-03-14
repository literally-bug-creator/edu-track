from enum import StrEnum


PREFIX = "/disciplines"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""

    CREATE_GROUP = "/{id}/groups/{group_id}"
    READ_GROUP = "/{id}/groups/{group_id}"
    DELETE_GROUP = "/{id}/groups/{group_id}"
    LIST_GROUPS = "/{id}/groups"

    CREATE_TEACHER = "/{id}/teachers/{teacher_id}"
    READ_TEACHER = "/{id}/teachers/{teacher_id}"
    DELETE_TEACHER = "/{id}/teachers/{teacher_id}"
    LIST_TEACHERS = "/{id}/teachers"
