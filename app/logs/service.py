from app.logs import repository as logs_repository
from app.logs.logs import Logger


def find_one(domain_slug: str, log_cat: str) -> Logger:
    logger = logs_repository.find_one(domain_slug, log_cat)
    return logger if logger else Logger(domain=domain_slug, cat=log_cat)


def log(domain_slug: str, log_cat: str, msg: str):
    logger = find_one(domain_slug, log_cat)
    logger.log(msg)
    logs_repository.save(logger)
