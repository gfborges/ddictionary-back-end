from app.domain.models import DomainCreation
from app.domain.models import DomainCreation
from app.domain.domain import Domain
import app.domain.repository as DomainReposiotry


def find_one(domain_name: str):
    return DomainReposiotry.find_one(domain_name)


def save(domain: DomainCreation):
    domain = Domain.new_domain(domain)
    result = DomainReposiotry.save(domain)
    return str(result.inserted_id)
