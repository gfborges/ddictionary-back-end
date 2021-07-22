from app.domain.models import DomainCreation
from app.domain.models import DomainCreation
from app.domain.domain import new_domain
import app.domain.repository as domain_reposiotry


def find_one(domain_slug: str):
    return domain_reposiotry.find_one(domain_slug)


def save(domain: DomainCreation):
    domain = new_domain(domain)
    result = domain_reposiotry.save(domain)
    return str(result.inserted_id)


def update(domain_slug: str, new_group: str):
    result = domain_reposiotry.update(domain_slug, new_group)
    print(result)
    return True
