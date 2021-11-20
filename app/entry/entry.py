import uuid
from dataclasses import dataclass, field
from datetime import datetime


class Entry:
    def __init__(self, **kwargs) -> None:
        self.domain = kwargs.get("domain")
        self.title = kwargs.get("title")
        self.group = kwargs.get("group")
        self.definitions = kwargs.get("definitions")
        self.translations = kwargs.get("translations")
        self.image = kwargs.get("image")
        self.created_at = kwargs.get(
            "created_at",
            datetime.utcnow().isoformat(),
        )
        self.id = kwargs.get("id", uuid.uuid4())
        self._id = kwargs.get("_id")

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
