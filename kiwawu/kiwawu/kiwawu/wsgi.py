"""
WSGI config for kiwawu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE")

import sys
sys.stdout = sys.stderr

from django.core.wsgi import get_wsgi_application
os.environ["DJANGO_SETTINGS_MODULE"] = "kiwawu.settings"
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kiwawu.settings")


application = get_wsgi_application()
