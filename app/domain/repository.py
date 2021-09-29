from app.database.escfg import get_es
from app.domain.domain import Domain
from pymongo.results import InsertOneResult
from app.database.mongo import get_db
from dataclasses import asdict

mongo = get_db()
es = get_es()


def find_one(domain_slug: str) -> dict:
    doc = mongo.db.domains.find_one({"slug": domain_slug})
    return Domain(**doc) if doc else None


def save(domain: Domain) -> InsertOneResult:
    insert_res = mongo.db.domains.insert_one(asdict(domain))
    es.indices.create(index=domain.slug)
    return insert_res


def update(domain_slug: str, new_group: str):
    filters = {"slug": domain_slug}
    update = {"$push": {"groups": new_group}}
    return mongo.db.domains.update_one(filters, update)
