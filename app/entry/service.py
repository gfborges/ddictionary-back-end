from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.entry.repositories import entry_repository


class EntryService:
    @staticmethod
    def get_all(domain: str) -> list[Entry]:
        ok, entries = entry_repository.get_all(domain)
        return entries

    @staticmethod
    def get_one(domain: str, group: str, title: str) -> Entry:
        ok, entry = entry_repository.get_one(
            domain=domain, group=group, title=title
        )
        return entry

    @staticmethod
    def get(id: str) -> Entry:
        ok, entry = entry_repository.get(id=id)
        return entry

    @staticmethod
    def save(entry: EntryCreation) -> Entry:
        result = entry_repository.save(entry)
        return result.inserted_id

    @staticmethod
    def delete(id: str):
        entry_repository.delete(id=id)

    @staticmethod
    def update(id: str, entry: EntryUpdate):
        entry_repository.update(id, entry)
