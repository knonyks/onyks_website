"""
Django settings for Onyx project.
"""

from pathlib import Path
import os

# --- Ścieżki ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Bezpieczeństwo / tryb pracy ---
# Na produkcji ustaw te wartości przez zmienne środowiskowe!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-j3+i3m6^o+wgd68!q)3#kpbou_)*46(#loc&!&f4)nu*i(^b)7",  # DEV fallback
)
DEBUG = os.getenv("DJANGO_DEBUG", "1") == "1"

ALLOWED_HOSTS = [
    "www.onyks.elka.pw.edu.pl",
    "onyks.elka.pw.edu.pl",
    "127.0.0.1",
    "localhost",
]

# Jeśli panel/formy będą działały pod HTTPS na domenie publicznej:
CSRF_TRUSTED_ORIGINS = [
    "https://onyks.elka.pw.edu.pl",
    "https://www.onyks.elka.pw.edu.pl",
]

# --- Aplikacje ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "website",
    # "django_cleanup.apps.CleanupConfig",  # (opcjonalnie) auto-usuwanie starych plików
]

# --- Middleware ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Onyx.urls"

# --- Szablony ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # np. [BASE_DIR / "templates"]
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Onyx.wsgi.application"

# --- Baza danych (DEV: SQLite) ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- Walidacja haseł ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- i18n / czas ---
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Warsaw"
USE_I18N = True
USE_TZ = True

# --- Statyczne ---
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "website" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# --- Media (uploady użytkownika) ---
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# (Opcjonalnie) jeżeli na C:\ brakuje miejsca na uploady w trakcie parsowania requestu:
# Ustaw katalog tymczasowy uploadu na inny dysk i zmniejsz bufor w pamięci.
FILE_UPLOAD_TEMP_DIR = os.getenv("DJANGO_FILE_UPLOAD_TEMP_DIR", None)
# np. w .env: DJANGO_FILE_UPLOAD_TEMP_DIR=E:\django_temp_uploads  (katalog musi istnieć)
# --- Klucze domyślne ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
