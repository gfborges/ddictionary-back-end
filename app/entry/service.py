from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.entry.repository import EntryReposiory


class EntryService:
    @staticmethod
    def get_all(domain: str) -> list[Entry]:
        return EntryReposiory.get_all(domain)

    @staticmethod
    def get_one(domain: str, group: str, title: str) -> Entry:
        return EntryReposiory.get_one(domain=domain, group=group, title=title)

    @staticmethod
    def get(id: str) -> Entry:
        return EntryReposiory.get(id=id)

    @staticmethod
    def save(entry: EntryCreation) -> Entry:
        result = EntryReposiory.save(entry)
        return result.inserted_id

    @staticmethod
    def delete(id: str):
        EntryReposiory.delete(id=id)

    @staticmethod
    def update(id: str, entry: EntryUpdate):
        EntryReposiory.update(id, entry)
