from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.entry import repository as EntryReposiory


class EntryService:
    @staticmethod
    def get_all(domain: str) -> list[Entry]:
        ok, entries = EntryReposiory.get_all(domain)
        return entries

    @staticmethod
    def get_one(domain: str, group: str, title: str) -> Entry:
        ok, entry = EntryReposiory.get_one(
            domain=domain, group=group, title=title
        )
        return entry

    @staticmethod
    def get(id: str) -> Entry:
        ok, entry = EntryReposiory.get(id=id)
        return entry

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
