"""Settings for Development Server"""
from ctrlacad.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

VAR_ROOT = '/var/www/ctrlacad'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ctrlacad',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

# WSGI_APPLICATION = 'ctrlacad.wsgi.dev.application'
