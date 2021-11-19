from pydantic import BaseModel


class GroupCreation(BaseModel):
    slug: str


class GroupUpdate(BaseModel):
    title: str
    domain: str
    slug: str
