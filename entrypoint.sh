#!/bin/sh

echo "${0}: running migrations."
python manage.py migrate

echo "${0}: creating admin user."

echo "from django.contrib.auth.models import User; print(\"Admin exists\") if User.objects.filter(username='seweryn').exists() else User.objects.create_superuser('admin', 'maciek@mjanuszewski.pl', 'admin1234')" | python manage.py shell

echo "${0}: collecting statics."
python manage.py collectstatic --noinput

echo "${0}: create initial data."
python manage.py create_initial_report

echo "${0}: running app."

gunicorn pdf_generator.wsgi:application \
	--name=root \
	--bind=0.0.0.0:8000 \
	--timeout=900 \
	--workers=3 \
	--threads=3 \
	--log-level=info \
	--reload

exec "$@"