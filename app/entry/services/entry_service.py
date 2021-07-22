from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.entry.repositories import entry_repository


def get_all(domain: str) -> list[Entry]:
    ok, entries = entry_repository.get_all(domain)
    return entries


def get_one(domain: str, group: str, title: str) -> Entry:
    ok, entry = entry_repository.get_one(
        domain=domain, group=group, title=title
    )
    return entry


def get(id: str) -> Entry:
    ok, entry = entry_repository.get(id=id)
    return entry


def save(entry: EntryCreation) -> Entry:
    result = entry_repository.save(entry)
    return result.inserted_id


def delete(domain: str, id: str):
    return entry_repository.delete(domain=domain, id=id)


def update(id: str, entry: EntryUpdate):
    return entry_repository.update(id, entry)
