from app.domain.domain import Domain
from dataclasses import asdict
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from app.entry.entry import Entry
from app.entry.models import EntrySearch, EntryUpdate
from app.database.mongo import get_db
from app.database.escfg import get_es

mongo = get_db()
es = get_es()


def find_many(domain: str) -> list[Entry]:
    docs = es.search(
        index=domain, doc_type="entry", body={"query": {"match_all": {}}}
    )
    return [Entry(**doc["_source"]) for doc in docs["hits"]["hits"]]


def find_one(domain: str, group: str, title: str) -> Entry:
    r = es.search(
        index=domain,
        doc_type="entry",
        body={
            "query": {
                "bool": {
                    "must": [
                        {"match": {"group": group}},
                        {"match": {"title": title}},
                    ]
                }
            }
        },
    )
    docs = r["hits"]["hits"]
    if not docs:
        return None
    return Entry(**docs[0]["_source"])


def find_by_id(domain: Domain, id: str) -> Entry:
    doc = es.get(index=domain.slug, doc_type="entry", id=id)
    if not ok(doc.get("_source")):
        return None
    return Entry(**doc["_source"])


def search(query: EntrySearch) -> list[Entry]:
    r = es.search(
        index=query.domain,
        doc_type="entry",
        body={
            "from": query.skip,
            "size": query.size,
            "query": {
                "simple_query_string": {
                    "query": query.text,
                },
            },
        },
    )
    docs = r["hits"]["hits"]
    return {
        "total": r["hits"]["total"]["value"],
        "data": [Entry(**doc["_source"]) for doc in docs],
    }


def save(entry: Entry) -> InsertOneResult:
    return es.index(
        index=entry.domain,
        id=entry.id,
        body=to_dict(entry),
        doc_type="entry",
    )


def delete(domain: str, id: str) -> DeleteResult:
    return es.delete(index=domain, doc_type="entry", id=id, ignore=[404])


def update(domain: Domain, id: str, entry: EntryUpdate) -> UpdateResult:
    return es.update(
        index=domain.slug,
        doc_type="entry",
        id=id,
        body={
            "doc": safe_asdict(entry),
        },
    )


def safe_asdict(obj: dict):
    dic = obj.dict()
    keys = [key for key, value in dic.items() if value is None]
    for key in keys:
        del dic[key]
    return dic


def ok(entry) -> bool:
    return entry is not None


def to_dict(obj):
    return {k: v for k, v in vars(obj).items() if v is not None}
