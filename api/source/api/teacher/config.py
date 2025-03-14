from enum import StrEnum


PREFIX = "/teachers"


class EPath(StrEnum):
    CREATE = ""
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
    LIST = ""
    LIST_DISCIPLINES = "/{id}/disciplines"
    READ_DISCIPLINE_AVG_MARK = "/{id}/disciplines/{discipline_id}/avg-mark"
    READ_GROUP = "/{id}/groups/{group_id}"
