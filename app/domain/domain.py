from app.domain.models import DomainCreation
import bcrypt


def __hash_password(domain: DomainCreation):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(domain.password.encode(), salt).decode()


def new_domain(domain_data: DomainCreation):
    return domain_data.dict() | {
        "password": __hash_password(domain_data),
        "groups": [],
    }


def domain_to_json(domain: dict):
    json = dict(domain)
    json["_id"] = str(json.get("_id"))
    del json["password"]
    return json
