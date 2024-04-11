from .base import *
from datetime import timedelta

DEBUG = False
SECRET_KEY = os.getenv("SECURED_KEY")

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    "https://admin.otreze.com",
    "https://www.admin.otreze.com"]

CORS_ALLOWED_ORIGINS = [
    "admin.otreze.com",
    "www.admin.otreze.com",
    "https://admin.otreze.com",
    "https://www.admin.otreze.com",
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=6),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=6),
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE_PROD"),
        'NAME': os.getenv("DB_NAME_PROD"),
        'USER': os.getenv("DB_USER_PROD"),
        'PASSWORD': os.getenv("DB_PASSWORD_PROD"),
        'HOST': os.getenv("DB_HOST_PROD"),
        'PORT': os.getenv("DB_PORT_PROD"),
    }
}

EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")