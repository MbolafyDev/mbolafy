# mbolafy/mbolafy/settings/base_dir_env.py

from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Exemple:
# mbolafy.settings.dev  -> .env.dev
# mbolafy.settings.prod -> .env.prod
settings_module = os.getenv('DJANGO_SETTINGS_MODULE', 'mbolafy.settings.dev')
env_suffix = settings_module.split('.')[-1]

ENV_FILE = BASE_DIR / f'.env.{env_suffix}'

load_dotenv(ENV_FILE)
