from app.entry.models import EntryCreation
from app.database.mongo import get_db


class EntryReposiory:
    mongo = get_db()

    @classmethod
    def get_all(self, domain: str) -> list[dict]:
        print("get_all", id(self.mongo), self.mongo.is_test())
        cursor = self.mongo.db.entries.find(
            filter={"domain": domain},
            projection={"_id": False},
        )
        return list(cursor)

    @classmethod
    def get_one(self, domain: str, group: str, title: str) -> list[dict]:
        return self.mongo.db.entries.find_one(
            filter={
                "domain": domain,
                "group": group,
                "title": title,
            },
            projection={"_id": False},
        )

    @classmethod
    def save(self, entry: EntryCreation) -> None:
        print("get_all", id(self.mongo), self.mongo.is_test())
        return self.mongo.db.entries.insert_one(entry)

    @classmethod
    def delete(self, domain: str, group: str, title: str) -> list[dict]:
        return self.mongo.db.entries.delete_one(
            filter={
                "domain": domain,
                "group": group,
                "title": title,
            },
        )
