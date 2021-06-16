from pydantic import BaseModel, Field
from typing import Optional


class DomainQuery(BaseModel):
    domain: str = Field(min_length=1)
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")


class EntryQuery(DomainQuery):
    title: str = Field(regex=r"^[A-Za-z\-]+$")
    group: str = Field(regex=r"^[A-Za-z\-]+$")


class EntryCreation(EntryQuery):
    definitions: list[str] = Field(min_length=1)
    translations: Optional[list[str]] = Field(min_length=1)


class EntryUpdate(BaseModel):
    title: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")
    definitions: Optional[list[str]] = Field(min_length=1)
    translations: Optional[list[str]] = Field(min_length=1)
