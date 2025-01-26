from config.predefined_users import PREDEFINED_USERS
from config.roles import PreDefinedRoles

predefined_users_list = []
for u  in PREDEFINED_USERS:
    roles = [ str(r).split(".")[1].lower() for r in u.get_roles()]
    username = u.get_username()
    password = u.get_password()
    predefined_users_list.append({"username": username, "password": password, "roles": roles})
print(predefined_users_list)
