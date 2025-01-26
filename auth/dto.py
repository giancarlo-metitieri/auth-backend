from pydantic import BaseModel

class SignupRequest(BaseModel):
    username: str
    password: str

class AccessRequest(BaseModel):
    permission: str

class GetUserRequest(BaseModel):
    username: str

