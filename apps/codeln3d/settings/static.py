import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

USE_AWS_S3 = int(os.environ.get("USE_AWS_S3", default=0))
if USE_AWS_S3:
    # aws settings
    AWS_LOCATION = "static"
    AWS_ACCESS_KEY_ID = str(os.getenv("AWS_ACCESS_KEY_ID"))
    AWS_SECRET_ACCESS_KEY = str(os.getenv("AWS_SECRET_ACCESS_KEY"))
    AWS_STORAGE_BUCKET_NAME = str(os.getenv("AWS_STORAGE_BUCKET_NAME"))
    AWS_DEFAULT_ACL = None

    STATICFILES_DIRS = [BASE_DIR / "static"]
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    # s3 static settings
    STATIC_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = "codeln3d.storage_backends.StaticStorage"
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    FILEBROWSER_DIRECTORY = PUBLIC_MEDIA_LOCATION
    DIRECTORY = PUBLIC_MEDIA_LOCATION
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "codeln3d.storage_backends.PublicMediaStorage"
    # s3 private media settings
    PRIVATE_MEDIA_LOCATION = "private"
    PRIVATE_FILE_STORAGE = "codeln3d.storage_backends.PrivateMediaStorage"
else:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    # Static files (CSS, JavaScript, Images)
    STATIC_URL = "/staticfiles/"
    MEDIA_URL = "/media/"
    STATIC_ROOT = BASE_DIR / "staticfiles"
    MEDIA_ROOT = BASE_DIR / "media"
    STATICFILES_DIRS = (BASE_DIR / "static",)
