from bson.objectid import ObjectId
import cloudinary
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from app.entry.entry import Entry
from app.entry.models import EntryCreation, EntryUpdate
from app.database.mongo import get_db
from app.database.cloudinarycfg import get_cloudinary_uploader

mongo = get_db()


cloudinary_uploader = get_cloudinary_uploader()


class EntryReposiory:
    @staticmethod
    def get_all(domain: str) -> list[Entry]:
        cursor = mongo.db.entries.find(filter={"domain": domain})
        return [Entry.new_entry(entry) for entry in cursor]

    @staticmethod
    def get_one(domain: str, group: str, title: str) -> Entry:
        entry = mongo.db.entries.find_one(
            filter={
                "domain": domain,
                "group": group,
                "title": title,
            }
        )
        return Entry.new_entry(entry)

    @staticmethod
    def get(id: str) -> Entry:
        entry = mongo.db.entries.find_one(
            filter={
                "_id": ObjectId(id),
            }
        )
        return Entry.new_entry(entry)

    @staticmethod
    def save(entry: EntryCreation) -> InsertOneResult:
        res = ImageRepository.save(entry)
        image = res.get("secure_url")
        return mongo.db.entries.insert_one(entry.dict() | {"image": image})

    @staticmethod
    def delete(id: str) -> DeleteResult:
        return mongo.db.entries.delete_one(
            filter={
                "_id": ObjectId(id),
            },
        )

    @staticmethod
    def update(id: str, entry: EntryUpdate) -> UpdateResult:
        return mongo.db.entries.update_one(
            filter=dict(_id=ObjectId(id)), update={"$set": entry.dict()}
        )


class ImageRepository:
    @staticmethod
    def save(entry: EntryCreation):
        public_id = f"{entry.domain}/{entry.group}/{entry.title}"
        return cloudinary_uploader.upload(entry.image, public_id=public_id)
