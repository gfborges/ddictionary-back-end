from datetime import datetime
import pytz
from bson.objectid import ObjectId

entries = dict(
    name="entries",
    data=(
        {
            "_id": ObjectId("60c809cbec2fc163dbda3666"),
            "title": "cat",
            "group": "feline",
            "domain": "pets",
            "definitions": ["crazy animal", "cute pet"],
            "translations": ["gato", "catze"],
            "created_at": datetime(1970, 1, 1, tzinfo=pytz.UTC),
        },
        {
            "_id": ObjectId("af24d828d3622d8660c80a01"),
            "title": "cockatoo",
            "group": "bird",
            "domain": "pets",
            "definitions": ["weird pet", "smart animal"],
            "translations": ["cacatua"],
            "created_at": datetime(1970, 1, 1, 12, 30, 59, tzinfo=pytz.UTC),
        },
        {
            "_id": ObjectId("80a16c08752a59e40696660c"),
            "title": "experience",
            "group": "entity",
            "domain": "cx",
            "definitions": [
                "event of contact between company and customer",
                "how the product is presented and delivered to the customer",
            ],
            "translations": ["experiencia"],
            "created_at": datetime(1970, 1, 1, 12, 30, 59, tzinfo=pytz.UTC),
        },
    ),
)

domains = dict(
    name="domains",
    data=(
        {
            "_id": ObjectId("c23f57d571bc787f7a7a87a0"),
            "name": "Pets",
            "slug": "pets",
            "password": "$2b$12$Gu3z4BSMKaSlMwiY9MeKDeakBVQ/fuPeehKGSd3eaqGOm3jxHfupC",
            "groups": ["feline", "bird"],
        },
        {
            "_id": ObjectId("07e9fc07b80fe2a92d4ae063"),
            "name": "Customer XP",
            "slug": "cx",
            "groups": [],
            "password": "$2b$12$tGss/ltJgIUcM3BHUbDjd.y2OhkI5ZI5.QGtC0uzhDZU4WK7iUrE2",
        },
    ),
)


class DataLoader:
    collections = [entries, domains]

    @classmethod
    def load(self, mongo):
        for collection in self.collections:
            mongo.db[collection.get("name")].insert_many(
                collection.get("data")
            )
