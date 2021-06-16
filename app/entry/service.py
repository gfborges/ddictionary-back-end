from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.entry.repository import EntryReposiory


class EntryService:
    @staticmethod
    def get_all(domain: str) -> list[dict]:
        return EntryReposiory.get_all(domain)

    @staticmethod
    def get_one(domain: str, group: str, title: str) -> dict:
        return EntryReposiory.get_one(domain=domain, group=group, title=title)

    @staticmethod
    def get(id: str) -> dict:
        return EntryReposiory.get(id=id)

    @staticmethod
    def save(entry: EntryCreation) -> Entry:
        result = EntryReposiory.save(entry)
        return result.inserted_id

    @staticmethod
    def delete(id: str) -> dict:
        return EntryReposiory.delete(id=id)

    @staticmethod
    def update(id: str, entry: EntryUpdate):
        return EntryReposiory.update(id, entry)
