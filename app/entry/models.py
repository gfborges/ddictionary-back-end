from datetime import datetime
from flask_jwt_extended.utils import get_jwt_identity
from pydantic import BaseModel, Field, validator
from typing import Optional


class DomainQuery(BaseModel):
    domain: str = Field(min_length=1)
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")


class EntryQuery(DomainQuery):
    title: str = Field()
    group: str = Field(regex=r"^[A-Za-z\-]+$")
    log: bool = Field(default=False)


class EntryCreation(EntryQuery):
    title: str = Field(min_length=1)
    group: str = Field(regex=r"^[A-Za-z\-]+$", min_length=1)
    domain: str = Field(min_length=1)
    definitions: list[str] = Field(min_length=1)
    translations: Optional[list[str]] = Field(default_factory=list)
    created_at: Optional[datetime] = Field(default=None)
    image: Optional[str] = Field(
        regex=r"^data:image/.*;base64,[A-Za-z0-9\+/]+={0,2}$",
        max_length=2_700_20,
    )

    @validator("created_at", pre=True, always=True)
    def set_ts_now(cls, v):
        return datetime.utcnow()

    @validator("domain", pre=True, always=True)
    def set_domain(cls, v):
        domain_slug = get_jwt_identity()
        return v or domain_slug


class EntryUpdate(BaseModel):
    title: Optional[str]
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")
    definitions: Optional[list[str]] = Field(min_length=1)
    translations: Optional[list[str]] = Field(min_length=1)
    domain: str = None

    @validator("domain", pre=True, always=True)
    def set_domain(cls, v):
        domain_slug = get_jwt_identity()
        return v or domain_slug


class EntrySearch(BaseModel):
    domain: str
    text: str
    skip: int = Field(default=0)
    size: int = Field(default=10)
    log: bool = False
