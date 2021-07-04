from app.domain.models import DomainCreation
from app.domain.domain import Domain
from app.domain.repository import DomainReposiotry


class DomainService:
    @staticmethod
    def find_one(domain_name: str) -> Domain:
        return DomainReposiotry.find_one(domain_name)

    @staticmethod
    def save(domain: DomainCreation):
        domain = Domain.new_domain(domain)
        result = DomainReposiotry.save(domain)
        return str(result.inserted_id)
