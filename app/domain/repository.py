from pymongo.results import InsertOneResult
from app.domain.models import DomainCreation
from app.database.mongo import get_db

mongo = get_db()


def find_one(domain_slug: str) -> dict:
    return mongo.db.domains.find_one({"slug": domain_slug})


def save(domain: dict) -> InsertOneResult:
    return mongo.db.domains.insert_one(domain)


def update(domain_slug: str, new_group: str):
    filters = {"slug": domain_slug}
    update = {"$push": {"groups": new_group}}
    return mongo.db.domains.update_one(filters, update)
