from .shared import *
import os
import django_heroku
import dj_database_url


# Activate Django-Heroku
django_heroku.settings(locals())

# Heroku config variables
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG'] == 'False'
ALLOWED_HOSTS = ['*']
DJANGO_ALLOWED_HOSTS = ['*']

# Use PostgreSQL
DATABASES = {
    'default': dj_database_url.config(),
    }

# Workaround the PostgreSQL mandate for SSL
# options = DATABASES['default'].get('OPTIONS', ())
# options.pop('sslmode', None)

# Whitenoise
WHITENOISE = os.environ['WHITENOISE'] == 'True'

# Celery
CELERY_BROKER_URL = 'amqp://localhost:5672'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# CORS
CORS_ORIGIN_ALLOW_ALL = os.environ['CORS_ORIGIN_ALLOW_ALL'] == 'True'
CORS_ALLOW_CREDENTIALs = os.environ['CORS_ALLOW_CREDENTIALS'] == 'False'


CELERY_BROKER_URL = os.environ.get('CLOUDAMQP_URL')
BROKER_POOl_LIMIT = 1

# Email (Contact Form) - allow less secure apps
# less secure app switch for gmail: myaccount.google.com/lesssecureapps
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS'] == 'True'
EMAIL_PORT = os.environ['EMAIL_PORT']