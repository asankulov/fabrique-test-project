#!/usr/bin/env bash

PIPENV_DIR=$(pipenv --venv)
export PIPENV_DIR
# shellcheck disable=SC1090
source "${PIPENV_DIR}/bin/activate"
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi --ini uwsgi.ini --virtualenv "${PIPENV_DIR}" --logto /var/log/uwsgi/fabrique.log
