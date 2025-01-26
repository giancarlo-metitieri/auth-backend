from config.permissions import Permission
from enum import Enum

class PreDefinedRoles(Enum):
    ADMIN = [Permission.IsAdmin]
    STUDENT = [Permission.CanDoXY, Permission.StudentAccess]
    TEACHER = [Permission.TeacherAccess]