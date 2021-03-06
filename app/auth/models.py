from pydantic import BaseModel, Field


class LoginInfo(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)
