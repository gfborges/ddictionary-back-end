from pydantic import BaseModel, Field


class EntryCreation(BaseModel):
    title: str = Field(regex=r"^[A-Za-z\-]+$")
    group: str = Field(regex=r"^[A-Za-z\-]+$")
