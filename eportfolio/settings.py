"""
Django settings for the eportfolio project.

The site is developed with Django (``python manage.py runserver``) and
published as static HTML on GitHub Pages (``python manage.py build``).
No database is needed: all content lives in ``main/content.py``.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# The key is only used for local development; nothing secret is signed,
# because the published site is plain static HTML.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-only-insecure-key-change-me")

DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "eportfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "eportfolio.wsgi.application"

DATABASES = {}

LANGUAGE_CODE = "en"
TIME_ZONE = "Europe/Madrid"
USE_I18N = False
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Public URL of the deployed site (used for canonical links and the sitemap).
SITE_URL = os.environ.get("SITE_URL", "https://jossseluuu.github.io/eportfolio")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
