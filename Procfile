web: gunicorn main.wsgi --log-file -
celery: celery worker -A main -l info -c 4