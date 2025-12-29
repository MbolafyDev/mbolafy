#!/usr/bin/env python
import os
import sys


def main():
    # ⚠️ OBLIGATOIRE : choisir un fichier settings réel
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'mbolafy.settings.prod'
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
