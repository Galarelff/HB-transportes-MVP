
#!/usr/bin/env python
"""Utilitario de linha de comando do projeto HB Transportes."""

import os
import sys


def main():
    """Executa comandos administrativos do Django."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings"
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django nao encontrado. Instale as dependencias "
            "do arquivo requirements.txt."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

