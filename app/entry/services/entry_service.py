from werkzeug.exceptions import BadRequest, Forbidden
from app.domain.domain import Domain
from flask_jwt_extended.utils import get_current_user
from app.entry.repositories import image_repository
from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.entry.repositories import entry_repository


def get_all(domain: str) -> list[Entry]:
    return entry_repository.get_all(domain)


def get_one(domain: str, group: str, title: str) -> Entry:
    return entry_repository.get_one(domain=domain, group=group, title=title)


def get(id: str) -> Entry:
    return entry_repository.get(id=id)


def save(domain: Domain, entry_dto: EntryCreation) -> Entry:
    __validate_entry(domain, entry_dto)
    image = __save_entry_image(entry_dto)
    entry_args = entry_dto.dict() | {"image": image}
    entry = Entry(**entry_args)
    result = entry_repository.save(entry)
    return result.inserted_id


def __validate_entry(domain: Domain, entry_dto: EntryCreation) -> None:
    if domain.slug != entry_dto.domain:
        raise Forbidden(
            "Invalid domain, you don't have permission to create entry"
        )
    entry = entry_repository.get_one(
        domain=entry_dto.domain, group=entry_dto.group, title=entry_dto.title
    )
    if entry:
        raise BadRequest("Repeated entry")


def __save_entry_image(entry_dto: EntryCreation):
    res = image_repository.save(entry_dto)
    return res.get("secure_url")


def delete(id: str):
    domain = get_current_user()
    return entry_repository.delete(domain=domain.slug, id=id)


def update(id: str, entry: EntryUpdate):
    return entry_repository.update(id, entry)
