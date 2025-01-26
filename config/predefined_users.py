from auth.user import PreDefinedUser
from auth.roles import PreDefinedRoles

PREDEFINED_USERS = [
    PreDefinedUser("student_user1", "password1", [PreDefinedRoles.STUDENT]),
    PreDefinedUser("teacher_user1", "password2", [PreDefinedRoles.TEACHER]),
    PreDefinedUser("student_user2", "password3", [PreDefinedRoles.STUDENT])
]