from config.roles import Permission
class PreDefinedRole:
    def __init__(self, role_name: str, perms: list[Permission]):
        self.__role_name = role_name
        self.__perms = perms

    def can_do(self, perm: Permission):
        return perm in self.__perms

    def get_name(self):
        return self.__role_name


class PreDefinedUser:
    def __init__(self, username:str, password: str, roles: list[str]):
        self.__username = username
        self.__password = password
        self.__roles = roles

