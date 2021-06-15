from bson.objectid import ObjectId
from app.entry.entry import Entry
from app.entry.models import EntryCreation
from app.database.mongo import get_db


class EntryReposiory:
    mongo = get_db()

    @classmethod
    def get_all(self, domain: str) -> list[dict]:
        cursor = self.mongo.db.entries.find(filter={"domain": domain})
        return [Entry.new_entry(entry) for entry in cursor]

    @classmethod
    def get_one(self, domain: str, group: str, title: str) -> Entry:
        entry = self.mongo.db.entries.find_one(
            filter={
                "domain": domain,
                "group": group,
                "title": title,
            }
        )
        return Entry.new_entry(entry)

    @classmethod
    def get(self, id: str) -> Entry:
        entry = self.mongo.db.entries.find_one(
            filter={
                "_id": ObjectId(id),
            }
        )
        return Entry.new_entry(entry)

    @classmethod
    def save(self, entry: EntryCreation) -> None:
        return self.mongo.db.entries.insert_one(entry.dict())

    @classmethod
    def delete(self, domain: str, group: str, title: str) -> None:
        return self.mongo.db.entries.delete_one(
            filter={
                "domain": domain,
                "group": group,
                "title": title,
            },
        )
