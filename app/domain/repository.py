from pymongo.results import InsertOneResult
from app.domain.models import DomainCreation
from app.database.mongo import get_db

mongo = get_db()


def find_one(domain_slug: str) -> dict:
    return mongo.db.domains.find_one({"slug": domain_slug})


def save(domain: dict) -> InsertOneResult:
    return mongo.db.domains.insert_one(domain)
