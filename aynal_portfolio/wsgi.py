"""
WSGI config for aynal_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aynal_portfolio.settings.production")

application = get_wsgi_application()
