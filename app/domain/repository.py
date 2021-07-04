from app.domain.domain import Domain
from app.database.mongo import get_db

mongo = get_db()


class DomainReposiotry:
    @staticmethod
    def find_one(domain_name: str) -> Domain:
        domain = mongo.db.domains.find_one({"name": domain_name})
        return Domain(**domain)
