from app.database.mongo import get_db
from app.logs.logs import Logger

mongo = get_db()


def find_one(domain_slug: str, log_cat: str):
    doc = mongo.db.logs.find_one({"domain": domain_slug, "cat": log_cat})
    return Logger(**doc) if doc else None


def save(logger: Logger):
    return mongo.db.logs.replace_one(
        {"domain": logger.domain, "cat": logger.cat},
        vars(logger),
        upsert=True,
    )
