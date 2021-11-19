from warnings import filters
from app.domain.domain import Domain
from app.group.group import Group
from app.group.models import GroupUpdate
from app.database.mongo import get_db

mongo = get_db()


def find_one(domain_slug: str, group_slug: str):
    filter = {"domain": domain_slug, "slug": group_slug}
    doc = mongo.db.groups.find_one(filter)
    return Group(**doc) if doc else None


def save(domain: Domain, group: Group):
    return mongo.db.groups.insert_one(vars(group))


def update(domain: Domain, group: GroupUpdate):
    filter = {"domain": domain.slug, "slug": group.slug}
    return mongo.db.groups.update_one(filter, {"$set": group.dict()})
