"""
WSGI config for pcwd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# set DJANGO_SETTINGS_MODULE based on the environment
if os.getenv('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcwd.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcwd.settings.development')

application = get_wsgi_application()
