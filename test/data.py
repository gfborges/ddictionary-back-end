from datetime import datetime
import pytz
from bson.objectid import ObjectId

entries = dict(
    name="entries",
    data=[
        {
            "_id": ObjectId("60c809cbec2fc163dbda3666"),
            "title": "cat",
            "group": "feline",
            "domain": "pets",
            "definitions": ["crazy animal", "cute pet"],
            "translations": ["gato", "catze"],
            "createdAt": datetime(1970, 1, 1, tzinfo=pytz.UTC),
        },
        {
            "_id": ObjectId("af24d828d3622d8660c80a01"),
            "title": "cockatoo",
            "group": "bird",
            "domain": "pets",
            "definitions": ["weird pet", "smart animal"],
            "translations": ["cacatua"],
            "createdAt": datetime(1970, 1, 1, 12, 30, 59, tzinfo=pytz.UTC),
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
            "createdAt": datetime(1970, 1, 1, 12, 30, 59, tzinfo=pytz.UTC),
        },
    ],
)


class DataLoader:
    collections = [entries]

    @classmethod
    def load(self, mongo):
        for collection in self.collections:
            mongo.db[collection["name"]].insert_many(collection["data"])
