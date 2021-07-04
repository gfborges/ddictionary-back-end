import cloudinary
import cloudinary.uploader
from app.config import Cloudinary


def config_cloudinary():
    cloudinary.config(
        cloud_name=Cloudinary.NAME,
        api_secret=Cloudinary.SECRET,
        api_key=Cloudinary.API_KEY,
        secure=True,
    )


def get_cloudinary_uploader():
    return cloudinary_uploader


cloudinary_uploader = cloudinary.uploader
