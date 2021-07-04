from app.domain.models import DomainCreation
from app.domain.domain import Domain
from app.database.mongo import get_db

mongo = get_db()


class DomainReposiotry:
    @staticmethod
    def find_one(domain_name: str) -> Domain:
        if domain := mongo.db.domains.find_one({"name": domain_name}):
            return Domain(**domain)

    @staticmethod
    def save(domain: Domain):
        return mongo.db.domains.insert_one(domain.dict())
