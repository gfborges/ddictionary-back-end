from app.domain.models import DomainCreation
import bcrypt


class Domain:
    def __init__(self, **domain):
        self.name = domain.get("name")
        self.password = domain.get("password").encode()
        self.id = domain.get("_id")

    @staticmethod
    def new_domain(domain: DomainCreation):
        domain = domain.dict() | {"password": Domain.__hash_password(domain)}
        return Domain(**domain)

    @staticmethod
    def __hash_password(domain: DomainCreation):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(domain.password.encode(), salt).decode()

    def __dict__(self):
        return {
            "name": self.name,
            "id": str(self.id),
        }

    def dict(self):
        d = {
            "name": self.name,
            "password": self.password,
        }
        if self.id is not None:
            d | {"id": self.id}
        return d

    def to_json(self):
        return self.__dict__()
