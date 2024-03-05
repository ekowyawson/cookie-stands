"""
WSGI config for cookie_stands_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cookie_stands_project.settings')

application = get_wsgi_application()

# Add an alias for Vercel deployment compatibility
app = application
# Automatically create an admin user
# call_command('createadmin')