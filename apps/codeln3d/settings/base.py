import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

#
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/staticfiles/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = (BASE_DIR / "static",)

##########
# database connection
DATABASES = {
    "sqlite3": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "codeln": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "argamato_semiose",
        "USER": "argamato",
        "PASSWORD": "bigbogus",
        "HOST": "localhost",
        "PORT": 5433,
        "DISABLE_SERVER_SIDE_CURSORS": True,
    },
    "test": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5433,  # default postgres port
    },
}
DATABASES["default"] = DATABASES["sqlite3"]

##########
# internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
