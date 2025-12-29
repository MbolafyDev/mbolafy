# mbolafy/mbolafy/settings/__init__.py
import os

# Si DJANGO_SETTINGS_MODULE n'est PAS défini,
# on force automatiquement la production
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'mbolafy.settings.prod'
    )
