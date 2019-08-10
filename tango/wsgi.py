"""
WSGI config for tango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

from django.conf import settings
from django.core.wsgi import get_wsgi_application
import os
import sys
from config import PROJECT_DIR, PROJECT_BASE_DIR, SITE_PKG_PATH, logger
sys.path.append(SITE_PKG_PATH)
sys.path.append(PROJECT_DIR)
sys.path.append(os.path.join(PROJECT_BASE_DIR, 't/tango/src/tango/settings/'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "production")

application = get_wsgi_application()

# Wrap werkzeug debugger if DEBUG is on
if settings.DEBUG:
    try:
        import django.views.debug
        import six
        from werkzeug.debug import DebuggedApplication

        def null_technical_500_response(request, exc_type, exc_value, tb):
            six.reraise(exc_type, exc_value, tb)

        django.views.debug.technical_500_response = null_technical_500_response
        application = DebuggedApplication(application, evalex=True)
    except ImportError:
        logger.exception("Exception while running on DEBUG mode.")
