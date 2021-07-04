from bson.objectid import ObjectId
from app.entry.models import EntryCreation
from datetime import datetime


class Entry:
    def __init__(
        self,
        _id: ObjectId,
        domain: str,
        title: str,
        group: str,
        definitions: list[str],
        translations: list[str] = None,
        image: str = None,
        createdAt: list[str] = datetime.utcnow(),
    ):
        self.id = _id
        self.domain = domain
        self.title = title
        self.group = group
        self.definitions = definitions
        self.translations = translations or []
        self.createdAt = createdAt
        self.image = image

    @staticmethod
    def new_entry(data: EntryCreation):
        if data is not None:
            return Entry(**data)
        return None

    def dict(self):
        return dict(
            _id=self.id,
            domain=self.domain,
            title=self.title,
            group=self.group,
            definitions=self.definitions,
            translations=self.translations,
            createdAt=self.createdAt,
        )

    def to_json(self):
        return dict(
            id=str(self.id),
            domain=self.domain,
            title=self.title,
            group=self.group,
            definitions=self.definitions,
            translations=self.translations,
            createdAt=self.createdAt.isoformat(),
            image=self.image,
        )

    def to_simple_json(self):
        return dict(
            id=str(self.id),
            domain=self.domain,
            title=self.title,
            group=self.group,
            definitions=self.definitions[:1],
        )
