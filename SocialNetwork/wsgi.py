"""
WSGI config for SocialNetwork project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
#This is how our python web app and the web server comunicates
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialNetwork.settings')

application = get_wsgi_application()