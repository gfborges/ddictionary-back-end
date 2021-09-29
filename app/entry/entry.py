import uuid
from dataclasses import dataclass, field
from datetime import datetime
from bson.objectid import ObjectId


@dataclass
class Entry:
    domain: str
    title: str
    group: str
    definitions: list[str]
    translations: list[str]
    image: str = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default=None)
    _id: ObjectId = field(default_factory=lambda: str(uuid.uuid4()))

    def update_date(self) -> None:
        self.updated_at = datetime.utcnow()

    def to_json(self, resumed=False):
        if not resumed:
            return self.__to_complete_json()
        print("here")
        return self.__to_json()

    def __to_json(self):
        return {
            "_id": str(self._id),
            "domain": self.domain,
            "title": self.title,
            "group": self.group,
            "definitions": self.definitions[0],
            "created_at": self.created_at.isoformat(),
        }

    def __to_complete_json(self):
        json = self.__to_json()
        return json | {
            "definitions": self.definitions,
            "translations": self.translations,
            "image": self.image,
        }
