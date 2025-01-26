from pydantic import BaseModel
from auth.roles import PreDefinedRoles
class User(BaseModel):
    username: str
    password: str


class PreDefinedUser:
    def __init__(self, username: str, password: str, roles: list[PreDefinedRoles]):
        self.__username = username
        self.__password = password
        self.__roles = roles

    def get_password(self):
        return self.__password

    def get_username(self):
        return self.__username

    def get_roles(self):
        return self.__roles