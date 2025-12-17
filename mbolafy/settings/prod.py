import os
from .base import *

DEBUG = False

# ALLOWED_HOSTS corrigé pour PythonAnywhere
ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    "mbolafly.pythonanywhere.com,www.mbolafly.pythonanywhere.com"
).split(',') + [".pythonanywhere.com", "localhost", "127.0.0.1"]

# Si tu es derrière le proxy HTTPS de PythonAnywhere
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# Base de données MySQL
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
