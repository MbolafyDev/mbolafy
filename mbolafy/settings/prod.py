import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    "mbolafly.pythonanywhere.com,www.mbolafly.pythonanywhere.com"
).split(',')


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
