from typing import Any
from app.domain.domain import Domain
from dataclasses import dataclass, field
from datetime import datetime
from bson.objectid import ObjectId


@dataclass
class Entry:
    domain: str
    title: str
    group: str
    definitions: list[str]
    transtaltions: list[str]
    image: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default=None)
    _id: ObjectId = field(default_factory=ObjectId)

    def update_date(self) -> None:
        self.updated_at = datetime.utcnow()

    def to_json(self, complete=False):
        if complete:
            return self.__to_complete_json()
        return self.__to_json()

    def __to_json(self):
        return {
            "_id": str(self.get("_id")),
            "domain": self.get("domain"),
            "title": self.get("title"),
            "group": self.get("group"),
            "definitions": self.get("definitions")[0],
            "created_at": self.get("created_at").isoformat(),
        }

    def __to_complete_json(self):
        json = self.__to_json()
        return json | {
            "definitions": json.get("definitions"),
            "translations": json.get("translations"),
            "image": json.get("image"),
        }
