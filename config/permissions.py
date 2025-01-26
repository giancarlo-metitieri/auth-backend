import enum

class Permission(enum.Enum):
    IsAdmin = "isAdmin"
    CanDoXY = "canDoXY"
    TeacherAccess = "TeacherAccess"
    StudentAccess = "StudentAccess"