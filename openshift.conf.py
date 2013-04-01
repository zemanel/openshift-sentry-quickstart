"""
Openshift Sentry configuration.
"""

import os.path
from sentry.conf.server import *

CONF_ROOT = os.environ['OPENSHIFT_REPO_DIR']

# append project security libraries to Python path
sys.path.append(os.path.join(CONF_ROOT, 'libs', 'openshift'))

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : os.environ['OPENSHIFT_APP_NAME'],
        'USER'      : os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
        'PASSWORD'  : os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
        'HOST'      : os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
        'PORT'      : os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
        }
}

# enable database caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
        }
}

# disable task queue
SENTRY_USE_QUEUE = False

# Generate a unique secure secret key based on Openshift environment variables

import openshiftlibs
default_keys = { 'SECRET_KEY': 'UmJUz9Efz9U7Bz6E2VQIC0TJySNQw3RwOfcfypgiV48D' }
use_keys = openshiftlibs.openshift_secure(default_keys)
SENTRY_KEY = use_keys['SECRET_KEY']

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.

SENTRY_URL_PREFIX = 'https://' + os.environ['OPENSHIFT_GEAR_DNS']

SENTRY_WEB_HOST = os.environ['OPENSHIFT_INTERNAL_IP']
SENTRY_WEB_PORT = os.environ['OPENSHIFT_INTERNAL_PORT']
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# Should Sentry allow users to create new accounts?
SENTRY_ALLOW_REGISTRATION = False

# setup static files
STATIC_ROOT = os.path.join(CONF_ROOT, 'wsgi', 'static')
STATIC_URL = '/static/'

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''
