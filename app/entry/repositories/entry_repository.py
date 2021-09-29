from app.domain.domain import Domain
from dataclasses import asdict
from bson.objectid import ObjectId
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from app.entry.entry import Entry
from app.entry.models import EntryUpdate
from app.database.mongo import get_db
from app.database.escfg import get_es

mongo = get_db()
es = get_es()


def get_all(domain: str) -> list[Entry]:
    cursor = mongo.db.entries.find(filter={"domain": domain})
    es.search(
        index=domain, doc_type="entry", body={"query": {"match_all": {}}}
    )
    return [Entry(**doc) for doc in cursor]


def get_one(domain: str, group: str, title: str) -> Entry:
    doc = mongo.db.entries.find_one(
        filter={
            "domain": domain,
            "group": group,
            "title": title,
        }
    )
    es.search(
        index=domain,
        doc_type="entry",
        body={
            "doc": {
                "query": {
                    "bool": {
                        "must": [
                            {"match": {"group": group}},
                            {"match": {"title": title}},
                        ]
                    }
                }
            }
        },
    )
    if is_ok(doc):
        return Entry(**doc)
    return None


def get(domain: Domain, id: str) -> Entry:
    doc = mongo.db.entries.find_one(
        filter={
            "_id": ObjectId(id),
        }
    )
    es.get(index=domain.slug, doc_type="entry", id=id)
    if is_ok(doc):
        return Entry(**doc)
    raise None


def save(entry: Entry) -> InsertOneResult:
    print(es)
    es.create(index=entry.domain, doc=entry, doc_type="entry")
    return mongo.db.entries.insert_one(asdict(entry))


def delete(domain: str, id: str) -> DeleteResult:
    print(es())
    es.delete(index=domain, doc_type="entry", id=id)
    return mongo.db.entries.delete_one(
        filter={
            "domain": domain,
            "_id": ObjectId(id),
        },
    )


def update(id: str, entry: EntryUpdate) -> UpdateResult:
    filters = {"_id": ObjectId(id), "domain": entry.domain}
    es.update(
        index=entry["domain"],
        doc_type="entry",
        id=id,
        body={
            "doc": safe_asdict(entry),
        },
    )
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
