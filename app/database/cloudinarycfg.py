import cloudinary
import cloudinary.uploader
from app.config import Cloudinary
from flask import Flask

cloudinary_uploader = cloudinary.uploader


def config_cloudinary(app: Flask):
    cloudinary.config(
        cloud_name=Cloudinary.NAME,
        api_secret=Cloudinary.SECRET,
        api_key=Cloudinary.API_KEY,
        secure=True,
    )


def get_cloudinary_uploader():
    return cloudinary_uploader
