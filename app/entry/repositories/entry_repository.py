from dataclasses import asdict
from bson.objectid import ObjectId
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from werkzeug.exceptions import NotFound
from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.database.mongo import get_db
from app.entry.repositories import image_repository

mongo = get_db()


def get_all(domain: str) -> list[Entry]:
    cursor = mongo.db.entries.find(filter={"domain": domain})
    return [Entry(**doc) for doc in cursor]


def get_one(domain: str, group: str, title: str) -> Entry:
    doc = mongo.db.entries.find_one(
        filter={
            "domain": domain,
            "group": group,
            "title": title,
        }
    )
    if is_ok(doc):
        return Entry(**doc)
    raise NotFound("Entry Not Found")


def get(id: str) -> tuple[bool, dict]:
    doc = mongo.db.entries.find_one(
        filter={
            "_id": ObjectId(id),
        }
    )
    if is_ok(doc):
        return Entry(**doc)
    raise NotFound("Entry Not Found")


def save(entry: EntryCreation) -> InsertOneResult:
    res = image_repository.save(entry)
    image = res.get("secure_url")
    return mongo.db.entries.insert_one(entry.dict() | {"image": image})


def delete(domain: str, id: str) -> DeleteResult:
    return mongo.db.entries.delete_one(
        filter={
            "domain": domain,
            "_id": ObjectId(id),
        },
    )


def update(id: str, entry: EntryUpdate) -> UpdateResult:
    filters = {"_id": ObjectId(id), "domain": entry.domain}
    return mongo.db.entries.update_one(
        filter=filters, update={"$set": safe_asdict(entry)}
    )


def safe_asdict(obj: dict):
    dic = obj.dict()
    keys = [key for key, value in dic.items() if value is None]
    for key in keys:
        del dic[key]
    return dic


def is_ok(entry) -> bool:
    return entry is not None
