from app.entry.models import EntryCreation
from app.database.cloudinarycfg import get_cloudinary_uploader

cloudinary = get_cloudinary_uploader()


def save(entry: EntryCreation):
    public_id = f"{entry.domain}/{entry.group}/{entry.title}"
    return cloudinary.upload(entry.image, public_id=public_id)
