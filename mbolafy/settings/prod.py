import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    "mbolafly.pythonanywhere.com,www.mbolafly.pythonanywhere.com"
).split(',') + ["127.0.0.1", "localhost"]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# Sécurité : vérifier le chargement des variables
if not os.getenv("DATABASE_NAME"):
    raise RuntimeError("❌ Variables MySQL non chargées (.env.prod)")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': '3306',
    }
}
