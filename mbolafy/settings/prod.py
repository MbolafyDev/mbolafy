# mbolafy/mbolafy/settings/prod.py

import os
from .base import *

# ---------------------------
# DEBUG
# ---------------------------
DEBUG = False

# ---------------------------
# ALLOWED HOSTS
# ---------------------------
ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    "mbolafly.pythonanywhere.com,www.mbolafly.com"
).split(',') + ["127.0.0.1", "localhost"]

# ---------------------------
# Proxy HTTPS
# ---------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# ---------------------------
# Vérification des variables critiques
# ---------------------------
required_vars = ["DATABASE_NAME", "DATABASE_USER", "DATABASE_PASSWORD", "DATABASE_HOST"]
missing_vars = [v for v in required_vars if not os.getenv(v)]
if missing_vars:
    raise RuntimeError(f"❌ Variables d'environnement manquantes : {', '.join(missing_vars)}")

# ---------------------------
# DATABASES MySQL
# ---------------------------
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT', '3306'),
    }
}
