from pathlib import Path
import os
from dotenv import load_dotenv

# Racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Déterminer le settings actif
settings_module = os.getenv(
    "DJANGO_SETTINGS_MODULE",
    "mbolafy.settings.prod"
)

env_suffix = settings_module.split(".")[-1]

# Fichier .env correspondant
ENV_FILE = BASE_DIR / f".env.{env_suffix}"

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
else:
    raise RuntimeError(f"❌ Fichier {ENV_FILE} introuvable")
