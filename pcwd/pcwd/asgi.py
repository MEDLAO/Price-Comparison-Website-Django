"""
ASGI config for pcwd project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# set DJANGO_SETTINGS_MODULE based on the environment
if os.getenv('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcwd.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcwd.settings.development')

application = get_asgi_application()
