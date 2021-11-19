from app.group import repository as group_repository
from werkzeug.exceptions import BadRequest

from app.domain.domain import Domain
from app.group.group import Group
from app.group.models import GroupCreation, GroupUpdate


def find_one(domain_slug: str, group_slug: str):
    return group_repository.find_one(domain_slug, group_slug)


def save(domain: Domain, group_dto: GroupCreation):
    _validate(group_dto)
    group = Group(domain=domain.slug, **group_dto.dict())
    result = group_repository.save(group)
    return result.inserted_id


def _validate(group_dto):
    if find_one(group_dto.slug):
        raise BadRequest("Group already exists")
    return


def update(domain: Domain, group_dto: GroupUpdate):
    result = group_repository.update(domain, group_dto)
    return True
