from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Forcer DJANGO_SETTINGS_MODULE par défaut
settings_module = os.getenv(
    'DJANGO_SETTINGS_MODULE',
    'mbolafy.settings.prod'
)

env_suffix = settings_module.split('.')[-1]

ENV_FILE = BASE_DIR / f'.env.{env_suffix}'

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
else:
    raise FileNotFoundError(f"❌ Fichier {ENV_FILE} introuvable")
