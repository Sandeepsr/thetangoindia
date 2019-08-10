#!/usr/bin/env python
import os
import sys
from config_settings import logger, SITE_PKG_PATH
sys.path.append(SITE_PKG_PATH)


if __name__ == "__main__":
    # CHANGED manage.py will use development settings by
    # default. Change the DJANGO_SETTINGS_MODULE environment variable
    # for using the environment specific settings file.
    logger.info("Executiong the command line: execute_from_command_line")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "tango.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
