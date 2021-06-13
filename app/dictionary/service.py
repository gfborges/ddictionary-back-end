import app.dictionary.repository as repository


def get_all(domain: str):
    return repository.get_all(domain)


def get_one(domain: str, group: str, title: str):
    return repository.get_one(domain=domain, group=group, title=title)
