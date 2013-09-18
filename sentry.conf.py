import os.path

from sentry.conf.server import *

CONF_ROOT = os.environ['OPENSHIFT_REPO_DIR']

# append project security libraries to Python path
sys.path.append(os.path.join(CONF_ROOT, 'libs', 'openshift'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['OPENSHIFT_APP_NAME']
    }
}

DATABASES['default'].update({
    'NAME': os.environ['OPENSHIFT_APP_NAME'],
    'USER': os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
    'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
    'HOST': os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
    'PORT': os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
})

#replace yours
import openshiftlibs

default_keys = {
    'SECRET_KEY': 'p*cch+!dmo_%visd87=$4%qoidi(-wmv^^c9vmvdyx(#eoehq+'
}
use_keys = openshiftlibs.openshift_secure(default_keys)
SENTRY_KEY = use_keys['SECRET_KEY']

SENTRY_PUBLIC = False

SENTRY_URL_PREFIX = 'https://' + os.environ['OPENSHIFT_GEAR_DNS']
#bypass sentry proxy settings, todo: implement middleware like https://docs.djangoproject.com/en/1.4/ref/request-response/#django.http.HttpRequest.get_host
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(CONF_ROOT, 'wsgi', 'static')
STATIC_URL = '/static/'

SENTRY_WEB_HOST = os.environ['OPENSHIFT_PYTHON_IP']
SENTRY_WEB_PORT = os.environ['OPENSHIFT_PYTHON_PORT']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''
