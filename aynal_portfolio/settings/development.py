from .base import *


DEBUG = True

SECRET_KEY = "django-insecure-local-development-only"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# ============================================================
# DATABASE
# ============================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ============================================================
# DEVELOPMENT SECURITY
# ============================================================

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]