from pydantic import BaseModel, Field


class DomainQuery(BaseModel):
    domain: str = Field(min_length=1)


class EntryQuery(DomainQuery):
    title: str = Field(regex=r"^[A-Za-z\-]+$")
    group: str = Field(regex=r"^[A-Za-z\-]+$")


class EntryCreation(EntryQuery):
    pass
