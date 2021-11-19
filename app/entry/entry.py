import re
import uuid
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Entry:
    domain: str
    title: str
    slug: str
    group: str
    definitions: list[str]
    translations: list[str]
    image: str = None
    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat(),
    )
    updated_at: datetime = field(default=None)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    _type: str = None
    _index: str = None
    _id: str = None

    def __post_init__(self):
        if self._id:
            self.id = self._id

    def update_date(self) -> None:
        self.updated_at = datetime.utcnow()

    def to_json(self, resumed=False):
        if not resumed:
            return self.__to_complete_json()
        return self.__to_json()

    def __to_json(self):
        return {
            "id": str(self.id),
            "domain": self.domain,
            "title": self.title,
            "group": self.group,
            "definitions": self.definitions[0],
            "created_at": self.created_at,
        }

    def __to_complete_json(self):
        json = self.__to_json()
        return json | {
            "definitions": self.definitions,
            "translations": self.translations,
            "image": self.image,
        }
