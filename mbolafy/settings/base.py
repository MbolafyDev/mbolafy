import os
from . import base_dir_env

# BASE_DIR chargé après dotenv
BASE_DIR = base_dir_env.BASE_DIR

# ---------------------------
#     Sécurité de base
# ---------------------------
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'unsafe-secret-key-for-dev'
)

# ---------------------------
#     Applications
# ---------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tes apps
    'portfolio',
    'accueil',
    'parcour',
    'experience',
    'competence',
    'projet',
    'contact',
]

# ---------------------------
#     Middleware
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mbolafy.urls'

# ---------------------------
#     Templates
# ---------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mbolafy.wsgi.application'

# ---------------------------
#     Password validators
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------
#     Langue / Temps
# ---------------------------
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True
USE_TZ = True

# ---------------------------
#     Static / Media
# ---------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------
#     Autres
# ---------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
