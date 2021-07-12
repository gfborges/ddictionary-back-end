from bson.objectid import ObjectId
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.database.mongo import get_db
from app.entry.repositories import image_repository

mongo = get_db()


def get_all(domain: str) -> tuple[bool, list[dict]]:
    cursor = mongo.db.entries.find(filter={"domain": domain})
    return True, list(cursor)


def get_one(domain: str, group: str, title: str) -> tuple[bool, dict]:
    entry = mongo.db.entries.find_one(
        filter={
            "domain": domain,
            "group": group,
            "title": title,
        }
    )
    ok = entry is not None
    return ok, entry


def get(id: str) -> tuple[bool, dict]:
    entry = mongo.db.entries.find_one(
        filter={
            "_id": ObjectId(id),
        }
    )
    ok = is_ok(entry)
    return ok, entry


def save(entry: EntryCreation) -> InsertOneResult:
    res = image_repository.save(entry)
    image = res.get("secure_url")
    return mongo.db.entries.insert_one(entry.dict() | {"image": image})


def delete(id: str) -> DeleteResult:
    return mongo.db.entries.delete_one(
        filter={
            "_id": ObjectId(id),
        },
    )


def update(id: str, entry: EntryUpdate) -> UpdateResult:
    return mongo.db.entries.update_one(
        filter=dict(_id=ObjectId(id)), update={"$set": entry.dict()}
    )


def is_ok(entry) -> bool:
    return entry is not None
