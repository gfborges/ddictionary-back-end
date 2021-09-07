from app.domain.models import DomainCreation
from app.domain.models import DomainCreation
from app.domain.domain import Domain
import app.domain.repository as domain_reposiotry


def find_one(domain_slug: str) -> Domain:
    return domain_reposiotry.find_one(domain_slug)


def save(domain_dto: DomainCreation) -> str:
    domain = Domain.create(domain_dto)
    result = domain_reposiotry.save(domain)
    return str(result.inserted_id)


def update(domain_slug: str, new_group: str):
    result = domain_reposiotry.update(domain_slug, new_group)
    return True
