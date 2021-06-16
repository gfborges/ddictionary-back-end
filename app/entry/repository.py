from bson.objectid import ObjectId
from app.entry.entry import Entry
from app.entry.models import EntryCreation
from app.database.mongo import get_db

mongo = get_db()


class EntryReposiory:
    @staticmethod
    def get_all(domain: str) -> list[dict]:
        cursor = mongo.db.entries.find(filter={"domain": domain})
        return [Entry.new_entry(entry) for entry in cursor]

    @staticmethod
    def get_one(domain: str, group: str, title: str) -> Entry:
        entry = mongo.db.entries.find_one(
            filter={
                "domain": domain,
                "group": group,
                "title": title,
            }
        )
        return Entry.new_entry(entry)

    @staticmethod
    def get(id: str) -> Entry:
        entry = mongo.db.entries.find_one(
            filter={
                "_id": ObjectId(id),
            }
        )
        return Entry.new_entry(entry)

    @staticmethod
    def save(entry: EntryCreation) -> None:
        return mongo.db.entries.insert_one(entry.dict())

    @staticmethod
    def delete(id: str) -> None:
        return mongo.db.entries.delete_one(
            filter={
                "_id": ObjectId(id),
            },
        )

    @staticmethod
    def update(id: str, entry):
        print(entry.dict())
        result = mongo.db.entries.update_one(
            filter=dict(_id=ObjectId(id)), update={"$set": entry.dict()}
        )
        print(result.matched_count, result.modified_count)
        return result
