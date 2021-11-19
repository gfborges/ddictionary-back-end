from app.domain.models import DomainCreation
from bson.objectid import ObjectId
from dataclasses import asdict, dataclass, field
import bcrypt


@dataclass()
class Domain:
    name: str
    password: str
    slug: str
    description: str = ""
    groups: list[str] = field(default_factory=list)
    _id: ObjectId = field(default_factory=ObjectId)

    @staticmethod
    def create(domain_dto: DomainCreation):
        domain_kwargs = domain_dto.dict() | {
            "password": Domain.__hash_password(domain_dto),
        }
        return Domain(**domain_kwargs)

    @staticmethod
    def __hash_password(domain_dto: DomainCreation):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(domain_dto.password.encode(), salt)
        return hashed_pw.decode()

    def to_json(self):
        d = asdict(self)
        del d["password"]
        d["_id"] = str(self._id)
        return d
