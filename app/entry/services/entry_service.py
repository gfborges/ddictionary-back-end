from flask_jwt_extended.utils import get_current_user
from werkzeug.exceptions import Forbidden
from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.entry.repositories import entry_repository


def get_all(domain: str) -> list[Entry]:
    return entry_repository.get_all(domain)


def get_one(domain: str, group: str, title: str) -> Entry:
    return entry_repository.get_one(domain=domain, group=group, title=title)


def get(id: str) -> Entry:
    return entry_repository.get(id=id)


def save(entry: EntryCreation) -> Entry:
    result = entry_repository.save(entry)
    return result.inserted_id


def delete(id: str):
    domain = get_current_user()
    return entry_repository.delete(domain=domain.slug, id=id)


def update(id: str, entry: EntryUpdate):
    return entry_repository.update(id, entry)
