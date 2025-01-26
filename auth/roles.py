from config.roles import PreDefinedRoles
from config.permissions import Permission

# roles_index = {}
# for role in ROLES_DEFINITION:
#     roles_index[role.get_name()] = role

roles_index = {str(value).split(".")[1].lower(): value for member, value in PreDefinedRoles.__members__.items()}
print("ROLES:",roles_index)

def can_role_do(role: str, permission: Permission):
    if role not in roles_index:
        raise Exception("Role Does Not Exist")
    return permission in roles_index[role].value