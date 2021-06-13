from app.database.mongo import get_db


def get_all(domain: str):
    cursor = mongo.db.dictionaries.find(
        filter={"domain": domain},
        projection={"_id": False},
    )
    return list(cursor)


def get_one(domain: str, group: str, title: str):
    return mongo.db.dictionaries.find_one(
        filter={
            "domain": domain,
            "group": group,
            "title": title,
        },
        projection={"_id": False},
    )


mongo = get_db()
