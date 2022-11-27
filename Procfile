release: sh -c 'python manage.py migrate'
web: python manage.py migrate && gunicorn PBPD04.wsgi