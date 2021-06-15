from app.entry.entry import Entry
from app.entry.models import EntryCreation
from app.entry.repository import EntryReposiory


def get_all(domain: str) -> list[dict]:
    return EntryReposiory.get_all(domain)


def get_one(domain: str, group: str, title: str) -> dict:
    return EntryReposiory.get_one(domain=domain, group=group, title=title)


def get(id: str) -> dict:
    return EntryReposiory.get(id=id)


def save(entry: EntryCreation) -> Entry:
    result = EntryReposiory.save(entry)
    return result.inserted_id


def delete(domain: str, group: str, title: str) -> dict:
    return EntryReposiory.delete(domain=domain, group=group, title=title)
