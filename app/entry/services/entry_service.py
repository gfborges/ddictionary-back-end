from werkzeug.exceptions import BadRequest, Forbidden
from app.domain.domain import Domain
from app.logs import service as log_service
from app.entry.repositories import image_repository
from app.entry.entry import Entry
from app.entry.models import (
    EntryCreation,
    EntryQuery,
    EntrySearch,
    EntryUpdate,
)
from app.entry.repositories import entry_repository


def find_many(domain: str) -> list[Entry]:
    return entry_repository.find_many(domain)


def find_one(query: EntryQuery) -> Entry:
    entry = entry_repository.find_one(
        domain=query.domain,
        group=query.group,
        title=query.title,
    )
    if entry and query.log:
        log_service.log(query.domain, "entry_view", query.title)
    return entry


def find_by_id(domain: Domain, id: str) -> Entry:
    return entry_repository.find_by_id(domain=domain, id=id)


def save(domain: Domain, entry_dto: EntryCreation) -> Entry:
    __validate_entry(domain, entry_dto)
    entry = entry_dto.dict()
    if entry_dto.image:
        image = __save_entry_image(entry_dto)
        entry["image"] = image
    entry = Entry(**entry)
    result = entry_repository.save(entry)
    print("print", result)
    return result["_id"]


def search(query: EntrySearch):
    if query.log:
        log_service.log(query.domain, "search", query.text)
    return entry_repository.search(query)


def delete(domain: Domain, id: str):
    deleted = entry_repository.delete(domain=domain.slug, id=id)
    return deleted.get("result", None)


def update(domain: Domain, id: str, entry: EntryUpdate):
    updated = entry_repository.update(domain, id, entry)
    return updated.get("result", None)


def __validate_entry(domain: Domain, entry_dto: EntryCreation) -> None:
    if domain.slug != entry_dto.domain:
        raise Forbidden(
            "Invalid domain, you don't have permission to create entry"
        )
    entry = entry_repository.find_one(
        domain=entry_dto.domain, group=entry_dto.group, title=entry_dto.title
    )
    if entry:
        raise BadRequest("Repeated entry")


def __save_entry_image(entry_dto: EntryCreation):
    res = image_repository.save(entry_dto)
    return res.get("secure_url")
