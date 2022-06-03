"""
WSGI config for kiwipiano project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

from kiwipiano import MyWSGIApp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiwipiano.settings')

application = get_wsgi_application()

application = MyWSGIApp()
application = WhiteNoise(application, root="/path/static/css")
application.add_files("/path/static/JS", prefix="JS/")

