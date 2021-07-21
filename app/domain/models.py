from pydantic import BaseModel, Field


class DomainCreation(BaseModel):
    name: str = Field(min_length=3)
    password: str = Field(min_length=5)
    slug: str = Field(min_length=3, regex=r"(\w-_\d)*")
