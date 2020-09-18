from .shared import *
import os
import django_heroku
import dj_database_url


# Activate Django-Heroku
django_heroku.settings(locals())

# Heroku config variables
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = ['*']
DJANGO_ALLOWED_HOSTS = ['*']

# Use PostgreSQL
DATABASES = {
    'default': dj_database_url.config()
    }

# Workaround the PostgreSQL mandate for SSL
options = DATABASES['default'].get('OPTIONS', ())
options.pop('sslmode', None)

# Whitenoise
WHITENOISE = os.environ['WHITENOISE']

# Celery
CELERY_BROKER_URL = 'amqp://localhost:5672'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# CORS
CORS_ORIGIN_ALLOW_ALL = os.environ['CORS_ORIGIN_ALLOW_ALL']

