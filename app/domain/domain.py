from app.domain.models import DomainCreation
import bcrypt


def __hash_password(domain: DomainCreation):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(domain.password.encode(), salt).decode()


def new_domain(domain_data: DomainCreation):
    return domain_data.dict() | {"password": __hash_password(domain_data)}


def domain_to_json(domain: dict):
    return {
        "name": domain.get("name"),
        "slug": domain.get("slug"),
        "_id": str(domain.get("_id")),
    }
