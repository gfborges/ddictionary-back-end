from datetime import datetime
from flask_jwt_extended.utils import get_jwt_identity
from pydantic import BaseModel, Field, validator
from typing import Optional


class DomainQuery(BaseModel):
    domain: Optional[str] = Field(min_length=1)
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")


class EntryQuery(DomainQuery):
    title: str = Field(regex=r"^[A-Za-z\-]+$")
    group: str = Field(regex=r"^[A-Za-z\-]+$")


class EntryCreation(EntryQuery):
    definitions: list[str] = Field(min_length=1)
    translations: Optional[list[str]] = Field(default=[])
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
    title: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")
    definitions: Optional[list[str]] = Field(min_length=1)
    translations: Optional[list[str]] = Field(min_length=1)
    domain: str = None

    @validator("domain", pre=True, always=True)
    def set_domain(cls, v):
        domain_slug = get_jwt_identity()
        return v or domain_slug
